from typing import Optional

import strawberry
from strawberry.types import Info
from typing_extensions import Annotated

from app.data_providers.PocketGraphClientSession import PocketGraphClientSession, PocketGraphConfig
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
) -> CorpusSlate:
    di = DiContainer.get()
    locale_model = LocaleModel.from_string(locale, default=LocaleModel.en_US)

    async with PocketGraphClientSession(CorpusApiGraphConfig()) as graph_client_session:
        slate_model = await NewTabDispatch(
            new_tab_slate_provider=NewTabSlateProvider(
                pocket_graph_client_session=graph_client_session,
                corpus_feature_group_client=di.corpus_client,
                recommendation_surface_id=NewTabDispatch.get_recommendation_surface_id(locale=locale_model),
                corpus_engagement_provider=di.corpus_engagement_provider,
                locale=locale_model,
                translation_provider=di.translation_provider,
            ),
            snowplow=SnowplowCorpusRecommendationsTracker(
                tracker=create_snowplow_tracker(),
                snowplow_config=SnowplowConfig(),
            ),
        ).get_slate(api_client=get_pocket_client(info))

    slate = CorpusSlate.from_pydantic(slate_model)
    slate.recommendations = slate_model.recommendations
    return slate
