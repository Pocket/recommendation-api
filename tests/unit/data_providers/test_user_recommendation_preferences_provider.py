import datetime
import json
import os

import pytest
from aws_xray_sdk import global_sdk_config

from app.config import ROOT_DIR
from app.data_providers.user_recommendation_preferences_provider import UserRecommendationPreferencesProvider
from app.models.user_recommendation_preferences import UserRecommendationPreferencesModel
from tests.assets.topics import technology_topic, business_topic
from tests.mocks.feature_store_mock import FeatureStoreMock


@pytest.fixture
def feature_store_mock():
    return FeatureStoreMock(
        feature_group_name=UserRecommendationPreferencesProvider.get_feature_group_name(),
        identifier_feature_name='user_id',
        records_json_path=os.path.join(ROOT_DIR, 'tests/assets/json/user_recommendation_preferences.json')
    )


@pytest.fixture
def preferences_provider(feature_store_mock, topic_provider_en_us) -> UserRecommendationPreferencesProvider:
    return UserRecommendationPreferencesProvider(
        aioboto3_session=feature_store_mock.aioboto3,
        topic_provider=topic_provider_en_us,
    )


@pytest.mark.asyncio  # This pytest-asyncio decorator allows us to use an async side_effect
class TestUserRecommendationPreferencesProvider:

    def setup(self):
        global_sdk_config.set_sdk_enabled(False)
        self.existing_user_id = '12341234'  # Defined in the above JSON fixture

    async def test_put(self, preferences_provider, feature_store_mock):
        """
        Test the case where the queried records exist in the Feature Group.
        """
        model = UserRecommendationPreferencesModel(
            user_id='user-123',
            updated_at=datetime.datetime(2022, 6, 9, 12, 30),
            preferred_topics=[technology_topic],
        )

        await preferences_provider.put(model)

        # Assert corpus_items reflect the corpus_candidate_sets.json fixture data.
        record = feature_store_mock.records_by_id[model.user_id]
        features = {feature['FeatureName']: feature['ValueAsString'] for feature in record}

        assert features['user_id'] == model.user_id
        assert features['updated_at'] == '2022-06-09T12:30:00Z'

        preferred_topics_feature = json.loads(features['preferred_topics'])
        assert len(preferred_topics_feature) == 1
        assert preferred_topics_feature[0]['id'] == model.preferred_topics[0].id

    async def test_fetch(self, preferences_provider, feature_store_mock):
        """
        Test the case where the queried records exist in the Feature Group.
        """
        model = await preferences_provider.fetch(self.existing_user_id)

        # Assert model matches fixture data in user_recommendation_preferences.json
        assert model.user_id == self.existing_user_id
        assert model.preferred_topics == [business_topic, technology_topic]

    async def test_fetch_non_existing_user(self, preferences_provider):
        """
        Test the case where the queried records exist in the Feature Group.
        """
        model = await preferences_provider.fetch('9999')

        # Assert model matches fixture data in user_recommendation_preferences.json
        assert model is None
