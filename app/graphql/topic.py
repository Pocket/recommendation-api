from graphene_pydantic import PydanticObjectType
from app.models.topic import TopicModel


class Topic(PydanticObjectType):
    class Meta:
        model = TopicModel
