import json
from typing import Dict, List, Any

import aioboto3
from aws_xray_sdk.core import xray_recorder

from app import config
from app.models.topic import TopicModel
from app.models.user_recommendation_preferences import UserRecommendationPreferencesModel


class UserRecommendationPreferencesProvider:
    _FEATURE_GROUP_VERSION = 1

    def __init__(self, aioboto3_session: aioboto3.session.Session = None):
        self.aioboto3_session = aioboto3_session if aioboto3_session else aioboto3.Session()

    async def put(self, model: UserRecommendationPreferencesModel):
        """
        Inserts or updates user recommendation preferences.
        :param model:
        """
        await self._put_feature_store_record(model)

    @classmethod
    def get_feature_group_name(cls):
        return f'{config.ENV}-user-recommendation-preferences-v{cls._FEATURE_GROUP_VERSION}'

    @xray_recorder.capture_async('UserRecommendationPreferencesProvider._put_feature_store_record')
    async def _put_feature_store_record(self, model: UserRecommendationPreferencesModel):
        """
        Writes a record to the feature group.
        :param model:
        """
        async with self.aioboto3_session.client('sagemaker-featurestore-runtime') as featurestore:
            await featurestore.put_record(
                FeatureGroupName=self.get_feature_group_name(),
                Record=self._feature_store_record_from_model(model)
            )

    @classmethod
    def _feature_store_record_from_model(cls, model: UserRecommendationPreferencesModel) -> List[Dict[str, Any]]:
        return [
            {
                'FeatureName': 'user_id',
                'ValueAsString': model.user_id
            },
            {
                'FeatureName': 'updated_at',
                'ValueAsString': model.updated_at.strftime("%Y-%m-%dT%H:%M:%SZ")
            },
            {
                'FeatureName': 'preferred_topics',
                'ValueAsString': json.dumps([cls._topic_feature_from_topic(t) for t in model.preferred_topics])
            },
        ]

    @classmethod
    def _topic_feature_from_topic(cls, topic: TopicModel) -> Dict[str, str]:
        return {'id': topic.id}
