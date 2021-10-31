from graphql.execution.executors.asyncio import AsyncioExecutor
from graphene.test import Client
from app.graphql.schema import schema
from tests.functional.test_dynamodb_base import TestDynamoDBBase


class TestGraphQLMetadata(TestDynamoDBBase):
    client: Client

    async def asyncSetUp(self):
        await super().asyncSetUp()
        self.populate_metadata_table()
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

    def populate_metadata_table(self):
        self.metadata_table.put_item(Item={
            'id': 'a187ffb4-5c6f-4079-bad9-92442e97bdd1',
            "display_name": 'tech',
            "page_type": 'topic_page',
            "slug": 'tech',
            "query": 'query',
            "curator_label": 'technology',
            "is_displayed": True,
            "is_promoted": False
        })
