import { Page } from "puppeteer";
import { BANK, BROWSER_NAME, ELEMENT_TYPE } from "src/enums";
import { BrowserScraper } from "src/scrapers/base";
import { validateAmount } from "src/utils/decorators";

export class BHDScraper extends BrowserScraper {
  static browserName = BROWSER_NAME.CHROME;
  bank = BANK.BHD;
  url = "https://bhd.com.do/calculators?calculator=DIVISAS";

  ratesSelector = "input.ng-untouched";
  dollarSectionSelector = '[id="3"]';
  euroSectionSelector = '[id="1"]';

  @validateAmount
  async getEuroBuyRate(page: Page): Promise<number> {
    await this.clickCurrencySection(this.euroSectionSelector, page);
    const rates = await this.getMultipleRates(
      this.ratesSelector,
      page,
      ELEMENT_TYPE.INPUT
    );

    return parseFloat(rates[2]);
  }

  @validateAmount
  async getEuroSellRate(page: Page): Promise<number> {
    await this.clickCurrencySection(this.euroSectionSelector, page);
    const rates = await this.getMultipleRates(
      this.ratesSelector,
      page,
      ELEMENT_TYPE.INPUT
    );

    return parseFloat(rates[4]);
  }

  @validateAmount
  async getDollarBuyRate(page: Page): Promise<number> {
    await this.clickCurrencySection(this.dollarSectionSelector, page);
    const rates = await this.getMultipleRates(
      this.ratesSelector,
      page,
      ELEMENT_TYPE.INPUT
    );

    return parseFloat(rates[2]);
  }

  @validateAmount
  async getDollarSellRate(page: Page): Promise<number> {
    await this.clickCurrencySection(this.dollarSectionSelector, page);
    const rates = await this.getMultipleRates(
      this.ratesSelector,
      page,
      ELEMENT_TYPE.INPUT
    );

    return parseFloat(rates[4]);
  }
}
