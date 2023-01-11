from datetime import datetime, timedelta
from typing import Optional
import pytz

from app.data_providers.slate_providers.slate_provider import SlateProvider
from app.models.recommendation_reason_type import RecommendationReasonType


class PocketHitsSlateProvider(SlateProvider):

    @property
    def candidate_set_id(self) -> str:
        return '92411893-ebdb-4a43-ad29-aa79e56e2136'

    @property
    def subheadline(self) -> str:
        # The date is supposed to progress at 3AM EDT.
        dt = datetime.now(tz=pytz.timezone('America/New_York')) - timedelta(hours=3)
        # This slate is only shown on the en-US Home, so the subheadline does not need to be localized.
        return f'{dt:%A}, {dt:%B} {dt.day}'

    @property
    def recommendation_reason_type(self) -> Optional[RecommendationReasonType]:
        return RecommendationReasonType.POCKET_HITS
