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

class ChannelArgKey(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    default_authority = b'grpc.default_authority'
    enable_census = b'grpc.census'
    http2_initial_sequence_number = b'grpc.http2.initial_sequence_number'
    max_concurrent_streams = b'grpc.max_concurrent_streams'
    max_receive_message_length = b'grpc.max_receive_message_length'
    max_send_message_length = b'grpc.max_send_message_length'
    primary_user_agent_string = b'grpc.primary_user_agent'
    secondary_user_agent_string = b'grpc.secondary_user_agent'
    ssl_session_cache = b'grpc.ssl_session_cache'
    ssl_target_name_override = b'grpc.ssl_target_name_override'
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'grpc._cython.cygrpc', 'enable_census': b'grpc.census', 'max_concurrent_streams': b'grpc.max_concurrent_streams', 'max_receive_message_length': b'grpc.max_receive_message_length', 'max_send_message_length': b'grpc.max_send_message_length', 'http2_initial_sequence_number': b'grpc.http2.initial_sequence_number', 'default_authority': b'grpc.default_authority', 'primary_user_agent_string': b'grpc.primary_user_agent', 'secondary_user_agent_string': b'grpc.secondary_user_agent', 'ssl_session_cache': b'grpc.ssl_session_cache', 'ssl_target_name_override': b'grpc.ssl_target_name_override', '__dict__': <attribute '__dict__' of 'ChannelArgKey' objects>, '__weakref__': <attribute '__weakref__' of 'ChannelArgKey' objects>, '__doc__': None})"


