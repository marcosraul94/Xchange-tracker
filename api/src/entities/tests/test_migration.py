import unittest
from src.entities.migration import Migration


class TestMigration(unittest.TestCase):
    def setUp(self) -> None:
        self.migration = Migration(name="adding table")

    def test_creation(self):
        self.assertEqual(self.migration.pk, "m#")
        self.assertEqual(self.migration.sk, "m#adding table")
        self.assertEqual(self.migration.name, "adding table")


if __name__ == "__main__":
    unittest.main()
