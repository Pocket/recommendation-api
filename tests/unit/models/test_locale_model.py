from app.models.localemodel import LocaleModel


_ALL_LOCALES = list(LocaleModel.__members__.values())


def test_from_string_full_locale():
    assert LocaleModel.en_US == LocaleModel.from_string('en-US', _ALL_LOCALES)
    assert LocaleModel.en_US == LocaleModel.from_string('en-us', _ALL_LOCALES)
    assert LocaleModel.de_DE == LocaleModel.from_string('de-DE', _ALL_LOCALES)
    assert LocaleModel.de_DE == LocaleModel.from_string('de-de', _ALL_LOCALES)


def test_from_string_language_match():
    assert LocaleModel.de_DE == LocaleModel.from_string('de-AT', _ALL_LOCALES)
    assert LocaleModel.en_US == LocaleModel.from_string('en-CA', _ALL_LOCALES)


def test_from_string_language_only():
    assert LocaleModel.en_US == LocaleModel.from_string('en', _ALL_LOCALES)
    assert LocaleModel.en_US == LocaleModel.from_string('EN', _ALL_LOCALES)
    assert LocaleModel.de_DE == LocaleModel.from_string('de', _ALL_LOCALES)
    assert LocaleModel.de_DE == LocaleModel.from_string('DE', _ALL_LOCALES)


def test_from_string_default():
    assert LocaleModel.from_string('xx-YY', _ALL_LOCALES) is None
    assert LocaleModel.en_US == LocaleModel.from_string('xx-YY', _ALL_LOCALES, LocaleModel.en_US)


def test_from_string_accepted_locales():
    assert LocaleModel.from_string('de-DE', [LocaleModel.en_US]) is None
    assert LocaleModel.en_US == LocaleModel.from_string('en', [LocaleModel.en_US])
