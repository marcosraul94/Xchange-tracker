import { Browser, Page } from "puppeteer";
import { BANK } from "src/enums";
import { ScrapeResult } from "src/interfaces";
import { time } from "src/utils/decorators";
import { NotImplementedError } from "src/utils/errors";

export abstract class ScraperBase {
  abstract url?: string;

  abstract run(): Promise<ScrapeResult>;

  abstract fetchData(): Promise<ScrapeResult>;
}

export class BrowserScraper implements ScraperBase {
  browser: Browser;
  url: string = "";
  bank: BANK = "" as BANK;

  constructor(browser: Browser) {
    this.browser = browser;
  }

  async getEuroBuyRate(page: Page): Promise<number> {
    throw NotImplementedError;
  }
  async getEuroSellRate(page: Page): Promise<number> {
    throw NotImplementedError;
  }
  async getDollarBuyRate(page: Page): Promise<number> {
    throw NotImplementedError;
  }
  async getDollarSellRate(page: Page): Promise<number> {
    throw NotImplementedError;
  }

  async loadPage(): Promise<Page> {
    const page = await this.browser.newPage();
    await page.goto(this.url);
    console.log(`Opened ${this.url}`);

    return page;
  }

  async clickCurrencySection(selector: string, page: Page) {
    await page.waitForSelector(selector);
    await page.$$eval(selector, (tds) => {
      tds.forEach((td) => (td as any).click());
    });
  }

  @time
  async fetchData(): Promise<ScrapeResult> {
    const page = await this.loadPage();

    const euroBuyRate = await this.getEuroBuyRate(page);
    const euroSellRate = await this.getEuroSellRate(page);

    const dollarBuyRate = await this.getDollarBuyRate(page);
    const dollarSellRate = await this.getDollarSellRate(page);

    await page.close();

    return {
      euro: { bank: this.bank, buy: euroBuyRate, sell: euroSellRate },
      dollar: { bank: this.bank, buy: dollarBuyRate, sell: dollarSellRate },
    };
  }

  async run(): Promise<ScrapeResult> {
    console.log(`Fetching data from ${this.bank}...`);
    const fetchedData = await this.fetchData();
    console.log(`Fetch completed from ${this.bank}!`);

    return fetchedData;
  }
}
