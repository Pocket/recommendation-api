from typing import Optional

import strawberry

from app.graphql.corpus_item import CorpusItem
from app.models.corpus_recommendation_model import CorpusRecommendationModel


@strawberry.experimental.pydantic.type(model=CorpusRecommendationModel)
class CorpusRecommendation:
    id: strawberry.ID
    corpus_item: strawberry.auto
