from graphene import ObjectType, String, Boolean


class Topic(ObjectType):
    display_name = String(required=True)
    slug = String(required=True)
    query = String(required=True)
    curator_label = String(required=True)
    is_displayed = Boolean(required=True)
    is_promoted = Boolean(required=True)
    social_title = String()
    social_description = String()
    social_image = String()

