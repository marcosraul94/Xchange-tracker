import { BANK } from "src/enums";
import { BrowserScrapers } from "src/types";

export interface BankRate {
  bank: BANK;
  sell: number;
  buy: number;
}

export interface ScrapingResult {
  dollar: BankRate;
  euro: BankRate;
}

export interface AppConfig {
  Scrapers: BrowserScrapers;
  timeout: number;
}
