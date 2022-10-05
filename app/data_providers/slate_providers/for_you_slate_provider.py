from typing import List, Dict

from app.data_providers.slate_providers.slate_provider import SlateProvider
from app.models.corpus_recommendation_model import CorpusRecommendationModel
from app.models.recommendation_reason_model import RecommendationReasonModel
from app.models.recommendation_reason_type import RecommendationReasonType
from app.models.topic import TopicModel
from app.rankers.algorithms import rank_by_preferred_topics


class ForYouSlateProvider(SlateProvider):

    @property
    def candidate_set_id(self) -> str:
        return '2066c835-a940-45ec-b1f7-267457d9e0a2'

    @property
    def headline(self) -> str:
        return 'For You'

    @property
    def subheadline(self) -> str:
        return 'Curated for your interests'

    async def get_recommendations(
            self, preferred_topics: List[TopicModel], recommendation_count: int
    ) -> List[CorpusRecommendationModel]:
        """
        :param preferred_topics: The user's preferred topics
        :param recommendation_count: The (maximum) number of recommendations to return
        :return: Corpus recommendations ranked based on preferred topics
        """
        items = await self.get_candidate_corpus_items()
        items = rank_by_preferred_topics(items, preferred_topics, recommendation_count)

        preferred_topic_by_id: Dict[str, TopicModel] = {t.corpus_topic_id: t for t in preferred_topics}

        return [
            CorpusRecommendationModel(
                corpus_item=item,
                reason=RecommendationReasonModel(
                    name=preferred_topic_by_id[item.topic].name,
                    type=RecommendationReasonType.PREFERRED_TOPICS,
                ) if item.topic in preferred_topic_by_id else None,  # Only put reason on items with preferred topic
            ) for item in items
        ]
