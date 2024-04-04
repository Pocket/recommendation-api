import random
from typing import List, Dict, Optional

from app.config import POCKET_HOME_V3_FEATURE_FLAG
from app.data_providers.slate_providers.slate_provider import HomeSlateProvider
from app.models.corpus_item_model import CorpusItemModel
from app.models.corpus_recommendation_model import CorpusRecommendationModel
from app.models.recommendation_reason_model import RecommendationReasonModel
from app.models.recommendation_reason_type import RecommendationReasonType
from app.models.topic import TopicModel
from app.rankers.algorithms import rank_by_preferred_topics, spread_topics, rank_by_impression_caps, thompson_sampling


class ForYouSlateProvider(HomeSlateProvider):

    @property
    def candidate_set_id(self) -> str:
        return '2066c835-a940-45ec-b1f7-267457d9e0a2'

    @property
    def recommendation_reason_type(self) -> Optional[RecommendationReasonType]:
        """
        :return: Recommendations in this slate are optimized to match the user's preferred topics.
        """
        return RecommendationReasonType.PREFERRED_TOPICS

    async def rank_corpus_items(
            self,
            items: List[CorpusItemModel],
            preferred_topics: List[TopicModel] = None,
            user_impression_capped_list: List[CorpusItemModel] = None,
            *args,
            **kwargs,
    ) -> List[CorpusItemModel]:
        """
        :param items: Candidate corpus items
        :param preferred_topics: Topics explicitly preferred by the user.
        :param user_impression_capped_list: List of impression capped CorpusItem ids for the user.
        :return: Ranks items based on topic preferences, with topic spreading.
        """
        # These parameters have default value 'None' to match the signature of the base class, but they are required.
        assert preferred_topics is not None
        assert user_impression_capped_list is not None

        assignment = await self.unleash_provider.get_assignment(POCKET_HOME_V3_FEATURE_FLAG)
        if assignment is None or assignment.assigned is False:
            # if they are not in the V3 Feature Flag, thompson sample
            metrics = await self.corpus_engagement_provider.get(
                self.recommendation_surface_id, self.configuration_id, items)

            items = thompson_sampling(
                recs=items,
                metrics=metrics,
                trailing_period=14,  # A long period might work better given that some topics get few impressions
                default_alpha_prior=20,  # beta * P95 item CTR for this slate (1.6%)
                default_beta_prior=1200)  # 5% of average daily item impressions for this slate

        items = rank_by_impression_caps(items, user_impression_capped_list)
        items = spread_topics(items)
        items = rank_by_preferred_topics(items, preferred_topics)
        return items

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
