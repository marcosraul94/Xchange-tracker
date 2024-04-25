import { Page } from "puppeteer";
import { BANK } from "src/enums";
import { BrowserScraper } from "src/scrapers/base";
import { validateAmount } from "src/utils/decorators";

export class BanescoScraper extends BrowserScraper {
  bank = BANK.BANESCO;
  url = "https://www.banesco.com.do/";

  currencyTogglerSelector = "div.calculator__currency-span-1";

  buySelector = "div.calculator__buy-inputs > div:nth-child(2) > input";
  sellSelector = "div.calculator__sell-inputs > div:nth-child(2) > input";

  async getSingleRateFromInput(selector: string, page: Page) {
    const element = await page.waitForSelector(selector);
    const value = await element?.evaluate((e) => (e as HTMLInputElement).value);
    if (!value) throw Error("Missing value");

    return parseFloat(value);
  }

  @validateAmount
  async getEuroBuyRate(page: Page): Promise<number> {
    await this.clickCurrencySection(this.currencyTogglerSelector, page);

    return this.getSingleRateFromInput(this.buySelector, page);
  }

  @validateAmount
  async getEuroSellRate(page: Page): Promise<number> {
    return this.getSingleRateFromInput(this.sellSelector, page);
  }

  @validateAmount
  async getDollarBuyRate(page: Page): Promise<number> {
    await this.clickCurrencySection(this.currencyTogglerSelector, page);

    return this.getSingleRateFromInput(this.buySelector, page);
  }

  @validateAmount
  async getDollarSellRate(page: Page): Promise<number> {
    return this.getSingleRateFromInput(this.sellSelector, page);
  }
}
