import aioboto3
from strawberry.types import Info

from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.data_providers.dispatch import SetupMomentDispatch
from app.data_providers.snowplow.config import create_snowplow_tracker, SnowplowConfig
from app.data_providers.snowplow.snowplow_corpus_slate_tracker import SnowplowCorpusSlateTracker
from app.data_providers.topic_provider import TopicProvider
from app.data_providers.user_recommendation_preferences_provider import UserRecommendationPreferencesProvider
from app.graphql.corpus_slate import CorpusSlate
from app.graphql.corpus_slate_lineup import CorpusSlateLineup
from app.graphql.resolvers.corpus_slate_recommendations_resolver import DEFAULT_RECOMMENDATION_COUNT
from app.graphql.util import get_field_argument, get_user_ids


async def resolve_home_slate_lineup(root, info: Info) -> CorpusSlateLineup:
    aioboto3_session = aioboto3.Session()
    corpus_client = CorpusFeatureGroupClient(aioboto3_session=aioboto3_session)
    topic_provider = TopicProvider(aioboto3_session)
    user_recommendation_preferences_provider = UserRecommendationPreferencesProvider(
        aioboto3_session=aioboto3_session,
        topic_provider=topic_provider
    )

    slate_count = int(get_field_argument(
        info.field_asts, ['homeSlateLineup', 'slates'], 'count', default_value=CorpusSlateLineup.DEFAULT_COUNT))

    recommendation_count = int(get_field_argument(
        info.field_asts, ['homeSlateLineup', 'slates', 'recommendations'], 'count',
        default_value=CorpusSlate.DEFAULT_COUNT))

    return await HomeDispatch(
        corpus_client=corpus_client,
        user_recommendation_preferences_provider=user_recommendation_preferences_provider,
        topic_provider=topic_provider,
        topic_slate_provider=TopicSlateProvider(corpus_client)
    ).get_slate_lineup(
        user=info.context['user'],
        slate_count=slate_count,
        recommendation_count=recommendation_count,
    )
