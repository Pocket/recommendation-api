from typing import Optional

import strawberry
from strawberry.types import Info
from typing_extensions import Annotated

from app.data_providers.dispatch import NewTabDispatch
from app.data_providers.slate_providers.new_tab_slate_provider import NewTabSlateProvider
from app.graphql.corpus_slate import CorpusSlate
from app.models.corpus_slate_lineup_model import RecommendationSurfaceId
from app.models.localemodel import LocaleModel
from app.singletons import DiContainer


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

    slate_model = await NewTabDispatch(
        new_tab_slate_provider=NewTabSlateProvider(
            corpus_feature_group_client=di.corpus_client,
            recommendation_surface_id=NewTabDispatch.get_recommendation_surface_id(locale=locale_model),
            corpus_engagement_provider=di.corpus_engagement_provider,
            locale=locale_model,
            translation_provider=di.translation_provider,
        )
    ).get_slate()

    slate = CorpusSlate.from_pydantic(slate_model)
    slate.recommendations = slate_model.recommendations
    return slate
