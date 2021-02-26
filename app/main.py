import logging

import uvicorn
import sentry_sdk

from aws_xray_sdk.core import xray_recorder
from fastapi import FastAPI, Response, status
from graphql.execution.executors.asyncio import AsyncioExecutor
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from xraysink.asgi.middleware import xray_middleware
from xraysink.context import AsyncContext

from app.config import ENV, ENV_PROD, ENV_DEV, service, sentry as sentry_config
from app.graphql.graphql import schema
from app.graphql.user_middleware import UserMiddleware
from app.graphql_app import GraphQLAppWithMiddleware, GraphQLSentryMiddleware
from app.models.candidate_set import CandidateSetModel
from app.models.layout_experiment import LayoutExperimentModel
from app.models.layout_config import LayoutConfigModel
from app.models.slate_config import SlateConfigModel
from app.health_status import get_health_status, set_health_status, HealthStatus


sentry_sdk.init(
    dsn=sentry_config['dsn'],
    release=sentry_config['release'],
    environment=sentry_config['environment'],
    traces_sample_rate=0.1
)
# Ignore graphql.execution.utils to prevent duplicate Sentry events. Exceptions are handled by GraphQLSentryMiddleware.
sentry_sdk.integrations.logging.ignore_logger("graphql.execution.utils")

# Standard asyncio X-Ray configuration, customise as you choose
xray_recorder.configure(context=AsyncContext(), service=service.get('domain'), plugins=['ecsplugin'])

app = FastAPI()
app.add_middleware(BaseHTTPMiddleware, dispatch=xray_middleware)
app.add_middleware(SentryAsgiMiddleware)

# Add our GraphQL route to the main url
app.add_route("/", GraphQLAppWithMiddleware(
    schema=schema,
    executor_class=AsyncioExecutor,
    middleware=[GraphQLSentryMiddleware(), UserMiddleware()]))


@app.get("/health-check")
async def read_root(response: Response):
    if get_health_status() != HealthStatus.HEALTHY:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE

    return {"status": get_health_status().name}


class MissingSlateException(ValueError):
    """
    Raise when a slate is referenced in a layout, but does not exist in slate_configs.json.
    This allows Sentry to group these exceptions, and trigger an alarm based on them.
    """
    pass


class MissingCandidateSetException(ValueError):
    """
    Raise when a candidate set is referenced in a slate, but does not exist in the database.
    This allows Sentry to group these exceptions, and trigger an alarm based on them.
    """
    pass


@app.on_event("startup")
async def load_slate_configs():
    # parse json into objects
    slate_configs = SlateConfigModel.load_slate_configs()
    SlateConfigModel.SLATE_CONFIGS_BY_ID = {s.id: s for s in slate_configs}
    layout_configs = LayoutConfigModel.load_layout_configs()
    LayoutConfigModel.LAYOUT_CONFIGS_BY_ID = {lc.id: lc for lc in layout_configs}

    # Validate layout and slate configs on prod and dev, not locally.
    if ENV in {ENV_PROD, ENV_DEV}:
        # wow i do not love this nested loop soup, BUT it does give us nice full context for the error message
        for slate_config in slate_configs:
            for experiment in slate_config.experiments:
                for cs in experiment.candidate_sets:
                    logging.info(f"Validating candidate set {cs}")
                    if not await CandidateSetModel.verify_candidate_set(cs):
                        # Send event to Sentry, but don't raise it, because missing candidate sets should not
                        # block successfully starting the application.
                        message = f'candidate set {slate_config.id}|{experiment.description}|{cs} was not found.'
                        logging.error(message)
                        sentry_sdk.capture_exception(MissingCandidateSetException(message))

        for layout_config in layout_configs:
            for experiment in layout_config.experiments:
                for slate in experiment.slates:
                    logging.info(f"Validating slate id {slate}")
                    if not LayoutExperimentModel.slate_id_exists(slate):
                        set_health_status(HealthStatus.UNHEALTHY)
                        raise MissingSlateException(
                            f'slate {layout_config.id}|{experiment.description}|{slate} was not found'
                            f'in json/slate_configs.json - application start failed')

    set_health_status(HealthStatus.HEALTHY)


if __name__ == "__main__":
    # This runs uvicorn in a local development environment.
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
