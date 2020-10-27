from graphene import ObjectType, ID, String

class FeedItem(ObjectType):
    id = ID()
    item_id = ID()
    title = String()
    topic = String()

    def resolve_title(parent, info):
        return f"title resolver"