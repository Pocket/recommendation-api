from mypy_boto3_dynamodb.service_resource import DynamoDBServiceResource


def populate_topics(table: DynamoDBServiceResource.Table):
    table.put_item(Item={
        'id': 'a187ffb4-5c6f-4079-bad9-92442e97bdd1',
        "display_name": 'Technology',
        "page_type": 'topic_page',
        "slug": 'tech',
        "query": 'query',
        "curator_label": 'technology',
        "is_displayed": True,
        "is_promoted": False
    })

    table.put_item(Item={
        'id': 'fea00efc-ee03-48f5-95dc-148550c0b69c',
        "display_name": 'Gaming',
        "page_type": 'topic_page',
        "slug": 'tech',
        "query": 'query',
        "curator_label": 'gaming',
        "is_displayed": True,
        "is_promoted": False
    })
