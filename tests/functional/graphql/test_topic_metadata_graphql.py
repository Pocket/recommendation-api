from fastapi.testclient import TestClient

from app.main import app
from tests.assets.topics import populate_topics, technology_topic
from tests.functional.test_dynamodb_base import TestDynamoDBBase


class TestGraphQLMetadata(TestDynamoDBBase):
    async def asyncSetUp(self):
        await super().asyncSetUp()
        populate_topics(self.metadata_table, topics=[technology_topic])

    def test_main_list_topics(self):
        with TestClient(app) as client:
            data = client.post("/", json={'query': '{ listTopics { name } }'}).json()
            assert data == {
                'data': {
                    'listTopics': [{
                        'name': 'Technology'
                    }]
                }
            }
