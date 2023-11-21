# encoding: utf-8
# module select
# from /usr/local/lib/python3.8/lib-dynload/select.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
"""
This module supports asynchronous I/O on multiple file descriptors.

*** IMPORTANT NOTICE ***
On Windows, only sockets are supported; on Unix, all file descriptors.
"""
# no imports

# Variables with simple values

EPOLLERR = 8
EPOLLET = 2147483648
EPOLLEXCLUSIVE = 268435456
EPOLLHUP = 16
EPOLLIN = 1
EPOLLMSG = 1024
EPOLLONESHOT = 1073741824
EPOLLOUT = 4
EPOLLPRI = 2
EPOLLRDBAND = 128
EPOLLRDHUP = 8192
EPOLLRDNORM = 64
EPOLLWRBAND = 512
EPOLLWRNORM = 256

EPOLL_CLOEXEC = 524288

PIPE_BUF = 4096

POLLERR = 8
POLLHUP = 16
POLLIN = 1
POLLMSG = 1024
POLLNVAL = 32
POLLOUT = 4
POLLPRI = 2
POLLRDBAND = 128
POLLRDHUP = 8192
POLLRDNORM = 64
POLLWRBAND = 512
POLLWRNORM = 256

# functions

def poll(*args, **kwargs): # real signature unknown
    """
    Returns a polling object.
    
    This object supports registering and unregistering file descriptors, and then
    polling them for I/O events.
    """
    pass

def select(*args, **kwargs): # real signature unknown
    """
    Wait until one or more file descriptors are ready for some kind of I/O.
    
    The first three arguments are iterables of file descriptors to be waited for:
    rlist -- wait until ready for reading
    wlist -- wait until ready for writing
    xlist -- wait for an "exceptional condition"
    If only one kind of condition is required, pass [] for the other lists.
    
    A file descriptor is either a socket or file object, or a small integer
    gotten from a fileno() method call on one of those.
    
    The optional 4th argument specifies a timeout in seconds; it may be
    a floating point number to specify fractions of seconds.  If it is absent
    or None, the call will never time out.
    
    The return value is a tuple of three lists corresponding to the first three
    arguments; each contains the subset of the corresponding file descriptors
    that are ready.
    
    *** IMPORTANT NOTICE ***
    On Windows, only sockets are supported; on Unix, all file
    descriptors can be used.
    """
    pass

# classes

class epoll(object):
    """
    Returns an epolling object.
    
      sizehint
        The expected number of events to be registered.  It must be positive,
        or -1 to use the default.  It is only used on older systems where
        epoll_create1() is not available; otherwise it has no effect (though its
        value is still checked).
      flags
        Deprecated and completely ignored.  However, when supplied, its value
        must be 0 or select.EPOLL_CLOEXEC, otherwise OSError is raised.
    """
    def close(self, *args, **kwargs): # real signature unknown
        """
        Close the epoll control file descriptor.
        
        Further operations on the epoll object will raise an exception.
        """
        pass

    def fileno(self, *args, **kwargs): # real signature unknown
        """ Return the epoll control file descriptor. """
        pass

    @classmethod
    def fromfd(cls, *args, **kwargs): # real signature unknown
        """ Create an epoll object from a given control fd. """
        pass

    def modify(self, *args, **kwargs): # real signature unknown
        """
        Modify event mask for a registered file descriptor.
        
          fd
            the target file descriptor of the operation
          eventmask
            a bit set composed of the various EPOLL constants
        """
        pass

    def poll(self, *args, **kwargs): # real signature unknown
        """
        Wait for events on the epoll file descriptor.
        
          timeout
            the maximum time to wait in seconds (as float);
            a timeout of None or -1 makes poll wait indefinitely
          maxevents
            the maximum number of events returned; -1 means no limit
        
        Returns a list containing any descriptors that have events to report,
        as a list of (fd, events) 2-tuples.
        """
        pass

    def register(self, *args, **kwargs): # real signature unknown
        """
        Registers a new fd or raises an OSError if the fd is already registered.
        
          fd
            the target file descriptor of the operation
          eventmask
            a bit set composed of the various EPOLL constants
        
        The epoll interface supports all file descriptors that support poll.
        """
        pass

    def unregister(self, *args, **kwargs): # real signature unknown
        """
        Remove a registered file descriptor from the epoll object.
        
          fd
            the target file descriptor of the operation
        """
        pass

    def __enter__(self, *args, **kwargs): # real signature unknown
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
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

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the epoll handler is closed"""



class error(Exception):
    """ Base class for I/O related errors. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    characters_written = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    errno = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """POSIX exception code"""

    filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """exception filename"""

    filename2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """second exception filename"""

    strerror = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """exception strerror"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffffacc0d430>'

__spec__ = None # (!) real value is "ModuleSpec(name='select', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffffacc0d430>, origin='/usr/local/lib/python3.8/lib-dynload/select.cpython-38-aarch64-linux-gnu.so')"

