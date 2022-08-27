from pydantic import BaseModel, Field

from app.models.corpus_item_model import CorpusItemModel


class CorpusRecommendationModel(BaseModel):
    id: str = Field(
        description='A unique identifier for this specific recommendation across all recommendations. '
                    'This identifier is generated by the a machine learning system making recommendation decisions. '
                    'This field can be joined with recommendation decisions to aggregate more meta data about the '
                    'decision.')

    corpus_item: CorpusItemModel = Field(description='Content meta data.')
