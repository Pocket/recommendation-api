import random
from typing import List, Optional

from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.data_providers.slate_providers.candidate_sets import get_topic_candidate_set
from app.data_providers.slate_providers.slate_provider import SlateProvider
from app.models.corpus_item_model import CorpusItemModel
from app.models.link import LinkModel
from app.models.localemodel import LocaleModel
from app.models.topic import TopicModel


class TopicSlateProvider(SlateProvider):
    def __init__(self, topic: TopicModel, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.topic = topic

    def __str__(self):
        return f'{self.__class__.__name__}/{self.topic.corpus_topic_id}'

    @property
    def candidate_set_id(self) -> str:
        return get_topic_candidate_set(corpus_topic_id=self.topic.corpus_topic_id, locale=self.locale)

    @property
    def headline(self) -> str:
        return self.topic.name

    @property
    def more_link(self) -> Optional[LinkModel]:
        # Topic pages only exist for en-US.
        if self.locale == LocaleModel.en_US:
            return LinkModel(
                text=f'Explore more {self.topic.name}',
                url=f'https://getpocket.com/explore/{self.topic.slug}')
        else:
            return None

    async def rank_corpus_items(self, items: List[CorpusItemModel], *args, **kwargs) -> List[CorpusItemModel]:
        """
        :param items: Candidate corpus items
        :return: Randomizes items.
        """
        random.shuffle(items)
        return items
