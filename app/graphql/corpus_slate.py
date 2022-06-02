from graphene_pydantic import PydanticObjectType

from app.models.corpus_slate_model import CorpusSlateModel


class CorpusSlate(PydanticObjectType):
    class Meta:
        model = CorpusSlateModel
