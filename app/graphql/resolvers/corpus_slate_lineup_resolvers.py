import asyncio

from strawberry.types import Info

from app.data_providers.PocketGraphClientSession import PocketGraphClientSession, PocketGraphConfig
from app.data_providers.dispatch import HomeDispatch
from app.data_providers.slate_providers.collection_slate_provider import CollectionSlateProvider
from app.data_providers.slate_providers.for_you_slate_provider import ForYouSlateProvider
from app.data_providers.slate_providers.life_hacks_slate_provider import LifeHacksSlateProvider
from app.data_providers.slate_providers.pocket_hits_slate_provider import PocketHitsSlateProvider
from app.data_providers.slate_providers.recommended_reads_slate_provider import RecommendedReadsSlateProvider
from app.data_providers.slate_providers.topic_slate_provider_factory import TopicSlateProviderFactory
from app.data_providers.snowplow.config import create_snowplow_tracker, SnowplowConfig
from app.data_providers.snowplow.snowplow_corpus_slate_lineup_tracker import SnowplowCorpusSlateLineupTracker
from app.data_providers.unleash_provider import UnleashProvider, UnleashConfig
from app.graphql.corpus_slate_lineup import CorpusSlateLineup
from app.graphql.resolvers.corpus_slate_lineup_slates_resolver import DEFAULT_SLATE_COUNT
from app.graphql.resolvers.corpus_slate_recommendations_resolver import DEFAULT_RECOMMENDATION_COUNT
from app.graphql.util import get_field_argument, get_request_user, get_pocket_client
from app.models.corpus_slate_lineup_model import RecommendationSurfaceId
from app.singletons import DiContainer


async def resolve_home_slate_lineup(root, info: Info) -> CorpusSlateLineup:
    di = DiContainer.get()
    user = get_request_user(info)
    api_client = get_pocket_client(info)

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

    async with PocketGraphClientSession(PocketGraphConfig()) as graph_client_session:
        unleash_provider = UnleashProvider(graph_client_session, unleash_config=UnleashConfig())

        slate_lineup_model = await HomeDispatch(
            corpus_client=di.corpus_client,
            preferences_provider=di.user_recommendation_preferences_provider,
            user_impression_cap_provider=di.user_impression_cap_provider,
            topic_provider=di.topic_provider,
            for_you_slate_provider=ForYouSlateProvider(
                di.corpus_client,
                corpus_engagement_provider=di.corpus_engagement_provider,
                recommendation_surface_id=RecommendationSurfaceId.HOME,
            ),
            recommended_reads_slate_provider=RecommendedReadsSlateProvider(di.corpus_client),
            topic_slate_providers=TopicSlateProviderFactory(di.corpus_client),
            collection_slate_provider=CollectionSlateProvider(di.corpus_client),
            pocket_hits_slate_provider=PocketHitsSlateProvider(di.corpus_client),
            life_hacks_slate_provider=LifeHacksSlateProvider(di.corpus_client),
            unleash_provider=unleash_provider,
        ).get_slate_lineup(
            user=user,
            slate_count=slate_count,
            recommendation_count=recommendation_count,
        )

    slate_lineup_tracker = SnowplowCorpusSlateLineupTracker(
        tracker=create_snowplow_tracker(), snowplow_config=SnowplowConfig())
    asyncio.create_task(
        slate_lineup_tracker.track(corpus_slate_lineup=slate_lineup_model, user=user, api_client=api_client))

    slate_lineup = CorpusSlateLineup.from_pydantic(slate_lineup_model)
    slate_lineup.slates = slate_lineup_model.slates

    return slate_lineup
