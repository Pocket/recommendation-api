import unittest

from graphql.language.ast import Field, Name, SelectionSet, Argument, IntValue

from app.graphql.util import get_field_argument


def _setup_moment_slate_field_fixture(query_name: str = 'setupMomentSlate', count_value: int = 3):
    return Field(
        name=Name(value=query_name),
        selection_set=SelectionSet(selections=[
            Field(name=Name(value='id')),
            Field(name=Name(value='headline')),
            Field(
                name=Name(value='recommendations'),
                arguments=[Argument(name=Name(value='count'), value=IntValue(value=f'{count_value}'))],
                selection_set=SelectionSet(selections=[
                    Field(name=Name(value='id')),
                    Field(
                        name=Name(value='corpusItem'),
                        selection_set=SelectionSet(selections=[Field(name=Name(value='id'))])
                    ),
                ])
            )
        ])
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
