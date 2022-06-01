from graphene import ObjectType, String, Field, List, Int
from graphene_federation import build_schema
import graphql

from app.data_providers.curation_api_client import CurationAPIClient
from app.data_providers.metrics_client import MetricsClient
from app.data_providers.slate_provider import SlateProvider
from app.graphql.ranked_corpus_slate import RankedCorpusSlate
from app.models.corpus_item_model import CorpusItemModel
from app.models.metrics.firefox_new_tab_metrics_factory import FirefoxNewTabMetricsFactory
from app.models.ranked_corpus_slate_instance import RankedCorpusSlateInstance
from app.models.corpus_slate_model import CorpusSlateModel
from app.data_providers.dispatch import Dispatch
from app.graphql.ranked_corpus_items import RankedCorpusItems
from app.graphql.corpus_slate import CorpusSlate
from app.models.ranked_corpus_items_instance import RankedCorpusItemsInstance
from app.models.corpus_recommendation_model import CorpusRecommendationModel
from app.models.topic import TopicModel
from app.models.slate import SlateModel
from app.models.slate_lineup import SlateLineupModel
from app.graphql.topic import Topic
from app.graphql.slate import Slate
from app.graphql.slate_lineup import SlateLineup


class Query(ObjectType):
    list_topics = List(Topic)

    get_slate = Field(Slate, slate_id=String(required=True, description="Slate id to get a specific slate"),
                      recommendation_count=Int(default_value=10,
                                               description="Number of recommendations to return, defaults to 10"))

    setup_moment_slate = Field(
        CorpusSlate,
    )

    get_ranked_corpus_slate = Field(RankedCorpusSlate, slate_id=String(required=True, description="A ranked list of recommendation items"))

    list_slates = Field(List(Slate), recommendation_count=Int(default_value=0,
                                                              description="Number of recommendations to return, defaults to 0"))
    get_slate_lineup = Field(SlateLineup, slate_lineup_id=String(required=True,
                                                                 description="SlateLineup id to get a specific slate lineup"),
                             slate_count=Int(default_value=8, description="Number of slates to return, defaults to 8"),
                             recommendation_count=Int(default_value=10,
                                                      description="Maximum number of recommendations to return, defaults to 10"))

    async def resolve_list_topics(self, info) -> [TopicModel]:
        return await TopicModel.get_all()

    async def resolve_get_slate(self, info, slate_id: str, recommendation_count: int = None) -> SlateModel:
        return await SlateModel.get_slate(slate_id=slate_id, user_id=info.context.get('user_id'),
                                          recommendation_count=recommendation_count)

    async def resolve_get_ranked_corpus_slate(self, info, slate_id: str) -> RankedCorpusSlateInstance:
        return await Dispatch(
            api_client=CurationAPIClient(),
            slate_provider=SlateProvider(),
            metrics_client=MetricsClient(
                firefox_newtab_metrics_factory=FirefoxNewTabMetricsFactory()
            )
        ).get_ranked_corpus_slate(
            slate_id=slate_id,
            user_id=info.context.get('user_id')
        )

    async def resolve_list_slates(self, info, recommendation_count: int) -> [SlateModel]:
        return await SlateModel.get_all(user_id=info.context.get('user_id'), recommendation_count=recommendation_count)

    async def resolve_get_slate_lineup(self, info, slate_lineup_id: str, recommendation_count: int = 10,
                                       slate_count: int = 8) -> SlateLineupModel:
        return await SlateLineupModel.get_slate_lineup_with_fallback(slate_lineup_id=slate_lineup_id,
                                                                     user_id=info.context.get('user_id'),
                                                                     recommendation_count=recommendation_count,
                                                                     slate_count=slate_count)

    async def resolve_setup_moment_slate(self, info) -> CorpusSlate:
        return CorpusSlate(
            id='2d6bd5a3-fbd5-454c-9eac-cd39780b18fc',
            headline='Save an article you find interesting',
            subheadline='Save one article',
            recommendations=[
                CorpusRecommendationModel(
                    id='ca42bad7-6346-457b-b23b-ef583a3d3f5c',
                    corpusItem=CorpusItemModel(id='b809c66c-4f8b-4e56-a9d4-67bb6f601a5b'),
                ),
                CorpusRecommendationModel(
                    id='ca42bad7-6346-457b-b23b-ef583a3d3f5c',
                    corpusItem=CorpusItemModel(id='69e9c46a-6859-4e77-a6c9-aa49ba5825bb'),
                ),
                CorpusRecommendationModel(
                    id='ca42bad7-6346-457b-b23b-ef583a3d3f5c',
                    corpusItem=CorpusItemModel(id='a43317f0-44c1-4ae8-ad14-e9e792a5ade7'),
                ),
            ],
        )

##
# Graphene requires that you define your schema programmatically.
# Looks like Graphene 3 will support loading from a .graphql file.
# For now this file should stay in sync with *.graphql
##
schema = build_schema(query=Query)
