from enum import Enum
from typing import Optional

import strawberry
from strawberry import auto, field, ID

from app.models.topic import TopicModel


@strawberry.enum(description='Represents a type of page for /explore\n'
                             'Deprecated for SlateLineups')
class PageType(Enum):
    """
    This enum mirrors app.models.topic.PageType

    Strawberry does not seem to handle Pydantic models with Enums well. As a workaround, redefine the Enum with @strawberry.enum.
    """
    editorial_collection = 'editorial_collection'
    topic_page = 'topic_page'


@strawberry.experimental.pydantic.type(model=TopicModel)
class Topic:
    id: ID
    name: auto
    display_name: auto = field(deprecation_reason='displayName is deprecated. Use name instead.')
    display_note: auto = field(
        description='If returned a note to show to the user about the topic')
    slug: auto = field(
        description='The slug that should be used in the url to represent the topic')
    query: auto = field(
        description='The query that was used internally for elasticsearch to find items')
    curator_label: auto = field(
        description='The label the curator uses internally to get items onto this topic')
    is_displayed: auto = field(
        description='Whether or not clients should show this topic ot users')
    is_promoted: auto = field(
        description='Whether or not this topic should be visiblly promoted (prominent on the page)')
    social_title: auto = field(
        description='The title to use in the HTML markup for SEO and social media sharing')
    social_description: auto = field(
        description='The description to use in the HTML markup for SEO and social media sharing')
    social_image: auto = field(
        description='The image to use in the HTML markup for SEO and social media sharing')
    page_type: PageType = field(
        description='The type of page this topic represents used in  generation')
    custom_feed_id: auto = field(
        description='The internal feed id that this topic will pull from if set')
