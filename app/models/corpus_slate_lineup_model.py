from datetime import datetime, timezone
from typing import List
from uuid import uuid4

from pydantic import BaseModel, Field

from app.models.corpus_slate_model import CorpusSlateModel


class CorpusSlateLineupModel(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()), description='UUID')
    slates: List[CorpusSlateModel] = Field(description='Slates.')
    recommended_at: datetime = Field(
        default_factory=lambda: datetime.now(tz=timezone.utc),
        description='UTC time when the slate was recommended')
