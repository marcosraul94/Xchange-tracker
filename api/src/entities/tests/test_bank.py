import unittest
from src.entities.bank import Bank
from src.enums import EntityType
from src.utils.serialization import DictSerialization


class TestBank(unittest.TestCase):
    def setUp(self) -> None:
        self.bank = Bank(name="bhd")

    def test_creation(self):
        self.assertEqual(self.bank.pk, "b#bhd")
        self.assertEqual(self.bank.sk, "b#bhd")
        self.assertEqual(self.bank.name, "bhd")
        self.assertEqual(self.bank.entity_type, EntityType.BANK)

    def test_from_serialized(self):
        serialized = DictSerialization.serialize(self.bank.to_dict())
        entity = Bank.from_serialized(serialized)

        for key in [
            "pk",
            "sk",
            "entity_type",
            "created_at",
            "updated_at",
            "name",
        ]:
            self.assertEqual(
                getattr(entity, key),
                getattr(self.bank, key),
            )


if __name__ == "__main__":
    unittest.main()
