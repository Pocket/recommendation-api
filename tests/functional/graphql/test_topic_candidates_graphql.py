from graphql.execution.executors.asyncio import AsyncioExecutor
from graphene.test import Client
from app.graphql.graphql import schema
from tests.functional.test_dynamodb_base import TestDynamoDBBase


class TestGraphQLCandidates(TestDynamoDBBase):
    client: Client

    def setup_method(self, method):
        super().setup_method(self)
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

        executed = self.client.execute('''{
            getTopicRecommendations(slug: "tech") {
                algorithmicRecommendations {feedItemId item {itemId} feedId publisher}
                curatedRecommendations {feedItemId item {itemId} feedId publisher}
            }
        }''', executor=AsyncioExecutor())
        assert executed == {
            'data': {
                'getTopicRecommendations': {
                    'algorithmicRecommendations': [],
                    'curatedRecommendations': [
                        {'feedItemId': 'RecommendationAPI/123', 'feedId': 5, 'item': {'itemId': '123'},
                         'publisher': 'test.yes'},
                        {'feedItemId': 'RecommendationAPI/1253', 'feedId': None, 'item': {'itemId': '1253'},
                         'publisher': 'test.yes'}
                    ],
                }
            }
        }

    def test_get_collection_topic_recommendations(self):
        self.metadataTable.put_item(Item={
            "id": "123123-12sd1asd3-5512",
            "display_name": 'special',
            "slug": 'special',
            "query": 'query',
            "curator_label": 'technology',
            "page_type": 'editorial_collection',
            "is_displayed": True,
            "is_promoted": False
        })

        self.candidateTable.put_item(Item={
            "id": "asdasd-12sd1asd3-5512",
            "topic_id": '123123-12sd1asd3-5512',
            "type": 'collection',
            "topic_id-type": '123123-12sd1asd3-5512|collection',
            "created_at": "2020-03-05T00:13:52.093Z",
            "candidates": [
                {
                    'item_id': 123,
                    'feed_id': 5,
                    'publisher': 'special.yes'
                },
                {
                    'item_id': 1253,
                    'publisher': 'test.yes'
                }
            ]
        })

        self.candidateTable.put_item(Item={
            "id": "a1dasd-12sd15d3-5522",
            "topic_id": '123123-12sd1asd3-5512',
            "type": 'algorithmic',
            "topic_id-type": '123123-12sd1asd3-5512|algorithmic',
            "created_at": "2020-03-05T00:13:52.093Z",
            "candidates": [
                {
                    'item_id': 123123123123,
                    'feed_id': 5,
                    'publisher': 'special.yes'
                },
                {
                    'item_id': 64556345,
                    'publisher': 'test.yes'
                }
            ]
        })

        self.candidateTable.put_item(Item={
            "id": "asdasd-12s2asd3-5312",
            "topic_id": '123123-12sd1asd3-5512',
            "type": 'curated',
            "topic_id-type": '123123-12sd1asd3-5512|curated',
            "created_at": "2020-03-05T00:13:52.093Z",
            "candidates": [
                {
                    'item_id': 8675309,
                    'feed_id': 5,
                    'publisher': '1234.yes'
                },
                {
                    'item_id': 8675309999999,
                    'publisher': '1235.yes'
                }
            ]
        })

        executed = self.client.execute('''{
            getTopicRecommendations(slug: "special") {
                algorithmicRecommendations {feedItemId item {itemId} feedId publisher}
                curatedRecommendations {feedItemId item {itemId} feedId publisher}
            }
        }''', executor=AsyncioExecutor())
        assert executed == {
            'data': {
                'getTopicRecommendations': {
                    'algorithmicRecommendations': [],
                    'curatedRecommendations': [
                        {'feedItemId': 'RecommendationAPI/123', 'feedId': 5, 'item': {'itemId': '123'},
                         'publisher': 'special.yes'},
                        {'feedItemId': 'RecommendationAPI/1253', 'feedId': None, 'item': {'itemId': '1253'},
                         'publisher': 'test.yes'}
                    ],
                }
            }
        }
