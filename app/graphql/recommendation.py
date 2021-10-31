import strawberry

from app.models.recommendation import RecommendationModel


@strawberry.federation.type(extend=False, keys=["itemId"])
@strawberry.experimental.pydantic.type(model=RecommendationModel, all_fields=True)
class Recommendation:
    pass
