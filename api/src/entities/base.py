from datetime import datetime, UTC
from src.constants import EntityType
from src.utils.serialization import DictSerialization


class Entity:
    def __init__(
        self,
        pk: str,
        sk: str,
        entity_type: EntityType,
        created_at: datetime = None,
        updated_at: datetime = None,
    ):
        self.pk = pk
        self.sk = sk
        self.entity_type = entity_type

        now = datetime.now(UTC)
        self.created_at = created_at or now
        self.updated_at = updated_at or now

    def to_dict(self):
        return {
            key: getattr(self, key)
            for key in dir(self)
            if not key.startswith("_") and not callable(getattr(self, key))
        }

    @classmethod
    def from_serialized(cls, serialized: dict):
        kwargs = DictSerialization.deserialize(serialized)

        return cls(**kwargs)

    def __eq__(self, value: "Entity") -> bool:
        return self.to_dict() == value.to_dict()
