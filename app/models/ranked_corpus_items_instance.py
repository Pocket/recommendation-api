from typing import List

from pydantic import BaseModel

from app.models.recommendation import RecommendationModel


class RankedCorpusItemsInstance(BaseModel):
    """
    Models a corpus slate
    """
    id: str
    requestId: str = None
    experimentId: str = None
    display_name: str = None
    description: str = None
    corpusItems: List[RecommendationModel] = None


