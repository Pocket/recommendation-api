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

class StatusCode(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    aborted = 10
    already_exists = 6
    cancelled = 1
    data_loss = 15
    deadline_exceeded = 4
    failed_precondition = 9
    internal = 13
    invalid_argument = 3
    not_found = 5
    ok = 0
    out_of_range = 11
    permission_denied = 7
    resource_exhausted = 8
    unauthenticated = 16
    unavailable = 14
    unimplemented = 12
    unknown = 2
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'grpc._cython.cygrpc', 'ok': 0, 'cancelled': 1, 'unknown': 2, 'invalid_argument': 3, 'deadline_exceeded': 4, 'not_found': 5, 'already_exists': 6, 'permission_denied': 7, 'unauthenticated': 16, 'resource_exhausted': 8, 'failed_precondition': 9, 'aborted': 10, 'out_of_range': 11, 'unimplemented': 12, 'internal': 13, 'unavailable': 14, 'data_loss': 15, '__dict__': <attribute '__dict__' of 'StatusCode' objects>, '__weakref__': <attribute '__weakref__' of 'StatusCode' objects>, '__doc__': None})"


