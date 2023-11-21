# encoding: utf-8
# module spwd
# from /usr/local/lib/python3.8/lib-dynload/spwd.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
"""
This module provides access to the Unix shadow password database.
It is available on various Unix versions.

Shadow password database entries are reported as 9-tuples of type struct_spwd,
containing the following items from the password database (see `<shadow.h>'):
sp_namp, sp_pwdp, sp_lstchg, sp_min, sp_max, sp_warn, sp_inact, sp_expire, sp_flag.
The sp_namp and sp_pwdp are strings, the rest are integers.
An exception is raised if the entry asked for cannot be found.
You have to be root to be able to use this module.
"""
# no imports

# functions

def getspall(*args, **kwargs): # real signature unknown
    """
    Return a list of all available shadow password database entries, in arbitrary order.
    
    See `help(spwd)` for more on shadow password database entries.
    """
    pass

def getspnam(*args, **kwargs): # real signature unknown
    """
    Return the shadow password database entry for the given user name.
    
    See `help(spwd)` for more on shadow password database entries.
    """
    pass

# classes

class struct_spwd(tuple):
    """
    spwd.struct_spwd: Results from getsp*() routines.
    
    This object may be accessed either as a 9-tuple of
      (sp_namp,sp_pwdp,sp_lstchg,sp_min,sp_max,sp_warn,sp_inact,sp_expire,sp_flag)
    or via the object attributes as named in the above tuple.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    sp_expire = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """#days since 1970-01-01 when account expires"""

    sp_flag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """reserved"""

    sp_inact = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """#days after pw expires until account is disabled"""

    sp_lstchg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """date of last change"""

    sp_max = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """max #days between changes"""

    sp_min = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """min #days between changes"""

    sp_nam = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """login name; deprecated"""

    sp_namp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """login name"""

    sp_pwd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """encrypted password; deprecated"""

    sp_pwdp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """encrypted password"""

    sp_warn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """#days before pw expires to warn user about it"""


    n_fields = 11
    n_sequence_fields = 9
    n_unnamed_fields = 0


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924670>'

__spec__ = None # (!) real value is "ModuleSpec(name='spwd', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924670>, origin='/usr/local/lib/python3.8/lib-dynload/spwd.cpython-38-aarch64-linux-gnu.so')"

