from pydantic import BaseModel, Field

from app.models.recommendation_reason_type import RecommendationReasonType


class RecommendationReasonModel(BaseModel):
    """
    Models a reason for why a Corpus Recommendation was recommended
    """
    name: str = Field(description='A succinct name for the recommendation reason that can be displayed to the user.')
    type: RecommendationReasonType = Field(description='The type of reason for why the recommendation is made.')
