# encoding: utf-8
# module _thread
# from (built-in)
# by generator 1.147
"""
This module provides primitive operations to write multi-threaded programs.
The 'threading' module provides a more convenient interface.
"""
# no imports

# Variables with simple values

TIMEOUT_MAX = 9223372036.0

# functions

def allocate(): # real signature unknown; restored from __doc__
    """
    allocate_lock() -> lock object
    (allocate() is an obsolete synonym)
    
    Create a new lock object. See help(type(threading.Lock())) for
    information about locks.
    """
    pass

def allocate_lock(): # real signature unknown; restored from __doc__
    """
    allocate_lock() -> lock object
    (allocate() is an obsolete synonym)
    
    Create a new lock object. See help(type(threading.Lock())) for
    information about locks.
    """
    pass

def exit(): # real signature unknown; restored from __doc__
    """
    exit()
    (exit_thread() is an obsolete synonym)
    
    This is synonymous to ``raise SystemExit''.  It will cause the current
    thread to exit silently unless the exception is caught.
    """
    pass

def exit_thread(): # real signature unknown; restored from __doc__
    """
    exit()
    (exit_thread() is an obsolete synonym)
    
    This is synonymous to ``raise SystemExit''.  It will cause the current
    thread to exit silently unless the exception is caught.
    """
    pass

def get_ident(): # real signature unknown; restored from __doc__
    """
    get_ident() -> integer
    
    Return a non-zero integer that uniquely identifies the current thread
    amongst other threads that exist simultaneously.
    This may be used to identify per-thread resources.
    Even though on some platforms threads identities may appear to be
    allocated consecutive numbers starting at 1, this behavior should not
    be relied upon, and the number should be seen purely as a magic cookie.
    A thread's identity may be reused for another thread after it exits.
    """
    return 0

def get_native_id(): # real signature unknown; restored from __doc__
    """
    get_native_id() -> integer
    
    Return a non-negative integer identifying the thread as reported
    by the OS (kernel). This may be used to uniquely identify a
    particular thread within a system.
    """
    return 0

def interrupt_main(): # real signature unknown; restored from __doc__
    """
    interrupt_main()
    
    Raise a KeyboardInterrupt in the main thread.
    A subthread can use this function to interrupt the main thread.
    """
    pass

def stack_size(size=None): # real signature unknown; restored from __doc__
    """
    stack_size([size]) -> size
    
    Return the thread stack size used when creating new threads.  The
    optional size argument specifies the stack size (in bytes) to be used
    for subsequently created threads, and must be 0 (use platform or
    configured default) or a positive integer value of at least 32,768 (32k).
    If changing the thread stack size is unsupported, a ThreadError
    exception is raised.  If the specified size is invalid, a ValueError
    exception is raised, and the stack size is unmodified.  32k bytes
     currently the minimum supported stack size value to guarantee
    sufficient stack space for the interpreter itself.
    
    Note that some platforms may have particular restrictions on values for
    the stack size, such as requiring a minimum stack size larger than 32 KiB or
    requiring allocation in multiples of the system memory page size
    - platform documentation should be referred to for more information
    (4 KiB pages are common; using multiples of 4096 for the stack size is
    the suggested approach in the absence of more specific information).
    """
    pass

def start_new(function, args, kwargs=None): # known case of _thread.start_new
    """
    start_new_thread(function, args[, kwargs])
    (start_new() is an obsolete synonym)
    
    Start a new thread and return its identifier.  The thread will call the
    function with positional arguments from the tuple args and keyword arguments
    taken from the optional dictionary kwargs.  The thread exits when the
    function returns; the return value is ignored.  The thread will also exit
    when the function raises an unhandled exception; a stack trace will be
    printed unless the exception is SystemExit.
    """
    return 0

def start_new_thread(function, args, kwargs=None): # real signature unknown; restored from __doc__
    """
    start_new_thread(function, args[, kwargs])
    (start_new() is an obsolete synonym)
    
    Start a new thread and return its identifier.  The thread will call the
    function with positional arguments from the tuple args and keyword arguments
    taken from the optional dictionary kwargs.  The thread exits when the
    function returns; the return value is ignored.  The thread will also exit
    when the function raises an unhandled exception; a stack trace will be
    printed unless the exception is SystemExit.
    """
    pass

def _count(): # real signature unknown; restored from __doc__
    """
    _count() -> integer
    
    Return the number of currently running Python threads, excluding
    the main thread. The returned number comprises all threads created
    through `start_new_thread()` as well as `threading.Thread`, and not
    yet finished.
    
    This function is meant for internal and specialized purposes only.
    In most applications `threading.enumerate()` should be used instead.
    """
    return 0

def _excepthook(*args, **kwargs): # real signature unknown
    """
    excepthook(exc_type, exc_value, exc_traceback, thread)
    
    Handle uncaught Thread.run() exception.
    """
    pass

def _set_sentinel(): # real signature unknown; restored from __doc__
    """
    _set_sentinel() -> lock
    
    Set a sentinel lock that will be released when the current thread
    state is finalized (after it is untied from the interpreter).
    
    This is a private API for the threading module.
    """
    pass

# classes

class error(Exception):
    """ Unspecified run-time error. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class LockType(object):
    """
    A lock object is a synchronization primitive.  To create a lock,
    call threading.Lock().  Methods are:
    
    acquire() -- lock the lock, possibly blocking until it can be obtained
    release() -- unlock of the lock
    locked() -- test whether the lock is currently locked
    
    A lock is not owned by the thread that locked it; another thread may
    unlock it.  A thread attempting to lock a lock that it has already locked
    will block until another thread unlocks it.  Deadlocks may ensue.
    """
    def acquire(self, blocking=True, timeout=-1): # real signature unknown; restored from __doc__
        """
        acquire(blocking=True, timeout=-1) -> bool
        (acquire_lock() is an obsolete synonym)
        
        Lock the lock.  Without argument, this blocks if the lock is already
        locked (even by the same thread), waiting for another thread to release
        the lock, and return True once the lock is acquired.
        With an argument, this will only block if the argument is true,
        and the return value reflects whether the lock is acquired.
        The blocking operation is interruptible.
        """
        return False

    def acquire_lock(self): # real signature unknown; restored from __doc__
        """
        acquire(blocking=True, timeout=-1) -> bool
        (acquire_lock() is an obsolete synonym)
        
        Lock the lock.  Without argument, this blocks if the lock is already
        locked (even by the same thread), waiting for another thread to release
        the lock, and return True once the lock is acquired.
        With an argument, this will only block if the argument is true,
        and the return value reflects whether the lock is acquired.
        The blocking operation is interruptible.
        """
        pass

    def locked(self): # real signature unknown; restored from __doc__
        """
        locked() -> bool
        (locked_lock() is an obsolete synonym)
        
        Return whether the lock is in the locked state.
        """
        return False

    def locked_lock(self): # real signature unknown; restored from __doc__
        """
        locked() -> bool
        (locked_lock() is an obsolete synonym)
        
        Return whether the lock is in the locked state.
        """
        pass

    def release(self): # real signature unknown; restored from __doc__
        """
        release()
        (release_lock() is an obsolete synonym)
        
        Release the lock, allowing another thread that is blocked waiting for
        the lock to acquire the lock.  The lock must be in the locked state,
        but it needn't be locked by the same thread that unlocks it.
        """
        pass

    def release_lock(self): # real signature unknown; restored from __doc__
        """
        release()
        (release_lock() is an obsolete synonym)
        
        Release the lock, allowing another thread that is blocked waiting for
        the lock to acquire the lock.  The lock must be in the locked state,
        but it needn't be locked by the same thread that unlocks it.
        """
        pass

    def __enter__(self, *args, **kwargs): # real signature unknown
        """
        acquire(blocking=True, timeout=-1) -> bool
        (acquire_lock() is an obsolete synonym)
        
        Lock the lock.  Without argument, this blocks if the lock is already
        locked (even by the same thread), waiting for another thread to release
        the lock, and return True once the lock is acquired.
        With an argument, this will only block if the argument is true,
        and the return value reflects whether the lock is acquired.
        The blocking operation is interruptible.
        """
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        """
        release()
        (release_lock() is an obsolete synonym)
        
        Release the lock, allowing another thread that is blocked waiting for
        the lock to acquire the lock.  The lock must be in the locked state,
        but it needn't be locked by the same thread that unlocks it.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass


class RLock(object):
    # no doc
    def acquire(self, blocking=True): # real signature unknown; restored from __doc__
        """
        acquire(blocking=True) -> bool
        
        Lock the lock.  `blocking` indicates whether we should wait
        for the lock to be available or not.  If `blocking` is False
        and another thread holds the lock, the method will return False
        immediately.  If `blocking` is True and another thread holds
        the lock, the method will wait for the lock to be released,
        take it and then return True.
        (note: the blocking operation is interruptible.)
        
        In all other cases, the method will return True immediately.
        Precisely, if the current thread already holds the lock, its
        internal counter is simply incremented. If nobody holds the lock,
        the lock is taken and its internal counter initialized to 1.
        """
        return False

    def release(self): # real signature unknown; restored from __doc__
        """
        release()
        
        Release the lock, allowing another thread that is blocked waiting for
        the lock to acquire the lock.  The lock must be in the locked state,
        and must be locked by the same thread that unlocks it; otherwise a
        `RuntimeError` is raised.
        
        Do note that if the lock was acquire()d several times in a row by the
        current thread, release() needs to be called as many times for the lock
        to be available for other threads.
        """
        pass

    def _acquire_restore(self, state): # real signature unknown; restored from __doc__
        """
        _acquire_restore(state) -> None
        
        For internal use by `threading.Condition`.
        """
        pass

    def _is_owned(self): # real signature unknown; restored from __doc__
        """
        _is_owned() -> bool
        
        For internal use by `threading.Condition`.
        """
        return False

    def _release_save(self): # real signature unknown; restored from __doc__
        """
        _release_save() -> tuple
        
        For internal use by `threading.Condition`.
        """
        return ()

    def __enter__(self, *args, **kwargs): # real signature unknown
        """
        acquire(blocking=True) -> bool
        
        Lock the lock.  `blocking` indicates whether we should wait
        for the lock to be available or not.  If `blocking` is False
        and another thread holds the lock, the method will return False
        immediately.  If `blocking` is True and another thread holds
        the lock, the method will wait for the lock to be released,
        take it and then return True.
        (note: the blocking operation is interruptible.)
        
        In all other cases, the method will return True immediately.
        Precisely, if the current thread already holds the lock, its
        internal counter is simply incremented. If nobody holds the lock,
        the lock is taken and its internal counter initialized to 1.
        """
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        """
        release()
        
        Release the lock, allowing another thread that is blocked waiting for
        the lock to acquire the lock.  The lock must be in the locked state,
        and must be locked by the same thread that unlocks it; otherwise a
        `RuntimeError` is raised.
        
        Do note that if the lock was acquire()d several times in a row by the
        current thread, release() needs to be called as many times for the lock
        to be available for other threads.
        """
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


class _ExceptHookArgs(tuple):
    """
    ExceptHookArgs
    
    Type used to pass arguments to threading.excepthook.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    exc_traceback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Exception traceback"""

    exc_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Exception type"""

    exc_value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Exception value"""

    thread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Thread"""


    n_fields = 4
    n_sequence_fields = 4
    n_unnamed_fields = 0


class _local(object):
    """ Thread-local data """
    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass


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

__spec__ = None # (!) real value is "ModuleSpec(name='_thread', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

