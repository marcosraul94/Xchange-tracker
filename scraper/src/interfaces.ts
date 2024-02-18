import { BANK } from "src/enums";

export interface BankRate {
  bank: BANK;
  sell: number;
  buy: number;
}

export interface ScrapeResult {
  dollar: BankRate;
  euro: BankRate;
}
