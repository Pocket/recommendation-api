import graphene

from graphene_pydantic import PydanticObjectType
from graphene_federation import external, extend

from app.models.corpus_item_model import CorpusItemModel

@extend(fields='id')
class CorpusItem(PydanticObjectType):
    id = external(graphene.String(required=True))

    class Meta:
        model = CorpusItemModel

