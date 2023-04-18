from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, Field, validator

from app.models.api_client import ApiClient
from app.models.corpus_slate_lineup_model import RecommendationSurfaceId, CorpusSlateLineupModel
from app.models.corpus_slate_model import CorpusSlateModel
from app.models.localemodel import LocaleModel
from app.models.request_user import RequestUser
from app.models.unleash_assignment import UnleashAssignmentModel


class CorpusRecommendationsSendEvent(BaseModel):
    """
    Models the event where recommendations are sent by Recommendation API to the client.
    """
    recommended_at: datetime = Field(
        default_factory=lambda: datetime.now(tz=timezone.utc),
        description='UTC time when when the recommendations were sent by the Recommendation API.')
    recommendation_surface_id: RecommendationSurfaceId = Field(
        description='Identifies the recommendation surface that the recommendations will be shown on.')
    locale: LocaleModel = Field(description='Locale that the recommendations and slate copy is targeted to')
    corpus_slate: Optional[CorpusSlateModel] = Field(
        default=None,
        description='The recommended CorpusSlate. Either corpus_slate_lineup or corpus_slate must be set.'
    )
    corpus_slate_lineup: Optional[CorpusSlateLineupModel] = Field(
        default=None,
        description='The recommended CorpusSlateLineup. Either corpus_slate_lineup or corpus_slate must be set.'
    )
    user: Optional[RequestUser] = None
    api_client: Optional[ApiClient] = None
    experiment: Optional[UnleashAssignmentModel] = None

    @validator('corpus_slate_lineup', always=True)
    def check_slate_or_lineup(cls, v, values):
        if not values.get('corpus_slate') and not v:
            raise ValueError('Either corpus_slate or corpus_slate_lineup is required')
        return v
