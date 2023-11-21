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

class CallError(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    already_accepted = 4
    already_finished = 7
    already_invoked = 5
    error = 1
    invalid_flags = 9
    invalid_metadata = 10
    not_invoked = 6
    not_on_client = 3
    not_on_server = 2
    ok = 0
    too_many_operations = 8
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'grpc._cython.cygrpc', 'ok': 0, 'error': 1, 'not_on_server': 2, 'not_on_client': 3, 'already_accepted': 4, 'already_invoked': 5, 'not_invoked': 6, 'already_finished': 7, 'too_many_operations': 8, 'invalid_flags': 9, 'invalid_metadata': 10, '__dict__': <attribute '__dict__' of 'CallError' objects>, '__weakref__': <attribute '__weakref__' of 'CallError' objects>, '__doc__': None})"


