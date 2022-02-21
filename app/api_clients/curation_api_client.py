import uuid
import requests
import json
from datetime import date, datetime

from app.exceptions.invalid_date_exception import InvalidDateException
from app.models.corpus_item_model import CorpusItemModel
from app.models.ranked_corpus_slate_instance import RankedCorpusSlateInstance


class CurationAPIClient(object):
    @classmethod
    async def get_ranked_corpus_slate(cls, slate_id: str, start_date: str=None, user_id=None):
        ranked_corpus_slate_id = "NEW_TAB_EN_US"

        if start_date:
            try:
                datetime.strptime(start_date, "%Y-%m-%d")
            except ValueError:
                raise InvalidDateException("Invalid date argument. Date must be formatted year-month-day like so: 1981-09-04")

        if not start_date:
            start_date = date.today().strftime("%Y-%m-%d")

        request_headers = {
            "apollographql-client-name": "recommendations-api",
            "apollographql-client-version": "1"
        }
        query = f"""
        query RecsApiItemRequest {{
            scheduledSurface(id: "{ranked_corpus_slate_id}") {{
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
        response = requests.post(url, headers=request_headers, json={'query': query})
        response_body = json.loads(response.text)
        corpus_slate = response_body.get("data").get("scheduledSurface").get("items")

        return RankedCorpusSlateInstance(
            slateId=str(uuid.UUID(int=sum([ord(char) for char in "IAmTheWalrus"]))),
            description="I am the corpus slate, coo coo ca choo",
            corpusSlate = [CorpusItemModel(id=item.get('id')) for item in corpus_slate],
        )