import { ElementHandle, Page } from "puppeteer";
import { BANK } from "src/enums";
import { ScrapeResult } from "src/interfaces";
import { BrowserScraper } from "src/scrapers/base";
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
      euro: { bank: this.bank, buy: euroBuyRate, sell: euroSellRate },
      dollar: { bank: this.bank, buy: dollarBuyRate, sell: dollarSellRate },
    };
  }

  async parseValue(page: Page, selector: string): Promise<number> {
    const element = (await page.waitForSelector(
      selector
    )) as ElementHandle<HTMLInputElement> | null;
    if (!element) throw Error("Not found selector");

    const amount = await element.evaluate((e) => e.value);
    return parseFloat(amount);
  }

  @validateAmount
  async getEuroBuyRate(page: Page): Promise<number> {
    return this.parseValue(page, "#compra_peso_euro_desktop");
  }

  @validateAmount
  async getEuroSellRate(page: Page): Promise<number> {
    return this.parseValue(page, "#venta_peso_euro_desktop");
  }

  @validateAmount
  async getDollarBuyRate(page: Page): Promise<number> {
    return this.parseValue(page, "#compra_peso_dolar_desktop");
  }

  @validateAmount
  async getDollarSellRate(page: Page): Promise<number> {
    return this.parseValue(page, "#venta_peso_dolar_desktop");
  }
}
