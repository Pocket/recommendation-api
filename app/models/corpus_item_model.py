from pydantic import BaseModel


class CorpusItemModel(BaseModel):
    id: str
    publisher: str = None
    topic: str = None
