from typing import Optional

from typing_extensions import Annotated

import strawberry
from strawberry.types import Info

from app.graphql.slate import Slate
from app.models.slate import SlateModel


async def resolve_get_slate(
        root,
        info: Info,
        slate_id: Annotated[str, strawberry.argument(description='The {Slate.id} of the slate to return')],
        recommendation_count: Annotated[
            Optional[int], strawberry.argument(
                description='Maximum number of recommendations to return in {Slate.recommendations}, defaults to 10')
        ] = 10
) -> Optional[Slate]:
    slate_model = await SlateModel.get_slate(
        slate_id=slate_id,
        user_id=info.context.get('request').headers.get('userId'),
        recommendation_count=recommendation_count)

    return Slate.from_pydantic(slate_model)
