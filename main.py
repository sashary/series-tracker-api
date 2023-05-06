from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter

from api.queries import Query
from api.mutations import Mutation
    
schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")