# encoding: utf-8
# module faulthandler
# from (built-in)
# by generator 1.147
""" faulthandler module. """
# no imports

# functions

def cancel_dump_traceback_later(): # real signature unknown; restored from __doc__
    """
    cancel_dump_traceback_later():
    cancel the previous call to dump_traceback_later().
    """
    pass

def disable(): # real signature unknown; restored from __doc__
    """ disable(): disable the fault handler """
    pass

def dump_traceback(file=None, all_threads=True): # real signature unknown; restored from __doc__
    """ dump_traceback(file=sys.stderr, all_threads=True): dump the traceback of the current thread, or of all threads if all_threads is True, into file """
    pass

def dump_traceback_later(timeout, repeat=False, file=None, exit=False): # real signature unknown; restored from __doc__
    """
    dump_traceback_later(timeout, repeat=False, file=sys.stderrn, exit=False):
    dump the traceback of all threads in timeout seconds,
    or each timeout seconds if repeat is True. If exit is True, call _exit(1) which is not safe.
    """
    pass

def enable(file=None, all_threads=True): # real signature unknown; restored from __doc__
    """ enable(file=sys.stderr, all_threads=True): enable the fault handler """
    pass

def is_enabled(): # real signature unknown; restored from __doc__
    """ is_enabled()->bool: check if the handler is enabled """
    return False

def register(signum, file=None, all_threads=True, chain=False): # real signature unknown; restored from __doc__
    """ register(signum, file=sys.stderr, all_threads=True, chain=False): register a handler for the signal 'signum': dump the traceback of the current thread, or of all threads if all_threads is True, into file """
    pass

def unregister(signum): # real signature unknown; restored from __doc__
    """ unregister(signum): unregister the handler of the signal 'signum' registered by register() """
    pass

def _fatal_error(message): # real signature unknown; restored from __doc__
    """ _fatal_error(message): call Py_FatalError(message) """
    pass

def _fatal_error_c_thread(*args, **kwargs): # real signature unknown
    """ fatal_error_c_thread(): call Py_FatalError() in a new C thread. """
    pass

def _read_null(): # real signature unknown; restored from __doc__
    """ _read_null(): read from NULL, raise a SIGSEGV or SIGBUS signal depending on the platform """
    pass

def _sigabrt(): # real signature unknown; restored from __doc__
    """ _sigabrt(): raise a SIGABRT signal """
    pass

def _sigfpe(): # real signature unknown; restored from __doc__
    """ _sigfpe(): raise a SIGFPE signal """
    pass

def _sigsegv(release_gil=False): # real signature unknown; restored from __doc__
    """ _sigsegv(release_gil=False): raise a SIGSEGV signal """
    pass

def _stack_overflow(): # real signature unknown; restored from __doc__
    """ _stack_overflow(): recursive call to raise a stack overflow """
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

__spec__ = None # (!) real value is "ModuleSpec(name='faulthandler', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

