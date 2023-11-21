# encoding: utf-8
# module _signal
# from (built-in)
# by generator 1.147
"""
This module provides mechanisms to use signal handlers in Python.

Functions:

alarm() -- cause SIGALRM after a specified time [Unix only]
setitimer() -- cause a signal (described below) after a specified
               float time and the timer may restart then [Unix only]
getitimer() -- get current value of timer [Unix only]
signal() -- set the action for a given signal
getsignal() -- get the signal action for a given signal
pause() -- wait until a signal arrives [Unix only]
default_int_handler() -- default SIGINT handler

signal constants:
SIG_DFL -- used to refer to the system default handler
SIG_IGN -- used to ignore the signal
NSIG -- number of defined signals
SIGINT, SIGTERM, etc. -- signal numbers

itimer constants:
ITIMER_REAL -- decrements in real time, and delivers SIGALRM upon
               expiration
ITIMER_VIRTUAL -- decrements only when the process is executing,
               and delivers SIGVTALRM upon expiration
ITIMER_PROF -- decrements both when the process is executing and
               when the system is executing on behalf of the process.
               Coupled with ITIMER_VIRTUAL, this timer is usually
               used to profile the time spent by the application
               in user and kernel space. SIGPROF is delivered upon
               expiration.


*** IMPORTANT NOTICE ***
A signal handler function is called with two arguments:
the first is the signal number, the second is the interrupted stack frame.
"""
# no imports

# Variables with simple values

ITIMER_PROF = 2
ITIMER_REAL = 0
ITIMER_VIRTUAL = 1

NSIG = 65

SIGABRT = 6
SIGALRM = 14
SIGBUS = 7
SIGCHLD = 17
SIGCLD = 17
SIGCONT = 18
SIGFPE = 8
SIGHUP = 1
SIGILL = 4
SIGINT = 2
SIGIO = 29
SIGIOT = 6
SIGKILL = 9
SIGPIPE = 13
SIGPOLL = 29
SIGPROF = 27
SIGPWR = 30
SIGQUIT = 3
SIGRTMAX = 64
SIGRTMIN = 34
SIGSEGV = 11
SIGSTOP = 19
SIGSYS = 31
SIGTERM = 15
SIGTRAP = 5
SIGTSTP = 20
SIGTTIN = 21
SIGTTOU = 22
SIGURG = 23
SIGUSR1 = 10
SIGUSR2 = 12
SIGVTALRM = 26
SIGWINCH = 28
SIGXCPU = 24
SIGXFSZ = 25

SIG_BLOCK = 0
SIG_DFL = 0
SIG_IGN = 1
SIG_SETMASK = 2
SIG_UNBLOCK = 1

# functions

def alarm(*args, **kwargs): # real signature unknown
    """ Arrange for SIGALRM to arrive after the given number of seconds. """
    pass

def default_int_handler(*more): # real signature unknown; restored from __doc__
    """
    default_int_handler(...)
    
    The default handler for SIGINT installed by Python.
    It raises KeyboardInterrupt.
    """
    pass

def getitimer(*args, **kwargs): # real signature unknown
    """ Returns current value of given itimer. """
    pass

def getsignal(*args, **kwargs): # real signature unknown
    """
    Return the current action for the given signal.
    
    The return value can be:
      SIG_IGN -- if the signal is being ignored
      SIG_DFL -- if the default action for the signal is in effect
      None    -- if an unknown handler is in effect
      anything else -- the callable Python object used as a handler
    """
    pass

def pause(*args, **kwargs): # real signature unknown
    """ Wait until a signal arrives. """
    pass

def pthread_kill(*args, **kwargs): # real signature unknown
    """ Send a signal to a thread. """
    pass

def pthread_sigmask(*args, **kwargs): # real signature unknown
    """ Fetch and/or change the signal mask of the calling thread. """
    pass

def raise_signal(*args, **kwargs): # real signature unknown
    """ Send a signal to the executing process. """
    pass

def setitimer(*args, **kwargs): # real signature unknown
    """
    Sets given itimer (one of ITIMER_REAL, ITIMER_VIRTUAL or ITIMER_PROF).
    
    The timer will fire after value seconds and after that every interval seconds.
    The itimer can be cleared by setting seconds to zero.
    
    Returns old values as a tuple: (delay, interval).
    """
    pass

def set_wakeup_fd(fd, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    set_wakeup_fd(fd, *, warn_on_full_buffer=True) -> fd
    
    Sets the fd to be written to (with the signal number) when a signal
    comes in.  A library can use this to wakeup select or poll.
    The previous fd or -1 is returned.
    
    The fd must be non-blocking.
    """
    pass

def siginterrupt(*args, **kwargs): # real signature unknown
    """
    Change system call restart behaviour.
    
    If flag is False, system calls will be restarted when interrupted by
    signal sig, else system calls will be interrupted.
    """
    pass

def signal(): # real signature unknown; restored from __doc__
    """
    Set the action for the given signal.
    
    The action can be SIG_DFL, SIG_IGN, or a callable Python object.
    The previous action is returned.  See getsignal() for possible return values.
    
    *** IMPORTANT NOTICE ***
    A signal handler function is called with two arguments:
    the first is the signal number, the second is the interrupted stack frame.
    """
    pass

def sigpending(*args, **kwargs): # real signature unknown
    """
    Examine pending signals.
    
    Returns a set of signal numbers that are pending for delivery to
    the calling thread.
    """
    pass

def sigtimedwait(*args, **kwargs): # real signature unknown
    """
    Like sigwaitinfo(), but with a timeout.
    
    The timeout is specified in seconds, with floating point numbers allowed.
    """
    pass

def sigwait(*args, **kwargs): # real signature unknown
    """
    Wait for a signal.
    
    Suspend execution of the calling thread until the delivery of one of the
    signals specified in the signal set sigset.  The function accepts the signal
    and returns the signal number.
    """
    pass

def sigwaitinfo(*args, **kwargs): # real signature unknown
    """
    Wait synchronously until one of the signals in *sigset* is delivered.
    
    Returns a struct_siginfo containing information about the signal.
    """
    pass

def strsignal(*args, **kwargs): # real signature unknown
    """
    Return the system description of the given signal.
    
    The return values can be such as "Interrupt", "Segmentation fault", etc.
    Returns None if the signal is not recognized.
    """
    pass

def valid_signals(*args, **kwargs): # real signature unknown
    """
    Return a set of valid signal numbers on this platform.
    
    The signal numbers returned by this function can be safely passed to
    functions like `pthread_sigmask`.
    """
    pass

# classes

class ItimerError(OSError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class struct_siginfo(tuple):
    """
    struct_siginfo: Result from sigwaitinfo or sigtimedwait.
    
    This object may be accessed either as a tuple of
    (si_signo, si_code, si_errno, si_pid, si_uid, si_status, si_band),
    or via the attributes si_signo, si_code, and so on.
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

    si_band = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """band event for SIGPOLL"""

    si_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """signal code"""

    si_errno = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """errno associated with this signal"""

    si_pid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """sending process ID"""

    si_signo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """signal number"""

    si_status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """exit value or signal"""

    si_uid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """real user ID of sending process"""


    n_fields = 7
    n_sequence_fields = 7
    n_unnamed_fields = 0


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

__spec__ = None # (!) real value is "ModuleSpec(name='_signal', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

