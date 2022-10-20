import strawberry

from app.graphql.recommendation_reason_type import RecommendationReasonType
from app.models.recommendation_reason_model import RecommendationReasonModel


@strawberry.experimental.pydantic.type(model=RecommendationReasonModel)
class RecommendationReason:
    name: strawberry.auto
    type: RecommendationReasonType
