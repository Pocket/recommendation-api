# encoding: utf-8
# module grp
# from /usr/local/lib/python3.8/lib-dynload/grp.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
"""
Access to the Unix group database.

Group entries are reported as 4-tuples containing the following fields
from the group database, in order:

  gr_name   - name of the group
  gr_passwd - group password (encrypted); often empty
  gr_gid    - numeric ID of the group
  gr_mem    - list of members

The gid is an integer, name and password are strings.  (Note that most
users are not explicitly listed as members of the groups they are in
according to the password database.  Check both databases to get
complete membership information.)
"""
# no imports

# functions

def getgrall(*args, **kwargs): # real signature unknown
    """
    Return a list of all available group entries, in arbitrary order.
    
    An entry whose name starts with '+' or '-' represents an instruction
    to use YP/NIS and may not be accessible via getgrnam or getgrgid.
    """
    pass

def getgrgid(*args, **kwargs): # real signature unknown
    """
    Return the group database entry for the given numeric group ID.
    
    If id is not valid, raise KeyError.
    """
    pass

def getgrnam(*args, **kwargs): # real signature unknown
    """
    Return the group database entry for the given group name.
    
    If name is not valid, raise KeyError.
    """
    pass

# classes

class struct_group(tuple):
    """
    grp.struct_group: Results from getgr*() routines.
    
    This object may be accessed either as a tuple of
      (gr_name,gr_passwd,gr_gid,gr_mem)
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

    gr_gid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """group id"""

    gr_mem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """group members"""

    gr_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """group name"""

    gr_passwd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """password"""


    n_fields = 4
    n_sequence_fields = 4
    n_unnamed_fields = 0


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xfffface88c70>'

__spec__ = None # (!) real value is "ModuleSpec(name='grp', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xfffface88c70>, origin='/usr/local/lib/python3.8/lib-dynload/grp.cpython-38-aarch64-linux-gnu.so')"

