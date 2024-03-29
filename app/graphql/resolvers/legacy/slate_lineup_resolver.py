import logging
from typing import Optional

from strawberry import argument
from strawberry.types import Info
from typing_extensions import Annotated

from app.graphql.slate_lineup import SlateLineup
from app.models.slate_lineup import SlateLineupModel


async def resolve_get_slate_lineup(
        root,
        info: Info,
        slate_lineup_id: Annotated[str, argument(description='The SlateLineup.id of the SlateLineup to return')],
        slate_count: Annotated[Optional[int], argument(
            description='Maximum number of slates to return in SlateLineup.slates, defaults to 8')] = 8,
        recommendation_count: Annotated[Optional[int], argument(
            description='Maximum number of recommendations to return in Slate.recommendations, defaults to 10')] = 10,
) -> Optional[SlateLineup]:
    logging.info(f'resolving getSlateLineup with slate_lineup_id={slate_lineup_id}, slate_count={slate_count}), '
                 f'recommendation_count={recommendation_count}')

    slate_lineup_model = await SlateLineupModel.get_slate_lineup(
        slate_lineup_id=slate_lineup_id,
        user_id=info.context.get('request').headers.get('userId'),
        recommendation_count=recommendation_count,
        slate_count=slate_count)

    return SlateLineup.from_pydantic(slate_lineup_model)
