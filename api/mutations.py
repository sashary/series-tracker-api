import strawberry

from api.services.series import add_series
from models.model_series import Series


@strawberry.type
class Mutation:
    add_series: Series = strawberry.field(resolver=add_series)
    