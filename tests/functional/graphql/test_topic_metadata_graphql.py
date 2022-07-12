from graphql.execution.executors.asyncio import AsyncioExecutor
from graphene.test import Client
from app.graphql.graphql_router import schema
from tests.assets.topics import populate_topics, technology_topic
from tests.functional.test_dynamodb_base import TestDynamoDBBase


class TestGraphQLMetadata(TestDynamoDBBase):
    client: Client

    async def asyncSetUp(self):
        await super().asyncSetUp()
        populate_topics(self.metadata_table, topics=[technology_topic])
        self.client = Client(schema)

    def test_main_list_topics(self):
        executed = self.client.execute('''{ listTopics { name } }''', executor=AsyncioExecutor())
        assert executed == {
            'data': {
                'listTopics': [{
                    'name': 'Technology'
                }]
            }
        }
