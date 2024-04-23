import { BANK } from "src/enums";
import { SimpleScrapers, BrowserScrapersClasses } from "src/types";

export interface BankRate {
  bank: BANK;
  sell: number;
  buy: number;
}

export interface ScrapeResult {
  dollar: BankRate;
  euro: BankRate;
}

export interface AppConfig {
  simpleScraperClasses: SimpleScrapers;
  browserScrapersClasses: BrowserScrapersClasses;
  timeout: number;
}
