from abc import ABC, abstractmethod
from typing import List

from app.graphql.corpus_item import CorpusItem


class CorpusFetchable(ABC):
    @abstractmethod
    async def get_ranked_corpus_items(self, corpus_id: str, start_date: str, user_id) -> List[CorpusItem]:
        return NotImplemented
