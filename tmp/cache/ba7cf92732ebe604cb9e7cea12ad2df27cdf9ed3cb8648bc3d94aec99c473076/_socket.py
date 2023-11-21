# encoding: utf-8
# module _socket
# from /usr/local/lib/python3.8/lib-dynload/_socket.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
"""
Implementation module for socket operations.

See the socket module for documentation.
"""
# no imports

# Variables with simple values

AF_ALG = 38
AF_APPLETALK = 5
AF_ASH = 18
AF_ATMPVC = 8
AF_ATMSVC = 20
AF_AX25 = 3
AF_BLUETOOTH = 31
AF_BRIDGE = 7
AF_CAN = 29
AF_DECnet = 12
AF_ECONET = 19
AF_INET = 2
AF_INET6 = 10
AF_IPX = 4
AF_IRDA = 23
AF_KEY = 15
AF_LLC = 26
AF_NETBEUI = 13
AF_NETLINK = 16
AF_NETROM = 6
AF_PACKET = 17
AF_PPPOX = 24
AF_QIPCRTR = 42
AF_RDS = 21
AF_ROSE = 11
AF_ROUTE = 16
AF_SECURITY = 14
AF_SNA = 22
AF_TIPC = 30
AF_UNIX = 1
AF_UNSPEC = 0
AF_VSOCK = 40
AF_WANPIPE = 25
AF_X25 = 9

AI_ADDRCONFIG = 32
AI_ALL = 16
AI_CANONNAME = 2
AI_NUMERICHOST = 4
AI_NUMERICSERV = 1024
AI_PASSIVE = 1
AI_V4MAPPED = 8

ALG_OP_DECRYPT = 0
ALG_OP_ENCRYPT = 1
ALG_OP_SIGN = 2
ALG_OP_VERIFY = 3

ALG_SET_AEAD_ASSOCLEN = 4
ALG_SET_AEAD_AUTHSIZE = 5

ALG_SET_IV = 2
ALG_SET_KEY = 1
ALG_SET_OP = 3
ALG_SET_PUBKEY = 6

BDADDR_ANY = '00:00:00:00:00:00'
BDADDR_LOCAL = '00:00:00:FF:FF:FF'

BTPROTO_HCI = 1
BTPROTO_L2CAP = 0
BTPROTO_RFCOMM = 3
BTPROTO_SCO = 2

CAN_BCM = 2

CAN_BCM_CAN_FD_FRAME = 2048

CAN_BCM_RX_ANNOUNCE_RESUME = 256

CAN_BCM_RX_CHANGED = 12

CAN_BCM_RX_CHECK_DLC = 64

CAN_BCM_RX_DELETE = 6

CAN_BCM_RX_FILTER_ID = 32

CAN_BCM_RX_NO_AUTOTIMER = 128

CAN_BCM_RX_READ = 7

CAN_BCM_RX_RTR_FRAME = 1024

CAN_BCM_RX_SETUP = 5
CAN_BCM_RX_STATUS = 10
CAN_BCM_RX_TIMEOUT = 11

CAN_BCM_SETTIMER = 1
CAN_BCM_STARTTIMER = 2

CAN_BCM_TX_ANNOUNCE = 8
CAN_BCM_TX_COUNTEVT = 4

CAN_BCM_TX_CP_CAN_ID = 16

CAN_BCM_TX_DELETE = 2
CAN_BCM_TX_EXPIRED = 9
CAN_BCM_TX_READ = 3

CAN_BCM_TX_RESET_MULTI_IDX = 512

CAN_BCM_TX_SEND = 4
CAN_BCM_TX_SETUP = 1
CAN_BCM_TX_STATUS = 8

CAN_EFF_FLAG = 2147483648
CAN_EFF_MASK = 536870911

CAN_ERR_FLAG = 536870912
CAN_ERR_MASK = 536870911

CAN_ISOTP = 6
CAN_RAW = 1

CAN_RAW_ERR_FILTER = 2

CAN_RAW_FD_FRAMES = 5

CAN_RAW_FILTER = 1
CAN_RAW_LOOPBACK = 3

CAN_RAW_RECV_OWN_MSGS = 4

CAN_RTR_FLAG = 1073741824

CAN_SFF_MASK = 2047

EAI_ADDRFAMILY = -9
EAI_AGAIN = -3
EAI_BADFLAGS = -1
EAI_FAIL = -4
EAI_FAMILY = -6
EAI_MEMORY = -10
EAI_NODATA = -5
EAI_NONAME = -2
EAI_OVERFLOW = -12
EAI_SERVICE = -8
EAI_SOCKTYPE = -7
EAI_SYSTEM = -11

has_ipv6 = True

HCI_DATA_DIR = 1

HCI_FILTER = 2

HCI_TIME_STAMP = 3

INADDR_ALLHOSTS_GROUP = 3758096385

INADDR_ANY = 0
INADDR_BROADCAST = 4294967295
INADDR_LOOPBACK = 2130706433

INADDR_MAX_LOCAL_GROUP = 3758096639

INADDR_NONE = 4294967295

INADDR_UNSPEC_GROUP = 3758096384

IOCTL_VM_SOCKETS_GET_LOCAL_CID = 1977

IPPORT_RESERVED = 1024
IPPORT_USERRESERVED = 5000

IPPROTO_AH = 51
IPPROTO_DSTOPTS = 60
IPPROTO_EGP = 8
IPPROTO_ESP = 50
IPPROTO_FRAGMENT = 44
IPPROTO_GRE = 47
IPPROTO_HOPOPTS = 0
IPPROTO_ICMP = 1
IPPROTO_ICMPV6 = 58
IPPROTO_IDP = 22
IPPROTO_IGMP = 2
IPPROTO_IP = 0
IPPROTO_IPIP = 4
IPPROTO_IPV6 = 41
IPPROTO_NONE = 59
IPPROTO_PIM = 103
IPPROTO_PUP = 12
IPPROTO_RAW = 255
IPPROTO_ROUTING = 43
IPPROTO_RSVP = 46
IPPROTO_SCTP = 132
IPPROTO_TCP = 6
IPPROTO_TP = 29
IPPROTO_UDP = 17

IPV6_CHECKSUM = 7
IPV6_DONTFRAG = 62
IPV6_DSTOPTS = 59
IPV6_HOPLIMIT = 52
IPV6_HOPOPTS = 54

IPV6_JOIN_GROUP = 20

IPV6_LEAVE_GROUP = 21

IPV6_MULTICAST_HOPS = 18
IPV6_MULTICAST_IF = 17
IPV6_MULTICAST_LOOP = 19

IPV6_NEXTHOP = 9
IPV6_PATHMTU = 61
IPV6_PKTINFO = 50
IPV6_RECVDSTOPTS = 58
IPV6_RECVHOPLIMIT = 51
IPV6_RECVHOPOPTS = 53
IPV6_RECVPATHMTU = 60
IPV6_RECVPKTINFO = 49
IPV6_RECVRTHDR = 56
IPV6_RECVTCLASS = 66
IPV6_RTHDR = 57
IPV6_RTHDRDSTOPTS = 55

IPV6_RTHDR_TYPE_0 = 0

IPV6_TCLASS = 67

IPV6_UNICAST_HOPS = 16

IPV6_V6ONLY = 26

IP_ADD_MEMBERSHIP = 35

IP_DEFAULT_MULTICAST_LOOP = 1
IP_DEFAULT_MULTICAST_TTL = 1

IP_DROP_MEMBERSHIP = 36

IP_HDRINCL = 3

IP_MAX_MEMBERSHIPS = 20

IP_MULTICAST_IF = 32
IP_MULTICAST_LOOP = 34
IP_MULTICAST_TTL = 33

IP_OPTIONS = 4
IP_RECVOPTS = 6
IP_RECVRETOPTS = 7
IP_RETOPTS = 7
IP_TOS = 1
IP_TRANSPARENT = 19
IP_TTL = 2

MSG_CMSG_CLOEXEC = 1073741824

MSG_CONFIRM = 2048
MSG_CTRUNC = 8
MSG_DONTROUTE = 4
MSG_DONTWAIT = 64
MSG_EOR = 128
MSG_ERRQUEUE = 8192
MSG_FASTOPEN = 536870912
MSG_MORE = 32768
MSG_NOSIGNAL = 16384
MSG_OOB = 1
MSG_PEEK = 2
MSG_TRUNC = 32
MSG_WAITALL = 256

NETLINK_CRYPTO = 21
NETLINK_DNRTMSG = 14
NETLINK_FIREWALL = 3

NETLINK_IP6_FW = 13

NETLINK_NFLOG = 5
NETLINK_ROUTE = 0
NETLINK_USERSOCK = 2
NETLINK_XFRM = 6

NI_DGRAM = 16
NI_MAXHOST = 1025
NI_MAXSERV = 32
NI_NAMEREQD = 8
NI_NOFQDN = 4
NI_NUMERICHOST = 1
NI_NUMERICSERV = 2

PACKET_BROADCAST = 1
PACKET_FASTROUTE = 6
PACKET_HOST = 0
PACKET_LOOPBACK = 5
PACKET_MULTICAST = 2
PACKET_OTHERHOST = 3
PACKET_OUTGOING = 4

PF_CAN = 29
PF_PACKET = 17
PF_RDS = 21

SCM_CREDENTIALS = 2
SCM_RIGHTS = 1

SHUT_RD = 0
SHUT_RDWR = 2
SHUT_WR = 1

SOCK_CLOEXEC = 524288
SOCK_DGRAM = 2
SOCK_NONBLOCK = 2048
SOCK_RAW = 3
SOCK_RDM = 4
SOCK_SEQPACKET = 5
SOCK_STREAM = 1

SOL_ALG = 279

SOL_CAN_BASE = 100
SOL_CAN_RAW = 101

SOL_HCI = 0
SOL_IP = 0
SOL_RDS = 276
SOL_SOCKET = 1
SOL_TCP = 6
SOL_TIPC = 271
SOL_UDP = 17

SOMAXCONN = 4096
SO_ACCEPTCONN = 30
SO_BINDTODEVICE = 25
SO_BROADCAST = 6
SO_DEBUG = 1
SO_DOMAIN = 39
SO_DONTROUTE = 5
SO_ERROR = 4
SO_KEEPALIVE = 9
SO_LINGER = 13
SO_MARK = 36
SO_OOBINLINE = 10
SO_PASSCRED = 16
SO_PASSSEC = 34
SO_PEERCRED = 17
SO_PEERSEC = 31
SO_PRIORITY = 12
SO_PROTOCOL = 38
SO_RCVBUF = 8
SO_RCVLOWAT = 18
SO_RCVTIMEO = 20
SO_REUSEADDR = 2
SO_REUSEPORT = 15
SO_SNDBUF = 7
SO_SNDLOWAT = 19
SO_SNDTIMEO = 21
SO_TYPE = 3

SO_VM_SOCKETS_BUFFER_MAX_SIZE = 2

SO_VM_SOCKETS_BUFFER_MIN_SIZE = 1

SO_VM_SOCKETS_BUFFER_SIZE = 0

TCP_CONGESTION = 13
TCP_CORK = 3

TCP_DEFER_ACCEPT = 9

TCP_FASTOPEN = 23
TCP_INFO = 11
TCP_KEEPCNT = 6
TCP_KEEPIDLE = 4
TCP_KEEPINTVL = 5
TCP_LINGER2 = 8
TCP_MAXSEG = 2
TCP_NODELAY = 1

TCP_NOTSENT_LOWAT = 25

TCP_QUICKACK = 12
TCP_SYNCNT = 7

TCP_USER_TIMEOUT = 18

TCP_WINDOW_CLAMP = 10

TIPC_ADDR_ID = 3
TIPC_ADDR_NAME = 2
TIPC_ADDR_NAMESEQ = 1

TIPC_CFG_SRV = 0

TIPC_CLUSTER_SCOPE = 2

TIPC_CONN_TIMEOUT = 130

TIPC_CRITICAL_IMPORTANCE = 3

TIPC_DEST_DROPPABLE = 129

TIPC_HIGH_IMPORTANCE = 2

TIPC_IMPORTANCE = 127

TIPC_LOW_IMPORTANCE = 0

TIPC_MEDIUM_IMPORTANCE = 1

TIPC_NODE_SCOPE = 3

TIPC_PUBLISHED = 1

TIPC_SRC_DROPPABLE = 128

TIPC_SUBSCR_TIMEOUT = 3

TIPC_SUB_CANCEL = 4
TIPC_SUB_PORTS = 1
TIPC_SUB_SERVICE = 2

TIPC_TOP_SRV = 1

TIPC_WAIT_FOREVER = -1

TIPC_WITHDRAWN = 2

TIPC_ZONE_SCOPE = 1

VMADDR_CID_ANY = 4294967295
VMADDR_CID_HOST = 2

VMADDR_PORT_ANY = 4294967295

VM_SOCKETS_INVALID_VERSION = 4294967295

# functions

def close(integer): # real signature unknown; restored from __doc__
    """
    close(integer) -> None
    
    Close an integer socket file descriptor.  This is like os.close(), but for
    sockets; on some platforms os.close() won't work for socket file descriptors.
    """
    pass

def CMSG_LEN(length): # real signature unknown; restored from __doc__
    """
    CMSG_LEN(length) -> control message length
    
    Return the total length, without trailing padding, of an ancillary
    data item with associated data of the given length.  This value can
    often be used as the buffer size for recvmsg() to receive a single
    item of ancillary data, but RFC 3542 requires portable applications to
    use CMSG_SPACE() and thus include space for padding, even when the
    item will be the last in the buffer.  Raises OverflowError if length
    is outside the permissible range of values.
    """
    pass

def CMSG_SPACE(length): # real signature unknown; restored from __doc__
    """
    CMSG_SPACE(length) -> buffer size
    
    Return the buffer size needed for recvmsg() to receive an ancillary
    data item with associated data of the given length, along with any
    trailing padding.  The buffer space needed to receive multiple items
    is the sum of the CMSG_SPACE() values for their associated data
    lengths.  Raises OverflowError if length is outside the permissible
    range of values.
    """
    pass

def dup(integer): # real signature unknown; restored from __doc__
    """
    dup(integer) -> integer
    
    Duplicate an integer socket file descriptor.  This is like os.dup(), but for
    sockets; on some platforms os.dup() won't work for socket file descriptors.
    """
    return 0

def getaddrinfo(host, port, family=None, type=None, proto=None, flags=None): # real signature unknown; restored from __doc__
    """
    getaddrinfo(host, port [, family, type, proto, flags])
        -> list of (family, type, proto, canonname, sockaddr)
    
    Resolve host and port into addrinfo struct.
    """
    return []

def getdefaulttimeout(): # real signature unknown; restored from __doc__
    """
    getdefaulttimeout() -> timeout
    
    Returns the default timeout in seconds (float) for new socket objects.
    A value of None indicates that new socket objects have no timeout.
    When the socket module is first imported, the default is None.
    """
    return timeout

def gethostbyaddr(host): # real signature unknown; restored from __doc__
    """
    gethostbyaddr(host) -> (name, aliaslist, addresslist)
    
    Return the true host name, a list of aliases, and a list of IP addresses,
    for a host.  The host argument is a string giving a host name or IP number.
    """
    pass

def gethostbyname(host): # real signature unknown; restored from __doc__
    """
    gethostbyname(host) -> address
    
    Return the IP address (a string of the form '255.255.255.255') for a host.
    """
    pass

def gethostbyname_ex(host): # real signature unknown; restored from __doc__
    """
    gethostbyname_ex(host) -> (name, aliaslist, addresslist)
    
    Return the true host name, a list of aliases, and a list of IP addresses,
    for a host.  The host argument is a string giving a host name or IP number.
    """
    pass

def gethostname(): # real signature unknown; restored from __doc__
    """
    gethostname() -> string
    
    Return the current host name.
    """
    return ""

def getnameinfo(sockaddr, flags): # real signature unknown; restored from __doc__
    """
    getnameinfo(sockaddr, flags) --> (host, port)
    
    Get host and port for a sockaddr.
    """
    pass

def getprotobyname(name): # real signature unknown; restored from __doc__
    """
    getprotobyname(name) -> integer
    
    Return the protocol number for the named protocol.  (Rarely used.)
    """
    return 0

def getservbyname(servicename, protocolname=None): # real signature unknown; restored from __doc__
    """
    getservbyname(servicename[, protocolname]) -> integer
    
    Return a port number from a service name and protocol name.
    The optional protocol name, if given, should be 'tcp' or 'udp',
    otherwise any protocol will match.
    """
    return 0

def getservbyport(port, protocolname=None): # real signature unknown; restored from __doc__
    """
    getservbyport(port[, protocolname]) -> string
    
    Return the service name from a port number and protocol name.
    The optional protocol name, if given, should be 'tcp' or 'udp',
    otherwise any protocol will match.
    """
    return ""

def htonl(integer): # real signature unknown; restored from __doc__
    """
    htonl(integer) -> integer
    
    Convert a 32-bit integer from host to network byte order.
    """
    return 0

def htons(integer): # real signature unknown; restored from __doc__
    """
    htons(integer) -> integer
    
    Convert a 16-bit unsigned integer from host to network byte order.
    Note that in case the received integer does not fit in 16-bit unsigned
    integer, but does fit in a positive C int, it is silently truncated to
    16-bit unsigned integer.
    However, this silent truncation feature is deprecated, and will raise an
    exception in future versions of Python.
    """
    return 0

def if_indextoname(if_index): # real signature unknown; restored from __doc__
    """
    if_indextoname(if_index)
    
    Returns the interface name corresponding to the interface index if_index.
    """
    pass

def if_nameindex(): # real signature unknown; restored from __doc__
    """
    if_nameindex()
    
    Returns a list of network interface information (index, name) tuples.
    """
    pass

def if_nametoindex(if_name): # real signature unknown; restored from __doc__
    """
    if_nametoindex(if_name)
    
    Returns the interface index corresponding to the interface name if_name.
    """
    pass

def inet_aton(string): # real signature unknown; restored from __doc__
    """
    inet_aton(string) -> bytes giving packed 32-bit IP representation
    
    Convert an IP address in string format (123.45.67.89) to the 32-bit packed
    binary format used in low-level network functions.
    """
    return b""

def inet_ntoa(packed_ip): # real signature unknown; restored from __doc__
    """
    inet_ntoa(packed_ip) -> ip_address_string
    
    Convert an IP address from 32-bit packed binary format to string format
    """
    pass

def inet_ntop(af, packed_ip): # real signature unknown; restored from __doc__
    """
    inet_ntop(af, packed_ip) -> string formatted IP address
    
    Convert a packed IP address of the given family to string format.
    """
    return ""

def inet_pton(af, ip): # real signature unknown; restored from __doc__
    """
    inet_pton(af, ip) -> packed IP address string
    
    Convert an IP address from string format to a packed string suitable
    for use with low-level network functions.
    """
    pass

def ntohl(integer): # real signature unknown; restored from __doc__
    """
    ntohl(integer) -> integer
    
    Convert a 32-bit integer from network to host byte order.
    """
    return 0

def ntohs(integer): # real signature unknown; restored from __doc__
    """
    ntohs(integer) -> integer
    
    Convert a 16-bit unsigned integer from network to host byte order.
    Note that in case the received integer does not fit in 16-bit unsigned
    integer, but does fit in a positive C int, it is silently truncated to
    16-bit unsigned integer.
    However, this silent truncation feature is deprecated, and will raise an
    exception in future versions of Python.
    """
    return 0

def setdefaulttimeout(timeout): # real signature unknown; restored from __doc__
    """
    setdefaulttimeout(timeout)
    
    Set the default timeout in seconds (float) for new socket objects.
    A value of None indicates that new socket objects have no timeout.
    When the socket module is first imported, the default is None.
    """
    pass

def sethostname(name): # real signature unknown; restored from __doc__
    """
    sethostname(name)
    
    Sets the hostname to name.
    """
    pass

def socketpair(family=None, type=None, proto=None): # real signature unknown; restored from __doc__
    """
    socketpair([family[, type [, proto]]]) -> (socket object, socket object)
    
    Create a pair of socket objects from the sockets returned by the platform
    socketpair() function.
    The arguments are the same as for socket() except the default family is
    AF_UNIX if defined on the platform; otherwise, the default is AF_INET.
    """
    pass

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



class gaierror(OSError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class herror(OSError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class SocketType(object):
    """
    socket(family=AF_INET, type=SOCK_STREAM, proto=0) -> socket object
    socket(family=-1, type=-1, proto=-1, fileno=None) -> socket object
    
    Open a socket of the given type.  The family argument specifies the
    address family; it defaults to AF_INET.  The type argument specifies
    whether this is a stream (SOCK_STREAM, this is the default)
    or datagram (SOCK_DGRAM) socket.  The protocol argument defaults to 0,
    specifying the default protocol.  Keyword arguments are accepted.
    The socket is created as non-inheritable.
    
    When a fileno is passed in, family, type and proto are auto-detected,
    unless they are explicitly set.
    
    A socket object represents one endpoint of a network connection.
    
    Methods of socket objects (keyword arguments not allowed):
    
    _accept() -- accept connection, returning new socket fd and client address
    bind(addr) -- bind the socket to a local address
    close() -- close the socket
    connect(addr) -- connect the socket to a remote address
    connect_ex(addr) -- connect, return an error code instead of an exception
    dup() -- return a new socket fd duplicated from fileno()
    fileno() -- return underlying file descriptor
    getpeername() -- return remote address [*]
    getsockname() -- return local address
    getsockopt(level, optname[, buflen]) -- get socket options
    gettimeout() -- return timeout or None
    listen([n]) -- start listening for incoming connections
    recv(buflen[, flags]) -- receive data
    recv_into(buffer[, nbytes[, flags]]) -- receive data (into a buffer)
    recvfrom(buflen[, flags]) -- receive data and sender's address
    recvfrom_into(buffer[, nbytes, [, flags])
      -- receive data and sender's address (into a buffer)
    sendall(data[, flags]) -- send all data
    send(data[, flags]) -- send data, may not send all of it
    sendto(data[, flags], addr) -- send data to a given address
    setblocking(0 | 1) -- set or clear the blocking I/O flag
    getblocking() -- return True if socket is blocking, False if non-blocking
    setsockopt(level, optname, value[, optlen]) -- set socket options
    settimeout(None | float) -- set or clear the timeout
    shutdown(how) -- shut down traffic in one or both directions
    if_nameindex() -- return all network interface indices and names
    if_nametoindex(name) -- return the corresponding interface index
    if_indextoname(index) -- return the corresponding interface name
    
     [*] not available on all platforms!
    """
    def bind(self, address): # real signature unknown; restored from __doc__
        """
        bind(address)
        
        Bind the socket to a local address.  For IP sockets, the address is a
        pair (host, port); the host must refer to the local host. For raw packet
        sockets the address is a tuple (ifname, proto [,pkttype [,hatype [,addr]]])
        """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """
        close()
        
        Close the socket.  It cannot be used after this call.
        """
        pass

    def connect(self, address): # real signature unknown; restored from __doc__
        """
        connect(address)
        
        Connect the socket to a remote address.  For IP sockets, the address
        is a pair (host, port).
        """
        pass

    def connect_ex(self, address): # real signature unknown; restored from __doc__
        """
        connect_ex(address) -> errno
        
        This is like connect(address), but returns an error code (the errno value)
        instead of raising an exception when an error occurs.
        """
        pass

    def detach(self): # real signature unknown; restored from __doc__
        """
        detach()
        
        Close the socket object without closing the underlying file descriptor.
        The object cannot be used after this call, but the file descriptor
        can be reused for other purposes.  The file descriptor is returned.
        """
        pass

    def fileno(self): # real signature unknown; restored from __doc__
        """
        fileno() -> integer
        
        Return the integer file descriptor of the socket.
        """
        return 0

    def getblocking(self): # real signature unknown; restored from __doc__
        """
        getblocking()
        
        Returns True if socket is in blocking mode, or False if it
        is in non-blocking mode.
        """
        pass

    def getpeername(self): # real signature unknown; restored from __doc__
        """
        getpeername() -> address info
        
        Return the address of the remote endpoint.  For IP sockets, the address
        info is a pair (hostaddr, port).
        """
        pass

    def getsockname(self): # real signature unknown; restored from __doc__
        """
        getsockname() -> address info
        
        Return the address of the local endpoint. The format depends on the
        address family. For IPv4 sockets, the address info is a pair
        (hostaddr, port).
        """
        pass

    def getsockopt(self, level, option, buffersize=None): # real signature unknown; restored from __doc__
        """
        getsockopt(level, option[, buffersize]) -> value
        
        Get a socket option.  See the Unix manual for level and option.
        If a nonzero buffersize argument is given, the return value is a
        string of that length; otherwise it is an integer.
        """
        pass

    def gettimeout(self): # real signature unknown; restored from __doc__
        """
        gettimeout() -> timeout
        
        Returns the timeout in seconds (float) associated with socket
        operations. A timeout of None indicates that timeouts on socket
        operations are disabled.
        """
        return timeout

    def listen(self, backlog=None): # real signature unknown; restored from __doc__
        """
        listen([backlog])
        
        Enable a server to accept connections.  If backlog is specified, it must be
        at least 0 (if it is lower, it is set to 0); it specifies the number of
        unaccepted connections that the system will allow before refusing new
        connections. If not specified, a default reasonable value is chosen.
        """
        pass

    def recv(self, buffersize, flags=None): # real signature unknown; restored from __doc__
        """
        recv(buffersize[, flags]) -> data
        
        Receive up to buffersize bytes from the socket.  For the optional flags
        argument, see the Unix manual.  When no data is available, block until
        at least one byte is available or until the remote end is closed.  When
        the remote end is closed and all data is read, return the empty string.
        """
        pass

    def recvfrom(self, buffersize, flags=None): # real signature unknown; restored from __doc__
        """
        recvfrom(buffersize[, flags]) -> (data, address info)
        
        Like recv(buffersize, flags) but also return the sender's address info.
        """
        pass

    def recvfrom_into(self, buffer, nbytes=None, flags=None): # real signature unknown; restored from __doc__
        """
        recvfrom_into(buffer[, nbytes[, flags]]) -> (nbytes, address info)
        
        Like recv_into(buffer[, nbytes[, flags]]) but also return the sender's address info.
        """
        pass

    def recvmsg(self, bufsize, ancbufsize=None, flags=None): # real signature unknown; restored from __doc__
        """
        recvmsg(bufsize[, ancbufsize[, flags]]) -> (data, ancdata, msg_flags, address)
        
        Receive normal data (up to bufsize bytes) and ancillary data from the
        socket.  The ancbufsize argument sets the size in bytes of the
        internal buffer used to receive the ancillary data; it defaults to 0,
        meaning that no ancillary data will be received.  Appropriate buffer
        sizes for ancillary data can be calculated using CMSG_SPACE() or
        CMSG_LEN(), and items which do not fit into the buffer might be
        truncated or discarded.  The flags argument defaults to 0 and has the
        same meaning as for recv().
        
        The return value is a 4-tuple: (data, ancdata, msg_flags, address).
        The data item is a bytes object holding the non-ancillary data
        received.  The ancdata item is a list of zero or more tuples
        (cmsg_level, cmsg_type, cmsg_data) representing the ancillary data
        (control messages) received: cmsg_level and cmsg_type are integers
        specifying the protocol level and protocol-specific type respectively,
        and cmsg_data is a bytes object holding the associated data.  The
        msg_flags item is the bitwise OR of various flags indicating
        conditions on the received message; see your system documentation for
        details.  If the receiving socket is unconnected, address is the
        address of the sending socket, if available; otherwise, its value is
        unspecified.
        
        If recvmsg() raises an exception after the system call returns, it
        will first attempt to close any file descriptors received via the
        SCM_RIGHTS mechanism.
        """
        pass

    def recvmsg_into(self, buffers, ancbufsize=None, flags=None): # real signature unknown; restored from __doc__
        """
        recvmsg_into(buffers[, ancbufsize[, flags]]) -> (nbytes, ancdata, msg_flags, address)
        
        Receive normal data and ancillary data from the socket, scattering the
        non-ancillary data into a series of buffers.  The buffers argument
        must be an iterable of objects that export writable buffers
        (e.g. bytearray objects); these will be filled with successive chunks
        of the non-ancillary data until it has all been written or there are
        no more buffers.  The ancbufsize argument sets the size in bytes of
        the internal buffer used to receive the ancillary data; it defaults to
        0, meaning that no ancillary data will be received.  Appropriate
        buffer sizes for ancillary data can be calculated using CMSG_SPACE()
        or CMSG_LEN(), and items which do not fit into the buffer might be
        truncated or discarded.  The flags argument defaults to 0 and has the
        same meaning as for recv().
        
        The return value is a 4-tuple: (nbytes, ancdata, msg_flags, address).
        The nbytes item is the total number of bytes of non-ancillary data
        written into the buffers.  The ancdata item is a list of zero or more
        tuples (cmsg_level, cmsg_type, cmsg_data) representing the ancillary
        data (control messages) received: cmsg_level and cmsg_type are
        integers specifying the protocol level and protocol-specific type
        respectively, and cmsg_data is a bytes object holding the associated
        data.  The msg_flags item is the bitwise OR of various flags
        indicating conditions on the received message; see your system
        documentation for details.  If the receiving socket is unconnected,
        address is the address of the sending socket, if available; otherwise,
        its value is unspecified.
        
        If recvmsg_into() raises an exception after the system call returns,
        it will first attempt to close any file descriptors received via the
        SCM_RIGHTS mechanism.
        """
        pass

    def recv_into(self, buffer, nbytes=None, flags=None): # real signature unknown; restored from __doc__
        """
        recv_into(buffer, [nbytes[, flags]]) -> nbytes_read
        
        A version of recv() that stores its data into a buffer rather than creating
        a new string.  Receive up to buffersize bytes from the socket.  If buffersize
        is not specified (or 0), receive up to the size available in the given buffer.
        
        See recv() for documentation about the flags.
        """
        pass

    def send(self, data, flags=None): # real signature unknown; restored from __doc__
        """
        send(data[, flags]) -> count
        
        Send a data string to the socket.  For the optional flags
        argument, see the Unix manual.  Return the number of bytes
        sent; this may be less than len(data) if the network is busy.
        """
        pass

    def sendall(self, data, flags=None): # real signature unknown; restored from __doc__
        """
        sendall(data[, flags])
        
        Send a data string to the socket.  For the optional flags
        argument, see the Unix manual.  This calls send() repeatedly
        until all data is sent.  If an error occurs, it's impossible
        to tell how much data has been sent.
        """
        pass

    def sendmsg(self, buffers, ancdata=None, flags=None, address=None): # real signature unknown; restored from __doc__
        """
        sendmsg(buffers[, ancdata[, flags[, address]]]) -> count
        
        Send normal and ancillary data to the socket, gathering the
        non-ancillary data from a series of buffers and concatenating it into
        a single message.  The buffers argument specifies the non-ancillary
        data as an iterable of bytes-like objects (e.g. bytes objects).
        The ancdata argument specifies the ancillary data (control messages)
        as an iterable of zero or more tuples (cmsg_level, cmsg_type,
        cmsg_data), where cmsg_level and cmsg_type are integers specifying the
        protocol level and protocol-specific type respectively, and cmsg_data
        is a bytes-like object holding the associated data.  The flags
        argument defaults to 0 and has the same meaning as for send().  If
        address is supplied and not None, it sets a destination address for
        the message.  The return value is the number of bytes of non-ancillary
        data sent.
        """
        pass

    def sendmsg_afalg(self, msg=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        sendmsg_afalg([msg], *, op[, iv[, assoclen[, flags=MSG_MORE]]])
        
        Set operation mode, IV and length of associated data for an AF_ALG
        operation socket.
        """
        pass

    def sendto(self, data, flags=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        sendto(data[, flags], address) -> count
        
        Like send(data, flags) but allows specifying the destination address.
        For IP sockets, the address is a pair (hostaddr, port).
        """
        pass

    def setblocking(self, flag): # real signature unknown; restored from __doc__
        """
        setblocking(flag)
        
        Set the socket to blocking (flag is true) or non-blocking (false).
        setblocking(True) is equivalent to settimeout(None);
        setblocking(False) is equivalent to settimeout(0.0).
        """
        pass

    def setsockopt(self, level, option, value): # real signature unknown; restored from __doc__
        """
        setsockopt(level, option, value: int)
        setsockopt(level, option, value: buffer)
        setsockopt(level, option, None, optlen: int)
        
        Set a socket option.  See the Unix manual for level and option.
        The value argument can either be an integer, a string buffer, or
        None, optlen.
        """
        pass

    def settimeout(self, timeout): # real signature unknown; restored from __doc__
        """
        settimeout(timeout)
        
        Set a timeout on socket operations.  'timeout' can be a float,
        giving in seconds, or None.  Setting a timeout of None disables
        the timeout feature and is equivalent to setblocking(1).
        Setting a timeout of zero is the same as setblocking(0).
        """
        pass

    def shutdown(self, flag): # real signature unknown; restored from __doc__
        """
        shutdown(flag)
        
        Shut down the reading side of the socket (flag == SHUT_RD), the writing side
        of the socket (flag == SHUT_WR), or both ends (flag == SHUT_RDWR).
        """
        pass

    def _accept(self): # real signature unknown; restored from __doc__
        """
        _accept() -> (integer, address info)
        
        Wait for an incoming connection.  Return a new socket file descriptor
        representing the connection, and the address of the client.
        For IP sockets, the address info is a pair (hostaddr, port).
        """
        pass

    def __del__(self, *args, **kwargs): # real signature unknown
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    family = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the socket family"""

    proto = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the socket protocol"""

    timeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the socket timeout"""

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the socket type"""



socket = SocketType


class timeout(OSError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

CAPI = None # (!) real value is '<capsule object "_socket.CAPI" at 0xffffacb6d150>'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffffacb6d520>'

__spec__ = None # (!) real value is "ModuleSpec(name='_socket', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffffacb6d520>, origin='/usr/local/lib/python3.8/lib-dynload/_socket.cpython-38-aarch64-linux-gnu.so')"

