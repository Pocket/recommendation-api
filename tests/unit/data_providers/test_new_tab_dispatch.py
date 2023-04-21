import pytest

from app.data_providers.dispatch import NewTabDispatch
from app.models.corpus_slate_lineup_model import RecommendationSurfaceId
from app.models.localemodel import LocaleModel


@pytest.mark.parametrize(
    "locale,recommendation_surface_id",
    [
        (LocaleModel.en_US, RecommendationSurfaceId.NEW_TAB_EN_US),
        (LocaleModel.de_DE, RecommendationSurfaceId.NEW_TAB_DE_DE),
        (LocaleModel.es_ES, RecommendationSurfaceId.NEW_TAB_ES_ES),
        (LocaleModel.fr_FR, RecommendationSurfaceId.NEW_TAB_FR_FR),
        (LocaleModel.it_IT, RecommendationSurfaceId.NEW_TAB_IT_IT),
    ])
def test_get_recommendation_surface_id(locale: LocaleModel, recommendation_surface_id: RecommendationSurfaceId):
    assert recommendation_surface_id == NewTabDispatch.get_recommendation_surface_id(locale)
