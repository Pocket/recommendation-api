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


from .GrpcCallWrapper import GrpcCallWrapper

class _AioCall(GrpcCallWrapper):
    # no doc
    def add_done_callback(self, *args, **kwargs): # real signature unknown
        pass

    def cancel(self, *args, **kwargs): # real signature unknown
        """
        Cancels the RPC in Core with given RPC status.
        
                Above abstractions must invoke this method to set Core objects into
                proper state.
        """
        pass

    def cancelled(self, *args, **kwargs): # real signature unknown
        """
        Returns if the RPC was cancelled.
        
                Returns:
                    True if the RPC was cancelled.
        """
        pass

    def done(self, *args, **kwargs): # real signature unknown
        """
        Returns if the RPC call has finished.
        
                Checks if the status has been provided, either
                because the RPC finished or because was cancelled..
        
                Returns:
                    True if the RPC can be considered finished.
        """
        pass

    def initial_metadata(self, *args, **kwargs): # real signature unknown
        """
        Returns the initial metadata of the RPC call.
        
                If the initial metadata has not been received yet this function will
                wait until the RPC gets finished.
        
                Returns:
                    The tuple object with the initial metadata.
        """
        pass

    def initiate_stream_stream(self, *args, **kwargs): # real signature unknown
        """
        Actual implementation of the complete stream-stream call.
        
                Needs to pay extra attention to the raise mechanism. If we want to
                propagate the final status exception, then we have to raise it.
                Othersize, it would end normally and raise `StopAsyncIteration()`.
        """
        pass

    def initiate_unary_stream(self, *args, **kwargs): # real signature unknown
        """ Implementation of the start of a unary-stream call. """
        pass

    def is_locally_cancelled(self, *args, **kwargs): # real signature unknown
        """
        Returns if the RPC was cancelled locally.
        
                Returns:
                    True when was cancelled locally, False when was cancelled remotelly or
                    is still ongoing.
        """
        pass

    def is_ok(self, *args, **kwargs): # real signature unknown
        """ Returns if the RPC is ended with ok. """
        pass

    def receive_serialized_message(self, *args, **kwargs): # real signature unknown
        """ Receives one single raw message in bytes. """
        pass

    def send_receive_close(self, *args, **kwargs): # real signature unknown
        """ Half close the RPC on the client-side. """
        pass

    def send_serialized_message(self, *args, **kwargs): # real signature unknown
        """ Sends one single raw message in bytes. """
        pass

    def set_internal_error(self, *args, **kwargs): # real signature unknown
        pass

    def status(self, *args, **kwargs): # real signature unknown
        """
        Returns the status of the RPC call.
        
                It returns the finshed status of the RPC. If the RPC
                has not finished yet this function will wait until the RPC
                gets finished.
        
                Returns:
                    Finished status of the RPC as an AioRpcStatus object.
        """
        pass

    def stream_unary(self, *args, **kwargs): # real signature unknown
        """
        Actual implementation of the complete unary-stream call.
        
                Needs to pay extra attention to the raise mechanism. If we want to
                propagate the final status exception, then we have to raise it.
                Othersize, it would end normally and raise `StopAsyncIteration()`.
        """
        pass

    def time_remaining(self, *args, **kwargs): # real signature unknown
        pass

    def unary_unary(self, *args, **kwargs): # real signature unknown
        """
        Performs a unary unary RPC.
        
                Args:
                  request: the serialized requests in bytes.
                  outbound_initial_metadata: optional outbound metadata.
        """
        pass

    def _handle_status_once_received(self, *args, **kwargs): # real signature unknown
        """ Handles the status sent by peer once received. """
        pass

    def _repr(self, *args, **kwargs): # real signature unknown
        """ Assembles the RPC representation string. """
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

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    _channel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _initial_metadata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0xffffabd730f0>'


