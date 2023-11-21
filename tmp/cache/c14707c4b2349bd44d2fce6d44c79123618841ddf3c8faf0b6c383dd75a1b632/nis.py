# encoding: utf-8
# module nis
# from /usr/local/lib/python3.8/lib-dynload/nis.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
""" This module contains functions for accessing NIS maps. """
# no imports

# functions

def cat(map, domain=None): # real signature unknown; restored from __doc__
    """
    cat(map, domain = defaultdomain)
    Returns the entire map as a dictionary. Optionally domain can be
    specified but it defaults to the system default domain.
    """
    pass

def get_default_domain(): # real signature unknown; restored from __doc__
    """
    get_default_domain() -> str
    Corresponds to the C library yp_get_default_domain() call, returning
    the default NIS domain.
    """
    return ""

def maps(domain=None): # real signature unknown; restored from __doc__
    """
    maps(domain = defaultdomain)
    Returns an array of all available NIS maps within a domain. If domain
    is not specified it defaults to the system default domain.
    """
    pass

def match(key, map, domain=None): # real signature unknown; restored from __doc__
    """
    match(key, map, domain = defaultdomain)
    Corresponds to the C library yp_match() call, returning the value of
    key in the given map. Optionally domain can be specified but it
    defaults to the system default domain.
    """
    pass

# classes

class error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924ac0>'

__spec__ = None # (!) real value is "ModuleSpec(name='nis', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924ac0>, origin='/usr/local/lib/python3.8/lib-dynload/nis.cpython-38-aarch64-linux-gnu.so')"

