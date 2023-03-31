# Based on botocore instrumentation:
# https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation/opentelemetry-instrumentation-botocore
# TODO: Open a PR to have this code merged into the above repo.
#
# Copyright The OpenTelemetry Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Instrument `aiobotocore`_ to trace asyncio service requests.

There are two options for instrumenting code. The first option is to use the
``opentelemetry-instrument`` executable which will automatically
instrument your Botocore client. The second is to programmatically enable
instrumentation via the following code:

.. _Botocore: https://pypi.org/project/botocore/

Usage
-----

.. code:: python

    from opentelemetry.instrumentation.aiobotocore import AioAiobotocoreInstrumentor
    import aiobotocore


    # Instrument aiobotocore
    AioAiobotocoreInstrumentor().instrument()

    # This will create a span with aiobotocore-specific attributes
    session = aiobotocore.session.get_session()
    async with session.create_client('s3', region_name='us-west-2',
                                   aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                                   aws_access_key_id=AWS_ACCESS_KEY_ID) as client:
        # list s3 objects using paginator
        paginator = client.get_paginator('list_objects')
        async for result in paginator.paginate(Bucket=bucket, Prefix=folder):
            for c in result.get('Contents', []):
                print(c)

API
---

The `instrument` method accepts the following keyword args:

tracer_provider (TracerProvider) - an optional tracer provider
request_hook (Callable) - a function with extra user-defined logic to be performed before performing the request
this function signature is:  async def request_hook(span: Span, service_name: str, operation_name: str, api_params: dict) -> None
response_hook (Callable) - a function with extra user-defined logic to be performed after performing the request
this function signature is:  async def request_hook(span: Span, service_name: str, operation_name: str, result: dict) -> None

for example:

.. code: python

    from opentelemetry.instrumentation.aiobotocore import AiobotocoreInstrumentor
    import aiobotocore

    # Instrument Botocore with hooks
    AiobotocoreInstrumentor().instrument(request_hook=request_hook, response_hook=response_hook)

    # This will create a span with aiobotocore-specific attributes
    session = aiobotocore.session.get_session()
    async with session.create_client('s3', region_name='us-west-2',
                                   aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                                   aws_access_key_id=AWS_ACCESS_KEY_ID) as client:
        # list s3 objects using paginator
        paginator = client.get_paginator('list_objects')
        async for result in paginator.paginate(Bucket=bucket, Prefix=folder):
            for c in result.get('Contents', []):
                print(c)
"""

import logging
from typing import Any, Callable, Collection, Dict, Optional, Tuple

from aiobotocore.client import AioBaseClient
from aiobotocore.endpoint import AioEndpoint
from botocore.exceptions import ClientError
from wrapt import wrap_function_wrapper

from opentelemetry import context as context_api

# FIXME: fix the importing of this private attribute when the location of the _SUPPRESS_HTTP_INSTRUMENTATION_KEY is defined.
from opentelemetry.context import _SUPPRESS_HTTP_INSTRUMENTATION_KEY

from app.instrumentation.aiobotocore.extensions import _find_extension
from app.instrumentation.aiobotocore.extensions.types import _AwsSdkCallContext, _AwsSdkExtension
from app.instrumentation.aiobotocore.package import _instruments
from app.instrumentation.aiobotocore.version import __version__
from opentelemetry.instrumentation.instrumentor import BaseInstrumentor
from opentelemetry.instrumentation.utils import (
    _SUPPRESS_INSTRUMENTATION_KEY,
    unwrap,
)
from opentelemetry.propagate import inject
from opentelemetry.semconv.trace import SpanAttributes
from opentelemetry.trace import get_tracer
from opentelemetry.trace.span import Span

logger = logging.getLogger(__name__)


# pylint: disable=unused-argument
def _patched_endpoint_prepare_request(wrapped, instance, args, kwargs):
    request = args[0]
    headers = request.headers
    inject(headers)
    return wrapped(*args, **kwargs)


class AiobotocoreInstrumentor(BaseInstrumentor):
    """An instrumentor for Botocore.

    See `BaseInstrumentor`
    """

    def __init__(self):
        super().__init__()
        self.request_hook = None
        self.response_hook = None

    def instrumentation_dependencies(self) -> Collection[str]:
        return _instruments

    def _instrument(self, **kwargs):
        # pylint: disable=attribute-defined-outside-init
        self._tracer = get_tracer(
            __name__, __version__, kwargs.get("tracer_provider")
        )

        self.request_hook = kwargs.get("request_hook")
        self.response_hook = kwargs.get("response_hook")

        wrap_function_wrapper(
            AioBaseClient,
            "_make_api_call",
            self._patched_api_call,
        )

        wrap_function_wrapper(
            AioEndpoint,
            "prepare_request",
            _patched_endpoint_prepare_request,
        )

    def _uninstrument(self, **kwargs):
        unwrap(AioBaseClient, "_make_api_call")
        unwrap(AioEndpoint, "prepare_request")

    # pylint: disable=too-many-branches
    async def _patched_api_call(self, original_func, instance, args, kwargs):
        if context_api.get_value(_SUPPRESS_INSTRUMENTATION_KEY):
            return await original_func(*args, **kwargs)

        call_context = _determine_call_context(instance, args)
        if call_context is None:
            return await original_func(*args, **kwargs)

        extension = _find_extension(call_context)
        if not extension.should_trace_service_call():
            return await original_func(*args, **kwargs)

        attributes = {
            SpanAttributes.RPC_SYSTEM: "aws-api",
            # X-RAY uses the service for the segment name if it is not empty:
            # https://aws-otel.github.io/docs/getting-started/x-ray#otel-span-attributes-translation
            SpanAttributes.RPC_SERVICE: f'{call_context.service_id}.{call_context.operation}',
            SpanAttributes.RPC_METHOD: call_context.operation,
            # TODO: update when semantic conventions exist
            "aws.region": call_context.region,
        }

        _safe_invoke(extension.extract_attributes, attributes)

        with self._tracer.start_as_current_span(
            call_context.span_name,
            kind=call_context.span_kind,
            attributes=attributes,
        ) as span:
            _safe_invoke(extension.before_service_call, span)
            self._call_request_hook(span, call_context)

            token = context_api.attach(
                context_api.set_value(_SUPPRESS_HTTP_INSTRUMENTATION_KEY, True)
            )

            result = None
            try:
                result = await original_func(*args, **kwargs)
            except ClientError as error:
                result = getattr(error, "response", None)
                _apply_response_attributes(span, result)
                _safe_invoke(extension.on_error, span, error)
                raise
            else:
                _apply_response_attributes(span, result)
                _safe_invoke(extension.on_success, span, result)
            finally:
                context_api.detach(token)
                _safe_invoke(extension.after_service_call)

                self._call_response_hook(span, call_context, result)

            return result

    def _call_request_hook(self, span: Span, call_context: _AwsSdkCallContext):
        if not callable(self.request_hook):
            return
        self.request_hook(
            span,
            call_context.service,
            call_context.operation,
            call_context.params,
        )

    def _call_response_hook(
        self, span: Span, call_context: _AwsSdkCallContext, result
    ):
        if not callable(self.response_hook):
            return
        self.response_hook(
            span, call_context.service, call_context.operation, result
        )


def _apply_response_attributes(span: Span, result):
    if result is None or not span.is_recording():
        return

    metadata = result.get("ResponseMetadata")
    if metadata is None:
        return

    request_id = metadata.get("RequestId")
    if request_id is None:
        headers = metadata.get("HTTPHeaders")
        if headers is not None:
            request_id = (
                headers.get("x-amzn-RequestId")
                or headers.get("x-amz-request-id")
                or headers.get("x-amz-id-2")
            )
    if request_id:
        # TODO: update when semantic conventions exist
        span.set_attribute("aws.request_id", request_id)

    retry_attempts = metadata.get("RetryAttempts")
    if retry_attempts is not None:
        # TODO: update when semantic conventions exists
        span.set_attribute("retry_attempts", retry_attempts)

    status_code = metadata.get("HTTPStatusCode")
    if status_code is not None:
        span.set_attribute(SpanAttributes.HTTP_STATUS_CODE, status_code)


def _determine_call_context(
    client: AioBaseClient, args: Tuple[str, Dict[str, Any]]
) -> Optional[_AwsSdkCallContext]:
    try:
        call_context = _AwsSdkCallContext(client, args)

        logger.debug(
            "AWS SDK invocation: %s %s",
            call_context.service,
            call_context.operation,
        )

        return call_context
    except Exception as ex:  # pylint:disable=broad-except
        # this shouldn't happen actually unless internals of botocore changed and
        # extracting essential attributes ('service' and 'operation') failed.
        logger.error("Error when initializing call context", exc_info=ex)
        return None


def _safe_invoke(function: Callable, *args):
    function_name = "<unknown>"
    try:
        function_name = function.__name__
        function(*args)
    except Exception as ex:  # pylint:disable=broad-except
        logger.error(
            "Error when invoking function '%s'", function_name, exc_info=ex
        )
