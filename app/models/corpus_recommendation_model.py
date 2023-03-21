import random
from typing import Optional
from uuid import uuid4

from pydantic import BaseModel, Field

from app.models.corpus_item_model import CorpusItemModel
from app.models.recommendation_reason_model import RecommendationReasonModel


class CorpusRecommendationModel(BaseModel):
    id: str = Field(
        default_factory=lambda: str(uuid4()),
        description='Clients should include this id in the `corpus_recommendation` Snowplow entity for impression, '
                    'content_open, and engagement events related to this recommendation. This id is different '
                    'across users, across requests, and across corpus items. The recommendation-api service associates '
                    'metadata with this id to join and aggregate recommendations in our data warehouse.')
    tile_id: float = Field(
        default=0,  # This value should be provided when constructing CorpusRecommendationModel for Firefox New Tab.
        description='Firefox clients require an integer id. Other clients should use `id` instead of this field. '
                    'tileId uniquely identifies the ScheduledSurface, CorpusItem, and scheduled_date. '
                    'tileId is greater than 0 and less than 2^53 to fit in a Javascript number (64-bit IEEE 754 float).'
                    ' The field type is a Float because a GraphQL Int is limited to 32 bit.')

    corpus_item: Optional[CorpusItemModel] = Field(description='Content meta data.')

    reason: Optional[RecommendationReasonModel] = Field(
        default=None,
        description='Reason why this CorpusItem is recommended to the user, or null if no reason is available.')
