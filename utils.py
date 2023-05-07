import uuid

db_datetime_format = "%Y-%m-%dT%H:%M:%S.000Z"

def generate_id():
    return str(uuid.uuid4())