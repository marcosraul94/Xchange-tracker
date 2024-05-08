import os
import logging
from src.enums import Environment


table_name = "exchange_tracker"
entity_type_gsi = "entity_type_gsi"
migrations_path = os.path.join(os.getcwd(), "migrations")

environment = os.getenv("ENVIRONMENT", Environment.DEV.value)
log_level = os.getenv("LOG_LEVEL", logging.DEBUG)

# DynamoDB config
dynamo_endpoint = os.getenv("DYNAMO_ENDPOINT")
aws_region = os.getenv("AWS_REGION")
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
