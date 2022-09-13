import random
from asyncio import gather
from datetime import datetime, timezone
import logging
import uuid

from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.data_providers.topic_slate_provider import TopicSlateProvider
from app.data_providers.topic_provider import TopicProvider
from app.data_providers.user_recommendation_preferences_provider import UserRecommendationPreferencesProvider
from app.models.corpus_recommendation_model import CorpusRecommendationModel
from app.models.corpus_slate_lineup_model import CorpusSlateLineupModel
from app.models.corpus_slate_model import CorpusSlateModel
from app.models.user_ids import UserIds
from app.rankers.algorithms import rank_by_preferred_topics


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
            recommended_at=datetime.now(tz=timezone.utc),
            headline=self.DISPLAY_NAME,
            subheadline=self.SUB_HEADLINE,
            recommendations=recommendations,
        )

        return corpus_slate


class HomeDispatch:

    def __init__(
            self,
            corpus_client: CorpusFeatureGroupClient,
            user_recommendation_preferences_provider: UserRecommendationPreferencesProvider,
            topic_provider: TopicProvider,
            topic_slate_provider: TopicSlateProvider,
    ):
        self.topic_provider = topic_provider
        self.corpus_client = corpus_client
        self.user_recommendation_preferences_provider = user_recommendation_preferences_provider
        self.topic_slate_provider = topic_slate_provider

        self.setup_moment_dispatch = self._create_setup_moment_dispatch()

    async def get_slate_lineup(
            self, user: UserIds, slate_count: int, recommendation_count: int
    ) -> CorpusSlateLineupModel:
        setup_moment_slate_coroutine = self.setup_moment_dispatch.get_ranked_corpus_slate(
            user=user,
            recommendation_count=recommendation_count,
        )

        topics = await self.topic_provider.get_all()
        remaining_slate_count = slate_count - 1  # first slate is setup moment
        if len(topics) > remaining_slate_count:
            topics = random.sample(topics, k=remaining_slate_count)

        topic_slates_coroutine = self.topic_slate_provider.get_slates(topics, recommendation_count=recommendation_count)

        setup_moment_slate, topic_slates = await gather(setup_moment_slate_coroutine, topic_slates_coroutine)
        slates = [setup_moment_slate] + topic_slates

        corpus_slate_lineup = CorpusSlateLineupModel(
            id=str(uuid.uuid4()),
            slates=slates,
            recommended_at = datetime.now(tz=timezone.utc),
        )

        return corpus_slate_lineup

    def _create_setup_moment_dispatch(self) -> SetupMomentDispatch:
        return SetupMomentDispatch(
            corpus_client=self.corpus_client,
            user_recommendation_preferences_provider=self.user_recommendation_preferences_provider,
            topic_provider=self.topic_provider,
        )
