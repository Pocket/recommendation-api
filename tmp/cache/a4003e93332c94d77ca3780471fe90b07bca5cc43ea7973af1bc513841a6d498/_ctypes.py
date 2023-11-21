# encoding: utf-8
# module _ctypes
# from /usr/local/lib/python3.8/lib-dynload/_ctypes.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
""" Create and manipulate C compatible data types in Python. """
# no imports

# Variables with simple values

FUNCFLAG_CDECL = 1
FUNCFLAG_PYTHONAPI = 4

FUNCFLAG_USE_ERRNO = 8
FUNCFLAG_USE_LASTERROR = 16

RTLD_GLOBAL = 256
RTLD_LOCAL = 0

_cast_addr = 281473566748280

_memmove_addr = 281473585750864

_memset_addr = 281473585755136

_string_at_addr = 281473566741624

_wstring_at_addr = 281473566747136

__version__ = '1.1.0'

# functions

def addressof(C_instance): # real signature unknown; restored from __doc__
    """
    addressof(C instance) -> integer
    Return the address of the C instance internal buffer
    """
    return 0

def alignment(C_type): # real signature unknown; restored from __doc__
    """
    alignment(C type) -> integer
    alignment(C instance) -> integer
    Return the alignment requirements of a C instance
    """
    return 0

def buffer_info(*args, **kwargs): # real signature unknown
    """ Return buffer interface information """
    pass

def byref(C_instance, offset=0): # real signature unknown; restored from __doc__
    """
    byref(C instance[, offset=0]) -> byref-object
    Return a pointer lookalike to a C instance, only usable
    as function argument
    """
    pass

def call_cdeclfunction(*args, **kwargs): # real signature unknown
    pass

def call_function(*args, **kwargs): # real signature unknown
    pass

def dlclose(*args, **kwargs): # real signature unknown
    """ dlclose a library """
    pass

def dlopen(name, flag, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ dlopen(name, flag={RTLD_GLOBAL|RTLD_LOCAL}) open a shared library """
    pass

def dlsym(*args, **kwargs): # real signature unknown
    """ find symbol in shared library """
    pass

def get_errno(*args, **kwargs): # real signature unknown
    pass

def POINTER(*args, **kwargs): # real signature unknown
    pass

def pointer(*args, **kwargs): # real signature unknown
    pass

def PyObj_FromPtr(*args, **kwargs): # real signature unknown
    pass

def Py_DECREF(*args, **kwargs): # real signature unknown
    pass

def Py_INCREF(*args, **kwargs): # real signature unknown
    pass

def resize(*args, **kwargs): # real signature unknown
    """ Resize the memory buffer of a ctypes instance """
    pass

def set_errno(*args, **kwargs): # real signature unknown
    pass

def sizeof(C_type): # real signature unknown; restored from __doc__
    """
    sizeof(C type) -> integer
    sizeof(C instance) -> integer
    Return the size in bytes of a C instance
    """
    return 0

def _unpickle(*args, **kwargs): # real signature unknown
    pass

# classes

class ArgumentError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class Array(_CData):
    """ XXX to be provided """
    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass


class CFuncPtr(_CData):
    """ Function Pointer """
    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
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

    argtypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """specify the argument types"""

    errcheck = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """a function to check for errors"""

    restype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """specify the result type"""



class Structure(_CData):
    """ Structure base class """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class Union(_CData):
    """ Union base class """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class _Pointer(_CData):
    """ XXX to be provided """
    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    contents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the object this pointer points to (read-write)"""



class _SimpleCData(_CData):
    """ XXX to be provided """
    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ctypes_from_outparam__(self, *args, **kwargs): # real signature unknown
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

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """current value"""



# variables with complex values

_pointer_type_cache = {
    None:  # (!) real value is "<class 'ctypes.c_wchar'>"
        None # (!) real value is "<class 'ctypes.LP_c_wchar'>"
    ,
    None:  # (!) real value is "<class 'ctypes.c_char'>"
        None # (!) real value is "<class 'ctypes.LP_c_char'>"
    ,
    None: None, # (!) real value is "<class 'ctypes.c_void_p'>"
}

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924ac0>'

__spec__ = None # (!) real value is "ModuleSpec(name='_ctypes', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924ac0>, origin='/usr/local/lib/python3.8/lib-dynload/_ctypes.cpython-38-aarch64-linux-gnu.so')"

