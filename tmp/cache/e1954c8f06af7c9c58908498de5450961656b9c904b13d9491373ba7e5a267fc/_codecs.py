# encoding: utf-8
# module _codecs
# from (built-in)
# by generator 1.147
# no doc
# no imports

# functions

def ascii_decode(*args, **kwargs): # real signature unknown
    pass

def ascii_encode(*args, **kwargs): # real signature unknown
    pass

def charmap_build(*args, **kwargs): # real signature unknown
    pass

def charmap_decode(*args, **kwargs): # real signature unknown
    pass

def charmap_encode(*args, **kwargs): # real signature unknown
    pass

def decode(*args, **kwargs): # real signature unknown
    """
    Decodes obj using the codec registered for encoding.
    
    Default encoding is 'utf-8'.  errors may be given to set a
    different error handling scheme.  Default is 'strict' meaning that encoding
    errors raise a ValueError.  Other possible values are 'ignore', 'replace'
    and 'backslashreplace' as well as any other name registered with
    codecs.register_error that can handle ValueErrors.
    """
    pass

def encode(*args, **kwargs): # real signature unknown
    """
    Encodes obj using the codec registered for encoding.
    
    The default encoding is 'utf-8'.  errors may be given to set a
    different error handling scheme.  Default is 'strict' meaning that encoding
    errors raise a ValueError.  Other possible values are 'ignore', 'replace'
    and 'backslashreplace' as well as any other name registered with
    codecs.register_error that can handle ValueErrors.
    """
    pass

def escape_decode(*args, **kwargs): # real signature unknown
    pass

def escape_encode(*args, **kwargs): # real signature unknown
    pass

def latin_1_decode(*args, **kwargs): # real signature unknown
    pass

def latin_1_encode(*args, **kwargs): # real signature unknown
    pass

def lookup(*args, **kwargs): # real signature unknown
    """ Looks up a codec tuple in the Python codec registry and returns a CodecInfo object. """
    pass

def lookup_error(errors): # real signature unknown; restored from __doc__
    """
    lookup_error(errors) -> handler
    
    Return the error handler for the specified error handling name or raise a
    LookupError, if no handler exists under this name.
    """
    pass

def raw_unicode_escape_decode(*args, **kwargs): # real signature unknown
    pass

def raw_unicode_escape_encode(*args, **kwargs): # real signature unknown
    pass

def readbuffer_encode(*args, **kwargs): # real signature unknown
    pass

def register(*args, **kwargs): # real signature unknown
    """
    Register a codec search function.
    
    Search functions are expected to take one argument, the encoding name in
    all lower case letters, and either return None, or a tuple of functions
    (encoder, decoder, stream_reader, stream_writer) (or a CodecInfo object).
    """
    pass

def register_error(*args, **kwargs): # real signature unknown
    """
    Register the specified error handler under the name errors.
    
    handler must be a callable object, that will be called with an exception
    instance containing information about the location of the encoding/decoding
    error and must return a (replacement, new position) tuple.
    """
    pass

def unicode_escape_decode(*args, **kwargs): # real signature unknown
    pass

def unicode_escape_encode(*args, **kwargs): # real signature unknown
    pass

def utf_16_be_decode(*args, **kwargs): # real signature unknown
    pass

def utf_16_be_encode(*args, **kwargs): # real signature unknown
    pass

def utf_16_decode(*args, **kwargs): # real signature unknown
    pass

def utf_16_encode(*args, **kwargs): # real signature unknown
    pass

def utf_16_ex_decode(*args, **kwargs): # real signature unknown
    pass

def utf_16_le_decode(*args, **kwargs): # real signature unknown
    pass

def utf_16_le_encode(*args, **kwargs): # real signature unknown
    pass

def utf_32_be_decode(*args, **kwargs): # real signature unknown
    pass

def utf_32_be_encode(*args, **kwargs): # real signature unknown
    pass

def utf_32_decode(*args, **kwargs): # real signature unknown
    pass

def utf_32_encode(*args, **kwargs): # real signature unknown
    pass

def utf_32_ex_decode(*args, **kwargs): # real signature unknown
    pass

def utf_32_le_decode(*args, **kwargs): # real signature unknown
    pass

def utf_32_le_encode(*args, **kwargs): # real signature unknown
    pass

def utf_7_decode(*args, **kwargs): # real signature unknown
    pass

def utf_7_encode(*args, **kwargs): # real signature unknown
    pass

def utf_8_decode(*args, **kwargs): # real signature unknown
    pass

def utf_8_encode(*args, **kwargs): # real signature unknown
    pass

def _forget_codec(*args, **kwargs): # real signature unknown
    """ Purge the named codec from the internal codec lookup cache """
    pass

# classes

class __loader__(object):
    """
    Meta path import for built-in modules.
    
        All methods are either class or static methods to avoid the need to
        instantiate the class.
    """
    @classmethod
    def create_module(cls, *args, **kwargs): # real signature unknown
        """ Create a built-in module """
        pass

    @classmethod
    def exec_module(cls, *args, **kwargs): # real signature unknown
        """ Exec a built-in module """
        pass

    @classmethod
    def find_module(cls, *args, **kwargs): # real signature unknown
        """
        Find the built-in module.
        
                If 'path' is ever specified then the search is considered a failure.
        
                This method is deprecated.  Use find_spec() instead.
        """
        pass

    @classmethod
    def find_spec(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def get_code(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have code objects. """
        pass

    @classmethod
    def get_source(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have source code. """
        pass

    @classmethod
    def is_package(cls, *args, **kwargs): # real signature unknown
        """ Return False as built-in modules are never packages. """
        pass

    @classmethod
    def load_module(cls, *args, **kwargs): # real signature unknown
        """
        Load the specified module into sys.modules and return it.
        
            This method is deprecated.  Use loader.exec_module instead.
        """
        pass

    def module_repr(module): # reliably restored by inspect
        """
        Return repr for the module.
        
                The method is deprecated.  The import machinery does the job itself.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__doc__': 'Meta path import for built-in modules.\\n\\n    All methods are either class or static methods to avoid the need to\\n    instantiate the class.\\n\\n    ', 'module_repr': <staticmethod object at 0xffffacf8a430>, 'find_spec': <classmethod object at 0xffffacf8a460>, 'find_module': <classmethod object at 0xffffacf8a490>, 'create_module': <classmethod object at 0xffffacf8a4c0>, 'exec_module': <classmethod object at 0xffffacf8a4f0>, 'get_code': <classmethod object at 0xffffacf8a580>, 'get_source': <classmethod object at 0xffffacf8a610>, 'is_package': <classmethod object at 0xffffacf8a6a0>, 'load_module': <classmethod object at 0xffffacf8a6d0>, '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"


# variables with complex values

__spec__ = None # (!) real value is "ModuleSpec(name='_codecs', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

