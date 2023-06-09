import pytest

from app.data_providers.dispatch import NewTabDispatch
from app.models.corpus_slate_lineup_model import RecommendationSurfaceId


@pytest.mark.parametrize(
    "locale,region,recommendation_surface_id",
    [
        # Test cases below are from the Newtab locales/region documentation maintained by the Firefox integration team:
        # https://docs.google.com/document/d/1omclr-eETJ7zAWTMI7mvvsc3_-ns2Iiho4jPEfrmZfo/edit
        ('en-CA', 'US', RecommendationSurfaceId.NEW_TAB_EN_US),
        ('en-GB', 'US', RecommendationSurfaceId.NEW_TAB_EN_US),
        ('en-US', 'US', RecommendationSurfaceId.NEW_TAB_EN_US),
        ('en-CA', 'CA', RecommendationSurfaceId.NEW_TAB_EN_US),
        ('en-GB', 'CA', RecommendationSurfaceId.NEW_TAB_EN_US),
        ('en-US', 'CA', RecommendationSurfaceId.NEW_TAB_EN_US),
        ('de', 'DE', RecommendationSurfaceId.NEW_TAB_DE_DE),
        ('de-AT', 'DE', RecommendationSurfaceId.NEW_TAB_DE_DE),
        ('de-CH', 'DE', RecommendationSurfaceId.NEW_TAB_DE_DE),
        ('en-CA', 'GB', RecommendationSurfaceId.NEW_TAB_EN_GB),
        ('en-GB', 'GB', RecommendationSurfaceId.NEW_TAB_EN_GB),
        ('en-US', 'GB', RecommendationSurfaceId.NEW_TAB_EN_GB),
        ('en-CA', 'IE', RecommendationSurfaceId.NEW_TAB_EN_GB),
        ('en-GB', 'IE', RecommendationSurfaceId.NEW_TAB_EN_GB),
        ('en-US', 'IE', RecommendationSurfaceId.NEW_TAB_EN_GB),
        ('fr-FR', 'FR', RecommendationSurfaceId.NEW_TAB_FR_FR),
        ('it', 'IT', RecommendationSurfaceId.NEW_TAB_IT_IT),
        ('es-ES', 'ES', RecommendationSurfaceId.NEW_TAB_ES_ES),
        ('en-CA', 'IN', RecommendationSurfaceId.NEW_TAB_EN_INTL),
        ('en-GB', 'IN', RecommendationSurfaceId.NEW_TAB_EN_INTL),
        ('en-US', 'IN', RecommendationSurfaceId.NEW_TAB_EN_INTL),
        ('de', 'CH', RecommendationSurfaceId.NEW_TAB_DE_DE),
        ('de', 'AT', RecommendationSurfaceId.NEW_TAB_DE_DE),
        ('de', 'BE', RecommendationSurfaceId.NEW_TAB_DE_DE),

        # Locale can be a main language only.
        ('en', 'CA', RecommendationSurfaceId.NEW_TAB_EN_US),
        ('en', 'GB', RecommendationSurfaceId.NEW_TAB_EN_GB),
        ('en', 'IE', RecommendationSurfaceId.NEW_TAB_EN_GB),
        ('en', 'IN', RecommendationSurfaceId.NEW_TAB_EN_INTL),
        ('en', 'US', RecommendationSurfaceId.NEW_TAB_EN_US),
        ('es', 'ES', RecommendationSurfaceId.NEW_TAB_ES_ES),
        ('fr', 'FR', RecommendationSurfaceId.NEW_TAB_FR_FR),
        ('it', 'IT', RecommendationSurfaceId.NEW_TAB_IT_IT),

        # Explicit region overrides region in locale language variant
        ('en-GB', 'US', RecommendationSurfaceId.NEW_TAB_EN_US),
        ('en-US', 'GB', RecommendationSurfaceId.NEW_TAB_EN_GB),
        ('en-US', 'IE', RecommendationSurfaceId.NEW_TAB_EN_GB),
        ('en-US', 'IN', RecommendationSurfaceId.NEW_TAB_EN_INTL),

        # Extract region from locale, if it is not explicitly provided.
        ('en-US', None, RecommendationSurfaceId.NEW_TAB_EN_US),
        ('en-GB', None, RecommendationSurfaceId.NEW_TAB_EN_GB),
        ('en-IE', None, RecommendationSurfaceId.NEW_TAB_EN_GB),

        # locale can start/end with whitespace, and case can vary.
        ('eN-US', None, RecommendationSurfaceId.NEW_TAB_EN_US),
        ('En-GB', None, RecommendationSurfaceId.NEW_TAB_EN_GB),
        ('EN-ie', None, RecommendationSurfaceId.NEW_TAB_EN_GB),
        ('en-IN', None, RecommendationSurfaceId.NEW_TAB_EN_INTL),

        # region can start/end with whitespace, and case can vary.
        ('en', 'US', RecommendationSurfaceId.NEW_TAB_EN_US),
        ('en', 'gB', RecommendationSurfaceId.NEW_TAB_EN_GB),
        ('en', 'Ie', RecommendationSurfaceId.NEW_TAB_EN_GB),
        ('en', 'in', RecommendationSurfaceId.NEW_TAB_EN_INTL),

        # Default to international NewTab when region is unknown.
        ('en', 'XX', RecommendationSurfaceId.NEW_TAB_EN_INTL),

        # Default to English when language is unknown.
        ('xx', 'US', RecommendationSurfaceId.NEW_TAB_EN_US),
        ('xx', 'GB', RecommendationSurfaceId.NEW_TAB_EN_GB),
        ('xx', 'YY', RecommendationSurfaceId.NEW_TAB_EN_INTL),
    ]
)
def test_get_recommendation_surface_id(locale: str, region: str, recommendation_surface_id: RecommendationSurfaceId):
    assert NewTabDispatch.get_recommendation_surface_id(locale, region) == recommendation_surface_id
