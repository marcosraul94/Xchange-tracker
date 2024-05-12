from datetime import date
from src.enums import Currency
from src.views.base import View
from src.entities.bank import Bank
from src.repositories.rate import RateRepo


class RateView(View):
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
