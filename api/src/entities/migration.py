from src.entities.base import Entity
from src.constants import EntityType
from src.utils.serialization import DictSerialization


class Migration(Entity):
    def __init__(self, name: str):
        pk = "m#"
        sk = f"{pk}{name}"
        entity_type = EntityType.MIGRATION

        self.name = name
        super().__init__(pk, sk, entity_type)

    @classmethod
    def from_serialized(cls, serialized: dict):
        deserialized = DictSerialization.deserialize(serialized)
        instance = Migration(deserialized["name"])
        instance.created_at = deserialized["created_at"]
        instance.updated_at = deserialized["updated_at"]

        return instance
