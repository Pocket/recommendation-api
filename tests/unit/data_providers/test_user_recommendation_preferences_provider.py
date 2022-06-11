import datetime
import json
import os

import aioboto3
import pytest

from aws_xray_sdk import global_sdk_config

from app.config import ROOT_DIR
from app.data_providers.user_recommendation_preferences_provider import UserRecommendationPreferencesProvider
from app.models.user_recommendation_preferences import UserRecommendationPreferencesModel
from tests.assets.topics import technology_topic
from tests.mocks.feature_store_mock import FeatureStoreMock


@pytest.mark.asyncio  # This pytest-asyncio decorator allows us to use an async side_effect
class TestUserRecommendationPreferencesProvider:

    def setup(self):
        global_sdk_config.set_sdk_enabled(False)

        self.feature_store_mock = FeatureStoreMock(
            feature_group_name=UserRecommendationPreferencesProvider.get_feature_group_name(),
            identifier_feature_name='user_id',
            records_json_path=os.path.join(ROOT_DIR, 'tests/assets/json/user_recommendation_preferences.json')
        )

        # This is the client that's under test.
        self.client = UserRecommendationPreferencesProvider(self.feature_store_mock.aioboto3)

    async def test_put(self):
        """
        Test the case where the queried records exist in the Feature Group.
        """
        model = UserRecommendationPreferencesModel(
            user_id='user-123',
            updated_at=datetime.datetime(2022, 6, 9, 12, 30),
            preferred_topics=[technology_topic],
        )

        await self.client.put(model)

        # Assert corpus_items reflect the corpus_candidate_sets.json fixture data.
        record = self.feature_store_mock.records_by_id[model.user_id]
        features = {feature['FeatureName']: feature['ValueAsString'] for feature in record}

        assert features['user_id'] == model.user_id
        assert features['updated_at'] == '2022-06-09T12:30:00Z'

        preferred_topics_feature = json.loads(features['preferred_topics'])
        assert len(preferred_topics_feature) == 1
        assert preferred_topics_feature[0]['id'] == model.preferred_topics[0].id
        assert preferred_topics_feature[0]['corpus_topic_id'] == model.preferred_topics[0].corpus_topic_id

    async def test_fetch(self):
        """
        Test the case where the queried records exist in the Feature Group.
        """
        model = await self.client.fetch('12341234')

        print(model)
