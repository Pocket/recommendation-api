# encoding: utf-8
# module aiohttp._http_parser
# from /.venv/lib/python3.8/site-packages/aiohttp/_http_parser.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import aiohttp.hdrs as hdrs # /.venv/lib/python3.8/site-packages/aiohttp/hdrs.py
from multidict._multidict import _CIMultiDict, _CIMultiDictProxy

import aiohttp.http_exceptions as __aiohttp_http_exceptions
import aiohttp.streams as __aiohttp_streams


# Variables with simple values

DEBUG = False
i = 45

# functions

def __pyx_unpickle_RawRequestMessage(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_RawResponseMessage(*args, **kwargs): # real signature unknown
    pass

# classes

class BadHttpMessage(__aiohttp_http_exceptions.HttpProcessingError):
    # no doc
    def __init__(self, message, *, headers=None): # reliably restored by inspect
        # no doc
        pass

    code = 400
    message = 'Bad Request'


class BadStatusLine(__aiohttp_http_exceptions.BadHttpMessage):
    # no doc
    def __init__(self, line=None, error=None): # reliably restored by inspect
        # no doc
        pass


class PayloadEncodingError(__aiohttp_http_exceptions.BadHttpMessage):
    """ Base class for payload errors """
    def __init__(self, message, *, headers=None): # reliably restored by inspect
        # no doc
        pass


class ContentLengthError(__aiohttp_http_exceptions.PayloadEncodingError):
    """ Not enough data for satisfy content length header. """
    def __init__(self, message, *, headers=None): # reliably restored by inspect
        # no doc
        pass


class HttpRequestParser(HttpParser):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0xffffabaa9510>'


class HttpResponseParser(HttpParser):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0xffffabaa9570>'


class InvalidHeader(__aiohttp_http_exceptions.BadHttpMessage):
    # no doc
    def __init__(self, hdr): # reliably restored by inspect
        # no doc
        pass


class InvalidURLError(__aiohttp_http_exceptions.BadHttpMessage):
    # no doc
    def __init__(self, message, *, headers=None): # reliably restored by inspect
        # no doc
        pass


class LineTooLong(__aiohttp_http_exceptions.BadHttpMessage):
    # no doc
    def __init__(self, line, limit=None, actual_size=None): # reliably restored by inspect
        # no doc
        pass


class RawRequestMessage(object):
    # no doc
    def _replace(self, *args, **kwargs): # real signature unknown
        pass

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

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    chunked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    compression = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    headers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    raw_headers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    should_close = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    upgrade = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    url = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class RawResponseMessage(object):
    # no doc
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

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    chunked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    compression = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    headers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    raw_headers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reason = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    should_close = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    upgrade = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class TransferEncodingError(__aiohttp_http_exceptions.PayloadEncodingError):
    """ transfer encoding error. """
    def __init__(self, message, *, headers=None): # reliably restored by inspect
        # no doc
        pass


class _DeflateBuffer(object):
    """ DeflateStream decompress stream and feed data into specified stream. """
    def begin_http_chunk_receiving(self): # reliably restored by inspect
        # no doc
        pass

    def end_http_chunk_receiving(self): # reliably restored by inspect
        # no doc
        pass

    def feed_data(self, chunk, size): # reliably restored by inspect
        # no doc
        pass

    def feed_eof(self): # reliably restored by inspect
        # no doc
        pass

    def set_exception(self, exc): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, out, encoding): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __annotations__ = {
        'decompressor': typing.Any,
    }
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'aiohttp.http_parser', '__annotations__': {'decompressor': typing.Any}, '__doc__': 'DeflateStream decompress stream and feed data into specified stream.', '__init__': <function DeflateBuffer.__init__ at 0xffffabaa0550>, 'set_exception': <function DeflateBuffer.set_exception at 0xffffabaa05e0>, 'feed_data': <function DeflateBuffer.feed_data at 0xffffabaa0670>, 'feed_eof': <function DeflateBuffer.feed_eof at 0xffffabaa0700>, 'begin_http_chunk_receiving': <function DeflateBuffer.begin_http_chunk_receiving at 0xffffabaa0790>, 'end_http_chunk_receiving': <function DeflateBuffer.end_http_chunk_receiving at 0xffffabaa0820>, '__dict__': <attribute '__dict__' of 'DeflateBuffer' objects>, '__weakref__': <attribute '__weakref__' of 'DeflateBuffer' objects>})"


class _HttpVersion(tuple):
    """ HttpVersion(major, minor) """
    def _asdict(self): # reliably restored by inspect
        """ Return a new dict which maps field names to their values. """
        pass

    @classmethod
    def _make(cls, *args, **kwargs): # real signature unknown
        """ Make a new HttpVersion object from a sequence or iterable """
        pass

    def _replace(self, **kwds): # reliably restored by inspect
        """ Return a new HttpVersion object replacing specified fields with new values """
        pass

    def __getnewargs__(self): # reliably restored by inspect
        """ Return self as a plain tuple.  Used by copy and pickle. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(_cls, major, minor): # reliably restored by inspect
        """ Create new instance of HttpVersion(major, minor) """
        pass

    def __repr__(self): # reliably restored by inspect
        """ Return a nicely formatted representation string """
        pass

    major = None # (!) real value is '<_collections._tuplegetter object at 0xffffab30e280>'
    minor = None # (!) real value is '<_collections._tuplegetter object at 0xffffab30e250>'
    _fields = (
        'major',
        'minor',
    )
    _fields_defaults = {}
    _field_defaults = {}
    _field_types = {
        'major': int,
        'minor': '<value is a self-reference, replaced by this string>',
    }
    __annotations__ = {
        'major': int,
        'minor': '<value is a self-reference, replaced by this string>',
    }
    __slots__ = ()


class _StreamReader(__aiohttp_streams.AsyncStreamReaderMixin):
    """
    An enhancement of asyncio.StreamReader.
    
        Supports asynchronous iteration by line, chunk or as available::
    
            async for line in reader:
                ...
            async for chunk in reader.iter_chunked(1024):
                ...
            async for slice in reader.iter_any():
                ...
    """
    def at_eof(self): # reliably restored by inspect
        """ Return True if the buffer is empty and 'feed_eof' was called. """
        pass

    def begin_http_chunk_receiving(self): # reliably restored by inspect
        # no doc
        pass

    def end_http_chunk_receiving(self): # reliably restored by inspect
        # no doc
        pass

    def exception(self): # reliably restored by inspect
        # no doc
        pass

    def feed_data(self, data, size=0): # reliably restored by inspect
        # no doc
        pass

    def feed_eof(self): # reliably restored by inspect
        # no doc
        pass

    def get_read_buffer_limits(self): # reliably restored by inspect
        # no doc
        pass

    def is_eof(self): # reliably restored by inspect
        """ Return True if  'feed_eof' was called. """
        pass

    def on_eof(self, callback): # reliably restored by inspect
        # no doc
        pass

    def read(self, n=-1): # reliably restored by inspect
        # no doc
        pass

    def readany(self): # reliably restored by inspect
        # no doc
        pass

    def readchunk(self): # reliably restored by inspect
        """
        Returns a tuple of (data, end_of_http_chunk).
        
                When chunked transfer
                encoding is used, end_of_http_chunk is a boolean indicating if the end
                of the data corresponds to the end of a HTTP chunk , otherwise it is
                always False.
        """
        pass

    def readexactly(self, n): # reliably restored by inspect
        # no doc
        pass

    def readline(self): # reliably restored by inspect
        # no doc
        pass

# Error generating skeleton for function readuntil: cannot use a string pattern on a bytes-like object

    def read_nowait(self, n=-1): # reliably restored by inspect
        # no doc
        pass

    def set_exception(self, exc): # reliably restored by inspect
        # no doc
        pass

    def unread_data(self, data): # reliably restored by inspect
        """ rollback reading some data from stream, inserting it to buffer head. """
        pass

    def wait_eof(self): # reliably restored by inspect
        # no doc
        pass

    def _read_nowait(self, n): # reliably restored by inspect
        """ Read not more than n bytes, or whole buffer if n == -1 """
        pass

    def _read_nowait_chunk(self, n): # reliably restored by inspect
        # no doc
        pass

    def _wait(self, func_name): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, protocol, limit, *, timer=None, loop=None): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    total_bytes = 0


class _URL(object):
    # no doc
    @classmethod
    def build(cls, *args, **kwargs): # real signature unknown
        """ Creates and returns a new URL """
        pass

    def human_repr(self): # reliably restored by inspect
        """ Return decoded human readable string for URL representation. """
        pass

    def is_absolute(self): # reliably restored by inspect
        """
        A check for absolute URLs.
        
                Return True for absolute ones (having scheme or starting
                with //), False otherwise.
        """
        pass

    def is_default_port(self): # reliably restored by inspect
        """
        A check for default port.
        
                Return True if port is default for specified scheme,
                e.g. 'http://python.org' or 'http://python.org:80', False
                otherwise.
        """
        pass

    def join(self, url): # reliably restored by inspect
        """
        Join URLs
        
                Construct a full (“absolute”) URL by combining a “base URL”
                (self) with another URL (url).
        
                Informally, this uses components of the base URL, in
                particular the addressing scheme, the network location and
                (part of) the path, to provide missing components in the
                relative URL.
        """
        pass

    def joinpath(self, *other, encoded=False): # reliably restored by inspect
        """ Return a new URL with the elements in other appended to the path. """
        pass

    def origin(self): # reliably restored by inspect
        """
        Return an URL with scheme, host and port parts only.
        
                user, password, path, query and fragment are removed.
        """
        pass

    def relative(self): # reliably restored by inspect
        """
        Return a relative part of the URL.
        
                scheme, user, password, host and port are removed.
        """
        pass

    def update_query(self, *args, **kwargs): # reliably restored by inspect
        """ Return a new URL with query part updated. """
        pass

    def with_fragment(self, fragment): # reliably restored by inspect
        """
        Return a new URL with fragment replaced.
        
                Autoencode fragment if needed.
        
                Clear fragment to default if None is passed.
        """
        pass

    def with_host(self, host): # reliably restored by inspect
        """
        Return a new URL with host replaced.
        
                Autoencode host if needed.
        
                Changing host for relative URLs is not allowed, use .join()
                instead.
        """
        pass

    def with_name(self, name): # reliably restored by inspect
        """
        Return a new URL with name (last part of path) replaced.
        
                Query and fragment parts are cleaned up.
        
                Name is encoded if needed.
        """
        pass

    def with_password(self, password): # reliably restored by inspect
        """
        Return a new URL with password replaced.
        
                Autoencode password if needed.
        
                Clear password if argument is None.
        """
        pass

    def with_path(self, path, *, encoded=False): # reliably restored by inspect
        """ Return a new URL with path replaced. """
        pass

    def with_port(self, port): # reliably restored by inspect
        """
        Return a new URL with port replaced.
        
                Clear port to default if None is passed.
        """
        pass

    def with_query(self, *args, **kwargs): # reliably restored by inspect
        """
        Return a new URL with query part replaced.
        
                Accepts any Mapping (e.g. dict, multidict.MultiDict instances)
                or str, autoencode the argument if needed.
        
                A sequence of (key, value) pairs is supported as well.
        
                It also can take an arbitrary number of keyword arguments.
        
                Clear query if None is passed.
        """
        pass

    def with_scheme(self, scheme): # reliably restored by inspect
        """ Return a new URL with scheme replaced. """
        pass

    def with_suffix(self, suffix): # reliably restored by inspect
        """
        Return a new URL with suffix (file extension of name) replaced.
        
                Query and fragment parts are cleaned up.
        
                suffix is encoded if needed.
        """
        pass

    def with_user(self, user): # reliably restored by inspect
        """
        Return a new URL with user replaced.
        
                Autoencode user if needed.
        
                Clear user/password if user is None.
        """
        pass

    @classmethod
    def _encode_host(cls, *args, **kwargs): # real signature unknown
        pass

    def _FRAGMENT_QUOTER(self, *args, **kwargs): # real signature unknown
        pass

    def _FRAGMENT_REQUOTER(self, *args, **kwargs): # real signature unknown
        pass

    def _get_str_query(self, *args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def _make_child(self, segments, encoded=False): # reliably restored by inspect
        """ add segments to self._val.path, accounting for absolute vs relative paths """
        pass

    @classmethod
    def _make_netloc(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def _normalize_path(cls, *args, **kwargs): # real signature unknown
        pass

    def _PATH_QUOTER(self, *args, **kwargs): # real signature unknown
        pass

    def _PATH_REQUOTER(self, *args, **kwargs): # real signature unknown
        pass

    def _PATH_UNQUOTER(self, *args, **kwargs): # real signature unknown
        pass

    def _QS_UNQUOTER(self, *args, **kwargs): # real signature unknown
        pass

    def _QUERY_PART_QUOTER(self, *args, **kwargs): # real signature unknown
        pass

    def _QUERY_QUOTER(self, *args, **kwargs): # real signature unknown
        pass

    def _QUERY_REQUOTER(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def _query_seq_pairs(cls, *args, **kwargs): # real signature unknown
        pass

    def _query_var(v): # reliably restored by inspect
        # no doc
        pass

    def _QUOTER(self, *args, **kwargs): # real signature unknown
        pass

    def _REQUOTER(self, *args, **kwargs): # real signature unknown
        pass

    def _UNQUOTER(self, *args, **kwargs): # real signature unknown
        pass

    def _validate_authority_uri_abs_path(host, path): # reliably restored by inspect
        """
        Ensure that path in URL with authority starts with a leading slash.
        
                Raise ValueError if not.
        """
        pass

    def __bool__(self): # reliably restored by inspect
        # no doc
        pass

    def __bytes__(self): # reliably restored by inspect
        # no doc
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __getstate__(self): # reliably restored by inspect
        # no doc
        pass

    def __ge__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __gt__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __hash__(self): # reliably restored by inspect
        # no doc
        pass

    @classmethod
    def __init_subclass__(cls, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __lt__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __mod__(self, query): # reliably restored by inspect
        # no doc
        pass

    @staticmethod # known case of __new__
    def __new__(cls, val=None, *, encoded=False, strict=None): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    def __setstate__(self, state): # reliably restored by inspect
        # no doc
        pass

    def __str__(self): # reliably restored by inspect
        # no doc
        pass

    def __truediv__(self, name): # reliably restored by inspect
        # no doc
        pass

    explicit_port = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Port part of URL, without scheme-based fallback.

        None for relative URLs or URLs without explicit port.

        """

    port = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Port part of URL, with scheme-based fallback.

        None for relative URLs or URLs without explicit port and
        scheme without default port substitution.

        """

    raw_authority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Encoded authority part of URL.

        Empty string for relative URLs.

        """

    raw_fragment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Encoded fragment part of URL.

        Empty string if fragment is missing.

        """

    raw_host = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Encoded host part of URL.

        None for relative URLs.

        """

    raw_password = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Encoded password part of URL.

        None if password is missing.

        """

    raw_path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Encoded path of URL.

        / for absolute URLs without path part.

        """

    raw_query_string = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Encoded query part of URL.

        Empty string if query is missing.

        """

    raw_user = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Encoded user part of URL.

        None if user is missing.

        """

    scheme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Scheme for absolute URLs.

        Empty string for relative URLs or URLs starting with //

        """

    _cache = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _val = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    authority = None # (!) real value is '<yarl._url.cached_property object at 0xffffacbe5d00>'
    fragment = None # (!) real value is '<yarl._url.cached_property object at 0xffffab97e3d0>'
    host = None # (!) real value is '<yarl._url.cached_property object at 0xffffacacedf0>'
    name = None # (!) real value is '<yarl._url.cached_property object at 0xffffab97e610>'
    parent = None # (!) real value is '<yarl._url.cached_property object at 0xffffab97e4f0>'
    parts = None # (!) real value is '<yarl._url.cached_property object at 0xffffab97e490>'
    password = None # (!) real value is '<yarl._url.cached_property object at 0xffffab9fb4f0>'
    path = None # (!) real value is '<yarl._url.cached_property object at 0xffffacaceeb0>'
    path_qs = None # (!) real value is '<yarl._url.cached_property object at 0xffffab97e310>'
    query = None # (!) real value is '<yarl._url.cached_property object at 0xffffab9fee50>'
    query_string = None # (!) real value is '<yarl._url.cached_property object at 0xffffab97e250>'
    raw_name = None # (!) real value is '<yarl._url.cached_property object at 0xffffab97e580>'
    raw_parts = None # (!) real value is '<yarl._url.cached_property object at 0xffffab97e430>'
    raw_path_qs = None # (!) real value is '<yarl._url.cached_property object at 0xffffab97e370>'
    raw_suffix = None # (!) real value is '<yarl._url.cached_property object at 0xffffab97e670>'
    raw_suffixes = None # (!) real value is '<yarl._url.cached_property object at 0xffffab97e730>'
    suffix = None # (!) real value is '<yarl._url.cached_property object at 0xffffab97e6d0>'
    suffixes = None # (!) real value is '<yarl._url.cached_property object at 0xffffab97e790>'
    user = None # (!) real value is '<yarl._url.cached_property object at 0xffffacbe5d60>'
    __slots__ = (
        '_cache',
        '_val',
    )


# variables with complex values


_HttpVersion10 = (
    1,
    0,
)

_HttpVersion11 = (
    1,
    1,
)

__all__ = (
    'HttpRequestParser',
    'HttpResponseParser',
    'RawRequestMessage',
    'RawResponseMessage',
)

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffffabaa9370>'

__spec__ = None # (!) real value is "ModuleSpec(name='aiohttp._http_parser', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffffabaa9370>, origin='/.venv/lib/python3.8/site-packages/aiohttp/_http_parser.cpython-38-aarch64-linux-gnu.so')"

__test__ = {}

