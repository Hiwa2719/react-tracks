import graphene

import tracks.schema
import users.schema


class Query(
    users.schema.Query,
    tracks.schema.Query,
):
    pass


class Mutation(users.schema.Mutation,
               tracks.schema.Mutation,
               ):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
