from typing import Optional, List, TYPE_CHECKING

from app.graphql.corpus_recommendation import CorpusRecommendation

if TYPE_CHECKING:
    from app.graphql.corpus_slate import CorpusSlate


DEFAULT_RECOMMENDATION_COUNT = 6  # The maximum number of recommendations that is returned by default in a CorpusSlate.


def corpus_slate_recommendations_resolver(
        root: 'CorpusSlate', count: Optional[int] = DEFAULT_RECOMMENDATION_COUNT) -> List[CorpusRecommendation]:
    """
    Currently, the only way to define arguments on nested objects in Strawberry is to define a resolver.
    :param root: The CorpusSlate object of which recommendations is a field.
    :param count: The maximum number of Corpus recommendations to return
    :return: This resolver assumes that the Query resolver generates recommendations, and returns `root.recommendations`
    """
    return root.recommendations[:count]
