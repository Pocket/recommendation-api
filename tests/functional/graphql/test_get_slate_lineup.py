from graphql.execution.executors.asyncio import AsyncioExecutor
from graphene.test import Client
from fastapi.testclient import TestClient

from app.graphql.graphql import schema
from app.main import app, load_slate_configs
from tests.functional.test_dynamodb_base import TestDynamoDBBase


class TestGetSlateLineup(TestDynamoDBBase):
    client: Client

    async def asyncSetUp(self):
        await super().asyncSetUp()
        self.populate_candidate_sets_table()
        self.client = Client(schema)

    def test_get_slate_lineup(self):
        with TestClient(app): # This context manager forces the FastAPI startup event to run, which we use to populate our slate lineup configuration
            executed = self.client.execute(
                '''
                    query GetSlateLineup {
                      getSlateLineup(slateLineupId: "aaf47c0f-1361-4c8c-a89f-fa45e1dc2978") {
                        slates {
                            description
                        }
                      }
                    }
                ''',
                context_value={"user_id": "johnjacobjingleheimerschmidt"},
                executor=AsyncioExecutor())
            assert executed == {
                'data': {
                    'slates': [{
                        'description': "Android is where it's at"
                    }],
                }
            }

    def populate_candidate_sets_table(self):
        self.candidate_set_table.put_item(Item={
            'id': '303174fc-a9ff-4a51-984a-e09ce7120d18',
            'candidates': [],
            'version': '1'
        })
        self.candidate_set_table.put_item(Item={
            'id': 'a8425a46-187a-4cdb-8157-5d2f308c52cd',
            'candidates': [],
            'version': '1'
        })
        self.candidate_set_table.put_item(Item={
            'id': 'dacc55ea-db8d-4858-a51d-e1c78298337e',
            'candidates': [],
            'version': '1'
        })
        self.candidate_set_table.put_item(Item={
            'id': '7ef90242-ff7a-44ac-8a32-53193e4a23eb',
            'candidates': [],
            'version': '1'
        })
