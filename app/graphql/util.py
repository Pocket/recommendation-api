from typing import List

from strawberry.types import Info
from strawberry.types.nodes import SelectedField

from app.models.user_ids import UserIds


def get_field_argument(
        fields: List[SelectedField],
        field_path: List[str],
        argument_name: str,
        default_value=None
):
    """
    Returns the value of a GraphQL field argument. In the following example the return value is  '3':
    query { setupMomentSlate{ recommendations(count: 3) { id } } }

    This function feels like it should be implemented in a GraphQL library. Graphene provides easy access to top-level
    query arguments, but I could not find an easy way to access arguments on other fields.
    Graphene has been deprecated from FastAPI/Starlette, and the recommended GraphQL library is now Strawberry.
    Perhaps Strawberry handles field arguments better?

    :param fields: List of GraphQL fields, which can be obtained from `graphql.ResolveInfo.field_asts`.
    :param field_path: GraphQL field names to traverse. ['setupMomentSlate', 'recommendations'] in the above example.
    :param argument_name: Name of the argument. 'count' in the above example.
    :param default_value: The value to return if the field and/or argument is missing from the query.
    :return: Field argument value in string representation, or `default_value` if field argument is not present.
    """
    for field in fields:
        if field.name == field_path[0]:
            if len(field_path) == 1:
                # End of recursion: We've reached the desired field, and can now find the argument.
                return field.arguments.get(argument_name, default_value)
            else:
                # Recursion with the next level of fields, with the first element from `field_path` removed.
                return get_field_argument(
                    fields=field.selections,
                    field_path=field_path[1:],
                    argument_name=argument_name,
                    default_value=default_value
                )

    return default_value


def get_user_ids(info: Info) -> UserIds:
    """
    Get user ids from the request headers that are available in the GraphQL context.
    :param info:
    :return:
    """
    headers = info.context.get('request').headers

    return UserIds(
        user_id=headers.get('userId'),
        hashed_user_id=headers.get('encodedId'),
        hashed_guid=headers.get('encodedGuid'),
        guid=headers.get('guid'),
    )
