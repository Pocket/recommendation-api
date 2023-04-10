import strawberry

from app.graphql.corpus_item import CorpusItem  # noqa: This import is required for Strawberry to register `CorpusItem`
from app.graphql.recommendation_reason import RecommendationReason  # noqa
from app.models.corpus_recommendation_model import CorpusRecommendationModel


@strawberry.experimental.pydantic.type(model=CorpusRecommendationModel)
class CorpusRecommendation:
    id: strawberry.ID
    # GraphQL Int is limited to 32-bit, so tile_id is converted from int to float here to support values up to 2^53.
    tile_id: float = strawberry.field(
        deprecation_reason='Only to be used by Firefox. Other clients should use `id`. We plan to also migrate Firefox '
                           'New Tab to use CorpusRecommendation.id instead of tileId to track recommendation telemetry.'
    )
    corpus_item: strawberry.auto
    reason: strawberry.auto
