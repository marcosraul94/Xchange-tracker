import { ElementHandle, Page } from "puppeteer";
import { BANK, BROWSER_NAME } from "src/enums";
import { BrowserScraper } from "src/scrapers/base";
import { validateAmount } from "src/utils/decorators";

export class BanreservasScraper extends BrowserScraper {
  bank = BANK.BANRESERVAS;
  url = "https://www.banreservas.com";

  @validateAmount
  async getEuroBuyRate(page: Page): Promise<number> {
    return this.getSingleRate(".tasacambio-compraEU", page);
  }

  @validateAmount
  async getEuroSellRate(page: Page): Promise<number> {
    return this.getSingleRate(".tasacambio-ventaEU", page);
  }

  @validateAmount
  async getDollarBuyRate(page: Page): Promise<number> {
    return this.getSingleRate(".tasacambio-compraUS", page);
  }

  @validateAmount
  async getDollarSellRate(page: Page): Promise<number> {
    return this.getSingleRate(".tasacambio-ventaUS", page);
  }
}
