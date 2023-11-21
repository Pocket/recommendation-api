# encoding: utf-8
# module _dbm
# from /usr/local/lib/python3.8/lib-dynload/_dbm.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

# Variables with simple values

library = 'Berkeley DB'

# functions

def open(*args, **kwargs): # real signature unknown
    """
    Return a database object.
    
      filename
        The filename to open.
      flags
        How to open the file.  "r" for reading, "w" for writing, etc.
      mode
        If creating a new file, the mode bits for the new file
        (e.g. os.O_RDWR).
    """
    pass

# classes

class error(OSError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924ac0>'

__spec__ = None # (!) real value is "ModuleSpec(name='_dbm', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924ac0>, origin='/usr/local/lib/python3.8/lib-dynload/_dbm.cpython-38-aarch64-linux-gnu.so')"

