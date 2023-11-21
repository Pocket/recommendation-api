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

class PseudoSocket(object):
    """ PseudoSocket(int family, int type, int proto, int fd) """
    def accept(self): # real signature unknown; restored from __doc__
        """ PseudoSocket.accept(self) """
        pass

    def bind(self, *args): # real signature unknown; restored from __doc__
        """ PseudoSocket.bind(self, *args) """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ PseudoSocket.close(self) """
        pass

    def connect(self, *args): # real signature unknown; restored from __doc__
        """ PseudoSocket.connect(self, *args) """
        pass

    def connect_ex(self, *args): # real signature unknown; restored from __doc__
        """ PseudoSocket.connect_ex(self, *args) """
        pass

    def detach(self): # real signature unknown; restored from __doc__
        """ PseudoSocket.detach(self) """
        pass

    def dup(self): # real signature unknown; restored from __doc__
        """ PseudoSocket.dup(self) """
        pass

    def fileno(self): # real signature unknown; restored from __doc__
        """ PseudoSocket.fileno(self) """
        pass

    def getpeername(self): # real signature unknown; restored from __doc__
        """ PseudoSocket.getpeername(self) """
        pass

    def getsockname(self): # real signature unknown; restored from __doc__
        """ PseudoSocket.getsockname(self) """
        pass

    def getsockopt(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """ PseudoSocket.getsockopt(self, *args, **kwargs) """
        pass

    def gettimeout(self): # real signature unknown; restored from __doc__
        """ PseudoSocket.gettimeout(self) """
        pass

    def get_inheritable(self): # real signature unknown; restored from __doc__
        """ PseudoSocket.get_inheritable(self) """
        pass

    def ioctl(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """ PseudoSocket.ioctl(self, *args, **kwargs) """
        pass

    def listen(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """ PseudoSocket.listen(self, *args, **kwargs) """
        pass

    def makefile(self): # real signature unknown; restored from __doc__
        """ PseudoSocket.makefile(self) """
        pass

    def recv(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """ PseudoSocket.recv(self, *args, **kwargs) """
        pass

    def recvfrom(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """ PseudoSocket.recvfrom(self, *args, **kwargs) """
        pass

    def recvfrom_into(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """ PseudoSocket.recvfrom_into(self, *args, **kwargs) """
        pass

    def recvmsg(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """ PseudoSocket.recvmsg(self, *args, **kwargs) """
        pass

    def recvmsg_into(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """ PseudoSocket.recvmsg_into(self, *args, **kwargs) """
        pass

    def recv_into(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """ PseudoSocket.recv_into(self, *args, **kwargs) """
        pass

    def send(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """ PseudoSocket.send(self, *args, **kwargs) """
        pass

    def sendall(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """ PseudoSocket.sendall(self, *args, **kwargs) """
        pass

    def sendfile(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """ PseudoSocket.sendfile(self, *args, **kwargs) """
        pass

    def sendmsg(self): # real signature unknown; restored from __doc__
        """ PseudoSocket.sendmsg(self) """
        pass

    def sendmsg_afalg(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """ PseudoSocket.sendmsg_afalg(self, *args, **kwargs) """
        pass

    def sendto(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """ PseudoSocket.sendto(self, *args, **kwargs) """
        pass

    def setblocking(self, flag): # real signature unknown; restored from __doc__
        """ PseudoSocket.setblocking(self, flag) """
        pass

    def setsockopt(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """ PseudoSocket.setsockopt(self, *args, **kwargs) """
        pass

    def settimeout(self, value): # real signature unknown; restored from __doc__
        """ PseudoSocket.settimeout(self, value) """
        pass

    def set_inheritable(self): # real signature unknown; restored from __doc__
        """ PseudoSocket.set_inheritable(self) """
        pass

    def share(self, process_id): # real signature unknown; restored from __doc__
        """ PseudoSocket.share(self, process_id) """
        pass

    def shutdown(self, *args): # real signature unknown; restored from __doc__
        """ PseudoSocket.shutdown(self, *args) """
        pass

    def __enter__(self): # real signature unknown; restored from __doc__
        """ PseudoSocket.__enter__(self) """
        pass

    def __exit__(self, *err): # real signature unknown; restored from __doc__
        """ PseudoSocket.__exit__(self, *err) """
        pass

    def __getstate__(self): # real signature unknown; restored from __doc__
        """ PseudoSocket.__getstate__(self) """
        pass

    def __init__(self, int_family, int_type, int_proto, int_fd): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce_cython__(self): # real signature unknown; restored from __doc__
        """ PseudoSocket.__reduce_cython__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate_cython__(self, __pyx_state): # real signature unknown; restored from __doc__
        """ PseudoSocket.__setstate_cython__(self, __pyx_state) """
        pass

    family = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    proto = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0xffffabb26900>'


