# Adapted from https://github.com/getsentry/sentry-python/blob/master/sentry_sdk/integrations/fastapi.py
# This integration differs only slightly from the FastApiIntegration:
# - event_processor() sets the Sentry transaction name to be the GraphQL operationName
# - only enable if graphql can be imported
import asyncio

from sentry_sdk.hub import Hub
from sentry_sdk.integrations import DidNotEnable

from typing import Any, Callable, Dict
from sentry_sdk.scope import Scope
from sentry_sdk.tracing import TRANSACTION_SOURCE_COMPONENT

try:
    from sentry_sdk.integrations.starlette import (
        StarletteIntegration,
        StarletteRequestExtractor,
    )
except DidNotEnable:
    raise DidNotEnable("Starlette is not installed")

try:
    import fastapi  # type: ignore
except ImportError:
    raise DidNotEnable("FastAPI is not installed")

try:
    import graphql  # type: ignore
except ImportError:
    raise DidNotEnable("graphql-core is not installed")


class GraphqlIntegration(StarletteIntegration):
    identifier = "graphql"

    @staticmethod
    def setup_once():
        # type: () -> None
        patch_get_request_handler()


def patch_get_request_handler():
    # type: () -> None
    old_get_request_handler = fastapi.routing.get_request_handler

    def _sentry_get_request_handler(*args, **kwargs):
        # type: (*Any, **Any) -> Any
        dependant = kwargs.get("dependant")
        if (
            dependant
            and dependant.call is not None
            and not asyncio.iscoroutinefunction(dependant.call)
        ):
            old_call = dependant.call

            def _sentry_call(*args, **kwargs):
                # type: (*Any, **Any) -> Any
                hub = Hub.current
                with hub.configure_scope() as sentry_scope:
                    if sentry_scope.profile is not None:
                        sentry_scope.profile.update_active_thread_id()
                    return old_call(*args, **kwargs)

            dependant.call = _sentry_call

        old_app = old_get_request_handler(*args, **kwargs)

        async def _sentry_app(*args, **kwargs):
            # type: (*Any, **Any) -> Any
            hub = Hub.current
            integration = hub.get_integration(GraphqlIntegration)
            if integration is None:
                return await old_app(*args, **kwargs)

            with hub.configure_scope() as sentry_scope:
                request = args[0]
                extractor = StarletteRequestExtractor(request)
                info = await extractor.extract_request_info()

                def _make_request_event_processor(req, integration):
                    # type: (Any, Any) -> Callable[[Dict[str, Any], Dict[str, Any]], Dict[str, Any]]
                    def event_processor(event, hint):
                        # type: (Dict[str, Any], Dict[str, Any]) -> Dict[str, Any]
                        if info:
                            if "data" in info:
                                data = info["data"]
                                if "operationName" in data:
                                    event["transaction"] = data["operationName"]
                                    event["transaction_info"] = {"source": TRANSACTION_SOURCE_COMPONENT}

                        return event

                    return event_processor

                sentry_scope._name = GraphqlIntegration.identifier
                sentry_scope.add_event_processor(
                    _make_request_event_processor(request, integration)
                )

            return await old_app(*args, **kwargs)

        return _sentry_app

    fastapi.routing.get_request_handler = _sentry_get_request_handler
