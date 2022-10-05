from typing import Optional

import aioboto3
from strawberry.types import Info

from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.data_providers.dispatch import HomeDispatch
from app.data_providers.slate_providers.collection_slate_provider import CollectionSlateProvider
from app.data_providers.slate_providers.for_you_slate_provider import ForYouSlateProvider
from app.data_providers.slate_providers.recommended_reads_slate_provider import RecommendedReadsSlateProvider
from app.data_providers.topic_provider import TopicProvider
from app.data_providers.slate_providers.topic_slate_provider import TopicSlateProvider
from app.data_providers.user_recommendation_preferences_provider import UserRecommendationPreferencesProvider
from app.graphql.corpus_slate import CorpusSlate
from app.graphql.corpus_slate_lineup import CorpusSlateLineup
from app.graphql.resolvers.corpus_slate_lineup_slates_resolver import DEFAULT_SLATE_COUNT
from app.graphql.resolvers.corpus_slate_recommendations_resolver import DEFAULT_RECOMMENDATION_COUNT
from app.graphql.util import get_field_argument, get_user_ids


async def resolve_home_slate_lineup(root, info: Info) -> CorpusSlateLineup:
    aioboto3_session = aioboto3.Session()
    corpus_client = CorpusFeatureGroupClient(aioboto3_session=aioboto3_session)
    user = get_user_ids(info)
    topic_provider = TopicProvider(aioboto3_session)
    user_recommendation_preferences_provider = UserRecommendationPreferencesProvider(
        aioboto3_session=aioboto3_session,
        topic_provider=topic_provider
    )

    slate_count = int(get_field_argument(
        fields=info.selected_fields,
        field_path=['homeSlateLineup', 'slates'],
        argument_name='count',
        default_value=DEFAULT_SLATE_COUNT))

    recommendation_count = int(get_field_argument(
        fields=info.selected_fields,
        field_path=['homeSlateLineup', 'slates', 'recommendations'],
        argument_name='count',
        default_value=DEFAULT_RECOMMENDATION_COUNT))

    slate_lineup_model = await HomeDispatch(
        corpus_client=corpus_client,
        preferences_provider=user_recommendation_preferences_provider,
        topic_provider=topic_provider,
        for_you_slate_provider=ForYouSlateProvider(corpus_client),
        recommended_reads_slate_provider=RecommendedReadsSlateProvider(corpus_client),
        topic_slate_provider=TopicSlateProvider(corpus_client),
        collection_slate_provider=CollectionSlateProvider(corpus_client),
    ).get_slate_lineup(
        user=user,
        slate_count=slate_count,
        recommendation_count=recommendation_count,
    )

    slate_lineup = CorpusSlateLineup.from_pydantic(slate_lineup_model)
    slate_lineup.slates = slate_lineup_model.slates
    return slate_lineup
