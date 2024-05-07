import unittest
from decimal import Decimal
from unittest.mock import patch
from src.entities.rate import Rate
from src.entities.bank import Bank
from src.enums import EntityType, Currency
from src.utils.serialization import DictSerialization


class TestRateEntity(unittest.TestCase):
    @patch("src.entities.rate.uuid.uuid4", return_value="id")
    def setUp(self, _) -> None:
        self.bank = Bank(name="bhd")
        self.amount = Decimal(10)
        self.rate = Rate(
            pk=self.bank.pk,
            amount=self.amount,
            currency=Currency.DOLLAR,
        )

    def test_creation(self):
        self.assertEqual(self.rate.pk, self.bank.pk)
        self.assertEqual(self.rate.sk, "r#id")
        self.assertEqual(self.rate.amount, self.amount)
        self.assertEqual(self.rate.entity_type, EntityType.RATE)
        self.assertEqual(self.rate.currency, Currency.DOLLAR)

    def test_from_serialized(self):
        serialized = DictSerialization.serialize(self.rate.to_dict())
        entity = Rate.from_serialized(serialized)

        for key in [
            "pk",
            "sk",
            "entity_type",
            "created_at",
            "updated_at",
            "amount",
            "currency",
        ]:
            self.assertEqual(
                getattr(entity, key),
                getattr(self.rate, key),
            )


if __name__ == "__main__":
    unittest.main()
