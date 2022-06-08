from pydantic import BaseModel


class CorpusItemModel (BaseModel):
    id: str
    topic: str = None
