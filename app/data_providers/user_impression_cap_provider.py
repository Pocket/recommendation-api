import logging
import aioboto3
from typing import List


from app import config
from app.exceptions.personalization_error import PersonalizationError
from app.models.corpus_item_model import CorpusItemModel
from app.models.request_user import RequestUser


class UserImpressionCapProvider:
    _FEATURE_GROUP_VERSION = 2
    _FEATURE_NAMES: List[str] = [
        'CORPUS_IDS',
    ]

    def __init__(self, aioboto3_session: aioboto3.session.Session):
        self.aioboto3_session = aioboto3_session

    async def get(self, user: RequestUser) -> List[CorpusItemModel]:
        """
        Get corpus item ids that should be filtered in slates that are shown to the user with given user.
        :param user: user ids for the corresponding list of impressed items
        :return: list of corpus item ids that should be filtered.
        """
        if not user.hashed_user_id:
            raise PersonalizationError("hashed_user_id must be provided for personalized impression filtering")

        impressed_item_ids = await self._query_item_list(user)
        if not impressed_item_ids:
            logging.info(f"No returned impressed item list for hashed_user_id={user.hashed_user_id}")

        return [CorpusItemModel(id=id) for id in impressed_item_ids]

    @classmethod
    def get_feature_group_name(cls):
        return f'{config.ENV}-user-impressions-v{cls._FEATURE_GROUP_VERSION}'

    @staticmethod
    def parse_snowflake_array(arr: str) -> List[str]:
        return arr.strip('[]').split(',')

    # TODO: Replace with OT. 'UserImpressionCapProvider._query_item_list')
    async def _query_item_list(self, user: RequestUser) -> List[str]:
        """
        Queries impressed items to be filtered from the Feature Group.

        :param user: Feature record ID to query
        :return: List with all items that should be filtered from slates/lineups returned by the recommendation-api
                 for the user corresponding to user_id
        """
        async with self.aioboto3_session.client('sagemaker-featurestore-runtime') as featurestore:
            record = await featurestore.get_record(
                FeatureGroupName=self.get_feature_group_name(),
                RecordIdentifierValueAsString=user.hashed_user_id,
                FeatureNames=self._FEATURE_NAMES
            )

        if "Record" in record:
            return self.parse_snowflake_array(record["Record"][0]['ValueAsString'])
        else:
            return []
