import { Page } from "puppeteer";
import { BANK } from "src/enums";
import { ScrapeResult } from "src/interfaces";
import { BrowserScraper } from "src/scrapers/base";
import { validateAmount } from "src/utils";

export class ScotiabankScraper extends BrowserScraper {
  bank = BANK.SCOTIABANK;
  url = "https://do.scotiabank.com/banca-personal/tarifas/tasas-de-cambio.html";

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
