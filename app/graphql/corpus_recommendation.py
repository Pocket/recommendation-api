import strawberry

from app.graphql.corpus_item import CorpusItem  # noqa: This import is required for Strawberry to register `CorpusItem`
from app.graphql.recommendation_reason import RecommendationReason  # noqa
from app.models.corpus_recommendation_model import CorpusRecommendationModel


@strawberry.experimental.pydantic.type(model=CorpusRecommendationModel)
class CorpusRecommendation:
    id: strawberry.ID
    tile_id: strawberry.auto = strawberry.field(
        deprecation_reason='Only to be used by Firefox. Other clients should use `id`.')
    corpus_item: strawberry.auto
    reason: strawberry.auto
