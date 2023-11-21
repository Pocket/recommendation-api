# encoding: utf-8
# module frozenlist._frozenlist
# from /.venv/lib/python3.8/site-packages/frozenlist/_frozenlist.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import sys as sys # <module 'sys' (built-in)>
import types as types # /usr/local/lib/python3.8/types.py
import collections.abc as __collections_abc


# functions

def __pyx_unpickle_FrozenList(*args, **kwargs): # real signature unknown
    pass

# classes

class FrozenList(object):
    # no doc
    def append(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def count(self, *args, **kwargs): # real signature unknown
        pass

    def extend(self, *args, **kwargs): # real signature unknown
        pass

    def freeze(self, *args, **kwargs): # real signature unknown
        pass

    def index(self, *args, **kwargs): # real signature unknown
        pass

    def insert(self, *args, **kwargs): # real signature unknown
        pass

    def pop(self, *args, **kwargs): # real signature unknown
        pass

    def remove(self, *args, **kwargs): # real signature unknown
        pass

    def reverse(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def __class_getitem__(cls, *args, **kwargs): # real signature unknown
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Return self+=value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __reversed__(self, *args, **kwargs): # real signature unknown
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    frozen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0xffffac7d7ab0>'


class MutableSequence(__collections_abc.Sequence):
    # no doc
    def append(self, value): # reliably restored by inspect
        """ S.append(value) -- append value to the end of the sequence """
        pass

    def clear(self): # reliably restored by inspect
        """ S.clear() -> None -- remove all items from S """
        pass

    def extend(self, values): # reliably restored by inspect
        """ S.extend(iterable) -- extend sequence by appending elements from the iterable """
        pass

    def insert(self, index, value): # reliably restored by inspect
        """ S.insert(index, value) -- insert value before index """
        pass

    def pop(self, index=-1): # reliably restored by inspect
        """
        S.pop([index]) -> item -- remove and return item at index (default last).
                   Raise IndexError if list is empty or index is out of range.
        """
        pass

    def remove(self, value): # reliably restored by inspect
        """
        S.remove(value) -- remove first occurrence of value.
                   Raise ValueError if the value is not present.
        """
        pass

    def reverse(self): # reliably restored by inspect
        """ S.reverse() -- reverse *IN PLACE* """
        pass

    def __delitem__(self, index): # reliably restored by inspect
        # no doc
        pass

    def __iadd__(self, values): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __setitem__(self, index, value): # reliably restored by inspect
        # no doc
        pass

    _abc_impl = None # (!) real value is '<_abc_data object at 0xffffacde3690>'
    __abstractmethods__ = frozenset({'__setitem__', '__len__', 'insert', '__delitem__', '__getitem__'})
    __slots__ = ()


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac7d7cd0>'

__spec__ = None # (!) real value is "ModuleSpec(name='frozenlist._frozenlist', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac7d7cd0>, origin='/.venv/lib/python3.8/site-packages/frozenlist/_frozenlist.cpython-38-aarch64-linux-gnu.so')"

__test__ = {}

