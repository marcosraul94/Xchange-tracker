import { ElementHandle, Page } from "puppeteer";
import { BANK, ELEMENT_TYPE } from "src/enums";
import { BrowserScraper } from "src/scrapers/base";
import { validateAmount } from "src/utils/decorators";

export class PopularScraper extends BrowserScraper {
  bank = BANK.POPULAR;
  url = "https://popularenlinea.com/personas/Paginas/Home.aspx";

  @validateAmount
  async getEuroBuyRate(page: Page): Promise<number> {
    return this.getSingleRate(
      "#compra_peso_euro_desktop",
      page,
      ELEMENT_TYPE.INPUT
    );
  }

  @validateAmount
  async getEuroSellRate(page: Page): Promise<number> {
    return this.getSingleRate(
      "#venta_peso_euro_desktop",
      page,
      ELEMENT_TYPE.INPUT
    );
  }

  @validateAmount
  async getDollarBuyRate(page: Page): Promise<number> {
    return this.getSingleRate(
      "#compra_peso_dolar_desktop",
      page,
      ELEMENT_TYPE.INPUT
    );
  }

  @validateAmount
  async getDollarSellRate(page: Page): Promise<number> {
    return this.getSingleRate(
      "#venta_peso_dolar_desktop",
      page,
      ELEMENT_TYPE.INPUT
    );
  }
}
