import boto3
import src.env as env

_db = None


def get_client():
    global _db

    if not _db:
        _db = boto3.resource(
            "dynamodb",
            endpoint_url=env.dynamo_endpoint,
            region_name=env.aws_region,
            aws_access_key_id=env.aws_access_key_id,
            aws_secret_access_key=env.aws_secret_access_key,
        )

    return _db
