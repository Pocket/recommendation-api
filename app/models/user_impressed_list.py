import logging
import aioboto3
from typing import List
import json

from aws_xray_sdk.core import xray_recorder
from app.exceptions.personalization_error import PersonalizationError


class UserImpressedList:
    _FEATURE_GROUP_VERSION = 1
    _FEATURE_NAMES: List[str] = [
        'resolved_ids',
    ]

    @xray_recorder.capture_async('models.user_impressed_list.get')
    async def get(self, user_id: str) -> List[int]:
        """
        Get item_ids that should be filtered in slates that are shown to the user with give user_id
        :param user_id: user_id for the corresponding list of impressed items
        :return: list of item_ids that should be filtered.  -- TODO: content_ids?
        """
        if not user_id:
            raise PersonalizationError("user_id must be provided for personalized impression filtering")

        impressed_items = await self._query_item_list(user_id)
        if not impressed_items:
            logging.info(f"No returned impressed item list for user_id={user_id}")

        return impressed_items

    @classmethod
    def get_feature_group_name(cls):
        return 'user-impressions'

    @xray_recorder.capture_async('UserImpressedList._query_item_list')
    async def _query_item_list(self, user_id: str) -> List[int]:
        """
        Queries impressed items to be filtered from the Feature Group.

        :param user_id: Feature record ID to query
        :return: List with all items that should be filtered from slates/lineups returned by the recommendation-api
                 for the user corresponding to user_id
        """

        async with aioboto3.client('sagemaker-featurestore-runtime') as featurestore:
            # TODO: Update aioboto3 to v9 to improve performance with featurestore's batch_get_record.
            #       - boto3 1.17.92 introduces BatchGetRecord
            #       - aioboto3 8.3.0 pins aiobotocore[boto3]==1.2.2
            #       - aiobotocore 1.2.2 pins boto3 1.16.52
            record = await featurestore.get_record(
                FeatureGroupName=self.get_feature_group_name(),
                RecordIdentifierValueAsString=str(user_id),
                FeatureNames=self._FEATURE_NAMES
            )

        if "Record" in record:
            return json.loads(record["Record"][0]['ValueAsString'])
        else:
            return []
