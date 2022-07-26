from datetime import datetime
from typing import List

from pydantic import BaseModel

from app.models.corpus_recommendation_model import CorpusRecommendationModel


class CorpusSlateModel(BaseModel):
    """
    Models a corpus slate
    """
    id: str
    recommendations: List[CorpusRecommendationModel]
    recommended_at: datetime  # UTC time when the slate was recommended
    headline: str
    subheadline: str = None
    more_link_url: str = None
    more_link_name: str = None


