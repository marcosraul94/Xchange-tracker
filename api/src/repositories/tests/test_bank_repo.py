import unittest
from src.utils.e2e import E2ETestCase
from src.entities.bank import Bank
from src.repositories.bank import BankRepo


class TestBankRepo(E2ETestCase):
    def setUp(self):
        super().setUp()
        self.repo = BankRepo()

    def test_creation(self):
        new_bank = Bank(name="new_bank")

        self.repo.create(new_bank)
        banks = self.repo.find_all()

        self.assertIn(new_bank, banks)

    def test_find_all(self):
        banks = self.repo.find_all()

        self.assertIsInstance(banks, list)
        self.assertTrue(len(banks) > 1)
        self.assertIsInstance(banks[0], Bank)


if __name__ == "__main__":
    unittest.main()
