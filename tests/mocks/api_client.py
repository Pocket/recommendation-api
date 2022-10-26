import pytest

from app.models.api_client import ApiClient


@pytest.fixture
def web_client():
    return ApiClient(
        consumer_key='web-client-consumer-key',
        api_id='94110',
        application_name='Pocket web-client',
        is_native=True,
        is_trusted=True,
    )
