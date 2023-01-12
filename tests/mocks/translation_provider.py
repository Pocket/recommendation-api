import pytest

from app.config import TRANSLATIONS_DIR
from app.data_providers.translation import TranslationProvider


@pytest.fixture
def translation_provider():
    return TranslationProvider(translations_dir=TRANSLATIONS_DIR)
