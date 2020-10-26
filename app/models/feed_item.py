from pydantic import BaseModel


class FeedItem(BaseModel):
    id: int
    title: str



