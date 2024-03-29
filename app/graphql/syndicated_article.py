from typing import List

import strawberry

from app.graphql.corpus_recommendation import CorpusRecommendation
from app.graphql.directives import CacheControl
from app.graphql.resolvers.item2item_resolvers import resolve_syndicated_end_of_article, resolve_syndicated_right_rail


@strawberry.federation.type(keys=["itemId publisherUrl originalItemId"])
class SyndicatedArticle:
    itemId: strawberry.ID  # this corresponds to Snowflake resolved_id
    publisherUrl: str
    originalItemId: strawberry.ID

    relatedEndOfArticle: List[CorpusRecommendation] = strawberry.field(
        directives=[CacheControl(maxAge=3600)],
        resolver=resolve_syndicated_end_of_article,
        description='Recommend similar syndicated articles.')
    relatedRightRail: List[CorpusRecommendation] = strawberry.field(
        directives=[CacheControl(maxAge=3600)],
        resolver=resolve_syndicated_right_rail,
        description='Recommend similar articles from the same publisher.')

    @classmethod
    def resolve_reference(cls,
                          itemId: strawberry.ID,
                          publisherUrl: str,
                          originalItemId: strawberry.ID):
        return SyndicatedArticle(itemId=itemId,
                                 publisherUrl=publisherUrl,
                                 originalItemId=originalItemId)
