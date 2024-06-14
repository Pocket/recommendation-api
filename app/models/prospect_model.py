from pydantic import BaseModel


class ProspectModel(BaseModel):
    id: str
    topic: str
    publisher: str
    url: str
    quality_score: float
