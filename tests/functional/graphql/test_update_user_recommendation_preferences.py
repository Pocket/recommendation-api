from datetime import datetime, timedelta

import pytest

from graphql.execution.executors.asyncio import AsyncioExecutor
from graphene.test import Client
from fastapi.testclient import TestClient

from app.data_providers.user_recommendation_preferences_provider import UserRecommendationPreferencesProvider
from app.graphql.graphql_router import schema
from app.main import app, load_slate_configs
from tests.assets.topics import populate_topics
from tests.functional.test_dynamodb_base import TestDynamoDBBase

from unittest.mock import patch
from collections import namedtuple

MockResponse = namedtuple('MockResponse', 'status')


class TestUpdateUserRecommendationPreferences(TestDynamoDBBase):
    client: Client

    async def asyncSetUp(self):
        await super().asyncSetUp()
        self.client = Client(schema)

    @patch('aiohttp.ClientSession.get', to_return=MockResponse(status=200))
    @patch.object(UserRecommendationPreferencesProvider, 'put')
    def test_update_user_recommendation_preferences(self, mock_data_provider_put, mock_client_session_get):
        topics = populate_topics(self.metadata_table)
        user_id = 'johnjacobjingleheimerschmidt'

        with TestClient(app):
            executed = self.client.execute(
                '''
                mutation Mutation($input: UpdateUserRecommendationPreferencesInput!) {
                  updateUserRecommendationPreferences(input: $input) {
                    preferredTopics {
                      id
                      name
                    }
                  }
                }
                ''',
                variables={
                    "input": {
                        "preferredTopics": [
                            {"id": "a187ffb4-5c6f-4079-bad9-92442e97bdd1"},
                        ]
                    }
                },
                context_value={'user_id': user_id},
                executor=AsyncioExecutor())

            response = executed.get('data').get('updateUserRecommendationPreferences')
            preferred_topics = response['preferredTopics']

            assert len(preferred_topics) == 1
            assert preferred_topics[0]['name'] == 'Technology'

            # Assert that the data provider was called with the right data.
            assert mock_data_provider_put.call_count == 1
            model_arg = mock_data_provider_put.call_args[0][0]
            assert model_arg.user_id == user_id
            self.assertAlmostEqual(model_arg.updated_at, datetime.utcnow(), delta=timedelta(minutes=1))
            assert len(model_arg.preferred_topics) == 1
            assert model_arg.preferred_topics[0].name == 'Technology'

