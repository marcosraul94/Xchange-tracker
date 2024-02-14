from src.db import DynamoDB

dynamodb = DynamoDB()


def handler(event, context):
    print(list(dynamodb.client.tables.all()))
