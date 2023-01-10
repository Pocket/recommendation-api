from app.config import TRANSLATIONS_DIR
from app.data_providers.translation import TranslationProvider, HomeTranslations
from app.models.localemodel import LocaleModel


def test_home_translations():
    translation_provider = TranslationProvider(translations_dir=TRANSLATIONS_DIR)
    home_translations = HomeTranslations(locale=LocaleModel.en_US, translations_provider=translation_provider)

    assert home_translations['ForYouSlateProvider.headline'] == 'For You'
    assert home_translations['LifeHacksSlateProvider.subheadline'] == 'Tips for better living'
