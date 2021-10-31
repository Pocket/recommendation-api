from functools import partial
from typing import Annotated

import strawberry


def count_annotation(name: str, default: int):
    """
    :param name: Name of the thing that this count annotation limits.
    :param default: Default value of the count.
    :return: An annotated type
    """
    return Annotated[
        int,
        strawberry.argument(description=f"Maximum number of {name} to return, defaulting to {default}")
    ]


recommendation_count_annotation = partial(count_annotation, name="recommendations")
slate_count_annotation = partial(count_annotation, name="slates")
