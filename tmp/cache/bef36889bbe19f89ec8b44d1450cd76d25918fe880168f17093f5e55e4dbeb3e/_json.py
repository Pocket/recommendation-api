# encoding: utf-8
# module _json
# from /usr/local/lib/python3.8/lib-dynload/_json.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
""" json speedups """
# no imports

# functions

def encode_basestring(string): # real signature unknown; restored from __doc__
    """
    encode_basestring(string) -> string
    
    Return a JSON representation of a Python string
    """
    return ""

def encode_basestring_ascii(string): # real signature unknown; restored from __doc__
    """
    encode_basestring_ascii(string) -> string
    
    Return an ASCII-only JSON representation of a Python string
    """
    return ""

def scanstring(string, end, strict=True): # real signature unknown; restored from __doc__
    """
    scanstring(string, end, strict=True) -> (string, end)
    
    Scan the string s for a JSON string. End is the index of the
    character in s after the quote that started the JSON string.
    Unescapes all valid JSON string escape sequences and raises ValueError
    on attempt to decode an invalid string. If strict is False then literal
    control characters are allowed in the string.
    
    Returns a tuple of the decoded string and the index of the character in s
    after the end quote.
    """
    pass

# classes

class make_encoder(object):
    """ _iterencode(obj, _current_indent_level) -> iterable """
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    default = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """default"""

    encoder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """encoder"""

    indent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """indent"""

    item_separator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """item_separator"""

    key_separator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """key_separator"""

    markers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """markers"""

    skipkeys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """skipkeys"""

    sort_keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """sort_keys"""



class make_scanner(object):
    """ JSON scanner object """
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    object_hook = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """object_hook"""

    object_pairs_hook = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parse_constant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """parse_constant"""

    parse_float = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """parse_float"""

    parse_int = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """parse_int"""

    strict = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """strict"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xfffface97df0>'

__spec__ = None # (!) real value is "ModuleSpec(name='_json', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xfffface97df0>, origin='/usr/local/lib/python3.8/lib-dynload/_json.cpython-38-aarch64-linux-gnu.so')"

