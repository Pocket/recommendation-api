from graphene_pydantic import PydanticObjectType

from app.models.corpus_recommendation_model import CorpusRecommendationModel


class CorpusRecommendation(PydanticObjectType):
    class Meta:
        model = CorpusRecommendationModel
