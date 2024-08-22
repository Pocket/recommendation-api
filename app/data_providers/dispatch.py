import asyncio
import functools
import random
import re
from asyncio import gather
from typing import List, Coroutine, Any, Tuple, Optional
from datetime import datetime

from app.config import DEFAULT_TOPICS, GERMAN_HOME_TOPICS, FR_FR_HOME_TOPICS, EN_GB_HOME_TOPICS, IT_IT_HOME_TOPICS, ES_ES_HOME_TOPICS, \
    POCKET_HOME_NO_SYNDICATION_FEATURE_FLAG
from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.data_providers.slate_providers.pockety_worthy_provider import PocketWorthyProvider
from app.data_providers.slate_providers.pride_slate_provider import PrideSlateProvider
from app.data_providers.user_recommendation_preferences_provider import UserRecommendationPreferencesProvider
from app.data_providers.util import integer_hash
from app.graphql.util import get_pocket_client
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
        LocaleModel.en_GB,
        LocaleModel.it_IT,
        LocaleModel.fr_FR,
        LocaleModel.es_ES
    ]

    def __init__(
            self,
            corpus_client: CorpusFeatureGroupClient,
            preferences_provider: UserRecommendationPreferencesProvider,
            user_impression_cap_provider: UserImpressionCapProvider,
            topic_provider: TopicProvider,
            for_you_slate_provider: ForYouSlateProvider,
            recommended_reads_slate_provider: RecommendedReadsSlateProvider,
            topic_slate_providers: TopicSlateProviderFactory,
            collection_slate_provider: CollectionSlateProvider,
            pocket_hits_slate_provider: PocketHitsSlateProvider,
            life_hacks_slate_provider: LifeHacksSlateProvider,
            unleash_provider: UnleashProvider,
            snowplow: SnowplowCorpusRecommendationsTracker,
            pocket_worthy_provider: PocketWorthyProvider,
            pride_provider: PrideSlateProvider,
    ):
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
        self.pocket_worthy_provider = pocket_worthy_provider
        self.pride_provider = pride_provider

    async def get_slate_lineup(
            self, user: RequestUser, locale: LocaleModel, recommendation_count: int,
            api_client: ApiClient
    ) -> CorpusSlateLineupModel:
        if locale == LocaleModel.en_US:
            slate_lineup_model, experiment = await self.get_en_us_slate_lineup(
                recommendation_count=recommendation_count, user=user)
        elif locale == LocaleModel.de_DE:
            slate_lineup_model, experiment = await self.get_de_de_slate_lineup(
                recommendation_count=recommendation_count, user=user)
        elif locale == LocaleModel.en_GB:
            slate_lineup_model, experiment = await self.get_en_gb_slate_lineup(
                recommendation_count=recommendation_count, user=user)
        elif locale == LocaleModel.fr_FR:
            slate_lineup_model, experiment = await self.get_fr_fr_slate_lineup(
                recommendation_count=recommendation_count, user=user)
        elif locale == LocaleModel.it_IT:
            slate_lineup_model, experiment = await self.get_it_it_slate_lineup(
                recommendation_count=recommendation_count, user=user)
        elif locale == LocaleModel.es_ES:
            slate_lineup_model, experiment = await self.get_es_es_slate_lineup(
                recommendation_count=recommendation_count, user=user)
        else:
            # Default to en-US
            slate_lineup_model, experiment = await self.get_en_us_slate_lineup(
                recommendation_count=recommendation_count, user=user)

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
            self, user: RequestUser, recommendation_count: int) -> Tuple[CorpusSlateLineupModel, Optional[UnleashAssignmentModel]]:
        """
        :param user:
        :param recommendation_count: Maximum number of recommendations to return.
        :param locale:
        :return: Slate lineup for en-US Home:
            1. Syndicated - Pocket Worthy
            2. Collections
            2. Pocket Hits
            3. 'For You' slate if preferred topics are available, or otherwise 'Recommended Reads'
            4. 'Life Hacks' slate
        """
        user_impression_capped_list, \
            preferred_topics, \
            no_syndication_assignment = await gather(
            self.user_impression_cap_provider.get(user),
            self._get_preferred_topics(user),
            self.unleash_provider.get_assignment(POCKET_HOME_NO_SYNDICATION_FEATURE_FLAG, user=user),
        )

        seed_id = self.get_seed_id(user=user)
        slates = [
            self.pocket_worthy_provider.get_slate(enable_thompson_sampling_with_seed=seed_id,
                                                  user_impression_capped_list=user_impression_capped_list),
            self.collection_slate_provider.get_slate(enable_thompson_sampling_with_seed=seed_id,
                                                     user_impression_capped_list=user_impression_capped_list),
            self.pocket_hits_slate_provider.get_slate(),
            self.get_for_you_or_recommended_reads(preferred_topics=preferred_topics,
                                                  user_impression_capped_list=user_impression_capped_list,
                                                  seed_id=seed_id
                                                  ),
            self.life_hacks_slate_provider.get_slate(enable_thompson_sampling_with_seed=seed_id,
                                                     user_impression_capped_list=user_impression_capped_list),
        ]
        if no_syndication_assignment is not None and no_syndication_assignment.variant == 'treatment' is True:
            del slates[0]

        return CorpusSlateLineupModel(
            slates=self._dedupe_and_limit(
                slates=list(await gather(*slates)),
                recommendation_count=recommendation_count,
            ),
        ), no_syndication_assignment

    async def get_for_you_or_recommended_reads(self, preferred_topics: List[TopicModel],
                                               user_impression_capped_list: List[CorpusItemModel],
                                               seed_id: int) -> CorpusSlateModel:
        """
        :param preferred_topics:
        :param user_impression_capped_list:

        Gets a personalized slate of articles or a default one if no preferred topics are available.
        """
        if preferred_topics:
            return await self.for_you_slate_provider.get_slate(
                preferred_topics=preferred_topics,
                user_impression_capped_list=user_impression_capped_list,
                enable_thompson_sampling_with_seed=seed_id
            )
        else:
            return await self.recommended_reads_slate_provider.get_slate(enable_thompson_sampling_with_seed=seed_id, user_impression_capped_list=user_impression_capped_list)

    async def get_de_de_slate_lineup(self, user: RequestUser, recommendation_count: int) -> \
            Tuple[CorpusSlateLineupModel, Optional[UnleashAssignmentModel]]:
        """
        :param recommendation_count:
        :param locale:
        :return: the Home slate lineup:
                1. Collection slate
                2. Recommended Reads
                3. Topic slates according to defaults
        """

        user_impression_capped_list = await self.user_impression_cap_provider.get(user)

        seed_id = self.get_seed_id(user=user)
        slates = [
            self.collection_slate_provider.get_slate(enable_thompson_sampling_with_seed=seed_id,
                                                     user_impression_capped_list=user_impression_capped_list),
            self.recommended_reads_slate_provider.get_slate(enable_thompson_sampling_with_seed=seed_id,
                                                            user_impression_capped_list=user_impression_capped_list),
        ]
        slates += await self._get_topic_slate_promises(preferred_topics=[], default=GERMAN_HOME_TOPICS)

        return CorpusSlateLineupModel(
            slates=self._dedupe_and_limit(
                slates=list(await gather(*slates)),
                recommendation_count=recommendation_count,
            ),
        ), None

    async def get_en_gb_slate_lineup(self, user: RequestUser, recommendation_count: int) -> \
            Tuple[CorpusSlateLineupModel, Optional[UnleashAssignmentModel]]:
        """
        :param recommendation_count:
        :param locale:
        :return: the Home slate lineup:
                1. Recommended Reads
                2. Life Hacks
                3. Topic slates according to defaults
        """

        user_impression_capped_list = await self.user_impression_cap_provider.get(user)

        seed_id = self.get_seed_id(user=user)
        slates = [
            self.recommended_reads_slate_provider.get_slate(enable_thompson_sampling_with_seed=seed_id,
                                                            user_impression_capped_list=user_impression_capped_list),
            self.life_hacks_slate_provider.get_slate(enable_thompson_sampling_with_seed=seed_id,
                                                     user_impression_capped_list=user_impression_capped_list),
        ]
        slates += await self._get_topic_slate_promises(preferred_topics=[], default=EN_GB_HOME_TOPICS)

        return CorpusSlateLineupModel(
            slates=self._dedupe_and_limit(
                slates=list(await gather(*slates)),
                recommendation_count=recommendation_count,
            ),
        ), None

    async def get_fr_fr_slate_lineup(self, user: RequestUser, recommendation_count: int) -> \
            Tuple[CorpusSlateLineupModel, Optional[UnleashAssignmentModel]]:
        """
        :param recommendation_count:
        :param locale:
        :return: the Home slate lineup:
                1. Recommended Reads
                2. Life Hacks
                3. Topic slates according to defaults
        """

        user_impression_capped_list = await self.user_impression_cap_provider.get(user)

        seed_id = self.get_seed_id(user=user)
        slates = [
            self.recommended_reads_slate_provider.get_slate(enable_thompson_sampling_with_seed=seed_id,
                                                            user_impression_capped_list=user_impression_capped_list),
            self.life_hacks_slate_provider.get_slate(enable_thompson_sampling_with_seed=seed_id,
                                                     user_impression_capped_list=user_impression_capped_list),
        ]
        slates += await self._get_topic_slate_promises(preferred_topics=[], default=FR_FR_HOME_TOPICS)

        return CorpusSlateLineupModel(
            slates=self._dedupe_and_limit(
                slates=list(await gather(*slates)),
                recommendation_count=recommendation_count,
            ),
        ), None

    async def get_it_it_slate_lineup(self, user: RequestUser, recommendation_count: int) -> \
            Tuple[CorpusSlateLineupModel, Optional[UnleashAssignmentModel]]:
        """
        :param recommendation_count:
        :param locale:
        :return: the Home slate lineup:
                1. Recommended Reads
                2. Life Hacks
                3. Topic slates according to defaults
        """

        user_impression_capped_list = await self.user_impression_cap_provider.get(user)

        seed_id = self.get_seed_id(user=user)
        slates = [
            self.recommended_reads_slate_provider.get_slate(enable_thompson_sampling_with_seed=seed_id,
                                                            user_impression_capped_list=user_impression_capped_list),
            self.life_hacks_slate_provider.get_slate(enable_thompson_sampling_with_seed=seed_id,
                                                     user_impression_capped_list=user_impression_capped_list),
        ]
        slates += await self._get_topic_slate_promises(preferred_topics=[], default=IT_IT_HOME_TOPICS)

        return CorpusSlateLineupModel(
            slates=self._dedupe_and_limit(
                slates=list(await gather(*slates)),
                recommendation_count=recommendation_count,
            ),
        ), None

    async def get_es_es_slate_lineup(self, user: RequestUser, recommendation_count: int) -> \
            Tuple[CorpusSlateLineupModel, Optional[UnleashAssignmentModel]]:
        """
        :param recommendation_count:
        :param locale:
        :return: the Home slate lineup:
                1. Recommended Reads
                2. Life Hacks
                3. Topic slates according to defaults
        """

        user_impression_capped_list = await self.user_impression_cap_provider.get(user)

        seed_id = self.get_seed_id(user=user)
        slates = [
            self.recommended_reads_slate_provider.get_slate(enable_thompson_sampling_with_seed=seed_id,
                                                            user_impression_capped_list=user_impression_capped_list),
            self.life_hacks_slate_provider.get_slate(enable_thompson_sampling_with_seed=seed_id,
                                                     user_impression_capped_list=user_impression_capped_list),
        ]
        slates += await self._get_topic_slate_promises(preferred_topics=[], default=ES_ES_HOME_TOPICS)

        return CorpusSlateLineupModel(
            slates=self._dedupe_and_limit(
                slates=list(await gather(*slates)),
                recommendation_count=recommendation_count,
            ),
        ), None

    def get_seed_id(self, user: RequestUser) -> Optional[int]:
        # Create a deterministic seed for thompson sampling if we can
        current_date = datetime.now().strftime("%Y-%m-%d")
        seed_id = None
        if user is not None and user.hashed_user_id is not None:
            seed_id = integer_hash(f"{user.hashed_user_id}{current_date}", 0, 2 ** 32)
        elif user is not None and user.hashed_guid is not None:
            seed_id = integer_hash(f"{user.hashed_guid}{current_date}", 0, 2 ** 32)
        return seed_id

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
        if user is None or user.hashed_user_id is None:
            return []
        preferences = await self.preferences_provider.fetch(str(user.hashed_user_id))
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

    async def get_slate(
            self,
            api_client: ApiClient,
            locale: str,
            region: Optional[str],
            enable_ranking_by_region: Optional[bool] = False
    ) -> CorpusSlateModel:
        """
        :return: the New Tab slate
        """
        corpus_slate = await self.new_tab_slate_provider.get_slate(region=region, enable_ranking_by_region=enable_ranking_by_region)

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
        Locale/region mapping is documented here:
        https://docs.google.com/document/d/1omclr-eETJ7zAWTMI7mvvsc3_-ns2Iiho4jPEfrmZfo/edit
        :param locale: The language variant preferred by the user (e.g. 'en-US', or 'en')
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
            elif derived_region in ['IN']:
                return RecommendationSurfaceId.NEW_TAB_EN_INTL
            else:
                # Default to the en-US New Tab if no 2-letter region can be derived from locale or region.
                return RecommendationSurfaceId.NEW_TAB_EN_US

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
