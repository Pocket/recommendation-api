from typing import List, Optional
from uuid import uuid5, UUID

from app.data_providers.corpus.corpus_fetchable import CorpusFetchable
from app.data_providers.feature_group.corpus_engagement_provider import CorpusEngagementProvider
from app.data_providers.slate_providers.slate_provider import SlateProvider, HomeSlateProvider
from app.data_providers.translation import TranslationProvider
from app.graphql.recommendation_reason_type import RecommendationReasonType
from app.models.corpus_item_model import CorpusItemModel
from app.models.corpus_slate_lineup_model import RecommendationSurfaceId
from app.models.localemodel import LocaleModel
from app.models.recommendation_reason_type import RecommendationReasonType
from app.models.request_user import RequestUser
from app.rankers.algorithms import rank_by_impression_caps
from app.recommenders.hybrid_cf import HybridCFRecommender


class HybridCFSlateProvider(HomeSlateProvider):
    def __init__(self, corpus_fetchable: CorpusFetchable,
            corpus_engagement_provider: CorpusEngagementProvider,
            recommendation_surface_id: RecommendationSurfaceId, locale: LocaleModel,
            translation_provider: TranslationProvider,
                 hybrid_cf_recommender: HybridCFRecommender,
                 ):
        super().__init__(corpus_fetchable, corpus_engagement_provider, recommendation_surface_id, locale,
                         translation_provider)
        self._hybrid_cf_recommender = hybrid_cf_recommender

    @property
    def candidate_set_id(self) -> str:
        return self.recommendation_surface_id.value

    @property
    def candidate_set_uuid(self) -> UUID:
        """
        :return: A UUID uniquely identifying the candidate_set_id, as is expected by the base class.
        """
        # The UUID on the left is an arbitrary one.
        return uuid5(UUID('2fc20c7b-b6c7-4bcd-a234-122e10217471'), self.candidate_set_id)

    @property
    def recommendation_reason_type(self) -> Optional[RecommendationReasonType]:
        return RecommendationReasonType.HYBRID_CF_RECOMMENDER

    def can_recommend(self, user: RequestUser) -> bool:
        return self._hybrid_cf_recommender.can_recommend(user.hashed_user_id)

    async def get_candidate_corpus_items(self, *args, **kwargs) -> List[CorpusItemModel]:
        user = kwargs['user']
        # request more candidates to filter them later with the impression filter
        return self._hybrid_cf_recommender.recommend(user.hashed_user_id, k=100)

    async def rank_corpus_items(
            self,
            items: List[CorpusItemModel],
            user_impression_capped_list: List[CorpusItemModel] = None,
            *args,
            **kwargs,
    ) -> List[CorpusItemModel]:
        # These parameters have default value 'None' to match the signature of the base class, but they are required.
        assert user_impression_capped_list is not None

        items = rank_by_impression_caps(items, user_impression_capped_list)
        return items
