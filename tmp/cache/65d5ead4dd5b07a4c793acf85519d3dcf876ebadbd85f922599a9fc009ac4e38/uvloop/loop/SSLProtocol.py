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

class SSLProtocol(object):
    """
    SSLProtocol(loop, app_protocol, sslcontext, waiter, server_side=False, server_hostname=None, call_connection_made=True, ssl_handshake_timeout=None, ssl_shutdown_timeout=None)
    SSL protocol.
    
        Implementation of SSL on top of a socket using incoming and outgoing
        buffers which are ssl.MemoryBIO objects.
    """
    def buffer_updated(self, nbytes): # real signature unknown; restored from __doc__
        """ SSLProtocol.buffer_updated(self, nbytes) """
        pass

    def connection_lost(self, exc): # real signature unknown; restored from __doc__
        """
        SSLProtocol.connection_lost(self, exc)
        Called when the low-level connection is lost or closed.
        
                The argument is an exception object or None (the latter
                meaning a regular EOF is received or the connection was
                aborted or closed).
        """
        pass

    def connection_made(self, transport): # real signature unknown; restored from __doc__
        """
        SSLProtocol.connection_made(self, transport)
        Called when the low-level connection is made.
        
                Start the SSL handshake.
        """
        pass

    def eof_received(self): # real signature unknown; restored from __doc__
        """
        SSLProtocol.eof_received(self)
        Called when the other end of the low-level stream
                is half-closed.
        
                If this returns a false value (including None), the transport
                will close itself.  If it returns a true value, closing the
                transport is up to the protocol.
        """
        pass

    def get_buffer(self, n): # real signature unknown; restored from __doc__
        """ SSLProtocol.get_buffer(self, n) """
        pass

    def pause_writing(self): # real signature unknown; restored from __doc__
        """
        SSLProtocol.pause_writing(self)
        Called when the low-level transport's buffer goes over
                the high-water mark.
        """
        pass

    def resume_writing(self): # real signature unknown; restored from __doc__
        """
        SSLProtocol.resume_writing(self)
        Called when the low-level transport's buffer drains below
                the low-water mark.
        """
        pass

    def _get_app_transport(self, context=None): # real signature unknown; restored from __doc__
        """ SSLProtocol._get_app_transport(self, context=None) """
        pass

    def __init__(self, loop, app_protocol, sslcontext, waiter, server_side=False, server_hostname=None, call_connection_made=True, ssl_handshake_timeout=None, ssl_shutdown_timeout=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ SSLProtocol.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ SSLProtocol.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0xffffabb267e0>'


