from unittest import TestCase
from src.repositories.base import Repository


class E2ETestCase(TestCase):
    def setUp(self):
        table = Repository().table
        response = table.scan()
        items = response.get("Items", [])

        for item in items:
            table.delete_item(Key={"pk": item["pk"], "sk": item["sk"]})
