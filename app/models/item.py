from pydantic import BaseModel


class ItemModel(BaseModel):
    item_id: str
