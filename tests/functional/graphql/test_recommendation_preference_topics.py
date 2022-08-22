from fastapi.testclient import TestClient

from app.main import app
from tests.assets.topics import populate_topics, technology_topic, gaming_topic
from tests.functional.test_dynamodb_base import TestDynamoDBBase


class TestRecommendationPreferenceTopics(TestDynamoDBBase):

    async def asyncSetUp(self):
        await super().asyncSetUp()

    def test_recommendation_preference_topics(self):
        populate_topics(self.metadata_table, topics=[technology_topic, gaming_topic])

        with TestClient(app) as client:
            query = 'query RecommendationPreferenceTopics { recommendationPreferenceTopics { id name } }'
            response = client.post("/", json={'query': query}).json()

            assert not response.get('errors')
            topics = response.get('data').get('recommendationPreferenceTopics')

            # 'Gaming' is filtered out, so the only topic remaining is 'Technology'.
            assert len(topics) == 1
            assert topics[0]['name'] == 'Technology'
