import puppeteer, { Browser, Page } from "puppeteer";
import { BANK } from "src/enums";
import { ScrapeResult } from "src/interfaces";

export abstract class ScraperBase {
  abstract url: string;

  abstract fetchData(): Promise<ScrapeResult>;

  abstract scrape(): Promise<ScrapeResult>;
}

export abstract class BrowserScraper extends ScraperBase {
  // @ts-ignore
  browser: Browser;
  abstract bank: BANK;

  abstract getEuroBuyRate(page: Page): Promise<number>;
  abstract getEuroSellRate(page: Page): Promise<number>;
  abstract getDollarBuyRate(page: Page): Promise<number>;
  abstract getDollarSellRate(page: Page): Promise<number>;

  async open() {
    console.log(`Opening browser...`);
    this.browser = await puppeteer.launch({
      headless: "new",
      timeout: 3000,
      args: ["--no-sandbox"],
    });
    console.log(`Browser opened successfully!`);
  }

  async close() {
    console.log(`Closing browser...`);
    if (!this.browser) return;

    await this.browser.close();
    console.log(`Browser closed successfully!`);
  }

  async scrape(): Promise<ScrapeResult> {
    await this.open();

    try {
      console.log(`Fetching data from ${this.bank}...`);
      const fetchedData = await this.fetchData();
      console.log(`Fetch completed from ${this.bank}!`);

      return fetchedData;
    } finally {
      await this.close();
    }
  }
}
