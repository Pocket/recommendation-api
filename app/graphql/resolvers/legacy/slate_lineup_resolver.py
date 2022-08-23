from strawberry.types import Info

from app.graphql.slate_lineup import SlateLineup
from app.models.slate_lineup import SlateLineupModel


async def resolve_get_slate_lineup(
        root, info: Info, slate_lineup_id: str, recommendation_count: int = 10, slate_count: int = 8) -> SlateLineup:
    slate_lineup_model = await SlateLineupModel.get_slate_lineup_with_fallback(
        slate_lineup_id=slate_lineup_id,
        user_id=info.context.get('request').headers.get('userId'),
        recommendation_count=recommendation_count,
        slate_count=slate_count)

    return SlateLineup.from_pydantic(slate_lineup_model)
