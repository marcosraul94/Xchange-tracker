import { BankRate } from "src/entities/bankRate";

export interface ScrapeResult {
  dollar: BankRate;
  euro: BankRate;
}
