from typing import List, Optional

from app.data_providers.content_based import ContentBasedRecommender
from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.data_providers.feature_group.corpus_engagement_provider import CorpusEngagementProvider
from app.data_providers.slate_providers.slate_provider import SlateProvider
from app.data_providers.translation import TranslationProvider
from app.graphql.recommendation_reason_type import RecommendationReasonType
from app.models.corpus_item_model import CorpusItemModel
from app.models.corpus_slate_lineup_model import RecommendationSurfaceId
from app.models.localemodel import LocaleModel
from app.models.recommendation_reason_type import RecommendationReasonType
from app.models.topic import TopicModel
from app.rankers.algorithms import rank_by_impression_caps, thompson_sampling


class SimilarToEngagedSlateProvider(SlateProvider):
    def __init__(self, corpus_feature_group_client: CorpusFeatureGroupClient,
                 corpus_engagement_provider: CorpusEngagementProvider,
                 recommendation_surface_id: RecommendationSurfaceId, locale: LocaleModel,
                 translation_provider: TranslationProvider,
                 content_based_recommender: ContentBasedRecommender):
        super().__init__(corpus_feature_group_client, corpus_engagement_provider, recommendation_surface_id, locale,
                         translation_provider)
        self._content_based_recommender = content_based_recommender

    @property
    def candidate_set_id(self) -> str:
        #TODO change
        return '2066c835-a940-45ec-b1f7-267457d9e0a2'

    @property
    def recommendation_reason_type(self) -> Optional[RecommendationReasonType]:
        """
        :return: Recommendations in this slate are optimized to match the user's preferred topics.
        """
        return RecommendationReasonType.SIMILAR_TO_ENGAGED

    async def get_candidate_corpus_items(self, *args, **kwargs) -> List[CorpusItemModel]:
        """
        :return: The CorpusItems from the candidate set, without any rankers or filters applied.
        """

        resolved_ids = kwargs['user_items']
        ids =  await self._content_based_recommender.search(resolved_ids)
        return [CorpusItemModel(id=id) for id in ids]

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
        assert user_impression_capped_list is not None

        metrics = await self.corpus_engagement_provider.get(
            self.recommendation_surface_id, self.configuration_id, items)

        items = thompson_sampling(
            recs=items,
            metrics=metrics,
            trailing_period=14,  # A long period might work better given that some topics get few impressions
            default_alpha_prior=20,  # beta * P95 item CTR for this slate (1.6%)
            default_beta_prior=1200)  # 5% of average daily item impressions for this slate

        items = rank_by_impression_caps(items, user_impression_capped_list)
        return items
