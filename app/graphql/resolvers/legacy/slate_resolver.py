from strawberry.types import Info

from app.graphql.slate import Slate
from app.models.slate import SlateModel


async def resolve_get_slate(root, info: Info, slate_id: str, recommendation_count: int = 10) -> Slate:
    slate_model = await SlateModel.get_slate(
        slate_id=slate_id,
        user_id=info.context.get('request').headers.get('userId'),
        recommendation_count=recommendation_count)

    return Slate.from_pydantic(slate_model)
