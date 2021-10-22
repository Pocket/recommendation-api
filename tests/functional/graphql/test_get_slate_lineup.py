from graphql.execution.executors.asyncio import AsyncioExecutor
from graphene.test import Client
from app.graphql.graphql import schema
from tests.functional.test_dynamodb_base import TestDynamoDBBase


class TestGetSlateLineup(TestDynamoDBBase):
    client: Client

    async def asyncSetUp(self):
        await super().asyncSetUp()
        self.populate_candidate_table()
        self.client = Client(schema)

    def test_get_slate_lineup(self):
        executed = self.client.execute('''
          query GetSlateLineup {
            getSlateLineup(slateLineupId: "34a35300-73c0-4ecc-8f11-4779b7dc1378") {
              slates {
                  description
              }
            }
          }
        ''', executor=AsyncioExecutor())
        assert executed == {
            'data': {
                'slates': [{
                    'description': "Android is where it's at"
                }],
            }
        }

    def populate_candidate_table(self):
        pass
        # self.candidate_table.put_item(Item={
        #     'id': 'a187ffb4-5c6f-4079-bad9-92442e97bdd1',
        #     "display_name": 'tech',
        #     "page_type": 'topic_page',
        #     "slug": 'tech',
        #     "query": 'query',
        #     "curator_label": 'technology',
        #     "is_displayed": True,
        #     "is_promoted": False
        # })
        # self.candidate_set_table.put_item(Item={})
