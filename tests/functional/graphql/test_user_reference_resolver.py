from graphql.execution.executors.asyncio import AsyncioExecutor
from graphene.test import Client
from fastapi.testclient import TestClient

from app.data_providers.user_recommendation_preferences_provider import (
    UserRecommendationPreferencesProviderV2,
)
from app.graphql.graphql_router import schema
from app.main import app
from app.models.user_ids import UserIds
from tests.assets.topics import populate_topics
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
        self.user_ids = UserIds(
            user_id=1,
            hashed_user_id='1-hashed',
        )

    @patch.object(UserRecommendationPreferencesProviderV2, 'fetch', return_value=None)
    def test_update_user_recommendation_preferences(self, mock_data_provider_fetch_v2):
        with TestClient(app):
            executed = self.client.execute(
                '''
                query ($representations: [_Any!]!) {
                  _entities(representations: $representations) {
                    ... on User {
                      id
                      recommendationPreferences {
                        preferredTopics {
                          name
                          id
                        }
                      }
                    }
                  }
                }
                ''',
                variables={
                    'representations': [
                        {
                            '__typename': 'User',
                            'id': self.user_ids.hashed_user_id,
                        },
                    ],
                },
                executor=AsyncioExecutor())

            assert not executed.get('error')
            entities = executed['data']['_entities']

            assert len(entities) == 1
            assert entities[0]['id'] == self.user_ids.hashed_user_id
            assert entities[0]['recommendationPreferences']['preferredTopics'] == []
            print("Done")
