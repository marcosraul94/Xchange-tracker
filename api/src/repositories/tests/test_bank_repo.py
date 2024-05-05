import unittest
from src.utils.e2e import E2ETestCase
from src.entities.bank import Bank
from src.repositories.bank import BankRepo


class TestMigration(E2ETestCase):
    def setUp(self):
        super().setUp()
        self.repo = BankRepo()
        self.bank = Bank(name="bhd")

    def test_creation(self):
        self.repo.create(self.bank)
        banks = self.repo.find_all()

        self.assertListEqual(banks, [self.bank])

    def test_find_all(self):
        another_bank = Bank(name="popular")
        self.repo.create(self.bank)
        self.repo.create(another_bank)
        banks = self.repo.find_all()

        self.assertListEqual([self.bank, another_bank], banks)


if __name__ == "__main__":
    unittest.main()
