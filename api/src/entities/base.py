from attrs import define, asdict
from datetime import datetime


@define
class Entity:
    id: str
    created_at: datetime
    updated_at: datetime
    entity_type: str = None

    def to_dict(self):
        return asdict(self)
