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
        self.table = self.create_explore_topics_metadata_table()
        self.table = self.create_explore_topics_candidates_table()
        self.populate_explore_topics_candidates_table()
        self.client = Client(schema)

    def teardown_method(self, method):
        super().teardown_method(self)
        self.table.delete()

    def test_main_get_topic_recommendations(self):
        executed = self.client.execute('''{
            getTopicRecommendations(slug: "business") {
                algorithmicRecommendations {feedItemId itemId feedId}
                curatedRecommendations {feedItemId itemId feedId}
            }
        }''')
        assert executed == {
            'data': {
                'getTopicRecommendations': {
                    'algorithmicRecommendations': [{'feedItemId': 'ExploreTopics/123', 'feedId': 1, 'itemId': '123'}],
                    'curatedRecommendations': [],
                }
            }
        }

    def populate_explore_topics_candidates_table(self):
        self.table.put_item(Item={
            "display_name": 'tech',
            "slug": 'tech',
            "query": 'query',
            "curator_label": 'technology',
            "is_displayed": True,
            "is_promoted": False
        })
