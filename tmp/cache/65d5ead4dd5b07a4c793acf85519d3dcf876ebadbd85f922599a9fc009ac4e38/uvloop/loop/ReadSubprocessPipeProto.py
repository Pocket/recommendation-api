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


from .WriteSubprocessPipeProto import WriteSubprocessPipeProto

class ReadSubprocessPipeProto(WriteSubprocessPipeProto, __asyncio_protocols.Protocol):
    # no doc
    def data_received(self, data): # real signature unknown; restored from __doc__
        """ ReadSubprocessPipeProto.data_received(self, data) """
        pass

    def __init__(self, proc, fd): # real signature unknown; restored from __doc__
        """ WriteSubprocessPipeProto.__init__(self, proc, fd) """
        pass


