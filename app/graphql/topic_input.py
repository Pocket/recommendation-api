import graphene


class TopicInput(graphene.InputObjectType):
    id = graphene.ID(required=True)
