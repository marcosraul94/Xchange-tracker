import src.db as db
from src.constants import table_name, entity_type_gsi
from src.entities.base import Entity
from src.utils.serialization import DictSerialization


class Repository:
    def __init__(
        self,
        client=db.get_client(),
        table_name=table_name,
        entity_type_gsi=entity_type_gsi,
    ) -> None:
        self.client = client
        self.table_name = table_name
        self.entity_type_index_name = entity_type_gsi

    @property
    def table(self):
        return self.client.Table(self.table_name)

    def create(self, entity: Entity):
        serialized = DictSerialization.serialize(entity.to_dict())

        self.table.put_item(Item={**serialized})

    def update(self, entity):
        raise NotImplementedError

    def find_all(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError
