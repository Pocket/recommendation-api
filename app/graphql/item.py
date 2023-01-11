from typing import List

import strawberry

from app.graphql.corpus_recommendation import CorpusRecommendation
from app.graphql.resolvers.item2item_resolvers import resolve_similar_to_saved
from app.models.item import ItemModel

# todo: figure out how to add pydantic convertion
@strawberry.federation.type(keys=["itemId"])
# @strawberry.experimental.pydantic.type(model=ItemModel)
class Item:
    itemId: str  # This type is a 'str' and not an 'ID' in our graph.

    relatedAfterArticle: List[CorpusRecommendation] = strawberry.field(
        resolver=resolve_similar_to_saved,
        description='Recommend similar articles to show in the bottom of an article.')

    relatedAfterCreate: List[CorpusRecommendation] = strawberry.field(
        resolver=resolve_similar_to_saved,
        description='Recommend similar articles after saving in Firefox.')

    @classmethod
    def resolve_reference(cls, itemId: str):
        return Item(itemId=itemId)
