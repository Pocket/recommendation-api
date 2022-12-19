import asyncio

import aioboto3
from typing import List, Optional, Dict

from aws_xray_sdk.core import xray_recorder

from app.data_providers.util import chunks

_BATCH_GET_RECORD_MAX_ITEMS = 10


class FeatureGroupClient:
    def __init__(self, aioboto3_session: aioboto3.session.Session):
        self.aioboto3_session = aioboto3_session

    async def batch_get_records(
            self, feature_group_name: str, ids: List[str], feature_names: Optional[List[str]]) -> List[Dict[str, str]]:
        """
        Queries impressed items to be filtered from the Feature Group.

        :param feature_group_name: Name of the Feature Group
        :param ids: list of record identifiers in string format.
        :param feature_names: List of names of Features to be retrieved. By default, all the Features are returned.
        :return: List with all items that should be filtered from slates/lineups returned by the recommendation-api
                 for the user corresponding to user_id
        """
        async with xray_recorder.capture_async(f'batch_get_records.{feature_group_name}'):
            async with self.aioboto3_session.client('sagemaker-featurestore-runtime') as featurestore:
                promises = [
                    featurestore.batch_get_record(
                        Identifiers=[
                            {
                                'FeatureGroupName': feature_group_name,
                                'RecordIdentifiersValueAsString': id_chunk,
                                'FeatureNames': feature_names,
                            }
                        ]
                    )
                    for id_chunk in chunks(ids, n=_BATCH_GET_RECORD_MAX_ITEMS)
                ]

                record_sets = await asyncio.gather(*promises)

        result = []
        for record_set in record_sets:
            for record in record_set['Records']:
                result.append(self.record_to_dict(record['Record']))

        return result

    @staticmethod
    def record_to_dict(record: List[Dict]) -> Dict:
        return {f['FeatureName']: f['ValueAsString'] for f in record}
