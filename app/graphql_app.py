from starlette.graphql import GraphQLApp
from starlette.concurrency import run_in_threadpool
import sentry_sdk



class GraphQLSentryMiddleware(object):
    def resolve(self, next, root, info, **args):
        try:
            return next(root, info, **args)
        except Exception as e:
            with sentry_sdk.push_scope() as scope:
                scope.set_context("info", info)
                sentry_sdk.capture_exception(e)
            raise e


class GraphQLAppWithMiddleware(GraphQLApp):

    """
    Copied from starlette.graphql
    """
    async def execute(  # type: ignore
        self, query, variables=None, context=None, operation_name=None
    ):
        if self.is_async:
            return await self.schema.execute(
                query,
                variables=variables,
                operation_name=operation_name,
                executor=self.executor,
                return_promise=True,
                context=context,
                middleware=[GraphQLSentryMiddleware()]
            )
        else:
            return await run_in_threadpool(
                self.schema.execute,
                query,
                variables=variables,
                operation_name=operation_name,
                context=context,
            )
