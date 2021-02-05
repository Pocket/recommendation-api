from graphene_pydantic import PydanticObjectType
from app.models.layout import LayoutModel


class Layout(PydanticObjectType):
    class Meta:
        model = LayoutModel
