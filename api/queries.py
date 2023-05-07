import typing

import strawberry

from api.services.series import get_series, get_series_tracked
from models.model_series import Series, SeriesTracking


@strawberry.type
class Query:
    series: typing.List[Series] = strawberry.field(resolver=get_series)
    series_tracking: typing.List[SeriesTracking] = strawberry.field(resolver=get_series_tracked)
    