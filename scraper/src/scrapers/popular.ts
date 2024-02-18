import { ElementHandle, Page } from "puppeteer";
import { BANK } from "src/enums";
import { ScrapeResult } from "src/interfaces";
import { BrowserScraper } from "src/scrapers/base";
import { DollarRate, EuroRate } from "src/entities/bankRate";
import { validateAmount } from "src/utils";

export class PopularScraper extends BrowserScraper {
  bank = BANK.POPULAR;
  url = "https://popularenlinea.com/personas/Paginas/Home.aspx";

  async fetchData(): Promise<ScrapeResult> {
    const page = await this.browser.newPage();
    await page.goto(this.url);

    const euroBuyRate = await this.getEuroBuyRate(page);
    const euroSellRate = await this.getEuroSellRate(page);

    const dollarBuyRate = await this.getDollarBuyRate(page);
    const dollarSellRate = await this.getDollarSellRate(page);

    return {
      euro: new EuroRate(this.bank, euroBuyRate, euroSellRate),
      dollar: new DollarRate(this.bank, dollarBuyRate, dollarSellRate),
    };
  }

  @validateAmount
  async getEuroBuyRate(page: Page): Promise<number> {
    const element = (await page.waitForSelector(
      "#compra_peso_euro_desktop"
    )) as ElementHandle<HTMLInputElement> | null;
    if (!element) throw Error("Not found selector");

    const amount = await element.evaluate((e) => e.value);
    return parseFloat(amount);
  }

  async getEuroSellRate(page: Page): Promise<number> {
    return 44;
  }

  async getDollarBuyRate(page: Page): Promise<number> {
    return 44;
  }

  async getDollarSellRate(page: Page): Promise<number> {
    return 44;
  }
}
