import json
import unittest
from decimal import Decimal
from datetime import timedelta
from freezegun import freeze_time
from parameterized import parameterized
from app import app
from src.enums import Currency, EntityType
from src.entities.rate import Rate
from src.utils.datetime import now
from src.utils.e2e import E2ETestCase
from src.repositories.bank import BankRepo
from src.repositories.rate import RateRepo
from src.utils.serialization import (
    DecimalSerialization,
    EnumSerialization,
    DateSerialization,
)

creation_time = now()


class TestRatesViewPost(E2ETestCase):
    def setUp(self):
        super().setUp()

        app.testing = True
        self.app = app.test_client()
        self.bank = BankRepo().find_all()[0]

    def send_post(self, rates: list):
        payload = {"rates": rates}

        res = self.app.post(
            "/rates", json=payload, content_type="application/json"
        )

        status_code = res.status_code
        data = json.loads(res.data.decode())

        return status_code, data["data"]

    @freeze_time(creation_time)
    def test_create_rates__entity(self):
        rates_to_create = [
            {
                "bank_name": self.bank.name,
                "amount": DecimalSerialization.serialize(Decimal("59")),
                "currency": EnumSerialization.serialize(Currency.DOLLAR),
            },
        ]

        status_code, data = self.send_post(rates_to_create)

        self.assertEqual(status_code, 201)
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 1)

        dollar_rate = Rate.from_serialized(data[0])

        self.assertEqual(dollar_rate.amount, Decimal("59"))
        self.assertEqual(dollar_rate.bank_name, self.bank.name)
        self.assertEqual(dollar_rate.currency, Currency.DOLLAR)
        self.assertEqual(dollar_rate.created_at, creation_time)
        self.assertEqual(dollar_rate.updated_at, creation_time)
        self.assertEqual(dollar_rate.entity_type, EntityType.RATE)

    def test_create_rates__multiple(self):
        rates_to_create = [
            {
                "bank_name": self.bank.name,
                "amount": DecimalSerialization.serialize(Decimal("59")),
                "currency": EnumSerialization.serialize(Currency.DOLLAR),
            },
            {
                "bank_name": self.bank.name,
                "amount": DecimalSerialization.serialize(Decimal("62")),
                "currency": EnumSerialization.serialize(Currency.EURO),
            },
        ]

        status_code, data = self.send_post(rates_to_create)

        self.assertEqual(status_code, 201)
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 2)

        dollar_rate = Rate.from_serialized(data[0])

        self.assertEqual(dollar_rate.amount, Decimal("59"))
        self.assertEqual(dollar_rate.bank_name, self.bank.name)
        self.assertEqual(dollar_rate.currency, Currency.DOLLAR)

        euro_rate = Rate.from_serialized(data[1])

        self.assertEqual(euro_rate.amount, Decimal("62"))
        self.assertEqual(euro_rate.bank_name, self.bank.name)
        self.assertEqual(euro_rate.currency, Currency.EURO)

    @parameterized.expand(
        [(None, TypeError), ("0", ValueError), ("-2", ValueError)]
    )
    def test_create_rates__invalid_amount(self, amount, error):
        rates_to_create = [
            {
                "bank_name": self.bank.name,
                "amount": amount,
                "currency": EnumSerialization.serialize(Currency.DOLLAR),
            }
        ]

        with self.assertRaises(error):
            self.send_post(rates_to_create)

    @parameterized.expand([None, "invalid name"])
    def test_create_rates__invalid_bank_name(self, bank_name):
        rates_to_create = [
            {
                "bank_name": bank_name,
                "amount": DecimalSerialization.serialize(Decimal("59")),
                "currency": EnumSerialization.serialize(Currency.DOLLAR),
            }
        ]

        with self.assertRaises(ValueError):
            self.send_post(rates_to_create)


class TestRatesViewGet(E2ETestCase):
    def setUp(self):
        super().setUp()

        app.testing = True
        self.app = app.test_client()
        self.repo = RateRepo()
        self.amount = Decimal("24")
        self.bank_1, self.bank_2, self.bank_3 = BankRepo().find_all()[:3]

    def send_get(self, query_string: dict):
        res = self.app.get("/rates", query_string=query_string)
        rates = res.get_json()["data"]

        return {Rate.from_serialized(rate) for rate in rates}

    @parameterized.expand([Currency.DOLLAR, Currency.EURO])
    def test_find_rates_by_day_and_currency__filter_by_day(
        self,
        currency: Currency,
    ):
        with freeze_time(creation_time - timedelta(days=1)):
            rate_from_yesterday_bank_1 = Rate(
                self.bank_1.name, self.amount, currency
            )

        with freeze_time(creation_time):
            rate_from_today_bank_2 = Rate(
                self.bank_2.name, self.amount, currency
            )
            rate_from_today_bank_3 = Rate(
                self.bank_3.name, self.amount, currency
            )

            self.repo.create_all(
                [
                    rate_from_yesterday_bank_1,
                    rate_from_today_bank_2,
                    rate_from_today_bank_3,
                ]
            )

        query_params = {
            "day": DateSerialization.serialize(creation_time.date()),
            "currency": EnumSerialization.serialize(currency),
        }

        self.assertSetEqual(
            self.send_get(query_params),
            {
                rate_from_today_bank_2,
                rate_from_today_bank_3,
            },
        )

    @parameterized.expand(
        [(Currency.DOLLAR, Currency.EURO), (Currency.EURO, Currency.DOLLAR)]
    )
    def test_find_rates_by_day_and_currency__filter_by_currency(
        self,
        correct_currency,
        wrong_currency,
    ):
        wrong_currency_rate_1 = Rate(
            self.bank_1.name, self.amount, wrong_currency
        )
        correct_currency_rate_2 = Rate(
            self.bank_2.name, self.amount, correct_currency
        )
        correct_currency_rate_3 = Rate(
            self.bank_3.name, self.amount, correct_currency
        )

        self.repo.create_all(
            [
                wrong_currency_rate_1,
                correct_currency_rate_2,
                correct_currency_rate_3,
            ]
        )

        query_params = {
            "day": DateSerialization.serialize(creation_time.date()),
            "currency": EnumSerialization.serialize(correct_currency),
        }

        self.assertSetEqual(
            self.send_get(query_params),
            {
                correct_currency_rate_2,
                correct_currency_rate_3,
            },
        )

    @parameterized.expand([Currency.DOLLAR, Currency.EURO])
    def find_by_bank_and_currency__filter_by_bank(self, currency):
        correct_bank_rate_1 = Rate(self.bank_1.name, self.amount, currency)
        incorrect_bank_rate = Rate(self.bank_2.name, self.amount, currency)
        correct_bank_rate_2 = Rate(self.bank_3.name, self.amount, currency)

        self.repo.create_all(
            [correct_bank_rate_1, incorrect_bank_rate, correct_bank_rate_2]
        )

        query_params = {
            "bank_name": self.bank_1.name,
            "currency": EnumSerialization.serialize(currency),
        }

        self.assertSetEqual(
            self.send_get(query_params),
            {correct_bank_rate_1, correct_bank_rate_2},
        )

    @parameterized.expand(
        [(Currency.DOLLAR, Currency.EURO), (Currency.EURO, Currency.DOLLAR)]
    )
    def find_by_bank_and_currency__filter_by_currency(
        self, correct_currency, wrong_currency
    ):
        correct_bank_name = self.bank_1.name

        with freeze_time(creation_time - timedelta(days=1)):
            wrong_currency_rate = Rate(
                correct_bank_name, self.amount, wrong_currency
            )

        correct_currency_rate_1 = Rate(
            correct_bank_name, self.amount, correct_currency
        )
        correct_currency_rate_2 = Rate(
            correct_bank_name, self.amount, correct_currency
        )

        self.repo.create_all(
            [
                wrong_currency_rate,
                correct_currency_rate_1,
                correct_currency_rate_2,
            ]
        )

        query_params = {
            "bank_name": correct_bank_name,
            "currency": EnumSerialization.serialize(correct_currency),
        }

        self.assertSetEqual(
            self.send_get(query_params),
            {correct_currency_rate_1, correct_currency_rate_2},
        )


if __name__ == "__main__":
    unittest.main()
