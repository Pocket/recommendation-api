import asyncio
import functools
import random
import re
from asyncio import gather
from typing import List, Coroutine, Any, Tuple, Optional

from app.config import DEFAULT_TOPICS, GERMAN_HOME_TOPICS
from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.data_providers.slate_providers.cf_slate_provider import HybridCFSlateProvider
from app.recommenders.item2item import Item2ItemRecommender, Item2ItemError, QdrantError, UnsupportedLanguage
from app.data_providers.slate_providers.collection_slate_provider import CollectionSlateProvider
from app.data_providers.slate_providers.for_you_slate_provider import ForYouSlateProvider
from app.data_providers.slate_providers.life_hacks_slate_provider import LifeHacksSlateProvider
from app.data_providers.slate_providers.pocket_hits_slate_provider import PocketHitsSlateProvider
from app.data_providers.slate_providers.recommended_reads_slate_provider import RecommendedReadsSlateProvider
from app.data_providers.slate_providers.topic_slate_provider_factory import TopicSlateProviderFactory
from app.data_providers.snowplow.snowplow_corpus_recommendations_tracker import SnowplowCorpusRecommendationsTracker
from app.data_providers.topic_provider import TopicProvider
from app.data_providers.unleash_provider import UnleashProvider
from app.data_providers.user_impression_cap_provider import UserImpressionCapProvider
from app.data_providers.user_recommendation_preferences_provider import UserRecommendationPreferencesProvider
from app.models.api_client import ApiClient
from app.models.corpus_item_model import CorpusItemModel
from app.models.corpus_recommendation_model import CorpusRecommendationModel
from app.models.corpus_recommendations_send_event import CorpusRecommendationsSendEvent
from app.models.corpus_slate_lineup_model import CorpusSlateLineupModel, RecommendationSurfaceId
from app.models.corpus_slate_model import CorpusSlateModel
from app.models.localemodel import LocaleModel
from app.models.request_user import RequestUser
from app.models.topic import TopicModel
from app.models.unleash_assignment import UnleashAssignmentModel
from app.rankers.algorithms import unique_domains_first
from app.data_providers.slate_providers.new_tab_slate_provider import NewTabSlateProvider


def _empty_on_error(func):
    """ Fallback to empty recommendations if Qdrant error occurred """
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except QdrantError:
            return []
    return wrapper


class Item2ItemDispatch:
    def __init__(self, item_recommender: Item2ItemRecommender):
        self.item_recommender = item_recommender

    async def after_save(self,
                         resolved_id: int,
                         lang: str,
                         count: int) -> List[CorpusRecommendationModel]:
        try:
            recs = await self.item_recommender.related(resolved_id, count, lang)
        except Item2ItemError:
            # do not fallback for "Similar stories" after saving
            recs = []
        return self._to_corpus_items(recs, count)

    @_empty_on_error
    async def after_article(self,
                            resolved_id: int,
                            lang: str,
                            count: int) -> List[CorpusRecommendationModel]:
        try:
            # request more to apply domain diversification
            recs = await self.item_recommender.related(resolved_id, count=20, lang=lang)
        except UnsupportedLanguage:
            # do not fallback for unsupported language
            return []
        except Item2ItemError:
            # fallback to frequently saved for "You Might Also Like"
            recs = await self.item_recommender.frequently_saved_curated(count=100)
            random.shuffle(recs)
        recs = unique_domains_first(recs)
        return self._to_corpus_items(recs, count)

    @_empty_on_error
    async def syndicated(self, resolved_id: int, count: int) -> List[CorpusRecommendationModel]:
        try:
            # request more to apply domain diversification
            recs = await self.item_recommender.syndicated(resolved_id, 20)
        except Item2ItemError:
            # fallback to frequently saved syndicated for syndicated "More Stories from Pocket"
            recs = await self.item_recommender.frequently_saved_syndicated(count=100)
            random.shuffle(recs)
        recs = unique_domains_first(recs)
        return self._to_corpus_items(recs, count)

    @_empty_on_error
    async def by_publisher(self,
                           resolved_id: int,
                           original_id: int,
                           domain: str,
                           count: int) -> List[CorpusRecommendationModel]:
        try:
            recs = await self.item_recommender.by_publisher(resolved_id, domain, original_id, count)
        except Item2ItemError:
            # fallback to random by the same publisher for syndicated right rail
            recs = await self.item_recommender.random_by_publisher(domain, count=100)
            random.shuffle(recs)
        return self._to_corpus_items(recs, count)

    @staticmethod
    def _to_corpus_items(recs, count):
        return [CorpusRecommendationModel(corpus_item=CorpusItemModel(id=r.corpus_item_id, topic=None))
                for r in recs[:count]]


class HomeDispatch:
    AVAILABLE_LOCALES = [
        LocaleModel.en_US,
        LocaleModel.de_DE,
    ]

    def __init__(
            self,
            corpus_client: CorpusFeatureGroupClient,
            preferences_provider: UserRecommendationPreferencesProvider,
            user_impression_cap_provider: UserImpressionCapProvider,
            topic_provider: TopicProvider,
            for_you_slate_provider: ForYouSlateProvider,
            hybrid_cf_slate_provider: HybridCFSlateProvider,
            recommended_reads_slate_provider: RecommendedReadsSlateProvider,
            topic_slate_providers: TopicSlateProviderFactory,
            collection_slate_provider: CollectionSlateProvider,
            pocket_hits_slate_provider: PocketHitsSlateProvider,
            life_hacks_slate_provider: LifeHacksSlateProvider,
            unleash_provider: UnleashProvider,
            snowplow: SnowplowCorpusRecommendationsTracker
    ):
        self.hybrid_cf_slate_provider = hybrid_cf_slate_provider
        self.snowplow = snowplow
        self.topic_provider = topic_provider
        self.corpus_client = corpus_client
        self.preferences_provider = preferences_provider
        self.user_impression_cap_provider = user_impression_cap_provider
        self.for_you_slate_provider = for_you_slate_provider
        self.recommended_reads_slate_provider = recommended_reads_slate_provider
        self.topic_slate_providers = topic_slate_providers
        self.collection_slate_provider = collection_slate_provider
        self.pocket_hits_slate_provider = pocket_hits_slate_provider
        self.life_hacks_slate_provider = life_hacks_slate_provider
        self.unleash_provider = unleash_provider

    async def get_slate_lineup(
            self, user: RequestUser, locale: LocaleModel, recommendation_count: int,
            api_client: ApiClient
    ) -> CorpusSlateLineupModel:
        if locale == LocaleModel.en_US:
            slate_lineup_model, experiment = await self.get_en_us_slate_lineup(
                recommendation_count=recommendation_count, user=user, locale=locale)
        elif locale == LocaleModel.de_DE:
            slate_lineup_model, experiment = await self.get_de_de_slate_lineup(
                recommendation_count=recommendation_count, locale=locale)
        else:
            raise ValueError(f'Invalid locale {locale}')

        asyncio.create_task(
            self.snowplow.track(CorpusRecommendationsSendEvent(
                corpus_slate_lineup=slate_lineup_model,
                recommendation_surface_id=RecommendationSurfaceId.HOME,
                locale=locale.value,
                user=user,
                api_client=api_client,
                experiment=experiment
            )))

        return slate_lineup_model

    async def get_en_us_slate_lineup(
            self, user: RequestUser, recommendation_count: int, locale: LocaleModel
    ) -> Tuple[CorpusSlateLineupModel, Optional[UnleashAssignmentModel]]:

        """
        :param user:
        :param recommendation_count: Maximum number of recommendations to return.
        :param locale:
        :return: Slate lineup for en-US Home:
            1. 'For You' slate if preferred topics are available, or otherwise 'Recommended Reads'
            2. Pocket Hits
            3. Collection slate
            4. 'Life Hacks' slate
            5. Topic slates according to preferred topics if available, otherwise default topics.
        """
        if self.hybrid_cf_slate_provider.can_recommend(user):
            user.user_models.append('hybrid_cf')

        user_impression_capped_list, \
        preferred_topics, \
        assignments = await gather(
            self.user_impression_cap_provider.get(user),
            self._get_preferred_topics(user),
            self.unleash_provider.get_assignments(['temp.web.recommendation-api.home.thompson-sampling-rerun',
                                                   'temp.web.recommendation-api.home.hybrid_cf_test'], user=user))

        thompson_sampling_asn, cf_asn = assignments
        enable_thompson_sampling = \
            thompson_sampling_asn is not None and thompson_sampling_asn.variant == 'treatment'
        enable_hybrid_cf = cf_asn is not None and cf_asn.variant == 'treatment'

        slates = []
        if enable_hybrid_cf and self.hybrid_cf_slate_provider.can_recommend(user):
            slates += [self.hybrid_cf_slate_provider.get_slate(user=user,
                                                               user_impression_capped_list=user_impression_capped_list)]
        else:
            if preferred_topics:
                slates += [self.for_you_slate_provider.get_slate(
                    preferred_topics=preferred_topics,
                    user_impression_capped_list=user_impression_capped_list,
                    enable_thompson_sampling=enable_thompson_sampling,
                )]
            else:
                slates += [self.recommended_reads_slate_provider.get_slate(
                    enable_thompson_sampling=enable_thompson_sampling
                )]

        slates += [
            self.pocket_hits_slate_provider.get_slate(),
            self.collection_slate_provider.get_slate(enable_thompson_sampling=enable_thompson_sampling),
            self.life_hacks_slate_provider.get_slate(),
        ]

        slates += await self._get_topic_slate_promises(preferred_topics=preferred_topics, default=DEFAULT_TOPICS)

        return CorpusSlateLineupModel(
            slates=self._dedupe_and_limit(
                slates=list(await gather(*slates)),
                recommendation_count=recommendation_count,
            ),
            recommendation_surface_id=RecommendationSurfaceId.HOME,
            locale=locale,
            experiment=thompson_sampling_asn,
        ), thompson_sampling_asn

    async def get_de_de_slate_lineup(self, recommendation_count: int, locale: LocaleModel) -> \
            Tuple[CorpusSlateLineupModel, Optional[UnleashAssignmentModel]]:
        """
        :param recommendation_count:
        :param locale:
        :return: the Home slate lineup:
            1. Recommended Reads
            2. Collection slate
            3. Topic slates according to defaults
        """
        slates = [
            self.recommended_reads_slate_provider.get_slate(),
            self.collection_slate_provider.get_slate(),
        ]

        slates += await self._get_topic_slate_promises(preferred_topics=[], default=GERMAN_HOME_TOPICS)

        return CorpusSlateLineupModel(
            slates=self._dedupe_and_limit(
                slates=list(await gather(*slates)),
                recommendation_count=recommendation_count,
            ),
            locale=locale,
        ), None

    @staticmethod
    def _dedupe_and_limit(slates: List[CorpusSlateModel], recommendation_count: int) -> List[CorpusSlateModel]:
        """
        Deduplicate recommendations across slates, and limit the number of recommendations.
        It is assumed each individual slate consists of unique items, and this function doesn't look for items occurring
        multiple times in the same slate.
        :param slates:
        :param recommendation_count: The maximum number of recommendations for each slate.
        :return: Slates with duplicates removed and recommendation_count limit applied.
        """
        seen_corpus_ids = set()

        for slate in slates:
            slate.remove_corpus_items(seen_corpus_ids).limit(recommendation_count)
            # Add all CorpusItem ids from slate to seen_item_ids
            seen_corpus_ids |= set(slate.corpus_item_ids())

        return slates

    async def _get_preferred_topics(self, user: RequestUser) -> List[TopicModel]:
        preferences = await self.preferences_provider.fetch(str(user.user_id))
        if preferences and preferences.preferred_topics:
            return preferences.preferred_topics
        else:
            return []

    async def _get_topic_slate_promises(
            self,
            preferred_topics: List[TopicModel],
            default: List[str],
    ) -> List[Coroutine[Any, Any, CorpusSlateModel]]:
        """
        :param preferred_topics: List topics that the user prefers.
        :param default: List of default topic ids to fall back to, if the user has no preferred topics.
        :return: List of callables/promises that return topic slates when awaited.
        """
        preferred_topic_ids = [t.id for t in preferred_topics]
        topics = await self.topic_provider.get_topics(preferred_topic_ids or default)
        return [self.topic_slate_providers[topic].get_slate() for topic in topics]


class NewTabDispatch:
    def __init__(self, new_tab_slate_provider: NewTabSlateProvider, snowplow: SnowplowCorpusRecommendationsTracker):
        self.new_tab_slate_provider = new_tab_slate_provider
        self.snowplow = snowplow

    async def get_slate(self, api_client: ApiClient, locale: str) -> CorpusSlateModel:
        """
        :return: the New Tab slate
        """
        corpus_slate = await self.new_tab_slate_provider.get_slate()

        asyncio.create_task(
            self.snowplow.track(event=CorpusRecommendationsSendEvent(
                corpus_slate=corpus_slate,
                recommendation_surface_id=self.new_tab_slate_provider.recommendation_surface_id,
                locale=locale,
                api_client=api_client,
            )))

        return corpus_slate

    @staticmethod
    def get_recommendation_surface_id(locale: str, region: Optional[str]) -> RecommendationSurfaceId:
        """
        :param locale: The language variant preferred by the user (e.g. 'en-US', 'en_US', or 'en')
        :param region: Optionally, the geographic region of the user, e.g. 'US'.
        :return: The most appropriate RecommendationSurfaceId for the given locale/region.
                 A value is always returned here. A Firefox pref determines which locales are eligible, so in this
                 function call we can assume that the locale/region has been deemed suitable to receive NewTab recs.
        """

        language = NewTabDispatch._extract_language(locale)
        derived_region = NewTabDispatch._derive_region(region=region, locale=locale)

        if language == 'de':
            return RecommendationSurfaceId.NEW_TAB_DE_DE
        elif language == 'es':
            return RecommendationSurfaceId.NEW_TAB_ES_ES
        elif language == 'fr':
            return RecommendationSurfaceId.NEW_TAB_FR_FR
        elif language == 'it':
            return RecommendationSurfaceId.NEW_TAB_IT_IT
        else:
            # Default to English language for all other values of language (including 'en' or None)
            if derived_region is None or derived_region in ['US', 'CA']:
                return RecommendationSurfaceId.NEW_TAB_EN_US
            elif derived_region in ['GB', 'IE']:
                return RecommendationSurfaceId.NEW_TAB_EN_GB
            else:
                # Default to the International New Tab if no 2-letter region can be derived from locale or region.
                return RecommendationSurfaceId.NEW_TAB_EN_INTL

    @staticmethod
    def _extract_language(locale: str) -> Optional[str]:
        """
        :return: A 2-letter language code from a locale string like 'en-US' or 'en'.
        """
        match = re.search(r'[a-zA-Z]{2}', locale)
        if match:
            return match.group().lower()
        else:
            return None

    @staticmethod
    def _derive_region(locale: str, region: Optional[str] = None) -> Optional[str]:
        """
        Derives the region from the `region` argument if provided, otherwise tries to extract from the locale.

        :param locale: The language-variant preferred by the user (e.g. 'en-US' means English-as-spoken in the US)
        :param region: Optionally, the geographic region of the user, e.g. 'US'.
        :return: A 2-letter region like 'US'.
        """
        if region:
            m1 = re.search(r'[a-zA-Z]{2}', region)
            if m1:
                return m1.group().upper()

        m2 = re.search(r'[_\-]([a-zA-Z]{2})', locale)
        if m2:
            return m2.group(1).upper()
        else:
            return None
