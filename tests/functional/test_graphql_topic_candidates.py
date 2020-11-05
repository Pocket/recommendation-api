from moto import mock_dynamodb2
from graphene.test import Client
from app.graphql.graphql import schema
from tests.functional.test_dynamodb_base import TestDynamoDBBase
from app.config import dynamodb as dynamodb_config


@mock_dynamodb2
class TestGraphQL(TestDynamoDBBase):
    def setup_method(self, method):
        dynamodb_config['endpoint_url'] = None
        super().setup_method(self)
        self.metadataTable = self.create_explore_topics_metadata_table()
        self.candidateTable = self.create_explore_topics_candidates_table()
        self.client = Client(schema)

    def teardown_method(self, method):
        super().teardown_method(self)
        self.metadataTable.delete()
        self.candidateTable.delete()

    def test_main_get_topic_recommendations(self):
        self.metadataTable.put_item(Item={
            "id": "123123-12sd1asd3-5512",
            "display_name": 'tech',
            "slug": 'tech',
            "query": 'query',
            "curator_label": 'technology',
            "is_displayed": True,
            "is_promoted": False
        })

        self.candidateTable.put_item(Item={
            "id": "asdasd-12sd1asd3-5512",
            "topic_id": '123123-12sd1asd3-5512',
            "type": 'curated',
            "topic_id-type": '123123-12sd1asd3-5512|curated',
            "created_at": "2020-03-05T00:13:52.093Z",
            "candidates": [
                {
                    'item_id': 123,
                    'feed_id': 5,
                },
                {
                    'item_id': 1253,
                }
            ]
        })

        executed = self.client.execute('''{
            getTopicRecommendations(slug: "tech") {
                algorithmicRecommendations {feedItemId itemId feedId}
                curatedRecommendations {feedItemId itemId feedId}
            }
        }''')
        assert executed == {
            'data': {
                'getTopicRecommendations': {
                    'algorithmicRecommendations': [],
                    'curatedRecommendations': [{'feedItemId': 'ExploreTopics/123', 'feedId': 5, 'itemId': '123'},{'feedItemId': 'ExploreTopics/1253', 'feedId': None, 'itemId': '1253'}],
                }
            }
        }
