from abc import ABC, abstractmethod
from typing import List

from app.models.corpus_item_model import CorpusItemModel


class CorpusFetchable(ABC):
    @abstractmethod
    async def get_corpus_items(self, corpus_ids: [str]) -> List[CorpusItemModel]:
        return NotImplemented
