# encoding: utf-8
# module _sqlite3
# from /usr/local/lib/python3.8/lib-dynload/_sqlite3.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import sqlite3 as __sqlite3


# Variables with simple values

PARSE_COLNAMES = 2
PARSE_DECLTYPES = 1

SQLITE_ALTER_TABLE = 26

SQLITE_ANALYZE = 28
SQLITE_ATTACH = 24

SQLITE_CREATE_INDEX = 1
SQLITE_CREATE_TABLE = 2

SQLITE_CREATE_TEMP_INDEX = 3
SQLITE_CREATE_TEMP_TABLE = 4
SQLITE_CREATE_TEMP_TRIGGER = 5
SQLITE_CREATE_TEMP_VIEW = 6

SQLITE_CREATE_TRIGGER = 7
SQLITE_CREATE_VIEW = 8
SQLITE_CREATE_VTABLE = 29

SQLITE_DELETE = 9
SQLITE_DENY = 1
SQLITE_DETACH = 25
SQLITE_DONE = 101

SQLITE_DROP_INDEX = 10
SQLITE_DROP_TABLE = 11

SQLITE_DROP_TEMP_INDEX = 12
SQLITE_DROP_TEMP_TABLE = 13
SQLITE_DROP_TEMP_TRIGGER = 14
SQLITE_DROP_TEMP_VIEW = 15

SQLITE_DROP_TRIGGER = 16
SQLITE_DROP_VIEW = 17
SQLITE_DROP_VTABLE = 30

SQLITE_FUNCTION = 31
SQLITE_IGNORE = 2
SQLITE_INSERT = 18
SQLITE_OK = 0
SQLITE_PRAGMA = 19
SQLITE_READ = 20
SQLITE_RECURSIVE = 33
SQLITE_REINDEX = 27
SQLITE_SAVEPOINT = 32
SQLITE_SELECT = 21
SQLITE_TRANSACTION = 22
SQLITE_UPDATE = 23

sqlite_version = '3.40.1'

version = '2.6.0'

# functions

def adapt(obj, protocol, alternate): # real signature unknown; restored from __doc__
    """ adapt(obj, protocol, alternate) -> adapt obj to given protocol. Non-standard. """
    pass

def complete_statement(sql): # real signature unknown; restored from __doc__
    """
    complete_statement(sql)
    
    Checks if a string contains a complete SQL statement. Non-standard.
    """
    pass

def connect(database, timeout=None, detect_types=None, isolation_level=None, check_same_thread=None, factory=None, cached_statements=None, uri=None): # real signature unknown; restored from __doc__
    """
    connect(database[, timeout, detect_types, isolation_level,
            check_same_thread, factory, cached_statements, uri])
    
    Opens a connection to the SQLite database file *database*. You can use
    ":memory:" to open a database connection to a database that resides in
    RAM instead of on disk.
    """
    pass

def enable_callback_tracebacks(flag): # real signature unknown; restored from __doc__
    """
    enable_callback_tracebacks(flag)
    
    Enable or disable callback functions throwing errors to stderr.
    """
    pass

def enable_shared_cache(do_enable): # real signature unknown; restored from __doc__
    """
    enable_shared_cache(do_enable)
    
    Enable or disable shared cache mode for the calling thread.
    Experimental/Non-standard.
    """
    pass

def register_adapter(type, callable): # real signature unknown; restored from __doc__
    """
    register_adapter(type, callable)
    
    Registers an adapter with pysqlite's adapter registry. Non-standard.
    """
    pass

def register_converter(typename, callable): # real signature unknown; restored from __doc__
    """
    register_converter(typename, callable)
    
    Registers a converter with pysqlite. Non-standard.
    """
    pass

# classes

class Connection(object):
    """ SQLite database connection object. """
    def backup(self, *args, **kwargs): # real signature unknown
        """ Makes a backup of the database. Non-standard. """
        pass

    def close(self, *args, **kwargs): # real signature unknown
        """ Closes the connection. """
        pass

    def commit(self, *args, **kwargs): # real signature unknown
        """ Commit the current transaction. """
        pass

    def create_aggregate(self, *args, **kwargs): # real signature unknown
        """ Creates a new aggregate. Non-standard. """
        pass

    def create_collation(self, *args, **kwargs): # real signature unknown
        """ Creates a collation function. Non-standard. """
        pass

    def create_function(self, *args, **kwargs): # real signature unknown
        """ Creates a new function. Non-standard. """
        pass

    def cursor(self, *args, **kwargs): # real signature unknown
        """ Return a cursor for the connection. """
        pass

    def enable_load_extension(self, *args, **kwargs): # real signature unknown
        """ Enable dynamic loading of SQLite extension modules. Non-standard. """
        pass

    def execute(self, *args, **kwargs): # real signature unknown
        """ Executes a SQL statement. Non-standard. """
        pass

    def executemany(self, *args, **kwargs): # real signature unknown
        """ Repeatedly executes a SQL statement. Non-standard. """
        pass

    def executescript(self, *args, **kwargs): # real signature unknown
        """ Executes a multiple SQL statements at once. Non-standard. """
        pass

    def interrupt(self, *args, **kwargs): # real signature unknown
        """ Abort any pending database operation. Non-standard. """
        pass

    def iterdump(self, *args, **kwargs): # real signature unknown
        """ Returns iterator to the dump of the database in an SQL text format. Non-standard. """
        pass

    def load_extension(self, *args, **kwargs): # real signature unknown
        """ Load SQLite extension module. Non-standard. """
        pass

    def rollback(self, *args, **kwargs): # real signature unknown
        """ Roll back the current transaction. """
        pass

    def set_authorizer(self, *args, **kwargs): # real signature unknown
        """ Sets authorizer callback. Non-standard. """
        pass

    def set_progress_handler(self, *args, **kwargs): # real signature unknown
        """ Sets progress handler callback. Non-standard. """
        pass

    def set_trace_callback(self, *args, **kwargs): # real signature unknown
        """ Sets a trace callback called for each SQL statement (passed as unicode). Non-standard. """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __enter__(self, *args, **kwargs): # real signature unknown
        """ For context manager. Non-standard. """
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        """ For context manager. Non-standard. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DatabaseError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DataError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IntegrityError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    InterfaceError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    InternalError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    in_transaction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    isolation_level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    NotSupportedError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    OperationalError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ProgrammingError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    row_factory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    text_factory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    total_changes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Warning = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Cursor(object):
    """ SQLite database cursor class. """
    def close(self, *args, **kwargs): # real signature unknown
        """ Closes the cursor. """
        pass

    def execute(self, *args, **kwargs): # real signature unknown
        """ Executes a SQL statement. """
        pass

    def executemany(self, *args, **kwargs): # real signature unknown
        """ Repeatedly executes a SQL statement. """
        pass

    def executescript(self, *args, **kwargs): # real signature unknown
        """ Executes a multiple SQL statements at once. Non-standard. """
        pass

    def fetchall(self, *args, **kwargs): # real signature unknown
        """ Fetches all rows from the resultset. """
        pass

    def fetchmany(self, *args, **kwargs): # real signature unknown
        """ Fetches several rows from the resultset. """
        pass

    def fetchone(self, *args, **kwargs): # real signature unknown
        """ Fetches one row from the resultset. """
        pass

    def setinputsizes(self, *args, **kwargs): # real signature unknown
        """ Required by DB-API. Does nothing in pysqlite. """
        pass

    def setoutputsize(self, *args, **kwargs): # real signature unknown
        """ Required by DB-API. Does nothing in pysqlite. """
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

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Implement next(self). """
        pass

    arraysize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    connection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lastrowid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rowcount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    row_factory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class DatabaseError(__sqlite3.Error):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DataError(__sqlite3.DatabaseError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class IntegrityError(__sqlite3.DatabaseError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class InterfaceError(__sqlite3.Error):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class InternalError(__sqlite3.DatabaseError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class NotSupportedError(__sqlite3.DatabaseError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class OperationalError(__sqlite3.DatabaseError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class OptimizedUnicode(object):
    """
    str(object='') -> str
    str(bytes_or_buffer[, encoding[, errors]]) -> str
    
    Create a new string object from the given object. If encoding or
    errors is specified, then the object must expose a data buffer
    that will be decoded using the given encoding and error handler.
    Otherwise, returns the result of object.__str__() (if defined)
    or repr(object).
    encoding defaults to sys.getdefaultencoding().
    errors defaults to 'strict'.
    """
    def capitalize(self, *args, **kwargs): # real signature unknown
        """
        Return a capitalized version of the string.
        
        More specifically, make the first character have upper case and the rest lower
        case.
        """
        pass

    def casefold(self, *args, **kwargs): # real signature unknown
        """ Return a version of the string suitable for caseless comparisons. """
        pass

    def center(self, *args, **kwargs): # real signature unknown
        """
        Return a centered string of length width.
        
        Padding is done using the specified fill character (default is a space).
        """
        pass

    def count(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.count(sub[, start[, end]]) -> int
        
        Return the number of non-overlapping occurrences of substring sub in
        string S[start:end].  Optional arguments start and end are
        interpreted as in slice notation.
        """
        return 0

    def encode(self, *args, **kwargs): # real signature unknown
        """
        Encode the string using the codec registered for encoding.
        
          encoding
            The encoding in which to encode the string.
          errors
            The error handling scheme to use for encoding errors.
            The default is 'strict' meaning that encoding errors raise a
            UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
            'xmlcharrefreplace' as well as any other name registered with
            codecs.register_error that can handle UnicodeEncodeErrors.
        """
        pass

    def endswith(self, suffix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.endswith(suffix[, start[, end]]) -> bool
        
        Return True if S ends with the specified suffix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        suffix can also be a tuple of strings to try.
        """
        return False

    def expandtabs(self, *args, **kwargs): # real signature unknown
        """
        Return a copy where all tab characters are expanded using spaces.
        
        If tabsize is not given, a tab size of 8 characters is assumed.
        """
        pass

    def find(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.find(sub[, start[, end]]) -> int
        
        Return the lowest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    def format(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        S.format(*args, **kwargs) -> str
        
        Return a formatted version of S, using substitutions from args and kwargs.
        The substitutions are identified by braces ('{' and '}').
        """
        return ""

    def format_map(self, mapping): # real signature unknown; restored from __doc__
        """
        S.format_map(mapping) -> str
        
        Return a formatted version of S, using substitutions from mapping.
        The substitutions are identified by braces ('{' and '}').
        """
        return ""

    def index(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.index(sub[, start[, end]]) -> int
        
        Return the lowest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Raises ValueError when the substring is not found.
        """
        return 0

    def isalnum(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is an alpha-numeric string, False otherwise.
        
        A string is alpha-numeric if all characters in the string are alpha-numeric and
        there is at least one character in the string.
        """
        pass

    def isalpha(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is an alphabetic string, False otherwise.
        
        A string is alphabetic if all characters in the string are alphabetic and there
        is at least one character in the string.
        """
        pass

    def isascii(self, *args, **kwargs): # real signature unknown
        """
        Return True if all characters in the string are ASCII, False otherwise.
        
        ASCII characters have code points in the range U+0000-U+007F.
        Empty string is ASCII too.
        """
        pass

    def isdecimal(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a decimal string, False otherwise.
        
        A string is a decimal string if all characters in the string are decimal and
        there is at least one character in the string.
        """
        pass

    def isdigit(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a digit string, False otherwise.
        
        A string is a digit string if all characters in the string are digits and there
        is at least one character in the string.
        """
        pass

    def isidentifier(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a valid Python identifier, False otherwise.
        
        Call keyword.iskeyword(s) to test whether string s is a reserved identifier,
        such as "def" or "class".
        """
        pass

    def islower(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a lowercase string, False otherwise.
        
        A string is lowercase if all cased characters in the string are lowercase and
        there is at least one cased character in the string.
        """
        pass

    def isnumeric(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a numeric string, False otherwise.
        
        A string is numeric if all characters in the string are numeric and there is at
        least one character in the string.
        """
        pass

    def isprintable(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is printable, False otherwise.
        
        A string is printable if all of its characters are considered printable in
        repr() or if it is empty.
        """
        pass

    def isspace(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a whitespace string, False otherwise.
        
        A string is whitespace if all characters in the string are whitespace and there
        is at least one character in the string.
        """
        pass

    def istitle(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a title-cased string, False otherwise.
        
        In a title-cased string, upper- and title-case characters may only
        follow uncased characters and lowercase characters only cased ones.
        """
        pass

    def isupper(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is an uppercase string, False otherwise.
        
        A string is uppercase if all cased characters in the string are uppercase and
        there is at least one cased character in the string.
        """
        pass

    def join(self, ab=None, pq=None, rs=None): # real signature unknown; restored from __doc__
        """
        Concatenate any number of strings.
        
        The string whose method is called is inserted in between each given string.
        The result is returned as a new string.
        
        Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
        """
        pass

    def ljust(self, *args, **kwargs): # real signature unknown
        """
        Return a left-justified string of length width.
        
        Padding is done using the specified fill character (default is a space).
        """
        pass

    def lower(self, *args, **kwargs): # real signature unknown
        """ Return a copy of the string converted to lowercase. """
        pass

    def lstrip(self, *args, **kwargs): # real signature unknown
        """
        Return a copy of the string with leading whitespace removed.
        
        If chars is given and not None, remove characters in chars instead.
        """
        pass

    def maketrans(self, *args, **kwargs): # real signature unknown
        """
        Return a translation table usable for str.translate().
        
        If there is only one argument, it must be a dictionary mapping Unicode
        ordinals (integers) or characters to Unicode ordinals, strings or None.
        Character keys will be then converted to ordinals.
        If there are two arguments, they must be strings of equal length, and
        in the resulting dictionary, each character in x will be mapped to the
        character at the same position in y. If there is a third argument, it
        must be a string, whose characters will be mapped to None in the result.
        """
        pass

    def partition(self, *args, **kwargs): # real signature unknown
        """
        Partition the string into three parts using the given separator.
        
        This will search for the separator in the string.  If the separator is found,
        returns a 3-tuple containing the part before the separator, the separator
        itself, and the part after it.
        
        If the separator is not found, returns a 3-tuple containing the original string
        and two empty strings.
        """
        pass

    def replace(self, *args, **kwargs): # real signature unknown
        """
        Return a copy with all occurrences of substring old replaced by new.
        
          count
            Maximum number of occurrences to replace.
            -1 (the default value) means replace all occurrences.
        
        If the optional argument count is given, only the first count occurrences are
        replaced.
        """
        pass

    def rfind(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.rfind(sub[, start[, end]]) -> int
        
        Return the highest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    def rindex(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.rindex(sub[, start[, end]]) -> int
        
        Return the highest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Raises ValueError when the substring is not found.
        """
        return 0

    def rjust(self, *args, **kwargs): # real signature unknown
        """
        Return a right-justified string of length width.
        
        Padding is done using the specified fill character (default is a space).
        """
        pass

    def rpartition(self, *args, **kwargs): # real signature unknown
        """
        Partition the string into three parts using the given separator.
        
        This will search for the separator in the string, starting at the end. If
        the separator is found, returns a 3-tuple containing the part before the
        separator, the separator itself, and the part after it.
        
        If the separator is not found, returns a 3-tuple containing two empty strings
        and the original string.
        """
        pass

    def rsplit(self, *args, **kwargs): # real signature unknown
        """
        Return a list of the words in the string, using sep as the delimiter string.
        
          sep
            The delimiter according which to split the string.
            None (the default value) means split according to any whitespace,
            and discard empty strings from the result.
          maxsplit
            Maximum number of splits to do.
            -1 (the default value) means no limit.
        
        Splits are done starting at the end of the string and working to the front.
        """
        pass

    def rstrip(self, *args, **kwargs): # real signature unknown
        """
        Return a copy of the string with trailing whitespace removed.
        
        If chars is given and not None, remove characters in chars instead.
        """
        pass

    def split(self, *args, **kwargs): # real signature unknown
        """
        Return a list of the words in the string, using sep as the delimiter string.
        
          sep
            The delimiter according which to split the string.
            None (the default value) means split according to any whitespace,
            and discard empty strings from the result.
          maxsplit
            Maximum number of splits to do.
            -1 (the default value) means no limit.
        """
        pass

    def splitlines(self, *args, **kwargs): # real signature unknown
        """
        Return a list of the lines in the string, breaking at line boundaries.
        
        Line breaks are not included in the resulting list unless keepends is given and
        true.
        """
        pass

    def startswith(self, prefix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.startswith(prefix[, start[, end]]) -> bool
        
        Return True if S starts with the specified prefix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        prefix can also be a tuple of strings to try.
        """
        return False

    def strip(self, *args, **kwargs): # real signature unknown
        """
        Return a copy of the string with leading and trailing whitespace removed.
        
        If chars is given and not None, remove characters in chars instead.
        """
        pass

    def swapcase(self, *args, **kwargs): # real signature unknown
        """ Convert uppercase characters to lowercase and lowercase characters to uppercase. """
        pass

    def title(self, *args, **kwargs): # real signature unknown
        """
        Return a version of the string where each word is titlecased.
        
        More specifically, words start with uppercased characters and all remaining
        cased characters have lower case.
        """
        pass

    def translate(self, *args, **kwargs): # real signature unknown
        """
        Replace each character in the string using the given translation table.
        
          table
            Translation table, which must be a mapping of Unicode ordinals to
            Unicode ordinals, strings, or None.
        
        The table must implement lookup/indexing via __getitem__, for instance a
        dictionary or list.  If this operation raises LookupError, the character is
        left untouched.  Characters mapped to None are deleted.
        """
        pass

    def upper(self, *args, **kwargs): # real signature unknown
        """ Return a copy of the string converted to uppercase. """
        pass

    def zfill(self, *args, **kwargs): # real signature unknown
        """
        Pad a numeric string with zeros on the left, to fill a field of the given width.
        
        The string is never truncated.
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Return a formatted version of the string as described by format_spec. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Return the size of the string in memory, in bytes. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass


class PrepareProtocol(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class ProgrammingError(__sqlite3.DatabaseError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Row(object):
    # no doc
    def keys(self, *args, **kwargs): # real signature unknown
        """ Returns the keys of the row. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass


class Warning(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

adapters = {
    (
        None, # (!) real value is "<class 'datetime.date'>"
        PrepareProtocol,
    ): 
        None # (!) real value is '<function register_adapters_and_converters.<locals>.adapt_date at 0xffffabe09040>'
    ,
    (
        None, # (!) real value is "<class 'datetime.datetime'>"
        '<value is a self-reference, replaced by this string>',
    ): 
        None # (!) real value is '<function register_adapters_and_converters.<locals>.adapt_datetime at 0xffffaba1aa60>'
    ,
}

converters = {
    'DATE': None, # (!) real value is '<function register_adapters_and_converters.<locals>.convert_date at 0xffffaba1aaf0>'
    'TIMESTAMP': None, # (!) real value is '<function register_adapters_and_converters.<locals>.convert_timestamp at 0xffffaba1a9d0>'
}

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924ac0>'

__spec__ = None # (!) real value is "ModuleSpec(name='_sqlite3', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924ac0>, origin='/usr/local/lib/python3.8/lib-dynload/_sqlite3.cpython-38-aarch64-linux-gnu.so')"

