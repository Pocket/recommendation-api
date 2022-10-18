import logging
import uuid
from asyncio import gather
from datetime import datetime, timezone
from typing import List, Coroutine, Any

from app.data_providers.item2item import Item2ItemRecommender
from app.data_providers.metrics_client import MetricsFetchable
from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.data_providers.slate_providers.collection_slate_provider import CollectionSlateProvider
from app.data_providers.slate_providers.for_you_slate_provider import ForYouSlateProvider
from app.data_providers.slate_providers.recommended_reads_slate_provider import RecommendedReadsSlateProvider
from app.data_providers.slate_providers.topic_slate_provider import TopicSlateProvider
from app.data_providers.slate_providers.topic_slate_provider_factory import TopicSlateProviderFactory
from app.data_providers.topic_provider import TopicProvider
from app.data_providers.user_recommendation_preferences_provider import UserRecommendationPreferencesProvider
from app.data_providers.util import flatten
from app.models.corpus_recommendation_model import CorpusRecommendationModel
from app.models.corpus_slate_lineup_model import CorpusSlateLineupModel, RecommendationSurfaceId
from app.models.corpus_slate_model import CorpusSlateModel
from app.models.topic import TopicModel
from app.models.user_ids import UserIds
from app.rankers.algorithms import rank_by_preferred_topics


class Item2ItemDispatch:

    def __init__(self,
                 metrics_client: MetricsFetchable,
                 item_recommender: Item2ItemRecommender):
        self.metrics_client = metrics_client
        self.item_recommender = item_recommender

    async def syndicated(self, item_id: str, count: int):
        candidates = self.item_recommender.syndicated(item_id, count)
        # ranked = self.metrics_client.rank_items(candidates, rankers=[thompson_sampling_28day])
        # return ranked
        return candidates

    async def by_publisher(self, item_id: str, domain_id: int, count: int):
        candidates = self.item_recommender.by_publisher(item_id, domain_id, count)
        # ranked = self.metrics_client.rank_items(candidates, rankers=[thompson_sampling_28day])
        # return ranked
        return candidates


class SetupMomentDispatch:
    """
    This is a shortcut dispatch helper for launching Setup Moment more quickly. We will want to migrate
    setup moment to RankingDispatch as soon as we want to include rankers or experimentation.
    """

    DISPLAY_NAME = 'Save an article you find interesting'
    SUB_HEADLINE = 'sub headline'
    DEFAULT_TOPICS = [
        '26a3efb4-0f82-415a-9f47-7893df85853f',  # Health & Fitness
        'c6242e35-4ef7-494f-ae9f-51f95b836424',  # Entertainment
        '25c716f1-e1b2-43db-bf52-1a5553d9fb74',  # Technology
        '7dc49254-686d-46e1-aa94-7ac3e7767f66',  # Travel
    ]

    CORPUS_CANDIDATE_SET_IDS = ['57d544d6-0758-4cd1-a7b4-86f454c8eae8']
    CONFIGURATION_ID = str(uuid.uuid5(uuid.UUID(CORPUS_CANDIDATE_SET_IDS[0]), 'SetupMoment'))

    def __init__(
            self,
            corpus_client: CorpusFeatureGroupClient,
            user_recommendation_preferences_provider: UserRecommendationPreferencesProvider,
            topic_provider: TopicProvider,
    ):
        self.topic_provider = topic_provider
        self.corpus_client = corpus_client
        self.user_recommendation_preferences_provider = user_recommendation_preferences_provider

    async def get_ranked_corpus_slate(self, user: UserIds, recommendation_count: int) -> CorpusSlateModel:
        items = await self.corpus_client.get_corpus_items(self.CORPUS_CANDIDATE_SET_IDS)

        user_recommendation_preferences = await self.user_recommendation_preferences_provider.fetch(str(user.user_id))
        if user_recommendation_preferences and user_recommendation_preferences.preferred_topics:
            topics = user_recommendation_preferences.preferred_topics
        else:
            logging.info(f'SetupMoment is unpersonalized for user {user.user_id} because no preferences were found.')
            topics = await self.topic_provider.get_topics(self.DEFAULT_TOPICS)

        items = rank_by_preferred_topics(items, topics, recommendation_count)
        items = items[:recommendation_count]
        recommendations = [CorpusRecommendationModel(id=str(uuid.uuid4()), corpus_item=item) for item in items]

        corpus_slate = CorpusSlateModel(
            id=str(uuid.uuid4()),
            configuration_id=self.CONFIGURATION_ID,
            recommended_at=datetime.now(tz=timezone.utc),
            headline=self.DISPLAY_NAME,
            subheadline=self.SUB_HEADLINE,
            recommendations=recommendations,
        )

        return corpus_slate


class HomeDispatch:

    DEFAULT_TOPICS = [
        '25c716f1-e1b2-43db-bf52-1a5553d9fb74',  # Technology
        'c6242e35-4ef7-494f-ae9f-51f95b836424',  # Entertainment
        '45f8e740-42e0-4f54-8363-21310a084f1f',  # Self-improvement
    ]

    def __init__(
            self,
            corpus_client: CorpusFeatureGroupClient,
            preferences_provider: UserRecommendationPreferencesProvider,
            topic_provider: TopicProvider,
            for_you_slate_provider: ForYouSlateProvider,
            recommended_reads_slate_provider: RecommendedReadsSlateProvider,
            topic_slate_providers: TopicSlateProviderFactory,
            collection_slate_provider: CollectionSlateProvider,
    ):
        self.topic_provider = topic_provider
        self.corpus_client = corpus_client
        self.preferences_provider = preferences_provider
        self.for_you_slate_provider = for_you_slate_provider
        self.recommended_reads_slate_provider = recommended_reads_slate_provider
        self.topic_slate_providers = topic_slate_providers
        self.collection_slate_provider = collection_slate_provider

    async def get_slate_lineup(
            self, user: UserIds, slate_count: int, recommendation_count: int
    ) -> CorpusSlateLineupModel:
        """
        Returns the Home slate lineup:
        1. 'For You' slate if preferred topics are available, otherwise this slate is simply not shown.
        2. Collection slate
        3. Topic slates according to preferred topics if available, otherwise default topics.

        :param user:
        :param slate_count:
        :param recommendation_count:
        :return:
        """
        slates = []

        preferred_topics = await self._get_preferred_topics(user)
        if preferred_topics:
            slates += [self.for_you_slate_provider.get_slate(
                preferred_topics=preferred_topics,
                recommendation_count=recommendation_count
            )]
        else:
            slates += [self.recommended_reads_slate_provider.get_slate()]

        slates += [self.collection_slate_provider.get_slate()]
        slates += await self._get_topic_slate_promises(preferred_topics=preferred_topics)

        return CorpusSlateLineupModel(
            slates=self._dedupe_and_limit(
                slates=list(await gather(*slates)),
                recommendation_count=recommendation_count,
            ),
            recommendation_surface_id=RecommendationSurfaceId.HOME,
        )

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

    async def _get_preferred_topics(self, user: UserIds) -> List[TopicModel]:
        preferences = await self.preferences_provider.fetch(str(user.user_id))
        if preferences and preferences.preferred_topics:
            return preferences.preferred_topics
        else:
            return []

    async def _get_topic_slate_promises(
            self, preferred_topics: List[TopicModel]) -> List[Coroutine[Any, Any, CorpusSlateModel]]:
        preferred_topic_ids = [t.id for t in preferred_topics]
        topics = await self.topic_provider.get_topics(preferred_topic_ids or self.DEFAULT_TOPICS)
        return [self.topic_slate_providers[topic].get_slate() for topic in topics]
