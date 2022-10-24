from pydantic import BaseModel


class CorpusItemModel(BaseModel):
    id: str
    publisher: str
    topic: str = None
