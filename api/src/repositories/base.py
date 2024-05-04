import src.db as db
from src.constants import table_name
from src.entities.base import Entity


class Repository:
    def __init__(self, client=db.get_client(), table_name=table_name) -> None:
        self.client = client
        self.table = client.Table(table_name)

    def create(self, entity: Entity):
        self.table.put_item(Item={**entity.serialize()})

    def update(self, entity):
        raise NotImplementedError

    def find_all(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError
