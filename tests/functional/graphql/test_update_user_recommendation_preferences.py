from fastapi.testclient import TestClient

from app.data_providers.user_recommendation_preferences_provider import (
    UserRecommendationPreferencesProvider,
    UserRecommendationPreferencesProviderV2,
)
from app.main import app
from app.models.user_ids import UserIds
from tests.assets.topics import populate_topics, technology_topic, business_topic
from tests.functional.test_dynamodb_base import TestDynamoDBBase

from unittest.mock import patch


class TestUpdateUserRecommendationPreferences(TestDynamoDBBase):
    async def asyncSetUp(self):
        await super().asyncSetUp()
        populate_topics(self.metadata_table)
        self.user_ids = UserIds(
            user_id=1,
            hashed_user_id='1-hashed',
        )

    @patch.object(UserRecommendationPreferencesProvider, 'put')
    @patch.object(UserRecommendationPreferencesProviderV2, 'put')
    def test_update_user_recommendation_preferences(self, mock_data_provider_put_v2, mock_data_provider_put):
        with TestClient(app) as client:
            data = client.post(
                "/",
                json={
                    'query': '''
                        mutation Mutation($input: UpdateUserRecommendationPreferencesInput!) {
                          updateUserRecommendationPreferences(input: $input) {
                            preferredTopics {
                              id
                              name
                            }
                          }
                        }
                    ''',
                    'variables': {
                        'input': {
                            'preferredTopics': [
                                {'id': technology_topic.id},
                                {'id': business_topic.id},
                            ]
                        }
                    },
                },
                headers={
                    'userId': str(self.user_ids.user_id),
                    'encodedId': self.user_ids.hashed_user_id,
                }
            ).json()

            assert not data.get('errors')

            preferences = data['data']['updateUserRecommendationPreferences']
            assert preferences['preferredTopics'] == [
                {'id': technology_topic.id, 'name': technology_topic.name},
                {'id': business_topic.id, 'name': business_topic.name},
            ]
