import json
from abc import ABC, abstractmethod
from functools import lru_cache
from os import path
from typing import Dict, Any

from app.models.localemodel import LocaleModel


class TranslationProvider:
    def __init__(self, translations_dir: str):
        self.translations_dir = translations_dir

    @lru_cache(maxsize=None)
    def load_locales_file(self, locale: str, file: str) -> Dict[str, str]:
        """
        :param locale: Locale corresponding to a subdirectory of the translations' directory (e.g. en-US)
        :param file: Filename (e.g. home.json)
        :return: Dict mapping translation keys to translated strings
        """
        with open(path.join(self.translations_dir, locale, file), 'r') as fp:
            return json.load(fp)


class Translations(ABC):
    """
    Abstract class providing translation strings. A Translations object can be used like a dict:
    """

    def __init__(self, locale: LocaleModel, translations_provider: TranslationProvider):
        self.locale = locale
        self.translations_provider = translations_provider

    @property
    @abstractmethod
    def _translation_filename(self) -> str:
        """
        :return: The translation filename, e.g. home.json
        """
        return NotImplemented

    @property
    def _strings(self) -> Dict[str, str]:
        return self.translations_provider.load_locales_file(locale=self.locale.value, file=self._translation_filename)

    def __getitem__(self, item: str) -> str:
        return self._strings[item]

    def __contains__(self, item):
        return item in self._strings

    def get(self, key: str, default: Any):
        return self._strings.get(key, default)


class HomeTranslations(Translations):
    @property
    def _translation_filename(self) -> str:
        return 'home.json'
