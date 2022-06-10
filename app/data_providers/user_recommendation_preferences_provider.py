import json
from typing import Dict, List, Any, Optional

import aioboto3
from aws_xray_sdk.core import xray_recorder

from app import config
from app.models.topic import TopicModel
from app.models.user_recommendation_preferences import UserRecommendationPreferencesModel


class UserRecommendationPreferencesProvider:
    _FEATURE_GROUP_VERSION = 1
    _FEATURE_NAMES: List[str] = ['user_id', 'updated_at', 'preferred_topics']

    def __init__(self, aioboto3_session: aioboto3.session.Session = None):
        self.aioboto3_session = aioboto3_session

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

    @xray_recorder.capture_async('UserRecommendationPreferencesProvider._get_feature_store_record')
    async def _get_feature_store_record(self, user_id: str) -> Optional[Dict[str, Any]]:
        """
        Queries user recommendation preferences from the Feature Group.

        :param user_id:
        :return: List with all items that should be filtered from slates/lineups returned by the recommendation-api
                 for the user corresponding to user_id
        """

        async with self.aioboto3_session.client('sagemaker-featurestore-runtime') as featurestore:
            record = await featurestore.get_record(
                FeatureGroupName=self.get_feature_group_name(),
                RecordIdentifierValueAsString=str(user_id),
                FeatureNames=self._FEATURE_NAMES
            )

        if "Record" not in record:
            # We do not have any preferences yet for this user_id.
            return None

        # Map list of features to dict.
        return {feature['FeatureName']: feature['ValueAsString'] for feature in record}

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
        return {'id': topic.id, 'corpus_topic_id': topic.corpus_topic_id}
