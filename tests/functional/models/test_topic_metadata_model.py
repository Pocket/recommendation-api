from moto import mock_dynamodb2

from tests.functional.test_dynamodb_base import TestDynamoDBBase
from app.config import aws as aws_config
from app.models.topic import TopicModel, PageType


@mock_dynamodb2
class TestTopicMetadata(TestDynamoDBBase):
    def setup_method(self, method):
        aws_config['endpoint_url'] = None
        super().setup_method(self)
        self.table = self.create_explore_topics_metadata_table()
        self.populate_explore_topics_metadata_table()

    def teardown_method(self, method):
        super().teardown_method(self)
        self.table.delete()

    def test_main_list_topics(self):
        executed = TopicModel.get_all()
        assert executed == [
            TopicModel(id='a187ffb4-5c6f-4079-bad9-92442e97bdd1',
                       display_name='tech',
                       slug='tech',
                       query='query',
                       curator_label='technology',
                       is_displayed=True,
                       is_promoted=False,
                       page_type=PageType.topic_page
                       ),
            TopicModel(id='a187ffb4-5c6f-4079-bad9-asd23234234',
                       display_name='Business',
                       slug='business',
                       query='money stonks',
                       curator_label='business',
                       is_displayed=True,
                       is_promoted=True,
                       page_type=PageType.editorial_collection
                       )
        ]

    def test_main_get_topic(self):
        executed = TopicModel.get_topic('business')
        assert executed == TopicModel(id='a187ffb4-5c6f-4079-bad9-asd23234234',
                                      display_name='Business',
                                      slug='business',
                                      query='money stonks',
                                      curator_label='business',
                                      is_displayed=True,
                                      is_promoted=True,
                                      page_type=PageType.editorial_collection
                                      )

    def test_main_get_nonexistent_topic(self):
        self.assertRaises(ValueError, TopicModel.get_topic, 'stonks')

    def populate_explore_topics_metadata_table(self):
        self.table.put_item(Item={
            'id': 'a187ffb4-5c6f-4079-bad9-92442e97bdd1',
            "display_name": 'tech',
            "slug": 'tech',
            "query": 'query',
            "curator_label": 'technology',
            "page_type": 'topic_page',
            "is_displayed": True,
            "is_promoted": False
        })

        self.table.put_item(Item={
            'id': 'a187ffb4-5c6f-4079-bad9-asd23234234',
            "display_name": 'Business',
            "slug": 'business',
            "query": 'money stonks',
            "curator_label": 'business',
            "page_type": 'editorial_collection',
            "is_displayed": True,
            "is_promoted": True
        })
