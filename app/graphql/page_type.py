from enum import Enum

import strawberry


@strawberry.enum
class PageType(Enum):
    editorial_collection = 'editorial_collection'
    topic_page = 'topic_page'
