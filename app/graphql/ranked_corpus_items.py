from graphene_pydantic import PydanticObjectType

from app.models.ranked_corpus_items_instance import RankedCorpusItemsInstance
from app.models.slate import SlateModel
# This import needs to exist so that the below class can resolve its requisite model
from app.graphql.corpus_item import CorpusItem


class RankedCorpusItems(PydanticObjectType):
    class Meta:
        model = RankedCorpusItemsInstance