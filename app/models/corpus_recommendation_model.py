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

    corpus_item: CorpusItemModel = Field(description='Content meta data.')

    reason: Optional[RecommendationReasonModel] = Field(
        default=None,
        description='Reason why this CorpusItem is recommended to the user, or null if no reason is available.')
