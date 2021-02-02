import uvicorn
import sentry_sdk
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from app.config import sentry as sentry_config

from fastapi import FastAPI, Request
from starlette.graphql import GraphQLApp
from app.graphql.graphql import schema
from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.middleware.base import BaseHTTPMiddleware
from aws_xray_sdk.core import xray_recorder
from xraysink.context import AsyncContext
from xraysink.asgi.middleware import xray_middleware
from app.config import service

sentry_sdk.init(
    dsn=sentry_config['dsn'],
    release=sentry_config['release'],
    environment=sentry_config['environment'],
    traces_sample_rate=0.1
)
sentry_sdk.utils.MAX_STRING_LENGTH = 8192  # undocumented truncation length as of v0.12.2

# Standard asyncio X-Ray configuration, customise as you choose
#xray_recorder.configure(context=AsyncContext(), service=service.get('domain'))


app = FastAPI()
app.add_middleware(SentryAsgiMiddleware)
#app.add_middleware(BaseHTTPMiddleware, dispatch=xray_middleware)

# Add our GraphQL route to the main url
app.add_route("/", GraphQLApp(schema=schema,
                              executor_class=AsyncioExecutor))


@app.get("/health-check")
async def read_root():
    return {"Hello": "World"}


@app.get("/divide-by-zero")
async def dummy_error():
    return {"Test": 1/0}


if __name__ == "__main__":
    # This runs uvicorn in a local development environment.
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
