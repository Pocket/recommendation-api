import sentry_sdk

from starlette.concurrency import run_in_threadpool
from starlette.graphql import GraphQLApp


async def capture_and_reraise(e):
    sentry_sdk.capture_exception(e)
    raise e


class GraphQLSentryMiddleware(object):
    """
    Middleware for Sentry - used in conjunction with GraphQLAppWithMiddleware (below) in `main.py`.
    """
    def resolve(self, next, root, info, **args):
        promise = next(root, info, **args)
        # Capture exceptions to Sentry and re-raise such that GraphQL can return a proper error message in the response
        return promise.then(did_reject=capture_and_reraise)


# Starlette has an open PR to support middleware, but it's not merged in as of today:
# https://github.com/encode/starlette/pull/1044
class GraphQLAppWithMiddleware(GraphQLApp):
    """
    Allows us to add middleware to a graphene app.
    """
    def __init__(self, *args, **kwargs):
        self._middleware = kwargs.pop('middleware', None)
        super().__init__(*args, **kwargs)

    """
    Copied from starlette.graphql, with the only modification being to add middleware.
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
                middleware=self._middleware
            )
        else:
            return await run_in_threadpool(
                self.schema.execute,
                query,
                variables=variables,
                operation_name=operation_name,
                context=context,
            )
