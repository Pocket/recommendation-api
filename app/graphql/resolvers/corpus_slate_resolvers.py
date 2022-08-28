from typing import Optional

import aioboto3
from strawberry.types import Info

from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.data_providers.dispatch import SetupMomentDispatch
from app.data_providers.snowplow.config import create_snowplow_tracker, SnowplowConfig
from app.data_providers.snowplow.snowplow_corpus_slate_tracker import SnowplowCorpusSlateTracker
from app.data_providers.topic_provider import TopicProvider
from app.data_providers.user_recommendation_preferences_provider import UserRecommendationPreferencesProvider
from app.graphql.corpus_slate import CorpusSlate
from app.graphql.resolvers.corpus_slate_recommendations_resolver import DEFAULT_RECOMMENDATION_COUNT
from app.graphql.util import get_field_argument, get_user_ids


async def resolve_setup_moment_slate(root, info: Info) -> Optional[CorpusSlate]:
    aioboto3_session = aioboto3.Session()
    corpus_client = CorpusFeatureGroupClient(aioboto3_session=aioboto3_session)
    topic_provider = TopicProvider(aioboto3_session)
    user_recommendation_preferences_provider = UserRecommendationPreferencesProvider(
        aioboto3_session=aioboto3_session,
        topic_provider=topic_provider
    )
    user = get_user_ids(info)

    recommendation_count = int(get_field_argument(
        fields=info.selected_fields,
        field_path=['setupMomentSlate', 'recommendations'],
        argument_name='count',
        default_value=DEFAULT_RECOMMENDATION_COUNT))

    corpus_slate_model = await SetupMomentDispatch(
        corpus_client=corpus_client,
        user_recommendation_preferences_provider=user_recommendation_preferences_provider,
        topic_provider=topic_provider,
    ).get_ranked_corpus_slate(
        user=user,
        recommendation_count=recommendation_count,
    )

    slate_tracker = SnowplowCorpusSlateTracker(tracker=create_snowplow_tracker(), snowplow_config=SnowplowConfig())
    await slate_tracker.track(corpus_slate_model, user=user)

    corpus_slate = CorpusSlate.from_pydantic(corpus_slate_model)
    corpus_slate.recommendations = corpus_slate_model.recommendations

    return corpus_slate
