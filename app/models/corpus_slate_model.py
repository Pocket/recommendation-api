from datetime import datetime, timezone
from typing import List, Optional, Set, Generator
from uuid import uuid4

from pydantic import BaseModel, Field

from app.models.corpus_recommendation_model import CorpusRecommendationModel
from app.models.link import LinkModel
from app.models.recommendation_reason_type import RecommendationReasonType


class CorpusSlateModel(BaseModel):
    """
    Models a corpus slate
    """
    id: str = Field(default_factory=uuid4, description='UUID')
    recommendations: List[CorpusRecommendationModel] = Field(
        description='Recommendations for the current request context.')
    recommended_at: datetime = Field(
        default_factory=lambda: datetime.now(tz=timezone.utc),
        description='UTC time when the slate was recommended')
    recommendation_reason_type: Optional[RecommendationReasonType] = Field(
        default=None,
        description="Indicates the main type of reason why recommendations are included in this slate, or null if none "
                    "is available."
    )
    headline: str = Field(
        description='The display headline for the slate. Surface context may be required to render determine what to '
                    'display. This will depend on if we connect the copy to the Surface, SlateExperiment, or Slate.')
    subheadline: Optional[str] = Field(
        default=None,
        description='A smaller, secondary headline that can be displayed to provide additional context on the slate.')
    more_link: Optional[LinkModel] = Field(
        default=None,
        description='Link to a page where the user can explore more recommendations similar to this slate, or null if '
                    'no link is provided.')

    def remove_corpus_items(self, corpus_item_ids: Set[str]) -> 'CorpusSlateModel':
        """
        Remove recommendations from this slate which match the given corpus item ids.
        :param corpus_item_ids: CorpusItem ids to be removed from this slate.
        :return: self
        """
        self.recommendations = [r for r in self.recommendations if r.corpus_item.id not in corpus_item_ids]
        return self

    def limit(self, count: int) -> 'CorpusSlateModel':
        """
        Keep the first _count_ recommendations in this slate.
        :param count: Maximum number of recommendations to keep.
        :return: self
        """
        self.recommendations = self.recommendations[:count]
        return self

    def corpus_item_ids(self) -> Generator[str, None, None]:
        """
        :return: This slate's CorpusItem ids in-order of recommendation
        """
        return (r.corpus_item.id for r in self.recommendations)
