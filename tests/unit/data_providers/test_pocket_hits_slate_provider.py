import pytest
from freezegun import freeze_time

from app.data_providers.slate_providers.pocket_hits_slate_provider import PocketHitsSlateProvider
from app.models.corpus_slate_lineup_model import RecommendationSurfaceId
from app.models.localemodel import LocaleModel
from app.models.recommendation_reason_type import RecommendationReasonType


@pytest.fixture
def pocket_hits_slate_provider(corpus_feature_group_client, corpus_engagement_provider, en_us_home_translations):
    return PocketHitsSlateProvider(
        corpus_feature_group_client=corpus_feature_group_client,
        corpus_engagement_provider=corpus_engagement_provider,
        recommendation_surface_id=RecommendationSurfaceId.HOME,
        locale=LocaleModel.en_US,
        home_translations=en_us_home_translations,
    )


@pytest.mark.asyncio
class TestPocketHitsSlateProvider:

    async def test_get_slate_reason_type(self, pocket_hits_slate_provider):
        slate = await pocket_hits_slate_provider.get_slate()

        assert RecommendationReasonType.POCKET_HITS == slate.recommendation_reason_type

    @freeze_time("2022-10-25 6:00:00", tz_offset=0)  # Tue 6am Oct 25th, 2022 UTC was Tue 2am Oct 25th EDT
    async def test_headline_before_cutoff_time(self, pocket_hits_slate_provider):
        slate = await pocket_hits_slate_provider.get_slate()

        assert slate.headline == 'Today’s Pocket Hits'
        assert slate.subheadline == 'Monday, October 24'  # At 2am EDT the date should be the previous day.

    @freeze_time("2022-10-25 7:00:00", tz_offset=0)  # Tue 2pm Oct 25th, 2022 UTC was Tue 3am Oct 25th EDT
    async def test_headline_after_cutoff_time(self, pocket_hits_slate_provider):
        slate = await pocket_hits_slate_provider.get_slate()

        assert slate.headline == 'Today’s Pocket Hits'
        assert slate.subheadline == 'Tuesday, October 25'  # At 3am EDT the date should be the current day.
