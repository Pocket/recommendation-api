import asyncio

from app.data_providers.snowplow.config import SnowplowConfig
from app.data_providers.snowplow.snowplow_corpus_slate_lineup_tracker import SnowplowCorpusSlateLineupTracker
from app.models.unleash_assignment import UnleashAssignmentModel

# PyTest is not able to find fixtures in these files without importing them.
from tests.mocks.snowplow import *
from tests.mocks.corpus_slate_lineup_model import *
from tests.mocks.user import *


@pytest.mark.asyncio
async def test_track_successful_response(snowplow_server, lineup_with_business_slate, user_1, caplog):
    snowplow_tracker = create_snowplow_tracker(snowplow_server)
    slate_tracker = SnowplowCorpusSlateLineupTracker(snowplow_tracker, SnowplowConfig())
    await slate_tracker.track(lineup_with_business_slate, user=user_1)

    # No warnings, errors, or critical log statements were created.
    assert not any(r for r in caplog.records if r.levelname in ('WARNING', 'ERROR', 'CRITICAL'))
    # Assert one request was made to Snowplow
    assert len(snowplow_server.app['requests']) == 1


@pytest.mark.asyncio
async def test_track_successful_experiment_response(snowplow_server, lineup_with_business_slate, user_1, caplog):
    snowplow_tracker = create_snowplow_tracker(snowplow_server)
    lineup_with_business_slate.experiment = UnleashAssignmentModel(assigned=True, name='getstarted', variant='control')

    slate_tracker = SnowplowCorpusSlateLineupTracker(snowplow_tracker, SnowplowConfig())
    await slate_tracker.track(lineup_with_business_slate, user=user_1)

    # No warnings, errors, or critical log statements were created.
    assert not any(r for r in caplog.records if r.levelname in ('WARNING', 'ERROR', 'CRITICAL'))
    # Assert one request was made to Snowplow
    assert len(snowplow_server.app['requests']) == 1


@pytest.mark.asyncio
async def test_track_failure_response(
        snowplow_tracker_with_server_failure, lineup_with_business_slate, user_1, caplog):
    slate_tracker = SnowplowCorpusSlateLineupTracker(snowplow_tracker_with_server_failure, SnowplowConfig())
    # Snowplow server errors don't cause an exception. Our service should continue to function independent of Snowplow.
    await slate_tracker.track(lineup_with_business_slate, user=user_1)

    # Assert that a 501 status code was logged.
    error_logs = [r for r in caplog.records if r.levelname == 'ERROR']
    assert len(error_logs) == 1
    assert "status code: 501" in error_logs[0].message
