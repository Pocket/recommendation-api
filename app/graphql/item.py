from typing import List

import strawberry
from strawberry.federation.schema_directives import Key

from app.graphql.corpus_recommendation import CorpusRecommendation
from app.graphql.resolvers.item2item_resolvers import resolve_similar_to_saved
from app.models.item import ItemModel


@strawberry.experimental.pydantic.type(
    model=ItemModel,
    directives=[Key(fields="itemId")])
class Item:
    item_id: str  # This type is a 'str' and not an 'ID' in our graph.

    relatedAfterArticle: List[CorpusRecommendation] = strawberry.field(
        resolver=resolve_similar_to_saved,
        description='Recommend similar articles to show in the bottom of an article.')

    relatedAfterCreate: List[CorpusRecommendation] = strawberry.field(
        resolver=resolve_similar_to_saved,
        description='Recommend similar articles after saving in Firefox.')
