import os

import pytest
from freezegun import freeze_time

from app.config import ROOT_DIR
from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.data_providers.slate_providers.pocket_hits_slate_provider import PocketHitsSlateProvider
from app.models.recommendation_reason_type import RecommendationReasonType
from tests.mocks.feature_store_mock import FeatureStoreMock


@pytest.mark.asyncio
class TestPocketHitsSlateProvider:

    def setup(self):
        self.feature_store_mock = FeatureStoreMock(
            feature_group_name=CorpusFeatureGroupClient.get_feature_group_name(),
            records_json_path=os.path.join(ROOT_DIR, 'tests/assets/json/corpus_candidate_sets.json')
        )

        self.corpus_feature_group_client = CorpusFeatureGroupClient(aioboto3_session=self.feature_store_mock.aioboto3)
        self.slate_provider = PocketHitsSlateProvider(corpus_feature_group_client=self.corpus_feature_group_client)

    async def test_get_slate_reason_type(self):
        slate = await self.slate_provider.get_slate()

        assert RecommendationReasonType.POCKET_HITS == slate.recommendation_reason_type

    @freeze_time("2022-10-25 6:00:00", tz_offset=0)  # Tue 6am Oct 25th, 2022 UTC was Tue 2am Oct 25th EDT
    async def test_headline(self):
        slate = await self.slate_provider.get_slate()

        assert slate.headline == 'Today’s Pocket Hits'
        assert slate.subheadline == 'Monday, October 24'  # At 2am EDT the date should be the previous day.

    @freeze_time("2022-10-25 7:00:00", tz_offset=0)  # Tue 2pm Oct 25th, 2022 UTC was Tue 3am Oct 25th EDT
    async def test_headline(self):
        slate = await self.slate_provider.get_slate()

        assert slate.headline == 'Today’s Pocket Hits'
        assert slate.subheadline == 'Tuesday, October 25'  # At 3am EDT the date should be the current day.
