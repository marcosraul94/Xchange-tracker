import json
import unittest
from decimal import Decimal
from freezegun import freeze_time
from parameterized import parameterized
from app import app
from src.enums import Currency, EntityType
from src.entities.rate import Rate
from src.utils.datetime import now
from src.utils.e2e import E2ETestCase
from src.repositories.bank import BankRepo
from src.utils.serialization import DecimalSerialization, EnumSerialization

creation_time = now()


class TestRatesView(E2ETestCase):
    def setUp(self):
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

        with self.assertRaises(TypeError):
            self.send_post(rates_to_create)


if __name__ == "__main__":
    unittest.main()
