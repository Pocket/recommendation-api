import random
from typing import List, Optional

from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.data_providers.slate_providers.slate_provider import SlateProvider
from app.models.corpus_item_model import CorpusItemModel
from app.models.corpus_slate_model import CorpusSlateModel
from app.models.link import LinkModel
from app.models.topic import TopicModel


class TopicSlateProvider(SlateProvider):

    # Map Corpus topic (keys) to the Corpus candidate set id (values).
    # TODO: Instead of hardcoding these values, consider moving them to the Sagemaker Feature Store, or a database.
    _TOPIC_CANDIDATE_SETS = {
        'SELF_IMPROVEMENT': '78f23805-66e7-46d5-9cfc-ff10a0335265',
        'POLITICS': '0a024f6e-b7e7-4be2-bc86-b603c26fc351',
        'BUSINESS': 'dd57c71e-049e-4f3a-b003-9d44d693d8c4',
        'HEALTH_FITNESS': 'ec9cd333-b136-419e-a091-d1f9ae573f27',
        'SCIENCE': 'cdc738bb-bf71-4794-b95f-cf4e0ea77572',
        'PARENTING': 'b09945d0-b211-44e6-afc8-c3f44997937d',
        'EDUCATION': '30a4f4e6-f4ec-4c8a-99f7-d75c147539ec',
        'CORONAVIRUS': '7d5b18b4-417d-47a5-8e55-a53ab7edea7b',
        'TECHNOLOGY': '2c657e89-3690-47fb-b08f-7930a87211c0',
        'FOOD': '952c8207-0112-46bc-ad06-a2d2c0163422',
        'ENTERTAINMENT': '079b190b-ad77-4be9-bf87-7261416c909e',
        'PERSONAL_FINANCE': '5e30b37b-e167-43a0-ac12-8c7b2cc78599',
        'CAREER': 'c5b8933f-83b5-4867-95af-9a025fe69115',
        'TRAVEL': 'e062d6dc-3fb9-4bbd-8ff4-6728a2054ffb',
        'SPORTS': '6f3ed598-0720-471a-bffc-3021aab2464c',
        'GAMING': '465cadb7-638d-41b7-8914-3d6c42f53b57',
    }

    def __init__(self, corpus_feature_group_client: CorpusFeatureGroupClient, topic: TopicModel):
        super().__init__(corpus_feature_group_client)
        self.topic = topic

    @property
    def candidate_set_id(self) -> str:
        return self._TOPIC_CANDIDATE_SETS[self.topic.corpus_topic_id]

    @property
    def headline(self) -> str:
        return self.topic.name

    @property
    def more_link(self) -> Optional[LinkModel]:
        return LinkModel(text=f'Explore more {self.topic.name}', url=f'https://getpocket.com/explore/{self.topic.slug}')

    async def rank_corpus_items(self, items: List[CorpusItemModel], *args, **kwargs) -> List[CorpusItemModel]:
        """
        :param items: Candidate corpus items
        :return: Randomizes items.
        """
        random.shuffle(items)
        return items
