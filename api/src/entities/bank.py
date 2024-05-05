from src.entities.base import Entity
from src.constants import EntityType


class Bank(Entity):
    def __init__(self, name: str):
        pk = "b#"
        sk = f"{pk}{name}"
        entity_type = EntityType.BANK

        self.name = name
        super().__init__(pk, sk, entity_type)
