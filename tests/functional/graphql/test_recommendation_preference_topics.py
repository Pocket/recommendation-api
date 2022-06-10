import pytest

from graphql.execution.executors.asyncio import AsyncioExecutor
from graphene.test import Client
from fastapi.testclient import TestClient

from app.graphql.graphql_router import schema
from app.main import app, load_slate_configs
from tests.assets.topics import populate_topics
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
    def test_setup_moment_slate(self, mock_client_session_get):
        populate_topics(self.metadata_table)

        with TestClient(app):
            executed = self.client.execute(
                '''
                query RecommendationPreferenceTopics {
                  recommendationPreferenceTopics {
                    id
                    name
                  }
                }
                ''',
                executor=AsyncioExecutor())

            response = executed.get('data').get('recommendationPreferenceTopics')

            # 'Gaming' is filtered out, so the only topic remaining is 'Technology'.
            assert len(response) == 1
            assert response[0]['name'] == 'Technology'
