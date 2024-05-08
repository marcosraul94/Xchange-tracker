import unittest
from decimal import Decimal
from freezegun import freeze_time
from datetime import timedelta, datetime, UTC
from src.utils.e2e import E2ETestCase
from src.enums import Currency
from src.entities.bank import Bank
from src.entities.rate import Rate
from src.repositories.rate import RateRepo


class TestRateRepo(E2ETestCase):
    def setUp(self):
        super().setUp()
        self.repo = RateRepo()
        self.bank = Bank(name="bhd")
        self.rate = Rate(
            bank_name=self.bank.name,
            amount=Decimal(12),
            currency=Currency.DOLLAR,
        )

    def test_creation(self):
        self.repo.create(self.rate)
        rates = self.repo.find_by_bank_and_currency(
            self.bank,
            self.rate.currency,
        )

        self.assertListEqual(rates, [self.rate])

    def test_find_by_bank_and_currency__filters_by_bank(self):
        other_bank = Bank(name="popular")
        rate_from_other_bank = Rate(
            bank_name=other_bank.name,
            amount=Decimal(19),
            currency=self.rate.currency,
        )
        self.repo.create(self.rate)
        self.repo.create(rate_from_other_bank)
        rates_from_bank = self.repo.find_by_bank_and_currency(
            self.bank,
            self.rate.currency,
        )
        rates_from_other_bank = self.repo.find_by_bank_and_currency(
            other_bank,
            self.rate.currency,
        )

        self.assertListEqual(rates_from_bank, [self.rate])
        self.assertListEqual(rates_from_other_bank, [rate_from_other_bank])

    def test_find_by_bank_and_currency__filers_by_currency(self):
        euro_rate = Rate(
            bank_name=self.rate.bank_name,
            amount=Decimal(19),
            currency=Currency.EURO,
        )
        self.repo.create(self.rate)
        self.repo.create(euro_rate)

        dollar_rates = self.repo.find_by_bank_and_currency(
            self.bank,
            self.rate.currency,
        )
        euro_rates = self.repo.find_by_bank_and_currency(
            self.bank,
            euro_rate.currency,
        )

        self.assertListEqual(dollar_rates, [self.rate])
        self.assertListEqual(euro_rates, [euro_rate])

    def test_find_by_day_and_currency__filters_by_date(self):
        now_rate = self.rate

        with freeze_time(now_rate.created_at - timedelta(days=1)):
            yesterday_rate = Rate(
                bank_name=self.bank.name,
                amount=Decimal(5),
                currency=Currency.DOLLAR,
            )

        with freeze_time(now_rate.created_at - timedelta(days=31)):
            last_month_rate = Rate(
                bank_name=self.bank.name,
                amount=Decimal(5),
                currency=Currency.DOLLAR,
            )

        self.repo.create_all([now_rate, yesterday_rate, last_month_rate])

        today = datetime.now(UTC).date()
        rates_from_today = self.repo.find_by_day_and_currency(
            today,
            Currency.DOLLAR,
        )

        self.assertListEqual(rates_from_today, [now_rate])

    def test_find_by_day_and_currency__filters_by_currency(self):
        day = self.rate.created_at.date()

        with freeze_time(day):
            euro_rate = Rate(
                bank_name=self.bank.name,
                amount=Decimal(5),
                currency=Currency.EURO,
            )
            self.repo.create(euro_rate)

        euro_rates_from_today = self.repo.find_by_day_and_currency(
            day,
            Currency.EURO,
        )

        self.assertListEqual(euro_rates_from_today, [euro_rate])


if __name__ == "__main__":
    unittest.main()
