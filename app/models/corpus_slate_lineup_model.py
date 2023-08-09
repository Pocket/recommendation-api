from enum import Enum
from typing import List, Optional
from uuid import uuid4

from pydantic import BaseModel, Field

from app.models.corpus_slate_model import CorpusSlateModel


class RecommendationSurfaceId(Enum):
    """
    Defines the possible recommendation surfaces. Currently, these are distinct from the GraphQL 'scheduled surfaces',
    but eventually we'll probably want to merge these concepts.
    """
    HOME = 'HOME'
    NEW_TAB_EN_US = 'NEW_TAB_EN_US'
    NEW_TAB_EN_GB = 'NEW_TAB_EN_GB'
    NEW_TAB_EN_INTL = 'NEW_TAB_EN_INTL'
    NEW_TAB_DE_DE = 'NEW_TAB_DE_DE'
    NEW_TAB_ES_ES = 'NEW_TAB_ES_ES'
    NEW_TAB_FR_FR = 'NEW_TAB_FR_FR'
    NEW_TAB_IT_IT = 'NEW_TAB_IT_IT'


class CorpusSlateLineupModel(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()), description='UUID')
    slates: List[CorpusSlateModel] = Field(description='Slates.')
