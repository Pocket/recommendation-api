# encoding: utf-8
# module scipy._lib._uarray._uarray calls itself uarray._uarray
# from /.venv/lib/python3.8/site-packages/scipy/_lib/_uarray/_uarray.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

# functions

def clear_backends(*args, **kwargs): # real signature unknown
    pass

def determine_backend(*args, **kwargs): # real signature unknown
    pass

def get_state(*args, **kwargs): # real signature unknown
    pass

def register_backend(*args, **kwargs): # real signature unknown
    pass

def set_global_backend(*args, **kwargs): # real signature unknown
    pass

def set_state(*args, **kwargs): # real signature unknown
    pass

# classes

class BackendNotImplementedError(NotImplementedError):
    """ An exception that is thrown when no compatible backend is found for a method. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class _BackendState(object):
    # no doc
    def _pickle(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def _unpickle(cls, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class _Function(object):
    # no doc
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __get__(self, *args, **kwargs): # real signature unknown
        """ Return an attribute of instance, which is of type owner. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    arg_extractor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    arg_replacer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    default = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    domain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'__repr__': <slot wrapper '__repr__' of 'uarray._Function' objects>, '__call__': <slot wrapper '__call__' of 'uarray._Function' objects>, '__getattribute__': <slot wrapper '__getattribute__' of 'uarray._Function' objects>, '__setattr__': <slot wrapper '__setattr__' of 'uarray._Function' objects>, '__delattr__': <slot wrapper '__delattr__' of 'uarray._Function' objects>, '__get__': <slot wrapper '__get__' of 'uarray._Function' objects>, '__init__': <slot wrapper '__init__' of 'uarray._Function' objects>, '__new__': <built-in method __new__ of type object at 0xffff9f8303f0>, '__dict__': <attribute '__dict__' of 'uarray._Function' objects>, 'arg_extractor': <attribute 'arg_extractor' of 'uarray._Function' objects>, 'arg_replacer': <attribute 'arg_replacer' of 'uarray._Function' objects>, 'default': <attribute 'default' of 'uarray._Function' objects>, 'domain': <attribute 'domain' of 'uarray._Function' objects>, '__doc__': None})"


class _SetBackendContext(object):
    # no doc
    def _pickle(self, *args, **kwargs): # real signature unknown
        pass

    def __enter__(self, *args, **kwargs): # real signature unknown
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class _SkipBackendContext(object):
    # no doc
    def _pickle(self, *args, **kwargs): # real signature unknown
        pass

    def __enter__(self, *args, **kwargs): # real signature unknown
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9f842430>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy._lib._uarray._uarray', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9f842430>, origin='/.venv/lib/python3.8/site-packages/scipy/_lib/_uarray/_uarray.cpython-38-aarch64-linux-gnu.so')"

