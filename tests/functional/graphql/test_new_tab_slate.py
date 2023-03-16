import random
import uuid
from unittest.mock import patch

from asgi_lifespan import LifespanManager
from httpx import AsyncClient

from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.data_providers.feature_group.feature_group_client import FeatureGroupClient
from app.data_providers.slate_providers.new_tab_slate_provider import MIN_TILE_ID, MAX_TILE_ID
from app.main import app
from app.models.corpus_item_model import CorpusItemModel
from tests.assets.topics import *
from tests.functional.test_dynamodb_base import TestDynamoDBBase


def _corpus_items_fixture(n: int) -> [CorpusItemModel]:
    corpus_topic_ids = [t.corpus_topic_id for t in all_topic_fixtures]
    return [CorpusItemModel(id=str(uuid.uuid4()), topic=random.choice(corpus_topic_ids)) for _ in range(n)]


def _format_new_tab_query(locale, region, count=50):
    return '''
        query {
          newTabSlate(locale: "%(locale)s", region: "%(region)s") {
            recommendations(count: %(count)d) {
              tileId
              corpusItem {
                id
              }
            }
          }
        }
    ''' % {'locale': locale, 'region': region, 'count': count}


class TestNewTabSlate(TestDynamoDBBase):
    async def asyncSetUp(self):
        await super().asyncSetUp()
        self.headers = {
            'apiId': '94110',
            'consumerKey': 'fx-client-consumer-key',
            'applicationName': 'Firefox',
            'applicationIsNative': 'true',
            'applicationIsTrusted': 'true',
        }

    @patch.object(CorpusFeatureGroupClient, 'fetch')
    async def test_new_tab_slate_italy(
            self,
            mock_fetch_corpus_items
    ):
        corpus_items_fixture = _corpus_items_fixture(n=100)
        mock_fetch_corpus_items.return_value = corpus_items_fixture

        async with AsyncClient(app=app, base_url="http://test") as client, LifespanManager(app):
            requested_recommendation_count = 50
            query = _format_new_tab_query(locale='it-IT', region='IT', count=requested_recommendation_count)
            response = await client.post('/', json={'query': query}, headers=self.headers)
            data = response.json()

            assert not data.get('errors')
            recommendations = data['data']['newTabSlate']['recommendations']

            # Assert that the expected number of slates is being returned.
            assert len(recommendations) == requested_recommendation_count
            # Assert that all tileId are unique integers in range [MIN_TILE_ID, MAX_TILE_ID)
            tile_ids = [r['tileId'] for r in recommendations]
            assert all(MIN_TILE_ID <= tile_id < MAX_TILE_ID for tile_id in tile_ids)
            assert all(int(tile_id) == tile_id for tile_id in tile_ids)
            assert len(set(tile_ids)) == len(tile_ids)
