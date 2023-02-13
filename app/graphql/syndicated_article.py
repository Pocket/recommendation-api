from typing import List

import strawberry
from strawberry.federation.schema_directives import Requires

from app.graphql.corpus_recommendation import CorpusRecommendation
from app.graphql.directives import CacheControl
from app.graphql.resolvers.item2item_resolvers import resolve_syndicated_end_of_article, resolve_syndicated_right_rail


@strawberry.federation.type(keys=["itemId"])
class SyndicatedArticle:
    itemId: strawberry.ID  # this corresponds to Snowflake resolved_id

    # these fields are from a different subgraph
    # see https://www.apollographql.com/docs/federation/entities-advanced/#contributing-computed-entity-fields
    publisherUrl: str = strawberry.federation.field(external=True)
    originalItemId: strawberry.ID = strawberry.federation.field(external=True)

    relatedEndOfArticle: List[CorpusRecommendation] = strawberry.field(
        directives=[CacheControl(maxAge=3600)],
        resolver=resolve_syndicated_end_of_article,
        description='Recommend similar syndicated articles.')
    relatedRightRail: List[CorpusRecommendation] = strawberry.field(
        directives=[CacheControl(maxAge=3600),
                    Requires(fields='publisherUrl originalItemId')],
        resolver=resolve_syndicated_right_rail,
        description='Recommend similar articles from the same publisher.')

