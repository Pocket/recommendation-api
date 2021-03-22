from graphql.execution.executors.asyncio import AsyncioExecutor
from graphene.test import Client
from app.graphql.graphql import schema
from tests.functional.test_dynamodb_base import TestDynamoDBBase


class TestGraphQLCandidates(TestDynamoDBBase):
    client: Client

    async def asyncSetUp(self):
        await super().asyncSetUp()
        self.client = Client(schema)

    def test_get_topic_recommendations(self):
        self.metadataTable.put_item(Item={
            "id": "123123-12sd1asd3-5512",
            "display_name": 'tech',
            "slug": 'tech',
            "query": 'query',
            "curator_label": 'technology',
            "page_type": 'topic_page',
            "is_displayed": True,
            "is_promoted": False
        })

        self.candidateTable.put_item(Item={
            "id": "asdasd-12sd1asd3-5512",
            "topic_id": '123123-12sd1asd3-5512',
            "type": 'curated',
            "topic_id-type": '123123-12sd1asd3-5512|curated',
            "created_at": "2020-03-05T00:13:52.093Z",
            "candidates": [
                {
                    'item_id': 123,
                    'feed_id': 5,
                    'publisher': 'test.yes'
                },
                {
                    'item_id': 1253,
                    'publisher': 'test.yes'
                }
            ]
        })

        executed = self.client.execute(''' {
            getSlateLineup(slateLineupId: "dc010ef1-1f34-473a-a4b5-4cc155e18a4a") {
                experimentId
                slates {
                    displayName
                }
             }         
        }''', executor=AsyncioExecutor())


        assert executed == {
            'data': {
                'getTopicRecommendations': {
                    'algorithmicRecommendations': [],
                    'curatedRecommendations': [
                        {
                            'feedItemId': 'RecommendationAPI/123',
                            'feedId': 5,
                            'itemId': '123',
                            'item': {'itemId': '123'},
                            'publisher': 'test.yes'
                        },
                        {
                            'feedItemId': 'RecommendationAPI/1253',
                            'feedId': None,
                            'itemId': '1253',
                            'item': {'itemId': '1253'},
                            'publisher': 'test.yes'
                        }
                    ],
                }
            }
        }
