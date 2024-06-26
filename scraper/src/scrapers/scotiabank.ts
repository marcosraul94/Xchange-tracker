import { Page } from "puppeteer";
import { BANK } from "src/enums";
import { BrowserScraper } from "src/scrapers/base";
import { validateAmount } from "src/utils/decorators";

export class ScotiabankScraper extends BrowserScraper {
  bank = BANK.SCOTIABANK;
  url = "https://do.scotiabank.com/banca-personal/tarifas/tasas-de-cambio.html";
  ratesSelector = 'td[style="text-align: center;"]';

  async loadPage(): Promise<Page> {
    const page = await this.browser.newPage();
    page.goto(this.url, { waitUntil: "domcontentloaded" });
    await page.waitForSelector(this.ratesSelector);
    console.log(`Opened ${this.url}`);

    return page;
  }

  @validateAmount
  async getEuroBuyRate(page: Page): Promise<number> {
    const rates = await this.getMultipleRates(this.ratesSelector, page);

    return parseFloat(rates[6]);
  }

  @validateAmount
  async getEuroSellRate(page: Page): Promise<number> {
    const rates = await this.getMultipleRates(this.ratesSelector, page);

    return parseFloat(rates[7]);
  }

  @validateAmount
  async getDollarBuyRate(page: Page): Promise<number> {
    const rates = await this.getMultipleRates(this.ratesSelector, page);

    return parseFloat(rates[3]);
  }

  @validateAmount
  async getDollarSellRate(page: Page): Promise<number> {
    const rates = await this.getMultipleRates(this.ratesSelector, page);

    return parseFloat(rates[4]);
  }
}
