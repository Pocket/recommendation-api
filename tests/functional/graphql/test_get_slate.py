from fastapi.testclient import TestClient

from app.main import app
from app.models.user_ids import UserIds
from tests.functional.test_dynamodb_base import TestDynamoDBBase

from unittest.mock import patch


class TestGetSlate(TestDynamoDBBase):

    async def asyncSetUp(self):
        await super().asyncSetUp()
        self.populate_candidate_sets_table()
        self.user_ids = UserIds(
            user_id=1,
            hashed_user_id='1-hashed',
        )

    def test_get_slate(self):
        with TestClient(app) as client:
            data = client.post(
                '/',
                json={
                    'query': '''
                        query GetSlate {
                          getSlate(slateId: "0f322865-64e6-472d-8147-b3d6637a7d67") {
                            description
                          }
                        }
                    ''',
                },
                headers={
                    'userId': 'johnjacobjingleheimerschmidt',
                }
            ).json()

            assert not data.get('errors')
            slate = data['data']['getSlate']

            # Testing that the slate has a description
            assert 'description' in slate

    def populate_candidate_sets_table(self):
        self.candidate_set_table.put_item(Item={
            'id': '303174fc-a9ff-4a51-984a-e09ce7120d18',
            'candidates': [],
            'version': '1'
        })
