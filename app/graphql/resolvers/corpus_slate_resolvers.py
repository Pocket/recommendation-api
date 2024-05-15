import logging
from typing import Optional

import strawberry
from strawberry.types import Info
from typing_extensions import Annotated

from app.data_providers.PocketGraphClientSession import PocketGraphClientSession, PocketGraphConfig
from app.data_providers.corpus.corpus_api_client import CorpusApiClient
from app.data_providers.dispatch import NewTabDispatch
from app.data_providers.slate_providers.new_tab_slate_provider import NewTabSlateProvider
from app.data_providers.snowplow.config import create_snowplow_tracker, SnowplowConfig
from app.data_providers.snowplow.snowplow_corpus_recommendations_tracker import SnowplowCorpusRecommendationsTracker
from app.graphql.corpus_slate import CorpusSlate
from app.graphql.util import get_pocket_client
from app.models.localemodel import LocaleModel
from app.singletons import DiContainer


class CorpusApiGraphConfig(PocketGraphConfig):
    # The dev environment does not have corpus items available, so we only connect to the production endpoint.
    ENDPOINT_URL = PocketGraphConfig.PROD_ENDPOINT_URL


async def resolve_new_tab_slate(
        root,
        info: Info,
        locale: Annotated[str, strawberry.argument(
            description="The Firefox build locale, for example 'fr-FR' or 'fr'. This determines which scheduled surface"
                        " will be returned.")],
        region: Annotated[Optional[str], strawberry.argument(
            description="The geographic region, for example 'FR' or 'IT', or null if unavailable. This is currently not"
                        " used, but will be used in the future to decide which scheduled surface to return when we"
                        " serve multiple markets with the same language.")],
        enable_ranking_by_region: Annotated[Optional[bool], strawberry.argument(
            description="Experimental parameter that when enabled, adjusts the ranking of items based on the region."
                        " By default this is off. Firefox Desktop will enable it by setting the pref "
                        " browser.newtabpage.activity-stream.discoverystream.pocket-feed-parameters to \"&enableRankingByRegion=1\""
                        " for the treatment branch of a Nimbus experiment."
        )] = False,
) -> CorpusSlate:
    di = DiContainer.get()
    if enable_ranking_by_region:
        # Log a message to indicate region-specific ranking is enabled.
        # The region-specific ranker will be implemented in MC-1036.
        logging.info(f"Results will soon be ranked for the {region} region")

    async with PocketGraphClientSession(CorpusApiGraphConfig()) as graph_client_session:
        slate_model = await NewTabDispatch(
            new_tab_slate_provider=NewTabSlateProvider(
                corpus_api_client=CorpusApiClient(graph_client_session),
                recommendation_surface_id=NewTabDispatch.get_recommendation_surface_id(locale=locale, region=region),
                corpus_engagement_provider=di.corpus_engagement_provider,
            ),
            snowplow=SnowplowCorpusRecommendationsTracker(
                tracker=create_snowplow_tracker(),
                snowplow_config=SnowplowConfig(),
            ),
        ).get_slate(api_client=get_pocket_client(info), locale=locale)

    slate = CorpusSlate.from_pydantic(slate_model)
    slate.recommendations = slate_model.recommendations
    return slate
