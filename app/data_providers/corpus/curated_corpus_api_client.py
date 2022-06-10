import itertools
from typing import List

import requests
import json
from datetime import date

from app.data_providers.corpus.corpus_fetchable import CorpusFetchable
from app.models.corpus_item_model import CorpusItemModel


class CuratedCorpusAPIClient(CorpusFetchable):
    async def get_corpus_items(self, corpus_ids: [str]):
        # Fetch Corporeal Candidates
        aggregate_corpus_response = await gather(*(self.fetch(corpus_id) for corpus_id in corpus_ids))

        return list(itertools.chain(*aggregate_corpus_response))

    async def fetch(
            self,
            corpus_id: str = "NEW_TAB_EN_US",
    ) -> List[CorpusItemModel]:
        if not start_date:
            start_date = date.today().strftime("%Y-%m-%d")

        request_headers = {
            "apollographql-client-name": "recommendations-api",
            "apollographql-client-version": "1"
        }

        injection_protected_corpus_id = json.dumps(str(corpus_id))
        injection_protected_start_date = json.dumps(str(start_date))

        query = f"""
        query RecsApiItemRequest {{
            scheduledSurface(id: {injection_protected_corpus_id}) {{
                id
                items(date: {injection_protected_start_date}) {{
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
