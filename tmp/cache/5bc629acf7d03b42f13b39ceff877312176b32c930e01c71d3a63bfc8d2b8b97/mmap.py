# encoding: utf-8
# module mmap
# from /usr/local/lib/python3.8/lib-dynload/mmap.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

# Variables with simple values

ACCESS_COPY = 3
ACCESS_DEFAULT = 0
ACCESS_READ = 1
ACCESS_WRITE = 2

ALLOCATIONGRANULARITY = 4096

MADV_DODUMP = 17
MADV_DOFORK = 11
MADV_DONTDUMP = 16
MADV_DONTFORK = 10
MADV_DONTNEED = 4
MADV_FREE = 8
MADV_HUGEPAGE = 14
MADV_HWPOISON = 100
MADV_MERGEABLE = 12
MADV_NOHUGEPAGE = 15
MADV_NORMAL = 0
MADV_RANDOM = 1
MADV_REMOVE = 9
MADV_SEQUENTIAL = 2
MADV_UNMERGEABLE = 13
MADV_WILLNEED = 3

MAP_ANON = 32
MAP_ANONYMOUS = 32
MAP_DENYWRITE = 2048
MAP_EXECUTABLE = 4096
MAP_PRIVATE = 2
MAP_SHARED = 1

PAGESIZE = 4096

PROT_EXEC = 4
PROT_READ = 1
PROT_WRITE = 2

# no functions
# classes

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



class mmap(object):
    """
    Windows: mmap(fileno, length[, tagname[, access[, offset]]])
    
    Maps length bytes from the file specified by the file handle fileno,
    and returns a mmap object.  If length is larger than the current size
    of the file, the file is extended to contain length bytes.  If length
    is 0, the maximum length of the map is the current size of the file,
    except that if the file is empty Windows raises an exception (you cannot
    create an empty mapping on Windows).
    
    Unix: mmap(fileno, length[, flags[, prot[, access[, offset]]]])
    
    Maps length bytes from the file specified by the file descriptor fileno,
    and returns a mmap object.  If length is 0, the maximum length of the map
    will be the current size of the file when mmap is called.
    flags specifies the nature of the mapping. MAP_PRIVATE creates a
    private copy-on-write mapping, so changes to the contents of the mmap
    object will be private to this process, and MAP_SHARED creates a mapping
    that's shared with all other processes mapping the same areas of the file.
    The default value is MAP_SHARED.
    
    To map anonymous memory, pass -1 as the fileno (both versions).
    """
    def close(self, *args, **kwargs): # real signature unknown
        pass

    def find(self, *args, **kwargs): # real signature unknown
        pass

    def flush(self, *args, **kwargs): # real signature unknown
        pass

    def madvise(self, *args, **kwargs): # real signature unknown
        pass

    def move(self, *args, **kwargs): # real signature unknown
        pass

    def read(self, *args, **kwargs): # real signature unknown
        pass

    def readline(self, *args, **kwargs): # real signature unknown
        pass

    def read_byte(self, *args, **kwargs): # real signature unknown
        pass

    def resize(self, *args, **kwargs): # real signature unknown
        pass

    def rfind(self, *args, **kwargs): # real signature unknown
        pass

    def seek(self, *args, **kwargs): # real signature unknown
        pass

    def size(self, *args, **kwargs): # real signature unknown
        pass

    def tell(self, *args, **kwargs): # real signature unknown
        pass

    def write(self, *args, **kwargs): # real signature unknown
        pass

    def write_byte(self, *args, **kwargs): # real signature unknown
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __enter__(self, *args, **kwargs): # real signature unknown
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, fileno, length, tagname=None, access=None, offset=None): # real signature unknown; restored from __doc__
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924ac0>'

__spec__ = None # (!) real value is "ModuleSpec(name='mmap', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924ac0>, origin='/usr/local/lib/python3.8/lib-dynload/mmap.cpython-38-aarch64-linux-gnu.so')"

