# encoding: utf-8
# module numpy.random._sfc64
# from /.venv/lib/python3.8/site-packages/numpy/random/_sfc64.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /.venv/lib/python3.8/site-packages/numpy/__init__.py
import numpy.random.bit_generator as __numpy_random_bit_generator


# no functions
# classes

class SFC64(__numpy_random_bit_generator.BitGenerator):
    """
    SFC64(seed=None)
    
        BitGenerator for Chris Doty-Humphrey's Small Fast Chaotic PRNG.
    
        Parameters
        ----------
        seed : {None, int, array_like[ints], SeedSequence}, optional
            A seed to initialize the `BitGenerator`. If None, then fresh,
            unpredictable entropy will be pulled from the OS. If an ``int`` or
            ``array_like[ints]`` is passed, then it will be passed to
            `SeedSequence` to derive the initial `BitGenerator` state. One may also
            pass in a `SeedSequence` instance.
    
        Notes
        -----
        ``SFC64`` is a 256-bit implementation of Chris Doty-Humphrey's Small Fast
        Chaotic PRNG ([1]_). ``SFC64`` has a few different cycles that one might be
        on, depending on the seed; the expected period will be about
        :math:`2^{255}` ([2]_). ``SFC64`` incorporates a 64-bit counter which means
        that the absolute minimum cycle length is :math:`2^{64}` and that distinct
        seeds will not run into each other for at least :math:`2^{64}` iterations.
    
        ``SFC64`` provides a capsule containing function pointers that produce
        doubles, and unsigned 32 and 64- bit integers. These are not
        directly consumable in Python and must be consumed by a ``Generator``
        or similar object that supports low-level access.
    
        **State and Seeding**
    
        The ``SFC64`` state vector consists of 4 unsigned 64-bit values. The last
        is a 64-bit counter that increments by 1 each iteration.
    
        The input seed is processed by `SeedSequence` to generate the first
        3 values, then the ``SFC64`` algorithm is iterated a small number of times
        to mix.
    
        **Compatibility Guarantee**
    
        ``SFC64`` makes a guarantee that a fixed seed will always produce the same
        random integer stream.
    
        References
        ----------
        .. [1] `"PractRand"
                <http://pracrand.sourceforge.net/RNG_engines.txt>`_
        .. [2] `"Random Invertible Mapping Statistics"
                <http://www.pcg-random.org/posts/random-invertible-mapping-statistics.html>`_
    """
    def __init__(self, seed=None): # real signature unknown; restored from __doc__
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


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0xffff9fb2b990>'


# variables with complex values

__all__ = [
    'SFC64',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9fb2b940>'

__spec__ = None # (!) real value is "ModuleSpec(name='numpy.random._sfc64', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9fb2b940>, origin='/.venv/lib/python3.8/site-packages/numpy/random/_sfc64.cpython-38-aarch64-linux-gnu.so')"

__test__ = {}

