import src.db as db


class Repository:
    __client = db.get_client()
    __table_name = "bank_rates"

    @classmethod
    def create_table(cls):
        table = cls.__client.create_table(
            TableName=cls.__table_name,
            KeySchema=[
                {"AttributeName": "pk", "KeyType": "HASH"},
                {"AttributeName": "sk", "KeyType": "RANGE"},
            ],
            AttributeDefinitions=[
                {"AttributeName": "pk", "AttributeType": "S"},
                {"AttributeName": "sk", "AttributeType": "S"},
            ],
            BillingMode="PAY_PER_REQUEST",
        )
        table.wait_until_exists()

        return table

    @classmethod
    def find_all(cls):
        raise NotImplementedError

    @classmethod
    def create(cls, entity):
        raise

    @classmethod
    def update(cls):
        pass

    @classmethod
    def delete(cls):
        pass
