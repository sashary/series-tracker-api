import typing
from datetime import datetime
from enum import Enum

from utils import db_datetime_format


class DBSerializer:
    def to_db(cls) -> typing.Dict[str, typing.Any]:
        class_vars = {}
        for key, value in vars(cls).items():
            #TODO: refactor to a mapping function if it gets too large
            if isinstance(value, datetime):
                class_vars[key] = value.strftime(db_datetime_format)
            elif isinstance(value, Enum):
                class_vars[key] = value.value
            else:
                class_vars[key] = value
        return class_vars
