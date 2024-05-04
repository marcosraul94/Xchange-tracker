from datetime import datetime, UTC
from enum import Enum
from src.constants import EntityType


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

    def serialize(self):
        serialized = {}

        for key, value in self.to_dict().items():
            if isinstance(value, datetime):
                serialized[key] = value.isoformat()
            elif isinstance(value, Enum):
                serialized[key] = value.value
            else:
                serialized[key] = value

        return serialized

    @classmethod
    def from_serialized(cls, entity: dict):
        kwargs = {}

        for key, value in entity.items():
            if key in ["created_at", "updated_at"]:
                kwargs[key] = datetime.fromisoformat(value)
            elif key == "entity_type":
                kwargs[key] = EntityType(value)
            else:
                kwargs[key] = value

        return cls(**kwargs)

    def __eq__(self, value: "Entity") -> bool:
        return self.to_dict() == value.to_dict()
