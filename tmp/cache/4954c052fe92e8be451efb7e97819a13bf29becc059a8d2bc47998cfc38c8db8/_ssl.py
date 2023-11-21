# encoding: utf-8
# module _ssl
# from /usr/local/lib/python3.8/lib-dynload/_ssl.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
"""
Implementation module for SSL socket operations.  See the socket module
for documentation.
"""

# imports
import ssl as __ssl


# Variables with simple values

ALERT_DESCRIPTION_ACCESS_DENIED = 49

ALERT_DESCRIPTION_BAD_CERTIFICATE = 42

ALERT_DESCRIPTION_BAD_CERTIFICATE_HASH_VALUE = 114

ALERT_DESCRIPTION_BAD_CERTIFICATE_STATUS_RESPONSE = 113

ALERT_DESCRIPTION_BAD_RECORD_MAC = 20

ALERT_DESCRIPTION_CERTIFICATE_EXPIRED = 45
ALERT_DESCRIPTION_CERTIFICATE_REVOKED = 44
ALERT_DESCRIPTION_CERTIFICATE_UNKNOWN = 46
ALERT_DESCRIPTION_CERTIFICATE_UNOBTAINABLE = 111

ALERT_DESCRIPTION_CLOSE_NOTIFY = 0

ALERT_DESCRIPTION_DECODE_ERROR = 50

ALERT_DESCRIPTION_DECOMPRESSION_FAILURE = 30

ALERT_DESCRIPTION_DECRYPT_ERROR = 51

ALERT_DESCRIPTION_HANDSHAKE_FAILURE = 40

ALERT_DESCRIPTION_ILLEGAL_PARAMETER = 47

ALERT_DESCRIPTION_INSUFFICIENT_SECURITY = 71

ALERT_DESCRIPTION_INTERNAL_ERROR = 80

ALERT_DESCRIPTION_NO_RENEGOTIATION = 100

ALERT_DESCRIPTION_PROTOCOL_VERSION = 70

ALERT_DESCRIPTION_RECORD_OVERFLOW = 22

ALERT_DESCRIPTION_UNEXPECTED_MESSAGE = 10

ALERT_DESCRIPTION_UNKNOWN_CA = 48

ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY = 115

ALERT_DESCRIPTION_UNRECOGNIZED_NAME = 112

ALERT_DESCRIPTION_UNSUPPORTED_CERTIFICATE = 43
ALERT_DESCRIPTION_UNSUPPORTED_EXTENSION = 110

ALERT_DESCRIPTION_USER_CANCELLED = 90

CERT_NONE = 0
CERT_OPTIONAL = 1
CERT_REQUIRED = 2

HAS_ALPN = True
HAS_ECDH = True
HAS_NPN = False
HAS_SNI = True
HAS_SSLv2 = False
HAS_SSLv3 = False
HAS_TLSv1 = True

HAS_TLSv1_1 = True
HAS_TLSv1_2 = True
HAS_TLSv1_3 = True

HAS_TLS_UNIQUE = True

HOSTFLAG_ALWAYS_CHECK_SUBJECT = 1

HOSTFLAG_MULTI_LABEL_WILDCARDS = 8

HOSTFLAG_NEVER_CHECK_SUBJECT = 32

HOSTFLAG_NO_PARTIAL_WILDCARDS = 4

HOSTFLAG_NO_WILDCARDS = 2

HOSTFLAG_SINGLE_LABEL_SUBDOMAINS = 16

OPENSSL_VERSION = 'OpenSSL 3.0.11 19 Sep 2023'

OPENSSL_VERSION_NUMBER = 805306544

OP_ALL = 2147483728

OP_CIPHER_SERVER_PREFERENCE = 4194304

OP_ENABLE_MIDDLEBOX_COMPAT = 1048576

OP_IGNORE_UNEXPECTED_EOF = 128

OP_NO_COMPRESSION = 131072
OP_NO_RENEGOTIATION = 1073741824
OP_NO_SSLv2 = 0
OP_NO_SSLv3 = 33554432
OP_NO_TICKET = 16384
OP_NO_TLSv1 = 67108864

OP_NO_TLSv1_1 = 268435456
OP_NO_TLSv1_2 = 134217728
OP_NO_TLSv1_3 = 536870912

OP_SINGLE_DH_USE = 0

OP_SINGLE_ECDH_USE = 0

PROTOCOL_SSLv23 = 2
PROTOCOL_TLS = 2
PROTOCOL_TLSv1 = 3

PROTOCOL_TLSv1_1 = 4
PROTOCOL_TLSv1_2 = 5

PROTOCOL_TLS_CLIENT = 16
PROTOCOL_TLS_SERVER = 17

PROTO_MAXIMUM_SUPPORTED = -1

PROTO_MINIMUM_SUPPORTED = -2

PROTO_SSLv3 = 768
PROTO_TLSv1 = 769

PROTO_TLSv1_1 = 770
PROTO_TLSv1_2 = 771
PROTO_TLSv1_3 = 772

SSL_ERROR_EOF = 8

SSL_ERROR_INVALID_ERROR_CODE = 10

SSL_ERROR_SSL = 1
SSL_ERROR_SYSCALL = 5

SSL_ERROR_WANT_CONNECT = 7
SSL_ERROR_WANT_READ = 2
SSL_ERROR_WANT_WRITE = 3

SSL_ERROR_WANT_X509_LOOKUP = 4

SSL_ERROR_ZERO_RETURN = 6

VERIFY_CRL_CHECK_CHAIN = 12
VERIFY_CRL_CHECK_LEAF = 4

VERIFY_DEFAULT = 0

VERIFY_X509_STRICT = 32

VERIFY_X509_TRUSTED_FIRST = 32768

_DEFAULT_CIPHERS = 'DEFAULT:!aNULL:!eNULL:!MD5:!3DES:!DES:!RC4:!IDEA:!SEED:!aDSS:!SRP:!PSK'

# functions

def get_default_verify_paths(*args, **kwargs): # real signature unknown
    """
    Return search paths and environment vars that are used by SSLContext's set_default_verify_paths() to load default CAs.
    
    The values are 'cert_file_env', 'cert_file', 'cert_dir_env', 'cert_dir'.
    """
    pass

def nid2obj(*args, **kwargs): # real signature unknown
    """ Lookup NID, short name, long name and OID of an ASN1_OBJECT by NID. """
    pass

def RAND_add(*args, **kwargs): # real signature unknown
    """
    Mix string into the OpenSSL PRNG state.
    
    entropy (a float) is a lower bound on the entropy contained in
    string.  See RFC 4086.
    """
    pass

def RAND_bytes(*args, **kwargs): # real signature unknown
    """ Generate n cryptographically strong pseudo-random bytes. """
    pass

def RAND_pseudo_bytes(*args, **kwargs): # real signature unknown
    """
    Generate n pseudo-random bytes.
    
    Return a pair (bytes, is_cryptographic).  is_cryptographic is True
    if the bytes generated are cryptographically strong.
    """
    pass

def RAND_status(*args, **kwargs): # real signature unknown
    """
    Returns 1 if the OpenSSL PRNG has been seeded with enough data and 0 if not.
    
    It is necessary to seed the PRNG with RAND_add() on some platforms before
    using the ssl() function.
    """
    pass

def txt2obj(*args, **kwargs): # real signature unknown
    """
    Lookup NID, short name, long name and OID of an ASN1_OBJECT.
    
    By default objects are looked up by OID. With name=True short and
    long name are also matched.
    """
    pass

def _test_decode_cert(*args, **kwargs): # real signature unknown
    pass

# classes

class MemoryBIO(object):
    # no doc
    def read(self, *args, **kwargs): # real signature unknown
        """
        Read up to size bytes from the memory BIO.
        
        If size is not specified, read the entire buffer.
        If the return value is an empty bytes instance, this means either
        EOF or that no data is available. Use the "eof" property to
        distinguish between the two.
        """
        pass

    def write(self, *args, **kwargs): # real signature unknown
        """
        Writes the bytes b into the memory BIO.
        
        Returns the number of bytes written.
        """
        pass

    def write_eof(self, *args, **kwargs): # real signature unknown
        """
        Write an EOF marker to the memory BIO.
        
        When all data has been read, the "eof" property will be True.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    eof = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether the memory BIO is at EOF."""

    pending = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of bytes pending in the memory BIO."""



class SSLError(OSError):
    """ An error occurred in the SSL implementation. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass


class SSLCertVerificationError(__ssl.SSLError, ValueError):
    """ A certificate could not be verified. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class SSLEOFError(__ssl.SSLError):
    """ SSL/TLS connection terminated abruptly. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class SSLSession(object):
    # no doc
    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    has_ticket = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Does the session contain a ticket?"""

    id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Session id"""

    ticket_lifetime_hint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Ticket life time hint."""

    time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Session creation time (seconds since epoch)."""

    timeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Session timeout (delta in seconds)."""


    __hash__ = None


class SSLSyscallError(__ssl.SSLError):
    """ System error when attempting SSL operation. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class SSLWantReadError(__ssl.SSLError):
    """
    Non-blocking SSL socket needs to read more data
    before the requested operation can be completed.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class SSLWantWriteError(__ssl.SSLError):
    """
    Non-blocking SSL socket needs to write more data
    before the requested operation can be completed.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class SSLZeroReturnError(__ssl.SSLError):
    """ SSL/TLS session closed cleanly. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class _SSLContext(object):
    # no doc
    def cert_store_stats(self, *args, **kwargs): # real signature unknown
        """
        Returns quantities of loaded X.509 certificates.
        
        X.509 certificates with a CA extension and certificate revocation lists
        inside the context's cert store.
        
        NOTE: Certificates in a capath directory aren't loaded unless they have
        been used at least once.
        """
        pass

    def get_ca_certs(self, *args, **kwargs): # real signature unknown
        """
        Returns a list of dicts with information of loaded CA certs.
        
        If the optional argument is True, returns a DER-encoded copy of the CA
        certificate.
        
        NOTE: Certificates in a capath directory aren't loaded unless they have
        been used at least once.
        """
        pass

    def get_ciphers(self, *args, **kwargs): # real signature unknown
        pass

    def load_cert_chain(self, *args, **kwargs): # real signature unknown
        pass

    def load_dh_params(self, *args, **kwargs): # real signature unknown
        pass

    def load_verify_locations(self, *args, **kwargs): # real signature unknown
        pass

    def session_stats(self, *args, **kwargs): # real signature unknown
        pass

    def set_ciphers(self, *args, **kwargs): # real signature unknown
        pass

    def set_default_verify_paths(self, *args, **kwargs): # real signature unknown
        pass

    def set_ecdh_curve(self, *args, **kwargs): # real signature unknown
        pass

    def _set_alpn_protocols(self, *args, **kwargs): # real signature unknown
        pass

    def _set_npn_protocols(self, *args, **kwargs): # real signature unknown
        pass

    def _wrap_bio(self, *args, **kwargs): # real signature unknown
        pass

    def _wrap_socket(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    check_hostname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    keylog_filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    maximum_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    minimum_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_tickets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Control the number of TLSv1.3 session tickets"""

    options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    post_handshake_auth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    protocol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sni_callback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set a callback that will be called when a server name is provided by the SSL/TLS client in the SNI extension.

If the argument is None then the callback is disabled. The method is called
with the SSLSocket, the server name as a string, and the SSLContext object.
See RFC 6066 for details of the SNI extension."""

    verify_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    verify_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _host_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _msg_callback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class _SSLSocket(object):
    # no doc
    def cipher(self, *args, **kwargs): # real signature unknown
        pass

    def compression(self, *args, **kwargs): # real signature unknown
        pass

    def do_handshake(self, *args, **kwargs): # real signature unknown
        pass

    def getpeercert(self, *args, **kwargs): # real signature unknown
        """
        Returns the certificate for the peer.
        
        If no certificate was provided, returns None.  If a certificate was
        provided, but not validated, returns an empty dictionary.  Otherwise
        returns a dict containing information about the peer certificate.
        
        If the optional argument is True, returns a DER-encoded copy of the
        peer certificate, or None if no certificate was provided.  This will
        return the certificate even if it wasn't validated.
        """
        pass

    def get_channel_binding(self, *args, **kwargs): # real signature unknown
        """
        Get channel binding data for current connection.
        
        Raise ValueError if the requested `cb_type` is not supported.  Return bytes
        of the data or None if the data is not available (e.g. before the handshake).
        Only 'tls-unique' channel binding data from RFC 5929 is supported.
        """
        pass

    def pending(self, *args, **kwargs): # real signature unknown
        """ Returns the number of already decrypted bytes available for read, pending on the connection. """
        pass

    def read(self, size, buffer=None): # real signature unknown; restored from __doc__
        """
        read(size, [buffer])
        Read up to size bytes from the SSL socket.
        """
        pass

    def selected_alpn_protocol(self, *args, **kwargs): # real signature unknown
        pass

    def shared_ciphers(self, *args, **kwargs): # real signature unknown
        pass

    def shutdown(self, *args, **kwargs): # real signature unknown
        """ Does the SSL shutdown handshake with the remote end. """
        pass

    def verify_client_post_handshake(self, *args, **kwargs): # real signature unknown
        """ Initiate TLS 1.3 post-handshake authentication """
        pass

    def version(self, *args, **kwargs): # real signature unknown
        pass

    def write(self, *args, **kwargs): # real signature unknown
        """
        Writes the bytes-like object b into the SSL object.
        
        Returns the number of bytes written.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """_setter_context(ctx)
This changes the context associated with the SSLSocket. This is typically
used from within a callback function set by the sni_callback
on the SSLContext to change the certificate information associated with the
SSLSocket before the cryptographic exchange handshake messages
"""

    owner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Python-level owner of this object.Passed as "self" in servername callback."""

    server_hostname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The currently set server hostname (for SNI)."""

    server_side = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether this is a server-side socket."""

    session = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """_setter_session(session)
Get / set SSLSession."""

    session_reused = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Was the client session reused during handshake?"""



# variables with complex values

err_codes_to_names = {
    (
        3,
        100,
    ): 
        'ARG2_LT_ARG3'
    ,
    (
        3,
        101,
    ): 
        'BAD_RECIPROCAL'
    ,
    (
        3,
        102,
    ): 
        'CALLED_WITH_EVEN_MODULUS'
    ,
    (
        3,
        103,
    ): 
        'DIV_BY_ZERO'
    ,
    (
        3,
        104,
    ): 
        'ENCODING_ERROR'
    ,
    (
        3,
        105,
    ): 
        'EXPAND_ON_STATIC_BIGNUM_DATA'
    ,
    (
        3,
        106,
    ): 
        'INVALID_LENGTH'
    ,
    (
        3,
        107,
    ): 
        'NOT_INITIALIZED'
    ,
    (
        3,
        108,
    ): 
        'NO_INVERSE'
    ,
    (
        3,
        109,
    ): 
        'TOO_MANY_TEMPORARY_VARIABLES'
    ,
    (
        3,
        110,
    ): 
        'INPUT_NOT_REDUCED'
    ,
    (
        3,
        111,
    ): 
        'NOT_A_SQUARE'
    ,
    (
        3,
        112,
    ): 
        'P_IS_NOT_PRIME'
    ,
    (
        3,
        113,
    ): 
        'TOO_MANY_ITERATIONS'
    ,
    (
        3,
        114,
    ): 
        'BIGNUM_TOO_LONG'
    ,
    (
        3,
        115,
    ): 
        'INVALID_RANGE'
    ,
    (
        3,
        116,
    ): 
        'NO_SOLUTION'
    ,
    (
        3,
        117,
    ): 
        'PRIVATE_KEY_TOO_LARGE'
    ,
    (
        3,
        118,
    ): 
        'BITS_TOO_SMALL'
    ,
    (
        3,
        119,
    ): 
        'INVALID_SHIFT'
    ,
    (
        3,
        120,
    ): 
        'NO_SUITABLE_DIGEST'
    ,
    (
        3,
        121,
    ): 
        'NO_PRIME_CANDIDATE'
    ,
    (
        4,
        100,
    ): 
        'ALGORITHM_MISMATCH'
    ,
    (
        4,
        101,
    ): 
        'BAD_E_VALUE'
    ,
    (
        4,
        102,
    ): 
        'BAD_FIXED_HEADER_DECRYPT'
    ,
    (
        4,
        103,
    ): 
        'BAD_PAD_BYTE_COUNT'
    ,
    (
        4,
        104,
    ): 
        'BAD_SIGNATURE'
    ,
    (
        4,
        105,
    ): 
        'MODULUS_TOO_LARGE'
    ,
    (
        4,
        106,
    ): 
        'BLOCK_TYPE_IS_NOT_01'
    ,
    (
        4,
        107,
    ): 
        'BLOCK_TYPE_IS_NOT_02'
    ,
    (
        4,
        108,
    ): 
        'DATA_GREATER_THAN_MOD_LEN'
    ,
    (
        4,
        109,
    ): 
        'DATA_TOO_LARGE'
    ,
    (
        4,
        110,
    ): 
        'DATA_TOO_LARGE_FOR_KEY_SIZE'
    ,
    (
        4,
        111,
    ): 
        'DATA_TOO_SMALL'
    ,
    (
        4,
        112,
    ): 
        'DIGEST_TOO_BIG_FOR_RSA_KEY'
    ,
    (
        4,
        113,
    ): 
        'NULL_BEFORE_BLOCK_MISSING'
    ,
    (
        4,
        114,
    ): 
        'PADDING_CHECK_FAILED'
    ,
    (
        4,
        115,
    ): 
        'SSLV3_ROLLBACK_ATTACK'
    ,
    (
        4,
        116,
    ): 
        'THE_ASN1_OBJECT_IDENTIFIER_IS_NOT_KNOWN_FOR_THIS_MD'
    ,
    (
        4,
        117,
    ): 
        'UNKNOWN_ALGORITHM_TYPE'
    ,
    (
        4,
        118,
    ): 
        'UNKNOWN_PADDING_TYPE'
    ,
    (
        4,
        119,
    ): 
        'WRONG_SIGNATURE_LENGTH'
    ,
    (
        4,
        120,
    ): 
        'KEY_SIZE_TOO_SMALL'
    ,
    (
        4,
        121,
    ): 
        'OAEP_DECODING_ERROR'
    ,
    (
        4,
        122,
    ): 
        'DATA_TOO_SMALL_FOR_KEY_SIZE'
    ,
    (
        4,
        123,
    ): 
        'D_E_NOT_CONGRUENT_TO_1'
    ,
    (
        4,
        124,
    ): 
        'DMP1_NOT_CONGRUENT_TO_D'
    ,
    (
        4,
        125,
    ): 
        'DMQ1_NOT_CONGRUENT_TO_D'
    ,
    (
        4,
        126,
    ): 
        'IQMP_NOT_INVERSE_OF_Q'
    ,
    (
        4,
        127,
    ): 
        'N_DOES_NOT_EQUAL_P_Q'
    ,
    (
        4,
        128,
    ): 
        'P_NOT_PRIME'
    ,
    (
        4,
        129,
    ): 
        'Q_NOT_PRIME'
    ,
    (
        4,
        130,
    ): 
        'RSA_OPERATIONS_NOT_SUPPORTED'
    ,
    (
        4,
        131,
    ): 
        'INVALID_MESSAGE_LENGTH'
    ,
    (
        4,
        132,
    ): 
        'DATA_TOO_LARGE_FOR_MODULUS'
    ,
    (
        4,
        133,
    ): 
        'FIRST_OCTET_INVALID'
    ,
    (
        4,
        134,
    ): 
        'LAST_OCTET_INVALID'
    ,
    (
        4,
        135,
    ): 
        'SLEN_RECOVERY_FAILED'
    ,
    (
        4,
        136,
    ): 
        'SLEN_CHECK_FAILED'
    ,
    (
        4,
        137,
    ): 
        'INVALID_HEADER'
    ,
    (
        4,
        138,
    ): 
        'INVALID_PADDING'
    ,
    (
        4,
        139,
    ): 
        'INVALID_TRAILER'
    ,
    (
        4,
        140,
    ): 
        'NO_PUBLIC_EXPONENT'
    ,
    (
        4,
        141,
    ): 
        'INVALID_PADDING_MODE'
    ,
    (
        4,
        142,
    ): 
        'INVALID_X931_DIGEST'
    ,
    (
        4,
        143,
    ): 
        'INVALID_DIGEST_LENGTH'
    ,
    (
        4,
        144,
    ): 
        'ILLEGAL_OR_UNSUPPORTED_PADDING_MODE'
    ,
    (
        4,
        145,
    ): 
        'DIGEST_NOT_ALLOWED'
    ,
    (
        4,
        146,
    ): 
        'INVALID_PSS_SALTLEN'
    ,
    (
        4,
        147,
    ): 
        'VALUE_MISSING'
    ,
    (
        4,
        148,
    ): 
        'OPERATION_NOT_SUPPORTED_FOR_THIS_KEYTYPE'
    ,
    (
        4,
        149,
    ): 
        'INVALID_PSS_PARAMETERS'
    ,
    (
        4,
        150,
    ): 
        'INVALID_SALT_LENGTH'
    ,
    (
        4,
        151,
    ): 
        'UNKNOWN_MASK_DIGEST'
    ,
    (
        4,
        152,
    ): 
        'MGF1_DIGEST_NOT_ALLOWED'
    ,
    (
        4,
        153,
    ): 
        'UNSUPPORTED_MASK_ALGORITHM'
    ,
    (
        4,
        154,
    ): 
        'UNSUPPORTED_MASK_PARAMETER'
    ,
    (
        4,
        155,
    ): 
        'UNSUPPORTED_SIGNATURE_TYPE'
    ,
    (
        4,
        156,
    ): 
        'INVALID_MGF1_MD'
    ,
    (
        4,
        157,
    ): 
        'INVALID_DIGEST'
    ,
    (
        4,
        158,
    ): 
        'DIGEST_DOES_NOT_MATCH'
    ,
    (
        4,
        159,
    ): 
        'PKCS_DECODING_ERROR'
    ,
    (
        4,
        160,
    ): 
        'INVALID_LABEL'
    ,
    (
        4,
        161,
    ): 
        'INVALID_OAEP_PARAMETERS'
    ,
    (
        4,
        162,
    ): 
        'UNSUPPORTED_ENCRYPTION_TYPE'
    ,
    (
        4,
        163,
    ): 
        'UNSUPPORTED_LABEL_SOURCE'
    ,
    (
        4,
        164,
    ): 
        'PSS_SALTLEN_TOO_SMALL'
    ,
    (
        4,
        165,
    ): 
        'KEY_PRIME_NUM_INVALID'
    ,
    (
        4,
        166,
    ): 
        'UNKNOWN_DIGEST'
    ,
    (
        4,
        167,
    ): 
        'INVALID_MULTI_PRIME_KEY'
    ,
    (
        4,
        168,
    ): 
        'MP_COEFFICIENT_NOT_INVERSE_OF_R'
    ,
    (
        4,
        169,
    ): 
        'MP_EXPONENT_NOT_CONGRUENT_TO_D'
    ,
    (
        4,
        170,
    ): 
        'MP_R_NOT_PRIME'
    ,
    (
        4,
        171,
    ): 
        'INVALID_KEYPAIR'
    ,
    (
        4,
        172,
    ): 
        'N_DOES_NOT_EQUAL_PRODUCT_OF_PRIMES'
    ,
    (
        4,
        173,
    ): 
        'INVALID_KEY_LENGTH'
    ,
    (
        4,
        174,
    ): 
        'INVALID_MODULUS'
    ,
    (
        4,
        175,
    ): 
        'INVALID_REQUEST'
    ,
    (
        4,
        176,
    ): 
        'INVALID_STRENGTH'
    ,
    (
        4,
        177,
    ): 
        'PAIRWISE_TEST_FAILURE'
    ,
    (
        4,
        178,
    ): 
        'PUB_EXPONENT_OUT_OF_RANGE'
    ,
    (
        4,
        179,
    ): 
        'MISSING_PRIVATE_KEY'
    ,
    (
        4,
        180,
    ): 
        'RANDOMNESS_SOURCE_STRENGTH_INSUFFICIENT'
    ,
    (
        4,
        181,
    ): 
        'INVALID_LENGTH'
    ,
    (
        5,
        100,
    ): 
        'NO_PRIVATE_VALUE'
    ,
    (
        5,
        101,
    ): 
        'BAD_GENERATOR'
    ,
    (
        5,
        102,
    ): 
        'INVALID_PUBKEY'
    ,
    (
        5,
        103,
    ): 
        'MODULUS_TOO_LARGE'
    ,
    (
        5,
        104,
    ): 
        'DECODE_ERROR'
    ,
    (
        5,
        105,
    ): 
        'PARAMETER_ENCODING_ERROR'
    ,
    (
        5,
        106,
    ): 
        'BN_ERROR'
    ,
    (
        5,
        107,
    ): 
        'NO_PARAMETERS_SET'
    ,
    (
        5,
        108,
    ): 
        'KEYS_NOT_SET'
    ,
    (
        5,
        109,
    ): 
        'BN_DECODE_ERROR'
    ,
    (
        5,
        110,
    ): 
        'INVALID_PARAMETER_NAME'
    ,
    (
        5,
        111,
    ): 
        'PEER_KEY_ERROR'
    ,
    (
        5,
        112,
    ): 
        'KDF_PARAMETER_ERROR'
    ,
    (
        5,
        113,
    ): 
        'SHARED_INFO_ERROR'
    ,
    (
        5,
        114,
    ): 
        'INVALID_PARAMETER_NID'
    ,
    (
        5,
        115,
    ): 
        'CHECK_INVALID_J_VALUE'
    ,
    (
        5,
        116,
    ): 
        'CHECK_INVALID_Q_VALUE'
    ,
    (
        5,
        117,
    ): 
        'CHECK_P_NOT_PRIME'
    ,
    (
        5,
        118,
    ): 
        'CHECK_P_NOT_SAFE_PRIME'
    ,
    (
        5,
        119,
    ): 
        'CHECK_Q_NOT_PRIME'
    ,
    (
        5,
        120,
    ): 
        'NOT_SUITABLE_GENERATOR'
    ,
    (
        5,
        121,
    ): 
        'UNABLE_TO_CHECK_GENERATOR'
    ,
    (
        5,
        122,
    ): 
        'CHECK_PUBKEY_INVALID'
    ,
    (
        5,
        123,
    ): 
        'CHECK_PUBKEY_TOO_LARGE'
    ,
    (
        5,
        124,
    ): 
        'CHECK_PUBKEY_TOO_SMALL'
    ,
    (
        5,
        125,
    ): 
        'MISSING_PUBKEY'
    ,
    (
        5,
        126,
    ): 
        'MODULUS_TOO_SMALL'
    ,
    (
        5,
        127,
    ): 
        'BAD_FFC_PARAMETERS'
    ,
    (
        5,
        128,
    ): 
        'INVALID_SECRET'
    ,
    (
        6,
        100,
    ): 
        'BAD_DECRYPT'
    ,
    (
        6,
        101,
    ): 
        'DIFFERENT_KEY_TYPES'
    ,
    (
        6,
        103,
    ): 
        'MISSING_PARAMETERS'
    ,
    (
        6,
        106,
    ): 
        'PUBLIC_KEY_NOT_RSA'
    ,
    (
        6,
        107,
    ): 
        'UNSUPPORTED_CIPHER'
    ,
    (
        6,
        108,
    ): 
        'UNSUPPORTED_KEY_SIZE'
    ,
    (
        6,
        109,
    ): 
        'WRONG_FINAL_BLOCK_LENGTH'
    ,
    (
        6,
        111,
    ): 
        'INPUT_NOT_INITIALIZED'
    ,
    (
        6,
        114,
    ): 
        'DECODE_ERROR'
    ,
    (
        6,
        118,
    ): 
        'UNSUPPORTED_PRIVATE_KEY_ALGORITHM'
    ,
    (
        6,
        121,
    ): 
        'UNKNOWN_PBE_ALGORITHM'
    ,
    (
        6,
        122,
    ): 
        'CIPHER_PARAMETER_ERROR'
    ,
    (
        6,
        123,
    ): 
        'UNSUPPORTED_KEYLENGTH'
    ,
    (
        6,
        124,
    ): 
        'UNSUPPORTED_KEY_DERIVATION_FUNCTION'
    ,
    (
        6,
        125,
    ): 
        'UNSUPPORTED_PRF'
    ,
    (
        6,
        126,
    ): 
        'UNSUPPORTED_SALT_TYPE'
    ,
    (
        6,
        127,
    ): 
        'EXPECTING_AN_RSA_KEY'
    ,
    (
        6,
        128,
    ): 
        'EXPECTING_A_DH_KEY'
    ,
    (
        6,
        129,
    ): 
        'EXPECTING_A_DSA_KEY'
    ,
    (
        6,
        130,
    ): 
        'INVALID_KEY_LENGTH'
    ,
    (
        6,
        131,
    ): 
        'NO_CIPHER_SET'
    ,
    (
        6,
        132,
    ): 
        'CTRL_NOT_IMPLEMENTED'
    ,
    (
        6,
        133,
    ): 
        'CTRL_OPERATION_NOT_IMPLEMENTED'
    ,
    (
        6,
        134,
    ): 
        'INITIALIZATION_ERROR'
    ,
    (
        6,
        135,
    ): 
        'UNSUPPORTED_NUMBER_OF_ROUNDS'
    ,
    (
        6,
        138,
    ): 
        'DATA_NOT_MULTIPLE_OF_BLOCK_LENGTH'
    ,
    (
        6,
        139,
    ): 
        'NO_DIGEST_SET'
    ,
    (
        6,
        142,
    ): 
        'EXPECTING_A_EC_KEY'
    ,
    (
        6,
        143,
    ): 
        'AES_KEY_SETUP_FAILED'
    ,
    (
        6,
        144,
    ): 
        'METHOD_NOT_SUPPORTED'
    ,
    (
        6,
        145,
    ): 
        'PRIVATE_KEY_DECODE_ERROR'
    ,
    (
        6,
        146,
    ): 
        'PRIVATE_KEY_ENCODE_ERROR'
    ,
    (
        6,
        147,
    ): 
        'COMMAND_NOT_SUPPORTED'
    ,
    (
        6,
        148,
    ): 
        'INVALID_OPERATION'
    ,
    (
        6,
        149,
    ): 
        'NO_OPERATION_SET'
    ,
    (
        6,
        150,
    ): 
        'OPERATION_NOT_SUPPORTED_FOR_THIS_KEYTYPE'
    ,
    (
        6,
        151,
    ): 
        'OPERATION_NOT_INITIALIZED'
    ,
    (
        6,
        152,
    ): 
        'INVALID_DIGEST'
    ,
    (
        6,
        153,
    ): 
        'DIFFERENT_PARAMETERS'
    ,
    (
        6,
        154,
    ): 
        'NO_KEY_SET'
    ,
    (
        6,
        155,
    ): 
        'BUFFER_TOO_SMALL'
    ,
    (
        6,
        156,
    ): 
        'UNSUPPORTED_ALGORITHM'
    ,
    (
        6,
        157,
    ): 
        'CAMELLIA_KEY_SETUP_FAILED'
    ,
    (
        6,
        158,
    ): 
        'NO_DEFAULT_DIGEST'
    ,
    (
        6,
        159,
    ): 
        'MESSAGE_DIGEST_IS_NULL'
    ,
    (
        6,
        160,
    ): 
        'UNKNOWN_CIPHER'
    ,
    (
        6,
        161,
    ): 
        'UNKNOWN_DIGEST'
    ,
    (
        6,
        162,
    ): 
        'PARTIALLY_OVERLAPPING'
    ,
    (
        6,
        163,
    ): 
        'INVALID_KEY'
    ,
    (
        6,
        164,
    ): 
        'EXPECTING_A_POLY1305_KEY'
    ,
    (
        6,
        165,
    ): 
        'ERROR_LOADING_SECTION'
    ,
    (
        6,
        166,
    ): 
        'ERROR_SETTING_FIPS_MODE'
    ,
    (
        6,
        167,
    ): 
        'FIPS_MODE_NOT_SUPPORTED'
    ,
    (
        6,
        168,
    ): 
        'INVALID_FIPS_MODE'
    ,
    (
        6,
        169,
    ): 
        'UNKNOWN_OPTION'
    ,
    (
        6,
        170,
    ): 
        'WRAP_MODE_NOT_ALLOWED'
    ,
    (
        6,
        171,
    ): 
        'ILLEGAL_SCRYPT_PARAMETERS'
    ,
    (
        6,
        172,
    ): 
        'MEMORY_LIMIT_EXCEEDED'
    ,
    (
        6,
        173,
    ): 
        'COPY_ERROR'
    ,
    (
        6,
        174,
    ): 
        'EXPECTING_AN_HMAC_KEY'
    ,
    (
        6,
        175,
    ): 
        'EXPECTING_A_SIPHASH_KEY'
    ,
    (
        6,
        176,
    ): 
        'ARIA_KEY_SETUP_FAILED'
    ,
    (
        6,
        177,
    ): 
        'ONLY_ONESHOT_SUPPORTED'
    ,
    (
        6,
        178,
    ): 
        'NOT_XOF_OR_INVALID_LENGTH'
    ,
    (
        6,
        179,
    ): 
        'PKEY_APPLICATION_ASN1_METHOD_ALREADY_REGISTERED'
    ,
    (
        6,
        180,
    ): 
        'KEY_SETUP_FAILED'
    ,
    (
        6,
        181,
    ): 
        'PBKDF2_ERROR'
    ,
    (
        6,
        182,
    ): 
        'GET_RAW_KEY_FAILED'
    ,
    (
        6,
        183,
    ): 
        'TOO_MANY_RECORDS'
    ,
    (
        6,
        184,
    ): 
        'CIPHER_NOT_GCM_MODE'
    ,
    (
        6,
        185,
    ): 
        'INVALID_CUSTOM_LENGTH'
    ,
    (
        6,
        186,
    ): 
        'INVALID_SALT_LENGTH'
    ,
    (
        6,
        187,
    ): 
        'PARAMETER_TOO_LARGE'
    ,
    (
        6,
        188,
    ): 
        'FINAL_ERROR'
    ,
    (
        6,
        189,
    ): 
        'UPDATE_ERROR'
    ,
    (
        6,
        190,
    ): 
        'NOT_ABLE_TO_COPY_CTX'
    ,
    (
        6,
        191,
    ): 
        'XTS_DATA_UNIT_IS_TOO_LARGE'
    ,
    (
        6,
        192,
    ): 
        'XTS_DUPLICATED_KEYS'
    ,
    (
        6,
        193,
    ): 
        'INVALID_PROVIDER_FUNCTIONS'
    ,
    (
        6,
        194,
    ): 
        'INVALID_IV_LENGTH'
    ,
    (
        6,
        195,
    ): 
        'BAD_KEY_LENGTH'
    ,
    (
        6,
        196,
    ): 
        'NO_KEYMGMT_PRESENT'
    ,
    (
        6,
        197,
    ): 
        'CANNOT_GET_PARAMETERS'
    ,
    (
        6,
        198,
    ): 
        'CANNOT_SET_PARAMETERS'
    ,
    (
        6,
        199,
    ): 
        'NO_KEYMGMT_AVAILABLE'
    ,
    (
        6,
        200,
    ): 
        'BAD_ALGORITHM_NAME'
    ,
    (
        6,
        201,
    ): 
        'CONFLICTING_ALGORITHM_NAME'
    ,
    (
        6,
        202,
    ): 
        'OUTPUT_WOULD_OVERFLOW'
    ,
    (
        6,
        203,
    ): 
        'INACCESSIBLE_KEY'
    ,
    (
        6,
        204,
    ): 
        'INACCESSIBLE_DOMAIN_PARAMETERS'
    ,
    (
        6,
        205,
    ): 
        'KEYMGMT_EXPORT_FAILURE'
    ,
    (
        6,
        206,
    ): 
        'NO_IMPORT_FUNCTION'
    ,
    (
        6,
        207,
    ): 
        'UNKNOWN_KEY_TYPE'
    ,
    (
        6,
        208,
    ): 
        'NULL_MAC_PKEY_CTX'
    ,
    (
        6,
        209,
    ): 
        'SET_DEFAULT_PROPERTY_FAILURE'
    ,
    (
        6,
        210,
    ): 
        'DEFAULT_QUERY_PARSE_ERROR'
    ,
    (
        6,
        211,
    ): 
        'UNABLE_TO_LOCK_CONTEXT'
    ,
    (
        6,
        212,
    ): 
        'UNABLE_TO_ENABLE_LOCKING'
    ,
    (
        6,
        213,
    ): 
        'LOCKING_NOT_SUPPORTED'
    ,
    (
        6,
        214,
    ): 
        'GENERATE_ERROR'
    ,
    (
        6,
        215,
    ): 
        'UNABLE_TO_GET_MAXIMUM_REQUEST_SIZE'
    ,
    (
        6,
        216,
    ): 
        'UNABLE_TO_GET_RANDOM_STRENGTH'
    ,
    (
        6,
        217,
    ): 
        'UNABLE_TO_SET_CALLBACKS'
    ,
    (
        6,
        218,
    ): 
        'INVALID_NULL_ALGORITHM'
    ,
    (
        6,
        219,
    ): 
        'EXPECTING_A_ECX_KEY'
    ,
    (
        6,
        220,
    ): 
        'INVALID_SEED_LENGTH'
    ,
    (
        6,
        221,
    ): 
        'INVALID_LENGTH'
    ,
    (
        6,
        222,
    ): 
        'INVALID_VALUE'
    ,
    (
        6,
        223,
    ): 
        'INVALID_SECRET_LENGTH'
    ,
    (
        6,
        224,
    ): 
        'UNSUPPORTED_KEY_TYPE'
    ,
    (
        6,
        225,
    ): 
        'CACHE_CONSTANTS_FAILED'
    ,
    (
        6,
        227,
    ): 
        'SETTING_XOF_FAILED'
    ,
    (
        8,
        101,
    ): 
        'UNKNOWN_NID'
    ,
    (
        8,
        102,
    ): 
        'OID_EXISTS'
    ,
    (
        8,
        103,
    ): 
        'UNKNOWN_OBJECT_NAME'
    ,
    (
        9,
        100,
    ): 
        'BAD_BASE64_DECODE'
    ,
    (
        9,
        101,
    ): 
        'BAD_DECRYPT'
    ,
    (
        9,
        102,
    ): 
        'BAD_END_LINE'
    ,
    (
        9,
        103,
    ): 
        'BAD_IV_CHARS'
    ,
    (
        9,
        104,
    ): 
        'BAD_PASSWORD_READ'
    ,
    (
        9,
        105,
    ): 
        'NOT_DEK_INFO'
    ,
    (
        9,
        106,
    ): 
        'NOT_ENCRYPTED'
    ,
    (
        9,
        107,
    ): 
        'NOT_PROC_TYPE'
    ,
    (
        9,
        108,
    ): 
        'NO_START_LINE'
    ,
    (
        9,
        109,
    ): 
        'PROBLEMS_GETTING_PASSWORD'
    ,
    (
        9,
        110,
    ): 
        'UNSUPPORTED_PUBLIC_KEY_TYPE'
    ,
    (
        9,
        111,
    ): 
        'READ_KEY'
    ,
    (
        9,
        112,
    ): 
        'SHORT_HEADER'
    ,
    (
        9,
        113,
    ): 
        'UNSUPPORTED_CIPHER'
    ,
    (
        9,
        114,
    ): 
        'UNSUPPORTED_ENCRYPTION'
    ,
    (
        9,
        115,
    ): 
        'ERROR_CONVERTING_PRIVATE_KEY'
    ,
    (
        9,
        116,
    ): 
        'BAD_MAGIC_NUMBER'
    ,
    (
        9,
        117,
    ): 
        'BAD_VERSION_NUMBER'
    ,
    (
        9,
        118,
    ): 
        'BIO_WRITE_FAILURE'
    ,
    (
        9,
        119,
    ): 
        'EXPECTING_PRIVATE_KEY_BLOB'
    ,
    (
        9,
        120,
    ): 
        'EXPECTING_PUBLIC_KEY_BLOB'
    ,
    (
        9,
        121,
    ): 
        'INCONSISTENT_HEADER'
    ,
    (
        9,
        122,
    ): 
        'KEYBLOB_HEADER_PARSE_ERROR'
    ,
    (
        9,
        123,
    ): 
        'KEYBLOB_TOO_SHORT'
    ,
    (
        9,
        124,
    ): 
        'PVK_DATA_TOO_SHORT'
    ,
    (
        9,
        125,
    ): 
        'PVK_TOO_SHORT'
    ,
    (
        9,
        126,
    ): 
        'UNSUPPORTED_KEY_COMPONENTS'
    ,
    (
        9,
        127,
    ): 
        'CIPHER_IS_NULL'
    ,
    (
        9,
        128,
    ): 
        'HEADER_TOO_LONG'
    ,
    (
        9,
        129,
    ): 
        'MISSING_DEK_IV'
    ,
    (
        9,
        130,
    ): 
        'UNEXPECTED_DEK_IV'
    ,
    (
        9,
        131,
    ): 
        'EXPECTING_DSS_KEY_BLOB'
    ,
    (
        9,
        132,
    ): 
        'EXPECTING_RSA_KEY_BLOB'
    ,
    (
        10,
        101,
    ): 
        'MISSING_PARAMETERS'
    ,
    (
        10,
        102,
    ): 
        'BAD_Q_VALUE'
    ,
    (
        10,
        103,
    ): 
        'MODULUS_TOO_LARGE'
    ,
    (
        10,
        104,
    ): 
        'DECODE_ERROR'
    ,
    (
        10,
        105,
    ): 
        'PARAMETER_ENCODING_ERROR'
    ,
    (
        10,
        106,
    ): 
        'INVALID_DIGEST_TYPE'
    ,
    (
        10,
        107,
    ): 
        'NO_PARAMETERS_SET'
    ,
    (
        10,
        108,
    ): 
        'BN_DECODE_ERROR'
    ,
    (
        10,
        109,
    ): 
        'BN_ERROR'
    ,
    (
        10,
        110,
    ): 
        'SEED_LEN_SMALL'
    ,
    (
        10,
        111,
    ): 
        'MISSING_PRIVATE_KEY'
    ,
    (
        10,
        112,
    ): 
        'INVALID_PARAMETERS'
    ,
    (
        10,
        113,
    ): 
        'Q_NOT_PRIME'
    ,
    (
        10,
        114,
    ): 
        'BAD_FFC_PARAMETERS'
    ,
    (
        10,
        115,
    ): 
        'P_NOT_PRIME'
    ,
    (
        10,
        116,
    ): 
        'TOO_MANY_RETRIES'
    ,
    (
        11,
        100,
    ): 
        'BAD_X509_FILETYPE'
    ,
    (
        11,
        101,
    ): 
        'CERT_ALREADY_IN_HASH_TABLE'
    ,
    (
        11,
        103,
    ): 
        'LOADING_CERT_DIR'
    ,
    (
        11,
        104,
    ): 
        'LOADING_DEFAULTS'
    ,
    (
        11,
        105,
    ): 
        'NO_CERT_SET_FOR_US_TO_VERIFY'
    ,
    (
        11,
        106,
    ): 
        'SHOULD_RETRY'
    ,
    (
        11,
        107,
    ): 
        'UNABLE_TO_FIND_PARAMETERS_IN_CHAIN'
    ,
    (
        11,
        108,
    ): 
        'UNABLE_TO_GET_CERTS_PUBLIC_KEY'
    ,
    (
        11,
        109,
    ): 
        'UNKNOWN_NID'
    ,
    (
        11,
        110,
    ): 
        'AKID_MISMATCH'
    ,
    (
        11,
        111,
    ): 
        'UNSUPPORTED_ALGORITHM'
    ,
    (
        11,
        112,
    ): 
        'WRONG_LOOKUP_TYPE'
    ,
    (
        11,
        113,
    ): 
        'INVALID_DIRECTORY'
    ,
    (
        11,
        114,
    ): 
        'CANT_CHECK_DH_KEY'
    ,
    (
        11,
        115,
    ): 
        'KEY_TYPE_MISMATCH'
    ,
    (
        11,
        116,
    ): 
        'KEY_VALUES_MISMATCH'
    ,
    (
        11,
        117,
    ): 
        'UNKNOWN_KEY_TYPE'
    ,
    (
        11,
        118,
    ): 
        'BASE64_DECODE_ERROR'
    ,
    (
        11,
        119,
    ): 
        'INVALID_FIELD_NAME'
    ,
    (
        11,
        120,
    ): 
        'UNKNOWN_TRUST_ID'
    ,
    (
        11,
        121,
    ): 
        'UNKNOWN_PURPOSE_ID'
    ,
    (
        11,
        122,
    ): 
        'WRONG_TYPE'
    ,
    (
        11,
        123,
    ): 
        'INVALID_TRUST'
    ,
    (
        11,
        124,
    ): 
        'METHOD_NOT_SUPPORTED'
    ,
    (
        11,
        125,
    ): 
        'PUBLIC_KEY_DECODE_ERROR'
    ,
    (
        11,
        126,
    ): 
        'PUBLIC_KEY_ENCODE_ERROR'
    ,
    (
        11,
        127,
    ): 
        'CRL_ALREADY_DELTA'
    ,
    (
        11,
        128,
    ): 
        'IDP_MISMATCH'
    ,
    (
        11,
        129,
    ): 
        'ISSUER_MISMATCH'
    ,
    (
        11,
        130,
    ): 
        'NO_CRL_NUMBER'
    ,
    (
        11,
        131,
    ): 
        'CRL_VERIFY_FAILURE'
    ,
    (
        11,
        132,
    ): 
        'NEWER_CRL_NOT_NEWER'
    ,
    (
        11,
        133,
    ): 
        'BAD_SELECTOR'
    ,
    (
        11,
        134,
    ): 
        'NAME_TOO_LONG'
    ,
    (
        11,
        135,
    ): 
        'NO_CERTIFICATE_FOUND'
    ,
    (
        11,
        136,
    ): 
        'NO_CERTIFICATE_OR_CRL_FOUND'
    ,
    (
        11,
        137,
    ): 
        'NO_CRL_FOUND'
    ,
    (
        11,
        138,
    ): 
        'INVALID_ATTRIBUTES'
    ,
    (
        11,
        139,
    ): 
        'CERTIFICATE_VERIFICATION_FAILED'
    ,
    (
        11,
        141,
    ): 
        'ERROR_GETTING_MD_BY_NID'
    ,
    (
        11,
        142,
    ): 
        'ERROR_USING_SIGINF_SET'
    ,
    (
        11,
        143,
    ): 
        'INVALID_DISTPOINT'
    ,
    (
        11,
        144,
    ): 
        'UNKNOWN_SIGID_ALGS'
    ,
    (
        13,
        100,
    ): 
        'AUX_ERROR'
    ,
    (
        13,
        102,
    ): 
        'BAD_OBJECT_HEADER'
    ,
    (
        13,
        105,
    ): 
        'BN_LIB'
    ,
    (
        13,
        106,
    ): 
        'BOOLEAN_IS_WRONG_LENGTH'
    ,
    (
        13,
        107,
    ): 
        'BUFFER_TOO_SMALL'
    ,
    (
        13,
        108,
    ): 
        'CIPHER_HAS_NO_OBJECT_IDENTIFIER'
    ,
    (
        13,
        109,
    ): 
        'DATA_IS_WRONG'
    ,
    (
        13,
        110,
    ): 
        'DECODE_ERROR'
    ,
    (
        13,
        112,
    ): 
        'ENCODE_ERROR'
    ,
    (
        13,
        114,
    ): 
        'ERROR_SETTING_CIPHER_PARAMS'
    ,
    (
        13,
        115,
    ): 
        'EXPECTING_AN_INTEGER'
    ,
    (
        13,
        116,
    ): 
        'EXPECTING_AN_OBJECT'
    ,
    (
        13,
        119,
    ): 
        'EXPLICIT_LENGTH_MISMATCH'
    ,
    (
        13,
        120,
    ): 
        'EXPLICIT_TAG_NOT_CONSTRUCTED'
    ,
    (
        13,
        121,
    ): 
        'FIELD_MISSING'
    ,
    (
        13,
        122,
    ): 
        'FIRST_NUM_TOO_LARGE'
    ,
    (
        13,
        123,
    ): 
        'HEADER_TOO_LONG'
    ,
    (
        13,
        124,
    ): 
        'ILLEGAL_CHARACTERS'
    ,
    (
        13,
        125,
    ): 
        'ILLEGAL_NULL'
    ,
    (
        13,
        126,
    ): 
        'ILLEGAL_OPTIONAL_ANY'
    ,
    (
        13,
        127,
    ): 
        'ILLEGAL_TAGGED_ANY'
    ,
    (
        13,
        128,
    ): 
        'INTEGER_TOO_LARGE_FOR_LONG'
    ,
    (
        13,
        129,
    ): 
        'INVALID_BMPSTRING_LENGTH'
    ,
    (
        13,
        130,
    ): 
        'INVALID_DIGIT'
    ,
    (
        13,
        131,
    ): 
        'INVALID_SEPARATOR'
    ,
    (
        13,
        133,
    ): 
        'INVALID_UNIVERSALSTRING_LENGTH'
    ,
    (
        13,
        134,
    ): 
        'INVALID_UTF8STRING'
    ,
    (
        13,
        137,
    ): 
        'MISSING_EOC'
    ,
    (
        13,
        138,
    ): 
        'MISSING_SECOND_NUMBER'
    ,
    (
        13,
        139,
    ): 
        'MSTRING_NOT_UNIVERSAL'
    ,
    (
        13,
        140,
    ): 
        'MSTRING_WRONG_TAG'
    ,
    (
        13,
        141,
    ): 
        'NON_HEX_CHARACTERS'
    ,
    (
        13,
        142,
    ): 
        'NOT_ENOUGH_DATA'
    ,
    (
        13,
        143,
    ): 
        'NO_MATCHING_CHOICE_TYPE'
    ,
    (
        13,
        144,
    ): 
        'NULL_IS_WRONG_LENGTH'
    ,
    (
        13,
        145,
    ): 
        'ODD_NUMBER_OF_CHARS'
    ,
    (
        13,
        147,
    ): 
        'SECOND_NUMBER_TOO_LARGE'
    ,
    (
        13,
        148,
    ): 
        'SEQUENCE_LENGTH_MISMATCH'
    ,
    (
        13,
        149,
    ): 
        'SEQUENCE_NOT_CONSTRUCTED'
    ,
    (
        13,
        150,
    ): 
        'SHORT_LINE'
    ,
    (
        13,
        151,
    ): 
        'STRING_TOO_LONG'
    ,
    (
        13,
        152,
    ): 
        'STRING_TOO_SHORT'
    ,
    (
        13,
        154,
    ): 
        'THE_ASN1_OBJECT_IDENTIFIER_IS_NOT_KNOWN_FOR_THIS_MD'
    ,
    (
        13,
        155,
    ): 
        'TOO_LONG'
    ,
    (
        13,
        156,
    ): 
        'TYPE_NOT_CONSTRUCTED'
    ,
    (
        13,
        159,
    ): 
        'UNEXPECTED_EOC'
    ,
    (
        13,
        160,
    ): 
        'UNKNOWN_FORMAT'
    ,
    (
        13,
        161,
    ): 
        'UNKNOWN_MESSAGE_DIGEST_ALGORITHM'
    ,
    (
        13,
        162,
    ): 
        'UNKNOWN_OBJECT_TYPE'
    ,
    (
        13,
        163,
    ): 
        'UNKNOWN_PUBLIC_KEY_TYPE'
    ,
    (
        13,
        164,
    ): 
        'UNSUPPORTED_ANY_DEFINED_BY_TYPE'
    ,
    (
        13,
        167,
    ): 
        'UNSUPPORTED_PUBLIC_KEY_TYPE'
    ,
    (
        13,
        168,
    ): 
        'WRONG_TAG'
    ,
    (
        13,
        170,
    ): 
        'ILLEGAL_OPTIONS_ON_ITEM_TEMPLATE'
    ,
    (
        13,
        171,
    ): 
        'ADDING_OBJECT'
    ,
    (
        13,
        172,
    ): 
        'ERROR_LOADING_SECTION'
    ,
    (
        13,
        173,
    ): 
        'ERROR_GETTING_TIME'
    ,
    (
        13,
        174,
    ): 
        'DEPTH_EXCEEDED'
    ,
    (
        13,
        175,
    ): 
        'ILLEGAL_BITSTRING_FORMAT'
    ,
    (
        13,
        176,
    ): 
        'ILLEGAL_BOOLEAN'
    ,
    (
        13,
        177,
    ): 
        'ILLEGAL_FORMAT'
    ,
    (
        13,
        178,
    ): 
        'ILLEGAL_HEX'
    ,
    (
        13,
        179,
    ): 
        'ILLEGAL_IMPLICIT_TAG'
    ,
    (
        13,
        180,
    ): 
        'ILLEGAL_INTEGER'
    ,
    (
        13,
        181,
    ): 
        'ILLEGAL_NESTED_TAGGING'
    ,
    (
        13,
        182,
    ): 
        'ILLEGAL_NULL_VALUE'
    ,
    (
        13,
        183,
    ): 
        'ILLEGAL_OBJECT'
    ,
    (
        13,
        184,
    ): 
        'ILLEGAL_TIME_VALUE'
    ,
    (
        13,
        185,
    ): 
        'INTEGER_NOT_ASCII_FORMAT'
    ,
    (
        13,
        186,
    ): 
        'INVALID_MODIFIER'
    ,
    (
        13,
        187,
    ): 
        'INVALID_NUMBER'
    ,
    (
        13,
        188,
    ): 
        'LIST_ERROR'
    ,
    (
        13,
        189,
    ): 
        'MISSING_VALUE'
    ,
    (
        13,
        190,
    ): 
        'NOT_ASCII_FORMAT'
    ,
    (
        13,
        191,
    ): 
        'OBJECT_NOT_ASCII_FORMAT'
    ,
    (
        13,
        192,
    ): 
        'SEQUENCE_OR_SET_NEEDS_CONFIG'
    ,
    (
        13,
        193,
    ): 
        'TIME_NOT_ASCII_FORMAT'
    ,
    (
        13,
        194,
    ): 
        'UNKNOWN_TAG'
    ,
    (
        13,
        195,
    ): 
        'TYPE_NOT_PRIMITIVE'
    ,
    (
        13,
        196,
    ): 
        'UNSUPPORTED_TYPE'
    ,
    (
        13,
        197,
    ): 
        'NESTED_ASN1_STRING'
    ,
    (
        13,
        198,
    ): 
        'DIGEST_AND_KEY_TYPE_NOT_SUPPORTED'
    ,
    (
        13,
        199,
    ): 
        'UNKNOWN_SIGNATURE_ALGORITHM'
    ,
    (
        13,
        200,
    ): 
        'WRONG_PUBLIC_KEY_TYPE'
    ,
    (
        13,
        201,
    ): 
        'NESTED_TOO_DEEP'
    ,
    (
        13,
        202,
    ): 
        'STREAMING_NOT_SUPPORTED'
    ,
    (
        13,
        203,
    ): 
        'ASN1_PARSE_ERROR'
    ,
    (
        13,
        204,
    ): 
        'ASN1_SIG_PARSE_ERROR'
    ,
    (
        13,
        205,
    ): 
        'INVALID_MIME_TYPE'
    ,
    (
        13,
        206,
    ): 
        'MIME_NO_CONTENT_TYPE'
    ,
    (
        13,
        207,
    ): 
        'MIME_PARSE_ERROR'
    ,
    (
        13,
        208,
    ): 
        'MIME_SIG_PARSE_ERROR'
    ,
    (
        13,
        209,
    ): 
        'NO_CONTENT_TYPE'
    ,
    (
        13,
        210,
    ): 
        'NO_MULTIPART_BODY_FAILURE'
    ,
    (
        13,
        211,
    ): 
        'NO_MULTIPART_BOUNDARY'
    ,
    (
        13,
        212,
    ): 
        'NO_SIG_CONTENT_TYPE'
    ,
    (
        13,
        213,
    ): 
        'SIG_INVALID_MIME_TYPE'
    ,
    (
        13,
        214,
    ): 
        'BMPSTRING_IS_WRONG_LENGTH'
    ,
    (
        13,
        215,
    ): 
        'UNIVERSALSTRING_IS_WRONG_LENGTH'
    ,
    (
        13,
        216,
    ): 
        'INVALID_OBJECT_ENCODING'
    ,
    (
        13,
        217,
    ): 
        'CONTEXT_NOT_INITIALISED'
    ,
    (
        13,
        218,
    ): 
        'INVALID_STRING_TABLE_VALUE'
    ,
    (
        13,
        219,
    ): 
        'INVALID_VALUE'
    ,
    (
        13,
        220,
    ): 
        'INVALID_BIT_STRING_BITS_LEFT'
    ,
    (
        13,
        221,
    ): 
        'ILLEGAL_PADDING'
    ,
    (
        13,
        222,
    ): 
        'ILLEGAL_ZERO_CONTENT'
    ,
    (
        13,
        223,
    ): 
        'TOO_LARGE'
    ,
    (
        13,
        224,
    ): 
        'TOO_SMALL'
    ,
    (
        13,
        225,
    ): 
        'WRONG_INTEGER_TYPE'
    ,
    (
        13,
        226,
    ): 
        'ILLEGAL_NEGATIVE_VALUE'
    ,
    (
        13,
        227,
    ): 
        'INVALID_SCRYPT_PARAMETERS'
    ,
    (
        13,
        228,
    ): 
        'UNSUPPORTED_CIPHER'
    ,
    (
        13,
        229,
    ): 
        'UNKNOWN_DIGEST'
    ,
    (
        13,
        230,
    ): 
        'BAD_TEMPLATE'
    ,
    (
        13,
        231,
    ): 
        'LENGTH_TOO_LONG'
    ,
    (
        14,
        100,
    ): 
        'MISSING_CLOSE_SQUARE_BRACKET'
    ,
    (
        14,
        101,
    ): 
        'MISSING_EQUAL_SIGN'
    ,
    (
        14,
        102,
    ): 
        'NO_CLOSE_BRACE'
    ,
    (
        14,
        103,
    ): 
        'UNABLE_TO_CREATE_NEW_SECTION'
    ,
    (
        14,
        104,
    ): 
        'VARIABLE_HAS_NO_VALUE'
    ,
    (
        14,
        105,
    ): 
        'NO_CONF'
    ,
    (
        14,
        106,
    ): 
        'NO_CONF_OR_ENVIRONMENT_VARIABLE'
    ,
    (
        14,
        107,
    ): 
        'NO_SECTION'
    ,
    (
        14,
        108,
    ): 
        'NO_VALUE'
    ,
    (
        14,
        109,
    ): 
        'MODULE_INITIALIZATION_ERROR'
    ,
    (
        14,
        110,
    ): 
        'ERROR_LOADING_DSO'
    ,
    (
        14,
        111,
    ): 
        'RECURSIVE_DIRECTORY_INCLUDE'
    ,
    (
        14,
        112,
    ): 
        'MISSING_INIT_FUNCTION'
    ,
    (
        14,
        113,
    ): 
        'UNKNOWN_MODULE_NAME'
    ,
    (
        14,
        114,
    ): 
        'NO_SUCH_FILE'
    ,
    (
        14,
        115,
    ): 
        'LIST_CANNOT_BE_NULL'
    ,
    (
        14,
        116,
    ): 
        'VARIABLE_EXPANSION_TOO_LONG'
    ,
    (
        14,
        117,
    ): 
        'SSL_COMMAND_SECTION_EMPTY'
    ,
    (
        14,
        118,
    ): 
        'SSL_COMMAND_SECTION_NOT_FOUND'
    ,
    (
        14,
        119,
    ): 
        'SSL_SECTION_EMPTY'
    ,
    (
        14,
        120,
    ): 
        'SSL_SECTION_NOT_FOUND'
    ,
    (
        14,
        121,
    ): 
        'NUMBER_TOO_LARGE'
    ,
    (
        14,
        122,
    ): 
        'INVALID_PRAGMA'
    ,
    (
        14,
        123,
    ): 
        'MANDATORY_BRACES_IN_VARIABLE_EXPANSION'
    ,
    (
        14,
        124,
    ): 
        'OPENSSL_CONF_REFERENCES_MISSING_SECTION'
    ,
    (
        14,
        125,
    ): 
        'RELATIVE_PATH'
    ,
    (
        15,
        101,
    ): 
        'FIPS_MODE_NOT_SUPPORTED'
    ,
    (
        15,
        102,
    ): 
        'ILLEGAL_HEX_DIGIT'
    ,
    (
        15,
        103,
    ): 
        'ODD_NUMBER_OF_DIGITS'
    ,
    (
        15,
        104,
    ): 
        'PROVIDER_ALREADY_EXISTS'
    ,
    (
        15,
        105,
    ): 
        'PROVIDER_SECTION_ERROR'
    ,
    (
        15,
        106,
    ): 
        'INSUFFICIENT_DATA_SPACE'
    ,
    (
        15,
        107,
    ): 
        'INSUFFICIENT_PARAM_SIZE'
    ,
    (
        15,
        108,
    ): 
        'INSUFFICIENT_SECURE_DATA_SPACE'
    ,
    (
        15,
        109,
    ): 
        'INVALID_NULL_ARGUMENT'
    ,
    (
        15,
        110,
    ): 
        'INVALID_OSSL_PARAM_TYPE'
    ,
    (
        15,
        111,
    ): 
        'SECURE_MALLOC_FAILURE'
    ,
    (
        15,
        112,
    ): 
        'STRING_TOO_LONG'
    ,
    (
        15,
        113,
    ): 
        'TOO_MANY_BYTES'
    ,
    (
        15,
        114,
    ): 
        'TOO_MANY_RECORDS'
    ,
    (
        15,
        115,
    ): 
        'ZERO_LENGTH_NUMBER'
    ,
    (
        15,
        116,
    ): 
        'TOO_SMALL_BUFFER'
    ,
    (
        15,
        117,
    ): 
        'BAD_ALGORITHM_NAME'
    ,
    (
        15,
        118,
    ): 
        'CONFLICTING_NAMES'
    ,
    (
        15,
        119,
    ): 
        'RANDOM_SECTION_ERROR'
    ,
    (
        15,
        120,
    ): 
        'UNKNOWN_NAME_IN_RANDOM_SECTION'
    ,
    (
        15,
        121,
    ): 
        'HEX_STRING_TOO_SHORT'
    ,
    (
        15,
        122,
    ): 
        'INVALID_NEGATIVE_VALUE'
    ,
    (
        16,
        100,
    ): 
        'BUFFER_TOO_SMALL'
    ,
    (
        16,
        101,
    ): 
        'INCOMPATIBLE_OBJECTS'
    ,
    (
        16,
        102,
    ): 
        'INVALID_ENCODING'
    ,
    (
        16,
        103,
    ): 
        'INVALID_FIELD'
    ,
    (
        16,
        104,
    ): 
        'INVALID_FORM'
    ,
    (
        16,
        106,
    ): 
        'POINT_AT_INFINITY'
    ,
    (
        16,
        107,
    ): 
        'POINT_IS_NOT_ON_CURVE'
    ,
    (
        16,
        108,
    ): 
        'SLOT_FULL'
    ,
    (
        16,
        109,
    ): 
        'INVALID_COMPRESSION_BIT'
    ,
    (
        16,
        110,
    ): 
        'INVALID_COMPRESSED_POINT'
    ,
    (
        16,
        111,
    ): 
        'NOT_INITIALIZED'
    ,
    (
        16,
        112,
    ): 
        'INVALID_ARGUMENT'
    ,
    (
        16,
        113,
    ): 
        'UNDEFINED_GENERATOR'
    ,
    (
        16,
        114,
    ): 
        'UNKNOWN_ORDER'
    ,
    (
        16,
        115,
    ): 
        'ASN1_ERROR'
    ,
    (
        16,
        116,
    ): 
        'INVALID_KEY'
    ,
    (
        16,
        117,
    ): 
        'INVALID_LENGTH'
    ,
    (
        16,
        118,
    ): 
        'DISCRIMINANT_IS_ZERO'
    ,
    (
        16,
        119,
    ): 
        'EC_GROUP_NEW_BY_NAME_FAILURE'
    ,
    (
        16,
        120,
    ): 
        'GROUP2PKPARAMETERS_FAILURE'
    ,
    (
        16,
        121,
    ): 
        'I2D_ECPKPARAMETERS_FAILURE'
    ,
    (
        16,
        122,
    ): 
        'INVALID_GROUP_ORDER'
    ,
    (
        16,
        123,
    ): 
        'INVALID_PRIVATE_KEY'
    ,
    (
        16,
        124,
    ): 
        'MISSING_PARAMETERS'
    ,
    (
        16,
        125,
    ): 
        'MISSING_PRIVATE_KEY'
    ,
    (
        16,
        126,
    ): 
        'NOT_IMPLEMENTED'
    ,
    (
        16,
        127,
    ): 
        'EXPLICIT_PARAMS_NOT_SUPPORTED'
    ,
    (
        16,
        128,
    ): 
        'UNDEFINED_ORDER'
    ,
    (
        16,
        129,
    ): 
        'UNKNOWN_GROUP'
    ,
    (
        16,
        130,
    ): 
        'WRONG_ORDER'
    ,
    (
        16,
        131,
    ): 
        'UNSUPPORTED_FIELD'
    ,
    (
        16,
        132,
    ): 
        'INVALID_PENTANOMIAL_BASIS'
    ,
    (
        16,
        133,
    ): 
        'INVALID_PEER_KEY'
    ,
    (
        16,
        134,
    ): 
        'PASSED_NULL_PARAMETER'
    ,
    (
        16,
        135,
    ): 
        'NOT_A_NIST_PRIME'
    ,
    (
        16,
        136,
    ): 
        'LADDER_POST_FAILURE'
    ,
    (
        16,
        137,
    ): 
        'INVALID_TRINOMIAL_BASIS'
    ,
    (
        16,
        138,
    ): 
        'INVALID_DIGEST_TYPE'
    ,
    (
        16,
        139,
    ): 
        'NO_PARAMETERS_SET'
    ,
    (
        16,
        140,
    ): 
        'KEYS_NOT_SET'
    ,
    (
        16,
        141,
    ): 
        'INVALID_CURVE'
    ,
    (
        16,
        142,
    ): 
        'DECODE_ERROR'
    ,
    (
        16,
        143,
    ): 
        'FIELD_TOO_LARGE'
    ,
    (
        16,
        144,
    ): 
        'BIGNUM_OUT_OF_RANGE'
    ,
    (
        16,
        145,
    ): 
        'WRONG_CURVE_PARAMETERS'
    ,
    (
        16,
        146,
    ): 
        'COORDINATES_OUT_OF_RANGE'
    ,
    (
        16,
        147,
    ): 
        'GF2M_NOT_SUPPORTED'
    ,
    (
        16,
        148,
    ): 
        'KDF_PARAMETER_ERROR'
    ,
    (
        16,
        149,
    ): 
        'PEER_KEY_ERROR'
    ,
    (
        16,
        150,
    ): 
        'SHARED_INFO_ERROR'
    ,
    (
        16,
        151,
    ): 
        'INVALID_DIGEST'
    ,
    (
        16,
        152,
    ): 
        'OPERATION_NOT_SUPPORTED'
    ,
    (
        16,
        153,
    ): 
        'LADDER_PRE_FAILURE'
    ,
    (
        16,
        154,
    ): 
        'NO_PRIVATE_VALUE'
    ,
    (
        16,
        155,
    ): 
        'POINT_ARITHMETIC_FAILURE'
    ,
    (
        16,
        156,
    ): 
        'BAD_SIGNATURE'
    ,
    (
        16,
        157,
    ): 
        'NEED_NEW_SETUP_VALUES'
    ,
    (
        16,
        158,
    ): 
        'RANDOM_NUMBER_GENERATION_FAILED'
    ,
    (
        16,
        159,
    ): 
        'CURVE_DOES_NOT_SUPPORT_SIGNING'
    ,
    (
        16,
        160,
    ): 
        'CURVE_DOES_NOT_SUPPORT_ECDH'
    ,
    (
        16,
        161,
    ): 
        'INVALID_OUTPUT_LENGTH'
    ,
    (
        16,
        162,
    ): 
        'LADDER_STEP_FAILURE'
    ,
    (
        16,
        163,
    ): 
        'POINT_COORDINATES_BLIND_FAILURE'
    ,
    (
        16,
        164,
    ): 
        'UNKNOWN_COFACTOR'
    ,
    (
        16,
        165,
    ): 
        'CANNOT_INVERT'
    ,
    (
        16,
        166,
    ): 
        'FAILED_MAKING_PUBLIC_KEY'
    ,
    (
        16,
        167,
    ): 
        'MISSING_OID'
    ,
    (
        16,
        168,
    ): 
        'INVALID_A'
    ,
    (
        16,
        169,
    ): 
        'INVALID_B'
    ,
    (
        16,
        170,
    ): 
        'CURVE_DOES_NOT_SUPPORT_ECDSA'
    ,
    (
        16,
        171,
    ): 
        'INVALID_COFACTOR'
    ,
    (
        16,
        172,
    ): 
        'INVALID_P'
    ,
    (
        16,
        173,
    ): 
        'INVALID_GENERATOR'
    ,
    (
        16,
        174,
    ): 
        'INVALID_NAMED_GROUP_CONVERSION'
    ,
    (
        16,
        175,
    ): 
        'INVALID_SEED'
    ,
    (
        16,
        176,
    ): 
        'TOO_MANY_RETRIES'
    ,
    (
        20,
        100,
    ): 
        'APP_DATA_IN_HANDSHAKE'
    ,
    (
        20,
        101,
    ): 
        'NO_SUITABLE_KEY_SHARE'
    ,
    (
        20,
        102,
    ): 
        'BAD_DH_VALUE'
    ,
    (
        20,
        103,
    ): 
        'BAD_CHANGE_CIPHER_SPEC'
    ,
    (
        20,
        104,
    ): 
        'INCONSISTENT_EXTMS'
    ,
    (
        20,
        105,
    ): 
        'BAD_HELLO_REQUEST'
    ,
    (
        20,
        106,
    ): 
        'BAD_DATA_RETURNED_BY_CALLBACK'
    ,
    (
        20,
        107,
    ): 
        'BAD_DECOMPRESSION'
    ,
    (
        20,
        108,
    ): 
        'BAD_KEY_SHARE'
    ,
    (
        20,
        109,
    ): 
        'CANNOT_CHANGE_CIPHER'
    ,
    (
        20,
        110,
    ): 
        'BAD_EXTENSION'
    ,
    (
        20,
        111,
    ): 
        'BAD_DIGEST_LENGTH'
    ,
    (
        20,
        112,
    ): 
        'MISSING_SIGALGS_EXTENSION'
    ,
    (
        20,
        113,
    ): 
        'INVALID_CONFIGURATION_NAME'
    ,
    (
        20,
        114,
    ): 
        'BAD_PSK_IDENTITY'
    ,
    (
        20,
        115,
    ): 
        'BAD_PACKET_LENGTH'
    ,
    (
        20,
        116,
    ): 
        'BAD_PROTOCOL_VERSION_NUMBER'
    ,
    (
        20,
        117,
    ): 
        'SSL_COMMAND_SECTION_EMPTY'
    ,
    (
        20,
        118,
    ): 
        'NO_SUITABLE_SIGNATURE_ALGORITHM'
    ,
    (
        20,
        119,
    ): 
        'BAD_RSA_ENCRYPT'
    ,
    (
        20,
        120,
    ): 
        'INVALID_KEY_UPDATE_TYPE'
    ,
    (
        20,
        121,
    ): 
        'STILL_IN_INIT'
    ,
    (
        20,
        122,
    ): 
        'BAD_KEY_UPDATE'
    ,
    (
        20,
        123,
    ): 
        'BAD_SIGNATURE'
    ,
    (
        20,
        124,
    ): 
        'BAD_SSL_FILETYPE'
    ,
    (
        20,
        125,
    ): 
        'SSL_COMMAND_SECTION_NOT_FOUND'
    ,
    (
        20,
        126,
    ): 
        'SSL_SECTION_EMPTY'
    ,
    (
        20,
        127,
    ): 
        'BAD_WRITE_RETRY'
    ,
    (
        20,
        128,
    ): 
        'BIO_NOT_SET'
    ,
    (
        20,
        129,
    ): 
        'BLOCK_CIPHER_PAD_IS_WRONG'
    ,
    (
        20,
        130,
    ): 
        'BN_LIB'
    ,
    (
        20,
        131,
    ): 
        'CA_DN_LENGTH_MISMATCH'
    ,
    (
        20,
        132,
    ): 
        'TOO_MANY_KEY_UPDATES'
    ,
    (
        20,
        133,
    ): 
        'CCS_RECEIVED_EARLY'
    ,
    (
        20,
        134,
    ): 
        'CERTIFICATE_VERIFY_FAILED'
    ,
    (
        20,
        135,
    ): 
        'CERT_LENGTH_MISMATCH'
    ,
    (
        20,
        136,
    ): 
        'SSL_SECTION_NOT_FOUND'
    ,
    (
        20,
        137,
    ): 
        'CIPHER_CODE_WRONG_LENGTH'
    ,
    (
        20,
        139,
    ): 
        'UNKNOWN_COMMAND'
    ,
    (
        20,
        140,
    ): 
        'COMPRESSED_LENGTH_TOO_LONG'
    ,
    (
        20,
        141,
    ): 
        'COMPRESSION_FAILURE'
    ,
    (
        20,
        142,
    ): 
        'COMPRESSION_LIBRARY_ERROR'
    ,
    (
        20,
        143,
    ): 
        'AT_LEAST_TLS_1_0_NEEDED_IN_FIPS_MODE'
    ,
    (
        20,
        144,
    ): 
        'CONNECTION_TYPE_NOT_SET'
    ,
    (
        20,
        145,
    ): 
        'DATA_BETWEEN_CCS_AND_FINISHED'
    ,
    (
        20,
        146,
    ): 
        'DATA_LENGTH_TOO_LONG'
    ,
    (
        20,
        147,
    ): 
        'DECRYPTION_FAILED'
    ,
    (
        20,
        148,
    ): 
        'DH_PUBLIC_VALUE_LENGTH_IS_WRONG'
    ,
    (
        20,
        149,
    ): 
        'DIGEST_CHECK_FAILED'
    ,
    (
        20,
        150,
    ): 
        'ENCRYPTED_LENGTH_TOO_LONG'
    ,
    (
        20,
        151,
    ): 
        'ERROR_IN_RECEIVED_CIPHER_LIST'
    ,
    (
        20,
        152,
    ): 
        'EXCESSIVE_MESSAGE_SIZE'
    ,
    (
        20,
        153,
    ): 
        'EXTRA_DATA_IN_MESSAGE'
    ,
    (
        20,
        154,
    ): 
        'GOT_A_FIN_BEFORE_A_CCS'
    ,
    (
        20,
        155,
    ): 
        'HTTPS_PROXY_REQUEST'
    ,
    (
        20,
        156,
    ): 
        'HTTP_REQUEST'
    ,
    (
        20,
        157,
    ): 
        'TLS_INVALID_ECPOINTFORMAT_LIST'
    ,
    (
        20,
        158,
    ): 
        'AT_LEAST_TLS_1_2_NEEDED_IN_SUITEB_MODE'
    ,
    (
        20,
        159,
    ): 
        'LENGTH_MISMATCH'
    ,
    (
        20,
        160,
    ): 
        'LENGTH_TOO_SHORT'
    ,
    (
        20,
        161,
    ): 
        'LIBRARY_HAS_NO_CIPHERS'
    ,
    (
        20,
        162,
    ): 
        'ILLEGAL_POINT_COMPRESSION'
    ,
    (
        20,
        163,
    ): 
        'EXT_LENGTH_MISMATCH'
    ,
    (
        20,
        164,
    ): 
        'TOO_MUCH_EARLY_DATA'
    ,
    (
        20,
        165,
    ): 
        'MISSING_DSA_SIGNING_CERT'
    ,
    (
        20,
        166,
    ): 
        'VERSION_TOO_HIGH'
    ,
    (
        20,
        167,
    ): 
        'CONTEXT_NOT_DANE_ENABLED'
    ,
    (
        20,
        168,
    ): 
        'MISSING_RSA_CERTIFICATE'
    ,
    (
        20,
        169,
    ): 
        'MISSING_RSA_ENCRYPTING_CERT'
    ,
    (
        20,
        170,
    ): 
        'MISSING_RSA_SIGNING_CERT'
    ,
    (
        20,
        171,
    ): 
        'MISSING_TMP_DH_KEY'
    ,
    (
        20,
        172,
    ): 
        'DANE_ALREADY_ENABLED'
    ,
    (
        20,
        173,
    ): 
        'DANE_CANNOT_OVERRIDE_MTYPE_FULL'
    ,
    (
        20,
        174,
    ): 
        'INVALID_MAX_EARLY_DATA'
    ,
    (
        20,
        175,
    ): 
        'DANE_NOT_ENABLED'
    ,
    (
        20,
        176,
    ): 
        'NO_CERTIFICATES_RETURNED'
    ,
    (
        20,
        177,
    ): 
        'NO_CERTIFICATE_ASSIGNED'
    ,
    (
        20,
        178,
    ): 
        'UNEXPECTED_END_OF_EARLY_DATA'
    ,
    (
        20,
        179,
    ): 
        'NO_CERTIFICATE_SET'
    ,
    (
        20,
        180,
    ): 
        'DANE_TLSA_BAD_CERTIFICATE'
    ,
    (
        20,
        181,
    ): 
        'NO_CIPHERS_AVAILABLE'
    ,
    (
        20,
        182,
    ): 
        'NOT_ON_RECORD_BOUNDARY'
    ,
    (
        20,
        183,
    ): 
        'NO_CIPHERS_SPECIFIED'
    ,
    (
        20,
        184,
    ): 
        'DANE_TLSA_BAD_CERTIFICATE_USAGE'
    ,
    (
        20,
        185,
    ): 
        'NO_CIPHER_MATCH'
    ,
    (
        20,
        186,
    ): 
        'BAD_CIPHER'
    ,
    (
        20,
        187,
    ): 
        'NO_COMPRESSION_SPECIFIED'
    ,
    (
        20,
        188,
    ): 
        'NO_METHOD_SPECIFIED'
    ,
    (
        20,
        189,
    ): 
        'DANE_TLSA_BAD_DATA_LENGTH'
    ,
    (
        20,
        190,
    ): 
        'NO_PRIVATE_KEY_ASSIGNED'
    ,
    (
        20,
        191,
    ): 
        'NO_PROTOCOLS_AVAILABLE'
    ,
    (
        20,
        192,
    ): 
        'DANE_TLSA_BAD_DIGEST_LENGTH'
    ,
    (
        20,
        193,
    ): 
        'NO_SHARED_CIPHER'
    ,
    (
        20,
        194,
    ): 
        'EXCEEDS_MAX_FRAGMENT_SIZE'
    ,
    (
        20,
        195,
    ): 
        'NULL_SSL_CTX'
    ,
    (
        20,
        196,
    ): 
        'NULL_SSL_METHOD_PASSED'
    ,
    (
        20,
        197,
    ): 
        'OLD_SESSION_CIPHER_NOT_RETURNED'
    ,
    (
        20,
        198,
    ): 
        'PACKET_LENGTH_TOO_LONG'
    ,
    (
        20,
        199,
    ): 
        'PEER_DID_NOT_RETURN_A_CERTIFICATE'
    ,
    (
        20,
        200,
    ): 
        'DANE_TLSA_BAD_MATCHING_TYPE'
    ,
    (
        20,
        201,
    ): 
        'DANE_TLSA_BAD_PUBLIC_KEY'
    ,
    (
        20,
        202,
    ): 
        'DANE_TLSA_BAD_SELECTOR'
    ,
    (
        20,
        203,
    ): 
        'DANE_TLSA_NULL_DATA'
    ,
    (
        20,
        204,
    ): 
        'ERROR_SETTING_TLSA_BASE_DOMAIN'
    ,
    (
        20,
        205,
    ): 
        'INVALID_ALERT'
    ,
    (
        20,
        206,
    ): 
        'CUSTOM_EXT_HANDLER_ALREADY_INSTALLED'
    ,
    (
        20,
        207,
    ): 
        'PROTOCOL_IS_SHUTDOWN'
    ,
    (
        20,
        208,
    ): 
        'SCT_VERIFICATION_FAILED'
    ,
    (
        20,
        209,
    ): 
        'MISSING_SUPPORTED_GROUPS_EXTENSION'
    ,
    (
        20,
        210,
    ): 
        'SSL_SESSION_VERSION_MISMATCH'
    ,
    (
        20,
        211,
    ): 
        'READ_BIO_NOT_SET'
    ,
    (
        20,
        212,
    ): 
        'INVALID_CT_VALIDATION_TYPE'
    ,
    (
        20,
        213,
    ): 
        'RECORD_LENGTH_MISMATCH'
    ,
    (
        20,
        214,
    ): 
        'NO_CHANGE_FOLLOWING_HRR'
    ,
    (
        20,
        215,
    ): 
        'REQUIRED_CIPHER_MISSING'
    ,
    (
        20,
        216,
    ): 
        'NO_VALID_SCTS'
    ,
    (
        20,
        217,
    ): 
        'UNSOLICITED_EXTENSION'
    ,
    (
        20,
        218,
    ): 
        'CIPHERSUITE_DIGEST_HAS_CHANGED'
    ,
    (
        20,
        219,
    ): 
        'BAD_PSK'
    ,
    (
        20,
        220,
    ): 
        'SIGNATURE_FOR_NON_SIGNING_CERTIFICATE'
    ,
    (
        20,
        221,
    ): 
        'MISSING_SIGNING_CERT'
    ,
    (
        20,
        222,
    ): 
        'INCONSISTENT_EARLY_DATA_ALPN'
    ,
    (
        20,
        223,
    ): 
        'PSK_IDENTITY_NOT_FOUND'
    ,
    (
        20,
        224,
    ): 
        'PSK_NO_CLIENT_CB'
    ,
    (
        20,
        225,
    ): 
        'PSK_NO_SERVER_CB'
    ,
    (
        20,
        226,
    ): 
        'CLIENTHELLO_TLSEXT'
    ,
    (
        20,
        227,
    ): 
        'PARSE_TLSEXT'
    ,
    (
        20,
        228,
    ): 
        'SSL_CTX_HAS_NO_DEFAULT_SSL_VERSION'
    ,
    (
        20,
        229,
    ): 
        'SSL_HANDSHAKE_FAILURE'
    ,
    (
        20,
        230,
    ): 
        'SSL_LIBRARY_HAS_NO_CIPHERS'
    ,
    (
        20,
        231,
    ): 
        'INCONSISTENT_EARLY_DATA_SNI'
    ,
    (
        20,
        232,
    ): 
        'SSL3_EXT_INVALID_MAX_FRAGMENT_LENGTH'
    ,
    (
        20,
        233,
    ): 
        'BAD_EARLY_DATA'
    ,
    (
        20,
        234,
    ): 
        'CALLBACK_FAILED'
    ,
    (
        20,
        235,
    ): 
        'NO_APPLICATION_PROTOCOL'
    ,
    (
        20,
        236,
    ): 
        'BAD_HANDSHAKE_STATE'
    ,
    (
        20,
        237,
    ): 
        'OVERFLOW_ERROR'
    ,
    (
        20,
        238,
    ): 
        'INVALID_CERTIFICATE_OR_ALG'
    ,
    (
        20,
        239,
    ): 
        'UNABLE_TO_FIND_PUBLIC_KEY_PARAMETERS'
    ,
    (
        20,
        240,
    ): 
        'BAD_PACKET'
    ,
    (
        20,
        241,
    ): 
        'INSUFFICIENT_SECURITY'
    ,
    (
        20,
        242,
    ): 
        'UNABLE_TO_LOAD_SSL3_MD5_ROUTINES'
    ,
    (
        20,
        243,
    ): 
        'UNABLE_TO_LOAD_SSL3_SHA1_ROUTINES'
    ,
    (
        20,
        244,
    ): 
        'UNEXPECTED_MESSAGE'
    ,
    (
        20,
        245,
    ): 
        'UNEXPECTED_RECORD'
    ,
    (
        20,
        246,
    ): 
        'UNKNOWN_ALERT_TYPE'
    ,
    (
        20,
        247,
    ): 
        'UNKNOWN_CERTIFICATE_TYPE'
    ,
    (
        20,
        248,
    ): 
        'UNKNOWN_CIPHER_RETURNED'
    ,
    (
        20,
        249,
    ): 
        'UNKNOWN_CIPHER_TYPE'
    ,
    (
        20,
        250,
    ): 
        'UNKNOWN_KEY_EXCHANGE_TYPE'
    ,
    (
        20,
        251,
    ): 
        'UNKNOWN_PKEY_TYPE'
    ,
    (
        20,
        252,
    ): 
        'UNKNOWN_PROTOCOL'
    ,
    (
        20,
        253,
    ): 
        'BINDER_DOES_NOT_VERIFY'
    ,
    (
        20,
        254,
    ): 
        'UNKNOWN_SSL_VERSION'
    ,
    (
        20,
        255,
    ): 
        'UNKNOWN_STATE'
    ,
    (
        20,
        256,
    ): 
        'MISSING_FATAL'
    ,
    (
        20,
        257,
    ): 
        'UNSUPPORTED_COMPRESSION_ALGORITHM'
    ,
    (
        20,
        258,
    ): 
        'UNSUPPORTED_PROTOCOL'
    ,
    (
        20,
        259,
    ): 
        'UNSUPPORTED_SSL_VERSION'
    ,
    (
        20,
        260,
    ): 
        'INVALID_CCS_MESSAGE'
    ,
    (
        20,
        261,
    ): 
        'WRONG_CIPHER_RETURNED'
    ,
    (
        20,
        262,
    ): 
        'UNEXPECTED_CCS_MESSAGE'
    ,
    (
        20,
        263,
    ): 
        'BAD_HRR_VERSION'
    ,
    (
        20,
        264,
    ): 
        'WRONG_SIGNATURE_LENGTH'
    ,
    (
        20,
        265,
    ): 
        'WRONG_SIGNATURE_SIZE'
    ,
    (
        20,
        266,
    ): 
        'WRONG_SSL_VERSION'
    ,
    (
        20,
        267,
    ): 
        'WRONG_VERSION_NUMBER'
    ,
    (
        20,
        268,
    ): 
        'X509_LIB'
    ,
    (
        20,
        269,
    ): 
        'X509_VERIFICATION_SETUP_PROBLEMS'
    ,
    (
        20,
        270,
    ): 
        'PATH_TOO_LONG'
    ,
    (
        20,
        271,
    ): 
        'BAD_LENGTH'
    ,
    (
        20,
        272,
    ): 
        'ATTEMPT_TO_REUSE_SESSION_IN_DIFFERENT_CONTEXT'
    ,
    (
        20,
        273,
    ): 
        'SSL_SESSION_ID_CONTEXT_TOO_LONG'
    ,
    (
        20,
        274,
    ): 
        'LIBRARY_BUG'
    ,
    (
        20,
        275,
    ): 
        'SERVERHELLO_TLSEXT'
    ,
    (
        20,
        276,
    ): 
        'UNINITIALIZED'
    ,
    (
        20,
        277,
    ): 
        'SESSION_ID_CONTEXT_UNINITIALIZED'
    ,
    (
        20,
        278,
    ): 
        'POST_HANDSHAKE_AUTH_ENCODING_ERR'
    ,
    (
        20,
        279,
    ): 
        'EXTENSION_NOT_RECEIVED'
    ,
    (
        20,
        280,
    ): 
        'INVALID_COMMAND'
    ,
    (
        20,
        281,
    ): 
        'DECRYPTION_FAILED_OR_BAD_RECORD_MAC'
    ,
    (
        20,
        282,
    ): 
        'INVALID_CONTEXT'
    ,
    (
        20,
        283,
    ): 
        'INVALID_CONFIG'
    ,
    (
        20,
        284,
    ): 
        'NOT_SERVER'
    ,
    (
        20,
        285,
    ): 
        'REQUEST_PENDING'
    ,
    (
        20,
        286,
    ): 
        'REQUEST_SENT'
    ,
    (
        20,
        287,
    ): 
        'NO_COOKIE_CALLBACK_SET'
    ,
    (
        20,
        288,
    ): 
        'PRIVATE_KEY_MISMATCH'
    ,
    (
        20,
        289,
    ): 
        'NOT_REPLACING_CERTIFICATE'
    ,
    (
        20,
        290,
    ): 
        'MISSING_PARAMETERS'
    ,
    (
        20,
        291,
    ): 
        'APPLICATION_DATA_AFTER_CLOSE_NOTIFY'
    ,
    (
        20,
        292,
    ): 
        'BAD_LEGACY_VERSION'
    ,
    (
        20,
        293,
    ): 
        'MIXED_HANDSHAKE_AND_NON_HANDSHAKE_DATA'
    ,
    (
        20,
        294,
    ): 
        'UNEXPECTED_EOF_WHILE_READING'
    ,
    (
        20,
        295,
    ): 
        'NO_SUITABLE_GROUPS'
    ,
    (
        20,
        296,
    ): 
        'COPY_PARAMETERS_FAILED'
    ,
    (
        20,
        297,
    ): 
        'NO_SUITABLE_DIGEST_ALGORITHM'
    ,
    (
        20,
        298,
    ): 
        'RECORD_TOO_SMALL'
    ,
    (
        20,
        299,
    ): 
        'CANNOT_GET_GROUP_NAME'
    ,
    (
        20,
        300,
    ): 
        'SSL3_SESSION_ID_TOO_LONG'
    ,
    (
        20,
        301,
    ): 
        'SSL_SESSION_ID_CALLBACK_FAILED'
    ,
    (
        20,
        302,
    ): 
        'SSL_SESSION_ID_CONFLICT'
    ,
    (
        20,
        303,
    ): 
        'SSL_SESSION_ID_HAS_BAD_LENGTH'
    ,
    (
        20,
        304,
    ): 
        'BAD_ECC_CERT'
    ,
    (
        20,
        305,
    ): 
        'OCSP_CALLBACK_FAILURE'
    ,
    (
        20,
        306,
    ): 
        'BAD_ECPOINT'
    ,
    (
        20,
        307,
    ): 
        'COMPRESSION_ID_NOT_WITHIN_PRIVATE_RANGE'
    ,
    (
        20,
        308,
    ): 
        'COOKIE_MISMATCH'
    ,
    (
        20,
        309,
    ): 
        'DUPLICATE_COMPRESSION_ID'
    ,
    (
        20,
        310,
    ): 
        'MISSING_PSK_KEX_MODES_EXTENSION'
    ,
    (
        20,
        311,
    ): 
        'MISSING_TMP_ECDH_KEY'
    ,
    (
        20,
        312,
    ): 
        'READ_TIMEOUT_EXPIRED'
    ,
    (
        20,
        314,
    ): 
        'UNABLE_TO_FIND_ECDH_PARAMETERS'
    ,
    (
        20,
        315,
    ): 
        'UNSUPPORTED_ELLIPTIC_CURVE'
    ,
    (
        20,
        318,
    ): 
        'ECC_CERT_NOT_FOR_SIGNING'
    ,
    (
        20,
        319,
    ): 
        'SSL3_EXT_INVALID_SERVERNAME'
    ,
    (
        20,
        320,
    ): 
        'SSL3_EXT_INVALID_SERVERNAME_TYPE'
    ,
    (
        20,
        324,
    ): 
        'NO_REQUIRED_DIGEST'
    ,
    (
        20,
        325,
    ): 
        'INVALID_TICKET_KEYS_LENGTH'
    ,
    (
        20,
        328,
    ): 
        'INVALID_STATUS_RESPONSE'
    ,
    (
        20,
        329,
    ): 
        'UNSUPPORTED_STATUS_TYPE'
    ,
    (
        20,
        330,
    ): 
        'NO_GOST_CERTIFICATE_SENT_BY_PEER'
    ,
    (
        20,
        331,
    ): 
        'NO_CLIENT_CERT_METHOD'
    ,
    (
        20,
        332,
    ): 
        'BAD_HANDSHAKE_LENGTH'
    ,
    (
        20,
        333,
    ): 
        'LEGACY_SIGALG_DISALLOWED_OR_UNSUPPORTED'
    ,
    (
        20,
        334,
    ): 
        'DTLS_MESSAGE_TOO_BIG'
    ,
    (
        20,
        335,
    ): 
        'RENEGOTIATE_EXT_TOO_LONG'
    ,
    (
        20,
        336,
    ): 
        'RENEGOTIATION_ENCODING_ERR'
    ,
    (
        20,
        337,
    ): 
        'RENEGOTIATION_MISMATCH'
    ,
    (
        20,
        338,
    ): 
        'UNSAFE_LEGACY_RENEGOTIATION_DISABLED'
    ,
    (
        20,
        339,
    ): 
        'NO_RENEGOTIATION'
    ,
    (
        20,
        340,
    ): 
        'INCONSISTENT_COMPRESSION'
    ,
    (
        20,
        341,
    ): 
        'INVALID_COMPRESSION_ALGORITHM'
    ,
    (
        20,
        342,
    ): 
        'REQUIRED_COMPRESSION_ALGORITHM_MISSING'
    ,
    (
        20,
        343,
    ): 
        'COMPRESSION_DISABLED'
    ,
    (
        20,
        344,
    ): 
        'OLD_SESSION_COMPRESSION_ALGORITHM_NOT_RETURNED'
    ,
    (
        20,
        345,
    ): 
        'SCSV_RECEIVED_WHEN_RENEGOTIATING'
    ,
    (
        20,
        347,
    ): 
        'BAD_SRP_A_LENGTH'
    ,
    (
        20,
        352,
    ): 
        'BAD_SRTP_MKI_VALUE'
    ,
    (
        20,
        353,
    ): 
        'BAD_SRTP_PROTECTION_PROFILE_LIST'
    ,
    (
        20,
        354,
    ): 
        'EMPTY_SRTP_PROTECTION_PROFILE_LIST'
    ,
    (
        20,
        357,
    ): 
        'INVALID_SRP_USERNAME'
    ,
    (
        20,
        358,
    ): 
        'MISSING_SRP_PARAM'
    ,
    (
        20,
        359,
    ): 
        'NO_SRTP_PROFILES'
    ,
    (
        20,
        360,
    ): 
        'SIGNATURE_ALGORITHMS_ERROR'
    ,
    (
        20,
        361,
    ): 
        'SRP_A_CALC'
    ,
    (
        20,
        362,
    ): 
        'SRTP_COULD_NOT_ALLOCATE_PROFILES'
    ,
    (
        20,
        363,
    ): 
        'SRTP_PROTECTION_PROFILE_LIST_TOO_LONG'
    ,
    (
        20,
        364,
    ): 
        'SRTP_UNKNOWN_PROTECTION_PROFILE'
    ,
    (
        20,
        367,
    ): 
        'TLS_ILLEGAL_EXPORTER_LABEL'
    ,
    (
        20,
        368,
    ): 
        'UNKNOWN_DIGEST'
    ,
    (
        20,
        369,
    ): 
        'USE_SRTP_NOT_NEGOTIATED'
    ,
    (
        20,
        370,
    ): 
        'WRONG_SIGNATURE_TYPE'
    ,
    (
        20,
        371,
    ): 
        'BAD_SRP_PARAMETERS'
    ,
    (
        20,
        372,
    ): 
        'SSL_NEGATIVE_LENGTH'
    ,
    (
        20,
        373,
    ): 
        'INAPPROPRIATE_FALLBACK'
    ,
    (
        20,
        374,
    ): 
        'ECDH_REQUIRED_FOR_SUITEB_MODE'
    ,
    (
        20,
        376,
    ): 
        'NO_SHARED_SIGNATURE_ALGORITHMS'
    ,
    (
        20,
        377,
    ): 
        'CERT_CB_ERROR'
    ,
    (
        20,
        378,
    ): 
        'WRONG_CURVE'
    ,
    (
        20,
        380,
    ): 
        'ILLEGAL_SUITEB_DIGEST'
    ,
    (
        20,
        381,
    ): 
        'MISSING_ECDSA_SIGNING_CERT'
    ,
    (
        20,
        383,
    ): 
        'WRONG_CERTIFICATE_TYPE'
    ,
    (
        20,
        384,
    ): 
        'BAD_VALUE'
    ,
    (
        20,
        385,
    ): 
        'INVALID_NULL_CMD_NAME'
    ,
    (
        20,
        386,
    ): 
        'UNKNOWN_CMD_NAME'
    ,
    (
        20,
        388,
    ): 
        'INVALID_SERVERINFO_DATA'
    ,
    (
        20,
        389,
    ): 
        'NO_PEM_EXTENSIONS'
    ,
    (
        20,
        390,
    ): 
        'BAD_DATA'
    ,
    (
        20,
        391,
    ): 
        'PEM_NAME_BAD_PREFIX'
    ,
    (
        20,
        392,
    ): 
        'PEM_NAME_TOO_SHORT'
    ,
    (
        20,
        394,
    ): 
        'DH_KEY_TOO_SMALL'
    ,
    (
        20,
        396,
    ): 
        'VERSION_TOO_LOW'
    ,
    (
        20,
        397,
    ): 
        'CA_KEY_TOO_SMALL'
    ,
    (
        20,
        398,
    ): 
        'CA_MD_TOO_WEAK'
    ,
    (
        20,
        399,
    ): 
        'EE_KEY_TOO_SMALL'
    ,
    (
        20,
        400,
    ): 
        'COOKIE_GEN_CALLBACK_FAILURE'
    ,
    (
        20,
        401,
    ): 
        'FRAGMENTED_CLIENT_HELLO'
    ,
    (
        20,
        402,
    ): 
        'INVALID_SEQUENCE_NUMBER'
    ,
    (
        20,
        403,
    ): 
        'NO_VERIFY_COOKIE_CALLBACK'
    ,
    (
        20,
        404,
    ): 
        'LENGTH_TOO_LONG'
    ,
    (
        20,
        405,
    ): 
        'FAILED_TO_INIT_ASYNC'
    ,
    (
        20,
        406,
    ): 
        'PIPELINE_FAILURE'
    ,
    (
        20,
        407,
    ): 
        'SHUTDOWN_WHILE_IN_INIT'
    ,
    (
        20,
        408,
    ): 
        'SSL_SESSION_ID_TOO_LONG'
    ,
    (
        20,
        409,
    ): 
        'TOO_MANY_WARN_ALERTS'
    ,
    (
        20,
        410,
    ): 
        'NO_SHARED_GROUPS'
    ,
    (
        20,
        443,
    ): 
        'BAD_RECORD_TYPE'
    ,
    (
        20,
        999,
    ): 
        'INVALID_SESSION_ID'
    ,
    (
        20,
        1010,
    ): 
        'SSLV3_ALERT_UNEXPECTED_MESSAGE'
    ,
    (
        20,
        1020,
    ): 
        'SSLV3_ALERT_BAD_RECORD_MAC'
    ,
    (
        20,
        1021,
    ): 
        'TLSV1_ALERT_DECRYPTION_FAILED'
    ,
    (
        20,
        1022,
    ): 
        'TLSV1_ALERT_RECORD_OVERFLOW'
    ,
    (
        20,
        1030,
    ): 
        'SSLV3_ALERT_DECOMPRESSION_FAILURE'
    ,
    (
        20,
        1040,
    ): 
        'SSLV3_ALERT_HANDSHAKE_FAILURE'
    ,
    (
        20,
        1041,
    ): 
        'SSLV3_ALERT_NO_CERTIFICATE'
    ,
    (
        20,
        1042,
    ): 
        'SSLV3_ALERT_BAD_CERTIFICATE'
    ,
    (
        20,
        1043,
    ): 
        'SSLV3_ALERT_UNSUPPORTED_CERTIFICATE'
    ,
    (
        20,
        1044,
    ): 
        'SSLV3_ALERT_CERTIFICATE_REVOKED'
    ,
    (
        20,
        1045,
    ): 
        'SSLV3_ALERT_CERTIFICATE_EXPIRED'
    ,
    (
        20,
        1046,
    ): 
        'SSLV3_ALERT_CERTIFICATE_UNKNOWN'
    ,
    (
        20,
        1047,
    ): 
        'SSLV3_ALERT_ILLEGAL_PARAMETER'
    ,
    (
        20,
        1048,
    ): 
        'TLSV1_ALERT_UNKNOWN_CA'
    ,
    (
        20,
        1049,
    ): 
        'TLSV1_ALERT_ACCESS_DENIED'
    ,
    (
        20,
        1050,
    ): 
        'TLSV1_ALERT_DECODE_ERROR'
    ,
    (
        20,
        1051,
    ): 
        'TLSV1_ALERT_DECRYPT_ERROR'
    ,
    (
        20,
        1060,
    ): 
        'TLSV1_ALERT_EXPORT_RESTRICTION'
    ,
    (
        20,
        1070,
    ): 
        'TLSV1_ALERT_PROTOCOL_VERSION'
    ,
    (
        20,
        1071,
    ): 
        'TLSV1_ALERT_INSUFFICIENT_SECURITY'
    ,
    (
        20,
        1080,
    ): 
        'TLSV1_ALERT_INTERNAL_ERROR'
    ,
    (
        20,
        1086,
    ): 
        'TLSV1_ALERT_INAPPROPRIATE_FALLBACK'
    ,
    (
        20,
        1090,
    ): 
        'TLSV1_ALERT_USER_CANCELLED'
    ,
    (
        20,
        1100,
    ): 
        'TLSV1_ALERT_NO_RENEGOTIATION'
    ,
    (
        20,
        1109,
    ): 
        'TLSV13_ALERT_MISSING_EXTENSION'
    ,
    (
        20,
        1110,
    ): 
        'TLSV1_UNSUPPORTED_EXTENSION'
    ,
    (
        20,
        1111,
    ): 
        'TLSV1_CERTIFICATE_UNOBTAINABLE'
    ,
    (
        20,
        1112,
    ): 
        'TLSV1_UNRECOGNIZED_NAME'
    ,
    (
        20,
        1113,
    ): 
        'TLSV1_BAD_CERTIFICATE_STATUS_RESPONSE'
    ,
    (
        20,
        1114,
    ): 
        'TLSV1_BAD_CERTIFICATE_HASH_VALUE'
    ,
    (
        20,
        1116,
    ): 
        'TLSV13_ALERT_CERTIFICATE_REQUIRED'
    ,
    (
        32,
        100,
    ): 
        'ACCEPT_ERROR'
    ,
    (
        32,
        101,
    ): 
        'BAD_FOPEN_MODE'
    ,
    (
        32,
        102,
    ): 
        'LENGTH_TOO_LONG'
    ,
    (
        32,
        103,
    ): 
        'CONNECT_ERROR'
    ,
    (
        32,
        104,
    ): 
        'TRANSFER_ERROR'
    ,
    (
        32,
        105,
    ): 
        'TRANSFER_TIMEOUT'
    ,
    (
        32,
        107,
    ): 
        'GETHOSTBYNAME_ADDR_IS_NOT_AF_INET'
    ,
    (
        32,
        110,
    ): 
        'NBIO_CONNECT_ERROR'
    ,
    (
        32,
        113,
    ): 
        'NO_PORT_DEFINED'
    ,
    (
        32,
        117,
    ): 
        'UNABLE_TO_BIND_SOCKET'
    ,
    (
        32,
        118,
    ): 
        'UNABLE_TO_CREATE_SOCKET'
    ,
    (
        32,
        119,
    ): 
        'UNABLE_TO_LISTEN_SOCKET'
    ,
    (
        32,
        120,
    ): 
        'UNINITIALIZED'
    ,
    (
        32,
        121,
    ): 
        'UNSUPPORTED_METHOD'
    ,
    (
        32,
        122,
    ): 
        'WSASTARTUP'
    ,
    (
        32,
        123,
    ): 
        'IN_USE'
    ,
    (
        32,
        124,
    ): 
        'BROKEN_PIPE'
    ,
    (
        32,
        125,
    ): 
        'INVALID_ARGUMENT'
    ,
    (
        32,
        126,
    ): 
        'WRITE_TO_READ_ONLY_BIO'
    ,
    (
        32,
        128,
    ): 
        'NO_SUCH_FILE'
    ,
    (
        32,
        129,
    ): 
        'AMBIGUOUS_HOST_OR_SERVICE'
    ,
    (
        32,
        130,
    ): 
        'MALFORMED_HOST_OR_SERVICE'
    ,
    (
        32,
        131,
    ): 
        'UNSUPPORTED_PROTOCOL_FAMILY'
    ,
    (
        32,
        132,
    ): 
        'GETSOCKNAME_ERROR'
    ,
    (
        32,
        133,
    ): 
        'GETSOCKNAME_TRUNCATED_ADDRESS'
    ,
    (
        32,
        134,
    ): 
        'GETTING_SOCKTYPE'
    ,
    (
        32,
        135,
    ): 
        'INVALID_SOCKET'
    ,
    (
        32,
        136,
    ): 
        'LISTEN_V6_ONLY'
    ,
    (
        32,
        137,
    ): 
        'UNABLE_TO_KEEPALIVE'
    ,
    (
        32,
        138,
    ): 
        'UNABLE_TO_NODELAY'
    ,
    (
        32,
        139,
    ): 
        'UNABLE_TO_REUSEADDR'
    ,
    (
        32,
        140,
    ): 
        'UNKNOWN_INFO_TYPE'
    ,
    (
        32,
        141,
    ): 
        'ADDRINFO_ADDR_IS_NOT_AF_INET'
    ,
    (
        32,
        142,
    ): 
        'LOOKUP_RETURNED_NOTHING'
    ,
    (
        32,
        143,
    ): 
        'NO_ACCEPT_ADDR_OR_SERVICE_SPECIFIED'
    ,
    (
        32,
        144,
    ): 
        'NO_HOSTNAME_OR_SERVICE_SPECIFIED'
    ,
    (
        32,
        145,
    ): 
        'UNAVAILABLE_IP_FAMILY'
    ,
    (
        32,
        146,
    ): 
        'UNSUPPORTED_IP_FAMILY'
    ,
    (
        32,
        147,
    ): 
        'CONNECT_TIMEOUT'
    ,
    (
        33,
        101,
    ): 
        'DIGEST_FAILURE'
    ,
    (
        33,
        104,
    ): 
        'OPERATION_NOT_SUPPORTED_ON_THIS_TYPE'
    ,
    (
        33,
        105,
    ): 
        'SIGNATURE_FAILURE'
    ,
    (
        33,
        106,
    ): 
        'UNABLE_TO_FIND_CERTIFICATE'
    ,
    (
        33,
        107,
    ): 
        'UNABLE_TO_FIND_MEM_BIO'
    ,
    (
        33,
        108,
    ): 
        'UNABLE_TO_FIND_MESSAGE_DIGEST'
    ,
    (
        33,
        109,
    ): 
        'UNKNOWN_DIGEST_TYPE'
    ,
    (
        33,
        110,
    ): 
        'UNKNOWN_OPERATION'
    ,
    (
        33,
        111,
    ): 
        'UNSUPPORTED_CIPHER_TYPE'
    ,
    (
        33,
        112,
    ): 
        'UNSUPPORTED_CONTENT_TYPE'
    ,
    (
        33,
        113,
    ): 
        'WRONG_CONTENT_TYPE'
    ,
    (
        33,
        114,
    ): 
        'WRONG_PKCS7_TYPE'
    ,
    (
        33,
        115,
    ): 
        'NO_RECIPIENT_MATCHES_CERTIFICATE'
    ,
    (
        33,
        116,
    ): 
        'CIPHER_NOT_INITIALIZED'
    ,
    (
        33,
        117,
    ): 
        'CERTIFICATE_VERIFY_ERROR'
    ,
    (
        33,
        118,
    ): 
        'CONTENT_AND_DATA_PRESENT'
    ,
    (
        33,
        119,
    ): 
        'DECRYPT_ERROR'
    ,
    (
        33,
        120,
    ): 
        'ERROR_ADDING_RECIPIENT'
    ,
    (
        33,
        121,
    ): 
        'ERROR_SETTING_CIPHER'
    ,
    (
        33,
        122,
    ): 
        'NO_CONTENT'
    ,
    (
        33,
        123,
    ): 
        'NO_SIGNATURES_ON_DATA'
    ,
    (
        33,
        124,
    ): 
        'PKCS7_ADD_SIGNATURE_ERROR'
    ,
    (
        33,
        127,
    ): 
        'PRIVATE_KEY_DOES_NOT_MATCH_CERTIFICATE'
    ,
    (
        33,
        128,
    ): 
        'SIGNER_CERTIFICATE_NOT_FOUND'
    ,
    (
        33,
        129,
    ): 
        'SMIME_TEXT_ERROR'
    ,
    (
        33,
        142,
    ): 
        'NO_SIGNERS'
    ,
    (
        33,
        143,
    ): 
        'INVALID_NULL_POINTER'
    ,
    (
        33,
        144,
    ): 
        'CIPHER_HAS_NO_OBJECT_IDENTIFIER'
    ,
    (
        33,
        145,
    ): 
        'PKCS7_DATASIGN'
    ,
    (
        33,
        147,
    ): 
        'SIGNING_CTRL_FAILURE'
    ,
    (
        33,
        148,
    ): 
        'SIGNING_NOT_SUPPORTED_FOR_THIS_KEY_TYPE'
    ,
    (
        33,
        149,
    ): 
        'ENCRYPTION_CTRL_FAILURE'
    ,
    (
        33,
        150,
    ): 
        'ENCRYPTION_NOT_SUPPORTED_FOR_THIS_KEY_TYPE'
    ,
    (
        33,
        151,
    ): 
        'NO_DEFAULT_DIGEST'
    ,
    (
        33,
        152,
    ): 
        'CTRL_ERROR'
    ,
    (
        33,
        153,
    ): 
        'PKCS7_ADD_SIGNER_ERROR'
    ,
    (
        33,
        154,
    ): 
        'NO_MATCHING_DIGEST_TYPE_FOUND'
    ,
    (
        33,
        155,
    ): 
        'INVALID_SIGNED_DATA_TYPE'
    ,
    (
        34,
        100,
    ): 
        'BN_DEC2BN_ERROR'
    ,
    (
        34,
        101,
    ): 
        'BN_TO_ASN1_INTEGER_ERROR'
    ,
    (
        34,
        102,
    ): 
        'EXTENSION_NOT_FOUND'
    ,
    (
        34,
        103,
    ): 
        'EXTENSION_SETTING_NOT_SUPPORTED'
    ,
    (
        34,
        104,
    ): 
        'INVALID_BOOLEAN_STRING'
    ,
    (
        34,
        105,
    ): 
        'INVALID_EXTENSION_STRING'
    ,
    (
        34,
        106,
    ): 
        'INVALID_NAME'
    ,
    (
        34,
        107,
    ): 
        'INVALID_NULL_ARGUMENT'
    ,
    (
        34,
        108,
    ): 
        'INVALID_EMPTY_NAME'
    ,
    (
        34,
        109,
    ): 
        'INVALID_NULL_VALUE'
    ,
    (
        34,
        110,
    ): 
        'INVALID_OBJECT_IDENTIFIER'
    ,
    (
        34,
        111,
    ): 
        'UNKNOWN_BIT_STRING_ARGUMENT'
    ,
    (
        34,
        114,
    ): 
        'NO_PUBLIC_KEY'
    ,
    (
        34,
        115,
    ): 
        'EXTENSION_NAME_ERROR'
    ,
    (
        34,
        116,
    ): 
        'EXTENSION_VALUE_ERROR'
    ,
    (
        34,
        117,
    ): 
        'UNSUPPORTED_OPTION'
    ,
    (
        34,
        118,
    ): 
        'BAD_IP_ADDRESS'
    ,
    (
        34,
        119,
    ): 
        'BAD_OBJECT'
    ,
    (
        34,
        120,
    ): 
        'UNKNOWN_OPTION'
    ,
    (
        34,
        121,
    ): 
        'NO_ISSUER_CERTIFICATE'
    ,
    (
        34,
        122,
    ): 
        'UNABLE_TO_GET_ISSUER_DETAILS'
    ,
    (
        34,
        123,
    ): 
        'UNABLE_TO_GET_ISSUER_KEYID'
    ,
    (
        34,
        124,
    ): 
        'MISSING_VALUE'
    ,
    (
        34,
        125,
    ): 
        'NO_SUBJECT_DETAILS'
    ,
    (
        34,
        126,
    ): 
        'ISSUER_DECODE_ERROR'
    ,
    (
        34,
        127,
    ): 
        'NO_ISSUER_DETAILS'
    ,
    (
        34,
        128,
    ): 
        'ERROR_IN_EXTENSION'
    ,
    (
        34,
        129,
    ): 
        'UNKNOWN_EXTENSION'
    ,
    (
        34,
        130,
    ): 
        'UNKNOWN_EXTENSION_NAME'
    ,
    (
        34,
        131,
    ): 
        'ERROR_CONVERTING_ZONE'
    ,
    (
        34,
        132,
    ): 
        'USER_TOO_LONG'
    ,
    (
        34,
        133,
    ): 
        'DUPLICATE_ZONE_ID'
    ,
    (
        34,
        134,
    ): 
        'INVALID_POLICY_IDENTIFIER'
    ,
    (
        34,
        135,
    ): 
        'INVALID_SECTION'
    ,
    (
        34,
        136,
    ): 
        'NO_CONFIG_DATABASE'
    ,
    (
        34,
        137,
    ): 
        'EXPECTED_A_SECTION_NAME'
    ,
    (
        34,
        138,
    ): 
        'INVALID_OPTION'
    ,
    (
        34,
        139,
    ): 
        'NO_POLICY_IDENTIFIER'
    ,
    (
        34,
        140,
    ): 
        'INVALID_NUMBER'
    ,
    (
        34,
        141,
    ): 
        'INVALID_NUMBERS'
    ,
    (
        34,
        142,
    ): 
        'NEED_ORGANIZATION_AND_NUMBERS'
    ,
    (
        34,
        143,
    ): 
        'INVALID_SYNTAX'
    ,
    (
        34,
        144,
    ): 
        'ERROR_CREATING_EXTENSION'
    ,
    (
        34,
        145,
    ): 
        'EXTENSION_EXISTS'
    ,
    (
        34,
        146,
    ): 
        'INVALID_PURPOSE'
    ,
    (
        34,
        147,
    ): 
        'OTHERNAME_ERROR'
    ,
    (
        34,
        148,
    ): 
        'OPERATION_NOT_DEFINED'
    ,
    (
        34,
        149,
    ): 
        'DIRNAME_ERROR'
    ,
    (
        34,
        150,
    ): 
        'SECTION_NOT_FOUND'
    ,
    (
        34,
        151,
    ): 
        'ILLEGAL_EMPTY_EXTENSION'
    ,
    (
        34,
        152,
    ): 
        'INCORRECT_POLICY_SYNTAX_TAG'
    ,
    (
        34,
        153,
    ): 
        'INVALID_PROXY_POLICY_SETTING'
    ,
    (
        34,
        154,
    ): 
        'NO_PROXY_CERT_POLICY_LANGUAGE_DEFINED'
    ,
    (
        34,
        155,
    ): 
        'POLICY_LANGUAGE_ALREADY_DEFINED'
    ,
    (
        34,
        156,
    ): 
        'POLICY_PATH_LENGTH'
    ,
    (
        34,
        157,
    ): 
        'POLICY_PATH_LENGTH_ALREADY_DEFINED'
    ,
    (
        34,
        158,
    ): 
        'INVALID_CERTIFICATE'
    ,
    (
        34,
        159,
    ): 
        'POLICY_WHEN_PROXY_LANGUAGE_REQUIRES_NO_POLICY'
    ,
    (
        34,
        160,
    ): 
        'DISTPOINT_ALREADY_SET'
    ,
    (
        34,
        161,
    ): 
        'INVALID_MULTIPLE_RDNS'
    ,
    (
        34,
        162,
    ): 
        'INVALID_ASNUMBER'
    ,
    (
        34,
        163,
    ): 
        'INVALID_ASRANGE'
    ,
    (
        34,
        164,
    ): 
        'INVALID_SAFI'
    ,
    (
        34,
        165,
    ): 
        'INVALID_INHERITANCE'
    ,
    (
        34,
        166,
    ): 
        'INVALID_IPADDRESS'
    ,
    (
        34,
        167,
    ): 
        'UNSUPPORTED_TYPE'
    ,
    (
        34,
        168,
    ): 
        'NEGATIVE_PATHLEN'
    ,
    (
        34,
        169,
    ): 
        'EMPTY_KEY_USAGE'
    ,
    (
        35,
        100,
    ): 
        'CANT_PACK_STRUCTURE'
    ,
    (
        35,
        101,
    ): 
        'DECODE_ERROR'
    ,
    (
        35,
        102,
    ): 
        'ENCODE_ERROR'
    ,
    (
        35,
        103,
    ): 
        'ENCRYPT_ERROR'
    ,
    (
        35,
        104,
    ): 
        'INVALID_NULL_ARGUMENT'
    ,
    (
        35,
        105,
    ): 
        'INVALID_NULL_PKCS12_POINTER'
    ,
    (
        35,
        106,
    ): 
        'IV_GEN_ERROR'
    ,
    (
        35,
        107,
    ): 
        'KEY_GEN_ERROR'
    ,
    (
        35,
        108,
    ): 
        'MAC_ABSENT'
    ,
    (
        35,
        109,
    ): 
        'MAC_GENERATION_ERROR'
    ,
    (
        35,
        110,
    ): 
        'MAC_SETUP_ERROR'
    ,
    (
        35,
        111,
    ): 
        'MAC_STRING_SET_ERROR'
    ,
    (
        35,
        112,
    ): 
        'INVALID_TYPE'
    ,
    (
        35,
        113,
    ): 
        'MAC_VERIFY_FAILURE'
    ,
    (
        35,
        114,
    ): 
        'PARSE_ERROR'
    ,
    (
        35,
        116,
    ): 
        'PKCS12_CIPHERFINAL_ERROR'
    ,
    (
        35,
        118,
    ): 
        'UNKNOWN_DIGEST_ALGORITHM'
    ,
    (
        35,
        119,
    ): 
        'UNSUPPORTED_PKCS12_MODE'
    ,
    (
        35,
        120,
    ): 
        'ERROR_SETTING_ENCRYPTED_DATA_TYPE'
    ,
    (
        35,
        121,
    ): 
        'CONTENT_TYPE_NOT_DATA'
    ,
    (
        36,
        100,
    ): 
        'PRNG_NOT_SEEDED'
    ,
    (
        36,
        101,
    ): 
        'FUNC_NOT_IMPLEMENTED'
    ,
    (
        36,
        102,
    ): 
        'ADDITIONAL_INPUT_TOO_LONG'
    ,
    (
        36,
        103,
    ): 
        'ALREADY_INSTANTIATED'
    ,
    (
        36,
        104,
    ): 
        'DRBG_NOT_INITIALISED'
    ,
    (
        36,
        105,
    ): 
        'ARGUMENT_OUT_OF_RANGE'
    ,
    (
        36,
        106,
    ): 
        'ENTROPY_INPUT_TOO_LONG'
    ,
    (
        36,
        107,
    ): 
        'ERROR_INITIALISING_DRBG'
    ,
    (
        36,
        108,
    ): 
        'ERROR_INSTANTIATING_DRBG'
    ,
    (
        36,
        109,
    ): 
        'ERROR_RETRIEVING_ADDITIONAL_INPUT'
    ,
    (
        36,
        110,
    ): 
        'ERROR_RETRIEVING_ENTROPY'
    ,
    (
        36,
        111,
    ): 
        'ERROR_RETRIEVING_NONCE'
    ,
    (
        36,
        112,
    ): 
        'GENERATE_ERROR'
    ,
    (
        36,
        113,
    ): 
        'INTERNAL_ERROR'
    ,
    (
        36,
        114,
    ): 
        'IN_ERROR_STATE'
    ,
    (
        36,
        115,
    ): 
        'NOT_INSTANTIATED'
    ,
    (
        36,
        116,
    ): 
        'PERSONALISATION_STRING_TOO_LONG'
    ,
    (
        36,
        117,
    ): 
        'REQUEST_TOO_LARGE_FOR_DRBG'
    ,
    (
        36,
        118,
    ): 
        'RESEED_ERROR'
    ,
    (
        36,
        119,
    ): 
        'SELFTEST_FAILURE'
    ,
    (
        36,
        120,
    ): 
        'UNSUPPORTED_DRBG_TYPE'
    ,
    (
        36,
        121,
    ): 
        'CANNOT_OPEN_FILE'
    ,
    (
        36,
        122,
    ): 
        'NOT_A_REGULAR_FILE'
    ,
    (
        36,
        123,
    ): 
        'FWRITE_ERROR'
    ,
    (
        36,
        124,
    ): 
        'ENTROPY_OUT_OF_RANGE'
    ,
    (
        36,
        125,
    ): 
        'RANDOM_POOL_OVERFLOW'
    ,
    (
        36,
        126,
    ): 
        'FAILED_TO_CREATE_LOCK'
    ,
    (
        36,
        127,
    ): 
        'ERROR_ENTROPY_POOL_WAS_IGNORED'
    ,
    (
        36,
        128,
    ): 
        'NO_DRBG_IMPLEMENTATION_SELECTED'
    ,
    (
        36,
        129,
    ): 
        'DRBG_ALREADY_INITIALIZED'
    ,
    (
        36,
        130,
    ): 
        'PARENT_LOCKING_NOT_ENABLED'
    ,
    (
        36,
        131,
    ): 
        'PARENT_STRENGTH_TOO_WEAK'
    ,
    (
        36,
        132,
    ): 
        'UNSUPPORTED_DRBG_FLAGS'
    ,
    (
        36,
        133,
    ): 
        'PREDICTION_RESISTANCE_NOT_SUPPORTED'
    ,
    (
        36,
        134,
    ): 
        'RANDOM_POOL_UNDERFLOW'
    ,
    (
        36,
        135,
    ): 
        'TOO_LITTLE_NONCE_REQUESTED'
    ,
    (
        36,
        136,
    ): 
        'TOO_MUCH_NONCE_REQUESTED'
    ,
    (
        36,
        137,
    ): 
        'DERIVATION_FUNCTION_MANDATORY_FOR_FIPS'
    ,
    (
        36,
        138,
    ): 
        'UNABLE_TO_GET_PARENT_STRENGTH'
    ,
    (
        36,
        139,
    ): 
        'INSUFFICIENT_DRBG_STRENGTH'
    ,
    (
        36,
        140,
    ): 
        'UNABLE_TO_LOCK_PARENT'
    ,
    (
        36,
        141,
    ): 
        'UNABLE_TO_GET_PARENT_RESEED_PROP_COUNTER'
    ,
    (
        36,
        143,
    ): 
        'UNABLE_TO_CREATE_DRBG'
    ,
    (
        36,
        144,
    ): 
        'UNABLE_TO_FETCH_DRBG'
    ,
    (
        37,
        100,
    ): 
        'CTRL_FAILED'
    ,
    (
        37,
        101,
    ): 
        'FILENAME_TOO_BIG'
    ,
    (
        37,
        102,
    ): 
        'FINISH_FAILED'
    ,
    (
        37,
        103,
    ): 
        'LOAD_FAILED'
    ,
    (
        37,
        104,
    ): 
        'NULL_HANDLE'
    ,
    (
        37,
        105,
    ): 
        'STACK_ERROR'
    ,
    (
        37,
        106,
    ): 
        'SYM_FAILURE'
    ,
    (
        37,
        107,
    ): 
        'UNLOAD_FAILED'
    ,
    (
        37,
        108,
    ): 
        'UNSUPPORTED'
    ,
    (
        37,
        109,
    ): 
        'NAME_TRANSLATION_FAILED'
    ,
    (
        37,
        110,
    ): 
        'DSO_ALREADY_LOADED'
    ,
    (
        37,
        111,
    ): 
        'NO_FILENAME'
    ,
    (
        37,
        112,
    ): 
        'SET_FILENAME_FAILED'
    ,
    (
        37,
        113,
    ): 
        'EMPTY_FILE_STRUCTURE'
    ,
    (
        37,
        114,
    ): 
        'FAILURE'
    ,
    (
        37,
        115,
    ): 
        'INCORRECT_FILE_SYNTAX'
    ,
    (
        38,
        100,
    ): 
        'ALREADY_LOADED'
    ,
    (
        38,
        101,
    ): 
        'UNIMPLEMENTED_PUBLIC_KEY_METHOD'
    ,
    (
        38,
        102,
    ): 
        'ENGINE_CONFIGURATION_ERROR'
    ,
    (
        38,
        103,
    ): 
        'CONFLICTING_ENGINE_ID'
    ,
    (
        38,
        104,
    ): 
        'DSO_FAILURE'
    ,
    (
        38,
        105,
    ): 
        'ENGINE_IS_NOT_IN_LIST'
    ,
    (
        38,
        106,
    ): 
        'FINISH_FAILED'
    ,
    (
        38,
        108,
    ): 
        'ID_OR_NAME_MISSING'
    ,
    (
        38,
        109,
    ): 
        'INIT_FAILED'
    ,
    (
        38,
        110,
    ): 
        'INTERNAL_LIST_ERROR'
    ,
    (
        38,
        112,
    ): 
        'NOT_LOADED'
    ,
    (
        38,
        116,
    ): 
        'NO_SUCH_ENGINE'
    ,
    (
        38,
        117,
    ): 
        'NOT_INITIALISED'
    ,
    (
        38,
        119,
    ): 
        'CTRL_COMMAND_NOT_IMPLEMENTED'
    ,
    (
        38,
        120,
    ): 
        'NO_CONTROL_FUNCTION'
    ,
    (
        38,
        125,
    ): 
        'NO_LOAD_FUNCTION'
    ,
    (
        38,
        128,
    ): 
        'FAILED_LOADING_PRIVATE_KEY'
    ,
    (
        38,
        129,
    ): 
        'FAILED_LOADING_PUBLIC_KEY'
    ,
    (
        38,
        130,
    ): 
        'NO_REFERENCE'
    ,
    (
        38,
        132,
    ): 
        'DSO_NOT_FOUND'
    ,
    (
        38,
        133,
    ): 
        'ARGUMENT_IS_NOT_A_NUMBER'
    ,
    (
        38,
        134,
    ): 
        'CMD_NOT_EXECUTABLE'
    ,
    (
        38,
        135,
    ): 
        'COMMAND_TAKES_INPUT'
    ,
    (
        38,
        136,
    ): 
        'COMMAND_TAKES_NO_INPUT'
    ,
    (
        38,
        137,
    ): 
        'INVALID_CMD_NAME'
    ,
    (
        38,
        138,
    ): 
        'INVALID_CMD_NUMBER'
    ,
    (
        38,
        143,
    ): 
        'INVALID_ARGUMENT'
    ,
    (
        38,
        144,
    ): 
        'NO_INDEX'
    ,
    (
        38,
        145,
    ): 
        'VERSION_INCOMPATIBILITY'
    ,
    (
        38,
        146,
    ): 
        'UNIMPLEMENTED_CIPHER'
    ,
    (
        38,
        147,
    ): 
        'UNIMPLEMENTED_DIGEST'
    ,
    (
        38,
        148,
    ): 
        'ENGINES_SECTION_ERROR'
    ,
    (
        38,
        149,
    ): 
        'ENGINE_SECTION_ERROR'
    ,
    (
        38,
        150,
    ): 
        'INVALID_STRING'
    ,
    (
        38,
        151,
    ): 
        'INVALID_INIT_VALUE'
    ,
    (
        39,
        101,
    ): 
        'CERTIFICATE_VERIFY_ERROR'
    ,
    (
        39,
        102,
    ): 
        'DIGEST_ERR'
    ,
    (
        39,
        103,
    ): 
        'MISSING_OCSPSIGNING_USAGE'
    ,
    (
        39,
        104,
    ): 
        'NOT_BASIC_RESPONSE'
    ,
    (
        39,
        105,
    ): 
        'NO_CERTIFICATES_IN_CHAIN'
    ,
    (
        39,
        106,
    ): 
        'DIGEST_NAME_ERR'
    ,
    (
        39,
        107,
    ): 
        'DIGEST_SIZE_ERR'
    ,
    (
        39,
        108,
    ): 
        'NO_RESPONSE_DATA'
    ,
    (
        39,
        109,
    ): 
        'NO_REVOKED_TIME'
    ,
    (
        39,
        110,
    ): 
        'PRIVATE_KEY_DOES_NOT_MATCH_CERTIFICATE'
    ,
    (
        39,
        111,
    ): 
        'RESPONSE_CONTAINS_NO_REVOCATION_DATA'
    ,
    (
        39,
        112,
    ): 
        'ROOT_CA_NOT_TRUSTED'
    ,
    (
        39,
        117,
    ): 
        'SIGNATURE_FAILURE'
    ,
    (
        39,
        118,
    ): 
        'SIGNER_CERTIFICATE_NOT_FOUND'
    ,
    (
        39,
        119,
    ): 
        'UNKNOWN_MESSAGE_DIGEST'
    ,
    (
        39,
        120,
    ): 
        'UNKNOWN_NID'
    ,
    (
        39,
        122,
    ): 
        'ERROR_IN_NEXTUPDATE_FIELD'
    ,
    (
        39,
        123,
    ): 
        'ERROR_IN_THISUPDATE_FIELD'
    ,
    (
        39,
        124,
    ): 
        'NEXTUPDATE_BEFORE_THISUPDATE'
    ,
    (
        39,
        125,
    ): 
        'STATUS_EXPIRED'
    ,
    (
        39,
        126,
    ): 
        'STATUS_NOT_YET_VALID'
    ,
    (
        39,
        127,
    ): 
        'STATUS_TOO_OLD'
    ,
    (
        39,
        128,
    ): 
        'REQUEST_NOT_SIGNED'
    ,
    (
        39,
        129,
    ): 
        'UNSUPPORTED_REQUESTORNAME_TYPE'
    ,
    (
        39,
        130,
    ): 
        'NO_SIGNER_KEY'
    ,
    (
        40,
        100,
    ): 
        'RESULT_TOO_LARGE'
    ,
    (
        40,
        101,
    ): 
        'RESULT_TOO_SMALL'
    ,
    (
        40,
        102,
    ): 
        'INDEX_TOO_LARGE'
    ,
    (
        40,
        103,
    ): 
        'INDEX_TOO_SMALL'
    ,
    (
        40,
        104,
    ): 
        'COMMON_OK_AND_CANCEL_CHARACTERS'
    ,
    (
        40,
        105,
    ): 
        'NO_RESULT_BUFFER'
    ,
    (
        40,
        106,
    ): 
        'UNKNOWN_CONTROL_COMMAND'
    ,
    (
        40,
        107,
    ): 
        'PROCESSING_ERROR'
    ,
    (
        40,
        108,
    ): 
        'UNKNOWN_TTYGET_ERRNO_VALUE'
    ,
    (
        40,
        109,
    ): 
        'SYSASSIGN_ERROR'
    ,
    (
        40,
        110,
    ): 
        'SYSDASSGN_ERROR'
    ,
    (
        40,
        111,
    ): 
        'SYSQIOW_ERROR'
    ,
    (
        40,
        112,
    ): 
        'USER_DATA_DUPLICATION_UNSUPPORTED'
    ,
    (
        41,
        99,
    ): 
        'ZLIB_DEFLATE_ERROR'
    ,
    (
        41,
        100,
    ): 
        'ZLIB_INFLATE_ERROR'
    ,
    (
        41,
        101,
    ): 
        'ZLIB_NOT_SUPPORTED'
    ,
    (
        44,
        100,
    ): 
        'NOT_A_CERTIFICATE'
    ,
    (
        44,
        101,
    ): 
        'NOT_A_CRL'
    ,
    (
        44,
        102,
    ): 
        'NOT_A_PRIVATE_KEY'
    ,
    (
        44,
        103,
    ): 
        'NOT_A_NAME'
    ,
    (
        44,
        104,
    ): 
        'NOT_PARAMETERS'
    ,
    (
        44,
        105,
    ): 
        'UNREGISTERED_SCHEME'
    ,
    (
        44,
        106,
    ): 
        'INVALID_SCHEME'
    ,
    (
        44,
        107,
    ): 
        'AMBIGUOUS_CONTENT_TYPE'
    ,
    (
        44,
        108,
    ): 
        'PATH_MUST_BE_ABSOLUTE'
    ,
    (
        44,
        109,
    ): 
        'UI_PROCESS_INTERRUPTED_OR_CANCELLED'
    ,
    (
        44,
        110,
    ): 
        'UNSUPPORTED_CONTENT_TYPE'
    ,
    (
        44,
        111,
    ): 
        'URI_AUTHORITY_UNSUPPORTED'
    ,
    (
        44,
        112,
    ): 
        'IS_NOT_A'
    ,
    (
        44,
        113,
    ): 
        'ERROR_VERIFYING_PKCS12_MAC'
    ,
    (
        44,
        114,
    ): 
        'PASSPHRASE_CALLBACK_ERROR'
    ,
    (
        44,
        115,
    ): 
        'BAD_PASSWORD_READ'
    ,
    (
        44,
        116,
    ): 
        'LOADER_INCOMPLETE'
    ,
    (
        44,
        117,
    ): 
        'LOADING_STARTED'
    ,
    (
        44,
        118,
    ): 
        'UNSUPPORTED_OPERATION'
    ,
    (
        44,
        119,
    ): 
        'SEARCH_ONLY_SUPPORTED_FOR_DIRECTORIES'
    ,
    (
        44,
        120,
    ): 
        'UNSUPPORTED_SEARCH_TYPE'
    ,
    (
        44,
        121,
    ): 
        'FINGERPRINT_SIZE_DOES_NOT_MATCH_DIGEST'
    ,
    (
        44,
        122,
    ): 
        'NOT_A_PUBLIC_KEY'
    ,
    (
        44,
        123,
    ): 
        'NO_LOADERS_FOUND'
    ,
    (
        46,
        99,
    ): 
        'ADD_SIGNER_ERROR'
    ,
    (
        46,
        100,
    ): 
        'CERTIFICATE_VERIFY_ERROR'
    ,
    (
        46,
        101,
    ): 
        'CIPHER_INITIALISATION_ERROR'
    ,
    (
        46,
        102,
    ): 
        'CIPHER_PARAMETER_INITIALISATION_ERROR'
    ,
    (
        46,
        103,
    ): 
        'CMS_DATAFINAL_ERROR'
    ,
    (
        46,
        104,
    ): 
        'CMS_LIB'
    ,
    (
        46,
        105,
    ): 
        'CONTENT_NOT_FOUND'
    ,
    (
        46,
        106,
    ): 
        'CONTENT_TYPE_NOT_COMPRESSED_DATA'
    ,
    (
        46,
        107,
    ): 
        'CONTENT_TYPE_NOT_ENVELOPED_DATA'
    ,
    (
        46,
        108,
    ): 
        'CONTENT_TYPE_NOT_SIGNED_DATA'
    ,
    (
        46,
        109,
    ): 
        'CONTENT_VERIFY_ERROR'
    ,
    (
        46,
        110,
    ): 
        'CTRL_ERROR'
    ,
    (
        46,
        111,
    ): 
        'CTRL_FAILURE'
    ,
    (
        46,
        112,
    ): 
        'DECRYPT_ERROR'
    ,
    (
        46,
        113,
    ): 
        'ERROR_GETTING_PUBLIC_KEY'
    ,
    (
        46,
        114,
    ): 
        'ERROR_READING_MESSAGEDIGEST_ATTRIBUTE'
    ,
    (
        46,
        115,
    ): 
        'ERROR_SETTING_KEY'
    ,
    (
        46,
        116,
    ): 
        'ERROR_SETTING_RECIPIENTINFO'
    ,
    (
        46,
        117,
    ): 
        'INVALID_ENCRYPTED_KEY_LENGTH'
    ,
    (
        46,
        118,
    ): 
        'INVALID_KEY_LENGTH'
    ,
    (
        46,
        119,
    ): 
        'MD_BIO_INIT_ERROR'
    ,
    (
        46,
        120,
    ): 
        'MESSAGEDIGEST_ATTRIBUTE_WRONG_LENGTH'
    ,
    (
        46,
        121,
    ): 
        'MESSAGEDIGEST_WRONG_LENGTH'
    ,
    (
        46,
        122,
    ): 
        'NOT_ENCRYPTED_DATA'
    ,
    (
        46,
        123,
    ): 
        'NOT_KEK'
    ,
    (
        46,
        124,
    ): 
        'NOT_KEY_TRANSPORT'
    ,
    (
        46,
        125,
    ): 
        'NOT_SUPPORTED_FOR_THIS_KEY_TYPE'
    ,
    (
        46,
        126,
    ): 
        'NO_CIPHER'
    ,
    (
        46,
        127,
    ): 
        'NO_CONTENT'
    ,
    (
        46,
        128,
    ): 
        'NO_DEFAULT_DIGEST'
    ,
    (
        46,
        129,
    ): 
        'NO_DIGEST_SET'
    ,
    (
        46,
        130,
    ): 
        'NO_KEY'
    ,
    (
        46,
        131,
    ): 
        'NO_MATCHING_DIGEST'
    ,
    (
        46,
        132,
    ): 
        'NO_MATCHING_RECIPIENT'
    ,
    (
        46,
        133,
    ): 
        'NO_PRIVATE_KEY'
    ,
    (
        46,
        134,
    ): 
        'NO_PUBLIC_KEY'
    ,
    (
        46,
        135,
    ): 
        'NO_SIGNERS'
    ,
    (
        46,
        136,
    ): 
        'PRIVATE_KEY_DOES_NOT_MATCH_CERTIFICATE'
    ,
    (
        46,
        137,
    ): 
        'RECIPIENT_ERROR'
    ,
    (
        46,
        138,
    ): 
        'SIGNER_CERTIFICATE_NOT_FOUND'
    ,
    (
        46,
        139,
    ): 
        'SIGNFINAL_ERROR'
    ,
    (
        46,
        140,
    ): 
        'SMIME_TEXT_ERROR'
    ,
    (
        46,
        141,
    ): 
        'STORE_INIT_ERROR'
    ,
    (
        46,
        142,
    ): 
        'TYPE_NOT_COMPRESSED_DATA'
    ,
    (
        46,
        143,
    ): 
        'TYPE_NOT_DATA'
    ,
    (
        46,
        144,
    ): 
        'TYPE_NOT_DIGESTED_DATA'
    ,
    (
        46,
        145,
    ): 
        'TYPE_NOT_ENCRYPTED_DATA'
    ,
    (
        46,
        146,
    ): 
        'TYPE_NOT_ENVELOPED_DATA'
    ,
    (
        46,
        147,
    ): 
        'UNABLE_TO_FINALIZE_CONTEXT'
    ,
    (
        46,
        148,
    ): 
        'UNKNOWN_CIPHER'
    ,
    (
        46,
        149,
    ): 
        'UNKNOWN_DIGEST_ALGORITHM'
    ,
    (
        46,
        150,
    ): 
        'UNKNOWN_ID'
    ,
    (
        46,
        151,
    ): 
        'UNSUPPORTED_COMPRESSION_ALGORITHM'
    ,
    (
        46,
        152,
    ): 
        'UNSUPPORTED_CONTENT_TYPE'
    ,
    (
        46,
        153,
    ): 
        'UNSUPPORTED_KEK_ALGORITHM'
    ,
    (
        46,
        154,
    ): 
        'UNSUPPORTED_RECIPIENT_TYPE'
    ,
    (
        46,
        155,
    ): 
        'UNSUPPORTED_RECIPIENTINFO_TYPE'
    ,
    (
        46,
        156,
    ): 
        'UNSUPPORTED_TYPE'
    ,
    (
        46,
        157,
    ): 
        'UNWRAP_ERROR'
    ,
    (
        46,
        158,
    ): 
        'VERIFICATION_FAILURE'
    ,
    (
        46,
        159,
    ): 
        'WRAP_ERROR'
    ,
    (
        46,
        160,
    ): 
        'CERTIFICATE_HAS_NO_KEYID'
    ,
    (
        46,
        161,
    ): 
        'ATTRIBUTE_ERROR'
    ,
    (
        46,
        162,
    ): 
        'MSGSIGDIGEST_VERIFICATION_FAILURE'
    ,
    (
        46,
        163,
    ): 
        'MSGSIGDIGEST_WRONG_LENGTH'
    ,
    (
        46,
        164,
    ): 
        'NEED_ONE_SIGNER'
    ,
    (
        46,
        165,
    ): 
        'NOT_A_SIGNED_RECEIPT'
    ,
    (
        46,
        166,
    ): 
        'NO_MATCHING_SIGNATURE'
    ,
    (
        46,
        167,
    ): 
        'NO_MSGSIGDIGEST'
    ,
    (
        46,
        168,
    ): 
        'NO_RECEIPT_REQUEST'
    ,
    (
        46,
        169,
    ): 
        'RECEIPT_DECODE_ERROR'
    ,
    (
        46,
        170,
    ): 
        'CONTENTIDENTIFIER_MISMATCH'
    ,
    (
        46,
        171,
    ): 
        'CONTENT_TYPE_MISMATCH'
    ,
    (
        46,
        172,
    ): 
        'MSGSIGDIGEST_ERROR'
    ,
    (
        46,
        173,
    ): 
        'NO_CONTENT_TYPE'
    ,
    (
        46,
        174,
    ): 
        'NO_KEY_OR_CERT'
    ,
    (
        46,
        175,
    ): 
        'CERTIFICATE_ALREADY_PRESENT'
    ,
    (
        46,
        176,
    ): 
        'INVALID_KEY_ENCRYPTION_PARAMETER'
    ,
    (
        46,
        177,
    ): 
        'NOT_PWRI'
    ,
    (
        46,
        178,
    ): 
        'NO_PASSWORD'
    ,
    (
        46,
        179,
    ): 
        'UNSUPPORTED_KEY_ENCRYPTION_ALGORITHM'
    ,
    (
        46,
        180,
    ): 
        'UNWRAP_FAILURE'
    ,
    (
        46,
        181,
    ): 
        'NOT_KEY_AGREEMENT'
    ,
    (
        46,
        183,
    ): 
        'ESS_SIGNING_CERTID_MISMATCH_ERROR'
    ,
    (
        46,
        184,
    ): 
        'CIPHER_AEAD_SET_TAG_ERROR'
    ,
    (
        46,
        185,
    ): 
        'CIPHER_GET_TAG'
    ,
    (
        46,
        186,
    ): 
        'KDF_PARAMETER_ERROR'
    ,
    (
        46,
        187,
    ): 
        'DECODE_ERROR'
    ,
    (
        46,
        188,
    ): 
        'PEER_KEY_ERROR'
    ,
    (
        46,
        189,
    ): 
        'SHARED_INFO_ERROR'
    ,
    (
        46,
        190,
    ): 
        'INVALID_LABEL'
    ,
    (
        46,
        191,
    ): 
        'INVALID_OAEP_PARAMETERS'
    ,
    (
        46,
        192,
    ): 
        'UNSUPPORTED_ENCRYPTION_TYPE'
    ,
    (
        46,
        193,
    ): 
        'UNSUPPORTED_LABEL_SOURCE'
    ,
    (
        46,
        194,
    ): 
        'UNSUPPORTED_CONTENT_ENCRYPTION_ALGORITHM'
    ,
    (
        47,
        100,
    ): 
        'CERTIFICATE_VERIFY_ERROR'
    ,
    (
        47,
        101,
    ): 
        'ESS_SIGNING_CERTIFICATE_ERROR'
    ,
    (
        47,
        102,
    ): 
        'INVALID_NULL_POINTER'
    ,
    (
        47,
        103,
    ): 
        'MESSAGE_IMPRINT_MISMATCH'
    ,
    (
        47,
        104,
    ): 
        'NONCE_MISMATCH'
    ,
    (
        47,
        105,
    ): 
        'NONCE_NOT_RETURNED'
    ,
    (
        47,
        106,
    ): 
        'NO_CONTENT'
    ,
    (
        47,
        107,
    ): 
        'NO_TIME_STAMP_TOKEN'
    ,
    (
        47,
        108,
    ): 
        'POLICY_MISMATCH'
    ,
    (
        47,
        109,
    ): 
        'SIGNATURE_FAILURE'
    ,
    (
        47,
        110,
    ): 
        'THERE_MUST_BE_ONE_SIGNER'
    ,
    (
        47,
        111,
    ): 
        'TSA_NAME_MISMATCH'
    ,
    (
        47,
        112,
    ): 
        'TSA_UNTRUSTED'
    ,
    (
        47,
        113,
    ): 
        'UNSUPPORTED_VERSION'
    ,
    (
        47,
        114,
    ): 
        'WRONG_CONTENT_TYPE'
    ,
    (
        47,
        115,
    ): 
        'COULD_NOT_SET_TIME'
    ,
    (
        47,
        116,
    ): 
        'ESS_ADD_SIGNING_CERT_ERROR'
    ,
    (
        47,
        117,
    ): 
        'INVALID_SIGNER_CERTIFICATE_PURPOSE'
    ,
    (
        47,
        118,
    ): 
        'PKCS7_ADD_SIGNATURE_ERROR'
    ,
    (
        47,
        119,
    ): 
        'PKCS7_ADD_SIGNED_ATTR_ERROR'
    ,
    (
        47,
        120,
    ): 
        'PRIVATE_KEY_DOES_NOT_MATCH_CERTIFICATE'
    ,
    (
        47,
        121,
    ): 
        'RESPONSE_SETUP_ERROR'
    ,
    (
        47,
        122,
    ): 
        'TIME_SYSCALL_ERROR'
    ,
    (
        47,
        123,
    ): 
        'TST_INFO_SETUP_ERROR'
    ,
    (
        47,
        124,
    ): 
        'TS_DATASIGN'
    ,
    (
        47,
        125,
    ): 
        'UNACCEPTABLE_POLICY'
    ,
    (
        47,
        126,
    ): 
        'UNSUPPORTED_MD_ALGORITHM'
    ,
    (
        47,
        127,
    ): 
        'COULD_NOT_SET_ENGINE'
    ,
    (
        47,
        129,
    ): 
        'PKCS7_TO_TS_TST_INFO_FAILED'
    ,
    (
        47,
        130,
    ): 
        'TOKEN_NOT_PRESENT'
    ,
    (
        47,
        131,
    ): 
        'TOKEN_PRESENT'
    ,
    (
        47,
        132,
    ): 
        'BAD_PKCS7_TYPE'
    ,
    (
        47,
        133,
    ): 
        'BAD_TYPE'
    ,
    (
        47,
        134,
    ): 
        'DETACHED_CONTENT'
    ,
    (
        47,
        135,
    ): 
        'VAR_BAD_VALUE'
    ,
    (
        47,
        136,
    ): 
        'VAR_LOOKUP_FAILURE'
    ,
    (
        47,
        137,
    ): 
        'CANNOT_LOAD_CERT'
    ,
    (
        47,
        138,
    ): 
        'CANNOT_LOAD_KEY'
    ,
    (
        47,
        139,
    ): 
        'ESS_ADD_SIGNING_CERT_V2_ERROR'
    ,
    (
        50,
        100,
    ): 
        'INVALID_LOG_ID_LENGTH'
    ,
    (
        50,
        101,
    ): 
        'UNRECOGNIZED_SIGNATURE_NID'
    ,
    (
        50,
        102,
    ): 
        'UNSUPPORTED_ENTRY_TYPE'
    ,
    (
        50,
        103,
    ): 
        'UNSUPPORTED_VERSION'
    ,
    (
        50,
        104,
    ): 
        'SCT_INVALID'
    ,
    (
        50,
        105,
    ): 
        'SCT_LIST_INVALID'
    ,
    (
        50,
        106,
    ): 
        'SCT_NOT_SET'
    ,
    (
        50,
        107,
    ): 
        'SCT_INVALID_SIGNATURE'
    ,
    (
        50,
        108,
    ): 
        'BASE64_DECODE_ERROR'
    ,
    (
        50,
        109,
    ): 
        'LOG_CONF_INVALID'
    ,
    (
        50,
        110,
    ): 
        'LOG_CONF_INVALID_KEY'
    ,
    (
        50,
        111,
    ): 
        'LOG_CONF_MISSING_DESCRIPTION'
    ,
    (
        50,
        112,
    ): 
        'LOG_CONF_MISSING_KEY'
    ,
    (
        50,
        113,
    ): 
        'LOG_KEY_INVALID'
    ,
    (
        50,
        114,
    ): 
        'SCT_LOG_ID_MISMATCH'
    ,
    (
        50,
        115,
    ): 
        'SCT_UNSUPPORTED_VERSION'
    ,
    (
        50,
        116,
    ): 
        'SCT_FUTURE_TIMESTAMP'
    ,
    (
        51,
        101,
    ): 
        'FAILED_TO_SET_POOL'
    ,
    (
        51,
        102,
    ): 
        'FAILED_TO_SWAP_CONTEXT'
    ,
    (
        51,
        103,
    ): 
        'INVALID_POOL_SIZE'
    ,
    (
        51,
        105,
    ): 
        'INIT_FAILED'
    ,
    (
        53,
        100,
    ): 
        'ASN1_ERROR'
    ,
    (
        53,
        101,
    ): 
        'BAD_SIGNATURE'
    ,
    (
        53,
        102,
    ): 
        'INVALID_DIGEST'
    ,
    (
        53,
        103,
    ): 
        'INVALID_DIGEST_TYPE'
    ,
    (
        53,
        104,
    ): 
        'INVALID_ENCODING'
    ,
    (
        53,
        105,
    ): 
        'INVALID_FIELD'
    ,
    (
        53,
        106,
    ): 
        'USER_ID_TOO_LARGE'
    ,
    (
        53,
        107,
    ): 
        'BUFFER_TOO_SMALL'
    ,
    (
        53,
        108,
    ): 
        'INVALID_CURVE'
    ,
    (
        53,
        109,
    ): 
        'NO_PARAMETERS_SET'
    ,
    (
        53,
        110,
    ): 
        'DIST_ID_TOO_LARGE'
    ,
    (
        53,
        111,
    ): 
        'ID_TOO_LARGE'
    ,
    (
        53,
        112,
    ): 
        'ID_NOT_SET'
    ,
    (
        53,
        113,
    ): 
        'INVALID_PRIVATE_KEY'
    ,
    (
        54,
        100,
    ): 
        'ESS_SIGNING_CERT_ADD_ERROR'
    ,
    (
        54,
        101,
    ): 
        'ESS_SIGNING_CERT_V2_ADD_ERROR'
    ,
    (
        54,
        102,
    ): 
        'ESS_SIGNING_CERTIFICATE_ERROR'
    ,
    (
        54,
        103,
    ): 
        'ESS_CERT_DIGEST_ERROR'
    ,
    (
        54,
        104,
    ): 
        'ESS_CERT_ID_NOT_FOUND'
    ,
    (
        54,
        105,
    ): 
        'ESS_CERT_ID_WRONG_ORDER'
    ,
    (
        54,
        106,
    ): 
        'ESS_DIGEST_ALG_UNKNOWN'
    ,
    (
        54,
        107,
    ): 
        'EMPTY_ESS_CERT_ID_LIST'
    ,
    (
        54,
        108,
    ): 
        'MISSING_SIGNING_CERTIFICATE_ATTRIBUTE'
    ,
    (
        55,
        100,
    ): 
        'NAME_TOO_LONG'
    ,
    (
        55,
        101,
    ): 
        'NOT_AN_ASCII_CHARACTER'
    ,
    (
        55,
        102,
    ): 
        'NOT_AN_HEXADECIMAL_DIGIT'
    ,
    (
        55,
        103,
    ): 
        'NOT_AN_IDENTIFIER'
    ,
    (
        55,
        104,
    ): 
        'NOT_AN_OCTAL_DIGIT'
    ,
    (
        55,
        105,
    ): 
        'NOT_A_DECIMAL_DIGIT'
    ,
    (
        55,
        106,
    ): 
        'NO_MATCHING_STRING_DELIMITER'
    ,
    (
        55,
        107,
    ): 
        'NO_VALUE'
    ,
    (
        55,
        108,
    ): 
        'PARSE_FAILED'
    ,
    (
        55,
        109,
    ): 
        'STRING_TOO_LONG'
    ,
    (
        55,
        110,
    ): 
        'TRAILING_CHARACTERS'
    ,
    (
        56,
        100,
    ): 
        'BAD_PBM_ITERATIONCOUNT'
    ,
    (
        56,
        101,
    ): 
        'MALFORMED_IV'
    ,
    (
        56,
        102,
    ): 
        'CRMFERROR'
    ,
    (
        56,
        103,
    ): 
        'ERROR'
    ,
    (
        56,
        104,
    ): 
        'ERROR_DECODING_CERTIFICATE'
    ,
    (
        56,
        105,
    ): 
        'ERROR_DECRYPTING_CERTIFICATE'
    ,
    (
        56,
        106,
    ): 
        'ERROR_DECRYPTING_SYMMETRIC_KEY'
    ,
    (
        56,
        107,
    ): 
        'FAILURE_OBTAINING_RANDOM'
    ,
    (
        56,
        108,
    ): 
        'ITERATIONCOUNT_BELOW_100'
    ,
    (
        56,
        109,
    ): 
        'NULL_ARGUMENT'
    ,
    (
        56,
        110,
    ): 
        'SETTING_MAC_ALGOR_FAILURE'
    ,
    (
        56,
        111,
    ): 
        'SETTING_OWF_ALGOR_FAILURE'
    ,
    (
        56,
        112,
    ): 
        'UNSUPPORTED_ALGORITHM'
    ,
    (
        56,
        113,
    ): 
        'POPOSKINPUT_NOT_SUPPORTED'
    ,
    (
        56,
        114,
    ): 
        'UNSUPPORTED_CIPHER'
    ,
    (
        56,
        115,
    ): 
        'UNSUPPORTED_METHOD_FOR_CREATING_POPO'
    ,
    (
        56,
        116,
    ): 
        'UNSUPPORTED_POPO_METHOD'
    ,
    (
        56,
        117,
    ): 
        'POPO_INCONSISTENT_PUBLIC_KEY'
    ,
    (
        56,
        118,
    ): 
        'POPO_MISSING_PUBLIC_KEY'
    ,
    (
        56,
        119,
    ): 
        'POPO_MISSING_SUBJECT'
    ,
    (
        56,
        120,
    ): 
        'POPO_RAVERIFIED_NOT_ACCEPTED'
    ,
    (
        56,
        121,
    ): 
        'POPO_MISSING'
    ,
    (
        57,
        100,
    ): 
        'BAD_DECRYPT'
    ,
    (
        57,
        101,
    ): 
        'KEY_SETUP_FAILED'
    ,
    (
        57,
        102,
    ): 
        'CIPHER_OPERATION_FAILED'
    ,
    (
        57,
        103,
    ): 
        'FAILED_TO_GET_PARAMETER'
    ,
    (
        57,
        104,
    ): 
        'FAILED_TO_SET_PARAMETER'
    ,
    (
        57,
        105,
    ): 
        'INVALID_KEY_LENGTH'
    ,
    (
        57,
        106,
    ): 
        'OUTPUT_BUFFER_TOO_SMALL'
    ,
    (
        57,
        107,
    ): 
        'WRONG_FINAL_BLOCK_LENGTH'
    ,
    (
        57,
        108,
    ): 
        'INVALID_AAD'
    ,
    (
        57,
        109,
    ): 
        'INVALID_IV_LENGTH'
    ,
    (
        57,
        110,
    ): 
        'INVALID_TAG'
    ,
    (
        57,
        111,
    ): 
        'INVALID_CUSTOM_LENGTH'
    ,
    (
        57,
        112,
    ): 
        'INVALID_SALT_LENGTH'
    ,
    (
        57,
        113,
    ): 
        'NOT_XOF_OR_INVALID_LENGTH'
    ,
    (
        57,
        114,
    ): 
        'NO_KEY_SET'
    ,
    (
        57,
        115,
    ): 
        'INVALID_DATA'
    ,
    (
        57,
        118,
    ): 
        'INVALID_TAG_LENGTH'
    ,
    (
        57,
        119,
    ): 
        'TAG_NOT_SET'
    ,
    (
        57,
        120,
    ): 
        'TAG_NOT_NEEDED'
    ,
    (
        57,
        121,
    ): 
        'FAILED_TO_GENERATE_KEY'
    ,
    (
        57,
        122,
    ): 
        'INVALID_DIGEST'
    ,
    (
        57,
        123,
    ): 
        'INVALID_ITERATION_COUNT'
    ,
    (
        57,
        125,
    ): 
        'INVALID_MODE'
    ,
    (
        57,
        126,
    ): 
        'TOO_MANY_RECORDS'
    ,
    (
        57,
        128,
    ): 
        'MISSING_KEY'
    ,
    (
        57,
        129,
    ): 
        'MISSING_MESSAGE_DIGEST'
    ,
    (
        57,
        130,
    ): 
        'MISSING_PASS'
    ,
    (
        57,
        131,
    ): 
        'MISSING_SALT'
    ,
    (
        57,
        132,
    ): 
        'MISSING_SECRET'
    ,
    (
        57,
        133,
    ): 
        'MISSING_SESSION_ID'
    ,
    (
        57,
        134,
    ): 
        'MISSING_TYPE'
    ,
    (
        57,
        135,
    ): 
        'MISSING_XCGHASH'
    ,
    (
        57,
        136,
    ): 
        'NOT_SUPPORTED'
    ,
    (
        57,
        137,
    ): 
        'UNSUPPORTED_MAC_TYPE'
    ,
    (
        57,
        138,
    ): 
        'VALUE_ERROR'
    ,
    (
        57,
        139,
    ): 
        'WRONG_OUTPUT_BUFFER_SIZE'
    ,
    (
        57,
        140,
    ): 
        'MISSING_SEED'
    ,
    (
        57,
        141,
    ): 
        'BAD_ENCODING'
    ,
    (
        57,
        142,
    ): 
        'BAD_LENGTH'
    ,
    (
        57,
        144,
    ): 
        'MISSING_CEK_ALG'
    ,
    (
        57,
        145,
    ): 
        'UNSUPPORTED_CEK_ALG'
    ,
    (
        57,
        147,
    ): 
        'UNABLE_TO_LOAD_SHA256'
    ,
    (
        57,
        148,
    ): 
        'XTS_DATA_UNIT_IS_TOO_LARGE'
    ,
    (
        57,
        149,
    ): 
        'XTS_DUPLICATED_KEYS'
    ,
    (
        57,
        150,
    ): 
        'MISSING_MAC'
    ,
    (
        57,
        151,
    ): 
        'INVALID_MAC'
    ,
    (
        57,
        152,
    ): 
        'UNSUPPORTED_NUMBER_OF_ROUNDS'
    ,
    (
        57,
        153,
    ): 
        'UNSUPPORTED_KEY_SIZE'
    ,
    (
        57,
        154,
    ): 
        'INVALID_SEED_LENGTH'
    ,
    (
        57,
        155,
    ): 
        'MISSING_CIPHER'
    ,
    (
        57,
        156,
    ): 
        'MISSING_CONSTANT'
    ,
    (
        57,
        157,
    ): 
        'INVALID_CONSTANT_LENGTH'
    ,
    (
        57,
        158,
    ): 
        'INVALID_KEY'
    ,
    (
        57,
        159,
    ): 
        'UNABLE_TO_GET_PASSPHRASE'
    ,
    (
        57,
        160,
    ): 
        'BN_ERROR'
    ,
    (
        57,
        161,
    ): 
        'BAD_TLS_CLIENT_VERSION'
    ,
    (
        57,
        162,
    ): 
        'FAILED_TO_DECRYPT'
    ,
    (
        57,
        164,
    ): 
        'FAILED_DURING_DERIVATION'
    ,
    (
        57,
        165,
    ): 
        'ILLEGAL_OR_UNSUPPORTED_PADDING_MODE'
    ,
    (
        57,
        166,
    ): 
        'INVALID_DIGEST_LENGTH'
    ,
    (
        57,
        167,
    ): 
        'INVALID_MGF1_MD'
    ,
    (
        57,
        168,
    ): 
        'INVALID_PADDING_MODE'
    ,
    (
        57,
        170,
    ): 
        'INVALID_X931_DIGEST'
    ,
    (
        57,
        171,
    ): 
        'KEY_SIZE_TOO_SMALL'
    ,
    (
        57,
        172,
    ): 
        'PSS_SALTLEN_TOO_SMALL'
    ,
    (
        57,
        173,
    ): 
        'ALGORITHM_MISMATCH'
    ,
    (
        57,
        174,
    ): 
        'DIGEST_NOT_ALLOWED'
    ,
    (
        57,
        175,
    ): 
        'FAILED_TO_SIGN'
    ,
    (
        57,
        176,
    ): 
        'INVALID_CURVE'
    ,
    (
        57,
        177,
    ): 
        'NO_PARAMETERS_SET'
    ,
    (
        57,
        178,
    ): 
        'OPERATION_NOT_SUPPORTED_FOR_THIS_KEYTYPE'
    ,
    (
        57,
        179,
    ): 
        'INVALID_SIGNATURE_SIZE'
    ,
    (
        57,
        180,
    ): 
        'FAILED_TO_CREATE_LOCK'
    ,
    (
        57,
        181,
    ): 
        'INSUFFICIENT_DRBG_STRENGTH'
    ,
    (
        57,
        182,
    ): 
        'PARENT_LOCKING_NOT_ENABLED'
    ,
    (
        57,
        183,
    ): 
        'XOF_DIGESTS_NOT_ALLOWED'
    ,
    (
        57,
        184,
    ): 
        'ADDITIONAL_INPUT_TOO_LONG'
    ,
    (
        57,
        185,
    ): 
        'ALREADY_INSTANTIATED'
    ,
    (
        57,
        186,
    ): 
        'ENTROPY_SOURCE_STRENGTH_TOO_WEAK'
    ,
    (
        57,
        187,
    ): 
        'PARENT_CANNOT_SUPPLY_ENTROPY_SEED'
    ,
    (
        57,
        188,
    ): 
        'ERROR_INSTANTIATING_DRBG'
    ,
    (
        57,
        189,
    ): 
        'ERROR_RETRIEVING_ENTROPY'
    ,
    (
        57,
        190,
    ): 
        'ERROR_RETRIEVING_NONCE'
    ,
    (
        57,
        191,
    ): 
        'GENERATE_ERROR'
    ,
    (
        57,
        192,
    ): 
        'IN_ERROR_STATE'
    ,
    (
        57,
        193,
    ): 
        'NOT_INSTANTIATED'
    ,
    (
        57,
        194,
    ): 
        'PARENT_STRENGTH_TOO_WEAK'
    ,
    (
        57,
        195,
    ): 
        'PERSONALISATION_STRING_TOO_LONG'
    ,
    (
        57,
        196,
    ): 
        'REQUEST_TOO_LARGE_FOR_DRBG'
    ,
    (
        57,
        197,
    ): 
        'RESEED_ERROR'
    ,
    (
        57,
        198,
    ): 
        'INVALID_PUBINFO'
    ,
    (
        57,
        199,
    ): 
        'UNABLE_TO_GET_PARENT_STRENGTH'
    ,
    (
        57,
        200,
    ): 
        'INVALID_UKM_LENGTH'
    ,
    (
        57,
        201,
    ): 
        'UNABLE_TO_LOCK_PARENT'
    ,
    (
        57,
        202,
    ): 
        'LENGTH_TOO_LARGE'
    ,
    (
        57,
        203,
    ): 
        'MISMATCHING_DOMAIN_PARAMETERS'
    ,
    (
        57,
        204,
    ): 
        'UNABLE_TO_RESEED'
    ,
    (
        57,
        205,
    ): 
        'DERIVATION_FUNCTION_INIT_FAILED'
    ,
    (
        57,
        206,
    ): 
        'REQUIRE_CTR_MODE_CIPHER'
    ,
    (
        57,
        207,
    ): 
        'UNABLE_TO_FIND_CIPHERS'
    ,
    (
        57,
        208,
    ): 
        'UNABLE_TO_INITIALISE_CIPHERS'
    ,
    (
        57,
        209,
    ): 
        'MISSING_OID'
    ,
    (
        57,
        210,
    ): 
        'INDICATOR_INTEGRITY_FAILURE'
    ,
    (
        57,
        211,
    ): 
        'INVALID_CONFIG_DATA'
    ,
    (
        57,
        212,
    ): 
        'INVALID_STATE'
    ,
    (
        57,
        213,
    ): 
        'MISSING_CONFIG_DATA'
    ,
    (
        57,
        214,
    ): 
        'MODULE_INTEGRITY_FAILURE'
    ,
    (
        57,
        215,
    ): 
        'SELF_TEST_KAT_FAILURE'
    ,
    (
        57,
        216,
    ): 
        'SELF_TEST_POST_FAILURE'
    ,
    (
        57,
        217,
    ): 
        'INVALID_OUTPUT_LENGTH'
    ,
    (
        57,
        218,
    ): 
        'INVALID_DIGEST_SIZE'
    ,
    (
        57,
        219,
    ): 
        'PATH_MUST_BE_ABSOLUTE'
    ,
    (
        57,
        220,
    ): 
        'NOT_A_PUBLIC_KEY'
    ,
    (
        57,
        221,
    ): 
        'NOT_A_PRIVATE_KEY'
    ,
    (
        57,
        222,
    ): 
        'SEARCH_ONLY_SUPPORTED_FOR_DIRECTORIES'
    ,
    (
        57,
        223,
    ): 
        'URI_AUTHORITY_UNSUPPORTED'
    ,
    (
        57,
        224,
    ): 
        'FIPS_MODULE_ENTERING_ERROR_STATE'
    ,
    (
        57,
        225,
    ): 
        'FIPS_MODULE_IN_ERROR_STATE'
    ,
    (
        57,
        226,
    ): 
        'NOT_PARAMETERS'
    ,
    (
        57,
        227,
    ): 
        'FIPS_MODULE_CONDITIONAL_ERROR'
    ,
    (
        57,
        228,
    ): 
        'PARENT_CANNOT_GENERATE_RANDOM_NUMBERS'
    ,
    (
        57,
        229,
    ): 
        'SEED_SOURCES_MUST_NOT_HAVE_A_PARENT'
    ,
    (
        57,
        230,
    ): 
        'INVALID_INPUT_LENGTH'
    ,
    (
        58,
        100,
    ): 
        'INVALID_ARGS'
    ,
    (
        58,
        102,
    ): 
        'MULTIPLE_SAN_SOURCES'
    ,
    (
        58,
        103,
    ): 
        'NULL_ARGUMENT'
    ,
    (
        58,
        107,
    ): 
        'ERROR_PARSING_PKISTATUS'
    ,
    (
        58,
        108,
    ): 
        'BAD_REQUEST_ID'
    ,
    (
        58,
        109,
    ): 
        'CERTID_NOT_FOUND'
    ,
    (
        58,
        110,
    ): 
        'FAILURE_OBTAINING_RANDOM'
    ,
    (
        58,
        111,
    ): 
        'MISSING_SENDER_IDENTIFICATION'
    ,
    (
        58,
        112,
    ): 
        'CERTIFICATE_NOT_FOUND'
    ,
    (
        58,
        113,
    ): 
        'CERTRESPONSE_NOT_FOUND'
    ,
    (
        58,
        114,
    ): 
        'CERT_AND_KEY_DO_NOT_MATCH'
    ,
    (
        58,
        115,
    ): 
        'ERROR_CALCULATING_PROTECTION'
    ,
    (
        58,
        116,
    ): 
        'ERROR_CREATING_CERTCONF'
    ,
    (
        58,
        117,
    ): 
        'ERROR_CREATING_CERTREP'
    ,
    (
        58,
        118,
    ): 
        'ERROR_CREATING_ERROR'
    ,
    (
        58,
        119,
    ): 
        'ERROR_CREATING_GENM'
    ,
    (
        58,
        120,
    ): 
        'ERROR_CREATING_GENP'
    ,
    (
        58,
        121,
    ): 
        'MISSING_P10CSR'
    ,
    (
        58,
        122,
    ): 
        'ERROR_CREATING_PKICONF'
    ,
    (
        58,
        123,
    ): 
        'ERROR_CREATING_POLLREP'
    ,
    (
        58,
        124,
    ): 
        'ERROR_CREATING_POLLREQ'
    ,
    (
        58,
        125,
    ): 
        'ERROR_CREATING_RP'
    ,
    (
        58,
        126,
    ): 
        'ERROR_CREATING_RR'
    ,
    (
        58,
        127,
    ): 
        'ERROR_PROTECTING_MESSAGE'
    ,
    (
        58,
        128,
    ): 
        'ERROR_SETTING_CERTHASH'
    ,
    (
        58,
        129,
    ): 
        'FAIL_INFO_OUT_OF_RANGE'
    ,
    (
        58,
        130,
    ): 
        'MISSING_KEY_INPUT_FOR_CREATING_PROTECTION'
    ,
    (
        58,
        131,
    ): 
        'MISSING_PRIVATE_KEY'
    ,
    (
        58,
        132,
    ): 
        'PKISTATUSINFO_NOT_FOUND'
    ,
    (
        58,
        133,
    ): 
        'UNEXPECTED_PKIBODY'
    ,
    (
        58,
        134,
    ): 
        'UNKNOWN_ALGORITHM_ID'
    ,
    (
        58,
        135,
    ): 
        'UNKNOWN_CERT_TYPE'
    ,
    (
        58,
        136,
    ): 
        'UNSUPPORTED_ALGORITHM'
    ,
    (
        58,
        137,
    ): 
        'UNSUPPORTED_KEY_TYPE'
    ,
    (
        58,
        138,
    ): 
        'WRONG_ALGORITHM_OID'
    ,
    (
        58,
        139,
    ): 
        'ALGORITHM_NOT_SUPPORTED'
    ,
    (
        58,
        140,
    ): 
        'ERROR_VALIDATING_PROTECTION'
    ,
    (
        58,
        141,
    ): 
        'FAILED_EXTRACTING_PUBKEY'
    ,
    (
        58,
        142,
    ): 
        'MISSING_KEY_USAGE_DIGITALSIGNATURE'
    ,
    (
        58,
        143,
    ): 
        'MISSING_PROTECTION'
    ,
    (
        58,
        144,
    ): 
        'MISSING_TRUST_STORE'
    ,
    (
        58,
        145,
    ): 
        'NO_SUITABLE_SENDER_CERT'
    ,
    (
        58,
        146,
    ): 
        'PKIBODY_ERROR'
    ,
    (
        58,
        147,
    ): 
        'POTENTIALLY_INVALID_CERTIFICATE'
    ,
    (
        58,
        148,
    ): 
        'RECIPNONCE_UNMATCHED'
    ,
    (
        58,
        149,
    ): 
        'REQUEST_NOT_ACCEPTED'
    ,
    (
        58,
        150,
    ): 
        'SENDER_GENERALNAME_TYPE_NOT_SUPPORTED'
    ,
    (
        58,
        151,
    ): 
        'SRVCERT_DOES_NOT_VALIDATE_MSG'
    ,
    (
        58,
        152,
    ): 
        'TRANSACTIONID_UNMATCHED'
    ,
    (
        58,
        153,
    ): 
        'UNEXPECTED_PVNO'
    ,
    (
        58,
        154,
    ): 
        'UNSUPPORTED_PROTECTION_ALG_DHBASEDMAC'
    ,
    (
        58,
        155,
    ): 
        'WRONG_PBM_VALUE'
    ,
    (
        58,
        156,
    ): 
        'CERTHASH_UNMATCHED'
    ,
    (
        58,
        157,
    ): 
        'CERTREQMSG_NOT_FOUND'
    ,
    (
        58,
        158,
    ): 
        'ERROR_PROCESSING_MESSAGE'
    ,
    (
        58,
        159,
    ): 
        'TRANSFER_ERROR'
    ,
    (
        58,
        160,
    ): 
        'ERROR_UNEXPECTED_CERTCONF'
    ,
    (
        58,
        161,
    ): 
        'MULTIPLE_REQUESTS_NOT_SUPPORTED'
    ,
    (
        58,
        162,
    ): 
        'ENCOUNTERED_WAITING'
    ,
    (
        58,
        163,
    ): 
        'ERROR_CREATING_CERTREQ'
    ,
    (
        58,
        164,
    ): 
        'FAILED_BUILDING_OWN_CHAIN'
    ,
    (
        58,
        165,
    ): 
        'MISSING_CERTID'
    ,
    (
        58,
        166,
    ): 
        'MISSING_PBM_SECRET'
    ,
    (
        58,
        167,
    ): 
        'BAD_CHECKAFTER_IN_POLLREP'
    ,
    (
        58,
        168,
    ): 
        'MISSING_REFERENCE_CERT'
    ,
    (
        58,
        169,
    ): 
        'CERTIFICATE_NOT_ACCEPTED'
    ,
    (
        58,
        170,
    ): 
        'MULTIPLE_RESPONSES_NOT_SUPPORTED'
    ,
    (
        58,
        171,
    ): 
        'ERROR_VALIDATING_SIGNATURE'
    ,
    (
        58,
        172,
    ): 
        'POLLING_FAILED'
    ,
    (
        58,
        173,
    ): 
        'WRONG_SERIAL_IN_RP'
    ,
    (
        58,
        174,
    ): 
        'INVALID_OPTION'
    ,
    (
        58,
        175,
    ): 
        'VALUE_TOO_LARGE'
    ,
    (
        58,
        176,
    ): 
        'ENCOUNTERED_KEYUPDATEWARNING'
    ,
    (
        58,
        177,
    ): 
        'VALUE_TOO_SMALL'
    ,
    (
        58,
        178,
    ): 
        'MISSING_SECRET'
    ,
    (
        58,
        179,
    ): 
        'MISSING_TRUST_ANCHOR'
    ,
    (
        58,
        180,
    ): 
        'RECEIVED_ERROR'
    ,
    (
        58,
        181,
    ): 
        'CHECKAFTER_OUT_OF_RANGE'
    ,
    (
        58,
        182,
    ): 
        'REQUEST_REJECTED_BY_SERVER'
    ,
    (
        58,
        183,
    ): 
        'MISSING_PUBLIC_KEY'
    ,
    (
        58,
        184,
    ): 
        'TOTAL_TIMEOUT'
    ,
    (
        58,
        185,
    ): 
        'UNEXPECTED_PKISTATUS'
    ,
    (
        58,
        186,
    ): 
        'UNKNOWN_PKISTATUS'
    ,
    (
        58,
        187,
    ): 
        'WRONG_CERTID_IN_RP'
    ,
    (
        58,
        188,
    ): 
        'WRONG_RP_COMPONENT_COUNT'
    ,
    (
        58,
        189,
    ): 
        'WRONG_CERTID'
    ,
    (
        58,
        190,
    ): 
        'MISSING_PRIVATE_KEY_FOR_POPO'
    ,
    (
        58,
        194,
    ): 
        'NO_STDIO'
    ,
    (
        59,
        100,
    ): 
        'INCORRECT_PROPERTY_QUERY'
    ,
    (
        59,
        101,
    ): 
        'ENCODER_NOT_FOUND'
    ,
    (
        59,
        102,
    ): 
        'MISSING_GET_PARAMS'
    ,
    (
        60,
        100,
    ): 
        'MISSING_GET_PARAMS'
    ,
    (
        60,
        101,
    ): 
        'COULD_NOT_DECODE_OBJECT'
    ,
    (
        60,
        102,
    ): 
        'DECODER_NOT_FOUND'
    ,
    (
        61,
        100,
    ): 
        'CONNECT_FAILURE'
    ,
    (
        61,
        101,
    ): 
        'ERROR_PARSING_URL'
    ,
    (
        61,
        102,
    ): 
        'ERROR_SENDING'
    ,
    (
        61,
        103,
    ): 
        'ERROR_RECEIVING'
    ,
    (
        61,
        104,
    ): 
        'RESPONSE_PARSE_ERROR'
    ,
    (
        61,
        105,
    ): 
        'RECEIVED_ERROR'
    ,
    (
        61,
        106,
    ): 
        'RECEIVED_WRONG_HTTP_VERSION'
    ,
    (
        61,
        107,
    ): 
        'TLS_NOT_ENABLED'
    ,
    (
        61,
        108,
    ): 
        'ASN1_LEN_EXCEEDS_MAX_RESP_LEN'
    ,
    (
        61,
        109,
    ): 
        'ERROR_PARSING_ASN1_LENGTH'
    ,
    (
        61,
        110,
    ): 
        'MISSING_ASN1_ENCODING'
    ,
    (
        61,
        111,
    ): 
        'MISSING_REDIRECT_LOCATION'
    ,
    (
        61,
        112,
    ): 
        'REDIRECTION_FROM_HTTPS_TO_HTTP'
    ,
    (
        61,
        113,
    ): 
        'RESPONSE_LINE_TOO_LONG'
    ,
    (
        61,
        114,
    ): 
        'STATUS_CODE_UNSUPPORTED'
    ,
    (
        61,
        115,
    ): 
        'TOO_MANY_REDIRECTIONS'
    ,
    (
        61,
        116,
    ): 
        'REDIRECTION_NOT_ENABLED'
    ,
    (
        61,
        117,
    ): 
        'MAX_RESP_LEN_EXCEEDED'
    ,
    (
        61,
        118,
    ): 
        'UNEXPECTED_CONTENT_TYPE'
    ,
    (
        61,
        119,
    ): 
        'ERROR_PARSING_CONTENT_LENGTH'
    ,
    (
        61,
        120,
    ): 
        'INCONSISTENT_CONTENT_LENGTH'
    ,
    (
        61,
        121,
    ): 
        'MISSING_CONTENT_TYPE'
    ,
    (
        61,
        122,
    ): 
        'SOCK_NOT_SUPPORTED'
    ,
    (
        61,
        123,
    ): 
        'INVALID_PORT_NUMBER'
    ,
    (
        61,
        124,
    ): 
        'INVALID_URL_SCHEME'
    ,
    (
        61,
        125,
    ): 
        'INVALID_URL_PATH'
    ,
    (
        61,
        126,
    ): 
        'HEADER_PARSE_ERROR'
    ,
    (
        61,
        127,
    ): 
        'SERVER_CANCELED_CONNECTION'
    ,
    (
        61,
        128,
    ): 
        'FAILED_READING_DATA'
    ,
    (
        61,
        129,
    ): 
        'RETRY_TIMEOUT'
    ,
}

err_names_to_codes = {
    'ACCEPT_ERROR': (
        32,
        100,
    ),
    'ADDING_OBJECT': (
        13,
        171,
    ),
    'ADDITIONAL_INPUT_TOO_LONG': (
        36,
        102,
    ),
    'ADDRINFO_ADDR_IS_NOT_AF_INET': (
        32,
        141,
    ),
    'ADD_SIGNER_ERROR': (
        46,
        99,
    ),
    'AES_KEY_SETUP_FAILED': (
        6,
        143,
    ),
    'AKID_MISMATCH': (
        11,
        110,
    ),
    'ALGORITHM_MISMATCH': (
        4,
        100,
    ),
    'ALGORITHM_NOT_SUPPORTED': (
        58,
        139,
    ),
    'ALREADY_INSTANTIATED': (
        36,
        103,
    ),
    'ALREADY_LOADED': (
        38,
        100,
    ),
    'AMBIGUOUS_CONTENT_TYPE': (
        44,
        107,
    ),
    'AMBIGUOUS_HOST_OR_SERVICE': (
        32,
        129,
    ),
    'APPLICATION_DATA_AFTER_CLOSE_NOTIFY': (
        20,
        291,
    ),
    'APP_DATA_IN_HANDSHAKE': (
        20,
        100,
    ),
    'ARG2_LT_ARG3': (
        3,
        100,
    ),
    'ARGUMENT_IS_NOT_A_NUMBER': (
        38,
        133,
    ),
    'ARGUMENT_OUT_OF_RANGE': (
        36,
        105,
    ),
    'ARIA_KEY_SETUP_FAILED': (
        6,
        176,
    ),
    'ASN1_ERROR': (
        53,
        100,
    ),
    'ASN1_LEN_EXCEEDS_MAX_RESP_LEN': (
        61,
        108,
    ),
    'ASN1_PARSE_ERROR': (
        13,
        203,
    ),
    'ASN1_SIG_PARSE_ERROR': (
        13,
        204,
    ),
    'ATTEMPT_TO_REUSE_SESSION_IN_DIFFERENT_CONTEXT': (
        20,
        272,
    ),
    'ATTRIBUTE_ERROR': (
        46,
        161,
    ),
    'AT_LEAST_TLS_1_0_NEEDED_IN_FIPS_MODE': (
        20,
        143,
    ),
    'AT_LEAST_TLS_1_2_NEEDED_IN_SUITEB_MODE': (
        20,
        158,
    ),
    'AUX_ERROR': (
        13,
        100,
    ),
    'BAD_ALGORITHM_NAME': (
        6,
        200,
    ),
    'BAD_BASE64_DECODE': (
        9,
        100,
    ),
    'BAD_CHANGE_CIPHER_SPEC': (
        20,
        103,
    ),
    'BAD_CHECKAFTER_IN_POLLREP': (
        58,
        167,
    ),
    'BAD_CIPHER': (
        20,
        186,
    ),
    'BAD_DATA': (
        20,
        390,
    ),
    'BAD_DATA_RETURNED_BY_CALLBACK': (
        20,
        106,
    ),
    'BAD_DECOMPRESSION': (
        20,
        107,
    ),
    'BAD_DECRYPT': (
        57,
        100,
    ),
    'BAD_DH_VALUE': (
        20,
        102,
    ),
    'BAD_DIGEST_LENGTH': (
        20,
        111,
    ),
    'BAD_EARLY_DATA': (
        20,
        233,
    ),
    'BAD_ECC_CERT': (
        20,
        304,
    ),
    'BAD_ECPOINT': (
        20,
        306,
    ),
    'BAD_ENCODING': (
        57,
        141,
    ),
    'BAD_END_LINE': (
        9,
        102,
    ),
    'BAD_EXTENSION': (
        20,
        110,
    ),
    'BAD_E_VALUE': (
        4,
        101,
    ),
    'BAD_FFC_PARAMETERS': (
        10,
        114,
    ),
    'BAD_FIXED_HEADER_DECRYPT': (
        4,
        102,
    ),
    'BAD_FOPEN_MODE': (
        32,
        101,
    ),
    'BAD_GENERATOR': (
        5,
        101,
    ),
    'BAD_HANDSHAKE_LENGTH': (
        20,
        332,
    ),
    'BAD_HANDSHAKE_STATE': (
        20,
        236,
    ),
    'BAD_HELLO_REQUEST': (
        20,
        105,
    ),
    'BAD_HRR_VERSION': (
        20,
        263,
    ),
    'BAD_IP_ADDRESS': (
        34,
        118,
    ),
    'BAD_IV_CHARS': (
        9,
        103,
    ),
    'BAD_KEY_LENGTH': (
        6,
        195,
    ),
    'BAD_KEY_SHARE': (
        20,
        108,
    ),
    'BAD_KEY_UPDATE': (
        20,
        122,
    ),
    'BAD_LEGACY_VERSION': (
        20,
        292,
    ),
    'BAD_LENGTH': (
        20,
        271,
    ),
    'BAD_MAGIC_NUMBER': (
        9,
        116,
    ),
    'BAD_OBJECT': (
        34,
        119,
    ),
    'BAD_OBJECT_HEADER': (
        13,
        102,
    ),
    'BAD_PACKET': (
        20,
        240,
    ),
    'BAD_PACKET_LENGTH': (
        20,
        115,
    ),
    'BAD_PAD_BYTE_COUNT': (
        4,
        103,
    ),
    'BAD_PASSWORD_READ': (
        9,
        104,
    ),
    'BAD_PBM_ITERATIONCOUNT': (
        56,
        100,
    ),
    'BAD_PKCS7_TYPE': (
        47,
        132,
    ),
    'BAD_PROTOCOL_VERSION_NUMBER': (
        20,
        116,
    ),
    'BAD_PSK': (
        20,
        219,
    ),
    'BAD_PSK_IDENTITY': (
        20,
        114,
    ),
    'BAD_Q_VALUE': (
        10,
        102,
    ),
    'BAD_RECIPROCAL': (
        3,
        101,
    ),
    'BAD_RECORD_TYPE': (
        20,
        443,
    ),
    'BAD_REQUEST_ID': (
        58,
        108,
    ),
    'BAD_RSA_ENCRYPT': (
        20,
        119,
    ),
    'BAD_SELECTOR': (
        11,
        133,
    ),
    'BAD_SIGNATURE': (
        20,
        123,
    ),
    'BAD_SRP_A_LENGTH': (
        20,
        347,
    ),
    'BAD_SRP_PARAMETERS': (
        20,
        371,
    ),
    'BAD_SRTP_MKI_VALUE': (
        20,
        352,
    ),
    'BAD_SRTP_PROTECTION_PROFILE_LIST': (
        20,
        353,
    ),
    'BAD_SSL_FILETYPE': (
        20,
        124,
    ),
    'BAD_TEMPLATE': (
        13,
        230,
    ),
    'BAD_TLS_CLIENT_VERSION': (
        57,
        161,
    ),
    'BAD_TYPE': (
        47,
        133,
    ),
    'BAD_VALUE': (
        20,
        384,
    ),
    'BAD_VERSION_NUMBER': (
        9,
        117,
    ),
    'BAD_WRITE_RETRY': (
        20,
        127,
    ),
    'BAD_X509_FILETYPE': (
        11,
        100,
    ),
    'BASE64_DECODE_ERROR': (
        11,
        118,
    ),
    'BIGNUM_OUT_OF_RANGE': (
        16,
        144,
    ),
    'BIGNUM_TOO_LONG': (
        3,
        114,
    ),
    'BINDER_DOES_NOT_VERIFY': (
        20,
        253,
    ),
    'BIO_NOT_SET': (
        20,
        128,
    ),
    'BIO_WRITE_FAILURE': (
        9,
        118,
    ),
    'BITS_TOO_SMALL': (
        3,
        118,
    ),
    'BLOCK_CIPHER_PAD_IS_WRONG': (
        20,
        129,
    ),
    'BLOCK_TYPE_IS_NOT_01': (
        4,
        106,
    ),
    'BLOCK_TYPE_IS_NOT_02': (
        4,
        107,
    ),
    'BMPSTRING_IS_WRONG_LENGTH': (
        13,
        214,
    ),
    'BN_DEC2BN_ERROR': (
        34,
        100,
    ),
    'BN_DECODE_ERROR': (
        10,
        108,
    ),
    'BN_ERROR': (
        57,
        160,
    ),
    'BN_LIB': (
        20,
        130,
    ),
    'BN_TO_ASN1_INTEGER_ERROR': (
        34,
        101,
    ),
    'BOOLEAN_IS_WRONG_LENGTH': (
        13,
        106,
    ),
    'BROKEN_PIPE': (
        32,
        124,
    ),
    'BUFFER_TOO_SMALL': (
        53,
        107,
    ),
    'CACHE_CONSTANTS_FAILED': (
        6,
        225,
    ),
    'CALLBACK_FAILED': (
        20,
        234,
    ),
    'CALLED_WITH_EVEN_MODULUS': (
        3,
        102,
    ),
    'CAMELLIA_KEY_SETUP_FAILED': (
        6,
        157,
    ),
    'CANNOT_CHANGE_CIPHER': (
        20,
        109,
    ),
    'CANNOT_GET_GROUP_NAME': (
        20,
        299,
    ),
    'CANNOT_GET_PARAMETERS': (
        6,
        197,
    ),
    'CANNOT_INVERT': (
        16,
        165,
    ),
    'CANNOT_LOAD_CERT': (
        47,
        137,
    ),
    'CANNOT_LOAD_KEY': (
        47,
        138,
    ),
    'CANNOT_OPEN_FILE': (
        36,
        121,
    ),
    'CANNOT_SET_PARAMETERS': (
        6,
        198,
    ),
    'CANT_CHECK_DH_KEY': (
        11,
        114,
    ),
    'CANT_PACK_STRUCTURE': (
        35,
        100,
    ),
    'CA_DN_LENGTH_MISMATCH': (
        20,
        131,
    ),
    'CA_KEY_TOO_SMALL': (
        20,
        397,
    ),
    'CA_MD_TOO_WEAK': (
        20,
        398,
    ),
    'CCS_RECEIVED_EARLY': (
        20,
        133,
    ),
    'CERTHASH_UNMATCHED': (
        58,
        156,
    ),
    'CERTID_NOT_FOUND': (
        58,
        109,
    ),
    'CERTIFICATE_ALREADY_PRESENT': (
        46,
        175,
    ),
    'CERTIFICATE_HAS_NO_KEYID': (
        46,
        160,
    ),
    'CERTIFICATE_NOT_ACCEPTED': (
        58,
        169,
    ),
    'CERTIFICATE_NOT_FOUND': (
        58,
        112,
    ),
    'CERTIFICATE_VERIFICATION_FAILED': (
        11,
        139,
    ),
    'CERTIFICATE_VERIFY_ERROR': (
        47,
        100,
    ),
    'CERTIFICATE_VERIFY_FAILED': (
        20,
        134,
    ),
    'CERTREQMSG_NOT_FOUND': (
        58,
        157,
    ),
    'CERTRESPONSE_NOT_FOUND': (
        58,
        113,
    ),
    'CERT_ALREADY_IN_HASH_TABLE': (
        11,
        101,
    ),
    'CERT_AND_KEY_DO_NOT_MATCH': (
        58,
        114,
    ),
    'CERT_CB_ERROR': (
        20,
        377,
    ),
    'CERT_LENGTH_MISMATCH': (
        20,
        135,
    ),
    'CHECKAFTER_OUT_OF_RANGE': (
        58,
        181,
    ),
    'CHECK_INVALID_J_VALUE': (
        5,
        115,
    ),
    'CHECK_INVALID_Q_VALUE': (
        5,
        116,
    ),
    'CHECK_PUBKEY_INVALID': (
        5,
        122,
    ),
    'CHECK_PUBKEY_TOO_LARGE': (
        5,
        123,
    ),
    'CHECK_PUBKEY_TOO_SMALL': (
        5,
        124,
    ),
    'CHECK_P_NOT_PRIME': (
        5,
        117,
    ),
    'CHECK_P_NOT_SAFE_PRIME': (
        5,
        118,
    ),
    'CHECK_Q_NOT_PRIME': (
        5,
        119,
    ),
    'CIPHERSUITE_DIGEST_HAS_CHANGED': (
        20,
        218,
    ),
    'CIPHER_AEAD_SET_TAG_ERROR': (
        46,
        184,
    ),
    'CIPHER_CODE_WRONG_LENGTH': (
        20,
        137,
    ),
    'CIPHER_GET_TAG': (
        46,
        185,
    ),
    'CIPHER_HAS_NO_OBJECT_IDENTIFIER': (
        33,
        144,
    ),
    'CIPHER_INITIALISATION_ERROR': (
        46,
        101,
    ),
    'CIPHER_IS_NULL': (
        9,
        127,
    ),
    'CIPHER_NOT_GCM_MODE': (
        6,
        184,
    ),
    'CIPHER_NOT_INITIALIZED': (
        33,
        116,
    ),
    'CIPHER_OPERATION_FAILED': (
        57,
        102,
    ),
    'CIPHER_PARAMETER_ERROR': (
        6,
        122,
    ),
    'CIPHER_PARAMETER_INITIALISATION_ERROR': (
        46,
        102,
    ),
    'CLIENTHELLO_TLSEXT': (
        20,
        226,
    ),
    'CMD_NOT_EXECUTABLE': (
        38,
        134,
    ),
    'CMS_DATAFINAL_ERROR': (
        46,
        103,
    ),
    'CMS_LIB': (
        46,
        104,
    ),
    'COMMAND_NOT_SUPPORTED': (
        6,
        147,
    ),
    'COMMAND_TAKES_INPUT': (
        38,
        135,
    ),
    'COMMAND_TAKES_NO_INPUT': (
        38,
        136,
    ),
    'COMMON_OK_AND_CANCEL_CHARACTERS': (
        40,
        104,
    ),
    'COMPRESSED_LENGTH_TOO_LONG': (
        20,
        140,
    ),
    'COMPRESSION_DISABLED': (
        20,
        343,
    ),
    'COMPRESSION_FAILURE': (
        20,
        141,
    ),
    'COMPRESSION_ID_NOT_WITHIN_PRIVATE_RANGE': (
        20,
        307,
    ),
    'COMPRESSION_LIBRARY_ERROR': (
        20,
        142,
    ),
    'CONFLICTING_ALGORITHM_NAME': (
        6,
        201,
    ),
    'CONFLICTING_ENGINE_ID': (
        38,
        103,
    ),
    'CONFLICTING_NAMES': (
        15,
        118,
    ),
    'CONNECTION_TYPE_NOT_SET': (
        20,
        144,
    ),
    'CONNECT_ERROR': (
        32,
        103,
    ),
    'CONNECT_FAILURE': (
        61,
        100,
    ),
    'CONNECT_TIMEOUT': (
        32,
        147,
    ),
    'CONTENTIDENTIFIER_MISMATCH': (
        46,
        170,
    ),
    'CONTENT_AND_DATA_PRESENT': (
        33,
        118,
    ),
    'CONTENT_NOT_FOUND': (
        46,
        105,
    ),
    'CONTENT_TYPE_MISMATCH': (
        46,
        171,
    ),
    'CONTENT_TYPE_NOT_COMPRESSED_DATA': (
        46,
        106,
    ),
    'CONTENT_TYPE_NOT_DATA': (
        35,
        121,
    ),
    'CONTENT_TYPE_NOT_ENVELOPED_DATA': (
        46,
        107,
    ),
    'CONTENT_TYPE_NOT_SIGNED_DATA': (
        46,
        108,
    ),
    'CONTENT_VERIFY_ERROR': (
        46,
        109,
    ),
    'CONTEXT_NOT_DANE_ENABLED': (
        20,
        167,
    ),
    'CONTEXT_NOT_INITIALISED': (
        13,
        217,
    ),
    'COOKIE_GEN_CALLBACK_FAILURE': (
        20,
        400,
    ),
    'COOKIE_MISMATCH': (
        20,
        308,
    ),
    'COORDINATES_OUT_OF_RANGE': (
        16,
        146,
    ),
    'COPY_ERROR': (
        6,
        173,
    ),
    'COPY_PARAMETERS_FAILED': (
        20,
        296,
    ),
    'COULD_NOT_DECODE_OBJECT': (
        60,
        101,
    ),
    'COULD_NOT_SET_ENGINE': (
        47,
        127,
    ),
    'COULD_NOT_SET_TIME': (
        47,
        115,
    ),
    'CRL_ALREADY_DELTA': (
        11,
        127,
    ),
    'CRL_VERIFY_FAILURE': (
        11,
        131,
    ),
    'CRMFERROR': (
        56,
        102,
    ),
    'CTRL_COMMAND_NOT_IMPLEMENTED': (
        38,
        119,
    ),
    'CTRL_ERROR': (
        33,
        152,
    ),
    'CTRL_FAILED': (
        37,
        100,
    ),
    'CTRL_FAILURE': (
        46,
        111,
    ),
    'CTRL_NOT_IMPLEMENTED': (
        6,
        132,
    ),
    'CTRL_OPERATION_NOT_IMPLEMENTED': (
        6,
        133,
    ),
    'CURVE_DOES_NOT_SUPPORT_ECDH': (
        16,
        160,
    ),
    'CURVE_DOES_NOT_SUPPORT_ECDSA': (
        16,
        170,
    ),
    'CURVE_DOES_NOT_SUPPORT_SIGNING': (
        16,
        159,
    ),
    'CUSTOM_EXT_HANDLER_ALREADY_INSTALLED': (
        20,
        206,
    ),
    'DANE_ALREADY_ENABLED': (
        20,
        172,
    ),
    'DANE_CANNOT_OVERRIDE_MTYPE_FULL': (
        20,
        173,
    ),
    'DANE_NOT_ENABLED': (
        20,
        175,
    ),
    'DANE_TLSA_BAD_CERTIFICATE': (
        20,
        180,
    ),
    'DANE_TLSA_BAD_CERTIFICATE_USAGE': (
        20,
        184,
    ),
    'DANE_TLSA_BAD_DATA_LENGTH': (
        20,
        189,
    ),
    'DANE_TLSA_BAD_DIGEST_LENGTH': (
        20,
        192,
    ),
    'DANE_TLSA_BAD_MATCHING_TYPE': (
        20,
        200,
    ),
    'DANE_TLSA_BAD_PUBLIC_KEY': (
        20,
        201,
    ),
    'DANE_TLSA_BAD_SELECTOR': (
        20,
        202,
    ),
    'DANE_TLSA_NULL_DATA': (
        20,
        203,
    ),
    'DATA_BETWEEN_CCS_AND_FINISHED': (
        20,
        145,
    ),
    'DATA_GREATER_THAN_MOD_LEN': (
        4,
        108,
    ),
    'DATA_IS_WRONG': (
        13,
        109,
    ),
    'DATA_LENGTH_TOO_LONG': (
        20,
        146,
    ),
    'DATA_NOT_MULTIPLE_OF_BLOCK_LENGTH': (
        6,
        138,
    ),
    'DATA_TOO_LARGE': (
        4,
        109,
    ),
    'DATA_TOO_LARGE_FOR_KEY_SIZE': (
        4,
        110,
    ),
    'DATA_TOO_LARGE_FOR_MODULUS': (
        4,
        132,
    ),
    'DATA_TOO_SMALL': (
        4,
        111,
    ),
    'DATA_TOO_SMALL_FOR_KEY_SIZE': (
        4,
        122,
    ),
    'DECODER_NOT_FOUND': (
        60,
        102,
    ),
    'DECODE_ERROR': (
        35,
        101,
    ),
    'DECRYPTION_FAILED': (
        20,
        147,
    ),
    'DECRYPTION_FAILED_OR_BAD_RECORD_MAC': (
        20,
        281,
    ),
    'DECRYPT_ERROR': (
        33,
        119,
    ),
    'DEFAULT_QUERY_PARSE_ERROR': (
        6,
        210,
    ),
    'DEPTH_EXCEEDED': (
        13,
        174,
    ),
    'DERIVATION_FUNCTION_INIT_FAILED': (
        57,
        205,
    ),
    'DERIVATION_FUNCTION_MANDATORY_FOR_FIPS': (
        36,
        137,
    ),
    'DETACHED_CONTENT': (
        47,
        134,
    ),
    'DH_KEY_TOO_SMALL': (
        20,
        394,
    ),
    'DH_PUBLIC_VALUE_LENGTH_IS_WRONG': (
        20,
        148,
    ),
    'DIFFERENT_KEY_TYPES': (
        6,
        101,
    ),
    'DIFFERENT_PARAMETERS': (
        6,
        153,
    ),
    'DIGEST_AND_KEY_TYPE_NOT_SUPPORTED': (
        13,
        198,
    ),
    'DIGEST_CHECK_FAILED': (
        20,
        149,
    ),
    'DIGEST_DOES_NOT_MATCH': (
        4,
        158,
    ),
    'DIGEST_ERR': (
        39,
        102,
    ),
    'DIGEST_FAILURE': (
        33,
        101,
    ),
    'DIGEST_NAME_ERR': (
        39,
        106,
    ),
    'DIGEST_NOT_ALLOWED': (
        4,
        145,
    ),
    'DIGEST_SIZE_ERR': (
        39,
        107,
    ),
    'DIGEST_TOO_BIG_FOR_RSA_KEY': (
        4,
        112,
    ),
    'DIRNAME_ERROR': (
        34,
        149,
    ),
    'DISCRIMINANT_IS_ZERO': (
        16,
        118,
    ),
    'DISTPOINT_ALREADY_SET': (
        34,
        160,
    ),
    'DIST_ID_TOO_LARGE': (
        53,
        110,
    ),
    'DIV_BY_ZERO': (
        3,
        103,
    ),
    'DMP1_NOT_CONGRUENT_TO_D': (
        4,
        124,
    ),
    'DMQ1_NOT_CONGRUENT_TO_D': (
        4,
        125,
    ),
    'DRBG_ALREADY_INITIALIZED': (
        36,
        129,
    ),
    'DRBG_NOT_INITIALISED': (
        36,
        104,
    ),
    'DSO_ALREADY_LOADED': (
        37,
        110,
    ),
    'DSO_FAILURE': (
        38,
        104,
    ),
    'DSO_NOT_FOUND': (
        38,
        132,
    ),
    'DTLS_MESSAGE_TOO_BIG': (
        20,
        334,
    ),
    'DUPLICATE_COMPRESSION_ID': (
        20,
        309,
    ),
    'DUPLICATE_ZONE_ID': (
        34,
        133,
    ),
    'D_E_NOT_CONGRUENT_TO_1': (
        4,
        123,
    ),
    'ECC_CERT_NOT_FOR_SIGNING': (
        20,
        318,
    ),
    'ECDH_REQUIRED_FOR_SUITEB_MODE': (
        20,
        374,
    ),
    'EC_GROUP_NEW_BY_NAME_FAILURE': (
        16,
        119,
    ),
    'EE_KEY_TOO_SMALL': (
        20,
        399,
    ),
    'EMPTY_ESS_CERT_ID_LIST': (
        54,
        107,
    ),
    'EMPTY_FILE_STRUCTURE': (
        37,
        113,
    ),
    'EMPTY_KEY_USAGE': (
        34,
        169,
    ),
    'EMPTY_SRTP_PROTECTION_PROFILE_LIST': (
        20,
        354,
    ),
    'ENCODER_NOT_FOUND': (
        59,
        101,
    ),
    'ENCODE_ERROR': (
        35,
        102,
    ),
    'ENCODING_ERROR': (
        3,
        104,
    ),
    'ENCOUNTERED_KEYUPDATEWARNING': (
        58,
        176,
    ),
    'ENCOUNTERED_WAITING': (
        58,
        162,
    ),
    'ENCRYPTED_LENGTH_TOO_LONG': (
        20,
        150,
    ),
    'ENCRYPTION_CTRL_FAILURE': (
        33,
        149,
    ),
    'ENCRYPTION_NOT_SUPPORTED_FOR_THIS_KEY_TYPE': (
        33,
        150,
    ),
    'ENCRYPT_ERROR': (
        35,
        103,
    ),
    'ENGINES_SECTION_ERROR': (
        38,
        148,
    ),
    'ENGINE_CONFIGURATION_ERROR': (
        38,
        102,
    ),
    'ENGINE_IS_NOT_IN_LIST': (
        38,
        105,
    ),
    'ENGINE_SECTION_ERROR': (
        38,
        149,
    ),
    'ENTROPY_INPUT_TOO_LONG': (
        36,
        106,
    ),
    'ENTROPY_OUT_OF_RANGE': (
        36,
        124,
    ),
    'ENTROPY_SOURCE_STRENGTH_TOO_WEAK': (
        57,
        186,
    ),
    'ERROR': (
        56,
        103,
    ),
    'ERROR_ADDING_RECIPIENT': (
        33,
        120,
    ),
    'ERROR_CALCULATING_PROTECTION': (
        58,
        115,
    ),
    'ERROR_CONVERTING_PRIVATE_KEY': (
        9,
        115,
    ),
    'ERROR_CONVERTING_ZONE': (
        34,
        131,
    ),
    'ERROR_CREATING_CERTCONF': (
        58,
        116,
    ),
    'ERROR_CREATING_CERTREP': (
        58,
        117,
    ),
    'ERROR_CREATING_CERTREQ': (
        58,
        163,
    ),
    'ERROR_CREATING_ERROR': (
        58,
        118,
    ),
    'ERROR_CREATING_EXTENSION': (
        34,
        144,
    ),
    'ERROR_CREATING_GENM': (
        58,
        119,
    ),
    'ERROR_CREATING_GENP': (
        58,
        120,
    ),
    'ERROR_CREATING_PKICONF': (
        58,
        122,
    ),
    'ERROR_CREATING_POLLREP': (
        58,
        123,
    ),
    'ERROR_CREATING_POLLREQ': (
        58,
        124,
    ),
    'ERROR_CREATING_RP': (
        58,
        125,
    ),
    'ERROR_CREATING_RR': (
        58,
        126,
    ),
    'ERROR_DECODING_CERTIFICATE': (
        56,
        104,
    ),
    'ERROR_DECRYPTING_CERTIFICATE': (
        56,
        105,
    ),
    'ERROR_DECRYPTING_SYMMETRIC_KEY': (
        56,
        106,
    ),
    'ERROR_ENTROPY_POOL_WAS_IGNORED': (
        36,
        127,
    ),
    'ERROR_GETTING_MD_BY_NID': (
        11,
        141,
    ),
    'ERROR_GETTING_PUBLIC_KEY': (
        46,
        113,
    ),
    'ERROR_GETTING_TIME': (
        13,
        173,
    ),
    'ERROR_INITIALISING_DRBG': (
        36,
        107,
    ),
    'ERROR_INSTANTIATING_DRBG': (
        36,
        108,
    ),
    'ERROR_IN_EXTENSION': (
        34,
        128,
    ),
    'ERROR_IN_NEXTUPDATE_FIELD': (
        39,
        122,
    ),
    'ERROR_IN_RECEIVED_CIPHER_LIST': (
        20,
        151,
    ),
    'ERROR_IN_THISUPDATE_FIELD': (
        39,
        123,
    ),
    'ERROR_LOADING_DSO': (
        14,
        110,
    ),
    'ERROR_LOADING_SECTION': (
        6,
        165,
    ),
    'ERROR_PARSING_ASN1_LENGTH': (
        61,
        109,
    ),
    'ERROR_PARSING_CONTENT_LENGTH': (
        61,
        119,
    ),
    'ERROR_PARSING_PKISTATUS': (
        58,
        107,
    ),
    'ERROR_PARSING_URL': (
        61,
        101,
    ),
    'ERROR_PROCESSING_MESSAGE': (
        58,
        158,
    ),
    'ERROR_PROTECTING_MESSAGE': (
        58,
        127,
    ),
    'ERROR_READING_MESSAGEDIGEST_ATTRIBUTE': (
        46,
        114,
    ),
    'ERROR_RECEIVING': (
        61,
        103,
    ),
    'ERROR_RETRIEVING_ADDITIONAL_INPUT': (
        36,
        109,
    ),
    'ERROR_RETRIEVING_ENTROPY': (
        36,
        110,
    ),
    'ERROR_RETRIEVING_NONCE': (
        36,
        111,
    ),
    'ERROR_SENDING': (
        61,
        102,
    ),
    'ERROR_SETTING_CERTHASH': (
        58,
        128,
    ),
    'ERROR_SETTING_CIPHER': (
        33,
        121,
    ),
    'ERROR_SETTING_CIPHER_PARAMS': (
        13,
        114,
    ),
    'ERROR_SETTING_ENCRYPTED_DATA_TYPE': (
        35,
        120,
    ),
    'ERROR_SETTING_FIPS_MODE': (
        6,
        166,
    ),
    'ERROR_SETTING_KEY': (
        46,
        115,
    ),
    'ERROR_SETTING_RECIPIENTINFO': (
        46,
        116,
    ),
    'ERROR_SETTING_TLSA_BASE_DOMAIN': (
        20,
        204,
    ),
    'ERROR_UNEXPECTED_CERTCONF': (
        58,
        160,
    ),
    'ERROR_USING_SIGINF_SET': (
        11,
        142,
    ),
    'ERROR_VALIDATING_PROTECTION': (
        58,
        140,
    ),
    'ERROR_VALIDATING_SIGNATURE': (
        58,
        171,
    ),
    'ERROR_VERIFYING_PKCS12_MAC': (
        44,
        113,
    ),
    'ESS_ADD_SIGNING_CERT_ERROR': (
        47,
        116,
    ),
    'ESS_ADD_SIGNING_CERT_V2_ERROR': (
        47,
        139,
    ),
    'ESS_CERT_DIGEST_ERROR': (
        54,
        103,
    ),
    'ESS_CERT_ID_NOT_FOUND': (
        54,
        104,
    ),
    'ESS_CERT_ID_WRONG_ORDER': (
        54,
        105,
    ),
    'ESS_DIGEST_ALG_UNKNOWN': (
        54,
        106,
    ),
    'ESS_SIGNING_CERTID_MISMATCH_ERROR': (
        46,
        183,
    ),
    'ESS_SIGNING_CERTIFICATE_ERROR': (
        47,
        101,
    ),
    'ESS_SIGNING_CERT_ADD_ERROR': (
        54,
        100,
    ),
    'ESS_SIGNING_CERT_V2_ADD_ERROR': (
        54,
        101,
    ),
    'EXCEEDS_MAX_FRAGMENT_SIZE': (
        20,
        194,
    ),
    'EXCESSIVE_MESSAGE_SIZE': (
        20,
        152,
    ),
    'EXPAND_ON_STATIC_BIGNUM_DATA': (
        3,
        105,
    ),
    'EXPECTED_A_SECTION_NAME': (
        34,
        137,
    ),
    'EXPECTING_AN_HMAC_KEY': (
        6,
        174,
    ),
    'EXPECTING_AN_INTEGER': (
        13,
        115,
    ),
    'EXPECTING_AN_OBJECT': (
        13,
        116,
    ),
    'EXPECTING_AN_RSA_KEY': (
        6,
        127,
    ),
    'EXPECTING_A_DH_KEY': (
        6,
        128,
    ),
    'EXPECTING_A_DSA_KEY': (
        6,
        129,
    ),
    'EXPECTING_A_ECX_KEY': (
        6,
        219,
    ),
    'EXPECTING_A_EC_KEY': (
        6,
        142,
    ),
    'EXPECTING_A_POLY1305_KEY': (
        6,
        164,
    ),
    'EXPECTING_A_SIPHASH_KEY': (
        6,
        175,
    ),
    'EXPECTING_DSS_KEY_BLOB': (
        9,
        131,
    ),
    'EXPECTING_PRIVATE_KEY_BLOB': (
        9,
        119,
    ),
    'EXPECTING_PUBLIC_KEY_BLOB': (
        9,
        120,
    ),
    'EXPECTING_RSA_KEY_BLOB': (
        9,
        132,
    ),
    'EXPLICIT_LENGTH_MISMATCH': (
        13,
        119,
    ),
    'EXPLICIT_PARAMS_NOT_SUPPORTED': (
        16,
        127,
    ),
    'EXPLICIT_TAG_NOT_CONSTRUCTED': (
        13,
        120,
    ),
    'EXTENSION_EXISTS': (
        34,
        145,
    ),
    'EXTENSION_NAME_ERROR': (
        34,
        115,
    ),
    'EXTENSION_NOT_FOUND': (
        34,
        102,
    ),
    'EXTENSION_NOT_RECEIVED': (
        20,
        279,
    ),
    'EXTENSION_SETTING_NOT_SUPPORTED': (
        34,
        103,
    ),
    'EXTENSION_VALUE_ERROR': (
        34,
        116,
    ),
    'EXTRA_DATA_IN_MESSAGE': (
        20,
        153,
    ),
    'EXT_LENGTH_MISMATCH': (
        20,
        163,
    ),
    'FAILED_BUILDING_OWN_CHAIN': (
        58,
        164,
    ),
    'FAILED_DURING_DERIVATION': (
        57,
        164,
    ),
    'FAILED_EXTRACTING_PUBKEY': (
        58,
        141,
    ),
    'FAILED_LOADING_PRIVATE_KEY': (
        38,
        128,
    ),
    'FAILED_LOADING_PUBLIC_KEY': (
        38,
        129,
    ),
    'FAILED_MAKING_PUBLIC_KEY': (
        16,
        166,
    ),
    'FAILED_READING_DATA': (
        61,
        128,
    ),
    'FAILED_TO_CREATE_LOCK': (
        36,
        126,
    ),
    'FAILED_TO_DECRYPT': (
        57,
        162,
    ),
    'FAILED_TO_GENERATE_KEY': (
        57,
        121,
    ),
    'FAILED_TO_GET_PARAMETER': (
        57,
        103,
    ),
    'FAILED_TO_INIT_ASYNC': (
        20,
        405,
    ),
    'FAILED_TO_SET_PARAMETER': (
        57,
        104,
    ),
    'FAILED_TO_SET_POOL': (
        51,
        101,
    ),
    'FAILED_TO_SIGN': (
        57,
        175,
    ),
    'FAILED_TO_SWAP_CONTEXT': (
        51,
        102,
    ),
    'FAILURE': (
        37,
        114,
    ),
    'FAILURE_OBTAINING_RANDOM': (
        56,
        107,
    ),
    'FAIL_INFO_OUT_OF_RANGE': (
        58,
        129,
    ),
    'FIELD_MISSING': (
        13,
        121,
    ),
    'FIELD_TOO_LARGE': (
        16,
        143,
    ),
    'FILENAME_TOO_BIG': (
        37,
        101,
    ),
    'FINAL_ERROR': (
        6,
        188,
    ),
    'FINGERPRINT_SIZE_DOES_NOT_MATCH_DIGEST': (
        44,
        121,
    ),
    'FINISH_FAILED': (
        38,
        106,
    ),
    'FIPS_MODE_NOT_SUPPORTED': (
        6,
        167,
    ),
    'FIPS_MODULE_CONDITIONAL_ERROR': (
        57,
        227,
    ),
    'FIPS_MODULE_ENTERING_ERROR_STATE': (
        57,
        224,
    ),
    'FIPS_MODULE_IN_ERROR_STATE': (
        57,
        225,
    ),
    'FIRST_NUM_TOO_LARGE': (
        13,
        122,
    ),
    'FIRST_OCTET_INVALID': (
        4,
        133,
    ),
    'FRAGMENTED_CLIENT_HELLO': (
        20,
        401,
    ),
    'FUNC_NOT_IMPLEMENTED': (
        36,
        101,
    ),
    'FWRITE_ERROR': (
        36,
        123,
    ),
    'GENERATE_ERROR': (
        36,
        112,
    ),
    'GETHOSTBYNAME_ADDR_IS_NOT_AF_INET': (
        32,
        107,
    ),
    'GETSOCKNAME_ERROR': (
        32,
        132,
    ),
    'GETSOCKNAME_TRUNCATED_ADDRESS': (
        32,
        133,
    ),
    'GETTING_SOCKTYPE': (
        32,
        134,
    ),
    'GET_RAW_KEY_FAILED': (
        6,
        182,
    ),
    'GF2M_NOT_SUPPORTED': (
        16,
        147,
    ),
    'GOT_A_FIN_BEFORE_A_CCS': (
        20,
        154,
    ),
    'GROUP2PKPARAMETERS_FAILURE': (
        16,
        120,
    ),
    'HEADER_PARSE_ERROR': (
        61,
        126,
    ),
    'HEADER_TOO_LONG': (
        9,
        128,
    ),
    'HEX_STRING_TOO_SHORT': (
        15,
        121,
    ),
    'HTTPS_PROXY_REQUEST': (
        20,
        155,
    ),
    'HTTP_REQUEST': (
        20,
        156,
    ),
    'I2D_ECPKPARAMETERS_FAILURE': (
        16,
        121,
    ),
    'IDP_MISMATCH': (
        11,
        128,
    ),
    'ID_NOT_SET': (
        53,
        112,
    ),
    'ID_OR_NAME_MISSING': (
        38,
        108,
    ),
    'ID_TOO_LARGE': (
        53,
        111,
    ),
    'ILLEGAL_BITSTRING_FORMAT': (
        13,
        175,
    ),
    'ILLEGAL_BOOLEAN': (
        13,
        176,
    ),
    'ILLEGAL_CHARACTERS': (
        13,
        124,
    ),
    'ILLEGAL_EMPTY_EXTENSION': (
        34,
        151,
    ),
    'ILLEGAL_FORMAT': (
        13,
        177,
    ),
    'ILLEGAL_HEX': (
        13,
        178,
    ),
    'ILLEGAL_HEX_DIGIT': (
        15,
        102,
    ),
    'ILLEGAL_IMPLICIT_TAG': (
        13,
        179,
    ),
    'ILLEGAL_INTEGER': (
        13,
        180,
    ),
    'ILLEGAL_NEGATIVE_VALUE': (
        13,
        226,
    ),
    'ILLEGAL_NESTED_TAGGING': (
        13,
        181,
    ),
    'ILLEGAL_NULL': (
        13,
        125,
    ),
    'ILLEGAL_NULL_VALUE': (
        13,
        182,
    ),
    'ILLEGAL_OBJECT': (
        13,
        183,
    ),
    'ILLEGAL_OPTIONAL_ANY': (
        13,
        126,
    ),
    'ILLEGAL_OPTIONS_ON_ITEM_TEMPLATE': (
        13,
        170,
    ),
    'ILLEGAL_OR_UNSUPPORTED_PADDING_MODE': (
        4,
        144,
    ),
    'ILLEGAL_PADDING': (
        13,
        221,
    ),
    'ILLEGAL_POINT_COMPRESSION': (
        20,
        162,
    ),
    'ILLEGAL_SCRYPT_PARAMETERS': (
        6,
        171,
    ),
    'ILLEGAL_SUITEB_DIGEST': (
        20,
        380,
    ),
    'ILLEGAL_TAGGED_ANY': (
        13,
        127,
    ),
    'ILLEGAL_TIME_VALUE': (
        13,
        184,
    ),
    'ILLEGAL_ZERO_CONTENT': (
        13,
        222,
    ),
    'INACCESSIBLE_DOMAIN_PARAMETERS': (
        6,
        204,
    ),
    'INACCESSIBLE_KEY': (
        6,
        203,
    ),
    'INAPPROPRIATE_FALLBACK': (
        20,
        373,
    ),
    'INCOMPATIBLE_OBJECTS': (
        16,
        101,
    ),
    'INCONSISTENT_COMPRESSION': (
        20,
        340,
    ),
    'INCONSISTENT_CONTENT_LENGTH': (
        61,
        120,
    ),
    'INCONSISTENT_EARLY_DATA_ALPN': (
        20,
        222,
    ),
    'INCONSISTENT_EARLY_DATA_SNI': (
        20,
        231,
    ),
    'INCONSISTENT_EXTMS': (
        20,
        104,
    ),
    'INCONSISTENT_HEADER': (
        9,
        121,
    ),
    'INCORRECT_FILE_SYNTAX': (
        37,
        115,
    ),
    'INCORRECT_POLICY_SYNTAX_TAG': (
        34,
        152,
    ),
    'INCORRECT_PROPERTY_QUERY': (
        59,
        100,
    ),
    'INDEX_TOO_LARGE': (
        40,
        102,
    ),
    'INDEX_TOO_SMALL': (
        40,
        103,
    ),
    'INDICATOR_INTEGRITY_FAILURE': (
        57,
        210,
    ),
    'INITIALIZATION_ERROR': (
        6,
        134,
    ),
    'INIT_FAILED': (
        38,
        109,
    ),
    'INPUT_NOT_INITIALIZED': (
        6,
        111,
    ),
    'INPUT_NOT_REDUCED': (
        3,
        110,
    ),
    'INSUFFICIENT_DATA_SPACE': (
        15,
        106,
    ),
    'INSUFFICIENT_DRBG_STRENGTH': (
        36,
        139,
    ),
    'INSUFFICIENT_PARAM_SIZE': (
        15,
        107,
    ),
    'INSUFFICIENT_SECURE_DATA_SPACE': (
        15,
        108,
    ),
    'INSUFFICIENT_SECURITY': (
        20,
        241,
    ),
    'INTEGER_NOT_ASCII_FORMAT': (
        13,
        185,
    ),
    'INTEGER_TOO_LARGE_FOR_LONG': (
        13,
        128,
    ),
    'INTERNAL_ERROR': (
        36,
        113,
    ),
    'INTERNAL_LIST_ERROR': (
        38,
        110,
    ),
    'INVALID_A': (
        16,
        168,
    ),
    'INVALID_AAD': (
        57,
        108,
    ),
    'INVALID_ALERT': (
        20,
        205,
    ),
    'INVALID_ARGS': (
        58,
        100,
    ),
    'INVALID_ARGUMENT': (
        38,
        143,
    ),
    'INVALID_ASNUMBER': (
        34,
        162,
    ),
    'INVALID_ASRANGE': (
        34,
        163,
    ),
    'INVALID_ATTRIBUTES': (
        11,
        138,
    ),
    'INVALID_B': (
        16,
        169,
    ),
    'INVALID_BIT_STRING_BITS_LEFT': (
        13,
        220,
    ),
    'INVALID_BMPSTRING_LENGTH': (
        13,
        129,
    ),
    'INVALID_BOOLEAN_STRING': (
        34,
        104,
    ),
    'INVALID_CCS_MESSAGE': (
        20,
        260,
    ),
    'INVALID_CERTIFICATE': (
        34,
        158,
    ),
    'INVALID_CERTIFICATE_OR_ALG': (
        20,
        238,
    ),
    'INVALID_CMD_NAME': (
        38,
        137,
    ),
    'INVALID_CMD_NUMBER': (
        38,
        138,
    ),
    'INVALID_COFACTOR': (
        16,
        171,
    ),
    'INVALID_COMMAND': (
        20,
        280,
    ),
    'INVALID_COMPRESSED_POINT': (
        16,
        110,
    ),
    'INVALID_COMPRESSION_ALGORITHM': (
        20,
        341,
    ),
    'INVALID_COMPRESSION_BIT': (
        16,
        109,
    ),
    'INVALID_CONFIG': (
        20,
        283,
    ),
    'INVALID_CONFIGURATION_NAME': (
        20,
        113,
    ),
    'INVALID_CONFIG_DATA': (
        57,
        211,
    ),
    'INVALID_CONSTANT_LENGTH': (
        57,
        157,
    ),
    'INVALID_CONTEXT': (
        20,
        282,
    ),
    'INVALID_CT_VALIDATION_TYPE': (
        20,
        212,
    ),
    'INVALID_CURVE': (
        53,
        108,
    ),
    'INVALID_CUSTOM_LENGTH': (
        57,
        111,
    ),
    'INVALID_DATA': (
        57,
        115,
    ),
    'INVALID_DIGEST': (
        53,
        102,
    ),
    'INVALID_DIGEST_LENGTH': (
        4,
        143,
    ),
    'INVALID_DIGEST_SIZE': (
        57,
        218,
    ),
    'INVALID_DIGEST_TYPE': (
        53,
        103,
    ),
    'INVALID_DIGIT': (
        13,
        130,
    ),
    'INVALID_DIRECTORY': (
        11,
        113,
    ),
    'INVALID_DISTPOINT': (
        11,
        143,
    ),
    'INVALID_EMPTY_NAME': (
        34,
        108,
    ),
    'INVALID_ENCODING': (
        53,
        104,
    ),
    'INVALID_ENCRYPTED_KEY_LENGTH': (
        46,
        117,
    ),
    'INVALID_EXTENSION_STRING': (
        34,
        105,
    ),
    'INVALID_FIELD': (
        53,
        105,
    ),
    'INVALID_FIELD_NAME': (
        11,
        119,
    ),
    'INVALID_FIPS_MODE': (
        6,
        168,
    ),
    'INVALID_FORM': (
        16,
        104,
    ),
    'INVALID_GENERATOR': (
        16,
        173,
    ),
    'INVALID_GROUP_ORDER': (
        16,
        122,
    ),
    'INVALID_HEADER': (
        4,
        137,
    ),
    'INVALID_INHERITANCE': (
        34,
        165,
    ),
    'INVALID_INIT_VALUE': (
        38,
        151,
    ),
    'INVALID_INPUT_LENGTH': (
        57,
        230,
    ),
    'INVALID_IPADDRESS': (
        34,
        166,
    ),
    'INVALID_ITERATION_COUNT': (
        57,
        123,
    ),
    'INVALID_IV_LENGTH': (
        57,
        109,
    ),
    'INVALID_KEY': (
        57,
        158,
    ),
    'INVALID_KEYPAIR': (
        4,
        171,
    ),
    'INVALID_KEY_ENCRYPTION_PARAMETER': (
        46,
        176,
    ),
    'INVALID_KEY_LENGTH': (
        4,
        173,
    ),
    'INVALID_KEY_UPDATE_TYPE': (
        20,
        120,
    ),
    'INVALID_LABEL': (
        4,
        160,
    ),
    'INVALID_LENGTH': (
        4,
        181,
    ),
    'INVALID_LOG_ID_LENGTH': (
        50,
        100,
    ),
    'INVALID_MAC': (
        57,
        151,
    ),
    'INVALID_MAX_EARLY_DATA': (
        20,
        174,
    ),
    'INVALID_MESSAGE_LENGTH': (
        4,
        131,
    ),
    'INVALID_MGF1_MD': (
        4,
        156,
    ),
    'INVALID_MIME_TYPE': (
        13,
        205,
    ),
    'INVALID_MODE': (
        57,
        125,
    ),
    'INVALID_MODIFIER': (
        13,
        186,
    ),
    'INVALID_MODULUS': (
        4,
        174,
    ),
    'INVALID_MULTIPLE_RDNS': (
        34,
        161,
    ),
    'INVALID_MULTI_PRIME_KEY': (
        4,
        167,
    ),
    'INVALID_NAME': (
        34,
        106,
    ),
    'INVALID_NAMED_GROUP_CONVERSION': (
        16,
        174,
    ),
    'INVALID_NEGATIVE_VALUE': (
        15,
        122,
    ),
    'INVALID_NULL_ALGORITHM': (
        6,
        218,
    ),
    'INVALID_NULL_ARGUMENT': (
        34,
        107,
    ),
    'INVALID_NULL_CMD_NAME': (
        20,
        385,
    ),
    'INVALID_NULL_PKCS12_POINTER': (
        35,
        105,
    ),
    'INVALID_NULL_POINTER': (
        47,
        102,
    ),
    'INVALID_NULL_VALUE': (
        34,
        109,
    ),
    'INVALID_NUMBER': (
        34,
        140,
    ),
    'INVALID_NUMBERS': (
        34,
        141,
    ),
    'INVALID_OAEP_PARAMETERS': (
        4,
        161,
    ),
    'INVALID_OBJECT_ENCODING': (
        13,
        216,
    ),
    'INVALID_OBJECT_IDENTIFIER': (
        34,
        110,
    ),
    'INVALID_OPERATION': (
        6,
        148,
    ),
    'INVALID_OPTION': (
        34,
        138,
    ),
    'INVALID_OSSL_PARAM_TYPE': (
        15,
        110,
    ),
    'INVALID_OUTPUT_LENGTH': (
        57,
        217,
    ),
    'INVALID_P': (
        16,
        172,
    ),
    'INVALID_PADDING': (
        4,
        138,
    ),
    'INVALID_PADDING_MODE': (
        4,
        141,
    ),
    'INVALID_PARAMETERS': (
        10,
        112,
    ),
    'INVALID_PARAMETER_NAME': (
        5,
        110,
    ),
    'INVALID_PARAMETER_NID': (
        5,
        114,
    ),
    'INVALID_PEER_KEY': (
        16,
        133,
    ),
    'INVALID_PENTANOMIAL_BASIS': (
        16,
        132,
    ),
    'INVALID_POLICY_IDENTIFIER': (
        34,
        134,
    ),
    'INVALID_POOL_SIZE': (
        51,
        103,
    ),
    'INVALID_PORT_NUMBER': (
        61,
        123,
    ),
    'INVALID_PRAGMA': (
        14,
        122,
    ),
    'INVALID_PRIVATE_KEY': (
        53,
        113,
    ),
    'INVALID_PROVIDER_FUNCTIONS': (
        6,
        193,
    ),
    'INVALID_PROXY_POLICY_SETTING': (
        34,
        153,
    ),
    'INVALID_PSS_PARAMETERS': (
        4,
        149,
    ),
    'INVALID_PSS_SALTLEN': (
        4,
        146,
    ),
    'INVALID_PUBINFO': (
        57,
        198,
    ),
    'INVALID_PUBKEY': (
        5,
        102,
    ),
    'INVALID_PURPOSE': (
        34,
        146,
    ),
    'INVALID_RANGE': (
        3,
        115,
    ),
    'INVALID_REQUEST': (
        4,
        175,
    ),
    'INVALID_SAFI': (
        34,
        164,
    ),
    'INVALID_SALT_LENGTH': (
        4,
        150,
    ),
    'INVALID_SCHEME': (
        44,
        106,
    ),
    'INVALID_SCRYPT_PARAMETERS': (
        13,
        227,
    ),
    'INVALID_SECRET': (
        5,
        128,
    ),
    'INVALID_SECRET_LENGTH': (
        6,
        223,
    ),
    'INVALID_SECTION': (
        34,
        135,
    ),
    'INVALID_SEED': (
        16,
        175,
    ),
    'INVALID_SEED_LENGTH': (
        57,
        154,
    ),
    'INVALID_SEPARATOR': (
        13,
        131,
    ),
    'INVALID_SEQUENCE_NUMBER': (
        20,
        402,
    ),
    'INVALID_SERVERINFO_DATA': (
        20,
        388,
    ),
    'INVALID_SESSION_ID': (
        20,
        999,
    ),
    'INVALID_SHIFT': (
        3,
        119,
    ),
    'INVALID_SIGNATURE_SIZE': (
        57,
        179,
    ),
    'INVALID_SIGNED_DATA_TYPE': (
        33,
        155,
    ),
    'INVALID_SIGNER_CERTIFICATE_PURPOSE': (
        47,
        117,
    ),
    'INVALID_SOCKET': (
        32,
        135,
    ),
    'INVALID_SRP_USERNAME': (
        20,
        357,
    ),
    'INVALID_STATE': (
        57,
        212,
    ),
    'INVALID_STATUS_RESPONSE': (
        20,
        328,
    ),
    'INVALID_STRENGTH': (
        4,
        176,
    ),
    'INVALID_STRING': (
        38,
        150,
    ),
    'INVALID_STRING_TABLE_VALUE': (
        13,
        218,
    ),
    'INVALID_SYNTAX': (
        34,
        143,
    ),
    'INVALID_TAG': (
        57,
        110,
    ),
    'INVALID_TAG_LENGTH': (
        57,
        118,
    ),
    'INVALID_TICKET_KEYS_LENGTH': (
        20,
        325,
    ),
    'INVALID_TRAILER': (
        4,
        139,
    ),
    'INVALID_TRINOMIAL_BASIS': (
        16,
        137,
    ),
    'INVALID_TRUST': (
        11,
        123,
    ),
    'INVALID_TYPE': (
        35,
        112,
    ),
    'INVALID_UKM_LENGTH': (
        57,
        200,
    ),
    'INVALID_UNIVERSALSTRING_LENGTH': (
        13,
        133,
    ),
    'INVALID_URL_PATH': (
        61,
        125,
    ),
    'INVALID_URL_SCHEME': (
        61,
        124,
    ),
    'INVALID_UTF8STRING': (
        13,
        134,
    ),
    'INVALID_VALUE': (
        6,
        222,
    ),
    'INVALID_X931_DIGEST': (
        4,
        142,
    ),
    'IN_ERROR_STATE': (
        36,
        114,
    ),
    'IN_USE': (
        32,
        123,
    ),
    'IQMP_NOT_INVERSE_OF_Q': (
        4,
        126,
    ),
    'ISSUER_DECODE_ERROR': (
        34,
        126,
    ),
    'ISSUER_MISMATCH': (
        11,
        129,
    ),
    'IS_NOT_A': (
        44,
        112,
    ),
    'ITERATIONCOUNT_BELOW_100': (
        56,
        108,
    ),
    'IV_GEN_ERROR': (
        35,
        106,
    ),
    'KDF_PARAMETER_ERROR': (
        16,
        148,
    ),
    'KEYBLOB_HEADER_PARSE_ERROR': (
        9,
        122,
    ),
    'KEYBLOB_TOO_SHORT': (
        9,
        123,
    ),
    'KEYMGMT_EXPORT_FAILURE': (
        6,
        205,
    ),
    'KEYS_NOT_SET': (
        16,
        140,
    ),
    'KEY_GEN_ERROR': (
        35,
        107,
    ),
    'KEY_PRIME_NUM_INVALID': (
        4,
        165,
    ),
    'KEY_SETUP_FAILED': (
        57,
        101,
    ),
    'KEY_SIZE_TOO_SMALL': (
        4,
        120,
    ),
    'KEY_TYPE_MISMATCH': (
        11,
        115,
    ),
    'KEY_VALUES_MISMATCH': (
        11,
        116,
    ),
    'LADDER_POST_FAILURE': (
        16,
        136,
    ),
    'LADDER_PRE_FAILURE': (
        16,
        153,
    ),
    'LADDER_STEP_FAILURE': (
        16,
        162,
    ),
    'LAST_OCTET_INVALID': (
        4,
        134,
    ),
    'LEGACY_SIGALG_DISALLOWED_OR_UNSUPPORTED': (
        20,
        333,
    ),
    'LENGTH_MISMATCH': (
        20,
        159,
    ),
    'LENGTH_TOO_LARGE': (
        57,
        202,
    ),
    'LENGTH_TOO_LONG': (
        20,
        404,
    ),
    'LENGTH_TOO_SHORT': (
        20,
        160,
    ),
    'LIBRARY_BUG': (
        20,
        274,
    ),
    'LIBRARY_HAS_NO_CIPHERS': (
        20,
        161,
    ),
    'LISTEN_V6_ONLY': (
        32,
        136,
    ),
    'LIST_CANNOT_BE_NULL': (
        14,
        115,
    ),
    'LIST_ERROR': (
        13,
        188,
    ),
    'LOADER_INCOMPLETE': (
        44,
        116,
    ),
    'LOADING_CERT_DIR': (
        11,
        103,
    ),
    'LOADING_DEFAULTS': (
        11,
        104,
    ),
    'LOADING_STARTED': (
        44,
        117,
    ),
    'LOAD_FAILED': (
        37,
        103,
    ),
    'LOCKING_NOT_SUPPORTED': (
        6,
        213,
    ),
    'LOG_CONF_INVALID': (
        50,
        109,
    ),
    'LOG_CONF_INVALID_KEY': (
        50,
        110,
    ),
    'LOG_CONF_MISSING_DESCRIPTION': (
        50,
        111,
    ),
    'LOG_CONF_MISSING_KEY': (
        50,
        112,
    ),
    'LOG_KEY_INVALID': (
        50,
        113,
    ),
    'LOOKUP_RETURNED_NOTHING': (
        32,
        142,
    ),
    'MAC_ABSENT': (
        35,
        108,
    ),
    'MAC_GENERATION_ERROR': (
        35,
        109,
    ),
    'MAC_SETUP_ERROR': (
        35,
        110,
    ),
    'MAC_STRING_SET_ERROR': (
        35,
        111,
    ),
    'MAC_VERIFY_FAILURE': (
        35,
        113,
    ),
    'MALFORMED_HOST_OR_SERVICE': (
        32,
        130,
    ),
    'MALFORMED_IV': (
        56,
        101,
    ),
    'MANDATORY_BRACES_IN_VARIABLE_EXPANSION': (
        14,
        123,
    ),
    'MAX_RESP_LEN_EXCEEDED': (
        61,
        117,
    ),
    'MD_BIO_INIT_ERROR': (
        46,
        119,
    ),
    'MEMORY_LIMIT_EXCEEDED': (
        6,
        172,
    ),
    'MESSAGEDIGEST_ATTRIBUTE_WRONG_LENGTH': (
        46,
        120,
    ),
    'MESSAGEDIGEST_WRONG_LENGTH': (
        46,
        121,
    ),
    'MESSAGE_DIGEST_IS_NULL': (
        6,
        159,
    ),
    'MESSAGE_IMPRINT_MISMATCH': (
        47,
        103,
    ),
    'METHOD_NOT_SUPPORTED': (
        11,
        124,
    ),
    'MGF1_DIGEST_NOT_ALLOWED': (
        4,
        152,
    ),
    'MIME_NO_CONTENT_TYPE': (
        13,
        206,
    ),
    'MIME_PARSE_ERROR': (
        13,
        207,
    ),
    'MIME_SIG_PARSE_ERROR': (
        13,
        208,
    ),
    'MISMATCHING_DOMAIN_PARAMETERS': (
        57,
        203,
    ),
    'MISSING_ASN1_ENCODING': (
        61,
        110,
    ),
    'MISSING_CEK_ALG': (
        57,
        144,
    ),
    'MISSING_CERTID': (
        58,
        165,
    ),
    'MISSING_CIPHER': (
        57,
        155,
    ),
    'MISSING_CLOSE_SQUARE_BRACKET': (
        14,
        100,
    ),
    'MISSING_CONFIG_DATA': (
        57,
        213,
    ),
    'MISSING_CONSTANT': (
        57,
        156,
    ),
    'MISSING_CONTENT_TYPE': (
        61,
        121,
    ),
    'MISSING_DEK_IV': (
        9,
        129,
    ),
    'MISSING_DSA_SIGNING_CERT': (
        20,
        165,
    ),
    'MISSING_ECDSA_SIGNING_CERT': (
        20,
        381,
    ),
    'MISSING_EOC': (
        13,
        137,
    ),
    'MISSING_EQUAL_SIGN': (
        14,
        101,
    ),
    'MISSING_FATAL': (
        20,
        256,
    ),
    'MISSING_GET_PARAMS': (
        59,
        102,
    ),
    'MISSING_INIT_FUNCTION': (
        14,
        112,
    ),
    'MISSING_KEY': (
        57,
        128,
    ),
    'MISSING_KEY_INPUT_FOR_CREATING_PROTECTION': (
        58,
        130,
    ),
    'MISSING_KEY_USAGE_DIGITALSIGNATURE': (
        58,
        142,
    ),
    'MISSING_MAC': (
        57,
        150,
    ),
    'MISSING_MESSAGE_DIGEST': (
        57,
        129,
    ),
    'MISSING_OCSPSIGNING_USAGE': (
        39,
        103,
    ),
    'MISSING_OID': (
        57,
        209,
    ),
    'MISSING_P10CSR': (
        58,
        121,
    ),
    'MISSING_PARAMETERS': (
        20,
        290,
    ),
    'MISSING_PASS': (
        57,
        130,
    ),
    'MISSING_PBM_SECRET': (
        58,
        166,
    ),
    'MISSING_PRIVATE_KEY': (
        4,
        179,
    ),
    'MISSING_PRIVATE_KEY_FOR_POPO': (
        58,
        190,
    ),
    'MISSING_PROTECTION': (
        58,
        143,
    ),
    'MISSING_PSK_KEX_MODES_EXTENSION': (
        20,
        310,
    ),
    'MISSING_PUBKEY': (
        5,
        125,
    ),
    'MISSING_PUBLIC_KEY': (
        58,
        183,
    ),
    'MISSING_REDIRECT_LOCATION': (
        61,
        111,
    ),
    'MISSING_REFERENCE_CERT': (
        58,
        168,
    ),
    'MISSING_RSA_CERTIFICATE': (
        20,
        168,
    ),
    'MISSING_RSA_ENCRYPTING_CERT': (
        20,
        169,
    ),
    'MISSING_RSA_SIGNING_CERT': (
        20,
        170,
    ),
    'MISSING_SALT': (
        57,
        131,
    ),
    'MISSING_SECOND_NUMBER': (
        13,
        138,
    ),
    'MISSING_SECRET': (
        57,
        132,
    ),
    'MISSING_SEED': (
        57,
        140,
    ),
    'MISSING_SENDER_IDENTIFICATION': (
        58,
        111,
    ),
    'MISSING_SESSION_ID': (
        57,
        133,
    ),
    'MISSING_SIGALGS_EXTENSION': (
        20,
        112,
    ),
    'MISSING_SIGNING_CERT': (
        20,
        221,
    ),
    'MISSING_SIGNING_CERTIFICATE_ATTRIBUTE': (
        54,
        108,
    ),
    'MISSING_SRP_PARAM': (
        20,
        358,
    ),
    'MISSING_SUPPORTED_GROUPS_EXTENSION': (
        20,
        209,
    ),
    'MISSING_TMP_DH_KEY': (
        20,
        171,
    ),
    'MISSING_TMP_ECDH_KEY': (
        20,
        311,
    ),
    'MISSING_TRUST_ANCHOR': (
        58,
        179,
    ),
    'MISSING_TRUST_STORE': (
        58,
        144,
    ),
    'MISSING_TYPE': (
        57,
        134,
    ),
    'MISSING_VALUE': (
        34,
        124,
    ),
    'MISSING_XCGHASH': (
        57,
        135,
    ),
    'MIXED_HANDSHAKE_AND_NON_HANDSHAKE_DATA': (
        20,
        293,
    ),
    'MODULE_INITIALIZATION_ERROR': (
        14,
        109,
    ),
    'MODULE_INTEGRITY_FAILURE': (
        57,
        214,
    ),
    'MODULUS_TOO_LARGE': (
        4,
        105,
    ),
    'MODULUS_TOO_SMALL': (
        5,
        126,
    ),
    'MP_COEFFICIENT_NOT_INVERSE_OF_R': (
        4,
        168,
    ),
    'MP_EXPONENT_NOT_CONGRUENT_TO_D': (
        4,
        169,
    ),
    'MP_R_NOT_PRIME': (
        4,
        170,
    ),
    'MSGSIGDIGEST_ERROR': (
        46,
        172,
    ),
    'MSGSIGDIGEST_VERIFICATION_FAILURE': (
        46,
        162,
    ),
    'MSGSIGDIGEST_WRONG_LENGTH': (
        46,
        163,
    ),
    'MSTRING_NOT_UNIVERSAL': (
        13,
        139,
    ),
    'MSTRING_WRONG_TAG': (
        13,
        140,
    ),
    'MULTIPLE_REQUESTS_NOT_SUPPORTED': (
        58,
        161,
    ),
    'MULTIPLE_RESPONSES_NOT_SUPPORTED': (
        58,
        170,
    ),
    'MULTIPLE_SAN_SOURCES': (
        58,
        102,
    ),
    'NAME_TOO_LONG': (
        11,
        134,
    ),
    'NAME_TRANSLATION_FAILED': (
        37,
        109,
    ),
    'NBIO_CONNECT_ERROR': (
        32,
        110,
    ),
    'NEED_NEW_SETUP_VALUES': (
        16,
        157,
    ),
    'NEED_ONE_SIGNER': (
        46,
        164,
    ),
    'NEED_ORGANIZATION_AND_NUMBERS': (
        34,
        142,
    ),
    'NEGATIVE_PATHLEN': (
        34,
        168,
    ),
    'NESTED_ASN1_STRING': (
        13,
        197,
    ),
    'NESTED_TOO_DEEP': (
        13,
        201,
    ),
    'NEWER_CRL_NOT_NEWER': (
        11,
        132,
    ),
    'NEXTUPDATE_BEFORE_THISUPDATE': (
        39,
        124,
    ),
    'NONCE_MISMATCH': (
        47,
        104,
    ),
    'NONCE_NOT_RETURNED': (
        47,
        105,
    ),
    'NON_HEX_CHARACTERS': (
        13,
        141,
    ),
    'NOT_ABLE_TO_COPY_CTX': (
        6,
        190,
    ),
    'NOT_AN_ASCII_CHARACTER': (
        55,
        101,
    ),
    'NOT_AN_HEXADECIMAL_DIGIT': (
        55,
        102,
    ),
    'NOT_AN_IDENTIFIER': (
        55,
        103,
    ),
    'NOT_AN_OCTAL_DIGIT': (
        55,
        104,
    ),
    'NOT_ASCII_FORMAT': (
        13,
        190,
    ),
    'NOT_A_CERTIFICATE': (
        44,
        100,
    ),
    'NOT_A_CRL': (
        44,
        101,
    ),
    'NOT_A_DECIMAL_DIGIT': (
        55,
        105,
    ),
    'NOT_A_NAME': (
        44,
        103,
    ),
    'NOT_A_NIST_PRIME': (
        16,
        135,
    ),
    'NOT_A_PRIVATE_KEY': (
        57,
        221,
    ),
    'NOT_A_PUBLIC_KEY': (
        57,
        220,
    ),
    'NOT_A_REGULAR_FILE': (
        36,
        122,
    ),
    'NOT_A_SIGNED_RECEIPT': (
        46,
        165,
    ),
    'NOT_A_SQUARE': (
        3,
        111,
    ),
    'NOT_BASIC_RESPONSE': (
        39,
        104,
    ),
    'NOT_DEK_INFO': (
        9,
        105,
    ),
    'NOT_ENCRYPTED': (
        9,
        106,
    ),
    'NOT_ENCRYPTED_DATA': (
        46,
        122,
    ),
    'NOT_ENOUGH_DATA': (
        13,
        142,
    ),
    'NOT_IMPLEMENTED': (
        16,
        126,
    ),
    'NOT_INITIALISED': (
        38,
        117,
    ),
    'NOT_INITIALIZED': (
        16,
        111,
    ),
    'NOT_INSTANTIATED': (
        36,
        115,
    ),
    'NOT_KEK': (
        46,
        123,
    ),
    'NOT_KEY_AGREEMENT': (
        46,
        181,
    ),
    'NOT_KEY_TRANSPORT': (
        46,
        124,
    ),
    'NOT_LOADED': (
        38,
        112,
    ),
    'NOT_ON_RECORD_BOUNDARY': (
        20,
        182,
    ),
    'NOT_PARAMETERS': (
        57,
        226,
    ),
    'NOT_PROC_TYPE': (
        9,
        107,
    ),
    'NOT_PWRI': (
        46,
        177,
    ),
    'NOT_REPLACING_CERTIFICATE': (
        20,
        289,
    ),
    'NOT_SERVER': (
        20,
        284,
    ),
    'NOT_SUITABLE_GENERATOR': (
        5,
        120,
    ),
    'NOT_SUPPORTED': (
        57,
        136,
    ),
    'NOT_SUPPORTED_FOR_THIS_KEY_TYPE': (
        46,
        125,
    ),
    'NOT_XOF_OR_INVALID_LENGTH': (
        57,
        113,
    ),
    'NO_ACCEPT_ADDR_OR_SERVICE_SPECIFIED': (
        32,
        143,
    ),
    'NO_APPLICATION_PROTOCOL': (
        20,
        235,
    ),
    'NO_CERTIFICATES_IN_CHAIN': (
        39,
        105,
    ),
    'NO_CERTIFICATES_RETURNED': (
        20,
        176,
    ),
    'NO_CERTIFICATE_ASSIGNED': (
        20,
        177,
    ),
    'NO_CERTIFICATE_FOUND': (
        11,
        135,
    ),
    'NO_CERTIFICATE_OR_CRL_FOUND': (
        11,
        136,
    ),
    'NO_CERTIFICATE_SET': (
        20,
        179,
    ),
    'NO_CERT_SET_FOR_US_TO_VERIFY': (
        11,
        105,
    ),
    'NO_CHANGE_FOLLOWING_HRR': (
        20,
        214,
    ),
    'NO_CIPHER': (
        46,
        126,
    ),
    'NO_CIPHERS_AVAILABLE': (
        20,
        181,
    ),
    'NO_CIPHERS_SPECIFIED': (
        20,
        183,
    ),
    'NO_CIPHER_MATCH': (
        20,
        185,
    ),
    'NO_CIPHER_SET': (
        6,
        131,
    ),
    'NO_CLIENT_CERT_METHOD': (
        20,
        331,
    ),
    'NO_CLOSE_BRACE': (
        14,
        102,
    ),
    'NO_COMPRESSION_SPECIFIED': (
        20,
        187,
    ),
    'NO_CONF': (
        14,
        105,
    ),
    'NO_CONFIG_DATABASE': (
        34,
        136,
    ),
    'NO_CONF_OR_ENVIRONMENT_VARIABLE': (
        14,
        106,
    ),
    'NO_CONTENT': (
        47,
        106,
    ),
    'NO_CONTENT_TYPE': (
        46,
        173,
    ),
    'NO_CONTROL_FUNCTION': (
        38,
        120,
    ),
    'NO_COOKIE_CALLBACK_SET': (
        20,
        287,
    ),
    'NO_CRL_FOUND': (
        11,
        137,
    ),
    'NO_CRL_NUMBER': (
        11,
        130,
    ),
    'NO_DEFAULT_DIGEST': (
        33,
        151,
    ),
    'NO_DIGEST_SET': (
        6,
        139,
    ),
    'NO_DRBG_IMPLEMENTATION_SELECTED': (
        36,
        128,
    ),
    'NO_FILENAME': (
        37,
        111,
    ),
    'NO_GOST_CERTIFICATE_SENT_BY_PEER': (
        20,
        330,
    ),
    'NO_HOSTNAME_OR_SERVICE_SPECIFIED': (
        32,
        144,
    ),
    'NO_IMPORT_FUNCTION': (
        6,
        206,
    ),
    'NO_INDEX': (
        38,
        144,
    ),
    'NO_INVERSE': (
        3,
        108,
    ),
    'NO_ISSUER_CERTIFICATE': (
        34,
        121,
    ),
    'NO_ISSUER_DETAILS': (
        34,
        127,
    ),
    'NO_KEY': (
        46,
        130,
    ),
    'NO_KEYMGMT_AVAILABLE': (
        6,
        199,
    ),
    'NO_KEYMGMT_PRESENT': (
        6,
        196,
    ),
    'NO_KEY_OR_CERT': (
        46,
        174,
    ),
    'NO_KEY_SET': (
        57,
        114,
    ),
    'NO_LOADERS_FOUND': (
        44,
        123,
    ),
    'NO_LOAD_FUNCTION': (
        38,
        125,
    ),
    'NO_MATCHING_CHOICE_TYPE': (
        13,
        143,
    ),
    'NO_MATCHING_DIGEST': (
        46,
        131,
    ),
    'NO_MATCHING_DIGEST_TYPE_FOUND': (
        33,
        154,
    ),
    'NO_MATCHING_RECIPIENT': (
        46,
        132,
    ),
    'NO_MATCHING_SIGNATURE': (
        46,
        166,
    ),
    'NO_MATCHING_STRING_DELIMITER': (
        55,
        106,
    ),
    'NO_METHOD_SPECIFIED': (
        20,
        188,
    ),
    'NO_MSGSIGDIGEST': (
        46,
        167,
    ),
    'NO_MULTIPART_BODY_FAILURE': (
        13,
        210,
    ),
    'NO_MULTIPART_BOUNDARY': (
        13,
        211,
    ),
    'NO_OPERATION_SET': (
        6,
        149,
    ),
    'NO_PARAMETERS_SET': (
        53,
        109,
    ),
    'NO_PASSWORD': (
        46,
        178,
    ),
    'NO_PEM_EXTENSIONS': (
        20,
        389,
    ),
    'NO_POLICY_IDENTIFIER': (
        34,
        139,
    ),
    'NO_PORT_DEFINED': (
        32,
        113,
    ),
    'NO_PRIME_CANDIDATE': (
        3,
        121,
    ),
    'NO_PRIVATE_KEY': (
        46,
        133,
    ),
    'NO_PRIVATE_KEY_ASSIGNED': (
        20,
        190,
    ),
    'NO_PRIVATE_VALUE': (
        16,
        154,
    ),
    'NO_PROTOCOLS_AVAILABLE': (
        20,
        191,
    ),
    'NO_PROXY_CERT_POLICY_LANGUAGE_DEFINED': (
        34,
        154,
    ),
    'NO_PUBLIC_EXPONENT': (
        4,
        140,
    ),
    'NO_PUBLIC_KEY': (
        34,
        114,
    ),
    'NO_RECEIPT_REQUEST': (
        46,
        168,
    ),
    'NO_RECIPIENT_MATCHES_CERTIFICATE': (
        33,
        115,
    ),
    'NO_REFERENCE': (
        38,
        130,
    ),
    'NO_RENEGOTIATION': (
        20,
        339,
    ),
    'NO_REQUIRED_DIGEST': (
        20,
        324,
    ),
    'NO_RESPONSE_DATA': (
        39,
        108,
    ),
    'NO_RESULT_BUFFER': (
        40,
        105,
    ),
    'NO_REVOKED_TIME': (
        39,
        109,
    ),
    'NO_SECTION': (
        14,
        107,
    ),
    'NO_SHARED_CIPHER': (
        20,
        193,
    ),
    'NO_SHARED_GROUPS': (
        20,
        410,
    ),
    'NO_SHARED_SIGNATURE_ALGORITHMS': (
        20,
        376,
    ),
    'NO_SIGNATURES_ON_DATA': (
        33,
        123,
    ),
    'NO_SIGNERS': (
        33,
        142,
    ),
    'NO_SIGNER_KEY': (
        39,
        130,
    ),
    'NO_SIG_CONTENT_TYPE': (
        13,
        212,
    ),
    'NO_SOLUTION': (
        3,
        116,
    ),
    'NO_SRTP_PROFILES': (
        20,
        359,
    ),
    'NO_START_LINE': (
        9,
        108,
    ),
    'NO_STDIO': (
        58,
        194,
    ),
    'NO_SUBJECT_DETAILS': (
        34,
        125,
    ),
    'NO_SUCH_ENGINE': (
        38,
        116,
    ),
    'NO_SUCH_FILE': (
        14,
        114,
    ),
    'NO_SUITABLE_DIGEST': (
        3,
        120,
    ),
    'NO_SUITABLE_DIGEST_ALGORITHM': (
        20,
        297,
    ),
    'NO_SUITABLE_GROUPS': (
        20,
        295,
    ),
    'NO_SUITABLE_KEY_SHARE': (
        20,
        101,
    ),
    'NO_SUITABLE_SENDER_CERT': (
        58,
        145,
    ),
    'NO_SUITABLE_SIGNATURE_ALGORITHM': (
        20,
        118,
    ),
    'NO_TIME_STAMP_TOKEN': (
        47,
        107,
    ),
    'NO_VALID_SCTS': (
        20,
        216,
    ),
    'NO_VALUE': (
        55,
        107,
    ),
    'NO_VERIFY_COOKIE_CALLBACK': (
        20,
        403,
    ),
    'NULL_ARGUMENT': (
        56,
        109,
    ),
    'NULL_BEFORE_BLOCK_MISSING': (
        4,
        113,
    ),
    'NULL_HANDLE': (
        37,
        104,
    ),
    'NULL_IS_WRONG_LENGTH': (
        13,
        144,
    ),
    'NULL_MAC_PKEY_CTX': (
        6,
        208,
    ),
    'NULL_SSL_CTX': (
        20,
        195,
    ),
    'NULL_SSL_METHOD_PASSED': (
        20,
        196,
    ),
    'NUMBER_TOO_LARGE': (
        14,
        121,
    ),
    'N_DOES_NOT_EQUAL_PRODUCT_OF_PRIMES': (
        4,
        172,
    ),
    'N_DOES_NOT_EQUAL_P_Q': (
        4,
        127,
    ),
    'OAEP_DECODING_ERROR': (
        4,
        121,
    ),
    'OBJECT_NOT_ASCII_FORMAT': (
        13,
        191,
    ),
    'OCSP_CALLBACK_FAILURE': (
        20,
        305,
    ),
    'ODD_NUMBER_OF_CHARS': (
        13,
        145,
    ),
    'ODD_NUMBER_OF_DIGITS': (
        15,
        103,
    ),
    'OID_EXISTS': (
        8,
        102,
    ),
    'OLD_SESSION_CIPHER_NOT_RETURNED': (
        20,
        197,
    ),
    'OLD_SESSION_COMPRESSION_ALGORITHM_NOT_RETURNED': (
        20,
        344,
    ),
    'ONLY_ONESHOT_SUPPORTED': (
        6,
        177,
    ),
    'OPENSSL_CONF_REFERENCES_MISSING_SECTION': (
        14,
        124,
    ),
    'OPERATION_NOT_DEFINED': (
        34,
        148,
    ),
    'OPERATION_NOT_INITIALIZED': (
        6,
        151,
    ),
    'OPERATION_NOT_SUPPORTED': (
        16,
        152,
    ),
    'OPERATION_NOT_SUPPORTED_FOR_THIS_KEYTYPE': (
        4,
        148,
    ),
    'OPERATION_NOT_SUPPORTED_ON_THIS_TYPE': (
        33,
        104,
    ),
    'OTHERNAME_ERROR': (
        34,
        147,
    ),
    'OUTPUT_BUFFER_TOO_SMALL': (
        57,
        106,
    ),
    'OUTPUT_WOULD_OVERFLOW': (
        6,
        202,
    ),
    'OVERFLOW_ERROR': (
        20,
        237,
    ),
    'PACKET_LENGTH_TOO_LONG': (
        20,
        198,
    ),
    'PADDING_CHECK_FAILED': (
        4,
        114,
    ),
    'PAIRWISE_TEST_FAILURE': (
        4,
        177,
    ),
    'PARAMETER_ENCODING_ERROR': (
        10,
        105,
    ),
    'PARAMETER_TOO_LARGE': (
        6,
        187,
    ),
    'PARENT_CANNOT_GENERATE_RANDOM_NUMBERS': (
        57,
        228,
    ),
    'PARENT_CANNOT_SUPPLY_ENTROPY_SEED': (
        57,
        187,
    ),
    'PARENT_LOCKING_NOT_ENABLED': (
        36,
        130,
    ),
    'PARENT_STRENGTH_TOO_WEAK': (
        36,
        131,
    ),
    'PARSE_ERROR': (
        35,
        114,
    ),
    'PARSE_FAILED': (
        55,
        108,
    ),
    'PARSE_TLSEXT': (
        20,
        227,
    ),
    'PARTIALLY_OVERLAPPING': (
        6,
        162,
    ),
    'PASSED_NULL_PARAMETER': (
        16,
        134,
    ),
    'PASSPHRASE_CALLBACK_ERROR': (
        44,
        114,
    ),
    'PATH_MUST_BE_ABSOLUTE': (
        57,
        219,
    ),
    'PATH_TOO_LONG': (
        20,
        270,
    ),
    'PBKDF2_ERROR': (
        6,
        181,
    ),
    'PEER_DID_NOT_RETURN_A_CERTIFICATE': (
        20,
        199,
    ),
    'PEER_KEY_ERROR': (
        16,
        149,
    ),
    'PEM_NAME_BAD_PREFIX': (
        20,
        391,
    ),
    'PEM_NAME_TOO_SHORT': (
        20,
        392,
    ),
    'PERSONALISATION_STRING_TOO_LONG': (
        36,
        116,
    ),
    'PIPELINE_FAILURE': (
        20,
        406,
    ),
    'PKCS12_CIPHERFINAL_ERROR': (
        35,
        116,
    ),
    'PKCS7_ADD_SIGNATURE_ERROR': (
        47,
        118,
    ),
    'PKCS7_ADD_SIGNED_ATTR_ERROR': (
        47,
        119,
    ),
    'PKCS7_ADD_SIGNER_ERROR': (
        33,
        153,
    ),
    'PKCS7_DATASIGN': (
        33,
        145,
    ),
    'PKCS7_TO_TS_TST_INFO_FAILED': (
        47,
        129,
    ),
    'PKCS_DECODING_ERROR': (
        4,
        159,
    ),
    'PKEY_APPLICATION_ASN1_METHOD_ALREADY_REGISTERED': (
        6,
        179,
    ),
    'PKIBODY_ERROR': (
        58,
        146,
    ),
    'PKISTATUSINFO_NOT_FOUND': (
        58,
        132,
    ),
    'POINT_ARITHMETIC_FAILURE': (
        16,
        155,
    ),
    'POINT_AT_INFINITY': (
        16,
        106,
    ),
    'POINT_COORDINATES_BLIND_FAILURE': (
        16,
        163,
    ),
    'POINT_IS_NOT_ON_CURVE': (
        16,
        107,
    ),
    'POLICY_LANGUAGE_ALREADY_DEFINED': (
        34,
        155,
    ),
    'POLICY_MISMATCH': (
        47,
        108,
    ),
    'POLICY_PATH_LENGTH': (
        34,
        156,
    ),
    'POLICY_PATH_LENGTH_ALREADY_DEFINED': (
        34,
        157,
    ),
    'POLICY_WHEN_PROXY_LANGUAGE_REQUIRES_NO_POLICY': (
        34,
        159,
    ),
    'POLLING_FAILED': (
        58,
        172,
    ),
    'POPOSKINPUT_NOT_SUPPORTED': (
        56,
        113,
    ),
    'POPO_INCONSISTENT_PUBLIC_KEY': (
        56,
        117,
    ),
    'POPO_MISSING': (
        56,
        121,
    ),
    'POPO_MISSING_PUBLIC_KEY': (
        56,
        118,
    ),
    'POPO_MISSING_SUBJECT': (
        56,
        119,
    ),
    'POPO_RAVERIFIED_NOT_ACCEPTED': (
        56,
        120,
    ),
    'POST_HANDSHAKE_AUTH_ENCODING_ERR': (
        20,
        278,
    ),
    'POTENTIALLY_INVALID_CERTIFICATE': (
        58,
        147,
    ),
    'PREDICTION_RESISTANCE_NOT_SUPPORTED': (
        36,
        133,
    ),
    'PRIVATE_KEY_DECODE_ERROR': (
        6,
        145,
    ),
    'PRIVATE_KEY_DOES_NOT_MATCH_CERTIFICATE': (
        47,
        120,
    ),
    'PRIVATE_KEY_ENCODE_ERROR': (
        6,
        146,
    ),
    'PRIVATE_KEY_MISMATCH': (
        20,
        288,
    ),
    'PRIVATE_KEY_TOO_LARGE': (
        3,
        117,
    ),
    'PRNG_NOT_SEEDED': (
        36,
        100,
    ),
    'PROBLEMS_GETTING_PASSWORD': (
        9,
        109,
    ),
    'PROCESSING_ERROR': (
        40,
        107,
    ),
    'PROTOCOL_IS_SHUTDOWN': (
        20,
        207,
    ),
    'PROVIDER_ALREADY_EXISTS': (
        15,
        104,
    ),
    'PROVIDER_SECTION_ERROR': (
        15,
        105,
    ),
    'PSK_IDENTITY_NOT_FOUND': (
        20,
        223,
    ),
    'PSK_NO_CLIENT_CB': (
        20,
        224,
    ),
    'PSK_NO_SERVER_CB': (
        20,
        225,
    ),
    'PSS_SALTLEN_TOO_SMALL': (
        4,
        164,
    ),
    'PUBLIC_KEY_DECODE_ERROR': (
        11,
        125,
    ),
    'PUBLIC_KEY_ENCODE_ERROR': (
        11,
        126,
    ),
    'PUBLIC_KEY_NOT_RSA': (
        6,
        106,
    ),
    'PUB_EXPONENT_OUT_OF_RANGE': (
        4,
        178,
    ),
    'PVK_DATA_TOO_SHORT': (
        9,
        124,
    ),
    'PVK_TOO_SHORT': (
        9,
        125,
    ),
    'P_IS_NOT_PRIME': (
        3,
        112,
    ),
    'P_NOT_PRIME': (
        4,
        128,
    ),
    'Q_NOT_PRIME': (
        4,
        129,
    ),
    'RANDOMNESS_SOURCE_STRENGTH_INSUFFICIENT': (
        4,
        180,
    ),
    'RANDOM_NUMBER_GENERATION_FAILED': (
        16,
        158,
    ),
    'RANDOM_POOL_OVERFLOW': (
        36,
        125,
    ),
    'RANDOM_POOL_UNDERFLOW': (
        36,
        134,
    ),
    'RANDOM_SECTION_ERROR': (
        15,
        119,
    ),
    'READ_BIO_NOT_SET': (
        20,
        211,
    ),
    'READ_KEY': (
        9,
        111,
    ),
    'READ_TIMEOUT_EXPIRED': (
        20,
        312,
    ),
    'RECEIPT_DECODE_ERROR': (
        46,
        169,
    ),
    'RECEIVED_ERROR': (
        61,
        105,
    ),
    'RECEIVED_WRONG_HTTP_VERSION': (
        61,
        106,
    ),
    'RECIPIENT_ERROR': (
        46,
        137,
    ),
    'RECIPNONCE_UNMATCHED': (
        58,
        148,
    ),
    'RECORD_LENGTH_MISMATCH': (
        20,
        213,
    ),
    'RECORD_TOO_SMALL': (
        20,
        298,
    ),
    'RECURSIVE_DIRECTORY_INCLUDE': (
        14,
        111,
    ),
    'REDIRECTION_FROM_HTTPS_TO_HTTP': (
        61,
        112,
    ),
    'REDIRECTION_NOT_ENABLED': (
        61,
        116,
    ),
    'RELATIVE_PATH': (
        14,
        125,
    ),
    'RENEGOTIATE_EXT_TOO_LONG': (
        20,
        335,
    ),
    'RENEGOTIATION_ENCODING_ERR': (
        20,
        336,
    ),
    'RENEGOTIATION_MISMATCH': (
        20,
        337,
    ),
    'REQUEST_NOT_ACCEPTED': (
        58,
        149,
    ),
    'REQUEST_NOT_SIGNED': (
        39,
        128,
    ),
    'REQUEST_PENDING': (
        20,
        285,
    ),
    'REQUEST_REJECTED_BY_SERVER': (
        58,
        182,
    ),
    'REQUEST_SENT': (
        20,
        286,
    ),
    'REQUEST_TOO_LARGE_FOR_DRBG': (
        36,
        117,
    ),
    'REQUIRED_CIPHER_MISSING': (
        20,
        215,
    ),
    'REQUIRED_COMPRESSION_ALGORITHM_MISSING': (
        20,
        342,
    ),
    'REQUIRE_CTR_MODE_CIPHER': (
        57,
        206,
    ),
    'RESEED_ERROR': (
        36,
        118,
    ),
    'RESPONSE_CONTAINS_NO_REVOCATION_DATA': (
        39,
        111,
    ),
    'RESPONSE_LINE_TOO_LONG': (
        61,
        113,
    ),
    'RESPONSE_PARSE_ERROR': (
        61,
        104,
    ),
    'RESPONSE_SETUP_ERROR': (
        47,
        121,
    ),
    'RESULT_TOO_LARGE': (
        40,
        100,
    ),
    'RESULT_TOO_SMALL': (
        40,
        101,
    ),
    'RETRY_TIMEOUT': (
        61,
        129,
    ),
    'ROOT_CA_NOT_TRUSTED': (
        39,
        112,
    ),
    'RSA_OPERATIONS_NOT_SUPPORTED': (
        4,
        130,
    ),
    'SCSV_RECEIVED_WHEN_RENEGOTIATING': (
        20,
        345,
    ),
    'SCT_FUTURE_TIMESTAMP': (
        50,
        116,
    ),
    'SCT_INVALID': (
        50,
        104,
    ),
    'SCT_INVALID_SIGNATURE': (
        50,
        107,
    ),
    'SCT_LIST_INVALID': (
        50,
        105,
    ),
    'SCT_LOG_ID_MISMATCH': (
        50,
        114,
    ),
    'SCT_NOT_SET': (
        50,
        106,
    ),
    'SCT_UNSUPPORTED_VERSION': (
        50,
        115,
    ),
    'SCT_VERIFICATION_FAILED': (
        20,
        208,
    ),
    'SEARCH_ONLY_SUPPORTED_FOR_DIRECTORIES': (
        57,
        222,
    ),
    'SECOND_NUMBER_TOO_LARGE': (
        13,
        147,
    ),
    'SECTION_NOT_FOUND': (
        34,
        150,
    ),
    'SECURE_MALLOC_FAILURE': (
        15,
        111,
    ),
    'SEED_LEN_SMALL': (
        10,
        110,
    ),
    'SEED_SOURCES_MUST_NOT_HAVE_A_PARENT': (
        57,
        229,
    ),
    'SELFTEST_FAILURE': (
        36,
        119,
    ),
    'SELF_TEST_KAT_FAILURE': (
        57,
        215,
    ),
    'SELF_TEST_POST_FAILURE': (
        57,
        216,
    ),
    'SENDER_GENERALNAME_TYPE_NOT_SUPPORTED': (
        58,
        150,
    ),
    'SEQUENCE_LENGTH_MISMATCH': (
        13,
        148,
    ),
    'SEQUENCE_NOT_CONSTRUCTED': (
        13,
        149,
    ),
    'SEQUENCE_OR_SET_NEEDS_CONFIG': (
        13,
        192,
    ),
    'SERVERHELLO_TLSEXT': (
        20,
        275,
    ),
    'SERVER_CANCELED_CONNECTION': (
        61,
        127,
    ),
    'SESSION_ID_CONTEXT_UNINITIALIZED': (
        20,
        277,
    ),
    'SETTING_MAC_ALGOR_FAILURE': (
        56,
        110,
    ),
    'SETTING_OWF_ALGOR_FAILURE': (
        56,
        111,
    ),
    'SETTING_XOF_FAILED': (
        6,
        227,
    ),
    'SET_DEFAULT_PROPERTY_FAILURE': (
        6,
        209,
    ),
    'SET_FILENAME_FAILED': (
        37,
        112,
    ),
    'SHARED_INFO_ERROR': (
        16,
        150,
    ),
    'SHORT_HEADER': (
        9,
        112,
    ),
    'SHORT_LINE': (
        13,
        150,
    ),
    'SHOULD_RETRY': (
        11,
        106,
    ),
    'SHUTDOWN_WHILE_IN_INIT': (
        20,
        407,
    ),
    'SIGNATURE_ALGORITHMS_ERROR': (
        20,
        360,
    ),
    'SIGNATURE_FAILURE': (
        47,
        109,
    ),
    'SIGNATURE_FOR_NON_SIGNING_CERTIFICATE': (
        20,
        220,
    ),
    'SIGNER_CERTIFICATE_NOT_FOUND': (
        33,
        128,
    ),
    'SIGNFINAL_ERROR': (
        46,
        139,
    ),
    'SIGNING_CTRL_FAILURE': (
        33,
        147,
    ),
    'SIGNING_NOT_SUPPORTED_FOR_THIS_KEY_TYPE': (
        33,
        148,
    ),
    'SIG_INVALID_MIME_TYPE': (
        13,
        213,
    ),
    'SLEN_CHECK_FAILED': (
        4,
        136,
    ),
    'SLEN_RECOVERY_FAILED': (
        4,
        135,
    ),
    'SLOT_FULL': (
        16,
        108,
    ),
    'SMIME_TEXT_ERROR': (
        33,
        129,
    ),
    'SOCK_NOT_SUPPORTED': (
        61,
        122,
    ),
    'SRP_A_CALC': (
        20,
        361,
    ),
    'SRTP_COULD_NOT_ALLOCATE_PROFILES': (
        20,
        362,
    ),
    'SRTP_PROTECTION_PROFILE_LIST_TOO_LONG': (
        20,
        363,
    ),
    'SRTP_UNKNOWN_PROTECTION_PROFILE': (
        20,
        364,
    ),
    'SRVCERT_DOES_NOT_VALIDATE_MSG': (
        58,
        151,
    ),
    'SSL3_EXT_INVALID_MAX_FRAGMENT_LENGTH': (
        20,
        232,
    ),
    'SSL3_EXT_INVALID_SERVERNAME': (
        20,
        319,
    ),
    'SSL3_EXT_INVALID_SERVERNAME_TYPE': (
        20,
        320,
    ),
    'SSL3_SESSION_ID_TOO_LONG': (
        20,
        300,
    ),
    'SSLV3_ALERT_BAD_CERTIFICATE': (
        20,
        1042,
    ),
    'SSLV3_ALERT_BAD_RECORD_MAC': (
        20,
        1020,
    ),
    'SSLV3_ALERT_CERTIFICATE_EXPIRED': (
        20,
        1045,
    ),
    'SSLV3_ALERT_CERTIFICATE_REVOKED': (
        20,
        1044,
    ),
    'SSLV3_ALERT_CERTIFICATE_UNKNOWN': (
        20,
        1046,
    ),
    'SSLV3_ALERT_DECOMPRESSION_FAILURE': (
        20,
        1030,
    ),
    'SSLV3_ALERT_HANDSHAKE_FAILURE': (
        20,
        1040,
    ),
    'SSLV3_ALERT_ILLEGAL_PARAMETER': (
        20,
        1047,
    ),
    'SSLV3_ALERT_NO_CERTIFICATE': (
        20,
        1041,
    ),
    'SSLV3_ALERT_UNEXPECTED_MESSAGE': (
        20,
        1010,
    ),
    'SSLV3_ALERT_UNSUPPORTED_CERTIFICATE': (
        20,
        1043,
    ),
    'SSLV3_ROLLBACK_ATTACK': (
        4,
        115,
    ),
    'SSL_COMMAND_SECTION_EMPTY': (
        20,
        117,
    ),
    'SSL_COMMAND_SECTION_NOT_FOUND': (
        20,
        125,
    ),
    'SSL_CTX_HAS_NO_DEFAULT_SSL_VERSION': (
        20,
        228,
    ),
    'SSL_HANDSHAKE_FAILURE': (
        20,
        229,
    ),
    'SSL_LIBRARY_HAS_NO_CIPHERS': (
        20,
        230,
    ),
    'SSL_NEGATIVE_LENGTH': (
        20,
        372,
    ),
    'SSL_SECTION_EMPTY': (
        20,
        126,
    ),
    'SSL_SECTION_NOT_FOUND': (
        20,
        136,
    ),
    'SSL_SESSION_ID_CALLBACK_FAILED': (
        20,
        301,
    ),
    'SSL_SESSION_ID_CONFLICT': (
        20,
        302,
    ),
    'SSL_SESSION_ID_CONTEXT_TOO_LONG': (
        20,
        273,
    ),
    'SSL_SESSION_ID_HAS_BAD_LENGTH': (
        20,
        303,
    ),
    'SSL_SESSION_ID_TOO_LONG': (
        20,
        408,
    ),
    'SSL_SESSION_VERSION_MISMATCH': (
        20,
        210,
    ),
    'STACK_ERROR': (
        37,
        105,
    ),
    'STATUS_CODE_UNSUPPORTED': (
        61,
        114,
    ),
    'STATUS_EXPIRED': (
        39,
        125,
    ),
    'STATUS_NOT_YET_VALID': (
        39,
        126,
    ),
    'STATUS_TOO_OLD': (
        39,
        127,
    ),
    'STILL_IN_INIT': (
        20,
        121,
    ),
    'STORE_INIT_ERROR': (
        46,
        141,
    ),
    'STREAMING_NOT_SUPPORTED': (
        13,
        202,
    ),
    'STRING_TOO_LONG': (
        55,
        109,
    ),
    'STRING_TOO_SHORT': (
        13,
        152,
    ),
    'SYM_FAILURE': (
        37,
        106,
    ),
    'SYSASSIGN_ERROR': (
        40,
        109,
    ),
    'SYSDASSGN_ERROR': (
        40,
        110,
    ),
    'SYSQIOW_ERROR': (
        40,
        111,
    ),
    'TAG_NOT_NEEDED': (
        57,
        120,
    ),
    'TAG_NOT_SET': (
        57,
        119,
    ),
    'THERE_MUST_BE_ONE_SIGNER': (
        47,
        110,
    ),
    'THE_ASN1_OBJECT_IDENTIFIER_IS_NOT_KNOWN_FOR_THIS_MD': (
        4,
        116,
    ),
    'TIME_NOT_ASCII_FORMAT': (
        13,
        193,
    ),
    'TIME_SYSCALL_ERROR': (
        47,
        122,
    ),
    'TLSV13_ALERT_CERTIFICATE_REQUIRED': (
        20,
        1116,
    ),
    'TLSV13_ALERT_MISSING_EXTENSION': (
        20,
        1109,
    ),
    'TLSV1_ALERT_ACCESS_DENIED': (
        20,
        1049,
    ),
    'TLSV1_ALERT_DECODE_ERROR': (
        20,
        1050,
    ),
    'TLSV1_ALERT_DECRYPTION_FAILED': (
        20,
        1021,
    ),
    'TLSV1_ALERT_DECRYPT_ERROR': (
        20,
        1051,
    ),
    'TLSV1_ALERT_EXPORT_RESTRICTION': (
        20,
        1060,
    ),
    'TLSV1_ALERT_INAPPROPRIATE_FALLBACK': (
        20,
        1086,
    ),
    'TLSV1_ALERT_INSUFFICIENT_SECURITY': (
        20,
        1071,
    ),
    'TLSV1_ALERT_INTERNAL_ERROR': (
        20,
        1080,
    ),
    'TLSV1_ALERT_NO_RENEGOTIATION': (
        20,
        1100,
    ),
    'TLSV1_ALERT_PROTOCOL_VERSION': (
        20,
        1070,
    ),
    'TLSV1_ALERT_RECORD_OVERFLOW': (
        20,
        1022,
    ),
    'TLSV1_ALERT_UNKNOWN_CA': (
        20,
        1048,
    ),
    'TLSV1_ALERT_USER_CANCELLED': (
        20,
        1090,
    ),
    'TLSV1_BAD_CERTIFICATE_HASH_VALUE': (
        20,
        1114,
    ),
    'TLSV1_BAD_CERTIFICATE_STATUS_RESPONSE': (
        20,
        1113,
    ),
    'TLSV1_CERTIFICATE_UNOBTAINABLE': (
        20,
        1111,
    ),
    'TLSV1_UNRECOGNIZED_NAME': (
        20,
        1112,
    ),
    'TLSV1_UNSUPPORTED_EXTENSION': (
        20,
        1110,
    ),
    'TLS_ILLEGAL_EXPORTER_LABEL': (
        20,
        367,
    ),
    'TLS_INVALID_ECPOINTFORMAT_LIST': (
        20,
        157,
    ),
    'TLS_NOT_ENABLED': (
        61,
        107,
    ),
    'TOKEN_NOT_PRESENT': (
        47,
        130,
    ),
    'TOKEN_PRESENT': (
        47,
        131,
    ),
    'TOO_LARGE': (
        13,
        223,
    ),
    'TOO_LITTLE_NONCE_REQUESTED': (
        36,
        135,
    ),
    'TOO_LONG': (
        13,
        155,
    ),
    'TOO_MANY_BYTES': (
        15,
        113,
    ),
    'TOO_MANY_ITERATIONS': (
        3,
        113,
    ),
    'TOO_MANY_KEY_UPDATES': (
        20,
        132,
    ),
    'TOO_MANY_RECORDS': (
        57,
        126,
    ),
    'TOO_MANY_REDIRECTIONS': (
        61,
        115,
    ),
    'TOO_MANY_RETRIES': (
        16,
        176,
    ),
    'TOO_MANY_TEMPORARY_VARIABLES': (
        3,
        109,
    ),
    'TOO_MANY_WARN_ALERTS': (
        20,
        409,
    ),
    'TOO_MUCH_EARLY_DATA': (
        20,
        164,
    ),
    'TOO_MUCH_NONCE_REQUESTED': (
        36,
        136,
    ),
    'TOO_SMALL': (
        13,
        224,
    ),
    'TOO_SMALL_BUFFER': (
        15,
        116,
    ),
    'TOTAL_TIMEOUT': (
        58,
        184,
    ),
    'TRAILING_CHARACTERS': (
        55,
        110,
    ),
    'TRANSACTIONID_UNMATCHED': (
        58,
        152,
    ),
    'TRANSFER_ERROR': (
        58,
        159,
    ),
    'TRANSFER_TIMEOUT': (
        32,
        105,
    ),
    'TSA_NAME_MISMATCH': (
        47,
        111,
    ),
    'TSA_UNTRUSTED': (
        47,
        112,
    ),
    'TST_INFO_SETUP_ERROR': (
        47,
        123,
    ),
    'TS_DATASIGN': (
        47,
        124,
    ),
    'TYPE_NOT_COMPRESSED_DATA': (
        46,
        142,
    ),
    'TYPE_NOT_CONSTRUCTED': (
        13,
        156,
    ),
    'TYPE_NOT_DATA': (
        46,
        143,
    ),
    'TYPE_NOT_DIGESTED_DATA': (
        46,
        144,
    ),
    'TYPE_NOT_ENCRYPTED_DATA': (
        46,
        145,
    ),
    'TYPE_NOT_ENVELOPED_DATA': (
        46,
        146,
    ),
    'TYPE_NOT_PRIMITIVE': (
        13,
        195,
    ),
    'UI_PROCESS_INTERRUPTED_OR_CANCELLED': (
        44,
        109,
    ),
    'UNABLE_TO_BIND_SOCKET': (
        32,
        117,
    ),
    'UNABLE_TO_CHECK_GENERATOR': (
        5,
        121,
    ),
    'UNABLE_TO_CREATE_DRBG': (
        36,
        143,
    ),
    'UNABLE_TO_CREATE_NEW_SECTION': (
        14,
        103,
    ),
    'UNABLE_TO_CREATE_SOCKET': (
        32,
        118,
    ),
    'UNABLE_TO_ENABLE_LOCKING': (
        6,
        212,
    ),
    'UNABLE_TO_FETCH_DRBG': (
        36,
        144,
    ),
    'UNABLE_TO_FINALIZE_CONTEXT': (
        46,
        147,
    ),
    'UNABLE_TO_FIND_CERTIFICATE': (
        33,
        106,
    ),
    'UNABLE_TO_FIND_CIPHERS': (
        57,
        207,
    ),
    'UNABLE_TO_FIND_ECDH_PARAMETERS': (
        20,
        314,
    ),
    'UNABLE_TO_FIND_MEM_BIO': (
        33,
        107,
    ),
    'UNABLE_TO_FIND_MESSAGE_DIGEST': (
        33,
        108,
    ),
    'UNABLE_TO_FIND_PARAMETERS_IN_CHAIN': (
        11,
        107,
    ),
    'UNABLE_TO_FIND_PUBLIC_KEY_PARAMETERS': (
        20,
        239,
    ),
    'UNABLE_TO_GET_CERTS_PUBLIC_KEY': (
        11,
        108,
    ),
    'UNABLE_TO_GET_ISSUER_DETAILS': (
        34,
        122,
    ),
    'UNABLE_TO_GET_ISSUER_KEYID': (
        34,
        123,
    ),
    'UNABLE_TO_GET_MAXIMUM_REQUEST_SIZE': (
        6,
        215,
    ),
    'UNABLE_TO_GET_PARENT_RESEED_PROP_COUNTER': (
        36,
        141,
    ),
    'UNABLE_TO_GET_PARENT_STRENGTH': (
        36,
        138,
    ),
    'UNABLE_TO_GET_PASSPHRASE': (
        57,
        159,
    ),
    'UNABLE_TO_GET_RANDOM_STRENGTH': (
        6,
        216,
    ),
    'UNABLE_TO_INITIALISE_CIPHERS': (
        57,
        208,
    ),
    'UNABLE_TO_KEEPALIVE': (
        32,
        137,
    ),
    'UNABLE_TO_LISTEN_SOCKET': (
        32,
        119,
    ),
    'UNABLE_TO_LOAD_SHA256': (
        57,
        147,
    ),
    'UNABLE_TO_LOAD_SSL3_MD5_ROUTINES': (
        20,
        242,
    ),
    'UNABLE_TO_LOAD_SSL3_SHA1_ROUTINES': (
        20,
        243,
    ),
    'UNABLE_TO_LOCK_CONTEXT': (
        6,
        211,
    ),
    'UNABLE_TO_LOCK_PARENT': (
        36,
        140,
    ),
    'UNABLE_TO_NODELAY': (
        32,
        138,
    ),
    'UNABLE_TO_RESEED': (
        57,
        204,
    ),
    'UNABLE_TO_REUSEADDR': (
        32,
        139,
    ),
    'UNABLE_TO_SET_CALLBACKS': (
        6,
        217,
    ),
    'UNACCEPTABLE_POLICY': (
        47,
        125,
    ),
    'UNAVAILABLE_IP_FAMILY': (
        32,
        145,
    ),
    'UNDEFINED_GENERATOR': (
        16,
        113,
    ),
    'UNDEFINED_ORDER': (
        16,
        128,
    ),
    'UNEXPECTED_CCS_MESSAGE': (
        20,
        262,
    ),
    'UNEXPECTED_CONTENT_TYPE': (
        61,
        118,
    ),
    'UNEXPECTED_DEK_IV': (
        9,
        130,
    ),
    'UNEXPECTED_END_OF_EARLY_DATA': (
        20,
        178,
    ),
    'UNEXPECTED_EOC': (
        13,
        159,
    ),
    'UNEXPECTED_EOF_WHILE_READING': (
        20,
        294,
    ),
    'UNEXPECTED_MESSAGE': (
        20,
        244,
    ),
    'UNEXPECTED_PKIBODY': (
        58,
        133,
    ),
    'UNEXPECTED_PKISTATUS': (
        58,
        185,
    ),
    'UNEXPECTED_PVNO': (
        58,
        153,
    ),
    'UNEXPECTED_RECORD': (
        20,
        245,
    ),
    'UNIMPLEMENTED_CIPHER': (
        38,
        146,
    ),
    'UNIMPLEMENTED_DIGEST': (
        38,
        147,
    ),
    'UNIMPLEMENTED_PUBLIC_KEY_METHOD': (
        38,
        101,
    ),
    'UNINITIALIZED': (
        20,
        276,
    ),
    'UNIVERSALSTRING_IS_WRONG_LENGTH': (
        13,
        215,
    ),
    'UNKNOWN_ALERT_TYPE': (
        20,
        246,
    ),
    'UNKNOWN_ALGORITHM_ID': (
        58,
        134,
    ),
    'UNKNOWN_ALGORITHM_TYPE': (
        4,
        117,
    ),
    'UNKNOWN_BIT_STRING_ARGUMENT': (
        34,
        111,
    ),
    'UNKNOWN_CERTIFICATE_TYPE': (
        20,
        247,
    ),
    'UNKNOWN_CERT_TYPE': (
        58,
        135,
    ),
    'UNKNOWN_CIPHER': (
        6,
        160,
    ),
    'UNKNOWN_CIPHER_RETURNED': (
        20,
        248,
    ),
    'UNKNOWN_CIPHER_TYPE': (
        20,
        249,
    ),
    'UNKNOWN_CMD_NAME': (
        20,
        386,
    ),
    'UNKNOWN_COFACTOR': (
        16,
        164,
    ),
    'UNKNOWN_COMMAND': (
        20,
        139,
    ),
    'UNKNOWN_CONTROL_COMMAND': (
        40,
        106,
    ),
    'UNKNOWN_DIGEST': (
        20,
        368,
    ),
    'UNKNOWN_DIGEST_ALGORITHM': (
        35,
        118,
    ),
    'UNKNOWN_DIGEST_TYPE': (
        33,
        109,
    ),
    'UNKNOWN_EXTENSION': (
        34,
        129,
    ),
    'UNKNOWN_EXTENSION_NAME': (
        34,
        130,
    ),
    'UNKNOWN_FORMAT': (
        13,
        160,
    ),
    'UNKNOWN_GROUP': (
        16,
        129,
    ),
    'UNKNOWN_ID': (
        46,
        150,
    ),
    'UNKNOWN_INFO_TYPE': (
        32,
        140,
    ),
    'UNKNOWN_KEY_EXCHANGE_TYPE': (
        20,
        250,
    ),
    'UNKNOWN_KEY_TYPE': (
        11,
        117,
    ),
    'UNKNOWN_MASK_DIGEST': (
        4,
        151,
    ),
    'UNKNOWN_MESSAGE_DIGEST': (
        39,
        119,
    ),
    'UNKNOWN_MESSAGE_DIGEST_ALGORITHM': (
        13,
        161,
    ),
    'UNKNOWN_MODULE_NAME': (
        14,
        113,
    ),
    'UNKNOWN_NAME_IN_RANDOM_SECTION': (
        15,
        120,
    ),
    'UNKNOWN_NID': (
        11,
        109,
    ),
    'UNKNOWN_OBJECT_NAME': (
        8,
        103,
    ),
    'UNKNOWN_OBJECT_TYPE': (
        13,
        162,
    ),
    'UNKNOWN_OPERATION': (
        33,
        110,
    ),
    'UNKNOWN_OPTION': (
        34,
        120,
    ),
    'UNKNOWN_ORDER': (
        16,
        114,
    ),
    'UNKNOWN_PADDING_TYPE': (
        4,
        118,
    ),
    'UNKNOWN_PBE_ALGORITHM': (
        6,
        121,
    ),
    'UNKNOWN_PKEY_TYPE': (
        20,
        251,
    ),
    'UNKNOWN_PKISTATUS': (
        58,
        186,
    ),
    'UNKNOWN_PROTOCOL': (
        20,
        252,
    ),
    'UNKNOWN_PUBLIC_KEY_TYPE': (
        13,
        163,
    ),
    'UNKNOWN_PURPOSE_ID': (
        11,
        121,
    ),
    'UNKNOWN_SIGID_ALGS': (
        11,
        144,
    ),
    'UNKNOWN_SIGNATURE_ALGORITHM': (
        13,
        199,
    ),
    'UNKNOWN_SSL_VERSION': (
        20,
        254,
    ),
    'UNKNOWN_STATE': (
        20,
        255,
    ),
    'UNKNOWN_TAG': (
        13,
        194,
    ),
    'UNKNOWN_TRUST_ID': (
        11,
        120,
    ),
    'UNKNOWN_TTYGET_ERRNO_VALUE': (
        40,
        108,
    ),
    'UNLOAD_FAILED': (
        37,
        107,
    ),
    'UNRECOGNIZED_SIGNATURE_NID': (
        50,
        101,
    ),
    'UNREGISTERED_SCHEME': (
        44,
        105,
    ),
    'UNSAFE_LEGACY_RENEGOTIATION_DISABLED': (
        20,
        338,
    ),
    'UNSOLICITED_EXTENSION': (
        20,
        217,
    ),
    'UNSUPPORTED': (
        37,
        108,
    ),
    'UNSUPPORTED_ALGORITHM': (
        11,
        111,
    ),
    'UNSUPPORTED_ANY_DEFINED_BY_TYPE': (
        13,
        164,
    ),
    'UNSUPPORTED_CEK_ALG': (
        57,
        145,
    ),
    'UNSUPPORTED_CIPHER': (
        9,
        113,
    ),
    'UNSUPPORTED_CIPHER_TYPE': (
        33,
        111,
    ),
    'UNSUPPORTED_COMPRESSION_ALGORITHM': (
        20,
        257,
    ),
    'UNSUPPORTED_CONTENT_ENCRYPTION_ALGORITHM': (
        46,
        194,
    ),
    'UNSUPPORTED_CONTENT_TYPE': (
        33,
        112,
    ),
    'UNSUPPORTED_DRBG_FLAGS': (
        36,
        132,
    ),
    'UNSUPPORTED_DRBG_TYPE': (
        36,
        120,
    ),
    'UNSUPPORTED_ELLIPTIC_CURVE': (
        20,
        315,
    ),
    'UNSUPPORTED_ENCRYPTION': (
        9,
        114,
    ),
    'UNSUPPORTED_ENCRYPTION_TYPE': (
        4,
        162,
    ),
    'UNSUPPORTED_ENTRY_TYPE': (
        50,
        102,
    ),
    'UNSUPPORTED_FIELD': (
        16,
        131,
    ),
    'UNSUPPORTED_IP_FAMILY': (
        32,
        146,
    ),
    'UNSUPPORTED_KEK_ALGORITHM': (
        46,
        153,
    ),
    'UNSUPPORTED_KEYLENGTH': (
        6,
        123,
    ),
    'UNSUPPORTED_KEY_COMPONENTS': (
        9,
        126,
    ),
    'UNSUPPORTED_KEY_DERIVATION_FUNCTION': (
        6,
        124,
    ),
    'UNSUPPORTED_KEY_ENCRYPTION_ALGORITHM': (
        46,
        179,
    ),
    'UNSUPPORTED_KEY_SIZE': (
        57,
        153,
    ),
    'UNSUPPORTED_KEY_TYPE': (
        6,
        224,
    ),
    'UNSUPPORTED_LABEL_SOURCE': (
        4,
        163,
    ),
    'UNSUPPORTED_MAC_TYPE': (
        57,
        137,
    ),
    'UNSUPPORTED_MASK_ALGORITHM': (
        4,
        153,
    ),
    'UNSUPPORTED_MASK_PARAMETER': (
        4,
        154,
    ),
    'UNSUPPORTED_MD_ALGORITHM': (
        47,
        126,
    ),
    'UNSUPPORTED_METHOD': (
        32,
        121,
    ),
    'UNSUPPORTED_METHOD_FOR_CREATING_POPO': (
        56,
        115,
    ),
    'UNSUPPORTED_NUMBER_OF_ROUNDS': (
        57,
        152,
    ),
    'UNSUPPORTED_OPERATION': (
        44,
        118,
    ),
    'UNSUPPORTED_OPTION': (
        34,
        117,
    ),
    'UNSUPPORTED_PKCS12_MODE': (
        35,
        119,
    ),
    'UNSUPPORTED_POPO_METHOD': (
        56,
        116,
    ),
    'UNSUPPORTED_PRF': (
        6,
        125,
    ),
    'UNSUPPORTED_PRIVATE_KEY_ALGORITHM': (
        6,
        118,
    ),
    'UNSUPPORTED_PROTECTION_ALG_DHBASEDMAC': (
        58,
        154,
    ),
    'UNSUPPORTED_PROTOCOL': (
        20,
        258,
    ),
    'UNSUPPORTED_PROTOCOL_FAMILY': (
        32,
        131,
    ),
    'UNSUPPORTED_PUBLIC_KEY_TYPE': (
        9,
        110,
    ),
    'UNSUPPORTED_RECIPIENTINFO_TYPE': (
        46,
        155,
    ),
    'UNSUPPORTED_RECIPIENT_TYPE': (
        46,
        154,
    ),
    'UNSUPPORTED_REQUESTORNAME_TYPE': (
        39,
        129,
    ),
    'UNSUPPORTED_SALT_TYPE': (
        6,
        126,
    ),
    'UNSUPPORTED_SEARCH_TYPE': (
        44,
        120,
    ),
    'UNSUPPORTED_SIGNATURE_TYPE': (
        4,
        155,
    ),
    'UNSUPPORTED_SSL_VERSION': (
        20,
        259,
    ),
    'UNSUPPORTED_STATUS_TYPE': (
        20,
        329,
    ),
    'UNSUPPORTED_TYPE': (
        34,
        167,
    ),
    'UNSUPPORTED_VERSION': (
        47,
        113,
    ),
    'UNWRAP_ERROR': (
        46,
        157,
    ),
    'UNWRAP_FAILURE': (
        46,
        180,
    ),
    'UPDATE_ERROR': (
        6,
        189,
    ),
    'URI_AUTHORITY_UNSUPPORTED': (
        57,
        223,
    ),
    'USER_DATA_DUPLICATION_UNSUPPORTED': (
        40,
        112,
    ),
    'USER_ID_TOO_LARGE': (
        53,
        106,
    ),
    'USER_TOO_LONG': (
        34,
        132,
    ),
    'USE_SRTP_NOT_NEGOTIATED': (
        20,
        369,
    ),
    'VALUE_ERROR': (
        57,
        138,
    ),
    'VALUE_MISSING': (
        4,
        147,
    ),
    'VALUE_TOO_LARGE': (
        58,
        175,
    ),
    'VALUE_TOO_SMALL': (
        58,
        177,
    ),
    'VARIABLE_EXPANSION_TOO_LONG': (
        14,
        116,
    ),
    'VARIABLE_HAS_NO_VALUE': (
        14,
        104,
    ),
    'VAR_BAD_VALUE': (
        47,
        135,
    ),
    'VAR_LOOKUP_FAILURE': (
        47,
        136,
    ),
    'VERIFICATION_FAILURE': (
        46,
        158,
    ),
    'VERSION_INCOMPATIBILITY': (
        38,
        145,
    ),
    'VERSION_TOO_HIGH': (
        20,
        166,
    ),
    'VERSION_TOO_LOW': (
        20,
        396,
    ),
    'WRAP_ERROR': (
        46,
        159,
    ),
    'WRAP_MODE_NOT_ALLOWED': (
        6,
        170,
    ),
    'WRITE_TO_READ_ONLY_BIO': (
        32,
        126,
    ),
    'WRONG_ALGORITHM_OID': (
        58,
        138,
    ),
    'WRONG_CERTID': (
        58,
        189,
    ),
    'WRONG_CERTID_IN_RP': (
        58,
        187,
    ),
    'WRONG_CERTIFICATE_TYPE': (
        20,
        383,
    ),
    'WRONG_CIPHER_RETURNED': (
        20,
        261,
    ),
    'WRONG_CONTENT_TYPE': (
        47,
        114,
    ),
    'WRONG_CURVE': (
        20,
        378,
    ),
    'WRONG_CURVE_PARAMETERS': (
        16,
        145,
    ),
    'WRONG_FINAL_BLOCK_LENGTH': (
        57,
        107,
    ),
    'WRONG_INTEGER_TYPE': (
        13,
        225,
    ),
    'WRONG_LOOKUP_TYPE': (
        11,
        112,
    ),
    'WRONG_ORDER': (
        16,
        130,
    ),
    'WRONG_OUTPUT_BUFFER_SIZE': (
        57,
        139,
    ),
    'WRONG_PBM_VALUE': (
        58,
        155,
    ),
    'WRONG_PKCS7_TYPE': (
        33,
        114,
    ),
    'WRONG_PUBLIC_KEY_TYPE': (
        13,
        200,
    ),
    'WRONG_RP_COMPONENT_COUNT': (
        58,
        188,
    ),
    'WRONG_SERIAL_IN_RP': (
        58,
        173,
    ),
    'WRONG_SIGNATURE_LENGTH': (
        20,
        264,
    ),
    'WRONG_SIGNATURE_SIZE': (
        20,
        265,
    ),
    'WRONG_SIGNATURE_TYPE': (
        20,
        370,
    ),
    'WRONG_SSL_VERSION': (
        20,
        266,
    ),
    'WRONG_TAG': (
        13,
        168,
    ),
    'WRONG_TYPE': (
        11,
        122,
    ),
    'WRONG_VERSION_NUMBER': (
        20,
        267,
    ),
    'WSASTARTUP': (
        32,
        122,
    ),
    'X509_LIB': (
        20,
        268,
    ),
    'X509_VERIFICATION_SETUP_PROBLEMS': (
        20,
        269,
    ),
    'XOF_DIGESTS_NOT_ALLOWED': (
        57,
        183,
    ),
    'XTS_DATA_UNIT_IS_TOO_LARGE': (
        57,
        148,
    ),
    'XTS_DUPLICATED_KEYS': (
        57,
        149,
    ),
    'ZERO_LENGTH_NUMBER': (
        15,
        115,
    ),
    'ZLIB_DEFLATE_ERROR': (
        41,
        99,
    ),
    'ZLIB_INFLATE_ERROR': (
        41,
        100,
    ),
    'ZLIB_NOT_SUPPORTED': (
        41,
        101,
    ),
}

lib_codes_to_names = {
    1: 'NONE',
    2: 'SYS',
    3: 'BN',
    4: 'RSA',
    5: 'DH',
    6: 'EVP',
    7: 'BUF',
    8: 'OBJ',
    9: 'PEM',
    10: 'DSA',
    11: 'X509',
    13: 'ASN1',
    14: 'CONF',
    15: 'CRYPTO',
    16: 'EC',
    20: 'SSL',
    23: 'OFFSET',
    32: 'BIO',
    33: 'PKCS7',
    34: 'X509V3',
    35: 'PKCS12',
    36: 'RAND',
    37: 'DSO',
    38: 'ENGINE',
    39: 'OCSP',
    40: 'UI',
    41: 'COMP',
    42: 'ECDSA',
    43: 'ECDH',
    44: 'OSSL_STORE',
    45: 'FIPS',
    46: 'CMS',
    47: 'TS',
    48: 'HMAC',
    50: 'CT',
    51: 'ASYNC',
    52: 'KDF',
    53: 'SM2',
    54: 'ESS',
    55: 'PROP',
    56: 'CRMF',
    57: 'PROV',
    58: 'CMP',
    59: 'OSSL_ENCODER',
    60: 'OSSL_DECODER',
    61: 'HTTP',
    128: 'USER',
    255: 'MASK',
}

OPENSSL_VERSION_INFO = (
    3,
    0,
    0,
    11,
    0,
)

_OPENSSL_API_VERSION = (
    3,
    0,
    0,
    11,
    0,
)

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924ac0>'

__spec__ = None # (!) real value is "ModuleSpec(name='_ssl', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924ac0>, origin='/usr/local/lib/python3.8/lib-dynload/_ssl.cpython-38-aarch64-linux-gnu.so')"

