from graphene_pydantic import PydanticObjectType

from app.models.corpus_slate_instance import CorpusSlateInstance
from app.models.slate import SlateModel
# This import needs to exist before Slate so that the below class can resolve the recommendation model
from app.graphql.recommendation import Recommendation


class CorpusSlate(PydanticObjectType):
    class Meta:
        model = CorpusSlateInstance
