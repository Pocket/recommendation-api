# encoding: utf-8
# module numpy.random._philox
# from /.venv/lib/python3.8/site-packages/numpy/random/_philox.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /.venv/lib/python3.8/site-packages/numpy/__init__.py
import numpy.random.bit_generator as __numpy_random_bit_generator


# no functions
# classes

class Philox(__numpy_random_bit_generator.BitGenerator):
    """
    Philox(seed=None, counter=None, key=None)
    
        Container for the Philox (4x64) pseudo-random number generator.
    
        Parameters
        ----------
        seed : {None, int, array_like[ints], SeedSequence}, optional
            A seed to initialize the `BitGenerator`. If None, then fresh,
            unpredictable entropy will be pulled from the OS. If an ``int`` or
            ``array_like[ints]`` is passed, then it will be passed to
            `SeedSequence` to derive the initial `BitGenerator` state. One may also
            pass in a `SeedSequence` instance.
        counter : {None, int, array_like}, optional
            Counter to use in the Philox state. Can be either
            a Python int (long in 2.x) in [0, 2**256) or a 4-element uint64 array.
            If not provided, the RNG is initialized at 0.
        key : {None, int, array_like}, optional
            Key to use in the Philox state.  Unlike ``seed``, the value in key is
            directly set. Can be either a Python int in [0, 2**128) or a 2-element
            uint64 array. `key` and ``seed`` cannot both be used.
    
        Attributes
        ----------
        lock: threading.Lock
            Lock instance that is shared so that the same bit git generator can
            be used in multiple Generators without corrupting the state. Code that
            generates values from a bit generator should hold the bit generator's
            lock.
    
        Notes
        -----
        Philox is a 64-bit PRNG that uses a counter-based design based on weaker
        (and faster) versions of cryptographic functions [1]_. Instances using
        different values of the key produce independent sequences.  Philox has a
        period of :math:`2^{256} - 1` and supports arbitrary advancing and jumping
        the sequence in increments of :math:`2^{128}`. These features allow
        multiple non-overlapping sequences to be generated.
    
        ``Philox`` provides a capsule containing function pointers that produce
        doubles, and unsigned 32 and 64- bit integers. These are not
        directly consumable in Python and must be consumed by a ``Generator``
        or similar object that supports low-level access.
    
        **State and Seeding**
    
        The ``Philox`` state vector consists of a 256-bit value encoded as
        a 4-element uint64 array and a 128-bit value encoded as a 2-element uint64
        array. The former is a counter which is incremented by 1 for every 4 64-bit
        randoms produced. The second is a key which determined the sequence
        produced. Using different keys produces independent sequences.
    
        The input ``seed`` is processed by `SeedSequence` to generate the key. The
        counter is set to 0.
    
        Alternately, one can omit the ``seed`` parameter and set the ``key`` and
        ``counter`` directly.
    
        **Parallel Features**
    
        The preferred way to use a BitGenerator in parallel applications is to use
        the `SeedSequence.spawn` method to obtain entropy values, and to use these
        to generate new BitGenerators:
    
        >>> from numpy.random import Generator, Philox, SeedSequence
        >>> sg = SeedSequence(1234)
        >>> rg = [Generator(Philox(s)) for s in sg.spawn(10)]
    
        ``Philox`` can be used in parallel applications by calling the ``jumped``
        method  to advances the state as-if :math:`2^{128}` random numbers have
        been generated. Alternatively, ``advance`` can be used to advance the
        counter for any positive step in [0, 2**256). When using ``jumped``, all
        generators should be chained to ensure that the segments come from the same
        sequence.
    
        >>> from numpy.random import Generator, Philox
        >>> bit_generator = Philox(1234)
        >>> rg = []
        >>> for _ in range(10):
        ...    rg.append(Generator(bit_generator))
        ...    bit_generator = bit_generator.jumped()
    
        Alternatively, ``Philox`` can be used in parallel applications by using
        a sequence of distinct keys where each instance uses different key.
    
        >>> key = 2**96 + 2**33 + 2**17 + 2**9
        >>> rg = [Generator(Philox(key=key+i)) for i in range(10)]
    
        **Compatibility Guarantee**
    
        ``Philox`` makes a guarantee that a fixed ``seed`` will always produce
        the same random integer stream.
    
        Examples
        --------
        >>> from numpy.random import Generator, Philox
        >>> rg = Generator(Philox(1234))
        >>> rg.standard_normal()
        0.123  # random
    
        References
        ----------
        .. [1] John K. Salmon, Mark A. Moraes, Ron O. Dror, and David E. Shaw,
               "Parallel Random Numbers: As Easy as 1, 2, 3," Proceedings of
               the International Conference for High Performance Computing,
               Networking, Storage and Analysis (SC11), New York, NY: ACM, 2011.
    """
    def advance(self, delta): # real signature unknown; restored from __doc__
        """
        advance(delta)
        
                Advance the underlying RNG as-if delta draws have occurred.
        
                Parameters
                ----------
                delta : integer, positive
                    Number of draws to advance the RNG. Must be less than the
                    size state variable in the underlying RNG.
        
                Returns
                -------
                self : Philox
                    RNG advanced delta steps
        
                Notes
                -----
                Advancing a RNG updates the underlying RNG state as-if a given
                number of calls to the underlying RNG have been made. In general
                there is not a one-to-one relationship between the number output
                random values from a particular distribution and the number of
                draws from the core RNG.  This occurs for two reasons:
        
                * The random values are simulated using a rejection-based method
                  and so, on average, more than one value from the underlying
                  RNG is required to generate an single draw.
                * The number of bits required to generate a simulated value
                  differs from the number of bits generated by the underlying
                  RNG.  For example, two 16-bit integer values can be simulated
                  from a single draw of a 32-bit RNG.
        
                Advancing the RNG state resets any pre-computed random numbers.
                This is required to ensure exact reproducibility.
        """
        pass

    def jumped(self, jumps=1): # real signature unknown; restored from __doc__
        """
        jumped(jumps=1)
        
                Returns a new bit generator with the state jumped
        
                The state of the returned bit generator is jumped as-if
                (2**128) * jumps random numbers have been generated.
        
                Parameters
                ----------
                jumps : integer, positive
                    Number of times to jump the state of the bit generator returned
        
                Returns
                -------
                bit_generator : Philox
                    New instance of generator jumped iter times
        """
        pass

    def __init__(self, seed=None, counter=None, key=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Get or set the PRNG state

        Returns
        -------
        state : dict
            Dictionary containing the information required to describe the
            state of the PRNG
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0xffff9fb2b420>'


# variables with complex values

__all__ = [
    'Philox',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9fb2b400>'

__spec__ = None # (!) real value is "ModuleSpec(name='numpy.random._philox', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9fb2b400>, origin='/.venv/lib/python3.8/site-packages/numpy/random/_philox.cpython-38-aarch64-linux-gnu.so')"

__test__ = {}

