import os
from unittest.mock import MagicMock

import pytest
from aws_xray_sdk import global_sdk_config

from app.config import ROOT_DIR
from app.data_providers.user_recommendation_preferences_provider import UserRecommendationPreferencesProviderV2
from tests.mocks.feature_store_mock import FeatureStoreMock
from tests.mocks.topic_provider import MockTopicProvider
from tests.unit.data_providers.test_user_recommendation_preferences_provider import \
    TestUserRecommendationPreferencesProvider


@pytest.mark.asyncio  # This pytest-asyncio decorator allows us to use an async side_effect
class TestUserRecommendationPreferencesProviderV2(TestUserRecommendationPreferencesProvider):

    def setup(self):
        global_sdk_config.set_sdk_enabled(False)

        self.feature_store_mock = FeatureStoreMock(
            feature_group_name=UserRecommendationPreferencesProviderV2.get_feature_group_name(),
            identifier_feature_name='user_id',
            records_json_path=os.path.join(ROOT_DIR, 'tests/assets/json/user_recommendation_preferences_v2.json')
        )

        self.existing_user_id = 'aaaaaaaaaaaaaaa123'  # Defined in the above JSON fixture

        # This is the client that's under test.
        self.client = UserRecommendationPreferencesProviderV2(
            aioboto3_session=self.feature_store_mock.aioboto3,
            topic_provider=MockTopicProvider(aioboto3_session=MagicMock())
        )

    async def test_feature_group_name(self):
        assert self.client.get_feature_group_name().endswith('recommendation-preferences-v2')
