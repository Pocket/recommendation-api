from tests.functional.test_dynamodb_base import TestDynamoDBBase
from app.models.topic import TopicModel, PageType


class TestTopicMetadata(TestDynamoDBBase):
    def setup_method(self, method):
        super().setup_method(self)
        self.populate_metadata_table()

    async def test_main_list_topics(self):
        executed = await TopicModel.get_all()
        assert executed == [
            TopicModel(id='a187ffb4-5c6f-4079-bad9-asd23234234',
                       display_name='Business',
                       slug='business',
                       query='money stonks',
                       curator_label='business',
                       is_displayed=True,
                       is_promoted=True,
                       custom_feed_id='7',
                       page_type=PageType.editorial_collection
                       ),
            TopicModel(id='a187ffb4-5c6f-4079-bad9-92442e97bdd1',
                       display_name='tech',
                       slug='tech',
                       query='query',
                       curator_label='technology',
                       is_displayed=True,
                       is_promoted=False,
                       page_type=PageType.topic_page
                       ),
        ]

    async def test_main_get_topic(self):
        executed = await TopicModel.get_topic('business')
        assert executed == TopicModel(id='a187ffb4-5c6f-4079-bad9-asd23234234',
                                      display_name='Business',
                                      slug='business',
                                      query='money stonks',
                                      curator_label='business',
                                      is_displayed=True,
                                      is_promoted=True,
                                      custom_feed_id='7',
                                      page_type=PageType.editorial_collection
                                      )

    async def test_main_get_nonexistent_topic(self):
        with self.assertRaises(ValueError):
            await TopicModel.get_topic(slug='stonks')

    def populate_metadata_table(self):
        self.metadataTable.put_item(Item={
            'id': 'a187ffb4-5c6f-4079-bad9-92442e97bdd1',
            "display_name": 'tech',
            "slug": 'tech',
            "query": 'query',
            "curator_label": 'technology',
            "page_type": 'topic_page',
            "is_displayed": True,
            "is_promoted": False
        })

        self.metadataTable.put_item(Item={
            'id': 'a187ffb4-5c6f-4079-bad9-asd23234234',
            "display_name": 'Business',
            "slug": 'business',
            "query": 'money stonks',
            "curator_label": 'business',
            "page_type": 'editorial_collection',
            'custom_feed_id': '7',
            "is_displayed": True,
            "is_promoted": True
        })
