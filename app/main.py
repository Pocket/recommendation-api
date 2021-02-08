import uvicorn
import sentry_sdk

from aws_xray_sdk.core import xray_recorder
from fastapi import FastAPI, Request
from graphql.execution.executors.asyncio import AsyncioExecutor
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from xraysink.asgi.middleware import xray_middleware
from xraysink.context import AsyncContext

from app.config import ENV, ENV_PROD, service, sentry as sentry_config
from app.graphql.graphql import schema
from app.graphql_app import GraphQLAppWithMiddleware, GraphQLSentryMiddleware
from app.models.experiment import Experiment
from app.models.slateconfig import SlateConfigModel


sentry_sdk.init(
    dsn=sentry_config['dsn'],
    release=sentry_config['release'],
    environment=sentry_config['environment'],
    traces_sample_rate=0.1
)
# Ignore graphql.execution.utils to prevent duplicate Sentry events. Exceptions are handled by GraphQLSentryMiddleware.
sentry_sdk.integrations.logging.ignore_logger("graphql.execution.utils")

# Standard asyncio X-Ray configuration, customise as you choose
xray_recorder.configure(context=AsyncContext(), service=service.get('domain'))

app = FastAPI()
app.add_middleware(BaseHTTPMiddleware, dispatch=xray_middleware)
app.add_middleware(SentryAsgiMiddleware)

# Add our GraphQL route to the main url
app.add_route("/", GraphQLAppWithMiddleware(
    schema=schema,
    executor_class=AsyncioExecutor,
    middleware=[GraphQLSentryMiddleware()]))


@app.get("/health-check")
async def read_root():
    return {"Hello": "World"}


@app.on_event("startup")
async def load_slate_configs():
    # parse json into objects
    SlateConfigModel.SLATE_CONFIGS = SlateConfigModel.load_slateconfigs()

    # if we're in prod, ensure candidate sets exist in the db
    if ENV == ENV_PROD:
        # wow i do not love this nested loop soup, BUT it does give us nice full context for the error message
        for slateconfig in SlateConfigModel.SLATE_CONFIGS:
            for experiment in slateconfig.experiments:
                for cs in experiment.candidate_sets:
                    # TODO: this check is currently stubbed to return True
                    # https://getpocket.atlassian.net/browse/BACK-598 will implement
                    if not Experiment.candidate_set_is_valid(cs):
                        raise ValueError(f'{slateconfig.id}|{experiment.description}|{cs} was not found in the database - '
                                         'application start failed')


if __name__ == "__main__":
    # This runs uvicorn in a local development environment.
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
