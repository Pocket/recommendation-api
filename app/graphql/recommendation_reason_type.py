from enum import Enum

import strawberry
from app.models.recommendation_reason_type import RecommendationReasonType as RecommendationReasonTypeModel


@strawberry.enum(description='Reasons why recommendations are made. Focuses on client needs and is not exhaustive.')
class RecommendationReasonType(Enum):
    """
    This enum mirrors app.models.recommendation_reason_type.RecommendationReasonType

    Strawberry does not seem to handle Pydantic models with Enums well. As a workaround, redefine the Enum with
    @strawberry.enum.
    """

    POCKET_HITS = strawberry.enum_value(
        RecommendationReasonTypeModel.POCKET_HITS.value,
        description='Recommendations are sourced from the Pocket Hits newsletter.'
    )

    PREFERRED_TOPICS = strawberry.enum_value(
        RecommendationReasonTypeModel.PREFERRED_TOPICS.value,
        description='Recommendations that match the user\'s topic preferences are ranked higher.'
    )

    HYBRID_CF_RECOMMENDER = strawberry.enum_value(
        RecommendationReasonTypeModel.HYBRID_CF_RECOMMENDER.value,
        description='Recommendations based on hybrid collaborative filtering.'
    )
