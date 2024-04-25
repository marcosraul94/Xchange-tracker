import { Page } from "puppeteer";
import { BANK } from "src/enums";
import { BrowserScraper } from "src/scrapers/base";
import { validateAmount } from "src/utils/decorators";

export class BHDScraper extends BrowserScraper {
  bank = BANK.BHD;
  url = "https://bhd.com.do/calculators?calculator=DIVISAS";
  
  dollarSectionSelector = '[id="3"]';
  euroSectionSelector = '[id="1"]';

  async getAllRates(page: Page) {
    const selector = "input.ng-untouched";
    await page.waitForSelector(selector);

    return page.$$eval(selector, (tds) => tds.map((td) => td.value)) as Promise<
      string[]
    >;
  }

  @validateAmount
  async getEuroBuyRate(page: Page): Promise<number> {
    await this.clickCurrencySection(this.euroSectionSelector, page);
    const rates = await this.getAllRates(page);

    return parseFloat(rates[2]);
  }

  @validateAmount
  async getEuroSellRate(page: Page): Promise<number> {
    await this.clickCurrencySection(this.euroSectionSelector, page);
    const rates = await this.getAllRates(page);

    return parseFloat(rates[4]);
  }

  @validateAmount
  async getDollarBuyRate(page: Page): Promise<number> {
    await this.clickCurrencySection(this.dollarSectionSelector, page);
    const rates = await this.getAllRates(page);

    return parseFloat(rates[2]);
  }

  @validateAmount
  async getDollarSellRate(page: Page): Promise<number> {
    await this.clickCurrencySection(this.dollarSectionSelector, page);
    const rates = await this.getAllRates(page);

    return parseFloat(rates[4]);
  }
}
