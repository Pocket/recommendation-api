# encoding: utf-8
# module multidict._multidict
# from /.venv/lib/python3.8/site-packages/multidict/_multidict.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

# functions

def getversion(*args, **kwargs): # real signature unknown
    pass

# classes

class MultiDict(object):
    """ Dictionary with the support for duplicate keys. """
    def add(self, *args, **kwargs): # real signature unknown
        """ Add the key and value, not overwriting any previous value. """
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        """ Remove all items from MultiDict """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        """ Return a copy of itself. """
        pass

    def extend(self, *args, **kwargs): # real signature unknown
        """
        Extend current MultiDict with more values.
        This method must be used instead of update.
        """
        pass

    def get(self, *args, **kwargs): # real signature unknown
        """
        Get first value matching the key.
        
        The method is alias for .getone().
        """
        pass

    def getall(self, *args, **kwargs): # real signature unknown
        """ Return a list of all values matching the key. """
        pass

    def getone(self, *args, **kwargs): # real signature unknown
        """ Get first value matching the key. """
        pass

    def items(self, *args, **kwargs): # real signature unknown
        """ Return a new view of the dictionary's items *(key, value) pairs). """
        pass

    def keys(self, *args, **kwargs): # real signature unknown
        """ Return a new view of the dictionary's keys. """
        pass

    def pop(self, *args, **kwargs): # real signature unknown
        """
        Remove the last occurrence of key and return the corresponding value.
        
        If key is not found, default is returned if given, otherwise KeyError is raised.
        """
        pass

    def popall(self, *args, **kwargs): # real signature unknown
        """
        Remove all occurrences of key and return the list of corresponding values.
        
        If key is not found, default is returned if given, otherwise KeyError is raised.
        """
        pass

    def popitem(self, *args, **kwargs): # real signature unknown
        """ Remove and return an arbitrary (key, value) pair. """
        pass

    def popone(self, *args, **kwargs): # real signature unknown
        """
        Remove the last occurrence of key and return the corresponding value.
        
        If key is not found, default is returned if given, otherwise KeyError is raised.
        """
        pass

    def setdefault(self, *args, **kwargs): # real signature unknown
        """ Return value for key, set value to default if key is not present. """
        pass

    def update(self, *args, **kwargs): # real signature unknown
        """ Update the dictionary from *other*, overwriting existing keys. """
        pass

    def values(self, *args, **kwargs): # real signature unknown
        """ Return a new view of the dictionary's values. """
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

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """ D.__sizeof__() -> size of D in memory, in bytes """
        pass

    __hash__ = None


class CIMultiDict(MultiDict):
    """ Dictionary with the support for duplicate case-insensitive keys. """
    def copy(self, *args, **kwargs): # real signature unknown
        """ Return a copy of itself. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class MultiDictProxy(object):
    """ Read-only proxy for MultiDict instance. """
    def copy(self, *args, **kwargs): # real signature unknown
        """ Return a copy of itself. """
        pass

    def get(self, *args, **kwargs): # real signature unknown
        """
        Get first value matching the key.
        
        The method is alias for .getone().
        """
        pass

    def getall(self, *args, **kwargs): # real signature unknown
        """ Return a list of all values matching the key. """
        pass

    def getone(self, *args, **kwargs): # real signature unknown
        """ Get first value matching the key. """
        pass

    def items(self, *args, **kwargs): # real signature unknown
        """ Return a new view of the dictionary's items *(key, value) pairs). """
        pass

    def keys(self, *args, **kwargs): # real signature unknown
        """ Return a new view of the dictionary's keys. """
        pass

    def values(self, *args, **kwargs): # real signature unknown
        """ Return a new view of the dictionary's values. """
        pass

    @classmethod
    def __class_getitem__(cls, *args, **kwargs): # real signature unknown
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
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

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    __hash__ = None


class CIMultiDictProxy(MultiDictProxy):
    """ Read-only proxy for CIMultiDict instance. """
    def copy(self, *args, **kwargs): # real signature unknown
        """ Return copy of itself """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
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

    __hash__ = None


class istr(str):
    """ istr class implementation """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac167340>'

__spec__ = None # (!) real value is "ModuleSpec(name='multidict._multidict', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac167340>, origin='/.venv/lib/python3.8/site-packages/multidict/_multidict.cpython-38-aarch64-linux-gnu.so')"

