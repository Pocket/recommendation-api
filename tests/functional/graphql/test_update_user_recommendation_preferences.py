from graphql.execution.executors.asyncio import AsyncioExecutor
from graphene.test import Client
from fastapi.testclient import TestClient

from app.data_providers.user_recommendation_preferences_provider import UserRecommendationPreferencesProvider
from app.graphql.graphql_router import schema
from app.main import app
from tests.assets.topics import populate_topics, technology_topic, business_topic
from tests.functional.test_dynamodb_base import TestDynamoDBBase

from unittest.mock import patch
from collections import namedtuple

MockResponse = namedtuple('MockResponse', 'status')


class TestUpdateUserRecommendationPreferences(TestDynamoDBBase):
    client: Client

    async def asyncSetUp(self):
        await super().asyncSetUp()
        populate_topics(self.metadata_table)
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
                            {"id": technology_topic.id},
                            {"id": business_topic.id},
                        ]
                    }
                },
                context_value={'user_id': user_id},
                executor=AsyncioExecutor())

            response = executed.get('data').get('updateUserRecommendationPreferences')

            assert response['preferredTopics'] == [
                {'id': technology_topic.id, 'name': technology_topic.name},
                {'id': business_topic.id, 'name': business_topic.name},
            ]
