import os

import pytest

from app import config
from app.config import ROOT_DIR
from app.data_providers.feature_group.corpus_engagement_provider import CorpusEngagementProvider
from app.data_providers.feature_group.feature_group_client import FeatureGroupClient
from tests.mocks.feature_store_mock import FeatureStoreMock


@pytest.fixture
def corpus_engagement_provider():
    feature_store_mock = FeatureStoreMock(
        feature_group_name=f'{config.ENV}-corpus-engagement-v1',
        records_json_path=os.path.join(ROOT_DIR, 'tests/assets/json/empty_feature_group.json')
    )

    feature_group_client = FeatureGroupClient(aioboto3_session=feature_store_mock.aioboto3)

    return CorpusEngagementProvider(feature_group_client)


@pytest.fixture
def failing_corpus_engagement_provider():
    # Initialize the client with a non-existing feature group 'foobar', to simulate a Feature Store failure scenario.
    feature_group_client = FeatureGroupClient(aioboto3_session=FeatureStoreMock('foobar').aioboto3)
    return CorpusEngagementProvider(feature_group_client)
