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


@strawberry.experimental.pydantic.type(
    model=TopicModel,
    description='Represents a topic for /explore\nDeprecated for SlateLineups')
class Topic:
    id: ID
    name: auto
    display_name: auto = field(deprecation_reason='displayName is deprecated. Use name instead.')
    display_note: auto
    slug: auto
    query: auto
    curator_label: auto
    is_displayed: auto
    is_promoted: auto
    social_title: auto
    social_description: auto
    social_image: auto
    page_type: PageType
    custom_feed_id: auto
