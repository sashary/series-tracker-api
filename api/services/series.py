import typing
from datetime import datetime

from api.adapters.database import insert_series_to_db
from constants import DYNAMODB_SERIES_TABLE_NAME
from models.model_series import Series, SeriesTracking
from utils import generate_id


def get_series() -> typing.List[Series]:
    # query_series = _database.get_item({'type':'series'})
    series_a = Series(id="1", name="A series", description="With a description", created_at=datetime(2010,3,3), updated_at=datetime(2010,3,3))
    return [ series_a ]


def get_series_tracked() -> typing.List[SeriesTracking]:
    return [
        SeriesTracking(last_chapter_read=1, last_chapter_read_date=datetime(2010,3,3), series=get_series()[0])
    ]

def add_series(series_name: str, series_description: typing.Optional[str] = None) -> Series:
    created_at, updated_at = datetime.now(), datetime.now()
    series = Series(id=generate_id(), name=series_name, description=series_description, created_at=created_at, updated_at=updated_at)
    insert_series_to_db(series.to_db())
    return series
