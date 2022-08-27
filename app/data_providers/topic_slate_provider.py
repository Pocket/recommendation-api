import random
import uuid
from asyncio import gather
from datetime import datetime, timezone
from typing import List

from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.models.corpus_item_model import CorpusItemModel
from app.models.corpus_recommendation_model import CorpusRecommendationModel
from app.models.corpus_slate_model import CorpusSlateModel
from app.models.topic import TopicModel


class TopicSlateProvider:

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

    def __init__(self, corpus_feature_group_client: CorpusFeatureGroupClient):
        self.corpus_feature_group_client = corpus_feature_group_client

    async def get_slates(self, topics: List[TopicModel], recommendation_count: int) -> List[CorpusSlateModel]:
        return list(await gather(*[
            self.get_slate(topic, recommendation_count=recommendation_count) for topic in topics
        ]))

    async def get_slate(self, topic: TopicModel, recommendation_count: int) -> CorpusSlateModel:
        candidate_set_id = self._TOPIC_CANDIDATE_SETS[topic.corpus_topic_id]
        items = await self.corpus_feature_group_client.get_corpus_items([candidate_set_id])
        if len(items) > recommendation_count:
            items = random.sample(items, k=recommendation_count)

        recommendations = [CorpusRecommendationModel(id=str(uuid.uuid4()), corpus_item=item) for item in items]

        return CorpusSlateModel(
            id=str(uuid.uuid4()),
            recommended_at=datetime.now(tz=timezone.utc),
            headline=topic.name,
            recommendations=recommendations,
        )
