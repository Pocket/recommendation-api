import datetime
import os

import pytest
from freezegun import freeze_time

from app.config import ROOT_DIR
from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.data_providers.slate_providers.pocket_hits_slate_provider import PocketHitsSlateProvider
from app.models.recommendation_reason_type import RecommendationReasonType
from tests.assets.topics import business_topic
from tests.mocks.feature_store_mock import FeatureStoreMock


@pytest.fixture
def patch_datetime_now(monkeypatch):

    class mydatetime:
        @classmethod
        def now(cls):
            return datetime.datetime(2022, 10, 24, 14, 0, 0)  # Oct 24th was a Monday

    monkeypatch.setattr(datetime, 'datetime', mydatetime)


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

    @freeze_time("2022-10-24 16:00:00")  # Oct 24th, 2022 was a Monday
    async def test_headline(self, patch_datetime_now):
        slate = await self.slate_provider.get_slate()

        assert slate.headline == 'Monday’s Pocket Hits'
        assert slate.subheadline is None
