from datetime import datetime
from typing import List

from pydantic import BaseModel, Field

from app.models.corpus_slate_model import CorpusSlateModel


class CorpusSlateLineupModel(BaseModel):
    id: str = Field(description='UUID')
    slates: List[CorpusSlateModel] = Field(description='Slates.')
    recommended_at: datetime  # UTC time when the slate was recommended
