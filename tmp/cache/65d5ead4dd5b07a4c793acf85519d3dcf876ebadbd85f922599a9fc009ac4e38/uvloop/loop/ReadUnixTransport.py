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


from .UVStream import UVStream

class ReadUnixTransport(UVStream):
    # no doc
    def abort(self): # real signature unknown; restored from __doc__
        """ ReadUnixTransport.abort(self) """
        pass

    def can_write_eof(self): # real signature unknown; restored from __doc__
        """ ReadUnixTransport.can_write_eof(self) """
        pass

    def get_write_buffer_limits(self): # real signature unknown; restored from __doc__
        """ ReadUnixTransport.get_write_buffer_limits(self) """
        pass

    def get_write_buffer_size(self): # real signature unknown; restored from __doc__
        """ ReadUnixTransport.get_write_buffer_size(self) """
        pass

    def set_write_buffer_limits(self, high=None, low=None): # real signature unknown; restored from __doc__
        """ ReadUnixTransport.set_write_buffer_limits(self, high=None, low=None) """
        pass

    def write(self, data): # real signature unknown; restored from __doc__
        """ ReadUnixTransport.write(self, data) """
        pass

    def writelines(self, list_of_data): # real signature unknown; restored from __doc__
        """ ReadUnixTransport.writelines(self, list_of_data) """
        pass

    def write_eof(self): # real signature unknown; restored from __doc__
        """ ReadUnixTransport.write_eof(self) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ ReadUnixTransport.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ ReadUnixTransport.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0xffffabb265a0>'


