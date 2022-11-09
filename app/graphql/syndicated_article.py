from typing import List

import strawberry

from app.graphql.corpus_recommendation import CorpusRecommendation
from app.graphql.resolvers.item2item_resolvers import resolve_end_of_article, resolve_right_rail


@strawberry.federation.type(keys=["itemId", "publisherUrl"])
class SyndicatedArticle:
    itemId: strawberry.ID  # this corresponds to Snowflake resolved_id
    publisherUrl: str

    relatedEndOfArticle: List[CorpusRecommendation] = strawberry.field(
        resolver=resolve_end_of_article,
        description='Recommend similar syndicated articles.')
    relatedRightRail: List[CorpusRecommendation] = strawberry.field(
        resolver=resolve_right_rail,
        description='Recommend similar articles from the same publisher.')

    @classmethod
    def resolve_reference(cls, itemId: strawberry.ID, publisherUrl: str):
        return SyndicatedArticle(itemId=itemId, publisherUrl=publisherUrl)

