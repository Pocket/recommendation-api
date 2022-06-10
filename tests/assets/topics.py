from mypy_boto3_dynamodb.service_resource import DynamoDBServiceResource

from app.models.topic import PageType, TopicModel

business_topic = TopicModel(
    id='a187ffb4-5c6f-4079-bad9-asd23234234',
    name='Business',
    display_name='Business',
    slug='business',
    query='money stonks',
    curator_label='business',
    is_displayed=True,
    is_promoted=True,
    custom_feed_id='7',
    page_type=PageType.editorial_collection
)

technology_topic = TopicModel(
    id='a187ffb4-5c6f-4079-bad9-92442e97bdd1',
    name='Technology',
    display_name='Technology',
    slug='tech',
    query='query',
    curator_label='technology',
    is_displayed=True,
    is_promoted=False,
    page_type=PageType.topic_page
)


def populate_topics(table: DynamoDBServiceResource.Table):
    table.put_item(Item=business_topic.dict())
    table.put_item(Item=technology_topic.dict())
