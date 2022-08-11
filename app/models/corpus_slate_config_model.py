from pydantic import BaseModel


class CorpusSlateConfigModel(BaseModel):
    """
    Unique identifier for this Corpus Slate config
    """
    id: str
