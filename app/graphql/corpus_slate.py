import strawberry

from app.graphql.resolvers.corpus_slate_recommendations_resolver import corpus_slate_recommendations_resolver
from app.models.corpus_slate_model import CorpusSlateModel


@strawberry.experimental.pydantic.type(model=CorpusSlateModel)
class CorpusSlate:
    id: strawberry.ID
    headline: strawberry.auto
    subheadline: strawberry.auto
    recommendations: strawberry.auto = strawberry.field(
        resolver=corpus_slate_recommendations_resolver,
        description='Recommendations for the current request context.')
