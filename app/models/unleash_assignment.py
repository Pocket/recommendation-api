from pydantic import BaseModel


class UnleashAssignmentModel(BaseModel):
    """
    Corresponds to the GraphQL UnleashAssignment object.
    @see https://studio.apollographql.com/graph/pocket-client-api/schema/reference/objects/UnleashAssignment
    """
    assigned: bool
    name: str
    payload: str = None
    variant: str = None
