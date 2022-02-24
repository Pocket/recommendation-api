import uuid
from abc import ABC, abstractmethod
from typing import List

import requests
import json
from datetime import date

from app.graphql.corpus_item import CorpusItem
from app.models.corpus_item_model import CorpusItemModel
from app.models.ranked_corpus_items_instance import RankedCorpusItemsInstance

class CurationAPIFetchable(ABC):
    @abstractmethod
    async def get_ranked_corpus_slate(self, corpus_id: str, start_date: str, user_id) -> List[CorpusItem]:
        return NotImplemented

class CurationAPIClient(CurationAPIFetchable):
    async def get_ranked_corpus_slate(self, corpus_id: str = "NEW_TAB_EN_US", start_date: str=None, user_id=None) -> List[CorpusItem]:
        if not start_date:
            start_date = date.today().strftime("%Y-%m-%d")

        request_headers = {
            "apollographql-client-name": "recommendations-api",
            "apollographql-client-version": "1"
        }

        query = f"""
        query RecsApiItemRequest {{
            scheduledSurface(id: {json.dumps(str(corpus_id))}) {{
                id
                items(date: {json.dumps(str(start_date))}) {{
                  id
                }}
            }}        
        }}
        """
        # Sounds like we want this to go directly to corpus API.
        # Let's talk to backend about this
        url = 'https://client-api.getpocket.com'
        response = requests.post(url, headers=request_headers, json={'query': query})
        response_body = json.loads(response.text)
        corpus_items = response_body.get("data").get("scheduledSurface").get("items")

        return corpus_items
