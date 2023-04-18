from aio_snowplow_tracker import Tracker, Emitter
from aio_snowplow_tracker.typing import HttpProtocol, Method

from app.config import ENV, ENV_PROD, ENV_DEV, ENV_LOCAL


class SnowplowConfig:
    APP_ID = f'pocket-data-products-recommendation-api-{ENV}'

    PROD_ENDPOINT_URL = 'com-getpocket-prod1.collector.snplow.net'
    DEV_ENDPOINT_URL = 'com-getpocket-prod1.mini.snplow.net'
    LOCAL_ENDPOINT_URL = 'snowplow:9090'
    ENDPOINT_URL = (
        PROD_ENDPOINT_URL if ENV == ENV_PROD else
        DEV_ENDPOINT_URL if ENV == ENV_DEV else
        LOCAL_ENDPOINT_URL
    )

    PROTOCOL: HttpProtocol = 'http' if ENV == ENV_LOCAL else 'https'
    METHOD: Method = 'post'
    BUFFER_SIZE: int = 1  # Number of events to buffer before flushing to Snowplow. 1 = No buffer.


def create_snowplow_tracker() -> Tracker:
    """
    Helper method to instantiate a Snowplow Tracker.
    :return:
    """
    emitter = Emitter(
        SnowplowConfig.ENDPOINT_URL,
        protocol=SnowplowConfig.PROTOCOL,
        method=SnowplowConfig.METHOD,
        buffer_size=SnowplowConfig.BUFFER_SIZE,
    )
    return Tracker(emitter, app_id=SnowplowConfig.APP_ID)
