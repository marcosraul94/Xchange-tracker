import src.db as db
from src.constants import table_name, entity_type_gsi
from src.entities.base import Entity
from src.utils.serialization import DictSerialization


class Repository:
    entity: Entity = Entity

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

    def deserialize_items(self, response):
        items = response.get("Items", [])

        return [self.entity.from_serialized(item) for item in items]

    def create(self, entity: Entity):
        self.create_all([entity])

    def create_all(self, entities: list[Entity]):
        with self.table.batch_writer() as batch:
            for entity in entities:
                serialized = DictSerialization.serialize(entity.to_dict())
                batch.put_item(Item={**serialized})
