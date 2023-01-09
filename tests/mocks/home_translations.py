import pytest

from app.config import TRANSLATIONS_DIR
from app.data_providers.translation import TranslationProvider, HomeTranslations
from app.models.localemodel import LocaleModel


@pytest.fixture
def en_us_home_translations():
    translation_provider = TranslationProvider(translations_dir=TRANSLATIONS_DIR)
    return HomeTranslations(locale=LocaleModel.en_US, translations_provider=translation_provider)
