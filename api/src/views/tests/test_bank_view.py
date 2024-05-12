import unittest
from app import app
from src.entities.bank import Bank


class TestBankView(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_fetches_all_banks(self):
        response = self.app.get("/banks")
        serialized_banks = response.get_json()["data"]
        banks = [Bank.from_serialized(bank) for bank in serialized_banks]

        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(banks) > 1)


if __name__ == "__main__":
    unittest.main()
