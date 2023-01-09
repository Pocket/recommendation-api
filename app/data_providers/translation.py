from functools import lru_cache
import json
import os
from abc import ABC, abstractmethod
from os import path
from typing import Dict, List, Any

from app.models.localemodel import LocaleModel


class TranslationProvider:
    def __init__(self, translations_dir: str):
        self.translations_dir = translations_dir

    @lru_cache(maxsize=None)
    def _get_valid_locales(self) -> List[str]:
        """
        :return: Locales for which translations are available.
        """
        return [f.name for f in os.scandir(self.translations_dir) if f.is_dir()]

    @lru_cache(maxsize=None)
    def load_locales_file(self, locale: str, file: str) -> Dict[str, str]:
        """
        :param locale: Locale corresponding to a subdirectory of the translations' directory.
        :param file: Filename without .json extension
        :return: Dict mapping translation keys to translated strings
        """
        with open(path.join(self.translations_dir, locale, f'{file}.json'), 'r') as fp:
            return json.load(fp)


class Translations(ABC):
    def __init__(self, locale: LocaleModel, translations_provider: TranslationProvider):
        self.locale = locale
        self.translations_provider = translations_provider

    @property
    @abstractmethod
    def _translation_filename(self) -> str:
        """
        :return: The translations filename without a .json extension
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
        return 'home'


class TopicTranslations(Translations):
    @property
    def _translation_filename(self) -> str:
        return 'topic'
