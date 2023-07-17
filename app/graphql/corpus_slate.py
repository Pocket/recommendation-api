from typing import Optional

import strawberry

from app.graphql.link import Link  # noqa: This import is required for Strawberry to register `Link`
from app.graphql.recommendation_reason_type import RecommendationReasonType
from app.graphql.resolvers.corpus_slate_recommendations_resolver import corpus_slate_recommendations_resolver
from app.models.corpus_slate_model import CorpusSlateModel


@strawberry.experimental.pydantic.type(
    model=CorpusSlateModel,
    description='This is the same as Slate but in this type all recommendations are backed by CorpusItems. '
                'This means that the editorial team has editorial control over the items served by this endpoint.')
class CorpusSlate:
    id: strawberry.ID
    headline: strawberry.auto
    subheadline: strawberry.auto
    recommendations: strawberry.auto = strawberry.field(
        resolver=corpus_slate_recommendations_resolver,
        description='Recommendations for the current request context.')
    recommendation_reason_type: Optional[RecommendationReasonType]
    more_link: strawberry.auto
    utm_source: strawberry.auto
