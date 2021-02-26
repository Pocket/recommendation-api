import json
import random
from typing import ClassVar

from pydantic import BaseModel
from aiocache import caches, Cache
from aiocache.serializers import BaseSerializer, JsonSerializer

import app.config
from typing import ClassVar, Optional, Union


# If the cached value parses to None, aiocache will consider this a cache-miss, so we need a special token for this.
class EmptyCacheValue:
    pass


class JsonSerializerWithMissingValues(JsonSerializer):

    def loads(self, value):
        result = super().loads(value)
        if result is None:
            return EmptyCacheValue
        else:
            return result


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
    caches.add(candidate_set_alias, get_cache_config(serializer_class=JsonSerializer))
    caches.add(clickdata_alias, get_cache_config(serializer_class=JsonSerializerWithMissingValues))
