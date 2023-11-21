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


class WriteSubprocessPipeProto(__asyncio_protocols.BaseProtocol):
    # no doc
    def connection_lost(self, exc): # real signature unknown; restored from __doc__
        """ WriteSubprocessPipeProto.connection_lost(self, exc) """
        pass

    def connection_made(self, transport): # real signature unknown; restored from __doc__
        """ WriteSubprocessPipeProto.connection_made(self, transport) """
        pass

    def pause_writing(self): # real signature unknown; restored from __doc__
        """ WriteSubprocessPipeProto.pause_writing(self) """
        pass

    def resume_writing(self): # real signature unknown; restored from __doc__
        """ WriteSubprocessPipeProto.resume_writing(self) """
        pass

    def __init__(self, proc, fd): # real signature unknown; restored from __doc__
        """ WriteSubprocessPipeProto.__init__(self, proc, fd) """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ WriteSubprocessPipeProto.__repr__(self) """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'uvloop.loop', '__init__': <cyfunction WriteSubprocessPipeProto.__init__ at 0xffffabefe1e0>, 'connection_made': <cyfunction WriteSubprocessPipeProto.connection_made at 0xffffabefe5f0>, '__repr__': <cyfunction WriteSubprocessPipeProto.__repr__ at 0xffffabefe6c0>, 'connection_lost': <cyfunction WriteSubprocessPipeProto.connection_lost at 0xffffabefe790>, 'pause_writing': <cyfunction WriteSubprocessPipeProto.pause_writing at 0xffffabefe860>, 'resume_writing': <cyfunction WriteSubprocessPipeProto.resume_writing at 0xffffabefe930>, '__dict__': <attribute '__dict__' of 'WriteSubprocessPipeProto' objects>, '__weakref__': <attribute '__weakref__' of 'WriteSubprocessPipeProto' objects>, '__doc__': None})"


