from graphene import ObjectType, String, List

from app.graphql.feed_item import FeedItem


class Query(ObjectType):
    # this defines a Field `hello` in our Schema with a single Argument `name`
    get_feed_items_for_topic = List(topic=String(default_value="finance"), of_type=FeedItem)

    # our Resolver method takes the GraphQL context (root, info) as well as
    # Argument (name) for the Field and returns data for the query Response
    def resolve_get_feed_items_for_topic(root, info, topic):
        feed_item = FeedItem()
        feed_item.itemID = '123'
        feed_item.id = '1'
        feed_item.topic = topic
        return [feed_item]

