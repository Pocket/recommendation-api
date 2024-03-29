from datetime import datetime

from fastapi.testclient import TestClient

from app.data_providers.user_recommendation_preferences_provider import UserRecommendationPreferencesProvider
from app.main import app
from app.models.request_user import RequestUser
from app.models.user_recommendation_preferences import UserRecommendationPreferencesModel
from tests.assets.topics import populate_topics, business_topic
from tests.functional.test_dynamodb_base import TestDynamoDBBase


from unittest.mock import patch


mock_user_preferences = UserRecommendationPreferencesModel(
    hashed_user_id='1-hashed',
    updated_at=datetime(2022, 7, 14, 8, 30),
    preferred_topics=[business_topic],
)


class TestUserReferenceResolver(TestDynamoDBBase):

    async def asyncSetUp(self):
        await super().asyncSetUp()
        populate_topics(self.metadata_table)
        self.request_user = RequestUser(
            user_id=1,
            hashed_user_id='1-hashed',
        )

    @patch.object(UserRecommendationPreferencesProvider, 'fetch', return_value=mock_user_preferences)
    def test_user_reference_resolver(self, mock_data_provider_fetch):
        with TestClient(app) as client:
            response = client.post(
                "/",
                json={
                    'query': '''
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
                    'variables': {
                        'representations': [
                            {
                                '__typename': 'User',
                                'id': self.request_user.hashed_user_id,
                            },
                        ],
                    },
                },
            )

            executed = response.json()

            assert not executed.get('errors')
            entities = executed['data']['_entities']

            assert len(entities) == 1
            assert entities[0]['id'] == self.request_user.hashed_user_id
            assert entities[0]['recommendationPreferences']['preferredTopics'] == [
                {'id': business_topic.id, 'name': business_topic.name}
            ]
