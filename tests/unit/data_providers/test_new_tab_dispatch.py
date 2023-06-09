import pytest

from app.data_providers.dispatch import NewTabDispatch
from app.models.corpus_slate_lineup_model import RecommendationSurfaceId


@pytest.mark.parametrize(
    "locale,region,recommendation_surface_id",
    [
        # Locale might be a language only
        ('en', 'US', RecommendationSurfaceId.NEW_TAB_EN_US),
        ('en', 'GB', RecommendationSurfaceId.NEW_TAB_EN_GB),
        ('en', 'IE', RecommendationSurfaceId.NEW_TAB_EN_GB),
        ('en', 'IN', RecommendationSurfaceId.NEW_TAB_EN_INTL),
        ('de', 'DE', RecommendationSurfaceId.NEW_TAB_DE_DE),
        ('de', 'DE', RecommendationSurfaceId.NEW_TAB_DE_DE),
        ('de', 'AT', RecommendationSurfaceId.NEW_TAB_DE_DE),
        ('de', 'CH', RecommendationSurfaceId.NEW_TAB_DE_DE),
        ('es', 'LI', RecommendationSurfaceId.NEW_TAB_ES_ES),
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

        # Accept underscores in locale
        ('en_US', None, RecommendationSurfaceId.NEW_TAB_EN_US),
        ('en_GB', None, RecommendationSurfaceId.NEW_TAB_EN_GB),
        ('de_DE', None, RecommendationSurfaceId.NEW_TAB_DE_DE),

        # locale can start/end with whitespace, and case can vary.
        ('\r\n\t  eN_US \n ', None, RecommendationSurfaceId.NEW_TAB_EN_US),
        ('\r\n\t  En_GB \n ', None, RecommendationSurfaceId.NEW_TAB_EN_GB),
        ('\r\n\t  EN_ie \n ', None, RecommendationSurfaceId.NEW_TAB_EN_GB),
        ('\r\n\t  en_IN \n ', None, RecommendationSurfaceId.NEW_TAB_EN_INTL),

        # region can start/end with whitespace, and case can vary.
        ('en', ' \n US  \t', RecommendationSurfaceId.NEW_TAB_EN_US),
        ('en', ' \n gB  \t', RecommendationSurfaceId.NEW_TAB_EN_GB),
        ('en', ' \n Ie  \t', RecommendationSurfaceId.NEW_TAB_EN_GB),
        ('en', ' \n in  \t', RecommendationSurfaceId.NEW_TAB_EN_INTL),

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
