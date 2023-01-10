from enum import Enum


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

    @classmethod
    def from_string(cls, val: str, default: en_US) -> 'LocaleModel':
        for locale in cls:
            if locale.value.lower() == val.lower():
                return locale

        return default
