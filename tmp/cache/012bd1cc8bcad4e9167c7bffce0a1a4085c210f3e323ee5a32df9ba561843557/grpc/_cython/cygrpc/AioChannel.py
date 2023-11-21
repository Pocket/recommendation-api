# encoding: utf-8
# module grpc._cython.cygrpc
# from /.venv/lib/python3.8/site-packages/grpc/_cython/cygrpc.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import logging as logging # /usr/local/lib/python3.8/logging/__init__.py
import os as os # /usr/local/lib/python3.8/os.py
import sys as sys # <module 'sys' (built-in)>
import threading as threading # /usr/local/lib/python3.8/threading.py
import time as time # <module 'time' (built-in)>
import grpc as grpc # /.venv/lib/python3.8/site-packages/grpc/__init__.py
import asyncio as asyncio # /usr/local/lib/python3.8/asyncio/__init__.py
import grpc._observability as _observability # /.venv/lib/python3.8/site-packages/grpc/_observability.py
import collections as collections # /usr/local/lib/python3.8/collections/__init__.py
import pkgutil as pkgutil # /usr/local/lib/python3.8/pkgutil.py
import codecs as codecs # /usr/local/lib/python3.8/codecs.py
import atexit as atexit # <module 'atexit' (built-in)>
import errno as errno # <module 'errno' (built-in)>
import contextvars as contextvars # /usr/local/lib/python3.8/contextvars.py
import socket as socket # /usr/local/lib/python3.8/socket.py
import enum as enum # /usr/local/lib/python3.8/enum.py
import inspect as inspect # /usr/local/lib/python3.8/inspect.py
import traceback as traceback # /usr/local/lib/python3.8/traceback.py
import functools as functools # /usr/local/lib/python3.8/functools.py
import enum as __enum


from .object import object

class AioChannel(object):
    # no doc
    def call(self, *args, **kwargs): # real signature unknown
        """
        Assembles a Cython Call object.
        
                Returns:
                  An _AioCall object.
        """
        pass

    def check_connectivity_state(self, *args, **kwargs): # real signature unknown
        """ A Cython wrapper for Core's check connectivity state API. """
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def closed(self, *args, **kwargs): # real signature unknown
        pass

    def closing(self, *args, **kwargs): # real signature unknown
        pass

    def watch_connectivity_state(self, *args, **kwargs): # real signature unknown
        """
        Watch for one connectivity state change.
        
                Keeps mirroring the behavior from Core, so we can easily switch to
                other design of API if necessary.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass


