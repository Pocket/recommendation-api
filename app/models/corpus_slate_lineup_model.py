from datetime import datetime, timezone
from enum import Enum
from typing import List, Optional
from uuid import uuid4

from pydantic import BaseModel, Field

from app.models.corpus_slate_model import CorpusSlateModel
from app.models.localemodel import LocaleModel
from app.models.unleash_assignment import UnleashAssignmentModel


class RecommendationSurfaceId(Enum):
    """
    Defines the possible recommendation surfaces. Currently, these are distinct from the GraphQL 'scheduled surfaces',
    but eventually we'll probably want to merge these concepts.
    """
    HOME = 'HOME'


class CorpusSlateLineupModel(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()), description='UUID')
    slates: List[CorpusSlateModel] = Field(description='Slates.')
    recommended_at: datetime = Field(
        default_factory=lambda: datetime.now(tz=timezone.utc),
        description='UTC time when the slate was recommended')
    recommendation_surface_id: RecommendationSurfaceId = Field(
        description='Identifies the recommendation surface that the slate lineup will be shown on.')
    locale: LocaleModel = Field(description='Locale that the recommendations and slate copy is targeted to')
    experiment: Optional[UnleashAssignmentModel] = None
