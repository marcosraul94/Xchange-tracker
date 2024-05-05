import unittest
from src.constants import EntityType
from src.entities.migration import Migration
from src.utils.serialization import DictSerialization


class TestMigration(unittest.TestCase):
    def setUp(self) -> None:
        self.migration = Migration(name="adding table")

    def test_creation(self):
        self.assertEqual(self.migration.pk, "m#")
        self.assertEqual(self.migration.sk, "m#adding table")
        self.assertEqual(self.migration.name, "adding table")
        self.assertEqual(self.migration.entity_type, EntityType.MIGRATION)

    def test_from_serialized(self):
        serialized = DictSerialization.serialize(self.migration.to_dict())
        entity = Migration.from_serialized(serialized)

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
                getattr(self.migration, key),
            )


if __name__ == "__main__":
    unittest.main()
