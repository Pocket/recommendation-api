import uuid
import requests
import json
from datetime import date

from app.models.corpus_item_model import CorpusItemModel
from app.models.ranked_corpus_items_instance import RankedCorpusItemsInstance


class CurationAPIClient(object):
    @classmethod
    async def get_ranked_corpus_items(cls, corpus_id: str, start_date: str=None, user_id=None):
        ranked_corpus_items_id = "NEW_TAB_EN_US"
        if not start_date:
            start_date = date.today().strftime("%Y-%m-%d")

        query = f"""
        query Query {{
            scheduledSurface(id: "{ranked_corpus_items_id}") {{
                id
                items(date: "{start_date}") {{
                  id
                }}
            }}        
        }}
        """
        # Sounds like we want this to go directly to corpus API.
        # Let's talk to backend about this
        url = 'https://client-api.getpocket.com'
        response = requests.post(url, json={'query': query})
        response_body = json.loads(response.text)
        corpus_items = response_body.get("data").get("scheduledSurface").get("items")

        return RankedCorpusItemsInstance(
            id=str(uuid.UUID(int=sum([ord(char) for char in "IAmTheWalrus"]))),
            description="I am the corpus slate, coo coo ca choo",
            corpusItems = [CorpusItemModel(id=item.get('id')) for item in corpus_items],
        )