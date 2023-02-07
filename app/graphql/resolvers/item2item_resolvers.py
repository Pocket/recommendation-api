from typing import List, Optional
from urllib.parse import urlparse

from strawberry import argument
from strawberry.types import Info
from typing_extensions import Annotated

from app.data_providers.dispatch import Item2ItemDispatch
from app.graphql.corpus_recommendation import CorpusRecommendation
from app.singletons import DiContainer

DEFAULT_RECOMMENDATION_COUNT = 10


async def resolve_similar_to_saved(
        root: 'Item',
        info: Info,
        count: Annotated[Optional[int], argument(
            description='Maximum number of recommendations to return, defaults to 10')]
        = DEFAULT_RECOMMENDATION_COUNT,
) -> List[CorpusRecommendation]:
    dispatch = Item2ItemDispatch(item_recommender=DiContainer.get().item2item_recommender)
    recs = await dispatch.after_save(resolved_id=int(root.item_id), count=count)
    return [CorpusRecommendation.from_pydantic(rec) for rec in recs]


async def resolve_after_article(
        root: 'Item',
        info: Info,
        count: Annotated[Optional[int], argument(
            description='Maximum number of recommendations to return, defaults to 10')]
        = DEFAULT_RECOMMENDATION_COUNT,
) -> List[CorpusRecommendation]:
    dispatch = Item2ItemDispatch(item_recommender=DiContainer.get().item2item_recommender)
    recs = await dispatch.after_article(resolved_id=int(root.item_id), count=count)
    return [CorpusRecommendation.from_pydantic(rec) for rec in recs]


async def resolve_syndicated_end_of_article(
        root: 'SyndicatedArticle',
        info: Info,
        count: Annotated[Optional[int], argument(
            description='Maximum number of recommendations to return, defaults to 10')]
        = DEFAULT_RECOMMENDATION_COUNT,
) -> List[CorpusRecommendation]:
    dispatch = Item2ItemDispatch(item_recommender=DiContainer.get().item2item_recommender)
    recs = await dispatch.syndicated(resolved_id=int(root.itemId), count=count)
    return [CorpusRecommendation.from_pydantic(rec) for rec in recs]


async def resolve_syndicated_right_rail(
        root: 'SyndicatedArticle',
        info: Info,
        count: Annotated[Optional[int], argument(
            description='Maximum number of recommendations to return, defaults to 10')]
        = DEFAULT_RECOMMENDATION_COUNT,
) -> List[CorpusRecommendation]:
    dispatch = Item2ItemDispatch(item_recommender=DiContainer.get().item2item_recommender)

    # domains are stored in snowflake without www
    domain = urlparse(root.publisherUrl).netloc.replace('www.', '')
    recs = await dispatch.by_publisher(resolved_id=int(root.itemId),
                                       domain=domain,
                                       original_id=int(root.originalItemId),
                                       count=count)
    return [CorpusRecommendation.from_pydantic(rec) for rec in recs]
