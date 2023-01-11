import os

import pytest

from app import config
from app.config import ROOT_DIR
from app.data_providers.feature_group.corpus_engagement_provider import CorpusEngagementProvider
from app.data_providers.feature_group.feature_group_client import FeatureGroupClient
from mocks.feature_store_mock import FeatureStoreMock


@pytest.fixture
def corpus_engagement_provider(corpus_feature_group_client):
    feature_store_mock = FeatureStoreMock(
        feature_group_name=f'{config.ENV}-corpus-engagement-v1',
        records_json_path=os.path.join(ROOT_DIR, 'tests/assets/json/empty_feature_group.json')
    )

    feature_group_client = FeatureGroupClient(aioboto3_session=feature_store_mock.aioboto3)

    return CorpusEngagementProvider(feature_group_client)
