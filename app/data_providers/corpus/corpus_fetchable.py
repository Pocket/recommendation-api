from abc import ABC, abstractmethod
from typing import List

from app.models.corpus_item_model import CorpusItemModel


class CorpusFetchable(ABC):
    @abstractmethod
    async def get_ranked_corpus_items(self, corpus_id: str, start_date: str, user_id) -> List[CorpusItemModel]:
        return NotImplemented
