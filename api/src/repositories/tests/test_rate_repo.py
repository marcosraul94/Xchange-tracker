import unittest
from decimal import Decimal
from freezegun import freeze_time
from datetime import timedelta, datetime, UTC
from src.utils.e2e import E2ETestCase
from src.enums import Currency
from src.entities.bank import Bank
from src.entities.rate import Rate
from src.repositories.rate import RateRepo


class TestBankRepo(E2ETestCase):
    def setUp(self):
        super().setUp()
        self.repo = RateRepo()
        self.bank = Bank(name="bhd")
        self.currency = Currency.EURO
        self.rate = Rate(
            bank_name=self.bank.name,
            amount=Decimal(12),
            currency=self.currency,
        )

    def test_creation(self):
        self.repo.create(self.rate)
        rates = self.repo.find_by_bank_and_currency(self.bank, self.currency)

        self.assertListEqual(rates, [self.rate])

    def test_find_by_bank_and_currency(self):
        other_bank = Bank(name="popular")
        rate_from_other_bank = Rate(
            bank_name=other_bank.name,
            amount=Decimal(19),
            currency=self.currency,
        )
        self.repo.create(self.rate)
        self.repo.create(rate_from_other_bank)
        rates_from_bank = self.repo.find_by_bank_and_currency(
            self.bank,
            self.currency,
        )
        rates_from_other_bank = self.repo.find_by_bank_and_currency(
            other_bank,
            self.currency,
        )

        self.assertListEqual(rates_from_bank, [self.rate])
        self.assertListEqual(rates_from_other_bank, [rate_from_other_bank])

    def test_find_by_day(self):
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
        rates_from_today = self.repo.find_by_day(today)

        self.assertListEqual(rates_from_today, [now_rate])


if __name__ == "__main__":
    unittest.main()
