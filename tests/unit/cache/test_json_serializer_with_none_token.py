from typing import Any

import pytest

from app.cache import JsonSerializerWithNoneToken, NoneValue


class TestJsonSerializerWithNoneToken:

    @pytest.mark.parametrize(
        "value,expected",
        [
            (None, '<NONE>'),
            ({"foo": "bar"}, '{"foo":"bar"}'),
            (NoneValue, '<NONE>'),
        ])
    def test_dumps(self, value: Any, expected: str):
        serializer = JsonSerializerWithNoneToken()
        assert expected == serializer.dumps(value)

    @pytest.mark.parametrize(
        "value,expected",
        [
            ('<NONE>', NoneValue),
            ('{"foo":"bar"}', {"foo": "bar"}),
        ])
    def test_loads(self, value: Any, expected: str):
        serializer = JsonSerializerWithNoneToken()
        assert expected == serializer.loads(value)
