from typing import List

from pydantic import BaseModel

from app.models.corpus_recommendation_model import CorpusRecommendationModel
# If the CorpusRecommendation GraphQL model is not imported here, Graphene will raise a 'ConversionError'.
from app.graphql.corpus_recommendation import CorpusRecommendation


class CorpusSlateModel(BaseModel):
    """
    Models a corpus slate
    """
    id: str
    recommendations: List[CorpusRecommendationModel]
    headline: str
    subheadline: str = None
    more_link_url: str = None
    more_link_name: str = None


