import json
import random
from typing import ClassVar

from pydantic import BaseModel
from aiocache import caches, Cache
from aiocache.serializers import BaseSerializer

import app.config
from app.models.candidate_set import CandidateSetModel
from app.models.clickdata import ClickdataModel
from typing import ClassVar, Optional, Union


# If the cached value parses to None, aiocache will consider this a cache-miss, so we need a special token for this.
class EmptyCacheValue:
    pass


class _PydanticSerializer(BaseSerializer):

    def dumps(self, value: Optional[BaseModel]):
        if value is None:
            return json.dumps(value)
        else:
            # JSON encode Pydantic model
            return value.json()

    def loads(self, value: str) -> Union[BaseModel, EmptyCacheValue]:
        if value is None or value == 'null':
            return EmptyCacheValue()
        else:
            return self._parse(value)

    def _parse(self, value: str):
        raise NotImplementedError()


class CandidateSetModelSerializer(_PydanticSerializer):

    def _parse(self, value: str):
        return CandidateSetModel.parse_raw(value)


class ClickdataModelSerializer(_PydanticSerializer):

    def _parse(self, value: str):
        return ClickdataModel.parse_raw(value)


def get_cache_config(serializer_class: ClassVar):
    server = random.choice(app.config.elasticache['servers'])
    endpoint, port = server.split(':')

    return {
        'cache': Cache.MEMCACHED,
        'endpoint': endpoint,
        'port': port,
        'serializer': {
            'class': serializer_class,
        },
    }


candidate_set_alias = 'candidate-set-cache'
clickdata_alias = 'clickdata-cache'


def initialize_caches():
    caches.add(candidate_set_alias, get_cache_config(serializer_class=CandidateSetModelSerializer))
    caches.add(clickdata_alias, get_cache_config(serializer_class=ClickdataModelSerializer))
