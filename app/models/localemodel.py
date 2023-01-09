from enum import Enum


class LocaleModel(Enum):
    en_US = 'en-US'
    de_DE = 'de-DE'

    @classmethod
    def from_string(cls, val: str) -> 'LocaleModel':
        for locale in cls:
            if locale.value.lower() == val.lower():
                return locale

        for locale in cls:
            if locale.value.lower().startswith(val.lower()):
                return locale

        return LocaleModel.en_US
