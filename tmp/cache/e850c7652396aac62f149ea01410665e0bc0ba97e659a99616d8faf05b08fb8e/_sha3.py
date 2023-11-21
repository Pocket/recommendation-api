# encoding: utf-8
# module _sha3
# from /usr/local/lib/python3.8/lib-dynload/_sha3.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

# Variables with simple values

implementation = 'generic 64-bit optimized implementation (lane complementing, all rounds unrolled)'

keccakopt = 64

# no functions
# classes

class sha3_224(object):
    """
    sha3_224([data]) -> SHA3 object
    
    Return a new SHA3 hash object with a hashbit length of 28 bytes.
    """
    def copy(self, *args, **kwargs): # real signature unknown
        """ Return a copy of the hash object. """
        pass

    def digest(self, *args, **kwargs): # real signature unknown
        """ Return the digest value as a bytes object. """
        pass

    def hexdigest(self, *args, **kwargs): # real signature unknown
        """ Return the digest value as a string of hexadecimal digits. """
        pass

    def update(self, *args, **kwargs): # real signature unknown
        """ Update this hash object's state with the provided bytes-like object. """
        pass

    def __init__(self, data=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    block_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    digest_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _capacity_bits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _rate_bits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _suffix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class sha3_256(object):
    """
    sha3_256([data]) -> SHA3 object
    
    Return a new SHA3 hash object with a hashbit length of 32 bytes.
    """
    def copy(self, *args, **kwargs): # real signature unknown
        """ Return a copy of the hash object. """
        pass

    def digest(self, *args, **kwargs): # real signature unknown
        """ Return the digest value as a bytes object. """
        pass

    def hexdigest(self, *args, **kwargs): # real signature unknown
        """ Return the digest value as a string of hexadecimal digits. """
        pass

    def update(self, *args, **kwargs): # real signature unknown
        """ Update this hash object's state with the provided bytes-like object. """
        pass

    def __init__(self, data=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    block_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    digest_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _capacity_bits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _rate_bits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _suffix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class sha3_384(object):
    """
    sha3_384([data]) -> SHA3 object
    
    Return a new SHA3 hash object with a hashbit length of 48 bytes.
    """
    def copy(self, *args, **kwargs): # real signature unknown
        """ Return a copy of the hash object. """
        pass

    def digest(self, *args, **kwargs): # real signature unknown
        """ Return the digest value as a bytes object. """
        pass

    def hexdigest(self, *args, **kwargs): # real signature unknown
        """ Return the digest value as a string of hexadecimal digits. """
        pass

    def update(self, *args, **kwargs): # real signature unknown
        """ Update this hash object's state with the provided bytes-like object. """
        pass

    def __init__(self, data=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    block_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    digest_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _capacity_bits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _rate_bits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _suffix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class sha3_512(object):
    """
    sha3_512([data]) -> SHA3 object
    
    Return a new SHA3 hash object with a hashbit length of 64 bytes.
    """
    def copy(self, *args, **kwargs): # real signature unknown
        """ Return a copy of the hash object. """
        pass

    def digest(self, *args, **kwargs): # real signature unknown
        """ Return the digest value as a bytes object. """
        pass

    def hexdigest(self, *args, **kwargs): # real signature unknown
        """ Return the digest value as a string of hexadecimal digits. """
        pass

    def update(self, *args, **kwargs): # real signature unknown
        """ Update this hash object's state with the provided bytes-like object. """
        pass

    def __init__(self, data=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    block_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    digest_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _capacity_bits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _rate_bits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _suffix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class shake_128(object):
    """
    shake_128([data]) -> SHAKE object
    
    Return a new SHAKE hash object.
    """
    def copy(self, *args, **kwargs): # real signature unknown
        """ Return a copy of the hash object. """
        pass

    def digest(self, *args, **kwargs): # real signature unknown
        """ Return the digest value as a bytes object. """
        pass

    def hexdigest(self, *args, **kwargs): # real signature unknown
        """ Return the digest value as a string of hexadecimal digits. """
        pass

    def update(self, *args, **kwargs): # real signature unknown
        """ Update this hash object's state with the provided bytes-like object. """
        pass

    def __init__(self, data=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    block_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    digest_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _capacity_bits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _rate_bits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _suffix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class shake_256(object):
    """
    shake_256([data]) -> SHAKE object
    
    Return a new SHAKE hash object.
    """
    def copy(self, *args, **kwargs): # real signature unknown
        """ Return a copy of the hash object. """
        pass

    def digest(self, *args, **kwargs): # real signature unknown
        """ Return the digest value as a bytes object. """
        pass

    def hexdigest(self, *args, **kwargs): # real signature unknown
        """ Return the digest value as a string of hexadecimal digits. """
        pass

    def update(self, *args, **kwargs): # real signature unknown
        """ Update this hash object's state with the provided bytes-like object. """
        pass

    def __init__(self, data=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    block_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    digest_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _capacity_bits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _rate_bits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _suffix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffffacc60520>'

__spec__ = None # (!) real value is "ModuleSpec(name='_sha3', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffffacc60520>, origin='/usr/local/lib/python3.8/lib-dynload/_sha3.cpython-38-aarch64-linux-gnu.so')"

