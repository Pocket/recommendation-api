from typing import List

from pydantic import BaseModel

from app.models.corpus_recommendation_model import CorpusRecommendationModel


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


