import json
import os
from collections import Counter

import pytest

from app.config import ROOT_DIR
from app.models.prospect_model import ProspectModel
from app.rankers.new_tab_scheduler import select_articles


N_TEST_REPEATS = 10


@pytest.fixture(scope="module")
def prospects_data():
    with open(os.path.join(ROOT_DIR, 'tests/assets/json/get_prospects.json')) as fp:
        return json.load(fp)


@pytest.mark.parametrize('repeat', range(N_TEST_REPEATS))
@pytest.mark.parametrize(
    'topic_duplicate_limit, publisher_duplicate_limit, optimal_length, optimal_total_score',
    [
        # Optimal length and total score were found by calling select_articles with n_gen=5000
        (2, 2, 17, 12.6),
        (1, 1, 10, 7.22),
        (3, 2, 21, 14.2),
        (0, 0, 0, 0),  # No prospects are expected to be selected when limits are 0
        (50, 50, 50, 25.5),  # All prospects are expected to be selected when limits equal to the number of prospects
    ])
def test_new_tab_scheduler(
        prospects_data,
        repeat,
        topic_duplicate_limit,
        publisher_duplicate_limit,
        optimal_length,
        optimal_total_score,
):
    article_data = prospects_data['data']['getProspects']
    articles = [
        ProspectModel(
            quality_score=1 - (i / len(article_data)),  # dummy linear quality score based on ranking
            **a
        )
        for i, a in enumerate(article_data)
    ]

    selection = select_articles(
        articles,
        topic_duplicate_limit=topic_duplicate_limit,
        publisher_duplicate_limit=publisher_duplicate_limit,
        # n_gen=5000  # Uncomment to find what is presumed to be the optimal solution
    )

    # Check that the number of selected items is close to expected. abs=1 means that a difference of 1 is allowed.
    assert len(selection) == pytest.approx(optimal_length, abs=1)

    # Check that total score is close to expected. rel=.1 means that a difference of 10% is allowed.
    assert sum(a.quality_score for a in selection) == pytest.approx(optimal_total_score, rel=.1)

    # Assert that the same topics are not selected too many times.
    for topic, count in Counter(a.topic for a in selection).items():
        assert count <= topic_duplicate_limit, f"{count} {topic} items is more than {topic_duplicate_limit}"

    # Assert that the same publishers are not selected too many times.
    for pub, count in Counter(a.publisher for a in selection).items():
        assert count <= publisher_duplicate_limit, f"{count} {pub} items is more than {publisher_duplicate_limit}"
