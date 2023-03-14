import os
import pytest

import app.config
from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.models.corpus_item_model import CorpusItemModel
from tests.mocks.feature_store_mock import FeatureStoreMock


@pytest.mark.asyncio  # This pytest-asyncio decorator allows us to use an async side_effect
class TestCorpusFeatureGroupClient:

    SLATE_ID = 'f99178fb-6bd0-4fa1-8109-cda181b697f6'  # Matches the slate_id in firefox_new_tab_engagement.json

    def setup(self):
        self.feature_store_mock = FeatureStoreMock(
            feature_group_name=CorpusFeatureGroupClient.get_feature_group_name(),
            records_json_path=os.path.join(app.config.ROOT_DIR, 'tests/assets/json/corpus_candidate_sets.json')
        )

        # This is the client that's under test.
        self.client = CorpusFeatureGroupClient(aioboto3_session=self.feature_store_mock.aioboto3)

    async def test_get_existing_records(self):
        """
        Test the case where the queried records exist in the Feature Group.
        """
        corpus_items = await self.client.get_corpus_items(
            list(self.feature_store_mock.records_by_id.keys())
        )

        # Assert corpus_items reflect the corpus_candidate_sets.json fixture data.
        assert len(corpus_items) > 100
        assert corpus_items[0].dict() == {"id": "cce6370a-3f54-47e5-a14a-5422cb581123", "topic": "HEALTH_FITNESS",
                                          "scheduled_date": None}

        assert all(type(item) == CorpusItemModel for item in corpus_items)

    async def test_get_non_existing_record(self):
        """
        Test that a ValueError is raised when querying a record that does not exist.
        """
        with pytest.raises(ValueError):
            await self.client.get_corpus_items(corpus_ids=['i-do-not-exist'])
