import puppeteer, { Browser } from "puppeteer";
import { ScraperBase } from "src/scrapers/base";
import { AppConfig } from "src/interfaces";
import { BrowserScrapers, SimpleScrapers } from "src/types";

export class ScrapingSession {
  protected browser?: Browser;
  protected simpleScraperClasses: SimpleScrapers;
  protected browserScraperClasses: BrowserScrapers;
  protected concurrency: number;

  constructor({
    simpleScraperClasses,
    browserScraperClasses,
    concurrency,
  }: AppConfig) {
    this.simpleScraperClasses = simpleScraperClasses;
    this.browserScraperClasses = browserScraperClasses;
    this.concurrency = concurrency;
  }

  async run() {
    try {
      const scrapers = await this.buildScrapers();

      const results = [];
      for (const scraper of scrapers) {
        const result = await scraper.run();
        results.push(result);
      }

      console.log(results);
    } finally {
      await this.closeBrowser();
    }

    console.log(`Completed scraping session`);
  }

  protected async buildScrapers(): Promise<ScraperBase[]> {
    if (this.browserScraperClasses.length > 0) await this.openBrowser();

    const browserScrapers = this.browserScraperClasses.map(
      (Scraper) => new Scraper(this.browser as Browser)
    );
    const simpleScrapers = this.simpleScraperClasses.map(
      (Scraper) => new Scraper()
    );

    return [...browserScrapers, ...simpleScrapers];
  }

  protected async closeBrowser() {
    if (!this.browser) return;

    console.log(`Closing browser...`);
    await this.browser.close();
    console.log(`Browser closed successfully!`);
  }

  protected async openBrowser() {
    console.log(`Opening browser...`);
    this.browser = await puppeteer.launch({
      headless: "new",
      timeout: 3000,
      args: ["--no-sandbox"],
    });
    console.log(`Browser opened successfully!`);
  }
}
