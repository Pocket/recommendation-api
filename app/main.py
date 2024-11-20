import logging

import sentry_sdk
import uvicorn
from fastapi import FastAPI, Request, Response, status
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.aiohttp_client import AioHttpClientInstrumentor
from opentelemetry.sdk.extension.aws.resource import AwsEcsResourceDetector
from opentelemetry.sdk.extension.aws.trace import AwsXRayIdGenerator
from opentelemetry.sdk.resources import Resource, get_aggregated_resources
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.trace.sampling import TraceIdRatioBased
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from strawberry.fastapi import GraphQLRouter

from app.cache import initialize_caches
from app.config import ENV, ENV_PROD, sentry as sentry_config, log_level, otel_daemon_address
from app.graphql.graphql_router import schema
from app.instrumentation.aiobotocore import AiobotocoreInstrumentor
from app.models.candidate_set import candidate_set_factory
from app.models.slate_config import SlateConfigModel
from app.models.slate_lineup_config import SlateLineupConfigModel, validate_unique_guids
from app.models.slate_lineup_experiment import SlateLineupExperimentModel
from app.singletons import DiContainer

logging.getLogger().setLevel(log_level)
logger = logging.getLogger(__name__)

sentry_sdk.init(
    dsn=sentry_config['dsn'],
    release=sentry_config['release'],
    environment=sentry_config['environment']
)
# Ignore graphql.execution.utils to prevent duplicate Sentry events. Exceptions are handled by GraphQLSentryMiddleware.
sentry_sdk.integrations.logging.ignore_logger("graphql.execution.utils")

app = FastAPI()
app.add_middleware(SentryAsgiMiddleware)

# Add our GraphQL route to the main url
graphql_app = GraphQLRouter(schema, path='/')
app.include_router(graphql_app)

# Instrument the app using Open Telemetry
# Sends generated traces in the OTLP format to an ADOT Collector running on port 4317
otlp_exporter = OTLPSpanExporter(
    endpoint=otel_daemon_address,
    insecure=True,  # HTTP is safe to use because we're connecting to a Docker sidecar.
)
# Configures the Global Tracer Provider
trace.set_tracer_provider(TracerProvider(
    sampler=TraceIdRatioBased(0.1),  # Set to 0 to disable tracing
    active_span_processor=BatchSpanProcessor(otlp_exporter),
    id_generator=AwsXRayIdGenerator(),
    resource=get_aggregated_resources(
        initial_resource=Resource(attributes={'service.name': 'RecommendationAPI'}),
        detectors=[AwsEcsResourceDetector()],
    ),
))
FastAPIInstrumentor.instrument_app(app, excluded_urls="/health-check")
AiobotocoreInstrumentor().instrument()
AioHttpClientInstrumentor().instrument()


@app.get("/health-check")
async def read_root(response: Response):
    return {"status": "HEALTHY"}

class MissingSlateException(ValueError):
    """
    Raise when a slate is referenced in a slate_lineup, but does not exist in slate_configs.json.
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
async def initialize_caches_startup_event():
    # aiocache needs to be on the same event loop as FastAPI.
    # Currently initialize_caches() isn't asynchronous, but we put initialize_caches() in a startup event, just in case
    # it will need to be in the future.
    initialize_caches()


@app.on_event("startup")
async def load_slate_configs():
    # parse json into objects
    slate_configs = SlateConfigModel.load_slate_configs()
    SlateConfigModel.SLATE_CONFIGS_BY_ID = {s.id: s for s in slate_configs}
    slate_lineup_configs = SlateLineupConfigModel.load_slate_lineup_configs()
    SlateLineupConfigModel.SLATE_LINEUP_CONFIGS_BY_ID = {lc.id: lc for lc in slate_lineup_configs}

@app.on_event("startup")
async def startup_event():
    DiContainer.init()

@app.post("/remove")
async def remove_event(request: Request, response: Response):
    """
    Handles remove events triggered by EventBridge.
    Logs the event details for debugging or processing.
    """
    try:
        body = await request.json()
        logger.info("Received remove event: %s", body)
        return {"status": "success", "message": "Event logged successfully."}
    except Exception as e:
        logger.error("Error processing remove event: %s", str(e))
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"status": "error", "message": "Failed to process event."}


if __name__ == "__main__":
    # This runs uvicorn in a local development environment.
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
