# encoding: utf-8
# module _contextvars
# from /usr/local/lib/python3.8/lib-dynload/_contextvars.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
""" Context Variables """
# no imports

# functions

def copy_context(*args, **kwargs): # real signature unknown
    pass

# classes

class Context(object):
    # no doc
    def copy(self, *args, **kwargs): # real signature unknown
        """ Return a shallow copy of the context object. """
        pass

    def get(self, *args, **kwargs): # real signature unknown
        """
        Return the value for `key` if `key` has the value in the context object.
        
        If `key` does not exist, return `default`. If `default` is not given,
        return None.
        """
        pass

    def items(self, *args, **kwargs): # real signature unknown
        """
        Return all variables and their values in the context object.
        
        The result is returned as a list of 2-tuples (variable, value).
        """
        pass

    def keys(self, *args, **kwargs): # real signature unknown
        """ Return a list of all variables in the context object. """
        pass

    def run(self, *args, **kwargs): # real signature unknown
        pass

    def values(self, *args, **kwargs): # real signature unknown
        """ Return a list of all variables' values in the context object. """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
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

    __hash__ = None


class ContextVar(object):
    # no doc
    def get(self, *args, **kwargs): # real signature unknown
        """
        Return a value for the context variable for the current context.
        
        If there is no value for the variable in the current context, the method will:
         * return the value of the default argument of the method, if provided; or
         * return the default value for the context variable, if it was created
           with one; or
         * raise a LookupError.
        """
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        """
        Reset the context variable.
        
        The variable is reset to the value it had before the `ContextVar.set()` that
        created the token was used.
        """
        pass

    def set(self): # real signature unknown; restored from __doc__
        """
        Call to set a new value for the context variable in the current context.
        
        The required value argument is the new value for the context variable.
        
        Returns a Token object that can be used to restore the variable to its previous
        value via the `ContextVar.reset()` method.
        """
        pass

    @classmethod
    def __class_getitem__(cls, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
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

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Token(object):
    # no doc
    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
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

    old_value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    var = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    MISSING = None # (!) real value is '<Token.MISSING>'
    __hash__ = None


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924ac0>'

__spec__ = None # (!) real value is "ModuleSpec(name='_contextvars', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924ac0>, origin='/usr/local/lib/python3.8/lib-dynload/_contextvars.cpython-38-aarch64-linux-gnu.so')"

