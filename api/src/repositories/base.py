import src.db as db
from src.constants import table_name
from src.entities.base import Entity
from src.utils.serialization import DictSerialization


class Repository:
    def __init__(self, client=db.get_client(), table_name=table_name) -> None:
        self.client = client
        self.table = client.Table(table_name)

    def create(self, entity: Entity):
        serialized = DictSerialization.serialize(entity.to_dict())

        self.table.put_item(Item={**serialized})

    def update(self, entity):
        raise NotImplementedError

    def find_all(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError
