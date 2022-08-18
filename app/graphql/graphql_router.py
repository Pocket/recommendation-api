import graphql
from graphene import ObjectType, String, Field, List, Int
from graphene_federation import build_schema
import aioboto3

from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.data_providers.corpus.curated_corpus_api_client import CuratedCorpusAPIClient
from app.data_providers.metrics_client import MetricsClient
from app.data_providers.slate_provider import SlateProvider
from app.data_providers.snowplow.config import SnowplowConfig, create_snowplow_tracker
from app.data_providers.snowplow.snowplow_corpus_slate_tracker import SnowplowCorpusSlateTracker
from app.data_providers.topic_provider import TopicProvider
from app.data_providers.user_recommendation_preferences_provider import UserRecommendationPreferencesProvider
from app.graphql.corpus_slate_lineup import CorpusSlateLineup
from app.graphql.ranked_corpus_slate import RankedCorpusSlate
from app.graphql.update_user_recommendation_preferences_mutation import UpdateUserRecommendationPreferences
from app.graphql.util import get_field_argument
from app.models.corpus_slate_lineup_model import CorpusSlateLineupModel
from app.models.metrics.firefox_new_tab_metrics_factory import FirefoxNewTabMetricsFactory
from app.models.ranked_corpus_slate_instance import RankedCorpusSlateInstance
from app.models.corpus_slate_model import CorpusSlateModel
from app.data_providers.dispatch import RankingDispatch, SetupMomentDispatch, HomeDispatch
from app.graphql.corpus_slate import CorpusSlate
from app.models.topic import TopicModel
from app.models.slate import SlateModel
from app.models.slate_lineup import SlateLineupModel
from app.graphql.topic import Topic
from app.graphql.slate import Slate
from app.graphql.slate_lineup import SlateLineup
from app.graphql.user import User


class Query(ObjectType):
    list_topics = List(Topic)

    get_slate = Field(Slate, slate_id=String(required=True, description="Slate id to get a specific slate"),
                      recommendation_count=Int(default_value=10,
                                               description="Number of recommendations to return, defaults to 10"))

    setup_moment_slate = Field(
        CorpusSlate,
    )

    home_slate_lineup = Field(
        CorpusSlateLineup,
    )

    recommendation_preference_topics = Field(
        List(Topic),
    )

    get_ranked_corpus_slate = Field(RankedCorpusSlate, slate_id=String(required=True, description="A ranked list of recommendation items"))

    list_slates = Field(List(Slate), recommendation_count=Int(default_value=0,
                                                              description="Number of recommendations to return, defaults to 0"))
    get_slate_lineup = Field(SlateLineup, slate_lineup_id=String(required=True,
                                                                 description="SlateLineup id to get a specific slate lineup"),
                             slate_count=Int(default_value=8, description="Number of slates to return, defaults to 8"),
                             recommendation_count=Int(default_value=10,
                                                      description="Maximum number of recommendations to return, defaults to 10"))

    async def resolve_list_topics(self, info) -> [TopicModel]:
        return await TopicProvider(aioboto3_session=aioboto3.Session()).get_all()

    async def resolve_get_slate(self, info, slate_id: str, recommendation_count: int = None) -> SlateModel:
        return await SlateModel.get_slate(slate_id=slate_id, user_id=info.context.get('user_id'),
                                          recommendation_count=recommendation_count)

    async def resolve_get_ranked_corpus_slate(self, info, slate_id: str) -> RankedCorpusSlateInstance:
        return await RankingDispatch(
            corpus_client=CuratedCorpusAPIClient(),
            slate_provider=SlateProvider(),
            metrics_client=MetricsClient(
                firefox_newtab_metrics_factory=FirefoxNewTabMetricsFactory()
            )
        ).get_ranked_corpus_slate(slate_id=slate_id)

    async def resolve_list_slates(self, info, recommendation_count: int) -> [SlateModel]:
        return await SlateModel.get_all(user_id=info.context.get('user_id'), recommendation_count=recommendation_count)

    async def resolve_get_slate_lineup(self, info, slate_lineup_id: str, recommendation_count: int = 10,
                                       slate_count: int = 8) -> SlateLineupModel:
        return await SlateLineupModel.get_slate_lineup_with_fallback(slate_lineup_id=slate_lineup_id,
                                                                     user_id=info.context.get('user_id'),
                                                                     recommendation_count=recommendation_count,
                                                                     slate_count=slate_count)

    async def resolve_setup_moment_slate(self, info: graphql.ResolveInfo, **kwargs) -> CorpusSlateModel:
        user = info.context['user']
        aioboto3_session = aioboto3.Session()
        corpus_client = CorpusFeatureGroupClient(aioboto3_session=aioboto3_session)
        topic_provider = TopicProvider(aioboto3_session)
        user_recommendation_preferences_provider = UserRecommendationPreferencesProvider(
            aioboto3_session=aioboto3_session,
            topic_provider=topic_provider
        )
        slate_tracker = SnowplowCorpusSlateTracker(tracker=create_snowplow_tracker(), snowplow_config=SnowplowConfig())

        recommendation_count = int(get_field_argument(
            info.field_asts, ['setupMomentSlate', 'recommendations'], 'count', default_value=CorpusSlate.DEFAULT_COUNT))

        corpus_slate = await SetupMomentDispatch(
            corpus_client=corpus_client,
            user_recommendation_preferences_provider=user_recommendation_preferences_provider,
            topic_provider=topic_provider,
        ).get_ranked_corpus_slate(
            user=user,
            recommendation_count=recommendation_count,
        )

        await slate_tracker.track(corpus_slate, user=user)
        return corpus_slate

    async def resolve_home_slate_lineup(self, info: graphql.ResolveInfo, **kwargs) -> CorpusSlateLineupModel:
        aioboto3_session = aioboto3.Session()
        corpus_client = CorpusFeatureGroupClient(aioboto3_session=aioboto3_session)
        topic_provider = TopicProvider(aioboto3_session)
        user_recommendation_preferences_provider = UserRecommendationPreferencesProvider(
            aioboto3_session=aioboto3_session,
            topic_provider=topic_provider
        )
        slate_tracker = SnowplowCorpusSlateTracker(tracker=create_snowplow_tracker(), snowplow_config=SnowplowConfig())

        slate_count = int(get_field_argument(
            info.field_asts, ['homeSlateLineup', 'slates'], 'count', default_value=CorpusSlateLineup.DEFAULT_COUNT))

        recommendation_count = int(get_field_argument(
            info.field_asts, ['homeSlateLineup', 'slates', 'recommendations'], 'count', default_value=CorpusSlate.DEFAULT_COUNT))

        return await HomeDispatch(
            corpus_client=corpus_client,
            user_recommendation_preferences_provider=user_recommendation_preferences_provider,
            slate_tracker=slate_tracker,
            topic_provider=topic_provider,
        ).get_slate_lineup(
            user=info.context['user'],
            slate_count=slate_count,
            recommendation_count=recommendation_count,
        )

    async def resolve_recommendation_preference_topics(self, info) -> [Topic]:
        topics = await TopicProvider(aioboto3_session=aioboto3.Session()).get_all()
        exclude_topic_names = ['Gaming', 'Sports', 'Education', 'Coronavirus']
        return [t for t in topics if t.name not in exclude_topic_names]


class Mutation(ObjectType):
    update_user_recommendation_preferences = UpdateUserRecommendationPreferences.Field()


# Any type with a __resolve_reference should be added to this list.
types = [
    User,
]


##
# Graphene requires that you define your schema programmatically.
# Looks like Graphene 3 will support loading from a .graphql file.
# For now this file should stay in sync with *.graphql
##
schema = build_schema(query=Query, mutation=Mutation, types=types)

