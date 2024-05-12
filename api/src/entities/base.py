from datetime import datetime, UTC
from src.enums import EntityType
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
    def from_serialized(
        cls,
        serialized: dict,
        constructor_keys=None,
        post_creation_keys=["created_at", "updated_at"],
    ):
        props = DictSerialization.deserialize(serialized)
        constructor_keys = (
            props
            if not constructor_keys
            else {k: v for k, v in props.items() if k in constructor_keys}
        )

        instance = cls(**constructor_keys)

        for k in post_creation_keys:
            setattr(instance, k, props[k])

        return instance

    def __eq__(self, value: "Entity") -> bool:
        if not isinstance(value, self.__class__):
            return False

        return self.to_dict() == value.to_dict()

    def __hash__(self):
        return hash(f"{self.pk}-{self.sk}")

    def __repr__(self) -> str:
        cls_name = self.__class__.__name__
        key_values = ", ".join(f"{k}={v}" for k, v in self.to_dict().items())

        return f"{cls_name}({key_values})"
