# encoding: utf-8
# module httptools.parser.parser
# from /.venv/lib/python3.8/site-packages/httptools/parser/parser.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import httptools.parser.errors as __httptools_parser_errors


# no functions
# classes

class HttpParserError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class HttpParserCallbackError(__httptools_parser_errors.HttpParserError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class HttpParserInvalidMethodError(__httptools_parser_errors.HttpParserError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class HttpParserInvalidStatusError(__httptools_parser_errors.HttpParserError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class HttpParserInvalidURLError(__httptools_parser_errors.HttpParserError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class HttpParserUpgrade(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class HttpRequestParser(HttpParser):
    # no doc
    def get_method(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0xffffabe8a030>'


class HttpResponseParser(HttpParser):
    # no doc
    def get_status_code(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0xffffabe8a8d0>'


# variables with complex values

__all__ = (
    'HttpRequestParser',
    'HttpResponseParser',
)

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffffabe8aaf0>'

__spec__ = None # (!) real value is "ModuleSpec(name='httptools.parser.parser', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffffabe8aaf0>, origin='/.venv/lib/python3.8/site-packages/httptools/parser/parser.cpython-38-aarch64-linux-gnu.so')"

__test__ = {}

