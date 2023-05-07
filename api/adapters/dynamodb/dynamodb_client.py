import functools

import boto3
from boto3.dynamodb.conditions import Attr, Key
from botocore.config import Config

from constants import (AWS_ACCESS_KEY_ID, AWS_REGION_NAME, AWS_RETRIES_AMOUNT,
                       AWS_SECRET_ACCESS_KEY, AWS_SIGNATURE_VERSION)


class DatabaseTable:
    #TODO: Handle error states
    def __init__(self, table_name) -> None:
        config = Config(
            region_name = AWS_REGION_NAME,
            signature_version = AWS_SIGNATURE_VERSION,
            #  AWS_ACCESS_KEY_ID : assigned automatically in env var
            # AWS_SECRET_ACCESS_KEY : assigned automatically in env var
            retries = {
                'max_attempts': AWS_RETRIES_AMOUNT,
                'mode': 'standard'
            }
        )
        dynamodb = boto3.resource('dynamodb', config=config)

        self.table = dynamodb.Table(table_name)

    def _pre_check_keys(func):
        @functools.wraps(func)
        def wrapper_verify_dict(*args, **kwargs):
            if(not args[1].get("id")):
                raise KeyError("Required field id not found when inserting item to DB")
            elif (not args[1].get("type")):
                raise KeyError("Required field type not found inserting item to DB")
            return func(*args, **kwargs)
        return wrapper_verify_dict

    def tracker_table(self):
        return self.table

    @_pre_check_keys
    def put_item(self, item_dict: dict):
        inserted_item = self.table.put_item(
            Item=item_dict
        )
        return {"status_code": inserted_item['ResponseMetadata']['HTTPStatusCode'], "metadata": inserted_item['ResponseMetadata']}
    
    def get_item(self, id: str, type: str):
        response = self.table.get_item(
            Key={"id": id, 'type': type}
        )
        return response['Item']
    
    def scan_for_items(self, filter_expression):
        response = self.table.query(
            filter_expression
        )
        return response['Items']

    # def update_and_get_item(self, **keys, update_expression, expression_attributes):
    #     update_item = self.table.update_item(
    #         Key=keys
    #     )
