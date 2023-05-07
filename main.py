import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from api.mutations import Mutation
from api.queries import Query

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")