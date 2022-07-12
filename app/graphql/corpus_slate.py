from graphene_pydantic import PydanticObjectType
from graphene import List, Int

from app.graphql.corpus_recommendation import CorpusRecommendation
from app.models.corpus_slate_model import CorpusSlateModel


class CorpusSlate(PydanticObjectType):
    DEFAULT_COUNT = 10

    recommendations = List(CorpusRecommendation, required=True, count=Int(default_value=DEFAULT_COUNT))

    class Meta:
        model = CorpusSlateModel
