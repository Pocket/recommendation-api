# encoding: utf-8
# module numpy.random.bit_generator
# from /.venv/lib/python3.8/site-packages/numpy/random/bit_generator.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
"""
BitGenerator base class and SeedSequence used to seed the BitGenerators.

SeedSequence is derived from Melissa E. O'Neill's C++11 `std::seed_seq`
implementation, as it has a lot of nice properties that we want.

https://gist.github.com/imneme/540829265469e673d045
http://www.pcg-random.org/posts/developing-a-seed_seq-alternative.html

The MIT License (MIT)

Copyright (c) 2015 Melissa E. O'Neill
Copyright (c) 2019 NumPy Developers

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import abc as abc # /usr/local/lib/python3.8/abc.py
import sys as sys # <module 'sys' (built-in)>
import re as re # /usr/local/lib/python3.8/re.py
import numpy as np # /.venv/lib/python3.8/site-packages/numpy/__init__.py
from itertools import cycle

from _thread import Lock

import abc as __abc


# functions

def randbits(k): # real signature unknown; restored from __doc__
    """ getrandbits(k) -> x.  Generates an int with k random bits. """
    pass

def _coerce_to_uint32_array(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Coerce an input to a uint32 array.
    
        If a `uint32` array, pass it through directly.
        If a non-negative integer, then break it up into `uint32` words, lowest
        bits first.
        If a string starting with "0x", then interpret as a hex integer, as above.
        If a string of decimal digits, interpret as a decimal integer, as above.
        If a sequence of ints or strings, interpret each element as above and
        concatenate.
    
        Note that the handling of `int64` or `uint64` arrays are not just
        straightforward views as `uint32` arrays. If an element is small enough to
        fit into a `uint32`, then it will only take up one `uint32` element in the
        output. This is to make sure that the interpretation of a sequence of
        integers is the same regardless of numpy's default integer type, which
        differs on different platforms.
    
        Parameters
        ----------
        x : int, str, sequence of int or str
    
        Returns
        -------
        seed_array : uint32 array
    
        Examples
        --------
        >>> import numpy as np
        >>> from numpy.random.bit_generator import _coerce_to_uint32_array
        >>> _coerce_to_uint32_array(12345)
        array([12345], dtype=uint32)
        >>> _coerce_to_uint32_array('12345')
        array([12345], dtype=uint32)
        >>> _coerce_to_uint32_array('0x12345')
        array([74565], dtype=uint32)
        >>> _coerce_to_uint32_array([12345, '67890'])
        array([12345, 67890], dtype=uint32)
        >>> _coerce_to_uint32_array(np.array([12345, 67890], dtype=np.uint32))
        array([12345, 67890], dtype=uint32)
        >>> _coerce_to_uint32_array(np.array([12345, 67890], dtype=np.int64))
        array([12345, 67890], dtype=uint32)
        >>> _coerce_to_uint32_array([12345, 0x10deadbeef, 67890, 0xdeadbeef])
        array([     12345, 3735928559,         16,      67890, 3735928559],
              dtype=uint32)
        >>> _coerce_to_uint32_array(1234567890123456789012345678901234567890)
        array([3460238034, 2898026390, 3235640248, 2697535605,          3],
              dtype=uint32)
    """
    pass

def _int_to_uint32_array(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_SeedlessSeedSequence(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_SeedSequence(*args, **kwargs): # real signature unknown
    pass

# classes

class BitGenerator(object):
    """
    BitGenerator(seed=None)
    
        Base Class for generic BitGenerators, which provide a stream
        of random bits based on different algorithms. Must be overridden.
    
        Parameters
        ----------
        seed : {None, int, array_like[ints], SeedSequence}, optional
            A seed to initialize the `BitGenerator`. If None, then fresh,
            unpredictable entropy will be pulled from the OS. If an ``int`` or
            ``array_like[ints]`` is passed, then it will be passed to
            `~numpy.random.SeedSequence` to derive the initial `BitGenerator` state.
            One may also pass in a `SeedSequence` instance.
    
        Attributes
        ----------
        lock : threading.Lock
            Lock instance that is shared so that the same BitGenerator can
            be used in multiple Generators without corrupting the state. Code that
            generates values from a bit generator should hold the bit generator's
            lock.
    
        See Also
        --------
        SeedSequence
    """
    def random_raw(self, size=None): # real signature unknown; restored from __doc__
        """
        random_raw(self, size=None)
        
                Return randoms as generated by the underlying BitGenerator
        
                Parameters
                ----------
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  Default is None, in which case a
                    single value is returned.
                output : bool, optional
                    Output values.  Used for performance testing since the generated
                    values are not returned.
        
                Returns
                -------
                out : uint or ndarray
                    Drawn samples.
        
                Notes
                -----
                This method directly exposes the raw underlying pseudo-random
                number generator. All values are returned as unsigned 64-bit
                values irrespective of the number of bits produced by the PRNG.
        
                See the class docstring for the number of bits returned.
        """
        pass

    def _benchmark(self, *args, **kwargs): # real signature unknown
        """ Used in tests """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, seed=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    capsule = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cffi = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        CFFI interface

        Returns
        -------
        interface : namedtuple
            Named tuple containing CFFI wrapper

            * state_address - Memory address of the state struct
            * state - pointer to the state struct
            * next_uint64 - function pointer to produce 64 bit integers
            * next_uint32 - function pointer to produce 32 bit integers
            * next_double - function pointer to produce doubles
            * bitgen - pointer to the bit generator struct
        """

    ctypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        ctypes interface

        Returns
        -------
        interface : namedtuple
            Named tuple containing ctypes wrapper

            * state_address - Memory address of the state struct
            * state - pointer to the state struct
            * next_uint64 - function pointer to produce 64 bit integers
            * next_uint32 - function pointer to produce 32 bit integers
            * next_double - function pointer to produce doubles
            * bitgen - pointer to the bit generator struct
        """

    lock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Get or set the PRNG state

        The base BitGenerator.state must be overridden by a subclass

        Returns
        -------
        state : dict
            Dictionary containing the information required to describe the
            state of the PRNG
        """

    _cffi = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _ctypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _seed_seq = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class ISeedSequence(__abc.ABC):
    """
    Abstract base class for seed sequences.
    
        ``BitGenerator`` implementations should treat any object that adheres to
        this interface as a seed sequence.
    
        See Also
        --------
        SeedSequence, SeedlessSeedSequence
    """
    def generate_state(self, n_words, dtype=None): # real signature unknown; restored from __doc__
        """
        generate_state(n_words, dtype=np.uint32)
        
                Return the requested number of words for PRNG seeding.
        
                A BitGenerator should call this method in its constructor with
                an appropriate `n_words` parameter to properly seed itself.
        
                Parameters
                ----------
                n_words : int
                dtype : np.uint32 or np.uint64, optional
                    The size of each word. This should only be either `uint32` or
                    `uint64`. Strings (`'uint32'`, `'uint64'`) are fine. Note that
                    requesting `uint64` will draw twice as many bits as `uint32` for
                    the same `n_words`. This is a convenience for `BitGenerator`s that
                    express their states as `uint64` arrays.
        
                Returns
                -------
                state : uint32 or uint64 array, shape=(n_words,)
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _abc_impl = None # (!) real value is '<_abc_data object at 0xffff9fdbf870>'
    __abstractmethods__ = frozenset({'generate_state'})
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'numpy.random.bit_generator', '__doc__': '\\n    Abstract base class for seed sequences.\\n\\n    ``BitGenerator`` implementations should treat any object that adheres to\\n    this interface as a seed sequence.\\n\\n    See Also\\n    --------\\n    SeedSequence, SeedlessSeedSequence\\n    ', 'generate_state': <cyfunction ISeedSequence.generate_state at 0xffff9fdcb040>, '__dict__': <attribute '__dict__' of 'ISeedSequence' objects>, '__weakref__': <attribute '__weakref__' of 'ISeedSequence' objects>, '__abstractmethods__': frozenset({'generate_state'}), '_abc_impl': <_abc_data object at 0xffff9fdbf870>})"


class ISpawnableSeedSequence(ISeedSequence):
    """ Abstract base class for seed sequences that can spawn. """
    def spawn(self, n_children): # real signature unknown; restored from __doc__
        """
        spawn(n_children)
        
                Spawn a number of child `SeedSequence` s by extending the
                `spawn_key`.
        
                Parameters
                ----------
                n_children : int
        
                Returns
                -------
                seqs : list of `SeedSequence` s
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _abc_impl = None # (!) real value is '<_abc_data object at 0xffff9fdbf840>'
    __abstractmethods__ = frozenset({'generate_state', 'spawn'})


class SeedlessSeedSequence(object):
    """
    A seed sequence for BitGenerators with no need for seed state.
    
        See Also
        --------
        SeedSequence, ISeedSequence
    """
    def generate_state(self, *args, **kwargs): # real signature unknown
        pass

    def spawn(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass


class SeedlessSequence(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class SeedSequence(object):
    """
    SeedSequence(entropy=None, *, spawn_key=(), pool_size=4)
    
        SeedSequence mixes sources of entropy in a reproducible way to set the
        initial state for independent and very probably non-overlapping
        BitGenerators.
    
        Once the SeedSequence is instantiated, you can call the `generate_state`
        method to get an appropriately sized seed. Calling `spawn(n) <spawn>` will
        create ``n`` SeedSequences that can be used to seed independent
        BitGenerators, i.e. for different threads.
    
        Parameters
        ----------
        entropy : {None, int, sequence[int]}, optional
            The entropy for creating a `SeedSequence`.
        spawn_key : {(), sequence[int]}, optional
            An additional source of entropy based on the position of this
            `SeedSequence` in the tree of such objects created with the
            `SeedSequence.spawn` method. Typically, only `SeedSequence.spawn` will
            set this, and users will not.
        pool_size : {int}, optional
            Size of the pooled entropy to store. Default is 4 to give a 128-bit
            entropy pool. 8 (for 256 bits) is another reasonable choice if working
            with larger PRNGs, but there is very little to be gained by selecting
            another value.
        n_children_spawned : {int}, optional
            The number of children already spawned. Only pass this if
            reconstructing a `SeedSequence` from a serialized form.
    
        Notes
        -----
    
        Best practice for achieving reproducible bit streams is to use
        the default ``None`` for the initial entropy, and then use
        `SeedSequence.entropy` to log/pickle the `entropy` for reproducibility:
    
        >>> sq1 = np.random.SeedSequence()
        >>> sq1.entropy
        243799254704924441050048792905230269161  # random
        >>> sq2 = np.random.SeedSequence(sq1.entropy)
        >>> np.all(sq1.generate_state(10) == sq2.generate_state(10))
        True
    """
    def generate_state(*args, **kwds): # reliably restored by inspect
        """
        generate_state(n_words, dtype=np.uint32)
        
                Return the requested number of words for PRNG seeding.
        
                A BitGenerator should call this method in its constructor with
                an appropriate `n_words` parameter to properly seed itself.
        
                Parameters
                ----------
                n_words : int
                dtype : np.uint32 or np.uint64, optional
                    The size of each word. This should only be either `uint32` or
                    `uint64`. Strings (`'uint32'`, `'uint64'`) are fine. Note that
                    requesting `uint64` will draw twice as many bits as `uint32` for
                    the same `n_words`. This is a convenience for `BitGenerator`s that
                    express their states as `uint64` arrays.
        
                Returns
                -------
                state : uint32 or uint64 array, shape=(n_words,)
        """
        pass

    def spawn(self, n_children): # real signature unknown; restored from __doc__
        """
        spawn(n_children)
        
                Spawn a number of child `SeedSequence` s by extending the
                `spawn_key`.
        
                Parameters
                ----------
                n_children : int
        
                Returns
                -------
                seqs : list of `SeedSequence` s
        """
        pass

    def __init__(self, entropy=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
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

    entropy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_children_spawned = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pool = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pool_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    spawn_key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0xffff9fdbf6f0>'


# variables with complex values

DECIMAL_RE = None # (!) real value is "re.compile('[0-9]+')"

__all__ = [
    'SeedSequence',
    'BitGenerator',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9fdbf550>'

__spec__ = None # (!) real value is "ModuleSpec(name='numpy.random.bit_generator', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9fdbf550>, origin='/.venv/lib/python3.8/site-packages/numpy/random/bit_generator.cpython-38-aarch64-linux-gnu.so')"

__test__ = {
    '_coerce_to_uint32_array (line 79)': ' Coerce an input to a uint32 array.\n\n    If a `uint32` array, pass it through directly.\n    If a non-negative integer, then break it up into `uint32` words, lowest\n    bits first.\n    If a string starting with "0x", then interpret as a hex integer, as above.\n    If a string of decimal digits, interpret as a decimal integer, as above.\n    If a sequence of ints or strings, interpret each element as above and\n    concatenate.\n\n    Note that the handling of `int64` or `uint64` arrays are not just\n    straightforward views as `uint32` arrays. If an element is small enough to\n    fit into a `uint32`, then it will only take up one `uint32` element in the\n    output. This is to make sure that the interpretation of a sequence of\n    integers is the same regardless of numpy\'s default integer type, which\n    differs on different platforms.\n\n    Parameters\n    ----------\n    x : int, str, sequence of int or str\n\n    Returns\n    -------\n    seed_array : uint32 array\n\n    Examples\n    --------\n    >>> import numpy as np\n    >>> from numpy.random.bit_generator import _coerce_to_uint32_array\n    >>> _coerce_to_uint32_array(12345)\n    array([12345], dtype=uint32)\n    >>> _coerce_to_uint32_array(\'12345\')\n    array([12345], dtype=uint32)\n    >>> _coerce_to_uint32_array(\'0x12345\')\n    array([74565], dtype=uint32)\n    >>> _coerce_to_uint32_array([12345, \'67890\'])\n    array([12345, 67890], dtype=uint32)\n    >>> _coerce_to_uint32_array(np.array([12345, 67890], dtype=np.uint32))\n    array([12345, 67890], dtype=uint32)\n    >>> _coerce_to_uint32_array(np.array([12345, 67890], dtype=np.int64))\n    array([12345, 67890], dtype=uint32)\n    >>> _coerce_to_uint32_array([12345, 0x10deadbeef, 67890, 0xdeadbeef])\n    array([     12345, 3735928559,         16,      67890, 3735928559],\n          dtype=uint32)\n    >>> _coerce_to_uint32_array(1234567890123456789012345678901234567890)\n    array([3460238034, 2898026390, 3235640248, 2697535605,          3],\n          dtype=uint32)\n    ',
}

