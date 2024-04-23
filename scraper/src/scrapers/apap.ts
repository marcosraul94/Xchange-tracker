import { ElementHandle, Page } from "puppeteer";
import { BANK } from "src/enums";
import { BrowserScraper } from "src/scrapers/base";
import { validateAmount } from "src/utils";

export class ApapScraper extends BrowserScraper {
  bank = BANK.APAP;
  url = "https://apap.com.do/";

  async parseValue(page: Page, selector: string): Promise<number> {
    const element = (await page.waitForSelector(
      selector
    )) as ElementHandle<HTMLDataElement> | null;
    if (!element) throw Error("Not found selector");

    const amount = await element.evaluate((e) => e.textContent?.split(" ")[0]);
    if (!amount) throw Error("Invalid amount");

    return parseFloat(amount);
  }

  @validateAmount
  async getEuroBuyRate(page: Page): Promise<number> {
    return this.parseValue(page, "#currency-buy-EUR");
  }

  @validateAmount
  async getEuroSellRate(page: Page): Promise<number> {
    return this.parseValue(page, "#currency-sell-EUR");
  }

  @validateAmount
  async getDollarBuyRate(page: Page): Promise<number> {
    return this.parseValue(page, "#currency-buy-USD");
  }

  @validateAmount
  async getDollarSellRate(page: Page): Promise<number> {
    return this.parseValue(page, "#currency-sell-USD");
  }
}
