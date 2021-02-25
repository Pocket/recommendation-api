from pydantic import BaseModel
from typing import Optional

class Candidate(BaseModel):
    item_id: int
    publisher: str
    feed_id: Optional[int]
