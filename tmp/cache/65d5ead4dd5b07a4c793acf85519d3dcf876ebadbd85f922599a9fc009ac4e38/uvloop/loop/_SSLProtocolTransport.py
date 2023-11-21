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

class _SSLProtocolTransport(object):
    # no doc
    def abort(self): # real signature unknown; restored from __doc__
        """
        _SSLProtocolTransport.abort(self)
        Close the transport immediately.
        
                Buffered data will be lost.  No more data will be received.
                The protocol's connection_lost() method will (eventually) be
                called with None as its argument.
        """
        pass

    def can_write_eof(self): # real signature unknown; restored from __doc__
        """
        _SSLProtocolTransport.can_write_eof(self)
        Return True if this transport supports write_eof(), False if not.
        """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """
        _SSLProtocolTransport.close(self)
        Close the transport.
        
                Buffered data will be flushed asynchronously.  No more data
                will be received.  After all buffered data is flushed, the
                protocol's connection_lost() method will (eventually) called
                with None as its argument.
        """
        pass

    def get_extra_info(self, name, default=None): # real signature unknown; restored from __doc__
        """
        _SSLProtocolTransport.get_extra_info(self, name, default=None)
        Get optional transport information.
        """
        pass

    def get_protocol(self): # real signature unknown; restored from __doc__
        """ _SSLProtocolTransport.get_protocol(self) """
        pass

    def get_read_buffer_limits(self): # real signature unknown; restored from __doc__
        """ _SSLProtocolTransport.get_read_buffer_limits(self) """
        pass

    def get_read_buffer_size(self): # real signature unknown; restored from __doc__
        """
        _SSLProtocolTransport.get_read_buffer_size(self)
        Return the current size of the read buffer.
        """
        pass

    def get_write_buffer_limits(self): # real signature unknown; restored from __doc__
        """ _SSLProtocolTransport.get_write_buffer_limits(self) """
        pass

    def get_write_buffer_size(self): # real signature unknown; restored from __doc__
        """
        _SSLProtocolTransport.get_write_buffer_size(self)
        Return the current size of the write buffers.
        """
        pass

    def is_closing(self): # real signature unknown; restored from __doc__
        """ _SSLProtocolTransport.is_closing(self) """
        pass

    def is_reading(self): # real signature unknown; restored from __doc__
        """ _SSLProtocolTransport.is_reading(self) """
        pass

    def pause_reading(self): # real signature unknown; restored from __doc__
        """
        _SSLProtocolTransport.pause_reading(self)
        Pause the receiving end.
        
                No data will be passed to the protocol's data_received()
                method until resume_reading() is called.
        """
        pass

    def resume_reading(self): # real signature unknown; restored from __doc__
        """
        _SSLProtocolTransport.resume_reading(self)
        Resume the receiving end.
        
                Data received will once again be passed to the protocol's
                data_received() method.
        """
        pass

    def set_protocol(self, protocol): # real signature unknown; restored from __doc__
        """ _SSLProtocolTransport.set_protocol(self, protocol) """
        pass

    def set_read_buffer_limits(self, high=None, low=None): # real signature unknown; restored from __doc__
        """
        _SSLProtocolTransport.set_read_buffer_limits(self, high=None, low=None)
        Set the high- and low-water limits for read flow control.
        
                These two values control when to call the upstream transport's
                pause_reading() and resume_reading() methods.  If specified,
                the low-water limit must be less than or equal to the
                high-water limit.  Neither value can be negative.
        
                The defaults are implementation-specific.  If only the
                high-water limit is given, the low-water limit defaults to an
                implementation-specific value less than or equal to the
                high-water limit.  Setting high to zero forces low to zero as
                well, and causes pause_reading() to be called whenever the
                buffer becomes non-empty.  Setting low to zero causes
                resume_reading() to be called only once the buffer is empty.
                Use of zero for either limit is generally sub-optimal as it
                reduces opportunities for doing I/O and computation
                concurrently.
        """
        pass

    def set_write_buffer_limits(self, high=None, low=None): # real signature unknown; restored from __doc__
        """
        _SSLProtocolTransport.set_write_buffer_limits(self, high=None, low=None)
        Set the high- and low-water limits for write flow control.
        
                These two values control when to call the protocol's
                pause_writing() and resume_writing() methods.  If specified,
                the low-water limit must be less than or equal to the
                high-water limit.  Neither value can be negative.
        
                The defaults are implementation-specific.  If only the
                high-water limit is given, the low-water limit defaults to an
                implementation-specific value less than or equal to the
                high-water limit.  Setting high to zero forces low to zero as
                well, and causes pause_writing() to be called whenever the
                buffer becomes non-empty.  Setting low to zero causes
                resume_writing() to be called only once the buffer is empty.
                Use of zero for either limit is generally sub-optimal as it
                reduces opportunities for doing I/O and computation
                concurrently.
        """
        pass

    def write(self, data): # real signature unknown; restored from __doc__
        """
        _SSLProtocolTransport.write(self, data)
        Write some data bytes to the transport.
        
                This does not block; it buffers the data and arranges for it
                to be sent out asynchronously.
        """
        pass

    def writelines(self, list_of_data): # real signature unknown; restored from __doc__
        """
        _SSLProtocolTransport.writelines(self, list_of_data)
        Write a list (or any iterable) of data bytes to the transport.
        
                The default implementation concatenates the arguments and
                calls write() on the result.
        """
        pass

    def write_eof(self): # real signature unknown; restored from __doc__
        """
        _SSLProtocolTransport.write_eof(self)
        Close the write end after flushing buffered data.
        
                This raises :exc:`NotImplementedError` right now.
        """
        pass

    def _force_close(self, exc): # real signature unknown; restored from __doc__
        """ _SSLProtocolTransport._force_close(self, exc) """
        pass

    def _test__append_write_backlog(self, data): # real signature unknown; restored from __doc__
        """ _SSLProtocolTransport._test__append_write_backlog(self, data) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ _SSLProtocolTransport.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ _SSLProtocolTransport.__setstate_cython__(self, __pyx_state) """
        pass

    _protocol_paused = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



