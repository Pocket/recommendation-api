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

# Standard asyncio X-Ray configuration, customise as you choose
xray_recorder.configure(context=AsyncContext(), service=service.get('domain'))


app = FastAPI()
app.add_middleware(BaseHTTPMiddleware, dispatch=xray_middleware)
app.add_middleware(SentryAsgiMiddleware)

# Add our GraphQL route to the main url
app.add_route("/", GraphQLApp(schema=schema,
                              executor_class=AsyncioExecutor))


@app.get("/health-check")
async def read_root():
    return {"Hello": "World"}


# Middleware for FastAPI to grab http exceptions
# https://medium.com/@PhilippeGirard5/integrate-sentry-to-fastapi-7250603c070f
@app.middleware("http")
async def sentry_exception(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        with sentry_sdk.push_scope() as scope:
            scope.set_context("request", request)
            scope.set_user({
                "ip_address": request.client.host,
            })
            sentry_sdk.capture_exception(e)
        raise e


if __name__ == "__main__":
    # This runs uvicorn in a local development environment.
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
