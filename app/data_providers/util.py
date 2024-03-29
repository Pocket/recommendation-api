import hashlib
from typing import List, Dict, Generator, TypeVar, Sequence


def flatten(items: List) -> List:
    """
    Recursively flattens a list-of-lists.
    :param items: List of lists
    :return: List of all non-list elements in sequence.
    """
    return sum(map(flatten, items), []) if isinstance(items, list) else [items]


def get_dict_without_none(d: Dict) -> Dict:
    return {k: v for k, v in d.items() if v is not None}


T = TypeVar('T')


# For Generator type-hint explanation, see https://docs.python.org/3/library/typing.html#typing.Generator
def chunks(sequence: Sequence[T], n: int) -> Generator[Sequence[T], None, None]:
    """Yield successive n-sized chunks from the sequence."""
    for i in range(0, len(sequence), n):
        yield sequence[i: i + n]


def integer_hash(s: str, start: int, stop: int) -> int:
    """
    :param s: String to be hashed.
    :param start:
    :param stop:
    :return: Integer hash of s in the range [start, stop)
    """
    return start + (int(hashlib.sha256(s.encode("utf-8")).hexdigest(), 16) % (stop - start))
