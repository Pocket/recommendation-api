import os
import random
import uuid
from typing import List

import pytest

from app.config import ROOT_DIR
from app.data_providers.corpus.corpus_api_client import CorpusApiClient
from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.models.corpus_item_model import CorpusItemModel
from tests.functional.test_util.caching import reset_caches
from tests.mocks.feature_store_mock import FeatureStoreMock


@pytest.fixture(scope='class')
def corpus_feature_group_client():
    feature_store_mock = FeatureStoreMock(
        feature_group_name=CorpusFeatureGroupClient.get_feature_group_name(),
        records_json_path=os.path.join(ROOT_DIR, 'tests/assets/json/corpus_candidate_sets.json')
    )

    return CorpusFeatureGroupClient(aioboto3_session=feature_store_mock.aioboto3)


CORPUS_API_CLIENT_FIXTURE_ITEM_COUNT = 48


class DummyCorpusApiClient(CorpusApiClient):
    async def fetch(
            self,
            corpus_id: str,
    ) -> List[CorpusItemModel]:
        return [
            CorpusItemModel(id=str(uuid.uuid4()), topic="BUSINESS") for _ in range(CORPUS_API_CLIENT_FIXTURE_ITEM_COUNT)
        ]

    def get_scheduled_date(self, corpus_item_id: str) -> str:
        return random.choice(['2023-04-17', '2023-04-18'])


@pytest.fixture
def corpus_api_client():
    return DummyCorpusApiClient(pocket_graph_client_session=None)


class DummyCorpusApiClientWithoutScheduledDate(DummyCorpusApiClient):
    def get_scheduled_date(self, corpus_item_id: str) -> str:
        # Simulate invalid data coming back from the Graph.
        return None


@pytest.fixture
def corpus_api_client_without_scheduled_date():
    return DummyCorpusApiClientWithoutScheduledDate(pocket_graph_client_session=None)
