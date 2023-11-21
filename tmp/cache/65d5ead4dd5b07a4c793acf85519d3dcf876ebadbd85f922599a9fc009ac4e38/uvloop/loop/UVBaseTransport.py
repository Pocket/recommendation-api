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


from .UVSocketHandle import UVSocketHandle

class UVBaseTransport(UVSocketHandle):
    # no doc
    def abort(self): # real signature unknown; restored from __doc__
        """ UVBaseTransport.abort(self) """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ UVBaseTransport.close(self) """
        pass

    def get_extra_info(self, name, default=None): # real signature unknown; restored from __doc__
        """ UVBaseTransport.get_extra_info(self, name, default=None) """
        pass

    def get_protocol(self): # real signature unknown; restored from __doc__
        """ UVBaseTransport.get_protocol(self) """
        pass

    def get_write_buffer_limits(self): # real signature unknown; restored from __doc__
        """ UVBaseTransport.get_write_buffer_limits(self) """
        pass

    def get_write_buffer_size(self): # real signature unknown; restored from __doc__
        """ UVBaseTransport.get_write_buffer_size(self) """
        pass

    def is_closing(self): # real signature unknown; restored from __doc__
        """ UVBaseTransport.is_closing(self) """
        pass

    def set_protocol(self, protocol): # real signature unknown; restored from __doc__
        """ UVBaseTransport.set_protocol(self, protocol) """
        pass

    def set_write_buffer_limits(self, high=None, low=None): # real signature unknown; restored from __doc__
        """ UVBaseTransport.set_write_buffer_limits(self, high=None, low=None) """
        pass

    def _force_close(self, exc): # real signature unknown; restored from __doc__
        """ UVBaseTransport._force_close(self, exc) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ UVBaseTransport.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ UVBaseTransport.__setstate_cython__(self, __pyx_state) """
        pass

    _closing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _paused = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0xffffabb260f0>'


