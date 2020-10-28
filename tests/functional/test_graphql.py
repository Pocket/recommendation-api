from moto import mock_dynamodb2
from graphene.test import Client
from app.graphql.graphql import schema
from tests.functional.test_dynamodb_base import TestDynamoDBBase

TABLE_NAME = 'explore_topics_metadata'


@mock_dynamodb2
class TestGraphQL(TestDynamoDBBase):
    def setup_method(self, method):
        super().setup_method(self)
        self.table = self.create_explore_topics_metadata_table()
        self.populate_explore_topics_metadata_table()
        self.client = Client(schema)

    def teardown_method(self, method):
        super().teardown_method(self)
        self.table.delete()

    def test_main_list_topics(self):
        executed = self.client.execute('''{ listTopics { displayName} }''')
        assert executed == {
            'data': {
                'listTopics': [{
                    'displayName': 'tech'
                }]
            }
        }

    def populate_explore_topics_metadata_table(self):
        self.table.put_item(Item={
            "display_name": 'tech',
            "slug": 'tech',
            "query": 'query',
            "curator_label": 'technology',
            "is_displayed": True,
            "is_promoted": False
        })
