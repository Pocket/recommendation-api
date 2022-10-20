from fastapi.testclient import TestClient

from app.main import app
from app.models.user_ids import UserIds
from tests.functional.test_dynamodb_base import TestDynamoDBBase

from unittest.mock import patch
from collections import namedtuple

MockResponse = namedtuple('MockResponse', 'status')


class TestGetSlateLineup(TestDynamoDBBase):

    async def asyncSetUp(self):
        await super().asyncSetUp()
        self.populate_candidate_sets_table()
        self.user_ids = UserIds(
            user_id=1,
            hashed_user_id='1-hashed',
        )

    @patch('aiohttp.ClientSession.get', to_return=MockResponse(status=200))
    def test_get_slate_lineup(self, mock_clientsession_get):
        with TestClient(app) as client:
            data = client.post(
                '/',
                json={
                    'query': '''
                        query GetSlateLineup {
                          getSlateLineup(slateLineupId: "aaf47c0f-1361-4c8c-a89f-fa45e1dc2978") {
                            slates {
                              description
                            }
                          }
                        }
                    ''',
                },
                headers={
                    'userId': 'johnjacobjingleheimerschmidt',
                }
            ).json()

            assert not data.get('errors')
            slate_list = data['data']['getSlateLineup']['slates']

            # Testing that multiple slates come back
            assert len(slate_list) > 1

            # Testing that they all have a description
            assert all('description' in slate for slate in slate_list)

            # FOR YOUR REFERENCE, the response JSON should look something like this:
            # {'data':
            #     {'getSlateLineup':
            #         {'slates': [
            #             {'description': 'Stories to fuel your mind, curated for your interests'},
            #             {'description': 'Pocket Collections'},
            #             {'description': 'Smart, quick reads from trusted sources'},
            #             {'description': 'The best longform journalism and essays popular in Pocket'},
            #             {'description': 'Great stories that stand the test of time'}
            #         ]
            #         }
            #     }
            # }

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
