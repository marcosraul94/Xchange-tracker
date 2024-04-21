import { Browser, Page } from "puppeteer";
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

  async loadPage(): Promise<Page> {
    const page = await this.browser.newPage();
    await page.goto(this.url);
    console.log(`Opened ${this.url}`);

    return page;
  }

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
