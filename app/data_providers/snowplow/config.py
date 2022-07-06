from snowplow_tracker import Tracker, Emitter
from snowplow_tracker.typing import HttpProtocol

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

    CORPUS_SLATE_SCHEMA = 'iglu:com.pocket/corpus_slate/jsonschema/1-0-0'
    USER_SCHEMA = 'iglu:com.pocket/user/jsonschema/1-0-0'
    OBJECT_UPDATE_SCHEMA = 'iglu:com.pocket/object_update/jsonschema/1-0-7'


def create_snowplow_tracker() -> Tracker:
    """
    Helper method to instantiate a Snowplow Tracker.
    :return:
    """
    # NOTE: Snowplow has an 'Emitter' and a 'AsyncEmitter'. The latter works with threads, and it still blocks the
    # eventloop. I did not find any implementation of an asyncio Snowplow tracker.
    emitter = Emitter(
        SnowplowConfig.ENDPOINT_URL,
        protocol=SnowplowConfig.PROTOCOL,
    )
    return Tracker(emitter, app_id=SnowplowConfig.APP_ID)
