# encoding: utf-8
# module _blake2
# from /usr/local/lib/python3.8/lib-dynload/_blake2.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
""" _blake2b provides BLAKE2b for hashlib """
# no imports

# Variables with simple values

BLAKE2B_MAX_DIGEST_SIZE = 64

BLAKE2B_MAX_KEY_SIZE = 64

BLAKE2B_PERSON_SIZE = 16

BLAKE2B_SALT_SIZE = 16

BLAKE2S_MAX_DIGEST_SIZE = 32

BLAKE2S_MAX_KEY_SIZE = 32

BLAKE2S_PERSON_SIZE = 8

BLAKE2S_SALT_SIZE = 8

# no functions
# classes

class blake2b(object):
    """ Return a new BLAKE2b hash object. """
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

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    block_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    digest_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    MAX_DIGEST_SIZE = 64
    MAX_KEY_SIZE = 64
    PERSON_SIZE = 16
    SALT_SIZE = 16


class blake2s(object):
    """ Return a new BLAKE2s hash object. """
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

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    block_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    digest_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    MAX_DIGEST_SIZE = 32
    MAX_KEY_SIZE = 32
    PERSON_SIZE = 8
    SALT_SIZE = 8


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffffacc607f0>'

__spec__ = None # (!) real value is "ModuleSpec(name='_blake2', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffffacc607f0>, origin='/usr/local/lib/python3.8/lib-dynload/_blake2.cpython-38-aarch64-linux-gnu.so')"

