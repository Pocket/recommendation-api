# encoding: utf-8
# module scipy.special._test_internal
# from /.venv/lib/python3.8/site-packages/scipy/special/_test_internal.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
"""
Wrappers to allow unit tests of internal C code.

This module includes wrappers for:
* Tests of the functions add_round_up() and add_round_down() from _round.h
* Several double-double functions from cephes/dd_real.c
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /.venv/lib/python3.8/site-packages/numpy/__init__.py

# functions

def assert_(val, msg=None): # reliably restored by inspect
    """
    Assert that works in release mode.
        Accepts callable msg to allow deferring evaluation until failure.
    
        The Python built-in ``assert`` does not work when executing code in
        optimized mode (the ``-O`` flag) - no byte-code is generated for it.
    
        For documentation on usage, refer to the Python documentation.
    """
    pass

def assert_allclose(actual, desired, rtol=1e-07, atol=0, equal_nan=True, err_msg=None, verbose=True): # reliably restored by inspect
    """
    Raises an AssertionError if two objects are not equal up to desired
        tolerance.
    
        Given two array_like objects, check that their shapes and all elements
        are equal (but see the Notes for the special handling of a scalar). An
        exception is raised if the shapes mismatch or any values conflict. In 
        contrast to the standard usage in numpy, NaNs are compared like numbers,
        no assertion is raised if both objects have NaNs in the same positions.
    
        The test is equivalent to ``allclose(actual, desired, rtol, atol)`` (note
        that ``allclose`` has different default values). It compares the difference
        between `actual` and `desired` to ``atol + rtol * abs(desired)``.
    
        .. versionadded:: 1.5.0
    
        Parameters
        ----------
        actual : array_like
            Array obtained.
        desired : array_like
            Array desired.
        rtol : float, optional
            Relative tolerance.
        atol : float, optional
            Absolute tolerance.
        equal_nan : bool, optional.
            If True, NaNs will compare equal.
        err_msg : str, optional
            The error message to be printed in case of failure.
        verbose : bool, optional
            If True, the conflicting values are appended to the error message.
    
        Raises
        ------
        AssertionError
            If actual and desired are not equal up to specified precision.
    
        See Also
        --------
        assert_array_almost_equal_nulp, assert_array_max_ulp
    
        Notes
        -----
        When one of `actual` and `desired` is a scalar and the other is
        array_like, the function checks that each element of the array_like
        object is equal to the scalar.
    
        Examples
        --------
        >>> x = [1e-5, 1e-3, 1e-1]
        >>> y = np.arccos(np.cos(x))
        >>> np.testing.assert_allclose(x, y, rtol=1e-5, atol=0)
    """
    pass

def have_fenv(*args, **kwargs): # real signature unknown
    pass

def random_double(*args, **kwargs): # real signature unknown
    pass

def test_add_round(*args, **kwargs): # real signature unknown
    pass

def _dd_exp(*args, **kwargs): # real signature unknown
    pass

def _dd_expm1(*args, **kwargs): # real signature unknown
    pass

def _dd_log(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924eb0>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.special._test_internal', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924eb0>, origin='/.venv/lib/python3.8/site-packages/scipy/special/_test_internal.cpython-38-aarch64-linux-gnu.so')"

__test__ = {}

