import pytest
import json

from app.data_providers.snowplow_client import SnowplowClient
from app.graphql.corpus_item import CorpusItem


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
    await snowplow_tracking.log_event(user_id=test_user_id, items = [CorpusItem(id='example-uuid-1'), CorpusItem(id='example-uuid-2'), CorpusItem(id='example-uuid-3')])

    tracked_payload = json.loads(
        mock_tracker.most_recent_payload.__dict__
            .get('nv_pairs')
            .get('recs_api_recommendations'))
    assert tracked_payload.get('recommendation_id') is not None # This is a uuid generated at call time
    assert tracked_payload.get('user_id') == test_user_id
    assert tracked_payload.get('slate_experiment_id') is None

    item_list = tracked_payload.get('items')
    assert len(item_list) == 3
    assert all([item.get('recommendation_item_id') for item in item_list]) # These are uuids generated at call time
    assert [item.get('scheduled_corpus_item_id') for item in item_list] == ["example-uuid-1", "example-uuid-2", "example-uuid-3"]

