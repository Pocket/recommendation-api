# encoding: utf-8
# module posix
# from (built-in)
# by generator 1.147
"""
This module provides access to operating system functionality that is
standardized by the C Standard and the POSIX standard (a thinly
disguised Unix interface).  Refer to the library manual and
corresponding Unix manual entries for more information on calls.
"""
# no imports

# Variables with simple values

CLD_CONTINUED = 6
CLD_DUMPED = 3
CLD_EXITED = 1
CLD_TRAPPED = 4

EX_CANTCREAT = 73
EX_CONFIG = 78
EX_DATAERR = 65
EX_IOERR = 74
EX_NOHOST = 68
EX_NOINPUT = 66
EX_NOPERM = 77
EX_NOUSER = 67
EX_OK = 0
EX_OSERR = 71
EX_OSFILE = 72
EX_PROTOCOL = 76
EX_SOFTWARE = 70
EX_TEMPFAIL = 75
EX_UNAVAILABLE = 69
EX_USAGE = 64

F_LOCK = 1
F_OK = 0
F_TEST = 3
F_TLOCK = 2
F_ULOCK = 0

GRND_NONBLOCK = 1
GRND_RANDOM = 2

MFD_ALLOW_SEALING = 2

MFD_CLOEXEC = 1
MFD_HUGETLB = 4

MFD_HUGE_16GB = 2281701376
MFD_HUGE_16MB = 1610612736
MFD_HUGE_1GB = 2013265920
MFD_HUGE_1MB = 1342177280
MFD_HUGE_256MB = 1879048192
MFD_HUGE_2GB = 2080374784
MFD_HUGE_2MB = 1409286144
MFD_HUGE_32MB = 1677721600
MFD_HUGE_512KB = 1275068416
MFD_HUGE_512MB = 1946157056
MFD_HUGE_64KB = 1073741824
MFD_HUGE_8MB = 1543503872
MFD_HUGE_MASK = 63
MFD_HUGE_SHIFT = 26

NGROUPS_MAX = 65536

O_ACCMODE = 3
O_APPEND = 1024
O_ASYNC = 8192
O_CLOEXEC = 524288
O_CREAT = 64
O_DIRECT = 65536
O_DIRECTORY = 16384
O_DSYNC = 4096
O_EXCL = 128
O_LARGEFILE = 0
O_NDELAY = 2048
O_NOATIME = 262144
O_NOCTTY = 256
O_NOFOLLOW = 32768
O_NONBLOCK = 2048
O_PATH = 2097152
O_RDONLY = 0
O_RDWR = 2
O_RSYNC = 1052672
O_SYNC = 1052672
O_TMPFILE = 4210688
O_TRUNC = 512
O_WRONLY = 1

POSIX_FADV_DONTNEED = 4
POSIX_FADV_NOREUSE = 5
POSIX_FADV_NORMAL = 0
POSIX_FADV_RANDOM = 1
POSIX_FADV_SEQUENTIAL = 2
POSIX_FADV_WILLNEED = 3

POSIX_SPAWN_CLOSE = 1
POSIX_SPAWN_DUP2 = 2
POSIX_SPAWN_OPEN = 0

PRIO_PGRP = 1
PRIO_PROCESS = 0
PRIO_USER = 2

P_ALL = 0
P_PGID = 2
P_PID = 1

RTLD_DEEPBIND = 8
RTLD_GLOBAL = 256
RTLD_LAZY = 1
RTLD_LOCAL = 0
RTLD_NODELETE = 4096
RTLD_NOLOAD = 4
RTLD_NOW = 2

RWF_DSYNC = 2
RWF_HIPRI = 1
RWF_NOWAIT = 8
RWF_SYNC = 4

R_OK = 4

SCHED_BATCH = 3
SCHED_FIFO = 1
SCHED_IDLE = 5
SCHED_OTHER = 0

SCHED_RESET_ON_FORK = 1073741824

SCHED_RR = 2

SEEK_DATA = 3
SEEK_HOLE = 4

ST_APPEND = 256
ST_MANDLOCK = 64
ST_NOATIME = 1024
ST_NODEV = 4
ST_NODIRATIME = 2048
ST_NOEXEC = 8
ST_NOSUID = 2
ST_RDONLY = 1
ST_RELATIME = 4096
ST_SYNCHRONOUS = 16
ST_WRITE = 128

TMP_MAX = 238328

WCONTINUED = 8

WEXITED = 4

WNOHANG = 1
WNOWAIT = 16777216

WSTOPPED = 2

WUNTRACED = 2

W_OK = 2

XATTR_CREATE = 1
XATTR_REPLACE = 2

XATTR_SIZE_MAX = 65536

X_OK = 1

# functions

def abort(*args, **kwargs): # real signature unknown
    """
    Abort the interpreter immediately.
    
    This function 'dumps core' or otherwise fails in the hardest way possible
    on the hosting operating system.  This function never returns.
    """
    pass

def access(*args, **kwargs): # real signature unknown
    """
    Use the real uid/gid to test for access to a path.
    
      path
        Path to be tested; can be string, bytes, or a path-like object.
      mode
        Operating-system mode bitfield.  Can be F_OK to test existence,
        or the inclusive-OR of R_OK, W_OK, and X_OK.
      dir_fd
        If not None, it should be a file descriptor open to a directory,
        and path should be relative; path will then be relative to that
        directory.
      effective_ids
        If True, access will use the effective uid/gid instead of
        the real uid/gid.
      follow_symlinks
        If False, and the last element of the path is a symbolic link,
        access will examine the symbolic link itself instead of the file
        the link points to.
    
    dir_fd, effective_ids, and follow_symlinks may not be implemented
      on your platform.  If they are unavailable, using them will raise a
      NotImplementedError.
    
    Note that most operations will use the effective uid/gid, therefore this
      routine can be used in a suid/sgid environment to test if the invoking user
      has the specified access to the path.
    """
    pass

def chdir(*args, **kwargs): # real signature unknown
    """
    Change the current working directory to the specified path.
    
    path may always be specified as a string.
    On some platforms, path may also be specified as an open file descriptor.
      If this functionality is unavailable, using it raises an exception.
    """
    pass

def chmod(*args, **kwargs): # real signature unknown
    """
    Change the access permissions of a file.
    
      path
        Path to be modified.  May always be specified as a str, bytes, or a path-like object.
        On some platforms, path may also be specified as an open file descriptor.
        If this functionality is unavailable, using it raises an exception.
      mode
        Operating-system mode bitfield.
      dir_fd
        If not None, it should be a file descriptor open to a directory,
        and path should be relative; path will then be relative to that
        directory.
      follow_symlinks
        If False, and the last element of the path is a symbolic link,
        chmod will modify the symbolic link itself instead of the file
        the link points to.
    
    It is an error to use dir_fd or follow_symlinks when specifying path as
      an open file descriptor.
    dir_fd and follow_symlinks may not be implemented on your platform.
      If they are unavailable, using them will raise a NotImplementedError.
    """
    pass

def chown(*args, **kwargs): # real signature unknown
    """
    Change the owner and group id of path to the numeric uid and gid.\
    
      path
        Path to be examined; can be string, bytes, a path-like object, or open-file-descriptor int.
      dir_fd
        If not None, it should be a file descriptor open to a directory,
        and path should be relative; path will then be relative to that
        directory.
      follow_symlinks
        If False, and the last element of the path is a symbolic link,
        stat will examine the symbolic link itself instead of the file
        the link points to.
    
    path may always be specified as a string.
    On some platforms, path may also be specified as an open file descriptor.
      If this functionality is unavailable, using it raises an exception.
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    If follow_symlinks is False, and the last element of the path is a symbolic
      link, chown will modify the symbolic link itself instead of the file the
      link points to.
    It is an error to use dir_fd or follow_symlinks when specifying path as
      an open file descriptor.
    dir_fd and follow_symlinks may not be implemented on your platform.
      If they are unavailable, using them will raise a NotImplementedError.
    """
    pass

def chroot(*args, **kwargs): # real signature unknown
    """ Change root directory to path. """
    pass

def close(*args, **kwargs): # real signature unknown
    """ Close a file descriptor. """
    pass

def closerange(*args, **kwargs): # real signature unknown
    """ Closes all file descriptors in [fd_low, fd_high), ignoring errors. """
    pass

def confstr(*args, **kwargs): # real signature unknown
    """ Return a string-valued system configuration variable. """
    pass

def copy_file_range(*args, **kwargs): # real signature unknown
    """
    Copy count bytes from one file descriptor to another.
    
      src
        Source file descriptor.
      dst
        Destination file descriptor.
      count
        Number of bytes to copy.
      offset_src
        Starting offset in src.
      offset_dst
        Starting offset in dst.
    
    If offset_src is None, then src is read from the current position;
    respectively for offset_dst.
    """
    pass

def cpu_count(*args, **kwargs): # real signature unknown
    """
    Return the number of CPUs in the system; return None if indeterminable.
    
    This number is not equivalent to the number of CPUs the current process can
    use.  The number of usable CPUs can be obtained with
    ``len(os.sched_getaffinity(0))``
    """
    pass

def ctermid(*args, **kwargs): # real signature unknown
    """ Return the name of the controlling terminal for this process. """
    pass

def device_encoding(*args, **kwargs): # real signature unknown
    """
    Return a string describing the encoding of a terminal's file descriptor.
    
    The file descriptor must be attached to a terminal.
    If the device is not a terminal, return None.
    """
    pass

def dup(*args, **kwargs): # real signature unknown
    """ Return a duplicate of a file descriptor. """
    pass

def dup2(*args, **kwargs): # real signature unknown
    """ Duplicate file descriptor. """
    pass

def execv(*args, **kwargs): # real signature unknown
    """
    Execute an executable path with arguments, replacing current process.
    
      path
        Path of executable file.
      argv
        Tuple or list of strings.
    """
    pass

def execve(*args, **kwargs): # real signature unknown
    """
    Execute an executable path with arguments, replacing current process.
    
      path
        Path of executable file.
      argv
        Tuple or list of strings.
      env
        Dictionary of strings mapping to strings.
    """
    pass

def fchdir(*args, **kwargs): # real signature unknown
    """
    Change to the directory of the given file descriptor.
    
    fd must be opened on a directory, not a file.
    Equivalent to os.chdir(fd).
    """
    pass

def fchmod(*args, **kwargs): # real signature unknown
    """
    Change the access permissions of the file given by file descriptor fd.
    
    Equivalent to os.chmod(fd, mode).
    """
    pass

def fchown(*args, **kwargs): # real signature unknown
    """
    Change the owner and group id of the file specified by file descriptor.
    
    Equivalent to os.chown(fd, uid, gid).
    """
    pass

def fdatasync(*args, **kwargs): # real signature unknown
    """ Force write of fd to disk without forcing update of metadata. """
    pass

def fork(*args, **kwargs): # real signature unknown
    """
    Fork a child process.
    
    Return 0 to child process and PID of child to parent process.
    """
    pass

def forkpty(*args, **kwargs): # real signature unknown
    """
    Fork a new process with a new pseudo-terminal as controlling tty.
    
    Returns a tuple of (pid, master_fd).
    Like fork(), return pid of 0 to the child process,
    and pid of child to the parent process.
    To both, return fd of newly opened pseudo-terminal.
    """
    pass

def fpathconf(*args, **kwargs): # real signature unknown
    """
    Return the configuration limit name for the file descriptor fd.
    
    If there is no limit, return -1.
    """
    pass

def fspath(*args, **kwargs): # real signature unknown
    """
    Return the file system path representation of the object.
    
    If the object is str or bytes, then allow it to pass through as-is. If the
    object defines __fspath__(), then return the result of that method. All other
    types raise a TypeError.
    """
    pass

def fstat(*args, **kwargs): # real signature unknown
    """
    Perform a stat system call on the given file descriptor.
    
    Like stat(), but for an open file descriptor.
    Equivalent to os.stat(fd).
    """
    pass

def fstatvfs(*args, **kwargs): # real signature unknown
    """
    Perform an fstatvfs system call on the given fd.
    
    Equivalent to statvfs(fd).
    """
    pass

def fsync(*args, **kwargs): # real signature unknown
    """ Force write of fd to disk. """
    pass

def ftruncate(*args, **kwargs): # real signature unknown
    """ Truncate a file, specified by file descriptor, to a specific length. """
    pass

def getcwd(*args, **kwargs): # real signature unknown
    """ Return a unicode string representing the current working directory. """
    pass

def getcwdb(*args, **kwargs): # real signature unknown
    """ Return a bytes string representing the current working directory. """
    pass

def getegid(*args, **kwargs): # real signature unknown
    """ Return the current process's effective group id. """
    pass

def geteuid(*args, **kwargs): # real signature unknown
    """ Return the current process's effective user id. """
    pass

def getgid(*args, **kwargs): # real signature unknown
    """ Return the current process's group id. """
    pass

def getgrouplist(user, group): # real signature unknown; restored from __doc__
    """
    getgrouplist(user, group) -> list of groups to which a user belongs
    
    Returns a list of groups to which a user belongs.
    
        user: username to lookup
        group: base group id of the user
    """
    return []

def getgroups(*args, **kwargs): # real signature unknown
    """ Return list of supplemental group IDs for the process. """
    pass

def getloadavg(*args, **kwargs): # real signature unknown
    """
    Return average recent system load information.
    
    Return the number of processes in the system run queue averaged over
    the last 1, 5, and 15 minutes as a tuple of three floats.
    Raises OSError if the load average was unobtainable.
    """
    pass

def getlogin(*args, **kwargs): # real signature unknown
    """ Return the actual login name. """
    pass

def getpgid(): # real signature unknown; restored from __doc__
    """ Call the system call getpgid(), and return the result. """
    pass

def getpgrp(*args, **kwargs): # real signature unknown
    """ Return the current process group id. """
    pass

def getpid(*args, **kwargs): # real signature unknown
    """ Return the current process id. """
    pass

def getppid(*args, **kwargs): # real signature unknown
    """
    Return the parent's process id.
    
    If the parent process has already exited, Windows machines will still
    return its id; others systems will return the id of the 'init' process (1).
    """
    pass

def getpriority(*args, **kwargs): # real signature unknown
    """ Return program scheduling priority. """
    pass

def getrandom(*args, **kwargs): # real signature unknown
    """ Obtain a series of random bytes. """
    pass

def getresgid(*args, **kwargs): # real signature unknown
    """ Return a tuple of the current process's real, effective, and saved group ids. """
    pass

def getresuid(*args, **kwargs): # real signature unknown
    """ Return a tuple of the current process's real, effective, and saved user ids. """
    pass

def getsid(pid): # real signature unknown; restored from __doc__
    """ Call the system call getsid(pid) and return the result. """
    pass

def getuid(*args, **kwargs): # real signature unknown
    """ Return the current process's user id. """
    pass

def getxattr(*args, **kwargs): # real signature unknown
    """
    Return the value of extended attribute attribute on path.
    
    path may be either a string, a path-like object, or an open file descriptor.
    If follow_symlinks is False, and the last element of the path is a symbolic
      link, getxattr will examine the symbolic link itself instead of the file
      the link points to.
    """
    pass

def get_blocking(*args, **kwargs): # real signature unknown
    """
    Get the blocking mode of the file descriptor.
    
    Return False if the O_NONBLOCK flag is set, True if the flag is cleared.
    """
    pass

def get_inheritable(*args, **kwargs): # real signature unknown
    """ Get the close-on-exe flag of the specified file descriptor. """
    pass

def get_terminal_size(*args, **kwargs): # real signature unknown
    """
    Return the size of the terminal window as (columns, lines).
    
    The optional argument fd (default standard output) specifies
    which file descriptor should be queried.
    
    If the file descriptor is not connected to a terminal, an OSError
    is thrown.
    
    This function will only be defined if an implementation is
    available for this system.
    
    shutil.get_terminal_size is the high-level function which should
    normally be used, os.get_terminal_size is the low-level implementation.
    """
    pass

def initgroups(username, gid): # real signature unknown; restored from __doc__
    """
    initgroups(username, gid) -> None
    
    Call the system initgroups() to initialize the group access list with all of
    the groups of which the specified username is a member, plus the specified
    group id.
    """
    pass

def isatty(*args, **kwargs): # real signature unknown
    """
    Return True if the fd is connected to a terminal.
    
    Return True if the file descriptor is an open file descriptor
    connected to the slave end of a terminal.
    """
    pass

def kill(*args, **kwargs): # real signature unknown
    """ Kill a process with a signal. """
    pass

def killpg(*args, **kwargs): # real signature unknown
    """ Kill a process group with a signal. """
    pass

def lchown(*args, **kwargs): # real signature unknown
    """
    Change the owner and group id of path to the numeric uid and gid.
    
    This function will not follow symbolic links.
    Equivalent to os.chown(path, uid, gid, follow_symlinks=False).
    """
    pass

def link(*args, **kwargs): # real signature unknown
    """
    Create a hard link to a file.
    
    If either src_dir_fd or dst_dir_fd is not None, it should be a file
      descriptor open to a directory, and the respective path string (src or dst)
      should be relative; the path will then be relative to that directory.
    If follow_symlinks is False, and the last element of src is a symbolic
      link, link will create a link to the symbolic link itself instead of the
      file the link points to.
    src_dir_fd, dst_dir_fd, and follow_symlinks may not be implemented on your
      platform.  If they are unavailable, using them will raise a
      NotImplementedError.
    """
    pass

def listdir(*args, **kwargs): # real signature unknown
    """
    Return a list containing the names of the files in the directory.
    
    path can be specified as either str, bytes, or a path-like object.  If path is bytes,
      the filenames returned will also be bytes; in all other circumstances
      the filenames returned will be str.
    If path is None, uses the path='.'.
    On some platforms, path may also be specified as an open file descriptor;\
      the file descriptor must refer to a directory.
      If this functionality is unavailable, using it raises NotImplementedError.
    
    The list is in arbitrary order.  It does not include the special
    entries '.' and '..' even if they are present in the directory.
    """
    pass

def listxattr(*args, **kwargs): # real signature unknown
    """
    Return a list of extended attributes on path.
    
    path may be either None, a string, a path-like object, or an open file descriptor.
    if path is None, listxattr will examine the current directory.
    If follow_symlinks is False, and the last element of the path is a symbolic
      link, listxattr will examine the symbolic link itself instead of the file
      the link points to.
    """
    pass

def lockf(*args, **kwargs): # real signature unknown
    """
    Apply, test or remove a POSIX lock on an open file descriptor.
    
      fd
        An open file descriptor.
      command
        One of F_LOCK, F_TLOCK, F_ULOCK or F_TEST.
      length
        The number of bytes to lock, starting at the current position.
    """
    pass

def lseek(*args, **kwargs): # real signature unknown
    """
    Set the position of a file descriptor.  Return the new position.
    
    Return the new cursor position in number of bytes
    relative to the beginning of the file.
    """
    pass

def lstat(*args, **kwargs): # real signature unknown
    """
    Perform a stat system call on the given path, without following symbolic links.
    
    Like stat(), but do not follow symbolic links.
    Equivalent to stat(path, follow_symlinks=False).
    """
    pass

def major(*args, **kwargs): # real signature unknown
    """ Extracts a device major number from a raw device number. """
    pass

def makedev(*args, **kwargs): # real signature unknown
    """ Composes a raw device number from the major and minor device numbers. """
    pass

def memfd_create(*args, **kwargs): # real signature unknown
    pass

def minor(*args, **kwargs): # real signature unknown
    """ Extracts a device minor number from a raw device number. """
    pass

def mkdir(*args, **kwargs): # real signature unknown
    """
    Create a directory.
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.
    
    The mode argument is ignored on Windows.
    """
    pass

def mkfifo(*args, **kwargs): # real signature unknown
    """
    Create a "fifo" (a POSIX named pipe).
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.
    """
    pass

def mknod(*args, **kwargs): # real signature unknown
    """
    Create a node in the file system.
    
    Create a node in the file system (file, device special file or named pipe)
    at path.  mode specifies both the permissions to use and the
    type of node to be created, being combined (bitwise OR) with one of
    S_IFREG, S_IFCHR, S_IFBLK, and S_IFIFO.  If S_IFCHR or S_IFBLK is set on mode,
    device defines the newly created device special file (probably using
    os.makedev()).  Otherwise device is ignored.
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.
    """
    pass

def nice(*args, **kwargs): # real signature unknown
    """ Add increment to the priority of process and return the new priority. """
    pass

def open(*args, **kwargs): # real signature unknown
    """
    Open a file for low level IO.  Returns a file descriptor (integer).
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.
    """
    pass

def openpty(*args, **kwargs): # real signature unknown
    """
    Open a pseudo-terminal.
    
    Return a tuple of (master_fd, slave_fd) containing open file descriptors
    for both the master and slave ends.
    """
    pass

def pathconf(*args, **kwargs): # real signature unknown
    """
    Return the configuration limit name for the file or directory path.
    
    If there is no limit, return -1.
    On some platforms, path may also be specified as an open file descriptor.
      If this functionality is unavailable, using it raises an exception.
    """
    pass

def pipe(*args, **kwargs): # real signature unknown
    """
    Create a pipe.
    
    Returns a tuple of two file descriptors:
      (read_fd, write_fd)
    """
    pass

def pipe2(*args, **kwargs): # real signature unknown
    """
    Create a pipe with flags set atomically.
    
    Returns a tuple of two file descriptors:
      (read_fd, write_fd)
    
    flags can be constructed by ORing together one or more of these values:
    O_NONBLOCK, O_CLOEXEC.
    """
    pass

def posix_fadvise(*args, **kwargs): # real signature unknown
    """
    Announce an intention to access data in a specific pattern.
    
    Announce an intention to access data in a specific pattern, thus allowing
    the kernel to make optimizations.
    The advice applies to the region of the file specified by fd starting at
    offset and continuing for length bytes.
    advice is one of POSIX_FADV_NORMAL, POSIX_FADV_SEQUENTIAL,
    POSIX_FADV_RANDOM, POSIX_FADV_NOREUSE, POSIX_FADV_WILLNEED, or
    POSIX_FADV_DONTNEED.
    """
    pass

def posix_fallocate(*args, **kwargs): # real signature unknown
    """
    Ensure a file has allocated at least a particular number of bytes on disk.
    
    Ensure that the file specified by fd encompasses a range of bytes
    starting at offset bytes from the beginning and continuing for length bytes.
    """
    pass

def posix_spawn(*args, **kwargs): # real signature unknown
    """
    Execute the program specified by path in a new process.
    
      path
        Path of executable file.
      argv
        Tuple or list of strings.
      env
        Dictionary of strings mapping to strings.
      file_actions
        A sequence of file action tuples.
      setpgroup
        The pgroup to use with the POSIX_SPAWN_SETPGROUP flag.
      resetids
        If the value is `true` the POSIX_SPAWN_RESETIDS will be activated.
      setsid
        If the value is `true` the POSIX_SPAWN_SETSID or POSIX_SPAWN_SETSID_NP will be activated.
      setsigmask
        The sigmask to use with the POSIX_SPAWN_SETSIGMASK flag.
      setsigdef
        The sigmask to use with the POSIX_SPAWN_SETSIGDEF flag.
      scheduler
        A tuple with the scheduler policy (optional) and parameters.
    """
    pass

def posix_spawnp(*args, **kwargs): # real signature unknown
    """
    Execute the program specified by path in a new process.
    
      path
        Path of executable file.
      argv
        Tuple or list of strings.
      env
        Dictionary of strings mapping to strings.
      file_actions
        A sequence of file action tuples.
      setpgroup
        The pgroup to use with the POSIX_SPAWN_SETPGROUP flag.
      resetids
        If the value is `True` the POSIX_SPAWN_RESETIDS will be activated.
      setsid
        If the value is `True` the POSIX_SPAWN_SETSID or POSIX_SPAWN_SETSID_NP will be activated.
      setsigmask
        The sigmask to use with the POSIX_SPAWN_SETSIGMASK flag.
      setsigdef
        The sigmask to use with the POSIX_SPAWN_SETSIGDEF flag.
      scheduler
        A tuple with the scheduler policy (optional) and parameters.
    """
    pass

def pread(*args, **kwargs): # real signature unknown
    """
    Read a number of bytes from a file descriptor starting at a particular offset.
    
    Read length bytes from file descriptor fd, starting at offset bytes from
    the beginning of the file.  The file offset remains unchanged.
    """
    pass

def preadv(*args, **kwargs): # real signature unknown
    """
    Reads from a file descriptor into a number of mutable bytes-like objects.
    
    Combines the functionality of readv() and pread(). As readv(), it will
    transfer data into each buffer until it is full and then move on to the next
    buffer in the sequence to hold the rest of the data. Its fourth argument,
    specifies the file offset at which the input operation is to be performed. It
    will return the total number of bytes read (which can be less than the total
    capacity of all the objects).
    
    The flags argument contains a bitwise OR of zero or more of the following flags:
    
    - RWF_HIPRI
    - RWF_NOWAIT
    
    Using non-zero flags requires Linux 4.6 or newer.
    """
    pass

def putenv(*args, **kwargs): # real signature unknown
    """ Change or add an environment variable. """
    pass

def pwrite(*args, **kwargs): # real signature unknown
    """
    Write bytes to a file descriptor starting at a particular offset.
    
    Write buffer to fd, starting at offset bytes from the beginning of
    the file.  Returns the number of bytes writte.  Does not change the
    current file offset.
    """
    pass

def pwritev(*args, **kwargs): # real signature unknown
    """
    Writes the contents of bytes-like objects to a file descriptor at a given offset.
    
    Combines the functionality of writev() and pwrite(). All buffers must be a sequence
    of bytes-like objects. Buffers are processed in array order. Entire contents of first
    buffer is written before proceeding to second, and so on. The operating system may
    set a limit (sysconf() value SC_IOV_MAX) on the number of buffers that can be used.
    This function writes the contents of each object to the file descriptor and returns
    the total number of bytes written.
    
    The flags argument contains a bitwise OR of zero or more of the following flags:
    
    - RWF_DSYNC
    - RWF_SYNC
    
    Using non-zero flags requires Linux 4.7 or newer.
    """
    pass

def read(*args, **kwargs): # real signature unknown
    """ Read from a file descriptor.  Returns a bytes object. """
    pass

def readlink(*args, **kwargs): # real signature unknown
    """
    Return a string representing the path to which the symbolic link points.
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
    and path should be relative; path will then be relative to that directory.
    
    dir_fd may not be implemented on your platform.  If it is unavailable,
    using it will raise a NotImplementedError.
    """
    pass

def readv(*args, **kwargs): # real signature unknown
    """
    Read from a file descriptor fd into an iterable of buffers.
    
    The buffers should be mutable buffers accepting bytes.
    readv will transfer data into each buffer until it is full
    and then move on to the next buffer in the sequence to hold
    the rest of the data.
    
    readv returns the total number of bytes read,
    which may be less than the total capacity of all the buffers.
    """
    pass

def register_at_fork(*args, **kwargs): # real signature unknown
    """
    Register callables to be called when forking a new process.
    
      before
        A callable to be called in the parent before the fork() syscall.
      after_in_child
        A callable to be called in the child after fork().
      after_in_parent
        A callable to be called in the parent after fork().
    
    'before' callbacks are called in reverse order.
    'after_in_child' and 'after_in_parent' callbacks are called in order.
    """
    pass

def remove(*args, **kwargs): # real signature unknown
    """
    Remove a file (same as unlink()).
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.
    """
    pass

def removexattr(*args, **kwargs): # real signature unknown
    """
    Remove extended attribute attribute on path.
    
    path may be either a string, a path-like object, or an open file descriptor.
    If follow_symlinks is False, and the last element of the path is a symbolic
      link, removexattr will modify the symbolic link itself instead of the file
      the link points to.
    """
    pass

def rename(*args, **kwargs): # real signature unknown
    """
    Rename a file or directory.
    
    If either src_dir_fd or dst_dir_fd is not None, it should be a file
      descriptor open to a directory, and the respective path string (src or dst)
      should be relative; the path will then be relative to that directory.
    src_dir_fd and dst_dir_fd, may not be implemented on your platform.
      If they are unavailable, using them will raise a NotImplementedError.
    """
    pass

def replace(*args, **kwargs): # real signature unknown
    """
    Rename a file or directory, overwriting the destination.
    
    If either src_dir_fd or dst_dir_fd is not None, it should be a file
      descriptor open to a directory, and the respective path string (src or dst)
      should be relative; the path will then be relative to that directory.
    src_dir_fd and dst_dir_fd, may not be implemented on your platform.
      If they are unavailable, using them will raise a NotImplementedError.
    """
    pass

def rmdir(*args, **kwargs): # real signature unknown
    """
    Remove a directory.
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.
    """
    pass

def scandir(*args, **kwargs): # real signature unknown
    """
    Return an iterator of DirEntry objects for given path.
    
    path can be specified as either str, bytes, or a path-like object.  If path
    is bytes, the names of yielded DirEntry objects will also be bytes; in
    all other circumstances they will be str.
    
    If path is None, uses the path='.'.
    """
    pass

def sched_getaffinity(*args, **kwargs): # real signature unknown
    """
    Return the affinity of the process identified by pid (or the current process if zero).
    
    The affinity is returned as a set of CPU identifiers.
    """
    pass

def sched_getparam(*args, **kwargs): # real signature unknown
    """
    Returns scheduling parameters for the process identified by pid.
    
    If pid is 0, returns parameters for the calling process.
    Return value is an instance of sched_param.
    """
    pass

def sched_getscheduler(*args, **kwargs): # real signature unknown
    """
    Get the scheduling policy for the process identifiedy by pid.
    
    Passing 0 for pid returns the scheduling policy for the calling process.
    """
    pass

def sched_get_priority_max(*args, **kwargs): # real signature unknown
    """ Get the maximum scheduling priority for policy. """
    pass

def sched_get_priority_min(*args, **kwargs): # real signature unknown
    """ Get the minimum scheduling priority for policy. """
    pass

def sched_rr_get_interval(*args, **kwargs): # real signature unknown
    """
    Return the round-robin quantum for the process identified by pid, in seconds.
    
    Value returned is a float.
    """
    pass

def sched_setaffinity(*args, **kwargs): # real signature unknown
    """
    Set the CPU affinity of the process identified by pid to mask.
    
    mask should be an iterable of integers identifying CPUs.
    """
    pass

def sched_setparam(*args, **kwargs): # real signature unknown
    """
    Set scheduling parameters for the process identified by pid.
    
    If pid is 0, sets parameters for the calling process.
    param should be an instance of sched_param.
    """
    pass

def sched_setscheduler(*args, **kwargs): # real signature unknown
    """
    Set the scheduling policy for the process identified by pid.
    
    If pid is 0, the calling process is changed.
    param is an instance of sched_param.
    """
    pass

def sched_yield(*args, **kwargs): # real signature unknown
    """ Voluntarily relinquish the CPU. """
    pass

def sendfile(out, in_, offset, count): # real signature unknown; restored from __doc__
    """
    sendfile(out, in, offset, count) -> byteswritten
    sendfile(out, in, offset, count[, headers][, trailers], flags=0)
                -> byteswritten
    Copy count bytes from file descriptor in to file descriptor out.
    """
    pass

def setegid(*args, **kwargs): # real signature unknown
    """ Set the current process's effective group id. """
    pass

def seteuid(*args, **kwargs): # real signature unknown
    """ Set the current process's effective user id. """
    pass

def setgid(*args, **kwargs): # real signature unknown
    """ Set the current process's group id. """
    pass

def setgroups(*args, **kwargs): # real signature unknown
    """ Set the groups of the current process to list. """
    pass

def setpgid(pid, pgrp): # real signature unknown; restored from __doc__
    """ Call the system call setpgid(pid, pgrp). """
    pass

def setpgrp(*args, **kwargs): # real signature unknown
    """ Make the current process the leader of its process group. """
    pass

def setpriority(*args, **kwargs): # real signature unknown
    """ Set program scheduling priority. """
    pass

def setregid(*args, **kwargs): # real signature unknown
    """ Set the current process's real and effective group ids. """
    pass

def setresgid(*args, **kwargs): # real signature unknown
    """ Set the current process's real, effective, and saved group ids. """
    pass

def setresuid(*args, **kwargs): # real signature unknown
    """ Set the current process's real, effective, and saved user ids. """
    pass

def setreuid(*args, **kwargs): # real signature unknown
    """ Set the current process's real and effective user ids. """
    pass

def setsid(): # real signature unknown; restored from __doc__
    """ Call the system call setsid(). """
    pass

def setuid(*args, **kwargs): # real signature unknown
    """ Set the current process's user id. """
    pass

def setxattr(*args, **kwargs): # real signature unknown
    """
    Set extended attribute attribute on path to value.
    
    path may be either a string, a path-like object,  or an open file descriptor.
    If follow_symlinks is False, and the last element of the path is a symbolic
      link, setxattr will modify the symbolic link itself instead of the file
      the link points to.
    """
    pass

def set_blocking(*args, **kwargs): # real signature unknown
    """
    Set the blocking mode of the specified file descriptor.
    
    Set the O_NONBLOCK flag if blocking is False,
    clear the O_NONBLOCK flag otherwise.
    """
    pass

def set_inheritable(*args, **kwargs): # real signature unknown
    """ Set the inheritable flag of the specified file descriptor. """
    pass

def stat(*args, **kwargs): # real signature unknown
    """
    Perform a stat system call on the given path.
    
      path
        Path to be examined; can be string, bytes, a path-like object or
        open-file-descriptor int.
      dir_fd
        If not None, it should be a file descriptor open to a directory,
        and path should be a relative string; path will then be relative to
        that directory.
      follow_symlinks
        If False, and the last element of the path is a symbolic link,
        stat will examine the symbolic link itself instead of the file
        the link points to.
    
    dir_fd and follow_symlinks may not be implemented
      on your platform.  If they are unavailable, using them will raise a
      NotImplementedError.
    
    It's an error to use dir_fd or follow_symlinks when specifying path as
      an open file descriptor.
    """
    pass

def statvfs(*args, **kwargs): # real signature unknown
    """
    Perform a statvfs system call on the given path.
    
    path may always be specified as a string.
    On some platforms, path may also be specified as an open file descriptor.
      If this functionality is unavailable, using it raises an exception.
    """
    pass

def strerror(*args, **kwargs): # real signature unknown
    """ Translate an error code to a message string. """
    pass

def symlink(*args, **kwargs): # real signature unknown
    """
    Create a symbolic link pointing to src named dst.
    
    target_is_directory is required on Windows if the target is to be
      interpreted as a directory.  (On Windows, symlink requires
      Windows 6.0 or greater, and raises a NotImplementedError otherwise.)
      target_is_directory is ignored on non-Windows platforms.
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.
    """
    pass

def sync(*args, **kwargs): # real signature unknown
    """ Force write of everything to disk. """
    pass

def sysconf(*args, **kwargs): # real signature unknown
    """ Return an integer-valued system configuration variable. """
    pass

def system(*args, **kwargs): # real signature unknown
    """ Execute the command in a subshell. """
    pass

def tcgetpgrp(*args, **kwargs): # real signature unknown
    """ Return the process group associated with the terminal specified by fd. """
    pass

def tcsetpgrp(*args, **kwargs): # real signature unknown
    """ Set the process group associated with the terminal specified by fd. """
    pass

def times(*args, **kwargs): # real signature unknown
    """
    Return a collection containing process timing information.
    
    The object returned behaves like a named tuple with these fields:
      (utime, stime, cutime, cstime, elapsed_time)
    All fields are floating point numbers.
    """
    pass

def truncate(*args, **kwargs): # real signature unknown
    """
    Truncate a file, specified by path, to a specific length.
    
    On some platforms, path may also be specified as an open file descriptor.
      If this functionality is unavailable, using it raises an exception.
    """
    pass

def ttyname(*args, **kwargs): # real signature unknown
    """
    Return the name of the terminal device connected to 'fd'.
    
      fd
        Integer file descriptor handle.
    """
    pass

def umask(*args, **kwargs): # real signature unknown
    """ Set the current numeric umask and return the previous umask. """
    pass

def uname(*args, **kwargs): # real signature unknown
    """
    Return an object identifying the current operating system.
    
    The object behaves like a named tuple with the following fields:
      (sysname, nodename, release, version, machine)
    """
    pass

def unlink(*args, **kwargs): # real signature unknown
    """
    Remove a file (same as remove()).
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.
    """
    pass

def unsetenv(*args, **kwargs): # real signature unknown
    """ Delete an environment variable. """
    pass

def urandom(*args, **kwargs): # real signature unknown
    """ Return a bytes object containing random bytes suitable for cryptographic use. """
    pass

def utime(*args, **kwargs): # real signature unknown
    """
    Set the access and modified time of path.
    
    path may always be specified as a string.
    On some platforms, path may also be specified as an open file descriptor.
      If this functionality is unavailable, using it raises an exception.
    
    If times is not None, it must be a tuple (atime, mtime);
        atime and mtime should be expressed as float seconds since the epoch.
    If ns is specified, it must be a tuple (atime_ns, mtime_ns);
        atime_ns and mtime_ns should be expressed as integer nanoseconds
        since the epoch.
    If times is None and ns is unspecified, utime uses the current time.
    Specifying tuples for both times and ns is an error.
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    If follow_symlinks is False, and the last element of the path is a symbolic
      link, utime will modify the symbolic link itself instead of the file the
      link points to.
    It is an error to use dir_fd or follow_symlinks when specifying path
      as an open file descriptor.
    dir_fd and follow_symlinks may not be available on your platform.
      If they are unavailable, using them will raise a NotImplementedError.
    """
    pass

def wait(*args, **kwargs): # real signature unknown
    """
    Wait for completion of a child process.
    
    Returns a tuple of information about the child process:
        (pid, status)
    """
    pass

def wait3(*args, **kwargs): # real signature unknown
    """
    Wait for completion of a child process.
    
    Returns a tuple of information about the child process:
      (pid, status, rusage)
    """
    pass

def wait4(*args, **kwargs): # real signature unknown
    """
    Wait for completion of a specific child process.
    
    Returns a tuple of information about the child process:
      (pid, status, rusage)
    """
    pass

def waitid(*args, **kwargs): # real signature unknown
    """
    Returns the result of waiting for a process or processes.
    
      idtype
        Must be one of be P_PID, P_PGID or P_ALL.
      id
        The id to wait on.
      options
        Constructed from the ORing of one or more of WEXITED, WSTOPPED
        or WCONTINUED and additionally may be ORed with WNOHANG or WNOWAIT.
    
    Returns either waitid_result or None if WNOHANG is specified and there are
    no children in a waitable state.
    """
    pass

def waitpid(*args, **kwargs): # real signature unknown
    """
    Wait for completion of a given child process.
    
    Returns a tuple of information regarding the child process:
        (pid, status)
    
    The options argument is ignored on Windows.
    """
    pass

def WCOREDUMP(*args, **kwargs): # real signature unknown
    """ Return True if the process returning status was dumped to a core file. """
    pass

def WEXITSTATUS(*args, **kwargs): # real signature unknown
    """ Return the process return code from status. """
    pass

def WIFCONTINUED(*args, **kwargs): # real signature unknown
    """
    Return True if a particular process was continued from a job control stop.
    
    Return True if the process returning status was continued from a
    job control stop.
    """
    pass

def WIFEXITED(*args, **kwargs): # real signature unknown
    """ Return True if the process returning status exited via the exit() system call. """
    pass

def WIFSIGNALED(*args, **kwargs): # real signature unknown
    """ Return True if the process returning status was terminated by a signal. """
    pass

def WIFSTOPPED(*args, **kwargs): # real signature unknown
    """ Return True if the process returning status was stopped. """
    pass

def write(*args, **kwargs): # real signature unknown
    """ Write a bytes object to a file descriptor. """
    pass

def writev(*args, **kwargs): # real signature unknown
    """
    Iterate over buffers, and write the contents of each to a file descriptor.
    
    Returns the total number of bytes written.
    buffers must be a sequence of bytes-like objects.
    """
    pass

def WSTOPSIG(*args, **kwargs): # real signature unknown
    """ Return the signal that stopped the process that provided the status value. """
    pass

def WTERMSIG(*args, **kwargs): # real signature unknown
    """ Return the signal that terminated the process that provided the status value. """
    pass

def _exit(*args, **kwargs): # real signature unknown
    """ Exit to the system with specified status, without normal exit processing. """
    pass

# classes

class DirEntry(object):
    # no doc
    def inode(self, *args, **kwargs): # real signature unknown
        """ Return inode of the entry; cached per entry. """
        pass

    def is_dir(self, *args, **kwargs): # real signature unknown
        """ Return True if the entry is a directory; cached per entry. """
        pass

    def is_file(self, *args, **kwargs): # real signature unknown
        """ Return True if the entry is a file; cached per entry. """
        pass

    def is_symlink(self, *args, **kwargs): # real signature unknown
        """ Return True if the entry is a symbolic link; cached per entry. """
        pass

    def stat(self, *args, **kwargs): # real signature unknown
        """ Return stat_result object for the entry; cached per entry. """
        pass

    def __fspath__(self, *args, **kwargs): # real signature unknown
        """ Returns the path for the entry. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the entry's base filename, relative to scandir() "path" argument"""

    path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the entry's full path name; equivalent to os.path.join(scandir_path, entry.name)"""



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



class sched_param(tuple):
    """
    Current has only one field: sched_priority");
    
      sched_priority
        A scheduling parameter.
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

    sched_priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the scheduling priority"""


    n_fields = 1
    n_sequence_fields = 1
    n_unnamed_fields = 0


class statvfs_result(tuple):
    """
    statvfs_result: Result from statvfs or fstatvfs.
    
    This object may be accessed either as a tuple of
      (bsize, frsize, blocks, bfree, bavail, files, ffree, favail, flag, namemax),
    or via the attributes f_bsize, f_frsize, f_blocks, f_bfree, and so on.
    
    See os.statvfs for more information.
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

    f_bavail = property(lambda self: 0)
    """:type: int"""

    f_bfree = property(lambda self: 0)
    """:type: int"""

    f_blocks = property(lambda self: 0)
    """:type: int"""

    f_bsize = property(lambda self: 0)
    """:type: int"""

    f_favail = property(lambda self: 0)
    """:type: int"""

    f_ffree = property(lambda self: 0)
    """:type: int"""

    f_files = property(lambda self: 0)
    """:type: int"""

    f_flag = property(lambda self: 0)
    """:type: int"""

    f_frsize = property(lambda self: 0)
    """:type: int"""

    f_fsid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f_namemax = property(lambda self: 0)
    """:type: int"""


    n_fields = 11
    n_sequence_fields = 10
    n_unnamed_fields = 0


class stat_result(tuple):
    """
    stat_result: Result from stat, fstat, or lstat.
    
    This object may be accessed either as a tuple of
      (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)
    or via the attributes st_mode, st_ino, st_dev, st_nlink, st_uid, and so on.
    
    Posix/windows: If your platform supports st_blksize, st_blocks, st_rdev,
    or st_flags, they are available as attributes only.
    
    See os.stat for more information.
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

    st_atime = property(lambda self: 0)
    """time of last access

    :type: int
    """

    st_atime_ns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """time of last access in nanoseconds"""

    st_blksize = property(lambda self: 0)
    """blocksize for filesystem I/O

    :type: int
    """

    st_blocks = property(lambda self: 0)
    """number of blocks allocated

    :type: int
    """

    st_ctime = property(lambda self: 0)
    """time of last change

    :type: int
    """

    st_ctime_ns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """time of last change in nanoseconds"""

    st_dev = property(lambda self: 0)
    """device

    :type: int
    """

    st_gid = property(lambda self: 0)
    """group ID of owner

    :type: int
    """

    st_ino = property(lambda self: 0)
    """inode

    :type: int
    """

    st_mode = property(lambda self: 0)
    """protection bits

    :type: int
    """

    st_mtime = property(lambda self: 0)
    """time of last modification

    :type: int
    """

    st_mtime_ns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """time of last modification in nanoseconds"""

    st_nlink = property(lambda self: 0)
    """number of hard links

    :type: int
    """

    st_rdev = property(lambda self: 0)
    """device type (if inode device)

    :type: int
    """

    st_size = property(lambda self: 0)
    """total size, in bytes

    :type: int
    """

    st_uid = property(lambda self: 0)
    """user ID of owner

    :type: int
    """


    n_fields = 19
    n_sequence_fields = 10
    n_unnamed_fields = 3


class terminal_size(tuple):
    """ A tuple of (columns, lines) for holding terminal window size """
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

    columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """width of the terminal window in characters"""

    lines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """height of the terminal window in characters"""


    n_fields = 2
    n_sequence_fields = 2
    n_unnamed_fields = 0


class times_result(tuple):
    """
    times_result: Result from os.times().
    
    This object may be accessed either as a tuple of
      (user, system, children_user, children_system, elapsed),
    or via the attributes user, system, children_user, children_system,
    and elapsed.
    
    See os.times for more information.
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

    children_system = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """system time of children"""

    children_user = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """user time of children"""

    elapsed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """elapsed time since an arbitrary point in the past"""

    system = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """system time"""

    user = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """user time"""


    n_fields = 5
    n_sequence_fields = 5
    n_unnamed_fields = 0


class uname_result(tuple):
    """
    uname_result: Result from os.uname().
    
    This object may be accessed either as a tuple of
      (sysname, nodename, release, version, machine),
    or via the attributes sysname, nodename, release, version, and machine.
    
    See os.uname for more information.
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

    machine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """hardware identifier"""

    nodename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """name of machine on network (implementation-defined)"""

    release = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """operating system release"""

    sysname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """operating system name"""

    version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """operating system version"""


    n_fields = 5
    n_sequence_fields = 5
    n_unnamed_fields = 0


class waitid_result(tuple):
    """
    waitid_result: Result from waitid.
    
    This object may be accessed either as a tuple of
      (si_pid, si_uid, si_signo, si_status, si_code),
    or via the attributes si_pid, si_uid, and so on.
    
    See os.waitid for more information.
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

    si_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    si_pid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    si_signo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    si_status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    si_uid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    n_fields = 5
    n_sequence_fields = 5
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

confstr_names = {
    'CS_GNU_LIBC_VERSION': 2,
    'CS_GNU_LIBPTHREAD_VERSION': 3,
    'CS_LFS64_CFLAGS': 1004,
    'CS_LFS64_LDFLAGS': 1005,
    'CS_LFS64_LIBS': 1006,
    'CS_LFS64_LINTFLAGS': 1007,
    'CS_LFS_CFLAGS': 1000,
    'CS_LFS_LDFLAGS': 1001,
    'CS_LFS_LIBS': 1002,
    'CS_LFS_LINTFLAGS': 1003,
    'CS_PATH': 0,
    'CS_XBS5_ILP32_OFF32_CFLAGS': 1100,
    'CS_XBS5_ILP32_OFF32_LDFLAGS': 1101,
    'CS_XBS5_ILP32_OFF32_LIBS': 1102,
    'CS_XBS5_ILP32_OFF32_LINTFLAGS': 1103,
    'CS_XBS5_ILP32_OFFBIG_CFLAGS': 1104,
    'CS_XBS5_ILP32_OFFBIG_LDFLAGS': 1105,
    'CS_XBS5_ILP32_OFFBIG_LIBS': 1106,
    'CS_XBS5_ILP32_OFFBIG_LINTFLAGS': 1107,
    'CS_XBS5_LP64_OFF64_CFLAGS': 1108,
    'CS_XBS5_LP64_OFF64_LDFLAGS': 1109,
    'CS_XBS5_LP64_OFF64_LIBS': 1110,
    'CS_XBS5_LP64_OFF64_LINTFLAGS': 1111,
    'CS_XBS5_LPBIG_OFFBIG_CFLAGS': 1112,
    'CS_XBS5_LPBIG_OFFBIG_LDFLAGS': 1113,
    'CS_XBS5_LPBIG_OFFBIG_LIBS': 1114,
    'CS_XBS5_LPBIG_OFFBIG_LINTFLAGS': 1115,
}

environ = {} # real value of type <class 'dict'> skipped

pathconf_names = {
    'PC_ALLOC_SIZE_MIN': 18,
    'PC_ASYNC_IO': 10,
    'PC_CHOWN_RESTRICTED': 6,
    'PC_FILESIZEBITS': 13,
    'PC_LINK_MAX': 0,
    'PC_MAX_CANON': 1,
    'PC_MAX_INPUT': 2,
    'PC_NAME_MAX': 3,
    'PC_NO_TRUNC': 7,
    'PC_PATH_MAX': 4,
    'PC_PIPE_BUF': 5,
    'PC_PRIO_IO': 11,
    'PC_REC_INCR_XFER_SIZE': 14,
    'PC_REC_MAX_XFER_SIZE': 15,
    'PC_REC_MIN_XFER_SIZE': 16,
    'PC_REC_XFER_ALIGN': 17,
    'PC_SOCK_MAXBUF': 12,
    'PC_SYMLINK_MAX': 19,
    'PC_SYNC_IO': 9,
    'PC_VDISABLE': 8,
}

sysconf_names = {
    'SC_2_CHAR_TERM': 95,
    'SC_2_C_BIND': 47,
    'SC_2_C_DEV': 48,
    'SC_2_C_VERSION': 96,
    'SC_2_FORT_DEV': 49,
    'SC_2_FORT_RUN': 50,
    'SC_2_LOCALEDEF': 52,
    'SC_2_SW_DEV': 51,
    'SC_2_UPE': 97,
    'SC_2_VERSION': 46,
    'SC_AIO_LISTIO_MAX': 23,
    'SC_AIO_MAX': 24,
    'SC_AIO_PRIO_DELTA_MAX': 25,
    'SC_ARG_MAX': 0,
    'SC_ASYNCHRONOUS_IO': 12,
    'SC_ATEXIT_MAX': 87,
    'SC_AVPHYS_PAGES': 86,
    'SC_BC_BASE_MAX': 36,
    'SC_BC_DIM_MAX': 37,
    'SC_BC_SCALE_MAX': 38,
    'SC_BC_STRING_MAX': 39,
    'SC_CHARCLASS_NAME_MAX': 45,
    'SC_CHAR_BIT': 101,
    'SC_CHAR_MAX': 102,
    'SC_CHAR_MIN': 103,
    'SC_CHILD_MAX': 1,
    'SC_CLK_TCK': 2,
    'SC_COLL_WEIGHTS_MAX': 40,
    'SC_DELAYTIMER_MAX': 26,
    'SC_EQUIV_CLASS_MAX': 41,
    'SC_EXPR_NEST_MAX': 42,
    'SC_FSYNC': 15,
    'SC_GETGR_R_SIZE_MAX': 69,
    'SC_GETPW_R_SIZE_MAX': 70,
    'SC_INT_MAX': 104,
    'SC_INT_MIN': 105,
    'SC_IOV_MAX': 60,
    'SC_JOB_CONTROL': 7,
    'SC_LINE_MAX': 43,
    'SC_LOGIN_NAME_MAX': 71,
    'SC_LONG_BIT': 106,
    'SC_MAPPED_FILES': 16,
    'SC_MB_LEN_MAX': 108,
    'SC_MEMLOCK': 17,
    'SC_MEMLOCK_RANGE': 18,
    'SC_MEMORY_PROTECTION': 19,
    'SC_MESSAGE_PASSING': 20,
    'SC_MQ_OPEN_MAX': 27,
    'SC_MQ_PRIO_MAX': 28,
    'SC_NGROUPS_MAX': 3,
    'SC_NL_ARGMAX': 119,
    'SC_NL_LANGMAX': 120,
    'SC_NL_MSGMAX': 121,
    'SC_NL_NMAX': 122,
    'SC_NL_SETMAX': 123,
    'SC_NL_TEXTMAX': 124,
    'SC_NPROCESSORS_CONF': 83,
    'SC_NPROCESSORS_ONLN': 84,
    'SC_NZERO': 109,
    'SC_OPEN_MAX': 4,
    'SC_PAGESIZE': 30,
    'SC_PAGE_SIZE': 30,
    'SC_PASS_MAX': 88,
    'SC_PHYS_PAGES': 85,
    'SC_PII': 53,
    'SC_PII_INTERNET': 56,
    'SC_PII_INTERNET_DGRAM': 62,
    'SC_PII_INTERNET_STREAM': 61,
    'SC_PII_OSI': 57,
    'SC_PII_OSI_CLTS': 64,
    'SC_PII_OSI_COTS': 63,
    'SC_PII_OSI_M': 65,
    'SC_PII_SOCKET': 55,
    'SC_PII_XTI': 54,
    'SC_POLL': 58,
    'SC_PRIORITIZED_IO': 13,
    'SC_PRIORITY_SCHEDULING': 10,
    'SC_REALTIME_SIGNALS': 9,
    'SC_RE_DUP_MAX': 44,
    'SC_RTSIG_MAX': 31,
    'SC_SAVED_IDS': 8,
    'SC_SCHAR_MAX': 111,
    'SC_SCHAR_MIN': 112,
    'SC_SELECT': 59,
    'SC_SEMAPHORES': 21,
    'SC_SEM_NSEMS_MAX': 32,
    'SC_SEM_VALUE_MAX': 33,
    'SC_SHARED_MEMORY_OBJECTS': 22,
    'SC_SHRT_MAX': 113,
    'SC_SHRT_MIN': 114,
    'SC_SIGQUEUE_MAX': 34,
    'SC_SSIZE_MAX': 110,
    'SC_STREAM_MAX': 5,
    'SC_SYNCHRONIZED_IO': 14,
    'SC_THREADS': 67,
    'SC_THREAD_ATTR_STACKADDR': 77,
    'SC_THREAD_ATTR_STACKSIZE': 78,
    'SC_THREAD_DESTRUCTOR_ITERATIONS': 73,
    'SC_THREAD_KEYS_MAX': 74,
    'SC_THREAD_PRIORITY_SCHEDULING': 79,
    'SC_THREAD_PRIO_INHERIT': 80,
    'SC_THREAD_PRIO_PROTECT': 81,
    'SC_THREAD_PROCESS_SHARED': 82,
    'SC_THREAD_SAFE_FUNCTIONS': 68,
    'SC_THREAD_STACK_MIN': 75,
    'SC_THREAD_THREADS_MAX': 76,
    'SC_TIMERS': 11,
    'SC_TIMER_MAX': 35,
    'SC_TTY_NAME_MAX': 72,
    'SC_TZNAME_MAX': 6,
    'SC_T_IOV_MAX': 66,
    'SC_UCHAR_MAX': 115,
    'SC_UINT_MAX': 116,
    'SC_UIO_MAXIOV': 60,
    'SC_ULONG_MAX': 117,
    'SC_USHRT_MAX': 118,
    'SC_VERSION': 29,
    'SC_WORD_BIT': 107,
    'SC_XBS5_ILP32_OFF32': 125,
    'SC_XBS5_ILP32_OFFBIG': 126,
    'SC_XBS5_LP64_OFF64': 127,
    'SC_XBS5_LPBIG_OFFBIG': 128,
    'SC_XOPEN_CRYPT': 92,
    'SC_XOPEN_ENH_I18N': 93,
    'SC_XOPEN_LEGACY': 129,
    'SC_XOPEN_REALTIME': 130,
    'SC_XOPEN_REALTIME_THREADS': 131,
    'SC_XOPEN_SHM': 94,
    'SC_XOPEN_UNIX': 91,
    'SC_XOPEN_VERSION': 89,
    'SC_XOPEN_XCU_VERSION': 90,
    'SC_XOPEN_XPG2': 98,
    'SC_XOPEN_XPG3': 99,
    'SC_XOPEN_XPG4': 100,
}

_have_functions = [
    'HAVE_FACCESSAT',
    'HAVE_FCHDIR',
    'HAVE_FCHMOD',
    'HAVE_FCHMODAT',
    'HAVE_FCHOWN',
    'HAVE_FCHOWNAT',
    'HAVE_FEXECVE',
    'HAVE_FDOPENDIR',
    'HAVE_FPATHCONF',
    'HAVE_FSTATAT',
    'HAVE_FSTATVFS',
    'HAVE_FTRUNCATE',
    'HAVE_FUTIMENS',
    'HAVE_FUTIMES',
    'HAVE_FUTIMESAT',
    'HAVE_LINKAT',
    'HAVE_LCHOWN',
    'HAVE_LSTAT',
    'HAVE_LUTIMES',
    'HAVE_MEMFD_CREATE',
    'HAVE_MKDIRAT',
    'HAVE_MKFIFOAT',
    'HAVE_MKNODAT',
    'HAVE_OPENAT',
    'HAVE_READLINKAT',
    'HAVE_RENAMEAT',
    'HAVE_SYMLINKAT',
    'HAVE_UNLINKAT',
    'HAVE_UTIMENSAT',
]

__spec__ = None # (!) real value is "ModuleSpec(name='posix', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

