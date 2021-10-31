import strawberry

from app.models.slate import SlateModel


@strawberry.federation.type(extend=True, keys=["id"])
@strawberry.experimental.pydantic.type(model=SlateModel, all_fields=True)
class Slate:
    pass
