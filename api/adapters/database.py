from api.adapters.dynamodb.dynamodb_client import DatabaseTable
from constants import DYNAMODB_SERIES_TABLE_NAME

_database = DatabaseTable(table_name=DYNAMODB_SERIES_TABLE_NAME)

def get_all_series():
    _database

def insert_series_to_db(series: dict):
    return _database.put_item(series)