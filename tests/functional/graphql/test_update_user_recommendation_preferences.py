from fastapi.testclient import TestClient

from app.data_providers.user_recommendation_preferences_provider import UserRecommendationPreferencesProviderV2
from app.main import app
from app.models.request_user import RequestUser
from tests.assets.topics import populate_topics, technology_topic, business_topic
from tests.functional.test_dynamodb_base import TestDynamoDBBase

from unittest.mock import patch


class TestUpdateUserRecommendationPreferences(TestDynamoDBBase):
    async def asyncSetUp(self):
        await super().asyncSetUp()
        populate_topics(self.metadata_table)
        self.request_user = RequestUser(
            user_id=1,
            hashed_user_id='1-hashed',
        )

    @patch.object(UserRecommendationPreferencesProviderV2, 'put')
    def test_update_user_recommendation_preferences(self, mock_data_provider_put_v2):
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
                    'userId': str(self.request_user.user_id),
                    'encodedId': self.request_user.hashed_user_id,
                }
            ).json()

            assert not data.get('errors')

            preferences = data['data']['updateUserRecommendationPreferences']
            assert preferences['preferredTopics'] == [
                {'id': technology_topic.id, 'name': technology_topic.name},
                {'id': business_topic.id, 'name': business_topic.name},
            ]
