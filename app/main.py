import uvicorn
import sentry_sdk

from aws_xray_sdk.core import xray_recorder
from fastapi import FastAPI, Response, status
from graphql.execution.executors.asyncio import AsyncioExecutor
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from xraysink.asgi.middleware import xray_middleware
from xraysink.context import AsyncContext

from app.config import ENV, ENV_PROD, service, sentry as sentry_config
from app.graphql.graphql import schema
from app.graphql_app import GraphQLAppWithMiddleware, GraphQLSentryMiddleware
from app.models.candidate_set import CandidateSetModel
from app.models.layout_experiment import LayoutExperimentModel
from app.models.layout_config import LayoutConfigModel
from app.models.slate_config import SlateConfigModel
from app.startup_validation import get_app_status, set_app_status, AppStatus


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
async def read_root(response: Response):
    if get_app_status() != AppStatus.SUCCESS:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE

    return {"status": get_app_status().name}


@app.on_event("startup")
async def load_slate_configs():
    # parse json into objects
    slate_configs = SlateConfigModel.load_slate_configs()
    SlateConfigModel.SLATE_CONFIGS_BY_ID = {s.id: s for s in slate_configs}
    layout_configs = LayoutConfigModel.load_layout_configs()
    LayoutConfigModel.LAYOUT_CONFIGS_BY_ID = {lc.id: lc for lc in layout_configs}

    # if we're in prod, ensure candidate sets exist in the db
    if True or ENV == ENV_PROD:
        # wow i do not love this nested loop soup, BUT it does give us nice full context for the error message
        for slate_config in slate_configs:
            for experiment in slate_config.experiments:
                for cs in experiment.candidate_sets:
                    if not await CandidateSetModel.verify_candidate_set(cs):
                        set_app_status(AppStatus.FAILED)
                        raise ValueError(f'candidate set {slate_config.id}|{experiment.description}|{cs} was not found'
                                         ' in the database - application start failed')

        for layout_config in layout_configs:
            for experiment in layout_config.experiments:
                for slate in experiment.slates:
                    if not LayoutExperimentModel.slate_id_exists(slate):
                        set_app_status(AppStatus.FAILED)
                        raise ValueError(f'slate {layout_config.id}|{experiment.description}|{slate} was not found'
                                         f' - application start failed')

    set_app_status(AppStatus.FAILED)


if __name__ == "__main__":
    # This runs uvicorn in a local development environment.
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
