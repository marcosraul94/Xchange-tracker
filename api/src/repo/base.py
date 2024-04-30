from api.src.db import DynamoDB


class Repository:
    __client = DynamoDB().client
    __table = 'tracker'

    @classmethod
    def find_all(cls):
        cls.__client.

    @classmethod
    def create(cls):
        pass

    @classmethod
    def update(cls):
        pass

    @classmethod
    def delete(cls):
        pass
