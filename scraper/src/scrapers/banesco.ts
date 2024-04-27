import { Page } from "puppeteer";
import { BANK, ELEMENT_TYPE } from "src/enums";
import { BrowserScraper } from "src/scrapers/base";
import { validateAmount } from "src/utils/decorators";

export class BanescoScraper extends BrowserScraper {
  bank = BANK.BANESCO;
  url = "https://www.banesco.com.do/";

  currencyTogglerSelector = "div.calculator__currency-span-1";
  buySelector = "div.calculator__buy-inputs > div:nth-child(2) > input";
  sellSelector = "div.calculator__sell-inputs > div:nth-child(2) > input";

  @validateAmount
  async getEuroBuyRate(page: Page): Promise<number> {
    await this.clickCurrencySection(this.currencyTogglerSelector, page);

    return this.getSingleRate(this.buySelector, page, ELEMENT_TYPE.INPUT);
  }

  @validateAmount
  async getEuroSellRate(page: Page): Promise<number> {
    return this.getSingleRate(this.sellSelector, page, ELEMENT_TYPE.INPUT);
  }

  @validateAmount
  async getDollarBuyRate(page: Page): Promise<number> {
    await this.clickCurrencySection(this.currencyTogglerSelector, page);

    return this.getSingleRate(this.buySelector, page, ELEMENT_TYPE.INPUT);
  }

  @validateAmount
  async getDollarSellRate(page: Page): Promise<number> {
    return this.getSingleRate(this.sellSelector, page, ELEMENT_TYPE.INPUT);
  }
}
