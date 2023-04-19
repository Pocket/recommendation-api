import itertools
from datetime import datetime, timedelta
from typing import List, Dict

import pytz

from app.data_providers.PocketGraphClientSession import PocketGraphClientSession
from app.data_providers.corpus.corpus_fetchable import CorpusFetchable
from app.models.corpus_item_model import CorpusItemModel


class CorpusApiClient(CorpusFetchable):
    _corpus_item_scheduled_date: Dict[str, str] = {}  # Maps CorpusItem.id to scheduledDate

    def __init__(self, pocket_graph_client_session: PocketGraphClientSession):
        self.pocket_graph_client_session = pocket_graph_client_session

    async def fetch(
            self,
            corpus_id: str,
    ) -> List[CorpusItemModel]:
        query = """
            query ScheduledSurface($scheduledSurfaceId: ID!, $date_today: Date!, $date_yesterday: Date!) {
              scheduledSurface(id: $scheduledSurfaceId) {
                items_today:     items(date: $date_today)     { corpusItem { id topic } scheduledDate }
                items_yesterday: items(date: $date_yesterday) { corpusItem { id topic } scheduledDate }
              }
            }
        """

        # The date is supposed to progress at midnight EST.
        today = datetime.now(tz=pytz.timezone('America/New_York'))
        yesterday = today - timedelta(days=1)

        body = {
            'query': query,
            'variables': {
              'scheduledSurfaceId': corpus_id,
              'date_today': today.strftime('%Y-%m-%d'),
              'date_yesterday': yesterday.strftime('%Y-%m-%d'),
            }
        }

        async with self.pocket_graph_client_session.post(url='/', json=body, raise_for_status=True) as resp:
            response_json = await resp.json()
            scheduled_surface = response_json['data']['scheduledSurface']
            all_items = itertools.chain(scheduled_surface['items_today'], scheduled_surface['items_yesterday'])

            corpus_items = []
            for item in all_items:
                corpus_item: CorpusItemModel = CorpusItemModel.parse_obj(item['corpusItem'])
                corpus_items.append(corpus_item)
                self._corpus_item_scheduled_date[corpus_item.id] = item['scheduledDate']

        return corpus_items

    def get_scheduled_date(self, corpus_item_id: str) -> str:
        """
        After fetch() is called, this returns the scheduled date for the given CorpusItem.id.
        :return: Date string in format YYYY-MM-DD.
        """
        return self._corpus_item_scheduled_date.get(corpus_item_id)
