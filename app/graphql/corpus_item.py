import strawberry

from app.models.corpus_item_model import CorpusItemModel


@strawberry.federation.type(keys=["id"])
@strawberry.experimental.pydantic.type(model=CorpusItemModel)
class CorpusItem:
    id: strawberry.ID
    topic: strawberry.auto
