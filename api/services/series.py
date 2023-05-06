from models.model_series import Series, SeriesTracking
from datetime import datetime
import typing

def get_series() -> typing.List[Series]:
    return [
        Series(id="1", name="A series", description="With a description", created_at=datetime(2010,3,3), updated_at=datetime(2010,3,3))
    ]


def get_series_tracked() -> typing.List[SeriesTracking]:
    return [
        SeriesTracking(last_chapter_read=1, last_chapter_read_date=datetime(2010,3,3), series=get_series()[0])
    ]

def add_series_to_track(series_id: str, last_chapter_read: typing.Optional[int] = None) -> SeriesTracking:
    series = [series for series in get_series() if series.id == series_id][0]
    return SeriesTracking(series=series, last_chapter_read=last_chapter_read, last_chapter_read_date=datetime(2010,3,3))