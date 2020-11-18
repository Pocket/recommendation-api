import uvicorn
import sentry_sdk
from app.config import sentry as sentry_config

from fastapi import FastAPI, Request
from starlette.graphql import GraphQLApp
from app.graphql.graphql import schema
from graphql.execution.executors.asyncio import AsyncioExecutor

sentry_sdk.init(
    dsn=sentry_config['dsn'],
    release=sentry_config['release'],
    environment=sentry_config['environment'],
    traces_sample_rate=0.1
)

app = FastAPI()

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
