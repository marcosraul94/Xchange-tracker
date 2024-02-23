import { ElementHandle, Page } from "puppeteer";
import { BANK } from "src/enums";
import { ScrapeResult } from "src/interfaces";
import { BrowserScraper } from "src/scrapers/base";
import { validateAmount, delay } from "src/utils";

export class BanreservasScraper extends BrowserScraper {
  bank = BANK.BANRESERVAS;
  url = "https://www.banreservas.com";

  async fetchData(): Promise<ScrapeResult> {
    const page = await this.browser.newPage();
    await page.goto(this.url);
    await delay(2000);

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
    )) as ElementHandle<HTMLDataElement> | null;
    if (!element) throw Error("Not found selector");

    const amount = await element.evaluate((e) => e.textContent);
    if (!amount) throw Error("Invalid amount");

    return parseFloat(amount);
  }

  @validateAmount
  async getEuroBuyRate(page: Page): Promise<number> {
    return this.parseValue(page, ".tasacambio-compraEU");
  }

  @validateAmount
  async getEuroSellRate(page: Page): Promise<number> {
    return this.parseValue(page, ".tasacambio-ventaEU");
  }

  @validateAmount
  async getDollarBuyRate(page: Page): Promise<number> {
    return this.parseValue(page, ".tasacambio-compraUS");
  }

  @validateAmount
  async getDollarSellRate(page: Page): Promise<number> {
    return this.parseValue(page, ".tasacambio-ventaUS");
  }
}
