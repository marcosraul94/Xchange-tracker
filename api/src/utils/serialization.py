from decimal import Decimal
from datetime import datetime
from src.constants import EntityType


class DatetimeSerialization:
    @classmethod
    def serialize(cls, value: datetime) -> str:
        return value.isoformat()

    @classmethod
    def deserialize(cls, value: str) -> datetime:
        return datetime.fromisoformat(value)


class EntityTypeSerialization:
    @classmethod
    def serialize(cls, value: EntityType) -> str:
        return value.value

    @classmethod
    def deserialize(cls, value: str) -> EntityType:
        return EntityType(value)


class DecimalSerialization:
    @classmethod
    def serialize(cls, value: Decimal) -> str:
        return str(value)

    @classmethod
    def deserialize(cls, value: str) -> Decimal:
        return Decimal(value)


class DictSerialization:
    @classmethod
    def serialize(cls, value: dict) -> dict:
        serialized = {}

        for k, v in value.items():
            if isinstance(v, datetime):
                serialized[k] = DatetimeSerialization.serialize(v)
            elif isinstance(v, EntityType):
                serialized[k] = EntityTypeSerialization.serialize(v)
            elif isinstance(v, Decimal):
                serialized[k] = DecimalSerialization.serialize(v)
            else:
                serialized[k] = v

        return serialized

    @classmethod
    def deserialize(cls, value: dict) -> dict:
        deserialized = {}

        for k, v in value.items():
            if k in ["created_at", "updated_at"]:
                deserialized[k] = DatetimeSerialization.deserialize(v)
            elif k == "amount":
                deserialized[k] = DecimalSerialization.deserialize(v)
            elif k == "entity_type":
                deserialized[k] = EntityTypeSerialization.deserialize(v)
            else:
                deserialized[k] = v

        return deserialized
