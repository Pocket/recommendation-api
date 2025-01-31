import re
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class CorpusItemModel(BaseModel):
    id: str
    topic: str | None = None
    publisher: str | None = None
    url: str | None = None

    ranked_with_engagement_updated_at: Optional[datetime] = Field(
        default=None,
        description='If this recommendation was ranked based on engagement data, this timestamp (in UNIX time, seconds)'
                    ' indicates the recency of the engagement data, enabling us to monitor the delay in our engagement'
                    ' feedback loop. If engagement data was not utilized for ranking, this value will be null.'
    )

    @property
    def is_syndicated(self) -> Optional[bool]:
        """
        :return: True if item is syndicated, False if not syndicated, or None if unknown because url is not available.
        """
        if self.url is not None:
            return re.search(r'^(https?://)?(www\.)?(get)?pocket\.com/explore/item', self.url) is not None
