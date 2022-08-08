from graphql.execution.executors.asyncio import AsyncioExecutor
from graphene.test import Client
from fastapi.testclient import TestClient

from app.data_providers.user_recommendation_preferences_provider import (
    UserRecommendationPreferencesProvider,
    UserRecommendationPreferencesProviderV2,
)
from app.graphql.graphql_router import schema
from app.main import app
from app.models.user import User
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
        self.user = User(
            user_id=1,
            hashed_user_id='1-hashed',
        )


    @patch.object(UserRecommendationPreferencesProvider, 'put')
    @patch.object(UserRecommendationPreferencesProviderV2, 'put')
    def test_update_user_recommendation_preferences(self, mock_data_provider_put_v2, mock_data_provider_put):
        topics = populate_topics(self.metadata_table)

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
                context_value={'user_id': self.user.user_id, 'user': self.user},
                executor=AsyncioExecutor())

            response = executed.get('data').get('updateUserRecommendationPreferences')

            assert response['preferredTopics'] == [
                {'id': technology_topic.id, 'name': technology_topic.name},
                {'id': business_topic.id, 'name': business_topic.name},
            ]
