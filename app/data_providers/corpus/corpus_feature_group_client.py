import itertools
from asyncio import gather
from typing import Dict, List

import json

import aioboto3
from aiocache import cached

from app import config
from app.data_providers.corpus.corpus_fetchable import CorpusFetchable
from app.models.corpus_item_model import CorpusItemModel


class CorpusFeatureGroupClient(CorpusFetchable):
    """
    Corpus candidate set for showing stories during setup moment onboarding.
    """
    _FEATURE_GROUP_VERSION = 1

    def __init__(self, aioboto3_session: aioboto3.session.Session):
        self.aioboto3_session = aioboto3_session

    async def get_corpus_items(self, corpus_ids: [str]) -> List[CorpusItemModel]:
        # Fetch Corporeal Candidates
        aggregate_corpus_response = await gather(*(self.fetch(corpus_id) for corpus_id in corpus_ids))

        return list(itertools.chain(*aggregate_corpus_response))

    async def fetch(
            self,
            corpus_id: str,
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

    # TODO: Replace with OT segment
    #@xray_recorder.capture_async('CorpusFeatureGroupClient._query_corpus_items')
    @cached(ttl=600)
    async def _query_corpus_items(self, corpus_candidate_set_id: str) -> List[Dict[str, str]]:
        """
        Queries impressed items to be filtered from the Feature Group.

        :param corpus_candidate_set_id: Feature record ID to query
        :return: List of corpus item dicts, with keys id, topic.
        """

        async with self.aioboto3_session.client('sagemaker-featurestore-runtime') as featurestore:
            record = await featurestore.get_record(
                FeatureGroupName=self.get_feature_group_name(),
                RecordIdentifierValueAsString=str(corpus_candidate_set_id),
                FeatureNames=['corpus_items']
            )

        if "Record" not in record:
            raise ValueError(f"corpus-candidate-sets")

        return json.loads(record["Record"][0]['ValueAsString'])
