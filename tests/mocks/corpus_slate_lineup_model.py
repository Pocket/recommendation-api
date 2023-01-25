from app.models.corpus_slate_lineup_model import CorpusSlateLineupModel, RecommendationSurfaceId
from app.models.localemodel import LocaleModel

from tests.mocks.corpus_slate_model import *


@pytest.fixture
def lineup_with_business_slate(corpus_slate_10_business_recs):
    return CorpusSlateLineupModel(
        slates=[corpus_slate_10_business_recs],
        recommendation_surface_id=RecommendationSurfaceId.HOME,
        locale=LocaleModel.en_US,
    )
