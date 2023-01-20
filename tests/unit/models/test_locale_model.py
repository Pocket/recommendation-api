from app.models.localemodel import LocaleModel


def test_from_string_full_locale():
    assert LocaleModel.en_US == LocaleModel.from_string('en-US')
    assert LocaleModel.en_US == LocaleModel.from_string('en-us')
    assert LocaleModel.de_DE == LocaleModel.from_string('de-DE')
    assert LocaleModel.de_DE == LocaleModel.from_string('de-de')


def test_from_string_language_match():
    assert LocaleModel.de_DE == LocaleModel.from_string('de-AT')
    assert LocaleModel.en_US == LocaleModel.from_string('en-CA')


def test_from_string_language_only():
    assert LocaleModel.en_US == LocaleModel.from_string('en')
    assert LocaleModel.en_US == LocaleModel.from_string('EN')
    assert LocaleModel.de_DE == LocaleModel.from_string('de')
    assert LocaleModel.de_DE == LocaleModel.from_string('DE')


def test_from_string_default():
    assert LocaleModel.from_string('xx-YY') is None
    assert LocaleModel.en_US == LocaleModel.from_string('xx-YY', LocaleModel.en_US)
