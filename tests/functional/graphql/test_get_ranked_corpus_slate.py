from graphql.execution.executors.asyncio import AsyncioExecutor
from graphene.test import Client
from fastapi.testclient import TestClient

from app.graphql.graphql import schema
from app.main import app, load_slate_configs
from tests.functional.test_dynamodb_base import TestDynamoDBBase

from unittest.mock import patch
from collections import namedtuple

MockResponse = namedtuple('MockResponse', 'status')

class TestGetRankedCorpusSlate(TestDynamoDBBase):
    client: Client

    async def asyncSetUp(self):
        await super().asyncSetUp()
        self.populate_candidate_sets_table()
        self.client = Client(schema)

    @patch('aiohttp.ClientSession.get', to_return=MockResponse(status=200))
    def test_get_corpus_slate(self, mock_client_session_get):
        with TestClient(app):
            executed = self.client.execute(
                '''
                    query TestGetRankedCorpusSlate {
                        getRankedCorpusSlate(slateId: "aaf47c0f-1361-4c8c-a89f-fa45e1dc2978") {
                          slateId
                          description 
                            corpusSlate {
                                id
                          }
                        }
                    }
                ''',
                context_value={"user_id": "johnjacobjingleheimerschmidt"},
                executor=AsyncioExecutor())

            response = executed.get('data').get('getRankedCorpusSlate')
            id = response.get('slateId')
            assert id == "00000000-0000-0000-0000-000000000496"
            description = response.get('description')
            assert description == "I am the corpus slate, coo coo ca choo"

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