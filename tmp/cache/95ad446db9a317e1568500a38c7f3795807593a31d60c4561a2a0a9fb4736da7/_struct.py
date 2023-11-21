# encoding: utf-8
# module _struct
# from /usr/local/lib/python3.8/lib-dynload/_struct.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
"""
Functions to convert between Python values and C structs.
Python bytes objects are used to hold the data representing the C struct
and also as format strings (explained below) to describe the layout of data
in the C struct.

The optional first format char indicates byte order, size and alignment:
  @: native order, size & alignment (default)
  =: native order, std. size & alignment
  <: little-endian, std. size & alignment
  >: big-endian, std. size & alignment
  !: same as >

The remaining chars indicate types of args and must match exactly;
these can be preceded by a decimal repeat count:
  x: pad byte (no data); c:char; b:signed byte; B:unsigned byte;
  ?: _Bool (requires C99; if not available, char is used instead)
  h:short; H:unsigned short; i:int; I:unsigned int;
  l:long; L:unsigned long; f:float; d:double; e:half-float.
Special cases (preceding decimal count indicates length):
  s:string (array of char); p: pascal string (with count byte).
Special cases (only available in native format):
  n:ssize_t; N:size_t;
  P:an integer type that is wide enough to hold a pointer.
Special case (not in native mode unless 'long long' in platform C):
  q:long long; Q:unsigned long long
Whitespace between formats is ignored.

The variable struct.error is an exception raised on errors.
"""
# no imports

# functions

def calcsize(fmt): # known case of _struct.calcsize
    """ Return size in bytes of the struct described by the format string. """
    return 0

def iter_unpack(*args, **kwargs): # real signature unknown
    """
    Return an iterator yielding tuples unpacked from the given bytes.
    
    The bytes are unpacked according to the format string, like
    a repeated invocation of unpack_from().
    
    Requires that the bytes length be a multiple of the format struct size.
    """
    pass

def pack(fmt, *args): # known case of _struct.pack
    """
    pack(format, v1, v2, ...) -> bytes
    
    Return a bytes object containing the values v1, v2, ... packed according
    to the format string.  See help(struct) for more on format strings.
    """
    return b""

def pack_into(fmt, buffer, offset, *args): # known case of _struct.pack_into
    """
    pack_into(format, buffer, offset, v1, v2, ...)
    
    Pack the values v1, v2, ... according to the format string and write
    the packed bytes into the writable buffer buf starting at offset.  Note
    that the offset is a required argument.  See help(struct) for more
    on format strings.
    """
    pass

def unpack(fmt, string): # known case of _struct.unpack
    """
    Return a tuple containing values unpacked according to the format string.
    
    The buffer's size in bytes must be calcsize(format).
    
    See help(struct) for more on format strings.
    """
    pass

def unpack_from(fmt, buffer, offset=0): # known case of _struct.unpack_from
    """
    Return a tuple containing values unpacked according to the format string.
    
    The buffer's size, minus offset, must be at least calcsize(format).
    
    See help(struct) for more on format strings.
    """
    pass

def _clearcache(*args, **kwargs): # real signature unknown
    """ Clear the internal cache. """
    pass

# classes

class error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class Struct(object):
    """
    Create a compiled struct object.
    
    Return a new Struct object which writes and reads binary data according to
    the format string.
    
    See help(struct) for more on format strings.
    """
    def iter_unpack(self, *args, **kwargs): # real signature unknown
        """
        Return an iterator yielding tuples.
        
        Tuples are unpacked from the given bytes source, like a repeated
        invocation of unpack_from().
        
        Requires that the bytes length be a multiple of the struct size.
        """
        pass

    def pack(self, *args): # known case of _struct.Struct.pack
        """
        S.pack(v1, v2, ...) -> bytes
        
        Return a bytes object containing values v1, v2, ... packed according
        to the format string S.format.  See help(struct) for more on format
        strings.
        """
        return b""

    def pack_into(self, buffer, offset, *args): # known case of _struct.Struct.pack_into
        """
        S.pack_into(buffer, offset, v1, v2, ...)
        
        Pack the values v1, v2, ... according to the format string S.format
        and write the packed bytes into the writable buffer buf starting at
        offset.  Note that the offset is a required argument.  See
        help(struct) for more on format strings.
        """
        pass

    def unpack(self, string): # known case of _struct.Struct.unpack
        """
        Return a tuple containing unpacked values.
        
        Unpack according to the format string Struct.format. The buffer's size
        in bytes must be Struct.size.
        
        See help(struct) for more on format strings.
        """
        pass

    def unpack_from(self, buffer, offset=0): # known case of _struct.Struct.unpack_from
        """
        Return a tuple containing unpacked values.
        
        Values are unpacked according to the format string Struct.format.
        
        The buffer's size in bytes, starting at position offset, must be
        at least Struct.size.
        
        See help(struct) for more on format strings.
        """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, fmt): # known case of _struct.Struct.__init__
        """
        Create a compiled struct object.
        
        Return a new Struct object which writes and reads binary data according to
        the format string.
        
        See help(struct) for more on format strings.
        # (copied from class doc)
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """ S.__sizeof__() -> size of S in memory, in bytes """
        pass

    format = property(lambda self: '')
    """struct format string

    :type: string
    """

    size = property(lambda self: 0)
    """struct size in bytes

    :type: int
    """



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac131af0>'

__spec__ = None # (!) real value is "ModuleSpec(name='_struct', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac131af0>, origin='/usr/local/lib/python3.8/lib-dynload/_struct.cpython-38-aarch64-linux-gnu.so')"

