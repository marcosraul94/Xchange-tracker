import { BANK } from "src/enums";

export class BankRate {
  bank: BANK;
  buy: number;
  sell: number;

  constructor(bank: BANK, buy: number, sell: number) {
    this.bank = bank;
    this.buy = buy;
    this.sell = sell;
  }
}

export class DollarRate extends BankRate {}

export class EuroRate extends BankRate {}
