import logging
import aioboto3
from typing import List
import json

from aws_xray_sdk.core import xray_recorder

from app import config
from app.exceptions.personalization_error import PersonalizationError
from app.models.corpus_item_model import CorpusItemModel
from app.models.user_ids import UserIds


class UserImpressionCapProvider:
    _FEATURE_GROUP_VERSION = 2
    _FEATURE_NAMES: List[str] = [
        'CORPUS_IDS',
    ]

    def __init__(self, aioboto3_session: aioboto3.session.Session):
        self.aioboto3_session = aioboto3_session

    @xray_recorder.capture_async('UserImpressionCapProvider.get')
    async def get(self, user_ids: UserIds) -> List[CorpusItemModel]:
        """
        Get corpus item ids that should be filtered in slates that are shown to the user with given user.
        :param user_ids: user ids for the corresponding list of impressed items
        :return: list of corpus item ids that should be filtered.
        """
        if not user_ids.hashed_user_id:
            raise PersonalizationError("hashed_user_id must be provided for personalized impression filtering")

        impressed_item_ids = await self._query_item_list(user_ids)
        if not impressed_item_ids:
            logging.info(f"No returned impressed item list for hashed_user_id={user_ids.hashed_user_id}")

        return [CorpusItemModel(id=id) for id in impressed_item_ids]

    @classmethod
    def get_feature_group_name(cls):
        return f'{config.ENV}-user-impressions-v{cls._FEATURE_GROUP_VERSION}'

    @xray_recorder.capture_async('UserImpressedList._query_item_list')
    async def _query_item_list(self, user_ids: UserIds) -> List[str]:
        """
        Queries impressed items to be filtered from the Feature Group.

        :param user_ids: Feature record ID to query
        :return: List with all items that should be filtered from slates/lineups returned by the recommendation-api
                 for the user corresponding to user_id
        """
        async with self.aioboto3_session.client('sagemaker-featurestore-runtime') as featurestore:
            record = await featurestore.get_record(
                FeatureGroupName=self.get_feature_group_name(),
                RecordIdentifierValueAsString=user_ids.hashed_user_id,
                FeatureNames=self._FEATURE_NAMES
            )

        if "Record" in record:
            return json.loads(record["Record"][0]['ValueAsString'])
        else:
            return []
