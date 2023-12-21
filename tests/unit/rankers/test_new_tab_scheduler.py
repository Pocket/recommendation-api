import json
import os
from collections import Counter

import pytest

from app.config import ROOT_DIR
from app.models.prospect_model import ProspectModel
from app.rankers.new_tab_scheduler import select_articles, DEFAULT_DUPLICATE_LIMIT


@pytest.mark.parametrize('repeat', range(100))
def test_new_tab_scheduler(repeat):
    with open(os.path.join(ROOT_DIR, 'tests/assets/json/get_prospects.json')) as fp:
        data = json.load(fp)

    article_data = data['data']['getProspects']
    articles = [
        ProspectModel(
            quality_score=1 - (i / len(article_data)),  # dummy linear quality score based on ranking
            **a
        )
        for i, a in enumerate(article_data)
    ]

    selection = select_articles(articles)

    # Assert that close to the maximum number of articles are selected. 5000 iterations results in 17 selected articles.
    assert len(selection) == pytest.approx(17, rel=1)

    # Assert that close to the maximum score achieved. 5000 iterations results in a sum of 12.6.
    assert sum(a.quality_score for a in selection) == pytest.approx(12.6, rel=1)

    # The same topic can be selected at most twice.
    for topic, count in Counter(a.topic for a in selection).items():
        assert count <= DEFAULT_DUPLICATE_LIMIT, f"{count} {topic} items, which is more than {DEFAULT_DUPLICATE_LIMIT}"

    # The same topic can be selected at most twice.
    for pub, count in Counter(a.publisher for a in selection).items():
        assert count <= DEFAULT_DUPLICATE_LIMIT, f"{count} {pub} items, which is more than {DEFAULT_DUPLICATE_LIMIT}"
