# encoding: utf-8
# module _tracemalloc
# from (built-in)
# by generator 1.147
""" Debug module to trace memory blocks allocated by Python. """
# no imports

# functions

def clear_traces(*args, **kwargs): # real signature unknown
    """ Clear traces of memory blocks allocated by Python. """
    pass

def get_traceback_limit(*args, **kwargs): # real signature unknown
    """
    Get the maximum number of frames stored in the traceback of a trace.
    
    By default, a trace of an allocated memory block only stores
    the most recent frame: the limit is 1.
    """
    pass

def get_traced_memory(*args, **kwargs): # real signature unknown
    """
    Get the current size and peak size of memory blocks traced by tracemalloc.
    
    Returns a tuple: (current: int, peak: int).
    """
    pass

def get_tracemalloc_memory(*args, **kwargs): # real signature unknown
    """
    Get the memory usage in bytes of the tracemalloc module.
    
    This memory is used internally to trace memory allocations.
    """
    pass

def is_tracing(*args, **kwargs): # real signature unknown
    """ Return True if the tracemalloc module is tracing Python memory allocations. """
    pass

def start(*args, **kwargs): # real signature unknown
    """
    Start tracing Python memory allocations.
    
    Also set the maximum number of frames stored in the traceback of a
    trace to nframe.
    """
    pass

def stop(*args, **kwargs): # real signature unknown
    """
    Stop tracing Python memory allocations.
    
    Also clear traces of memory blocks allocated by Python.
    """
    pass

def _get_object_traceback(*args, **kwargs): # real signature unknown
    """
    Get the traceback where the Python object obj was allocated.
    
    Return a tuple of (filename: str, lineno: int) tuples.
    Return None if the tracemalloc module is disabled or did not
    trace the allocation of the object.
    """
    pass

def _get_traces(*args, **kwargs): # real signature unknown
    """
    Get traces of all memory blocks allocated by Python.
    
    Return a list of (size: int, traceback: tuple) tuples.
    traceback is a tuple of (filename: str, lineno: int) tuples.
    
    Return an empty list if the tracemalloc module is disabled.
    """
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

__spec__ = None # (!) real value is "ModuleSpec(name='_tracemalloc', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

