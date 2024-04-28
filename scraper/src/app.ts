import puppeteer, { Browser } from "puppeteer";
import { AppConfig, ScrapingResult } from "src/interfaces";
import { SimpleScrapers, BrowserScrapersClasses } from "src/types";
import { BROWSER_NAME } from "src/enums";

export class ScrapingSession {
  protected simpleScraperClasses: SimpleScrapers;
  protected browserScrapersClasses: BrowserScrapersClasses;
  protected timeout: number;
  public results: ScrapingResult[] = [];

  constructor({
    simpleScraperClasses = [],
    browserScrapersClasses = {},
    timeout = 10000,
  }: AppConfig) {
    this.simpleScraperClasses = simpleScraperClasses;
    this.browserScrapersClasses = browserScrapersClasses;
    this.timeout = timeout;
  }

  async run() {
    let openedBrowserName: BROWSER_NAME | undefined;
    let browser: Browser | undefined;

    try {
      for (const [browserName, Scrapers] of Object.entries(
        this.browserScrapersClasses
      )) {
        if (openedBrowserName !== browserName) {
          await this.closeBrowser(browser);
          browser = await this.openBrowser(browserName as BROWSER_NAME);
          openedBrowserName = browserName as BROWSER_NAME;
        }
        for (const Scraper of Scrapers) {
          const result = await new Scraper(browser as Browser).run();
          if (result) this.results.push(result);
        }
      }
    } finally {
      await this.closeBrowser(browser);
    }

    console.log(`Completed scraping session`);
  }

  async save() {}

  protected async closeBrowser(browser?: Browser) {
    if (!browser) return;

    console.log(`Closing browser...`);
    await browser.close();
    console.log(`Browser closed successfully!`);
  }

  protected async openBrowser(
    browserName: BROWSER_NAME = BROWSER_NAME.FIREFOX
  ) {
    console.log(`Opening ${browserName}...`);
    const browser = await puppeteer.launch({
      product: browserName,
      headless: true,
      timeout: 10000,
      args: ["--no-sandbox"],
    });
    console.log(`Browser opened successfully!`);

    return browser;
  }
}
