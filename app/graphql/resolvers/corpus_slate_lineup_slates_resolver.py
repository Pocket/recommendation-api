from typing import TYPE_CHECKING, Optional, List

from app.graphql.corpus_slate import CorpusSlate

if TYPE_CHECKING:
    from app.graphql.corpus_slate_lineup import CorpusSlateLineup


DEFAULT_SLATE_COUNT = 15  # The maximum number of recommendations that is returned by default in a CorpusSlate.


def corpus_slate_lineup_slates_resolver(
        root: 'CorpusSlateLineup', count: Optional[int] = DEFAULT_SLATE_COUNT) -> List[CorpusSlate]:
    """
    Currently, the only way to define arguments on nested objects in Strawberry is to define a resolver.
    :param root: The CorpusSlateLineup object of which slates is a field.
    :param count: The maximum number of Corpus slates to return
    :return: This resolver assumes that the Query resolver generates slates, and returns `root.slates`
    """
    return root.slates[:count]
