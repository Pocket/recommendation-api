import strawberry

from app.graphql.resolvers.corpus_slate_lineup_slates_resolver import corpus_slate_lineup_slates_resolver
from app.models.corpus_slate_lineup_model import CorpusSlateLineupModel


@strawberry.experimental.pydantic.type(model=CorpusSlateLineupModel, description='A collection of slates.')
class CorpusSlateLineup:
    id: strawberry.ID
    slates: strawberry.auto = strawberry.field(resolver=corpus_slate_lineup_slates_resolver, description='Slates.')
