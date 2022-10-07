from typing import List


def flatten(items: List) -> List:
    """
    Recursively flattens a list-of-lists.
    :param items: List of lists
    :return: List of all non-list elements in sequence.
    """
    return sum(map(flatten, items), []) if isinstance(items, list) else [items]
