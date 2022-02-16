from typing import List

from pydantic import BaseModel

from app.models.corpus_item_model import CorpusItemModel


class RankedCorpusSlateInstance(BaseModel):
    """
    Models a corpus slate
    """
    slateId: str
    requestId: str = None
    experimentId: str = None
    display_name: str = None
    description: str = None
    corpusSlate: List[CorpusItemModel] = None


