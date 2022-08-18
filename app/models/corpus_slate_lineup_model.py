from datetime import datetime
from typing import List

from pydantic import BaseModel

from app.models.corpus_slate_model import CorpusSlateModel


class CorpusSlateLineupModel(BaseModel):
    id: str
    slates: List[CorpusSlateModel]
    recommended_at: datetime  # UTC time when the slate was recommended
