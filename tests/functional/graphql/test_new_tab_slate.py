import random
import uuid
from unittest.mock import patch

from asgi_lifespan import LifespanManager
from httpx import AsyncClient

from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.data_providers.feature_group.feature_group_client import FeatureGroupClient
from app.data_providers.snowplow.config import SnowplowConfig
from app.main import app
from app.models.corpus_item_model import CorpusItemModel
from app.models.request_user import RequestUser
from tests.assets.topics import *
from tests.functional.test_dynamodb_base import TestDynamoDBBase
from tests.functional.test_util.snowplow import SnowplowMicroClient


def _corpus_items_fixture(n: int) -> [CorpusItemModel]:
    corpus_topic_ids = [t.corpus_topic_id for t in all_topic_fixtures]
    return [CorpusItemModel(id=str(uuid.uuid4()), topic=random.choice(corpus_topic_ids)) for _ in range(n)]


def _format_new_tab_query(locale, region, count=50):
    return '''
        query {
          newTabSlate(locale: "%(locale)s") {
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
        self.request_user = RequestUser(
            user_id=1,
            hashed_user_id='1-hashed',
        )
        self.headers = {
            'userId': str(self.request_user.user_id),
            'encodedId': self.request_user.hashed_user_id,
            'apiId': '94110',
            'consumerKey': 'web-client-consumer-key',
            'applicationName': 'Pocket web-client',
            'applicationIsNative': 'true',
            'applicationIsTrusted': 'true',
        }

        populate_topics(self.metadata_table)
        self.snowplow_micro = SnowplowMicroClient(config=SnowplowConfig())
        self.snowplow_micro.reset_snowplow_events()

    @patch.object(CorpusFeatureGroupClient, 'fetch')
    @patch.object(FeatureGroupClient, 'batch_get_records')
    async def test_new_tab_slate_italy(
            self,
            mock_batch_get_records,
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
            assert all(r['tileId'] > 100000 for r in recommendations)
