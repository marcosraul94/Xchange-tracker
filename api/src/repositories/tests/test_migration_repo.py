import unittest
from src.utils.e2e import E2ETestCase
from src.entities.migration import Migration
from src.repositories.migration import MigrationRepo


class TestMigration(E2ETestCase):
    def setUp(self):
        super().setUp()
        self.repo = MigrationRepo()
        self.migration = Migration(name="adding table")

    def test_creation(self):
        self.repo.create(self.migration)
        migrations = self.repo.find_all()

        self.assertListEqual(migrations, [self.migration])

    def test_find_all(self):
        another_migration = Migration(name="removing rows")
        self.repo.create(self.migration)
        self.repo.create(another_migration)
        migrations = self.repo.find_all()

        self.assertListEqual([self.migration, another_migration], migrations)


if __name__ == "__main__":
    unittest.main()
