from graphene import ObjectType, String, List, Schema
from app.graphql.feed_item import FeedItem
from app.graphql.topic import Topic
from app.models.topic import Topic as TopicModel
import os
from boto3.dynamodb.conditions import Key


class Query(ObjectType):
    # this defines a Field `feed_items_for_topic` in our Schema with a single Argument `topic`
    # and notes that it returns a list of FeedItems
    get_feed_items_for_topic = List(topic=String(default_value="finance"), of_type=FeedItem)
    list_topics = List(Topic)

    # our Resolver method takes the GraphQL context (root, info) as well as
    # Argument (name) for the Field and returns data for the query Response
    def resolve_get_feed_items_for_topic(self, info, topic):
        # Example on returning a list of feed_items
        feed_item = FeedItem()
        feed_item.itemID = '123'
        feed_item.id = '1'
        feed_item.topic = topic
        return [feed_item]

    def resolve_list_topics(self, info):
        return TopicModel.get_all()


##
# Graphene requires that you define your schema programaticaly.
# Looks like Graphene 3 will support loading from a .graphql file.
# For now this file should stay in sync with *.graphql
##
schema = Schema(query=Query)
