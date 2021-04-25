import graphene
import graphqltest.schema

class Query(graphqltest.schema.Query, graphene.ObjectType):
    pass

class Mutation(graphqltest.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)