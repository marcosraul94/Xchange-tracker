import { ElementHandle, Page } from "puppeteer";
import { BANK } from "src/enums";
import { BrowserScraper } from "src/scrapers/base";
import { validateAmount } from "src/utils/decorators";

export class BanreservasScraper extends BrowserScraper {
  bank = BANK.BANRESERVAS;
  url = "https://www.banreservas.com";

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
