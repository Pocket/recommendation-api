from moto import mock_dynamodb2
from mypy_boto3_dynamodb.service_resource import DynamoDBServiceResource

from tests.functional.test_dynamodb_base import TestDynamoDBBase
from app.config import dynamodb as dynamodb_config
from app.models.recommendation import RecommendationModel, RecommendationType


@mock_dynamodb2
class TestRecommendationsModel(TestDynamoDBBase):
    metadataTable: DynamoDBServiceResource.Table
    candidateTable: DynamoDBServiceResource.Table

    def setup_method(self, method):
        dynamodb_config['endpoint_url'] = None
        super().setup_method(self)
        self.metadataTable = self.create_explore_topics_metadata_table()
        self.candidateTable = self.create_explore_topics_candidates_table()
        self.populate_explore_topics_metadata_table()

    def teardown_method(self, method):
        super().teardown_method(self)
        self.metadataTable.delete()
        self.candidateTable.delete()

    def test_get_latest_curated_candidates_for_topic(self):
        self.candidateTable.put_item(Item={
            "id": "asdasd-12sd1asd3-5512",
            "topic_id": 'a187ffb4-5c6f-4079-bad9-92442e97bdd1',
            "type": 'curated',
            "topic_id-type": 'a187ffb4-5c6f-4079-bad9-92442e97bdd1|curated',
            "created_at": "2020-03-05T00:13:52.093Z",
            "candidates": [
                {
                    'item_id': 123,
                    'feed_id': 5,
                },
                {
                    'item_id': 1253,
                }
            ]
        })

        self.candidateTable.put_item(Item={
            "id": "asdasd-12sd1asd3-5512",
            "topic_id": 'a187ffb4-5c6f-4079-bad9-92442e97bdd1',
            "type": 'curated',
            "topic_id-type": 'a187ffb4-5c6f-4079-bad9-92442e97bdd1|curated',
            "created_at": "2020-09-05T00:13:52.093Z",
            "candidates": [
                {
                    'item_id': 986,
                    'feed_id': 6,
                },
                {
                    'item_id': 93,
                }
            ]
        })

        self.candidateTable.put_item(Item={
            "id": "asdasd-12sd1asd3-5512",
            "topic_id": 'a187ffb4-5c6f-4079-bad9-92442e97bdd1',
            "type": 'curated',
            "topic_id-type": 'a187ffb4-5c6f-4079-bad9-92442e97bdd1|curated',
            "created_at": "2020-01-05T00:13:52.093Z",
            "candidates": [
                {
                    'item_id': 652,
                    'feed_id': 6,
                },
                {
                    'item_id': 9845,
                }
            ]
        })

        executed = RecommendationModel.get_recommendations(slug='tech', recommendation_type=RecommendationType.CURATED)
        assert executed == [
            RecommendationModel(item_id=986, feed_id=6, feed_item_id='ExploreTopics/986'),
            RecommendationModel(item_id=93, feed_item_id='ExploreTopics/93'),
        ]

    def populate_explore_topics_metadata_table(self):
        self.metadataTable.put_item(Item={
            'id': 'a187ffb4-5c6f-4079-bad9-92442e97bdd1',
            "display_name": 'tech',
            "slug": 'tech',
            "query": 'query',
            "curator_label": 'technology',
            "is_displayed": True,
            "is_promoted": False
        })

        self.metadataTable.put_item(Item={
            'id': 'a187ffb4-5c6f-4079-bad9-asd23234234',
            "display_name": 'Business',
            "slug": 'business',
            "query": 'money stonks',
            "curator_label": 'business',
            "is_displayed": True,
            "is_promoted": True
        })
