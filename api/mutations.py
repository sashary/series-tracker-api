import strawberry

from api.services.series import add_series_to_track
from models.model_series import SeriesTracking

@strawberry.type
class Mutation:
    add_series_to_track: SeriesTracking = strawberry.field(resolver=add_series_to_track)
    