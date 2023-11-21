# encoding: utf-8
# module _testbuffer
# from /usr/local/lib/python3.8/lib-dynload/_testbuffer.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

# Variables with simple values

ND_FORTRAN = 4

ND_GETBUF_FAIL = 64
ND_GETBUF_UNDEFINED = 128

ND_MAX_NDIM = 128

ND_PIL = 16
ND_REDIRECT = 32
ND_SCALAR = 8
ND_VAREXPORT = 1
ND_WRITABLE = 2

PyBUF_ANY_CONTIGUOUS = 152

PyBUF_CONTIG = 9

PyBUF_CONTIG_RO = 8

PyBUF_C_CONTIGUOUS = 56

PyBUF_FORMAT = 4
PyBUF_FULL = 285

PyBUF_FULL_RO = 284

PyBUF_F_CONTIGUOUS = 88

PyBUF_INDIRECT = 280
PyBUF_ND = 8
PyBUF_READ = 256
PyBUF_RECORDS = 29

PyBUF_RECORDS_RO = 28

PyBUF_SIMPLE = 0
PyBUF_STRIDED = 25

PyBUF_STRIDED_RO = 24

PyBUF_STRIDES = 24
PyBUF_WRITABLE = 1
PyBUF_WRITE = 512

# functions

def cmp_contig(*args, **kwargs): # real signature unknown
    pass

def get_contiguous(*args, **kwargs): # real signature unknown
    pass

def get_pointer(*args, **kwargs): # real signature unknown
    pass

def get_sizeof_void_p(*args, **kwargs): # real signature unknown
    pass

def is_contiguous(*args, **kwargs): # real signature unknown
    pass

def py_buffer_to_contiguous(*args, **kwargs): # real signature unknown
    pass

def slice_indices(*args, **kwargs): # real signature unknown
    pass

# classes

class ndarray(object):
    # no doc
    def add_suboffsets(self, *args, **kwargs): # real signature unknown
        pass

    def memoryview_from_buffer(self, *args, **kwargs): # real signature unknown
        pass

    def pop(self, *args, **kwargs): # real signature unknown
        pass

    def push(self, *args, **kwargs): # real signature unknown
        pass

    def tobytes(self, *args, **kwargs): # real signature unknown
        pass

    def tolist(self, *args, **kwargs): # real signature unknown
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
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

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    contiguous = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    c_contiguous = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f_contiguous = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    itemsize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nbytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ndim = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    obj = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    readonly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    shape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    strides = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    suboffsets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class staticarray(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924ac0>'

__spec__ = None # (!) real value is "ModuleSpec(name='_testbuffer', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924ac0>, origin='/usr/local/lib/python3.8/lib-dynload/_testbuffer.cpython-38-aarch64-linux-gnu.so')"

