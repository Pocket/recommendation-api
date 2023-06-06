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

        # Accept underscore without region
        ('en_US', None, RecommendationSurfaceId.NEW_TAB_EN_US),
        ('en_GB', None, RecommendationSurfaceId.NEW_TAB_EN_GB),
        ('en_IE', None, RecommendationSurfaceId.NEW_TAB_EN_GB),
        ('en_IN', None, RecommendationSurfaceId.NEW_TAB_EN_INTL),
        ('de_DE', None, RecommendationSurfaceId.NEW_TAB_DE_DE),
        ('es_ES', None, RecommendationSurfaceId.NEW_TAB_ES_ES),
        ('fr_FR', None, RecommendationSurfaceId.NEW_TAB_FR_FR),
        ('it_IT', None, RecommendationSurfaceId.NEW_TAB_IT_IT),

        # Accept dashes instead of underscores.
        ('en-US', None, RecommendationSurfaceId.NEW_TAB_EN_US),
        ('en-GB', None, RecommendationSurfaceId.NEW_TAB_EN_GB),
        ('en-IE', None, RecommendationSurfaceId.NEW_TAB_EN_GB),

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

        # Accept underscore and region
        ('en_US', 'US', RecommendationSurfaceId.NEW_TAB_EN_US),
        ('en_GB', 'GB', RecommendationSurfaceId.NEW_TAB_EN_GB),
        ('de_DE', 'DE', RecommendationSurfaceId.NEW_TAB_DE_DE),

        # Explicit region overrides region in locale language variant
        ('en_GB', 'US', RecommendationSurfaceId.NEW_TAB_EN_US),
        ('en_US', 'GB', RecommendationSurfaceId.NEW_TAB_EN_GB),
        ('en_US', 'IE', RecommendationSurfaceId.NEW_TAB_EN_GB),
        ('en_US', 'IN', RecommendationSurfaceId.NEW_TAB_EN_INTL),

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
