import random

from aiocache import caches, Cache
from aiocache.serializers import JsonSerializer

import app.config
from typing import ClassVar


class JsonSerializerWithNoneToken(JsonSerializer):
    """
    This class caches None values, and returns EmptyCacheValue instead of None.

    aiocache considers None values to be cache misses, and will therefore always call the function.
    """

    # Special token representing a cached None value.
    class NoneValue:
        pass

    _NONE_STRING: str = '<NONE>'

    def dumps(self, value):
        """
        :return: '<NONE>' if value is None, otherwise dumps value to json.
        """
        if value is None:
            return self._NONE_STRING
        else:
            return super().dumps(value)

    def loads(self, value):
        """
        :return: NoneValue if value is '<NONE>', otherwise loads value using json.loads.
        """
        result = super().loads(value)
        if result == self._NONE_STRING:
            return JsonSerializerWithNoneToken.NoneValue
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
    caches.add(clickdata_alias, get_cache_config(serializer_class=JsonSerializerWithNoneToken))
