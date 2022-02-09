from typing import List

from pydantic import BaseModel

from app.models.recommendation import RecommendationModel


class CorpusSlateInstance(BaseModel):
    """
    Models a corpus slate
    """
    id: str
    requestId: str = None
    experimentId: str = None
    display_name: str = None
    description: str = None
    recommendations: List[RecommendationModel] = None

