from typing import List

import strawberry

# from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
# from app.data_providers.corpus.curated_corpus_api_client import CuratedCorpusAPIClient
# from app.data_providers.metrics_client import MetricsClient
# from app.data_providers.slate_provider import SlateProvider
# from app.data_providers.snowplow.config import SnowplowConfig, create_snowplow_tracker
# from app.data_providers.snowplow.snowplow_corpus_slate_tracker import SnowplowCorpusSlateTracker
# from app.data_providers.topic_provider import TopicProvider
# from app.data_providers.user_recommendation_preferences_provider import UserRecommendationPreferencesProvider
# from app.graphql.ranked_corpus_slate import RankedCorpusSlate
# from app.graphql.update_user_recommendation_preferences_mutation import UpdateUserRecommendationPreferences
# from app.graphql.util import get_field_argument
# from app.models.metrics.firefox_new_tab_metrics_factory import FirefoxNewTabMetricsFactory
# from app.models.ranked_corpus_slate_instance import RankedCorpusSlateInstance
# from app.models.corpus_slate_model import CorpusSlateModel
# from app.data_providers.dispatch import RankingDispatch, SetupMomentDispatch
# from app.graphql.corpus_slate import CorpusSlate
# from app.models.topic import TopicModel
# from app.models.slate import SlateModel
# from app.models.slate_lineup import SlateLineupModel
# from app.graphql.topic import Topic
# from app.graphql.slate import Slate
# from app.graphql.slate_lineup import SlateLineup
# from app.graphql.user import User



# class Query(ObjectType):
#     list_topics = List(Topic)
#
#     get_slate = Field(Slate, slate_id=String(required=True, description="Slate id to get a specific slate"),
#                       recommendation_count=Int(default_value=10,
#                                                description="Number of recommendations to return, defaults to 10"))
#
#     setup_moment_slate = Field(
#         CorpusSlate,
#     )
#
#     recommendation_preference_topics = Field(
#         List(Topic),
#     )
#
#     get_ranked_corpus_slate = Field(RankedCorpusSlate, slate_id=String(required=True, description="A ranked list of recommendation items"))
#
#     list_slates = Field(List(Slate), recommendation_count=Int(default_value=0,
#                                                               description="Number of recommendations to return, defaults to 0"))
#     get_slate_lineup = Field(SlateLineup, slate_lineup_id=String(required=True,
#                                                                  description="SlateLineup id to get a specific slate lineup"),
#                              slate_count=Int(default_value=8, description="Number of slates to return, defaults to 8"),
#                              recommendation_count=Int(default_value=10,
#                                                       description="Maximum number of recommendations to return, defaults to 10"))
#
#     async def resolve_list_topics(self, info) -> [TopicModel]:
#         return await TopicProvider(aioboto3_session=aioboto3.Session()).get_all()
#
#     async def resolve_get_slate(self, info, slate_id: str, recommendation_count: int = None) -> SlateModel:
#         return await SlateModel.get_slate(slate_id=slate_id, user_id=info.context.get('user_id'),
#                                           recommendation_count=recommendation_count)
#
#     async def resolve_get_slate_lineup(self, info, slate_lineup_id: str, recommendation_count: int = 10,
#                                        slate_count: int = 8) -> SlateLineupModel:
#         return await SlateLineupModel.get_slate_lineup_with_fallback(slate_lineup_id=slate_lineup_id,
#                                                                      user_id=info.context.get('user_id'),
#                                                                      recommendation_count=recommendation_count,
#                                                                      slate_count=slate_count)
#
#
# class Mutation(ObjectType):
#     update_user_recommendation_preferences = UpdateUserRecommendationPreferences.Field()
#
#
from app.graphql.corpus_slate import CorpusSlate
from app.graphql.resolvers.corpus_slate_resolvers import resolve_setup_moment_slate
from app.graphql.topic import Topic
from app.graphql.update_user_recommendation_preferences_mutation import Mutation
from app.graphql.user import User
from app.graphql.resolvers.topic_resolvers import list_topics, resolve_recommendation_preference_topics


@strawberry.type
class Query:
    setup_moment_slate: CorpusSlate = strawberry.field(
        resolver=resolve_setup_moment_slate,
        description='Get stories during Setup Moment onboarding that are personalized with user preferences provided '
                    'during onboarding.'
    )

    recommendation_preference_topics: List[Topic] = strawberry.field(
        resolver=resolve_recommendation_preference_topics,
        description='List all topics that the user can express a preference for.')

    list_topics: List[Topic] = strawberry.field(
        resolver=list_topics,
        deprecation_reason='`recommendation_preference_topics` gets topics that users can express a preference for.',
        description='List all available topics that we have recommendations for.')


schema = strawberry.federation.Schema(Query, mutation=Mutation, types=[User], enable_federation_2=True)
