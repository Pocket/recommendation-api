from graphene import ObjectType, List, String, Boolean, ID


class Topic(ObjectType):
    id = ID(required=True)
    display_name = String(required=True)
    slug = String(required=True)
    query = List(of_type=String, required=True)
    curator_label = String(required=True)
    is_displayed = Boolean(required=True)
    is_promoted = Boolean(required=True)
    social_title = String()
    social_description = String()
    social_image = String()

