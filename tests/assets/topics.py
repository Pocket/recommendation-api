from typing import List

from mypy_boto3_dynamodb.service_resource import DynamoDBServiceResource

from app.models.topic import PageType, TopicModel

business_topic = TopicModel(
    id='a187ffb4-5c6f-4079-bad9-asd23234234',
    corpus_topic_id='BUSINESS',
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
    corpus_topic_id='TECHNOLOGY',
    name='Technology',
    display_name='Technology',
    slug='tech',
    query='query',
    curator_label='technology',
    is_displayed=True,
    is_promoted=False,
    page_type=PageType.topic_page
)

gaming_topic = TopicModel(
    id='fea00efc-ee03-48f5-95dc-148550c0b69c',
    corpus_topic_id='GAMING',
    name='Gaming',
    display_name='Gaming',
    slug='gaming',
    query='hobbies video games gaming gamer',
    curator_label='Gaming',
    is_displayed=False,
    is_promoted=False,
    page_type=PageType.topic_page
)


def populate_topics(table: DynamoDBServiceResource.Table, topics: List[TopicModel] = None):
    if topics is None:
        topics = [business_topic, technology_topic]

    for topic in topics:
        table.put_item(Item=topic.dict())
