import pytest

from app.models.corpus_item_model import CorpusItemModel
from tests.assets.topics import business_topic


@pytest.mark.parametrize(('url', 'is_syndicated'), [
    ('https://getpocket.com/explore/item/8-natural-ways-to-repel-insects-without-bug-spray', True),
    ('http://getpocket.com/explore/item/8-natural-ways-to-repel-insects-without-bug-spray', True),
    ('https://www.getpocket.com/explore/item/8-natural-ways-to-repel-insects-without-bug-spray', True),
    ('https://pocket.com/explore/item/8-natural-ways-to-repel-insects-without-bug-spray', True),  # pocket.com redirect
    ('https://getpocket.com/explore/item/the-secrets-of-real-life-wedding-crashers?utm_source=pocket-newtab', True),
    ('https://getpocket.com/collections/the-unexpected-flavor-combos-too-delicious-not-to-try', False),  # collection
    ('https://getpocket.com/explore/entertainment', False),  # topic page
    ('https://www.harpersbazaar.com/beauty/hair/a44284121/hair-braiders-harlem-injuries-protections/', False),
    ('https://example.com/?utm_content=https://www.getpocket.com/explore/item/example', False),
    (None, None),
])
def test_corpus_item_model_is_syndicated(url, is_syndicated):
    corpus_item = CorpusItemModel(
        id='rec-123',
        topic=business_topic.corpus_topic_id,
        publisher='The Original Publisher',
        url=url,
    )

    assert corpus_item.is_syndicated == is_syndicated
