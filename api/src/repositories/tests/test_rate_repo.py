import unittest
from decimal import Decimal
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
        self.rate = Rate(
            pk=self.bank.pk,
            amount=Decimal(12),
            currency=Currency.EURO,
        )

    def test_creation(self):
        self.repo.create(self.rate)
        rates = self.repo.find_by_bank(self.bank)

        self.assertListEqual(rates, [self.rate])

    def test_find_by_bank(self):
        other_bank = Bank(name="popular")
        rate_from_other_bank = Rate(
            pk=other_bank.pk,
            amount=Decimal(19),
            currency=Currency.DOLLAR,
        )
        self.repo.create(self.rate)
        self.repo.create(rate_from_other_bank)
        rates_from_bank = self.repo.find_by_bank(self.bank)
        rates_from_other_bank = self.repo.find_by_bank(other_bank)

        self.assertListEqual(rates_from_bank, [self.rate])
        self.assertListEqual(rates_from_other_bank, [rate_from_other_bank])

    def test_find_by_day(self):
        now_rate = self.rate

        earlier_rate = Rate(
            pk=self.bank.pk,
            amount=Decimal(5),
            currency=Currency.DOLLAR,
        )
        earlier_rate.created_at -= timedelta(milliseconds=1)

        yesterday_rate = Rate(
            pk=self.bank.pk,
            amount=Decimal(5),
            currency=Currency.DOLLAR,
        )
        yesterday_rate.created_at -= timedelta(days=1)

        last_month_rate = Rate(
            pk=self.bank.pk,
            amount=Decimal(5),
            currency=Currency.DOLLAR,
        )
        last_month_rate.created_at -= timedelta(days=32)

        self.repo.create_all(
            [now_rate, earlier_rate, yesterday_rate, last_month_rate]
        )

        today = datetime.now(UTC).date()
        rates_from_today = self.repo.find_by_day(today)

        self.assertListEqual(rates_from_today, [earlier_rate, now_rate])


if __name__ == "__main__":
    unittest.main()
