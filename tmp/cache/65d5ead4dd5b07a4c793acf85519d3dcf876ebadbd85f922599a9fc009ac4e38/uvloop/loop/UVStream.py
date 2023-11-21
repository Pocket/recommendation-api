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


from .UVBaseTransport import UVBaseTransport

class UVStream(UVBaseTransport):
    # no doc
    def can_write_eof(self): # real signature unknown; restored from __doc__
        """ UVStream.can_write_eof(self) """
        pass

    def is_reading(self): # real signature unknown; restored from __doc__
        """ UVStream.is_reading(self) """
        pass

    def pause_reading(self): # real signature unknown; restored from __doc__
        """ UVStream.pause_reading(self) """
        pass

    def resume_reading(self): # real signature unknown; restored from __doc__
        """ UVStream.resume_reading(self) """
        pass

    def write(self, buf): # real signature unknown; restored from __doc__
        """ UVStream.write(self, buf) """
        pass

    def writelines(self, bufs): # real signature unknown; restored from __doc__
        """ UVStream.writelines(self, bufs) """
        pass

    def write_eof(self): # real signature unknown; restored from __doc__
        """ UVStream.write_eof(self) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ UVStream.__reduce_cython__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ UVStream.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0xffffabb26390>'


