import unittest
from datetime import datetime, UTC
from src.entities.base import Entity
from src.constants import EntityType
from src.utils.serialization import DictSerialization


class TestEntity(unittest.TestCase):
    def setUp(self) -> None:
        self.now = datetime.now(UTC)
        self.entity = Entity(
            pk="pk",
            sk="sk",
            entity_type=EntityType.BANK,
            created_at=self.now,
            updated_at=self.now,
        )

    def test_creation(self):
        self.assertEqual(self.entity.pk, "pk")
        self.assertEqual(self.entity.sk, "sk")
        self.assertEqual(self.entity.created_at, self.now)
        self.assertEqual(self.entity.updated_at, self.now)

    def test_to_dict(self):
        self.assertDictEqual(
            self.entity.to_dict(),
            {
                "pk": "pk",
                "sk": "sk",
                "entity_type": EntityType.BANK,
                "created_at": self.now,
                "updated_at": self.now,
            },
        )

    def test_from_serialized(self):
        serialized = DictSerialization.serialize(self.entity.to_dict())
        entity = Entity.from_serialized(serialized)

        for key in ["pk", "sk", "entity_type", "created_at", "updated_at"]:
            self.assertEqual(getattr(entity, key), getattr(self.entity, key))

    def test_equality(self):
        serialized = DictSerialization.serialize(self.entity.to_dict())
        same_entity = Entity.from_serialized(serialized)

        self.assertEqual(same_entity, self.entity)

    def test_inequality(self):
        serialized = DictSerialization.serialize(self.entity.to_dict())
        different_entity = Entity.from_serialized(serialized)
        different_entity.sk = "different"

        self.assertNotEqual(different_entity, self.entity)


if __name__ == "__main__":
    unittest.main()
