from pytest import fail

from app.data_providers.slate_provider import SlateProvider, InvalidIdError


def test_get__invalid_id():
    provider = SlateProvider()

    try:
        provider.getSlate("DEFINITELY-not-a-valid-id")
        fail("invalid id should raise an exception")
    except InvalidIdError:
        pass


def test_get__nominal():
    provider = SlateProvider()

    german_new_tab_config = provider.getSlate("79655eb2-47a1-4a26-9235-29e4768ff0a1")

    # I tried to pick something we won't change here so we're just testing the get behavior and not
    # our actual documentation strings. PROBABLY the language code should stay in the description though.
    assert "de-DE" in german_new_tab_config.internalDescription
