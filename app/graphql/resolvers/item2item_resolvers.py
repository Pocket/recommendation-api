from typing import List

from strawberry.types import Info

from app.data_providers.dispatch import Item2ItemDispatch
from app.data_providers.item2item import Item2ItemRecommender
from app.graphql.corpus_recommendation import CorpusRecommendation
from app.graphql.util import get_field_argument

DEFAULT_RECOMMENDATION_COUNT = 10


async def resolve_syndicated(root, info: Info) -> List[CorpusRecommendation]:
    recommendation_count = int(get_field_argument(
        fields=info.selected_fields,
        field_path=['item2item', 'syndicated'],
        argument_name='count',
        default_value=DEFAULT_RECOMMENDATION_COUNT))

    resolved_id = str(get_field_argument(
        fields=info.selected_fields,
        field_path=['item2item', 'syndicated'],
        argument_name='resolved_id'))

    recommender = Item2ItemRecommender()

    dispatch = Item2ItemDispatch(item_recommender=recommender, metrics_client=None)

    return await dispatch.syndicated(item_id=resolved_id, count=recommendation_count)


async def resolve_publisher(root, info: Info) -> List[CorpusRecommendation]:
    recommendation_count = int(get_field_argument(
        fields=info.selected_fields,
        field_path=['item2item', 'publisher'],
        argument_name='count',
        default_value=DEFAULT_RECOMMENDATION_COUNT))

    domain_id = int(get_field_argument(
        fields=info.selected_fields,
        field_path=['item2item', 'publisher'],
        argument_name='domain_id'))

    resolved_id = str(get_field_argument(
        fields=info.selected_fields,
        field_path=['item2item', 'publisher'],
        argument_name='resolved_id'))

    recommender = Item2ItemRecommender()
    dispatch = Item2ItemDispatch(item_recommender=recommender, metrics_client=None)

    return await dispatch.by_publisher(item_id=resolved_id,
                                       domain_id=domain_id,
                                       count=recommendation_count)
