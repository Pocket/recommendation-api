from enum import Enum

from pydantic import BaseModel, Field
from typing import Dict, Optional


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
    id: str = Field(description='The id of the topic')
    corpus_topic_id: str = Field(description='Corpus API topic identifier')
    name: str = Field(description='The name of the topic to show to the user')
    display_name: str = Field(description='The name of the topic to show to the user')
    page_type: PageType = Field(description='The type of page this topic represents used in  generation')
    slug: str = Field(description='The slug that should be used in the url to represent the topic')
    query: str = Field(description='The query that was used internally for elasticsearch to find items')
    curator_label: str = Field(description='The label the curator uses internally to get items onto this topic')
    is_displayed: bool = Field(description='Whether or not clients should show this topic ot users')
    is_promoted: bool = Field(
        description='Whether or not this topic should be visiblly promoted (prominent on the page)')
    display_note: Optional[str] = Field(description='If returned a note to show to the user about the topic')
    social_title: Optional[str] = Field(
        description='The title to use in the HTML markup for SEO and social media sharing')
    social_description: Optional[str] = Field(
        description='The description to use in the HTML markup for SEO and social media sharing')
    social_image: Optional[str] = Field(
        description='The image to use in the HTML markup for SEO and social media sharing')
    custom_feed_id: Optional[str] = Field(description='The internal feed id that this topic will pull from if set')

    @staticmethod
    def from_dict(item: Dict) -> 'TopicModel':
        # Map display_name to name. display_name is being deprecated, but still present in the database.
        return TopicModel.parse_obj(dict({'name': item['display_name']}, **item))
