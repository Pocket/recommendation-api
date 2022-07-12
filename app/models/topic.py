from enum import Enum
from pydantic import BaseModel
from typing import Dict


class PageType(str, Enum):
    """
    Define the possible page types for a topic.
    """
    editorial_collection = 'editorial_collection'
    topic_page = 'topic_page'


class TopicModel(BaseModel):
    """
    Models a topic, e.g. Technology, Gaming.
    """
    id: str
    corpus_topic_id: str
    name: str
    display_name: str
    page_type: PageType
    slug: str
    query: str
    curator_label: str
    is_displayed: bool
    is_promoted: bool
    display_note: str = None
    social_title: str = None
    social_description: str = None
    social_image: str = None
    custom_feed_id: str = None

    @staticmethod
    def from_dict(item: Dict) -> 'TopicModel':
        # Map display_name to name. display_name is being deprecated, but still present in the database.
        return TopicModel.parse_obj(dict({'name': item['display_name']}, **item))
