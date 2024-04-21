import { BANK } from "src/enums";
import {
  BrowserScrapers,
  SimpleScrapers,
  BrowserScrapersClasses,
} from "src/types";

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
  simpleScraperClasses: BrowserScrapers;
  browserScrapersClasses: BrowserScrapersClasses;
  timeout: number;
}
