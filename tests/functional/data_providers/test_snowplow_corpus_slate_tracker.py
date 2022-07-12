from app.data_providers.snowplow.config import SnowplowConfig
from app.data_providers.snowplow.snowplow_corpus_slate_tracker import SnowplowCorpusSlateTracker

# PyTest is not able to find fixtures in these files without importing them.
from tests.mocks.snowplow import *
from tests.mocks.corpus_slate_model import *


async def test_track_successful_response(snowplow_tracker, corpus_slate_10_business_recs, caplog):
    slate_tracker = SnowplowCorpusSlateTracker(snowplow_tracker, snowplow_config=SnowplowConfig())
    await slate_tracker.track(corpus_slate_10_business_recs, user_id='1234')

    # No warnings, errors, or critical log statements were created.
    assert not any(r for r in caplog.records if r.levelname in ('WARNING', 'ERROR', 'CRITICAL'))


async def test_track_failure_response(snowplow_tracker_with_server_failure, corpus_slate_10_business_recs, caplog):
    slate_tracker = SnowplowCorpusSlateTracker(snowplow_tracker_with_server_failure, snowplow_config=SnowplowConfig())
    # Snowplow server errors don't cause an exception. Our service should continue to function independent of Snowplow.
    await slate_tracker.track(corpus_slate_10_business_recs, user_id='1234')

    # Assert that a 501 status code was logged.
    # TODO: We should change this level from 'warning' to 'error' in aio_snowplow_tracker.
    warning_logs = [r for r in caplog.records if r.levelname == 'WARNING']
    assert len(warning_logs) == 1
    assert "status code: 501" in warning_logs[0].message
