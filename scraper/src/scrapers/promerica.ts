import { Page } from "puppeteer";
import { BANK } from "src/enums";
import { BrowserScraper } from "src/scrapers/base";
import { validateAmount } from "src/utils/decorators";

export class PromericaScraper extends BrowserScraper {
  bank = BANK.PROMERICA;
  url = "https://www.promerica.com.do/";

  euroSectionSelector =
    "#tipoCambioHome > div:nth-child(1) > nav > a.btn.btn-link.tipoEuro";
  dollarSectionSelector =
    "#tipoCambioHome > div:nth-child(1) > nav > a.btn.btn-link.tipoDolar";

  buySelector = "#tipoCambioHome > div:nth-child(2) > p > span:nth-child(1)";
  sellSelector = "#tipoCambioHome > div:nth-child(2) > p > span:nth-child(3)";

  @validateAmount
  async getEuroBuyRate(page: Page): Promise<number> {
    await this.clickCurrencySection(this.euroSectionSelector, page);

    return this.getSingleRate(this.buySelector, page);
  }

  @validateAmount
  async getEuroSellRate(page: Page): Promise<number> {
    await this.clickCurrencySection(this.euroSectionSelector, page);

    return this.getSingleRate(this.sellSelector, page);
  }

  @validateAmount
  async getDollarBuyRate(page: Page): Promise<number> {
    await this.clickCurrencySection(this.dollarSectionSelector, page);

    return this.getSingleRate(this.buySelector, page);
  }

  @validateAmount
  async getDollarSellRate(page: Page): Promise<number> {
    await this.clickCurrencySection(this.dollarSectionSelector, page);

    return this.getSingleRate(this.sellSelector, page);
  }
}
