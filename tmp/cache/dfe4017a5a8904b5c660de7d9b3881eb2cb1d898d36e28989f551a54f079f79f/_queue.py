# encoding: utf-8
# module _queue
# from /usr/local/lib/python3.8/lib-dynload/_queue.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
"""
C implementation of the Python queue module.
This module is an implementation detail, please do not use it directly.
"""
# no imports

# no functions
# classes

class Empty(Exception):
    """ Exception raised by Queue.get(block=0)/get_nowait(). """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class SimpleQueue(object):
    """ Simple, unbounded, reentrant FIFO queue. """
    def empty(self, *args, **kwargs): # real signature unknown
        """ Return True if the queue is empty, False otherwise (not reliable!). """
        pass

    def get(self, *args, **kwargs): # real signature unknown
        """
        Remove and return an item from the queue.
        
        If optional args 'block' is true and 'timeout' is None (the default),
        block if necessary until an item is available. If 'timeout' is
        a non-negative number, it blocks at most 'timeout' seconds and raises
        the Empty exception if no item was available within that time.
        Otherwise ('block' is false), return an item if one is immediately
        available, else raise the Empty exception ('timeout' is ignored
        in that case).
        """
        pass

    def get_nowait(self, *args, **kwargs): # real signature unknown
        """
        Remove and return an item from the queue without blocking.
        
        Only get an item if one is immediately available. Otherwise
        raise the Empty exception.
        """
        pass

    def put(self, *args, **kwargs): # real signature unknown
        """
        Put the item on the queue.
        
        The optional 'block' and 'timeout' arguments are ignored, as this method
        never blocks.  They are provided for compatibility with the Queue class.
        """
        pass

    def put_nowait(self, *args, **kwargs): # real signature unknown
        """
        Put an item into the queue without blocking.
        
        This is exactly equivalent to `put(item)` and is only provided
        for compatibility with the Queue class.
        """
        pass

    def qsize(self, *args, **kwargs): # real signature unknown
        """ Return the approximate size of the queue (not reliable!). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924ac0>'

__spec__ = None # (!) real value is "ModuleSpec(name='_queue', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924ac0>, origin='/usr/local/lib/python3.8/lib-dynload/_queue.cpython-38-aarch64-linux-gnu.so')"

