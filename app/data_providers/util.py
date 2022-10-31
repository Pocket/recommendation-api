from typing import List, Dict


def flatten(items: List) -> List:
    """
    Recursively flattens a list-of-lists.
    :param items: List of lists
    :return: List of all non-list elements in sequence.
    """
    return sum(map(flatten, items), []) if isinstance(items, list) else [items]


def get_dict_without_none(d: Dict) -> Dict:
    return {k: v for k, v in d.items() if v is not None}
