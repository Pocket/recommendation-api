# encoding: utf-8
# module _stat
# from (built-in)
# by generator 1.147
"""
S_IFMT_: file type bits
S_IFDIR: directory
S_IFCHR: character device
S_IFBLK: block device
S_IFREG: regular file
S_IFIFO: fifo (named pipe)
S_IFLNK: symbolic link
S_IFSOCK: socket file
S_IFDOOR: door
S_IFPORT: event port
S_IFWHT: whiteout

S_ISUID: set UID bit
S_ISGID: set GID bit
S_ENFMT: file locking enforcement
S_ISVTX: sticky bit
S_IREAD: Unix V7 synonym for S_IRUSR
S_IWRITE: Unix V7 synonym for S_IWUSR
S_IEXEC: Unix V7 synonym for S_IXUSR
S_IRWXU: mask for owner permissions
S_IRUSR: read by owner
S_IWUSR: write by owner
S_IXUSR: execute by owner
S_IRWXG: mask for group permissions
S_IRGRP: read by group
S_IWGRP: write by group
S_IXGRP: execute by group
S_IRWXO: mask for others (not in group) permissions
S_IROTH: read by others
S_IWOTH: write by others
S_IXOTH: execute by others

UF_NODUMP: do not dump file
UF_IMMUTABLE: file may not be changed
UF_APPEND: file may only be appended to
UF_OPAQUE: directory is opaque when viewed through a union stack
UF_NOUNLINK: file may not be renamed or deleted
UF_COMPRESSED: OS X: file is hfs-compressed
UF_HIDDEN: OS X: file should not be displayed
SF_ARCHIVED: file may be archived
SF_IMMUTABLE: file may not be changed
SF_APPEND: file may only be appended to
SF_NOUNLINK: file may not be renamed or deleted
SF_SNAPSHOT: file is a snapshot file

ST_MODE
ST_INO
ST_DEV
ST_NLINK
ST_UID
ST_GID
ST_SIZE
ST_ATIME
ST_MTIME
ST_CTIME

FILE_ATTRIBUTE_*: Windows file attribute constants
                   (only present on Windows)
"""
# no imports

# Variables with simple values

SF_APPEND = 262144
SF_ARCHIVED = 65536
SF_IMMUTABLE = 131072
SF_NOUNLINK = 1048576
SF_SNAPSHOT = 2097152

ST_ATIME = 7
ST_CTIME = 9
ST_DEV = 2
ST_GID = 5
ST_INO = 1
ST_MODE = 0
ST_MTIME = 8
ST_NLINK = 3
ST_SIZE = 6
ST_UID = 4

S_ENFMT = 1024
S_IEXEC = 64
S_IFBLK = 24576
S_IFCHR = 8192
S_IFDIR = 16384
S_IFDOOR = 0
S_IFIFO = 4096
S_IFLNK = 40960
S_IFPORT = 0
S_IFREG = 32768
S_IFSOCK = 49152
S_IFWHT = 0
S_IREAD = 256
S_IRGRP = 32
S_IROTH = 4
S_IRUSR = 256
S_IRWXG = 56
S_IRWXO = 7
S_IRWXU = 448
S_ISGID = 1024
S_ISUID = 2048
S_ISVTX = 512
S_IWGRP = 16
S_IWOTH = 2
S_IWRITE = 128
S_IWUSR = 128
S_IXGRP = 8
S_IXOTH = 1
S_IXUSR = 64

UF_APPEND = 4
UF_COMPRESSED = 32
UF_HIDDEN = 32768
UF_IMMUTABLE = 2
UF_NODUMP = 1
UF_NOUNLINK = 16
UF_OPAQUE = 8

# functions

def filemode(*args, **kwargs): # real signature unknown
    """ Convert a file's mode to a string of the form '-rwxrwxrwx' """
    pass

def S_IFMT(*args, **kwargs): # real signature unknown
    """ Return the portion of the file's mode that describes the file type. """
    pass

def S_IMODE(*args, **kwargs): # real signature unknown
    """ Return the portion of the file's mode that can be set by os.chmod(). """
    pass

def S_ISBLK(mode): # real signature unknown; restored from __doc__
    """
    S_ISBLK(mode) -> bool
    
    Return True if mode is from a block special device file.
    """
    return False

def S_ISCHR(mode): # real signature unknown; restored from __doc__
    """
    S_ISCHR(mode) -> bool
    
    Return True if mode is from a character special device file.
    """
    return False

def S_ISDIR(mode): # real signature unknown; restored from __doc__
    """
    S_ISDIR(mode) -> bool
    
    Return True if mode is from a directory.
    """
    return False

def S_ISDOOR(mode): # real signature unknown; restored from __doc__
    """
    S_ISDOOR(mode) -> bool
    
    Return True if mode is from a door.
    """
    return False

def S_ISFIFO(mode): # real signature unknown; restored from __doc__
    """
    S_ISFIFO(mode) -> bool
    
    Return True if mode is from a FIFO (named pipe).
    """
    return False

def S_ISLNK(mode): # real signature unknown; restored from __doc__
    """
    S_ISLNK(mode) -> bool
    
    Return True if mode is from a symbolic link.
    """
    return False

def S_ISPORT(mode): # real signature unknown; restored from __doc__
    """
    S_ISPORT(mode) -> bool
    
    Return True if mode is from an event port.
    """
    return False

def S_ISREG(mode): # real signature unknown; restored from __doc__
    """
    S_ISREG(mode) -> bool
    
    Return True if mode is from a regular file.
    """
    return False

def S_ISSOCK(mode): # real signature unknown; restored from __doc__
    """
    S_ISSOCK(mode) -> bool
    
    Return True if mode is from a socket.
    """
    return False

def S_ISWHT(mode): # real signature unknown; restored from __doc__
    """
    S_ISWHT(mode) -> bool
    
    Return True if mode is from a whiteout.
    """
    return False

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

__spec__ = None # (!) real value is "ModuleSpec(name='_stat', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

