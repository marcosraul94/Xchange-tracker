import puppeteer, { Browser } from "puppeteer";
import { AppConfig, ScrapingResult } from "src/interfaces";
import { BrowserScrapers } from "src/types";
import { BANK, BROWSER_NAME } from "src/enums";

export class ScrapingSession {
  protected Scrapers: BrowserScrapers = [];
  protected timeout: number;
  public results: ScrapingResult[] = [];
  public failedBanks: BANK[] = [];

  constructor({ Scrapers = [], timeout = 10000 }: AppConfig) {
    this.Scrapers = [...Scrapers];
    this.Scrapers.sort((Scraper) => Scraper.browserName as any);

    this.timeout = timeout;
  }

  async run() {
    let browser: Browser | undefined;
    let browserName: BROWSER_NAME | undefined;

    for (const Scraper of this.Scrapers) {
      if (Scraper.browserName !== browserName) {
        await this.closeBrowser(browser);
        browser = await this.openBrowser(Scraper.browserName);
        browserName = Scraper.browserName;
      }

      const scraper = new Scraper(browser as Browser);
      const result = await scraper.run();

      if (result) this.results.push(result);
      else this.failedBanks.push(scraper.bank);
    }

    await this.closeBrowser(browser);

    console.log(`Completed scraping session!`);
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
      ignoreHTTPSErrors: true,
      product: browserName,
      headless: true,
      timeout: 10000,
      args: ["--no-sandbox"],
    });
    console.log(`Browser opened successfully!`);

    return browser;
  }
}
