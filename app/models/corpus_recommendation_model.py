from pydantic import BaseModel

from app.models.corpus_item_model import CorpusItemModel


class CorpusRecommendationModel (BaseModel):
    id: str

    corpus_item: CorpusItemModel
