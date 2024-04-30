import unittest
from datetime import datetime
from src.entities.base import Entity


class TestModel(unittest.TestCase):
    def setUp(self) -> None:
        self.now = datetime.now()
        self.entity = Entity(id="a", created_at=self.now, updated_at=self.now)

    def test_creation(self):
        self.assertEqual(self.entity.id, "a")
        self.assertEqual(self.entity.created_at, self.now)
        self.assertEqual(self.entity.updated_at, self.now)

    def test_to_dict(self):
        self.assertEqual(
            self.entity.to_dict(),
            {
                "id": "a",
                "created_at": self.now,
                "updated_at": self.now,
                "entity_type": None,
            },
        )


if __name__ == "__main__":
    unittest.main()
