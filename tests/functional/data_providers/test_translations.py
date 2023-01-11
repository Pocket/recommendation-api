from app.config import TRANSLATIONS_DIR
from app.data_providers.translation import TranslationProvider
from app.models.localemodel import LocaleModel


def test_home_translations():
    translation_provider = TranslationProvider(translations_dir=TRANSLATIONS_DIR)
    home_translations = translation_provider.get_translations(locale=LocaleModel.en_US, filename='home.json')

    assert home_translations['ForYouSlateProvider.headline'] == 'For You'
    assert home_translations['LifeHacksSlateProvider.subheadline'] == 'Tips for better living'
