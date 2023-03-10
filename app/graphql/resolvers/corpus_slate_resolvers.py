from typing import Optional

import strawberry
from strawberry.types import Info

from app.data_providers.dispatch import NewTabDispatch
from app.data_providers.slate_providers.recommended_reads_slate_provider import RecommendedReadsSlateProvider
from app.graphql.corpus_slate import CorpusSlate
from app.models.corpus_slate_lineup_model import RecommendationSurfaceId
from app.models.localemodel import LocaleModel
from app.singletons import DiContainer


async def resolve_new_tab_slate(
        root,
        info: Info,
        locale: str = strawberry.argument(
            description="The Firefox build locale, for example 'fr-FR' or 'fr'. This determines which scheduled surface"
                        " will be returned."),
        region: Optional[str] = strawberry.argument(
            description="The geographic region, for example 'FR' or 'IT', or null if unavailable. This is currently not"
                        " used, but will be used in the future to decide which scheduled surface to return when we"
                        " serve multiple markets with the same language."),
) -> CorpusSlate:
    di = DiContainer.get()
    locale_model = LocaleModel.from_string(locale, default=LocaleModel.en_US)

    slate_model = await NewTabDispatch(
        recommended_reads_slate_provider=RecommendedReadsSlateProvider(
            corpus_feature_group_client=di.corpus_client,
            recommendation_surface_id=RecommendationSurfaceId.HOME,
            corpus_engagement_provider=di.corpus_engagement_provider,
            locale=locale_model,
            translation_provider=di.translation_provider,
        )
    ).get_slate()

    return CorpusSlate.from_pydantic(slate_model)
