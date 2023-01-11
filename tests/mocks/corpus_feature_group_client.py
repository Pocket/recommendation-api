import os

import pytest

from app.config import ROOT_DIR
from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from tests.mocks.feature_store_mock import FeatureStoreMock


@pytest.fixture(scope='class')
def corpus_feature_group_client():
    feature_store_mock = FeatureStoreMock(
        feature_group_name=CorpusFeatureGroupClient.get_feature_group_name(),
        records_json_path=os.path.join(ROOT_DIR, 'tests/assets/json/corpus_candidate_sets.json')
    )

    return CorpusFeatureGroupClient(aioboto3_session=feature_store_mock.aioboto3)
