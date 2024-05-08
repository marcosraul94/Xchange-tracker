import unittest
from decimal import Decimal
from freezegun import freeze_time
from src.entities.rate import Rate
from src.enums import EntityType, Currency
from src.utils.serialization import DictSerialization

frozen_day = "2024-05-08"


class TestRateEntity(unittest.TestCase):
    @freeze_time(frozen_day)
    def setUp(self) -> None:
        self.amount = Decimal(10)
        self.rate = Rate(
            bank_name="bhd",
            amount=self.amount,
            currency=Currency.DOLLAR,
        )

    def test_creation(self):
        self.assertEqual(self.rate.pk, "b#bhd")
        self.assertEqual(self.rate.sk, f"r#dollar#{frozen_day}")
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
