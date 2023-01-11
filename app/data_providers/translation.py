import json
from functools import lru_cache
from os import path
from typing import Dict

from app.models.localemodel import LocaleModel


class TranslationProvider:
    def __init__(self, translations_dir: str):
        self.translations_dir = translations_dir

    @lru_cache(maxsize=None)  # Python 3.9 adds a @cache decorator for a simple unbounded function cache.
    def get_translations(self, locale: LocaleModel, filename: str) -> Dict[str, str]:
        """
        :param locale: Locale corresponding to a subdirectory of the translations' directory (e.g. en-US)
        :param filename: Filename (e.g. home.json)
        :return: Dict mapping translation keys to translated strings
        """
        with open(path.join(self.translations_dir, locale.value, filename), 'r') as fp:
            return json.load(fp)
