from typing import List

from pydantic import BaseModel

from app.models.corpus_item_model import CorpusItemModel

class RankedCorpusItemsInstance(BaseModel):
    """
    Models a corpus slate
    """
    id: str
    requestId: str = None
    experimentId: str = None
    display_name: str = None
    description: str = None
    corpusItems: List[CorpusItemModel] = None



