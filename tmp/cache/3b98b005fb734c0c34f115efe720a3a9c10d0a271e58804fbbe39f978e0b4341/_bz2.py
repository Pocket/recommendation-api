# encoding: utf-8
# module _bz2
# from /usr/local/lib/python3.8/lib-dynload/_bz2.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

# no functions
# classes

class BZ2Compressor(object):
    """
    Create a compressor object for compressing data incrementally.
    
      compresslevel
        Compression level, as a number between 1 and 9.
    
    For one-shot compression, use the compress() function instead.
    """
    def compress(self, *args, **kwargs): # real signature unknown
        """
        Provide data to the compressor object.
        
        Returns a chunk of compressed data if possible, or b'' otherwise.
        
        When you have finished providing data to the compressor, call the
        flush() method to finish the compression process.
        """
        pass

    def flush(self, *args, **kwargs): # real signature unknown
        """
        Finish the compression process.
        
        Returns the compressed data left in internal buffers.
        
        The compressor object may not be used after this method is called.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class BZ2Decompressor(object):
    """
    Create a decompressor object for decompressing data incrementally.
    
    For one-shot decompression, use the decompress() function instead.
    """
    def decompress(self): # real signature unknown; restored from __doc__
        """
        Decompress *data*, returning uncompressed data as bytes.
        
        If *max_length* is nonnegative, returns at most *max_length* bytes of
        decompressed data. If this limit is reached and further output can be
        produced, *self.needs_input* will be set to ``False``. In this case, the next
        call to *decompress()* may provide *data* as b'' to obtain more of the output.
        
        If all of the input data was decompressed and returned (either because this
        was less than *max_length* bytes, or because *max_length* was negative),
        *self.needs_input* will be set to True.
        
        Attempting to decompress data after the end of stream is reached raises an
        EOFError.  Any data found after the end of the stream is ignored and saved in
        the unused_data attribute.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    eof = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the end-of-stream marker has been reached."""

    needs_input = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if more input is needed before more decompressed data can be produced."""

    unused_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Data found after the end of the compressed stream."""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xfffface777c0>'

__spec__ = None # (!) real value is "ModuleSpec(name='_bz2', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xfffface777c0>, origin='/usr/local/lib/python3.8/lib-dynload/_bz2.cpython-38-aarch64-linux-gnu.so')"

