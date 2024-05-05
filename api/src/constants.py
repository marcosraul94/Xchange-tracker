import os
from src.enums import Environment


table_name = "exchange_tracker"

migrations_path = os.path.join(os.getcwd(), "migrations")

environment = os.getenv("ENVIRONMENT", Environment.TEST.value)

# DynamoDB config
dynamo_endpoint = os.getenv("DYNAMO_ENDPOINT")
aws_region = os.getenv("AWS_REGION")
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
