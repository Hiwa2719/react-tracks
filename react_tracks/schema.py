import graphene
import tracks.schema


class Query(tracks.schema.Query):
    pass


class Mutation(tracks.schema.Mutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
