from typing import List, Optional

import strawberry
from strawberry.types import Info
from strawberry import argument
from strawberry.types import Info
from typing_extensions import Annotated

from app.data_providers.dispatch import Item2ItemDispatch
from app.data_providers.item2item import Item2ItemRecommender
from app.graphql.corpus_recommendation import CorpusRecommendation
from app.graphql.util import get_field_argument
from app.singletons import item2item_recommender

DEFAULT_RECOMMENDATION_COUNT = 10


async def resolve_syndicated(root, info: Info,
        resolved_id: Annotated[strawberry.ID, argument(
            description='Article ID')],
        recommendation_count: Annotated[Optional[int], argument(
            description='Maximum number of recommendations to return, defaults to 10')] = 10,
) -> List[strawberry.ID]:
    dispatch = Item2ItemDispatch(item_recommender=item2item_recommender)
                                 # , metrics_client=None)

    return [strawberry.ID(str(id))
            for id in await dispatch.syndicated(resolved_id=int(resolved_id),
                                                count=recommendation_count)]


async def resolve_publisher(root, info: Info,
                            resolved_id: Annotated[strawberry.ID, argument(
                                description='Article ID')],
                            domain_id: Annotated[strawberry.ID, argument(
                                description='Domain ID')],
                            recommendation_count: Annotated[Optional[int], argument(
                                description='Maximum number of recommendations to return, defaults to 10')] = 10,
                            ) -> List[strawberry.ID]:
    dispatch = Item2ItemDispatch(item_recommender=item2item_recommender)
                                 # , metrics_client=None)

    return [strawberry.ID(str(id))
            for id in await dispatch.by_publisher(resolved_id=int(resolved_id),
                                                  domain_id=int(domain_id),
                                                  count=recommendation_count)]
