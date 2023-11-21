# encoding: utf-8
# module _asyncio
# from /usr/local/lib/python3.8/lib-dynload/_asyncio.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
""" Accelerator module for asyncio """
# no imports

# functions

def get_event_loop(): # real signature unknown; restored from __doc__
    """
    Return an asyncio event loop.
    
    When called from a coroutine or a callback (e.g. scheduled with
    call_soon or similar API), this function will always return the
    running event loop.
    
    If there is no running event loop set, the function will return
    the result of `get_event_loop_policy().get_event_loop()` call.
    """
    pass

def get_running_loop(*args, **kwargs): # real signature unknown
    """
    Return the running event loop.  Raise a RuntimeError if there is none.
    
    This function is thread-specific.
    """
    pass

def _enter_task(*args, **kwargs): # real signature unknown
    """
    Enter into task execution or resume suspended task.
    
    Task belongs to loop.
    
    Returns None.
    """
    pass

def _get_running_loop(*args, **kwargs): # real signature unknown
    """
    Return the running event loop or None.
    
    This is a low-level function intended to be used by event loops.
    This function is thread-specific.
    """
    pass

def _leave_task(*args, **kwargs): # real signature unknown
    """
    Leave task execution or suspend a task.
    
    Task belongs to loop.
    
    Returns None.
    """
    pass

def _register_task(*args, **kwargs): # real signature unknown
    """
    Register a new task in asyncio as executed by loop.
    
    Returns None.
    """
    pass

def _set_running_loop(*args, **kwargs): # real signature unknown
    """
    Set the running event loop.
    
    This is a low-level function intended to be used by event loops.
    This function is thread-specific.
    """
    pass

def _unregister_task(*args, **kwargs): # real signature unknown
    """
    Unregister a task.
    
    Returns None.
    """
    pass

# classes

class Future(object):
    """
    This class is *almost* compatible with concurrent.futures.Future.
    
        Differences:
    
        - result() and exception() do not take a timeout argument and
          raise an exception when the future isn't done yet.
    
        - Callbacks registered with add_done_callback() are always called
          via the event loop's call_soon_threadsafe().
    
        - This class is not compatible with the wait() and as_completed()
          methods in the concurrent.futures package.
    """
    def add_done_callback(self, *args, **kwargs): # real signature unknown
        """
        Add a callback to be run when the future becomes done.
        
        The callback is called with a single argument - the future object. If
        the future is already done when this is called, the callback is
        scheduled with call_soon.
        """
        pass

    def cancel(self, *args, **kwargs): # real signature unknown
        """
        Cancel the future and schedule callbacks.
        
        If the future is already done or cancelled, return False.  Otherwise,
        change the future's state to cancelled, schedule the callbacks and
        return True.
        """
        pass

    def cancelled(self, *args, **kwargs): # real signature unknown
        """ Return True if the future was cancelled. """
        pass

    def done(self, *args, **kwargs): # real signature unknown
        """
        Return True if the future is done.
        
        Done means either that a result / exception are available, or that the
        future was cancelled.
        """
        pass

    def exception(self, or_None_if_no_exception_was_set): # real signature unknown; restored from __doc__
        """
        Return the exception that was set on this future.
        
        The exception (or None if no exception was set) is returned only if
        the future is done.  If the future has been cancelled, raises
        CancelledError.  If the future isn't done yet, raises
        InvalidStateError.
        """
        pass

    def get_loop(self, *args, **kwargs): # real signature unknown
        """ Return the event loop the Future is bound to. """
        pass

    def remove_done_callback(self, *args, **kwargs): # real signature unknown
        """
        Remove all instances of a callback from the "call when done" list.
        
        Returns the number of callbacks removed.
        """
        pass

    def result(self, *args, **kwargs): # real signature unknown
        """
        Return the result this future represents.
        
        If the future has been cancelled, raises CancelledError.  If the
        future's result isn't yet available, raises InvalidStateError.  If
        the future is done and has an exception set, this exception is raised.
        """
        pass

    def set_exception(self, *args, **kwargs): # real signature unknown
        """
        Mark the future done and set an exception.
        
        If the future is already done when this method is called, raises
        InvalidStateError.
        """
        pass

    def set_result(self, *args, **kwargs): # real signature unknown
        """
        Mark the future done and set its result.
        
        If the future is already done when this method is called, raises
        InvalidStateError.
        """
        pass

    def _repr_info(self, *args, **kwargs): # real signature unknown
        pass

    def __await__(self, *args, **kwargs): # real signature unknown
        """ Return an iterator to be used in await expression. """
        pass

    def __del__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    _asyncio_future_blocking = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _callbacks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _exception = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _log_traceback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _loop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _source_traceback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Task(Future):
    """ A coroutine wrapped in a Future. """
    def add_done_callback(self, *args, **kwargs): # real signature unknown
        """
        Add a callback to be run when the future becomes done.
        
        The callback is called with a single argument - the future object. If
        the future is already done when this is called, the callback is
        scheduled with call_soon.
        """
        pass

    @classmethod
    def all_tasks(cls, *args, **kwargs): # real signature unknown
        """
        Return a set of all tasks for an event loop.
        
        By default all tasks for the current event loop are returned.
        """
        pass

    def cancel(self): # real signature unknown; restored from __doc__
        """
        Request that this task cancel itself.
        
        This arranges for a CancelledError to be thrown into the
        wrapped coroutine on the next cycle through the event loop.
        The coroutine then has a chance to clean up or even deny
        the request using try/except/finally.
        
        Unlike Future.cancel, this does not guarantee that the
        task will be cancelled: the exception might be caught and
        acted upon, delaying cancellation of the task or preventing
        cancellation completely.  The task may also return a value or
        raise a different exception.
        
        Immediately after this method is called, Task.cancelled() will
        not return True (unless the task was already cancelled).  A
        task will be marked as cancelled when the wrapped coroutine
        terminates with a CancelledError exception (even if cancel()
        was not called).
        """
        pass

    def cancelled(self, *args, **kwargs): # real signature unknown
        """ Return True if the future was cancelled. """
        pass

    @classmethod
    def current_task(cls, *args, **kwargs): # real signature unknown
        """
        Return the currently running task in an event loop or None.
        
        By default the current task for the current event loop is returned.
        
        None is returned when called not in the context of a Task.
        """
        pass

    def done(self, *args, **kwargs): # real signature unknown
        """
        Return True if the future is done.
        
        Done means either that a result / exception are available, or that the
        future was cancelled.
        """
        pass

    def exception(self, or_None_if_no_exception_was_set): # real signature unknown; restored from __doc__
        """
        Return the exception that was set on this future.
        
        The exception (or None if no exception was set) is returned only if
        the future is done.  If the future has been cancelled, raises
        CancelledError.  If the future isn't done yet, raises
        InvalidStateError.
        """
        pass

    def get_coro(self, *args, **kwargs): # real signature unknown
        pass

    def get_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_stack(self, *args, **kwargs): # real signature unknown
        """
        Return the list of stack frames for this task's coroutine.
        
        If the coroutine is not done, this returns the stack where it is
        suspended.  If the coroutine has completed successfully or was
        cancelled, this returns an empty list.  If the coroutine was
        terminated by an exception, this returns the list of traceback
        frames.
        
        The frames are always ordered from oldest to newest.
        
        The optional limit gives the maximum number of frames to
        return; by default all available frames are returned.  Its
        meaning differs depending on whether a stack or a traceback is
        returned: the newest frames of a stack are returned, but the
        oldest frames of a traceback are returned.  (This matches the
        behavior of the traceback module.)
        
        For reasons beyond our control, only one stack frame is
        returned for a suspended coroutine.
        """
        pass

    def print_stack(self, *args, **kwargs): # real signature unknown
        """
        Print the stack or traceback for this task's coroutine.
        
        This produces output similar to that of the traceback module,
        for the frames retrieved by get_stack().  The limit argument
        is passed to get_stack().  The file argument is an I/O stream
        to which the output is written; by default output is written
        to sys.stderr.
        """
        pass

    def remove_done_callback(self, *args, **kwargs): # real signature unknown
        """
        Remove all instances of a callback from the "call when done" list.
        
        Returns the number of callbacks removed.
        """
        pass

    def result(self, *args, **kwargs): # real signature unknown
        """
        Return the result this future represents.
        
        If the future has been cancelled, raises CancelledError.  If the
        future's result isn't yet available, raises InvalidStateError.  If
        the future is done and has an exception set, this exception is raised.
        """
        pass

    def set_exception(self, *args, **kwargs): # real signature unknown
        pass

    def set_name(self, *args, **kwargs): # real signature unknown
        pass

    def set_result(self, *args, **kwargs): # real signature unknown
        pass

    def _repr_info(self, *args, **kwargs): # real signature unknown
        pass

    def __await__(self, *args, **kwargs): # real signature unknown
        """ Return an iterator to be used in await expression. """
        pass

    def __del__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    _asyncio_future_blocking = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _callbacks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _coro = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _exception = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _fut_waiter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _log_destroy_pending = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _log_traceback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _loop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _must_cancel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _source_traceback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

_all_tasks = None # (!) real value is 'set()'

_current_tasks = {}

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924ac0>'

__spec__ = None # (!) real value is "ModuleSpec(name='_asyncio', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924ac0>, origin='/usr/local/lib/python3.8/lib-dynload/_asyncio.cpython-38-aarch64-linux-gnu.so')"

