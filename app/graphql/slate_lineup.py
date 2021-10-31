import strawberry

from app.models.slate_lineup import SlateLineupModel


@strawberry.experimental.pydantic.type(model=SlateLineupModel, all_fields=True)
class SlateLineup:
    pass
