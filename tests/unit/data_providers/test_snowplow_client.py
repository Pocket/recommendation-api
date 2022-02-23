import pytest
import json

from app.data_providers.snowplow_client import SnowplowClient

class MockTracker():
    def __init__(self):
        self.most_recent_payload = {}

    def track(self, pb):
        self.most_recent_payload = pb

@pytest.mark.asyncio
async def test_log_event():
    mock_tracker = MockTracker()

    snowplow_tracking = SnowplowClient(tracker=mock_tracker)

    test_user_id = 14464
    await snowplow_tracking.log_event(user_id=test_user_id, items = [])

    tracked_payload = json.loads(
        mock_tracker.most_recent_payload.__dict__
            .get('nv_pairs')
            .get('recs_api_recommendations'))
    assert tracked_payload.get('user_id') == test_user_id
