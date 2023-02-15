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

import abc
import inspect
import json
from typing import Any, Callable, Dict, List, Optional, Tuple, Union
from urllib.parse import urlparse

from app.instrumentation.aiobotocore.extensions.types import (
    _AttributeMapT,
    _AwsSdkCallContext,
    _AwsSdkExtension,
    _BotoResultT,
)
from opentelemetry.semconv.trace import SpanAttributes
from opentelemetry.trace.span import Span
from opentelemetry.util.types import AttributeValue

_AttributePathT = Union[str, Tuple[str]]


# converter functions


def _conv_val_to_single_attr_tuple(value: str) -> Tuple[str]:
    return None if value is None else (value,)


def _conv_dict_to_key_tuple(value: Dict[str, Any]) -> Optional[Tuple[str]]:
    return tuple(value.keys()) if isinstance(value, Dict) else None


def _conv_list_to_json_list(value: List) -> Optional[List[str]]:
    return (
        [json.dumps(item) for item in value]
        if isinstance(value, List)
        else None
    )


def _conv_val_to_single_json_tuple(value: str) -> Optional[Tuple[str]]:
    return (json.dumps(value),) if value is not None else None


def _conv_dict_to_json_str(value: Dict) -> Optional[str]:
    return json.dumps(value) if isinstance(value, Dict) else None


def _conv_val_to_len(value) -> Optional[int]:
    return len(value) if value is not None else None


################################################################################
# span attribute names
################################################################################
_AWS_SAGEMAKER_FEATURESTORE_TABLE_NAMES = 'aws.sagemaker_featurestore.table_names'
_AWS_SAGEMAKER_FEATURESTORE_RECORD_IDENTIFIERS = 'aws.sagemaker_featurestore.record_identifiers'
_AWS_SAGEMAKER_FEATURESTORE_FEATURE_NAMES = 'aws.sagemaker_featurestore.feature_names'
_AWS_SAGEMAKER_FEATURESTORE_BATCH_IDENTIFIERS = 'aws.sagemaker_featurestore.batch_identifiers'

################################################################################
# common request attributes
################################################################################

_REQ_FEATURE_GROUP_NAME = ('FeatureGroupName', None)

_REQ_RECORD_IDENTIFIER = ('RecordIdentifierValueAsString', None)

_REQ_FEATURE_NAMES = ("FeatureNames", _conv_list_to_json_list)

################################################################################
# FeatureStore operations with enhanced attributes
################################################################################

_AttrSpecT = Tuple[_AttributePathT, Optional[Callable]]


class _FeatureStoreOperation(abc.ABC):
    start_attributes = None  # type: Optional[Dict[str, _AttrSpecT]]
    request_attributes = None  # type: Optional[Dict[str, _AttrSpecT]]
    response_attributes = None  # type: Optional[Dict[str, _AttrSpecT]]

    @classmethod
    @abc.abstractmethod
    def operation_name(cls):
        pass

    @classmethod
    def add_start_attributes(
        cls, call_context: _AwsSdkCallContext, attributes: _AttributeMapT
    ):
        pass

    @classmethod
    def add_response_attributes(
        cls, call_context: _AwsSdkCallContext, span: Span, result: _BotoResultT
    ):
        pass


class _OpBatchGetRecord(_FeatureStoreOperation):
    start_attributes = {
        _AWS_SAGEMAKER_FEATURESTORE_BATCH_IDENTIFIERS: ("Identifiers", _conv_list_to_json_list),
    }
    response_attributes = {
    }

    @classmethod
    def operation_name(cls):
        return "BatchGetRecord"


class _OpDeleteRecord(_FeatureStoreOperation):
    start_attributes = {
        #SpanAttributes.AWS_DYNAMODB_TABLE_NAMES: _REQ_TABLE_NAME,
    }
    response_attributes = {
        #SpanAttributes.AWS_DYNAMODB_CONSUMED_CAPACITY: _RES_CONSUMED_CAP_SINGLE,
        #SpanAttributes.AWS_DYNAMODB_ITEM_COLLECTION_METRICS: _RES_ITEM_COL_METRICS,
    }

    @classmethod
    def operation_name(cls):
        return "DeleteRecord"


class _OpGetRecord(_FeatureStoreOperation):
    start_attributes = {
        _AWS_SAGEMAKER_FEATURESTORE_TABLE_NAMES: _REQ_FEATURE_GROUP_NAME,
        _AWS_SAGEMAKER_FEATURESTORE_RECORD_IDENTIFIERS: _REQ_RECORD_IDENTIFIER,
        _AWS_SAGEMAKER_FEATURESTORE_FEATURE_NAMES: _REQ_FEATURE_NAMES,
    }
    request_attributes = {
        # SpanAttributes.AWS_DYNAMODB_CONSISTENT_READ: _REQ_CONSISTENT_READ,
        # SpanAttributes.AWS_DYNAMODB_PROJECTION: _REQ_PROJECTION,
    }
    response_attributes = {
        # SpanAttributes.AWS_DYNAMODB_CONSUMED_CAPACITY: _RES_CONSUMED_CAP_SINGLE,
    }

    @classmethod
    def operation_name(cls):
        return "GetRecord"


class _OpPutRecord(_FeatureStoreOperation):
    start_attributes = {
        # SpanAttributes.AWS_DYNAMODB_TABLE_NAMES: _REQ_TABLE_NAME
    }
    response_attributes = {
        # SpanAttributes.AWS_DYNAMODB_CONSUMED_CAPACITY: _RES_CONSUMED_CAP_SINGLE,
        # SpanAttributes.AWS_DYNAMODB_ITEM_COLLECTION_METRICS: _RES_ITEM_COL_METRICS,
    }

    @classmethod
    def operation_name(cls):
        return "PutRecord"


################################################################################
# FeatureStore extension
################################################################################

_OPERATION_MAPPING = {
    op.operation_name(): op
    for op in globals().values()
    if inspect.isclass(op)
    and issubclass(op, _FeatureStoreOperation)
    and not inspect.isabstract(op)
}  # type: Dict[str, _FeatureStoreOperation]


class _FeatureStoreExtension(_AwsSdkExtension):
    def __init__(self, call_context: _AwsSdkCallContext):
        super().__init__(call_context)
        self._op = _OPERATION_MAPPING.get(call_context.operation)

    def extract_attributes(self, attributes: _AttributeMapT):
        feature_group_names = self._format_feature_group_names(self._call_context.params)
        attributes[SpanAttributes.RPC_SERVICE] = f'FeatureStore.{self._call_context.operation}: {feature_group_names}'

        attributes[SpanAttributes.DB_OPERATION] = self._call_context.operation
        attributes[SpanAttributes.NET_PEER_NAME] = self._get_peer_name()

        if self._op is None:
            return

        def attr_setter(key: str, value: AttributeValue):
            attributes[key] = value

        self._add_attributes(
            self._call_context.params, self._op.start_attributes, attr_setter
        )

    def _get_peer_name(self) -> str:
        return urlparse(self._call_context.endpoint_url).netloc

    def before_service_call(self, span: Span):
        if not span.is_recording() or self._op is None:
            return

        self._add_attributes(
            self._call_context.params,
            self._op.request_attributes,
            span.set_attribute,
        )

    def on_success(self, span: Span, result: _BotoResultT):
        if not span.is_recording():
            return

        if self._op is None:
            return

        self._add_attributes(
            result, self._op.response_attributes, span.set_attribute
        )

    def _format_feature_group_names(self, provider: Dict[str, Any]):
        if 'FeatureGroupName' in provider:
            return provider['FeatureGroupName']
        elif 'Identifiers' in provider:
            unique_feature_group_names = {identifier['FeatureGroupName'] for identifier in provider['Identifiers']}
            if len(unique_feature_group_names) == 1:
                return list(unique_feature_group_names)[0]
            else:
                return '<multiple feature groups>'

    def _add_attributes(
        self,
        provider: Dict[str, Any],
        attributes: Dict[str, _AttrSpecT],
        setter: Callable[[str, AttributeValue], None],
    ):
        if attributes is None:
            return

        for attr_key, attr_spec in attributes.items():
            attr_path, converter = attr_spec
            value = self._get_attr_value(provider, attr_path)
            if value is None:
                continue
            if converter is not None:
                value = converter(value)
            if value is None:
                continue
            setter(attr_key, value)

    @staticmethod
    def _get_attr_value(provider: Dict[str, Any], attr_path: _AttributePathT):
        if isinstance(attr_path, str):
            return provider.get(attr_path)

        value = provider
        for path_part in attr_path:
            value = value.get(path_part)
            if value is None:
                return None

        return None if value is provider else value
