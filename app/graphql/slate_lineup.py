from graphene_pydantic import PydanticObjectType
from app.models.slate_lineup import SlateLineupModel


class SlateLineup(PydanticObjectType):
    class Meta:
        model = SlateLineupModel
