from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field

from app.models.corpus_recommendation_model import CorpusRecommendationModel


class CorpusSlateModel(BaseModel):
    """
    Models a corpus slate
    """
    id: str = Field(description='UUID')
    recommendations: List[CorpusRecommendationModel] = Field(
        description='Recommendations for the current request context.')
    recommended_at: datetime = Field(description='UTC time when the slate was recommended')
    headline: str = Field(
        description='The display headline for the slate. Surface context may be required to render determine what to '
                    'display. This will depend on if we connect the copy to the Surface, SlateExperiment, or Slate.')
    subheadline: Optional[str] = Field(
        default=None,
        description='A smaller, secondary headline that can be displayed to provide additional context on the slate.')
    more_link_url: str = Field(
        default=None,
        description='The URL destination of the page to explore more content like this Slate.')
    more_link_name: str = Field(
        default=None,
        description='The display name for the link to explore more content like this Slate.')


