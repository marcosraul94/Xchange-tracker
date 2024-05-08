from src.entities.base import Entity
from src.enums import EntityType


class Bank(Entity):
    def __init__(self, name: str):
        pk = f"b#{name}"

        self.name = name
        super().__init__(pk, sk=pk, entity_type=EntityType.BANK)

    @classmethod
    def from_serialized(cls, serialized: dict):
        return super().from_serialized(serialized, constructor_keys=["name"])
