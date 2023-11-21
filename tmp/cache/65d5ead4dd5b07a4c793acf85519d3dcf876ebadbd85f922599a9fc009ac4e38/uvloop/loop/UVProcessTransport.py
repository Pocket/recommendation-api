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


from .UVProcess import UVProcess

class UVProcessTransport(UVProcess):
    # no doc
    def close(self): # real signature unknown; restored from __doc__
        """ UVProcessTransport.close(self) """
        pass

    def get_extra_info(self, name, default=None): # real signature unknown; restored from __doc__
        """ UVProcessTransport.get_extra_info(self, name, default=None) """
        pass

    def get_pid(self): # real signature unknown; restored from __doc__
        """ UVProcessTransport.get_pid(self) """
        pass

    def get_pipe_transport(self, fd): # real signature unknown; restored from __doc__
        """ UVProcessTransport.get_pipe_transport(self, fd) """
        pass

    def get_protocol(self): # real signature unknown; restored from __doc__
        """ UVProcessTransport.get_protocol(self) """
        pass

    def get_returncode(self): # real signature unknown; restored from __doc__
        """ UVProcessTransport.get_returncode(self) """
        pass

    def is_closing(self): # real signature unknown; restored from __doc__
        """ UVProcessTransport.is_closing(self) """
        pass

    def kill(self): # real signature unknown; restored from __doc__
        """ UVProcessTransport.kill(self) """
        pass

    def send_signal(self, int_signal): # real signature unknown; restored from __doc__
        """ UVProcessTransport.send_signal(self, int signal) """
        pass

    def set_protocol(self, protocol): # real signature unknown; restored from __doc__
        """ UVProcessTransport.set_protocol(self, protocol) """
        pass

    def terminate(self): # real signature unknown; restored from __doc__
        """ UVProcessTransport.terminate(self) """
        pass

    def _wait(self): # real signature unknown; restored from __doc__
        """ UVProcessTransport._wait(self) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ UVProcessTransport.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ UVProcessTransport.__setstate_cython__(self, __pyx_state) """
        pass

    def __stdio_inited(self, waiter, stdio_fut): # real signature unknown; restored from __doc__
        """ UVProcessTransport.__stdio_inited(self, waiter, stdio_fut) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0xffffabb266c0>'


