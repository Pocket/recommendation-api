import random
import uuid

from graphql.execution.executors.asyncio import AsyncioExecutor
from graphene.test import Client
from fastapi.testclient import TestClient

from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.graphql.graphql_router import schema
from app.main import app
from app.models.corpus_item_model import CorpusItemModel
from tests.functional.test_dynamodb_base import TestDynamoDBBase

from unittest.mock import patch
from collections import namedtuple

MockResponse = namedtuple('MockResponse', 'status')


class TestSetupMomentSlate(TestDynamoDBBase):
    client: Client

    async def asyncSetUp(self):
        await super().asyncSetUp()
        self.client = Client(schema)

    @patch('aiohttp.ClientSession.get', to_return=MockResponse(status=200))
    @patch.object(CorpusFeatureGroupClient, 'get_ranked_corpus_items')
    def test_setup_moment_slate(self, mock_get_ranked_corpus_items, mock_client_session_get):
        corpus_items_fixture = self._get_corpus_items_fixture()
        mock_get_ranked_corpus_items.return_value = corpus_items_fixture

        with TestClient(app):
            executed = self.client.execute(
                '''
                query SetupMomentSlate {
                  setupMomentSlate {
                    headline
                    subheadline
                    recommendations {
                      id
                      corpusItem {
                        id
                      }
                    }
                  }
                }
                ''',
                context_value={'user_id': 'johnjacobjingleheimerschmidt'},
                executor=AsyncioExecutor())

            response = executed.get('data').get('setupMomentSlate')
            assert response['headline'] == 'Save an article you find interesting'

            # Currently, CorpusItems from the Feature Group are returned in the same order.
            recs = response['recommendations']
            assert len(recs) == 30  # top-30 ranker is applied
            assert [rec['corpusItem']['id'] for rec in recs] == [item.id for item in corpus_items_fixture][:30]

    def _get_corpus_items_fixture(self, n=100) -> [CorpusItemModel]:
        corpus_topics = ["HEALTH_FITNESS", "SELF_IMPROVEMENT", "FOOD", "SELF_IMPROVEMENT", "TRAVEL"]
        return [CorpusItemModel(id=uuid.uuid4().hex, topic=random.choice(corpus_topics)) for _ in range(n)]
