from typing import List

from mypy_boto3_dynamodb.service_resource import DynamoDBServiceResource

from app.models.topic import PageType, TopicModel


business_topic = TopicModel(
    id='1bf756c0-632f-49e8-9cce-324f38f4cc71',
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
    id='25c716f1-e1b2-43db-bf52-1a5553d9fb74',
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

health_topic = TopicModel(
    id='26a3efb4-0f82-415a-9f47-7893df85853f',
    corpus_topic_id='HEALTH_FITNESS',
    name='Health & Fitness',
    display_name='Health',
    slug='Health',
    query='Health',
    curator_label='Health',
    is_displayed=False,
    is_promoted=False,
    page_type=PageType.topic_page
)

entertainment_topic = TopicModel(
    id='c6242e35-4ef7-494f-ae9f-51f95b836424',
    corpus_topic_id='ENTERTAINMENT',
    name='Entertainment',
    display_name='Entertainment',
    slug='Entertainment',
    query='Entertainment',
    curator_label='Entertainment',
    is_displayed=False,
    is_promoted=False,
    page_type=PageType.topic_page
)

travel_topic = TopicModel(
    id='7dc49254-686d-46e1-aa94-7ac3e7767f66',
    corpus_topic_id='TRAVEL',
    name='Travel',
    display_name='Travel',
    slug='Travel',
    query='Travel',
    curator_label='Travel',
    is_displayed=True,
    is_promoted=True,
    page_type=PageType.topic_page
)


all_topic_fixtures = [
    business_topic,
    gaming_topic,
    technology_topic,
    health_topic,
    travel_topic,
    entertainment_topic,
]


def populate_topics(table: DynamoDBServiceResource.Table, topics: List[TopicModel] = None):
    if topics is None:
        topics = all_topic_fixtures

    for topic in topics:
        topic_dict = topic.dict()
        table.put_item(Item=topic_dict)
