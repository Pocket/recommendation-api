from graphql.execution.executors.asyncio import AsyncioExecutor
from graphene.test import Client
from mypy_boto3_dynamodb.service_resource import DynamoDBServiceResource
from app.graphql.graphql import schema
from tests.functional.test_dynamodb_base import TestDynamoDBBase
from app.config import dynamodb as dynamodb_config


class TestGraphQLMetadata(TestDynamoDBBase):
    client: Client

    def setup_method(self, method):
        super().setup_method(self)
        self.populate_explore_topics_metadata_table()
        self.client = Client(schema)

    def test_main_list_topics(self):
        executed = self.client.execute('''{ listTopics { displayName} }''', executor=AsyncioExecutor())
        assert executed == {
            'data': {
                'listTopics': [{
                    'displayName': 'tech'
                }]
            }
        }

    def populate_explore_topics_metadata_table(self):
        self.metadataTable.put_item(Item={
            'id': 'a187ffb4-5c6f-4079-bad9-92442e97bdd1',
            "display_name": 'tech',
            "page_type": 'topic_page',
            "slug": 'tech',
            "query": 'query',
            "curator_label": 'technology',
            "is_displayed": True,
            "is_promoted": False
        })
