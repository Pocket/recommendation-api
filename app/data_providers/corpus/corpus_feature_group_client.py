from typing import Dict, List

import json

import aioboto3
from aws_xray_sdk.core import xray_recorder

from app import config
from app.data_providers.corpus.corpus_fetchable import CorpusFetchable
from app.graphql.corpus_item import CorpusItem
from app.models.corpus_item_model import CorpusItemModel


class CorpusFeatureGroupClient(CorpusFetchable):
    """
    Corpus candidate set for showing stories during setup moment onboarding.
    """
    SETUP_MOMENT_CORPUS_CANDIDATE_SET_ID = 'deea0f06-9dc9-44a5-b864-fea4a4d0beb7'

    _FEATURE_GROUP_VERSION = 1
    _FEATURE_NAMES: List[str] = ['corpus_items']

    def __init__(self, aioboto3_session: aioboto3.session.Session = None):
        self.aioboto3_session = aioboto3_session if aioboto3_session else aioboto3.Session()

    async def get_ranked_corpus_items(
            self,
            corpus_id: str = SETUP_MOMENT_CORPUS_CANDIDATE_SET_ID,
            start_date: str = None,
            user_id=None,
    ) -> List[CorpusItemModel]:
        corpus_items_dicts = await self._query_corpus_items(corpus_id)
        corpus_items = [self.corpus_item_from_dict(d) for d in corpus_items_dicts]

        return corpus_items

    @classmethod
    def get_feature_group_name(cls):
        return f'{config.ENV}-corpus-candidate-sets-v{cls._FEATURE_GROUP_VERSION}'

    @classmethod
    def corpus_item_from_dict(cls, obj: Dict[str, str]) -> CorpusItemModel:
        # Convert keys to lowercase.
        return CorpusItemModel.parse_obj({k.lower(): v for k, v in obj.items()})

    @xray_recorder.capture_async('UserImpressedList._query_item_list')
    async def _query_corpus_items(self, corpus_candidate_set_id: str) -> List[Dict[str, str]]:
        """
        Queries impressed items to be filtered from the Feature Group.

        :param corpus_candidate_set_id: Feature record ID to query
        :return: List with all items that should be filtered from slates/lineups returned by the recommendation-api
                 for the user corresponding to user_id
        """

        async with self.aioboto3_session.client('sagemaker-featurestore-runtime') as featurestore:
            record = await featurestore.get_record(
                FeatureGroupName=self.get_feature_group_name(),
                RecordIdentifierValueAsString=str(corpus_candidate_set_id),
                FeatureNames=self._FEATURE_NAMES
            )

        if "Record" not in record:
            raise ValueError(f"corpus-candidate-sets")

        return json.loads(record["Record"][0]['ValueAsString'])
