import strawberry

from app.models.corpus_slate_lineup_model import CorpusSlateLineupModel


@strawberry.experimental.pydantic.type(model=CorpusSlateLineupModel, description='A collection of slates.')
class CorpusSlateLineup:
    DEFAULT_COUNT = 10

    id: strawberry.ID
    slates: strawberry.auto
