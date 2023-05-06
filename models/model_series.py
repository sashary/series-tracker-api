import strawberry
import typing
from datetime import datetime

@strawberry.type
class Series:
    id: strawberry.ID
    name: str
    description: str
    created_at: datetime
    updated_at: datetime

@strawberry.type
class SeriesTracking:
    series: Series
    last_chapter_read: typing.Optional[int]
    last_chapter_read_date: typing.Optional[datetime]