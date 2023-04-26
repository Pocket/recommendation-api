from enum import Enum
from typing import List


class LocaleValue(str):
    @property
    def language(self):
        return self.split('-')[0]

    @property
    def language_variant(self):
        return self.split('-')[1]


class LocaleModel(Enum):
    en_US = LocaleValue('en-US')
    de_DE = LocaleValue('de-DE')
    es_ES = LocaleValue('es-ES')
    fr_FR = LocaleValue('fr-FR')
    it_IT = LocaleValue('it-IT')

    @staticmethod
    def from_string(val: str, available_locales: List['LocaleModel'], default: 'LocaleModel' = None) -> 'LocaleModel':
        """
        :return: The first value in `available_locales` that equals `val` (case-insensitive), otherwise the first locale
                 which language matches the part of `val` before a hyphen (case-insensitive), otherwise the default.
        """
        for locale in available_locales:
            if locale.value.lower() == val.lower():
                return locale

        language = val.split('-')[0].lower()
        for locale in available_locales:
            if locale.value.startswith(language):
                return locale

        return default
