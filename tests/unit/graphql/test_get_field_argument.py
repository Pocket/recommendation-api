import unittest

from strawberry.types.nodes import SelectedField

from app.graphql.util import get_field_argument


def _setup_moment_slate_field_fixture(query_name: str = 'setupMomentSlate', count_value: int = 3):
    return SelectedField(
        name=query_name, directives={}, arguments={},
        selections=[
            SelectedField(name='headline', directives={}, arguments={}, selections=[]),
            SelectedField(name='subheadline', directives={}, arguments={}, selections=[]),
            SelectedField(
                name='recommendations', directives={}, arguments={'count': str(count_value)}, selections=[
                    SelectedField(
                        name='id', directives={}, arguments={}, selections=[]),
                    SelectedField(
                        name='corpusItem', directives={}, arguments={},
                        selections=[
                            SelectedField(name='id', directives={}, arguments={}, selections=[]),
                            SelectedField(name='topic', directives={}, arguments={}, selections=[])
                        ]
                    )
                ],
            )
        ]
    )


_setup_moment_slate_fields_fixture = [_setup_moment_slate_field_fixture()]


class TestGetFieldArgument(unittest.TestCase):

    def test_existing_field_argument(self):
        argument_value = get_field_argument(
            _setup_moment_slate_fields_fixture,
            field_path=['setupMomentSlate', 'recommendations'],
            argument_name='count',
        )

        assert argument_value == '3'

    def test_multiple_queries(self):
        multiple_queries_fixture = [
            _setup_moment_slate_field_fixture(query_name='aDifferentQuery', count_value=123),
            _setup_moment_slate_field_fixture(),
        ]

        argument_value = get_field_argument(
            multiple_queries_fixture,
            field_path=['setupMomentSlate', 'recommendations'],
            argument_name='count'
        )

        assert argument_value == '3'

    def test_non_existing_field(self):
        argument_value = get_field_argument(
            _setup_moment_slate_fields_fixture,
            field_path=['setupMomentSlate', 'fooBar'],
            argument_name='count',
        )

        assert argument_value is None

    def test_non_existing_argument(self):
        argument_value = get_field_argument(
            _setup_moment_slate_fields_fixture,
            field_path=['setupMomentSlate', 'recommendations'],
            argument_name='fooBar',
        )

        assert argument_value is None

    def test_non_existing_argument_returns_default_value(self):
        argument_value = get_field_argument(
            _setup_moment_slate_fields_fixture,
            field_path=['setupMomentSlate', 'recommendations'],
            argument_name='fooBar',
            default_value=123
        )

        assert argument_value == 123
