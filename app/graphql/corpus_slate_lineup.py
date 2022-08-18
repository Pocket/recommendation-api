from graphene_pydantic import PydanticObjectType
from graphene import List, Int

from app.graphql.corpus_slate import CorpusSlate
from app.models.corpus_slate_lineup_model import CorpusSlateLineupModel


class CorpusSlateLineup(PydanticObjectType):
    DEFAULT_COUNT = 10

    slates = List(CorpusSlate, required=True, count=Int(default_value=DEFAULT_COUNT))

    class Meta:
        model = CorpusSlateLineupModel
