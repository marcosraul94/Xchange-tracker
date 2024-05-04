from datetime import datetime
from src.entities.base import Entity
from src.constants import EntityType


class Migration(Entity):
    def __init__(
        self,
        name: str,
        pk: str = "m#",
        sk: str = None,
        entity_type: EntityType = EntityType.MIGRATION,
        created_at: datetime = None,
        updated_at: datetime = None,
    ):
        sk = sk or f"{pk}{name}"
        super().__init__(pk, sk, entity_type, created_at, updated_at)
        self.name = name
