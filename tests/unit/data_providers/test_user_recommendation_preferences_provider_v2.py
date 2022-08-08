import datetime
import json
import os
from unittest.mock import MagicMock

import pytest
from aws_xray_sdk import global_sdk_config

from app.config import ROOT_DIR
from app.data_providers.user_recommendation_preferences_provider import UserRecommendationPreferencesProviderV2
from app.models.user_recommendation_preferences import UserRecommendationPreferencesModelV2
from tests.assets.topics import technology_topic, business_topic
from tests.mocks.feature_store_mock import FeatureStoreMock
from tests.mocks.topic_provider import MockTopicProvider


@pytest.mark.asyncio  # This pytest-asyncio decorator allows us to use an async side_effect
class TestUserRecommendationPreferencesProviderV2:

    def setup(self):
        global_sdk_config.set_sdk_enabled(False)

        self.feature_store_mock = FeatureStoreMock(
            feature_group_name=UserRecommendationPreferencesProviderV2.get_feature_group_name(),
            identifier_feature_name='hashed_user_id',
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

    async def test_put(self):
        """
        Test the case where the queried records exist in the Feature Group.
        """
        model = UserRecommendationPreferencesModelV2(
            hashed_user_id='user-123',
            updated_at=datetime.datetime(2022, 6, 9, 12, 30),
            preferred_topics=[technology_topic],
        )

        await self.client.put(model)

        # Assert corpus_items reflect the corpus_candidate_sets.json fixture data.
        record = self.feature_store_mock.records_by_id[model.hashed_user_id]
        features = {feature['FeatureName']: feature['ValueAsString'] for feature in record}

        assert features['hashed_user_id'] == model.hashed_user_id
        assert features['updated_at'] == '2022-06-09T12:30:00Z'

        preferred_topics_feature = json.loads(features['preferred_topics'])
        assert len(preferred_topics_feature) == 1
        assert preferred_topics_feature[0]['id'] == model.preferred_topics[0].id

    async def test_fetch(self):
        """
        Test the case where the queried records exist in the Feature Group.
        """
        model = await self.client.fetch(self.existing_user_id)

        # Assert model matches fixture data in user_recommendation_preferences.json
        assert model.hashed_user_id == self.existing_user_id
        assert model.preferred_topics == [business_topic, technology_topic]

    async def test_fetch_non_existing_user(self):
        """
        Test the case where the queried records exist in the Feature Group.
        """
        model = await self.client.fetch('9999')

        # Assert model matches fixture data in user_recommendation_preferences.json
        assert model is None
