import uuid

import pytest

from app.models.corpus_item_model import CorpusItemModel
from app.models.corpus_recommendation_model import CorpusRecommendationModel
from app.models.corpus_slate_model import CorpusSlateModel


@pytest.fixture
def corpus_slate_10_business_recs():
    return CorpusSlateModel(
        id=str(uuid.uuid4()),
        headline="All your favorite stories",
        recommendations=[
            CorpusRecommendationModel(
                id=str(uuid.uuid4()),
                corpus_item=CorpusItemModel(id=str(uuid.uuid4()), topic="BUSINESS"),
            )
            for _ in range(10)
        ]
    )
