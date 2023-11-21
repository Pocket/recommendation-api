# encoding: utf-8
# module uvloop.loop
# from /.venv/lib/python3.8/site-packages/uvloop/loop.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import uvloop._noop as _noop # /.venv/lib/python3.8/site-packages/uvloop/_noop.py
import gc as gc # <module 'gc' (built-in)>
import stat as stat # /usr/local/lib/python3.8/stat.py
import sys as sys # <module 'sys' (built-in)>
import enum as enum # /usr/local/lib/python3.8/enum.py
import asyncio as asyncio # /usr/local/lib/python3.8/asyncio/__init__.py
import asyncio.protocols as __asyncio_protocols
import enum as __enum
import _asyncio as ___asyncio


from .object import object

class Loop(object):
    """ Loop() """
    def add_reader(self, fileobj, callback, *args): # real signature unknown; restored from __doc__
        """
        Loop.add_reader(self, fileobj, callback, *args)
        Add a reader callback.
        """
        pass

    def add_signal_handler(self, sig, callback, *args): # real signature unknown; restored from __doc__
        """
        Loop.add_signal_handler(self, sig, callback, *args)
        Add a handler for a signal.  UNIX only.
        
                Raise ValueError if the signal number is invalid or uncatchable.
                Raise RuntimeError if there is a problem setting up the handler.
        """
        pass

    def add_writer(self, fileobj, callback, *args): # real signature unknown; restored from __doc__
        """
        Loop.add_writer(self, fileobj, callback, *args)
        Add a writer callback..
        """
        pass

    def call_at(self, when, callback, *args, context=None): # real signature unknown; restored from __doc__
        """
        Loop.call_at(self, when, callback, *args, context=None)
        Like call_later(), but uses an absolute time.
        
                Absolute time corresponds to the event loop's time() method.
        """
        pass

    def call_exception_handler(self, context): # real signature unknown; restored from __doc__
        """
        Loop.call_exception_handler(self, context)
        Call the current event loop's exception handler.
        
                The context argument is a dict containing the following keys:
        
                - 'message': Error message;
                - 'exception' (optional): Exception object;
                - 'future' (optional): Future instance;
                - 'handle' (optional): Handle instance;
                - 'protocol' (optional): Protocol instance;
                - 'transport' (optional): Transport instance;
                - 'socket' (optional): Socket instance.
        
                New keys maybe introduced in the future.
        
                Note: do not overload this method in an event loop subclass.
                For custom exception handling, use the
                `set_exception_handler()` method.
        """
        pass

    def call_later(self, delay, callback, *args, context=None): # real signature unknown; restored from __doc__
        """
        Loop.call_later(self, delay, callback, *args, context=None)
        Arrange for a callback to be called at a given time.
        
                Return a Handle: an opaque object with a cancel() method that
                can be used to cancel the call.
        
                The delay can be an int or float, expressed in seconds.  It is
                always relative to the current time.
        
                Each callback will be called exactly once.  If two callbacks
                are scheduled for exactly the same time, it undefined which
                will be called first.
        
                Any positional arguments after the callback will be passed to
                the callback when it is called.
        """
        pass

    def call_soon(self, callback, *args, context=None): # real signature unknown; restored from __doc__
        """
        Loop.call_soon(self, callback, *args, context=None)
        Arrange for a callback to be called as soon as possible.
        
                This operates as a FIFO queue: callbacks are called in the
                order in which they are registered.  Each callback will be
                called exactly once.
        
                Any positional arguments after the callback will be passed to
                the callback when it is called.
        """
        pass

    def call_soon_threadsafe(self, callback, *args, context=None): # real signature unknown; restored from __doc__
        """
        Loop.call_soon_threadsafe(self, callback, *args, context=None)
        Like call_soon(), but thread-safe.
        """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """
        Loop.close(self)
        Close the event loop.
        
                The event loop must not be running.
        
                This is idempotent and irreversible.
        
                No other methods should be called after this one.
        """
        pass

    def connect_accepted_socket(self, protocol_factory, sock, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Loop.connect_accepted_socket(self, protocol_factory, sock, *, ssl=None, ssl_handshake_timeout=None, ssl_shutdown_timeout=None)
        Handle an accepted connection.
        
                This is used by servers that accept connections outside of
                asyncio but that use asyncio to handle connections.
        
                This method is a coroutine.  When completed, the coroutine
                returns a (transport, protocol) pair.
        """
        pass

    def connect_read_pipe(self, proto_factory, pipe): # real signature unknown; restored from __doc__
        """
        Loop.connect_read_pipe(self, proto_factory, pipe)
        Register read pipe in event loop. Set the pipe to non-blocking mode.
        
                protocol_factory should instantiate object with Protocol interface.
                pipe is a file-like object.
                Return pair (transport, protocol), where transport supports the
                ReadTransport interface.
        """
        pass

    def connect_write_pipe(self, proto_factory, pipe): # real signature unknown; restored from __doc__
        """
        Loop.connect_write_pipe(self, proto_factory, pipe)
        Register write pipe in event loop.
        
                protocol_factory should instantiate object with BaseProtocol interface.
                Pipe is file-like object already switched to nonblocking.
                Return pair (transport, protocol), where transport support
                WriteTransport interface.
        """
        pass

    def create_connection(self, protocol_factory, host=None, port=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Loop.create_connection(self, protocol_factory, host=None, port=None, *, ssl=None, family=0, proto=0, flags=0, sock=None, local_addr=None, server_hostname=None, ssl_handshake_timeout=None, ssl_shutdown_timeout=None)
        Connect to a TCP server.
        
                Create a streaming transport connection to a given Internet host and
                port: socket family AF_INET or socket.AF_INET6 depending on host (or
                family if specified), socket type SOCK_STREAM. protocol_factory must be
                a callable returning a protocol instance.
        
                This method is a coroutine which will try to establish the connection
                in the background.  When successful, the coroutine returns a
                (transport, protocol) pair.
        """
        pass

    def create_datagram_endpoint(self, protocol_factory, local_addr=None, remote_addr=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Loop.create_datagram_endpoint(self, protocol_factory, local_addr=None, remote_addr=None, *, family=0, proto=0, flags=0, reuse_address=_unset, reuse_port=None, allow_broadcast=None, sock=None)
        A coroutine which creates a datagram endpoint.
        
                This method will try to establish the endpoint in the background.
                When successful, the coroutine returns a (transport, protocol) pair.
        
                protocol_factory must be a callable returning a protocol instance.
        
                socket family AF_INET or socket.AF_INET6 depending on host (or
                family if specified), socket type SOCK_DGRAM.
        
                reuse_port tells the kernel to allow this endpoint to be bound to
                the same port as other existing endpoints are bound to, so long as
                they all set this flag when being created. This option is not
                supported on Windows and some UNIX's. If the
                :py:data:`~socket.SO_REUSEPORT` constant is not defined then this
                capability is unsupported.
        
                allow_broadcast tells the kernel to allow this endpoint to send
                messages to the broadcast address.
        
                sock can optionally be specified in order to use a preexisting
                socket object.
        """
        pass

    def create_future(self): # real signature unknown; restored from __doc__
        """
        Loop.create_future(self)
        Create a Future object attached to the loop.
        """
        pass

    def create_server(self, protocol_factory, host=None, port=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Loop.create_server(self, protocol_factory, host=None, port=None, *, int family=uv.AF_UNSPEC, int flags=uv.AI_PASSIVE, sock=None, backlog=100, ssl=None, reuse_address=None, reuse_port=None, ssl_handshake_timeout=None, ssl_shutdown_timeout=None, start_serving=True)
        A coroutine which creates a TCP server bound to host and port.
        
                The return value is a Server object which can be used to stop
                the service.
        
                If host is an empty string or None all interfaces are assumed
                and a list of multiple sockets will be returned (most likely
                one for IPv4 and another one for IPv6). The host parameter can also be
                a sequence (e.g. list) of hosts to bind to.
        
                family can be set to either AF_INET or AF_INET6 to force the
                socket to use IPv4 or IPv6. If not set it will be determined
                from host (defaults to AF_UNSPEC).
        
                flags is a bitmask for getaddrinfo().
        
                sock can optionally be specified in order to use a preexisting
                socket object.
        
                backlog is the maximum number of queued connections passed to
                listen() (defaults to 100).
        
                ssl can be set to an SSLContext to enable SSL over the
                accepted connections.
        
                reuse_address tells the kernel to reuse a local socket in
                TIME_WAIT state, without waiting for its natural timeout to
                expire. If not specified will automatically be set to True on
                UNIX.
        
                reuse_port tells the kernel to allow this endpoint to be bound to
                the same port as other existing endpoints are bound to, so long as
                they all set this flag when being created. This option is not
                supported on Windows.
        
                ssl_handshake_timeout is the time in seconds that an SSL server
                will wait for completion of the SSL handshake before aborting the
                connection. Default is 60s.
        
                ssl_shutdown_timeout is the time in seconds that an SSL server
                will wait for completion of the SSL shutdown before aborting the
                connection. Default is 30s.
        """
        pass

    def create_task(self, coro, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Loop.create_task(self, coro, *, name=None, context=None)
        Schedule a coroutine object.
        
                Return a task object.
        
                If name is not None, task.set_name(name) will be called if the task
                object has the set_name attribute, true for default Task in Python 3.8.
        
                An optional keyword-only context argument allows specifying a custom
                contextvars.Context for the coro to run in. The current context copy is
                created when no context is provided.
        """
        pass

    def create_unix_connection(self, protocol_factory, path=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ Loop.create_unix_connection(self, protocol_factory, path=None, *, ssl=None, sock=None, server_hostname=None, ssl_handshake_timeout=None, ssl_shutdown_timeout=None) """
        pass

    def create_unix_server(self, protocol_factory, path=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Loop.create_unix_server(self, protocol_factory, path=None, *, backlog=100, sock=None, ssl=None, ssl_handshake_timeout=None, ssl_shutdown_timeout=None, start_serving=True)
        A coroutine which creates a UNIX Domain Socket server.
        
                The return value is a Server object, which can be used to stop
                the service.
        
                path is a str, representing a file systsem path to bind the
                server socket to.
        
                sock can optionally be specified in order to use a preexisting
                socket object.
        
                backlog is the maximum number of queued connections passed to
                listen() (defaults to 100).
        
                ssl can be set to an SSLContext to enable SSL over the
                accepted connections.
        
                ssl_handshake_timeout is the time in seconds that an SSL server
                will wait for completion of the SSL handshake before aborting the
                connection. Default is 60s.
        
                ssl_shutdown_timeout is the time in seconds that an SSL server
                will wait for completion of the SSL shutdown before aborting the
                connection. Default is 30s.
        """
        pass

    def default_exception_handler(self, context): # real signature unknown; restored from __doc__
        """
        Loop.default_exception_handler(self, context)
        Default exception handler.
        
                This is called when an exception occurs and no exception
                handler is set, and can be called by a custom exception
                handler that wants to defer to the default behavior.
        
                The context parameter has the same meaning as in
                `call_exception_handler()`.
        """
        pass

    def getaddrinfo(self, host, port, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ Loop.getaddrinfo(self, host, port, *, int family=0, int type=0, int proto=0, int flags=0) """
        pass

    def getnameinfo(self, sockaddr, int_flags=0): # real signature unknown; restored from __doc__
        """ Loop.getnameinfo(self, sockaddr, int flags=0) """
        pass

    def get_debug(self): # real signature unknown; restored from __doc__
        """ Loop.get_debug(self) """
        pass

    def get_exception_handler(self): # real signature unknown; restored from __doc__
        """
        Loop.get_exception_handler(self)
        Return an exception handler, or None if the default one is in use.
        """
        pass

    def get_task_factory(self): # real signature unknown; restored from __doc__
        """
        Loop.get_task_factory(self)
        Return a task factory, or None if the default one is in use.
        """
        pass

    def is_closed(self): # real signature unknown; restored from __doc__
        """
        Loop.is_closed(self)
        Returns True if the event loop was closed.
        """
        pass

    def is_running(self): # real signature unknown; restored from __doc__
        """
        Loop.is_running(self)
        Return whether the event loop is currently running.
        """
        pass

    def remove_reader(self, fileobj): # real signature unknown; restored from __doc__
        """
        Loop.remove_reader(self, fileobj)
        Remove a reader callback.
        """
        pass

    def remove_signal_handler(self, sig): # real signature unknown; restored from __doc__
        """
        Loop.remove_signal_handler(self, sig)
        Remove a handler for a signal.  UNIX only.
        
                Return True if a signal handler was removed, False if not.
        """
        pass

    def remove_writer(self, fileobj): # real signature unknown; restored from __doc__
        """
        Loop.remove_writer(self, fileobj)
        Remove a writer callback.
        """
        pass

    def run_forever(self): # real signature unknown; restored from __doc__
        """
        Loop.run_forever(self)
        Run the event loop until stop() is called.
        """
        pass

    def run_in_executor(self, executor, func, *args): # real signature unknown; restored from __doc__
        """ Loop.run_in_executor(self, executor, func, *args) """
        pass

    def run_until_complete(self, future): # real signature unknown; restored from __doc__
        """
        Loop.run_until_complete(self, future)
        Run until the Future is done.
        
                If the argument is a coroutine, it is wrapped in a Task.
        
                WARNING: It would be disastrous to call run_until_complete()
                with the same coroutine twice -- it would wrap it in two
                different Tasks and that can't be good.
        
                Return the Future's result, or raise its exception.
        """
        pass

    def set_debug(self, enabled): # real signature unknown; restored from __doc__
        """ Loop.set_debug(self, enabled) """
        pass

    def set_default_executor(self, executor): # real signature unknown; restored from __doc__
        """ Loop.set_default_executor(self, executor) """
        pass

    def set_exception_handler(self, handler): # real signature unknown; restored from __doc__
        """
        Loop.set_exception_handler(self, handler)
        Set handler as the new event loop exception handler.
        
                If handler is None, the default exception handler will
                be set.
        
                If handler is a callable object, it should have a
                signature matching '(loop, context)', where 'loop'
                will be a reference to the active event loop, 'context'
                will be a dict object (see `call_exception_handler()`
                documentation for details about context).
        """
        pass

    def set_task_factory(self, factory): # real signature unknown; restored from __doc__
        """
        Loop.set_task_factory(self, factory)
        Set a task factory that will be used by loop.create_task().
        
                If factory is None the default task factory will be set.
        
                If factory is a callable, it should have a signature matching
                '(loop, coro)', where 'loop' will be a reference to the active
                event loop, 'coro' will be a coroutine object.  The callable
                must return a Future.
        """
        pass

    def shutdown_asyncgens(self): # real signature unknown; restored from __doc__
        """
        Loop.shutdown_asyncgens(self)
        Shutdown all active asynchronous generators.
        """
        pass

    def shutdown_default_executor(self): # real signature unknown; restored from __doc__
        """
        Loop.shutdown_default_executor(self)
        Schedule the shutdown of the default executor.
        """
        pass

    def sock_accept(self, sock): # real signature unknown; restored from __doc__
        """
        Loop.sock_accept(self, sock)
        Accept a connection.
        
                The socket must be bound to an address and listening for connections.
                The return value is a pair (conn, address) where conn is a new socket
                object usable to send and receive data on the connection, and address
                is the address bound to the socket on the other end of the connection.
        
                This method is a coroutine.
        """
        pass

    def sock_connect(self, sock, address): # real signature unknown; restored from __doc__
        """
        Loop.sock_connect(self, sock, address)
        Connect to a remote socket at address.
        
                This method is a coroutine.
        """
        pass

    def sock_recv(self, sock, n): # real signature unknown; restored from __doc__
        """
        Loop.sock_recv(self, sock, n)
        Receive data from the socket.
        
                The return value is a bytes object representing the data received.
                The maximum amount of data to be received at once is specified by
                nbytes.
        
                This method is a coroutine.
        """
        pass

    def sock_recvfrom(self, sock, bufsize): # real signature unknown; restored from __doc__
        """ Loop.sock_recvfrom(self, sock, bufsize) """
        pass

    def sock_recvfrom_into(self, sock, buf, nbytes=0): # real signature unknown; restored from __doc__
        """ Loop.sock_recvfrom_into(self, sock, buf, nbytes=0) """
        pass

    def sock_recv_into(self, sock, buf): # real signature unknown; restored from __doc__
        """
        Loop.sock_recv_into(self, sock, buf)
        Receive data from the socket.
        
                The received data is written into *buf* (a writable buffer).
                The return value is the number of bytes written.
        
                This method is a coroutine.
        """
        pass

    def sock_sendall(self, sock, data): # real signature unknown; restored from __doc__
        """
        Loop.sock_sendall(self, sock, data)
        Send data to the socket.
        
                The socket must be connected to a remote socket. This method continues
                to send data from data until either all data has been sent or an
                error occurs. None is returned on success. On error, an exception is
                raised, and there is no way to determine how much data, if any, was
                successfully processed by the receiving end of the connection.
        
                This method is a coroutine.
        """
        pass

    def sock_sendto(self, sock, data, address): # real signature unknown; restored from __doc__
        """ Loop.sock_sendto(self, sock, data, address) """
        pass

    def start_tls(self, transport, protocol, sslcontext, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Loop.start_tls(self, transport, protocol, sslcontext, *, server_side=False, server_hostname=None, ssl_handshake_timeout=None, ssl_shutdown_timeout=None)
        Upgrade transport to TLS.
        
                Return a new transport that *protocol* should start using
                immediately.
        """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """
        Loop.stop(self)
        Stop running the event loop.
        
                Every callback already scheduled will still run.  This simply informs
                run_forever to stop looping after a complete iteration.
        """
        pass

    def subprocess_exec(self, protocol_factory, program, *args, shell=False, **kwargs): # real signature unknown; restored from __doc__
        """ Loop.subprocess_exec(self, protocol_factory, program, *args, shell=False, **kwargs) """
        pass

    def subprocess_shell(self, protocol_factory, cmd, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ Loop.subprocess_shell(self, protocol_factory, cmd, *, shell=True, **kwargs) """
        pass

    def time(self): # real signature unknown; restored from __doc__
        """
        Loop.time(self)
        Return the time according to the event loop's clock.
        
                This is a float expressed in seconds since an epoch, but the
                epoch, precision, accuracy and drift are unspecified and may
                differ per event loop.
        """
        pass

    def _asyncgen_finalizer_hook(self, agen): # real signature unknown; restored from __doc__
        """ Loop._asyncgen_finalizer_hook(self, agen) """
        pass

    def _asyncgen_firstiter_hook(self, agen): # real signature unknown; restored from __doc__
        """ Loop._asyncgen_firstiter_hook(self, agen) """
        pass

    def _check_default_executor(self): # real signature unknown; restored from __doc__
        """ Loop._check_default_executor(self) """
        pass

    def _do_shutdown(self, future): # real signature unknown; restored from __doc__
        """ Loop._do_shutdown(self, future) """
        pass

    def _get_backend_id(self): # real signature unknown; restored from __doc__
        """
        Loop._get_backend_id(self)
        This method is used by uvloop tests and is not part of the API.
        """
        pass

    def _monitor_fs(self, unicode_path, callback): # real signature unknown; restored from __doc__
        """ Loop._monitor_fs(self, unicode path: str, callback) -> asyncio.Handle """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Loop.__reduce_cython__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Loop.__setstate_cython__(self, __pyx_state) """
        pass

    def __sighandler(self, signum, frame): # real signature unknown; restored from __doc__
        """ Loop.__sighandler(self, signum, frame) """
        pass

    def __subprocess_run(self, protocol_factory, args, stdin=None, stdout=None, stderr=None, universal_newlines=False, shell=True, bufsize=0, preexec_fn=None, close_fds=None, cwd=None, env=None, startupinfo=None, creationflags=0, restore_signals=True, start_new_session=False, executable=None, pass_fds=(), __uvloop_sleep_after_fork=False): # real signature unknown; restored from __doc__
        """ Loop.__subprocess_run(self, protocol_factory, args, stdin=subprocess_PIPE, stdout=subprocess_PIPE, stderr=subprocess_PIPE, universal_newlines=False, shell=True, bufsize=0, preexec_fn=None, close_fds=None, cwd=None, env=None, startupinfo=None, creationflags=0, restore_signals=True, start_new_session=False, executable=None, pass_fds=(), __uvloop_sleep_after_fork=False) """
        pass

    print_debug_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    slow_callback_duration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """slow_callback_duration: object"""

    _closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _debug_cb_handles_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _debug_cb_handles_total = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _debug_cb_timer_handles_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _debug_cb_timer_handles_total = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _debug_cc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _debug_exception_handler_cnt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _debug_handles_closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _debug_handles_current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _debug_handles_total = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _debug_stream_listen_errors_total = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _debug_stream_read_cb_errors_total = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _debug_stream_read_cb_total = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _debug_stream_read_eof_cb_errors_total = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _debug_stream_read_eof_total = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _debug_stream_read_errors_total = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _debug_stream_shutdown_errors_total = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _debug_stream_write_cb_errors_total = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _debug_stream_write_ctx_cnt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _debug_stream_write_ctx_total = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _debug_stream_write_errors_total = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _debug_stream_write_tries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _debug_uv_handles_freed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _debug_uv_handles_total = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _poll_read_cb_errors_total = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _poll_read_events_total = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _poll_write_cb_errors_total = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _poll_write_events_total = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _sock_try_write_total = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0xffffabb261b0>'


