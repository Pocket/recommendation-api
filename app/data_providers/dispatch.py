import logging
import uuid

from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.data_providers.corpus.corpus_fetchable import CorpusFetchable
from app.data_providers.snowplow.snowplow_corpus_slate_tracker import SnowplowCorpusSlateTracker
from app.data_providers.metrics_client import MetricsFetchable
from app.data_providers.slate_provider import SlateProvider, SlateProvidable
from app.data_providers.topic_provider import TopicProvider
from app.data_providers.user_recommendation_preferences_provider import UserRecommendationPreferencesProvider
from app.models.corpus_recommendation_model import CorpusRecommendationModel
from app.models.corpus_slate_model import CorpusSlateModel
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
            slate_tracker: SnowplowCorpusSlateTracker,
            topic_provider: TopicProvider,
    ):
        self.topic_provider = topic_provider
        self.corpus_client = corpus_client
        self.user_recommendation_preferences_provider = user_recommendation_preferences_provider
        self.slate_tracker = slate_tracker

    async def get_ranked_corpus_slate(self, user_id: str, recommendation_count: int) -> CorpusSlateModel:
        items = await self.corpus_client.get_corpus_items(self.CORPUS_CANDIDATE_SET_IDS)

        user_recommendation_preferences = await self.user_recommendation_preferences_provider.fetch(user_id)
        if user_recommendation_preferences and user_recommendation_preferences.preferred_topics:
            topics = user_recommendation_preferences.preferred_topics
        else:
            logging.info(f'SetupMoment is unpersonalized for user {user_id} because no preferences were found.')
            topics = await self.topic_provider.get_topics(self.DEFAULT_TOPICS)

        items = rank_by_preferred_topics(items, topics, recommendation_count)
        items = items[:recommendation_count]
        recommendations = [CorpusRecommendationModel(id=str(uuid.uuid4()), corpus_item=item) for item in items]

        corpus_slate = CorpusSlateModel(
            id=str(uuid.uuid4()),
            headline=self.DISPLAY_NAME,
            subheadline=self.SUB_HEADLINE,
            recommendations=recommendations,
        )

        await self.slate_tracker.track(corpus_slate, user_id=user_id)

        return corpus_slate


class RankingDispatch:
    """
    This class is responsible for accepting:

     a dependency to get items to rank (api_client),
     a strategy for ranking them (slate_provider),
     and the data to execute ranking (metrics_client),

     and then using those three things to shape the list of items to the order and size we serve to a client.

     If there are NO rankers, it sends the original list of items, with no reshaping, to the client.
    """
    def __init__(
            self,
            corpus_client: CorpusFetchable,
            slate_provider: SlateProvider,
            metrics_client: MetricsFetchable
    ):
        self.corpus_client = corpus_client
        self.slate_provider = slate_provider
        self.metrics_client = metrics_client

    async def get_ranked_corpus_slate(self, slate_id) -> CorpusSlateModel:
        """
        From a slate identifier find the appropriate experiment. Then fetch the candidate set and sort the corpus items.
        :param slate_id: defined in `slate_configs.json`
        :return: CorpusSlateModel
        """
        corpus_slate_schema = self.slate_provider.get_slate(slate_id)
        experiment = self.slate_provider.get_random_experiment(slate_id)

        # Fetch Corporeal Candidates
        items = await self.corpus_client.get_corpus_items(experiment.corpus_ids())
        items = await self.metrics_client.rank_items(items, experiment.rankers)

        recommendations = [CorpusRecommendationModel(id=uuid.uuid4().hex, corpus_item=item) for item in items]

        return CorpusSlateModel(
            id=slate_id,
            headline=corpus_slate_schema.displayName,
            subheadline=corpus_slate_schema.description,
            recommendations=recommendations,
        )
