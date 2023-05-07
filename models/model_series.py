import typing
from datetime import datetime
from enum import Enum

import strawberry

from models.serializer import DBSerializer


@strawberry.enum
class SeriesMetaType(Enum):
    SERIES = 'series'
    SERIES_TRACKING = 'tracking'

@strawberry.type
class Series(DBSerializer):
    id: strawberry.ID
    name: str
    description: typing.Optional[str]
    created_at: datetime
    updated_at: datetime
    type: strawberry.Private[SeriesMetaType] = SeriesMetaType.SERIES

@strawberry.type
class SeriesTracking:
    series: Series
    last_chapter_read: typing.Optional[int]
    last_chapter_read_date: typing.Optional[datetime]
    type: strawberry.Private[SeriesMetaType] = SeriesMetaType.SERIES_TRACKING