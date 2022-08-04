import json
from typing import Dict, List, Any, Optional

import aioboto3
import dateutil.parser
from aws_xray_sdk.core import xray_recorder

from app import config
from app.data_providers.topic_provider import TopicProvider
from app.models.topic import TopicModel
from app.models.user_recommendation_preferences import UserRecommendationPreferencesModel


class UserRecommendationPreferencesProvider:
    """
    Put or fetch user preferred topics in a Feature Group keyed on the integer user id.
    """

    _FEATURE_GROUP_VERSION = 1
    _FEATURE_NAMES: List[str] = ['user_id', 'updated_at', 'preferred_topics']

    def __init__(self, aioboto3_session: aioboto3.session.Session, topic_provider: TopicProvider):
        self.aioboto3_session = aioboto3_session
        self.topic_provider = topic_provider

    async def put(self, model: UserRecommendationPreferencesModel):
        """
        Inserts or updates user recommendation preferences.
        :param model:
        """
        await self._put_feature_store_record(model)

    async def fetch(self, user_id: str) -> Optional[UserRecommendationPreferencesModel]:
        """
        Gets user recommendation preferences for a given user id.
        :param user_id:
        :return:
        """
        if user_id is None:
            raise ValueError('user_id is required in UserRecommendationPreferencesProvider.fetch')

        feature_store_record = await self._get_feature_store_record(user_id)
        if not feature_store_record:
            return None

        model = await self._model_from_feature_store_record(feature_store_record)
        return model

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

        if 'Record' not in record:
            # We do not have any preferences yet for this user_id.
            return None

        # Map list of features to dict.
        return {feature['FeatureName']: feature['ValueAsString'] for feature in record['Record']}

    @xray_recorder.capture_async('UserRecommendationPreferencesProvider._model_from_feature_store_record')
    async def _model_from_feature_store_record(
        self, record: Optional[Dict[str, Any]],
    ) -> UserRecommendationPreferencesModel:
        preferred_topics = json.loads(record['preferred_topics'])

        return UserRecommendationPreferencesModel(
            user_id=record['user_id'],
            updated_at=dateutil.parser.isoparse(record['updated_at']),
            preferred_topics=await self.topic_provider.get_topics([t['id'] for t in preferred_topics])
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
                'ValueAsString': model.updated_at.strftime('%Y-%m-%dT%H:%M:%SZ')
            },
            {
                'FeatureName': 'preferred_topics',
                'ValueAsString': json.dumps([cls._topic_feature_from_topic(t) for t in model.preferred_topics])
            },
        ]

    @classmethod
    def _topic_feature_from_topic(cls, topic: TopicModel) -> Dict[str, str]:
        return {'id': topic.id}


class UserRecommendationPreferencesProviderV2(UserRecommendationPreferencesProvider):
    """
    Put or fetch user preferred topics in a Feature Group keyed on the hashed user id.
    """
    _FEATURE_GROUP_VERSION = 2
