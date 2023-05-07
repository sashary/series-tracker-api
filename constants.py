import os

# AWS Configurations
AWS_REGION_NAME = os.environ.get("AWS_REGION_NAME", "us-east-1")
AWS_SIGNATURE_VERSION = os.environ.get("AWS_SIGNATURE_VERSION", "v4")
AWS_RETRIES_AMOUNT = int(os.environ.get("AWS_RETRIES_AMOUNT", 4))
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

# AWS Dynamodb
DYNAMODB_SERIES_TABLE_NAME = os.environ.get("DYNAMODB_SERIES_TABLE_NAME")
