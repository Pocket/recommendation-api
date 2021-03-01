from graphene import ObjectType, String, Field, List, Int
from graphene_federation import build_schema

from app.models.topic import TopicModel
from app.models.topic_recommendations import TopicRecommendationsModel
from app.models.slate import SlateModel
from app.models.layout import LayoutModel
from app.graphql.topic import Topic
from app.graphql.topic_recommendations import TopicRecommendations
from app.graphql.slate import Slate
from app.graphql.layout import Layout


class Query(ObjectType):
    get_topic_recommendations = Field(TopicRecommendations, slug=String(required=True, description="Topic slug to get "
                                                                                                   "recommendations "
                                                                                                   "for"),
                                      algorithmic_count=Int(default_value=20, description="Number of algorithmic "
                                                                                          "results to return"),
                                      curated_count=Int(default_value=5, description="Number of curated "
                                                                                     "results to return"))
    list_topics = List(Topic)
    get_slate = Field(Slate, slate_id=String(required=True, description="Slate id to get a specific slate"),
                      recommendation_count=Int(default_value=None,
                                               description="Number of recommendations to return, defaults to all"))
    list_slates = Field(List(Slate), recommendation_count=Int(default_value=0,
                                                              description="Number of recommendations to return, defaults to 0"))
    get_layout = Field(Layout, layout_id=String(required=True, description="Layout id to get a specific layout"),
                       slate_count=Int(default_value=None, description="Number of slates to return, defaults to all"),
                       recommendation_count=Int(default_value=None,
                                                description="Number of recommendations to return, defaults to all"))

    async def resolve_get_topic_recommendations(self, info, slug: str, algorithmic_count: int,
                                                curated_count: int) -> TopicRecommendationsModel:
        return await TopicRecommendationsModel.get_recommendations(slug=slug, algorithmic_count=algorithmic_count,
                                                                   curated_count=curated_count)

    async def resolve_list_topics(self, info) -> [TopicModel]:
        return await TopicModel.get_all()

    async def resolve_get_slate(self, info, slate_id: str, recommendation_count: int = None) -> SlateModel:
        return await SlateModel.get_slate(slate_id=slate_id, user_id=info.context.get('user_id'),
                                          recommendation_count=recommendation_count)

    async def resolve_list_slates(self, info, recommendation_count: int) -> [SlateModel]:
        return await SlateModel.get_all(recommendation_count=recommendation_count)

    async def resolve_get_layout(self, info, layout_id: str, recommendation_count: int = None,
                                 slate_count: int = None) -> LayoutModel:
        return await LayoutModel.get_layout(layout_id=layout_id, user_id=info.context.get('user_id'),
                                            recommendation_count=recommendation_count,
                                            slate_count=slate_count)


##
# Graphene requires that you define your schema programmatically.
# Looks like Graphene 3 will support loading from a .graphql file.
# For now this file should stay in sync with *.graphql
##
schema = build_schema(query=Query)
