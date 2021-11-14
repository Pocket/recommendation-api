from typing import Annotated, List, Optional

import strawberry
import sentry_sdk
from graphql import GraphQLError
from strawberry.types import Info, ExecutionContext

from app.graphql.annotations import recommendation_count_annotation, slate_count_annotation
from app.models.topic import TopicModel
from app.models.slate import SlateModel
from app.models.slate_lineup import SlateLineupModel
# Import order of these Strawberry GraphQL models is important. Dependant models need to be important first.
from app.graphql.topic import Topic
from app.graphql.item import Item
from app.graphql.recommendation import Recommendation
from app.graphql.slate import Slate
from app.graphql.slate_lineup import SlateLineup


@strawberry.type
class Query:

    @strawberry.field(
        description="List all topics",
        deprecation_reason="RecommendationAPI no longer keeps an up-to-date list of topics",
    )
    async def listTopics(self) -> List['Topic']:
        return await TopicModel.get_all()

    @strawberry.field(description="Get a single slate")
    async def getSlate(
            self,
            info: Info,
            slate_id: Annotated[str, strawberry.argument(description="Slate id to get a specific slate")],
            recommendation_count: recommendation_count_annotation(default=10) = 10,
    ) -> 'Slate':
        return Slate.from_pydantic(await SlateModel.get_slate(
            slate_id=slate_id,
            user_id=info.context.get('user_id'),
            recommendation_count=recommendation_count,
        ))

    @strawberry.field(description="List all slates")
    async def listSlates(
            self,
            info: Info,
            recommendation_count: recommendation_count_annotation(default=0) = 0,
    ) -> List['Slate']:
        slate_models = await SlateModel.get_all(
            user_id=info.context.get('user_id'),
            recommendation_count=recommendation_count,
        )
        return [Slate.from_pydantic(s) for s in slate_models]


    @strawberry.field(description="Get a lineup of slates")
    async def getSlateLineup(
            self,
            info: Info,
            slate_lineup_id: Annotated[str, strawberry.argument(description="SlateLineup id to get a specific lineup")],
            recommendation_count: recommendation_count_annotation(default=10) = 10,
            slate_count: slate_count_annotation(default=8) = 8,
    ) -> 'SlateLineup':
        return SlateLineup.from_pydantic(await SlateLineupModel.get_slate_lineup_with_fallback(
            slate_lineup_id=slate_lineup_id,
            user_id=info.context.get('user_id'),
            recommendation_count=recommendation_count,
            slate_count=slate_count,
        ))


class SchemaWithSentryExceptionHandling(strawberry.Schema):
    """
    Modify the Strawberry schema to send exceptions to Sentry.
    @see https://strawberry.rocks/docs/types/schema#handling-execution-errors
    """
    def process_errors(
        self,
        errors: List[GraphQLError],
        execution_context: Optional[ExecutionContext] = None,
    ) -> None:
        for error in errors:
            # A GraphQLError wraps the underlying error so we have to access it
            # through the `original_error` property
            # https://graphql-core-3.readthedocs.io/en/latest/modules/error.html#graphql.error.GraphQLError
            # If original_error is not available, we'll fall back to the GraphQL exception.
            exception = error.original_error or error
            sentry_sdk.capture_exception(exception)
        # Call method on base class.
        super().process_errors(errors=errors, execution_context=execution_context)
