from datetime import date
from decimal import Decimal
from src.enums import Currency
from src.views.base import View
from src.entities.bank import Bank
from src.entities.rate import Rate
from src.repositories.rate import RateRepo
from src.repositories.bank import BankRepo
from src.utils.serialization import DictSerialization


class RatesView(View):
    repo = RateRepo()

    def get(self, day: date, currency: Currency, bank: Bank):
        if not currency:
            raise ValueError(f"Missing currency: {currency}")

        if not bank or not day:
            raise ValueError(f"Missing bank or day: {[bank, day]}")

        rates = (
            self.repo.find_by_bank_and_currency(bank, currency)
            if bank
            else self.repo.find_by_day_and_currency(day, currency)
        )

        return self.format_response([rate.to_dict() for rate in rates])

    def post(self, rates: list[dict]):
        existing_bank_names = [bank.name for bank in BankRepo().find_all()]
        created_rates: list[Rate] = []

        for rate in rates:
            if rate["bank_name"] not in existing_bank_names:
                raise ValueError(
                    f"{rate['bank_name']} does not match existing banks"
                )

            if rate["amount"] <= Decimal("0"):
                raise ValueError(
                    f"Invalid amount {rate['amount']} from {rate['bank_name']}"
                )

            created_rates.append(Rate(**rate))

        self.repo.create_all(created_rates)

        return self.format_response(
            [
                DictSerialization.serialize(rate.to_dict())
                for rate in created_rates
            ],
            status_code=201,
        )
