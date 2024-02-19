import puppeteer, { Browser, Page } from "puppeteer";
import { BANK } from "src/enums";
import { ScrapeResult } from "src/interfaces";

export abstract class ScraperBase {
  abstract url: string;

  abstract run(): Promise<ScrapeResult>;

  abstract fetchData(): Promise<ScrapeResult>;
}

export abstract class BrowserScraper extends ScraperBase {
  browser: Browser;
  abstract bank: BANK;

  constructor(browser: Browser) {
    super();
    this.browser = browser;
  }

  abstract getEuroBuyRate(page: Page): Promise<number>;
  abstract getEuroSellRate(page: Page): Promise<number>;
  abstract getDollarBuyRate(page: Page): Promise<number>;
  abstract getDollarSellRate(page: Page): Promise<number>;

  async run(): Promise<ScrapeResult> {
    console.log(`Fetching data from ${this.bank}...`);
    const fetchedData = await this.fetchData();
    console.log(`Fetch completed from ${this.bank}!`);

    return fetchedData;
  }
}
