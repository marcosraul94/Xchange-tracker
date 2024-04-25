import { Browser, Page } from "puppeteer";
import { BANK, ELEMENT_TYPE } from "src/enums";
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

  async getSingleRate(
    selector: string,
    page: Page,
    elementType: ELEMENT_TYPE = ELEMENT_TYPE.TXT
  ) {
    const element = await page.waitForSelector(selector);
    if (!element) throw Error("Not found selector");

    let amount;
    if (elementType === ELEMENT_TYPE.TXT) {
      amount = await element.evaluate((e) => e.textContent);
    }
    if (elementType === ELEMENT_TYPE.INPUT) {
      amount = await element.evaluate((e) => (e as HTMLInputElement).value);
    }

    if (!amount) throw Error("Invalid amount");
    return parseFloat(amount);
  }

  async getMultipleRates(
    selector: string,
    page: Page,
    elementType: ELEMENT_TYPE = ELEMENT_TYPE.TXT
  ) {
    const element = await page.waitForSelector(selector);
    if (!element) throw Error("Not found selector");

    let amounts: any[] = [];
    if (elementType === ELEMENT_TYPE.TXT) {
      amounts = await page.$$eval(selector, (elements) =>
        elements.map((e) => e.textContent)
      );
    }
    if (elementType === ELEMENT_TYPE.INPUT) {
      amounts = await page.$$eval(selector, (elements) =>
        elements.map((e) => (e as HTMLInputElement).value)
      );
    }

    if (amounts?.length === 0) throw Error("Invalid amounts");

    return amounts;
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
