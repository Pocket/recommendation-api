import json
import os
from collections import Counter

import pytest

from app.config import ROOT_DIR
from app.models.prospect_model import ProspectModel
from app.rankers.new_tab_scheduler import select_articles, DEFAULT_TOPIC_LIMITS

N_TEST_REPEATS = 10


@pytest.fixture(scope="module")
def prospects_data():
    with open(os.path.join(ROOT_DIR, 'tests/assets/json/get_prospects.json')) as fp:
        return json.load(fp)


@pytest.fixture()
def prospects(prospects_data):
    prospects_list = prospects_data['data']['getProspects']
    return [
        ProspectModel(
            quality_score=1 - (i / len(prospects_list)),  # dummy linear quality score based on ranking
            **a
        )
        for i, a in enumerate(prospects_list)
    ]


@pytest.mark.parametrize('repeat', range(N_TEST_REPEATS))
@pytest.mark.parametrize(
    'topic_duplicate_limits,'
    'topic_duplicate_limit_fallback,'
    'publisher_duplicate_limit,'
    'optimal_length,'
    'optimal_total_score',
    [
        # Optimal length and total score were found by calling select_articles with n_gen=5000
        (DEFAULT_TOPIC_LIMITS, 2, 2, 21, 13.94),  # Different limits per topic
        (dict(), 3, 2, 21, 14.2),  # Fixed topic (3) and publisher (2) limits
        (dict(), 1, 1, 10, 7.22),  # Fixed topic (1) and publisher (1) limits
        (dict(), 0, 0, 0, 0),  # No prospects are expected to be selected when limits are 0
        (dict(), 50, 50, 50, 25.5),  # All prospects are selected when limits are high
    ])
def test_new_tab_scheduler(
        prospects,
        repeat,
        topic_duplicate_limits,
        topic_duplicate_limit_fallback,
        publisher_duplicate_limit,
        optimal_length,
        optimal_total_score,
):
    selection = select_articles(
        prospects,
        topic_duplicate_limits=topic_duplicate_limits,
        topic_duplicate_limit_fallback=topic_duplicate_limit_fallback,
        publisher_duplicate_limit=publisher_duplicate_limit,
        # n_gen=5000  # Uncomment to find what is presumed to be the optimal solution
    )

    # Check that the number of selected items is close to expected. abs=2 means that a difference of 2 is allowed.
    assert len(selection) == pytest.approx(optimal_length, abs=2)

    # Check that total score is close to expected. rel=.2 means that a difference of 20% is allowed.
    assert sum(a.quality_score for a in selection) == pytest.approx(optimal_total_score, rel=.2)

    # Assert that the same topics are not selected too many times.
    for topic, count in Counter(a.topic for a in selection).items():
        assert count <= topic_duplicate_limits.get(topic, topic_duplicate_limit_fallback),\
            f"{count} {topic} items is more than {topic_duplicate_limit_fallback}"

    # Assert that the same publishers are not selected too many times.
    for pub, count in Counter(a.publisher for a in selection).items():
        assert count <= publisher_duplicate_limit, f"{count} {pub} items is more than {publisher_duplicate_limit}"
