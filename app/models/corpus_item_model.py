import datetime

from pydantic import BaseModel


class CorpusItemModel(BaseModel):
    id: str
    topic: str = None
    scheduled_date: str = None
