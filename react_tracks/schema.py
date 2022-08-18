import graphene
import tracks.schema

class Query(tracks.schema.Query):
    pass


schema = graphene.Schema(query=Query)