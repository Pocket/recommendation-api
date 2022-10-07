from typing import List, Dict

from app.data_providers.slate_providers.slate_provider import SlateProvider
from app.models.corpus_item_model import CorpusItemModel
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
        return 'Recommended for your interests'

    async def rank_corpus_items(
            self,
            items: List[CorpusItemModel],
            preferred_topics: List[TopicModel] = None,
            recommendation_count: int = None,
            *args,
            **kwargs
    ) -> List[CorpusItemModel]:
        """
        :param items: Candidate corpus items
        :param preferred_topics: Topics explicitly preferred by the user.
        :param recommendation_count: Maximum recommendations to return.
        :return: Ranks items based on topic preferences, with topic spreading.
        """
        return rank_by_preferred_topics(items, preferred_topics, recommendation_count)

    async def get_recommendations(
            self,
            ranked_items: List[CorpusItemModel],
            preferred_topics: List[TopicModel] = None,
            *args,
            **kwargs,
    ) -> List[CorpusRecommendationModel]:
        """
        :return: Corpus recommendations ranked based on the preferred topics
        """
        preferred_topic_by_id: Dict[str, TopicModel] = {t.corpus_topic_id: t for t in preferred_topics}

        return [
            CorpusRecommendationModel(
                corpus_item=item,
                reason=RecommendationReasonModel(
                    name=preferred_topic_by_id[item.topic].name,
                    type=RecommendationReasonType.PREFERRED_TOPICS,
                ) if item.topic in preferred_topic_by_id else None,  # Only put reason on items with preferred topic
            ) for item in ranked_items
        ]
