import pytest

from app.data_providers.snowplow.config import SnowplowConfig
from tests.functional.test_util.snowplow import SnowplowMicroClient


@pytest.fixture
def snowplow_micro() -> SnowplowMicroClient:
    snowplow_micro = SnowplowMicroClient(config=SnowplowConfig())
    snowplow_micro.reset_snowplow_events()
    return snowplow_micro
