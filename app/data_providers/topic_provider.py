from enum import Enum

import aioboto3
from aiocache import cached
from boto3.dynamodb.conditions import Key
from typing import List, Optional, Set, Sequence, Dict, Any

from app.config import dynamodb as dynamodb_config
from app.data_providers.translation import TranslationProvider
from app.models.localemodel import LocaleModel
from app.models.topic import TopicModel


class TopicProvider:

    def __init__(
            self,
            aioboto3_session: aioboto3.session.Session,
            locale: LocaleModel,
            translation_provider: TranslationProvider,
    ):
        self.aioboto3_session = aioboto3_session
        self.locale = locale
        self.topic_translations = translation_provider.get_translations(locale, 'topics.json')

    async def get_all(self) -> List[TopicModel]:
        """
        Retrieves all topics from dynamo db

        :return: a list of TopicModel objects
        """
        topic_dicts = [{**t, **self.topic_translations.get(t['corpus_topic_id'], {})} for t in await self._scan_table()]
        return sorted(list(map(TopicModel.from_dict, topic_dicts)), key=lambda topic: topic.slug)

    @cached(ttl=600, key='TopicProvider._scan_table')
    async def _scan_table(self) -> List[Dict[str, Any]]:
        """
        :return: Items
        """
        async with self.aioboto3_session.resource('dynamodb', endpoint_url=dynamodb_config['endpoint_url']) as db:
            table = await db.Table(dynamodb_config['metadata']['table'])
            response = await table.scan()
            return response['Items']

    async def get_topics_by_legacy_id(self, topics_ids: Sequence[str]) -> List[TopicModel]:
        """
        :param topics_ids: List or tuple of legacy UUID topic ids. Invalid ids are ignored.
        :return: A list of TopicModel objects for the given topic_ids.
        """
        all_topics = await self.get_all()
        topics_by_id = {topic.id: topic for topic in all_topics}
        return [topics_by_id[topic_id] for topic_id in topics_ids if topic_id in topics_by_id]

    async def get_topics_by_corpus_topic_id(self, topics_ids: Sequence[str]) -> List[TopicModel]:
        """
        :param topics_ids: List or tuple of corpus topic ids. Invalid ids are ignored.
        :return: A list of TopicModel objects for the given topic_ids.
        """
        all_topics = await self.get_all()
        topics_by_id = {topic.corpus_topic_id: topic for topic in all_topics}
        return [topics_by_id[topic_id] for topic_id in topics_ids if topic_id in topics_by_id]
