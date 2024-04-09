import { Page } from "puppeteer";
import { BANK } from "src/enums";
import { BrowserScraper } from "src/scrapers/base";
import { validateAmount } from "src/utils";

export class ScotiabankScraper extends BrowserScraper {
  bank = BANK.SCOTIABANK;
  url = "https://do.scotiabank.com/banca-personal/tarifas/tasas-de-cambio.html";

  async getAllRates(page: Page) {
    return page.$$eval('td[style="text-align: center;"]', (tds) =>
      tds.map((td) => td.textContent)
    ) as Promise<string[]>;
  }

  @validateAmount
  async getEuroBuyRate(page: Page): Promise<number> {
    const rates = await this.getAllRates(page);

    return parseFloat(rates[6]);
  }

  @validateAmount
  async getEuroSellRate(page: Page): Promise<number> {
    const rates = await this.getAllRates(page);

    return parseFloat(rates[7]);
  }

  @validateAmount
  async getDollarBuyRate(page: Page): Promise<number> {
    const rates = await this.getAllRates(page);

    return parseFloat(rates[3]);
  }

  @validateAmount
  async getDollarSellRate(page: Page): Promise<number> {
    const rates = await this.getAllRates(page);

    return parseFloat(rates[4]);
  }

  async parseValue(amount: string): Promise<number> {
    return parseFloat(amount);
  }
}
