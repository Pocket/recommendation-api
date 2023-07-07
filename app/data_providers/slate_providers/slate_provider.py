from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import uuid5, UUID

from opentelemetry import trace

from app.data_providers.corpus.corpus_fetchable import CorpusFetchable
from app.data_providers.feature_group.corpus_engagement_provider import CorpusEngagementProvider
from app.data_providers.translation import TranslationProvider
from app.graphql.recommendation_reason_type import RecommendationReasonType
from app.models.corpus_item_model import CorpusItemModel
from app.models.corpus_recommendation_model import CorpusRecommendationModel
from app.models.corpus_slate_lineup_model import RecommendationSurfaceId
from app.models.corpus_slate_model import CorpusSlateModel
from app.models.link import LinkModel
from app.models.localemodel import LocaleModel


class SlateProvider(ABC):

    def __init__(
        self,
        corpus_fetchable: CorpusFetchable,
        corpus_engagement_provider: CorpusEngagementProvider,
        recommendation_surface_id: RecommendationSurfaceId,
    ):
        self.corpus_fetchable = corpus_fetchable
        self.corpus_engagement_provider = corpus_engagement_provider
        self.recommendation_surface_id = recommendation_surface_id

    @property
    @abstractmethod
    def candidate_set_id(self) -> str:
        """
        :return: candidate set identifier, which identifies the corpus items that serve as the input for this slate.
                 Feature Group uses a UUID-format, and Curated Corpus API uses a human-readable id (e.g. NEW_TAB_EN_US).
        """
        return NotImplemented

    @property
    def candidate_set_uuid(self) -> UUID:
        """
        Implementing classes with a candidate_set_id that is not a UUID string should override this to return a UUID.
        :return: Returns the candidate_set_id in UUID format.
        """
        return UUID(self.candidate_set_id)

    @property
    def headline(self) -> str:
        """
        :return: Slate headline
        """
        return NotImplemented

    @property
    def subheadline(self) -> Optional[str]:
        """
        :return: (optional) Slate subheadline
        """
        return None

    @property
    def more_link(self) -> Optional[LinkModel]:
        """
        :return: (optional) Slate link to explore more content
        """
        return None

    @property
    def provider_name(self) -> str:
        """
        :return: Name for the slate provider, representing the ranking/filtering algorithms that are applied.
        """
        return self.__class__.__name__

    def __str__(self):
        return self.provider_name

    @property
    def configuration_id(self) -> str:
        """
        :return: UUID slate's configuration id, identifying the context and type of content that this slate provides.
        """
        return str(uuid5(self.candidate_set_uuid, self.provider_name))

    @property
    def recommendation_reason_type(self) -> Optional[RecommendationReasonType]:
        """
        :return: (optional) Reason why recommendations in this slate are recommended.
        """
        return None

    async def get_candidate_corpus_items(self, *args, **kwargs) -> List[CorpusItemModel]:
        """
        :return: The CorpusItems from the candidate set, without any rankers or filters applied.
        """
        return await self.corpus_fetchable.fetch(self.candidate_set_id)

    async def rank_corpus_items(self, items: List[CorpusItemModel], *args, **kwargs) -> List[CorpusItemModel]:
        """
        :param items: Candidate corpus items
        :return: CorpusItems with rankers and filters applied. Unless overridden, input is returned unchanged.
        """
        return items

    async def get_recommendations(self, ranked_items: List[CorpusItemModel], *args, **kwargs) -> List[
        CorpusRecommendationModel]:
        """
        :param ranked_items: The ranked Corpus items to be recommended.
        :return: a CorpusRecommendationModel for each given CorpusItemModel.
        """
        return [CorpusRecommendationModel(corpus_item=item) for item in ranked_items]

    async def get_slate(self, *args, **kwargs) -> CorpusSlateModel:
        """
        :param recommendation_count: The desired number of recommendations. Fewer or more than this may be returned.
        It's good to return ~2x more recommendations to account for any duplicates that are removed at a later stage.
        Fewer may be returned if insufficient content is available.
        :return: A Corpus Slate that can be recommended
        """
        with trace.get_tracer(__name__).start_as_current_span(f'{str(self)}.get_slate'):
            candidate_items = await self.get_candidate_corpus_items(*args, **kwargs)
            ranked_items = await self.rank_corpus_items(candidate_items, *args, **kwargs)
            recommendations = await self.get_recommendations(ranked_items, *args, **kwargs)

            return CorpusSlateModel(
                configuration_id=self.configuration_id,
                headline=self.headline,
                subheadline=self.subheadline,
                more_link=self.more_link,
                recommendations=recommendations,
                recommendation_reason_type=self.recommendation_reason_type,
            )


class HomeSlateProvider(SlateProvider, ABC):
    def __init__(
            self,
            corpus_fetchable: CorpusFetchable,
            corpus_engagement_provider: CorpusEngagementProvider,
            recommendation_surface_id: RecommendationSurfaceId,
            locale: LocaleModel,
            translation_provider: TranslationProvider,
    ):
        super().__init__(corpus_fetchable, corpus_engagement_provider, recommendation_surface_id)

        self.locale = locale
        self.home_translations = translation_provider.get_translations(self.locale, filename='home.json')

    @property
    def headline(self) -> str:
        """
        :return: Slate headline
        """
        return self.home_translations[f'{self.provider_name}.headline']

    @property
    def subheadline(self) -> Optional[str]:
        """
        :return: (optional) Slate subheadline
        """
        return self.home_translations.get(f'{self.provider_name}.subheadline', None)
