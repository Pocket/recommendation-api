from graphene import ObjectType, Int, ID


class Recommendation(ObjectType):
    feed_item_id = ID()
    item_id = ID()
    feed_id = Int()
