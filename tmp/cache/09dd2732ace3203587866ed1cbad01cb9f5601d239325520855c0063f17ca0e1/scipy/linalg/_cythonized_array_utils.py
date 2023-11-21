# encoding: utf-8
# module scipy.linalg._cythonized_array_utils
# from /.venv/lib/python3.8/site-packages/scipy/linalg/_cythonized_array_utils.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /.venv/lib/python3.8/site-packages/numpy/__init__.py

# functions

def bandwidth(a): # real signature unknown; restored from __doc__
    """
    bandwidth(a)
    Return the lower and upper bandwidth of a 2D numeric array.
    
        Parameters
        ----------
        a : ndarray
            Input array of size (N, M)
    
        Returns
        -------
        lu : tuple
            2-tuple of ints indicating the lower and upper bandwith. A zero
            denotes no sub- or super-diagonal on that side (triangular), and,
            say for N rows (N-1) means that side is full. Same example applies
            to the upper triangular part with (M-1).
    
        Raises
        ------
        TypeError
            If the dtype of the array is not supported, in particular, NumPy
            float16, float128 and complex256 dtypes.
    
        Notes
        -----
        This helper function simply runs over the array looking for the nonzero
        entries whether there exists a banded structure in the array or not. Hence,
        the performance depends on the density of nonzero entries and also
        memory-layout. Fortran- or C- contiguous arrays are handled best and
        otherwise suffers from extra random memory access cost.
    
        The strategy is to look for only untested band elements in the upper
        and lower triangular parts separately; depending on the memory layout
        we scan row-wise or column-wise. Moreover, say we are scanning rows
        and in the 6th row, 4th entry is nonzero then, on the succeeding rows
        the horizontal search is done only up to that band entries since we know
        that band is occupied. Therefore, a completely dense matrix scan cost is
        in the the order of n.
    
        Examples
        --------
        >>> import numpy as np
        >>> from scipy.linalg import bandwidth
        >>> A = np.array([[3., 0., 0., 0., 0.],
        ...               [0., 4., 0., 0., 0.],
        ...               [0., 0., 5., 1., 0.],
        ...               [8., 0., 0., 6., 2.],
        ...               [0., 9., 0., 0., 7.]])
        >>> bandwidth(A)
        (3, 1)
    """
    pass

def bandwidth_c(*args, **kwargs): # real signature unknown
    pass

def bandwidth_noncontig(*args, **kwargs): # real signature unknown
    pass

def ishermitian(a, atol=None, rtol=None): # real signature unknown; restored from __doc__
    """
    ishermitian(a, atol=None, rtol=None)
    Check if a square 2D array is Hermitian.
    
        Parameters
        ----------
        a : ndarray
            Input array of size (N, N)
    
        atol : float, optional
            Absolute error bound
    
        rtol : float, optional
            Relative error bound
    
        Returns
        -------
        her : bool
            Returns True if the array Hermitian.
    
        Raises
        ------
        TypeError
            If the dtype of the array is not supported, in particular, NumPy
            float16, float128 and complex256 dtypes.
    
        See Also
        --------
        issymmetric : Check if a square 2D array is symmetric
    
        Notes
        -----
        For square empty arrays the result is returned True by convention.
    
        `numpy.inf` will be treated as a number, that is to say ``[[1, inf],
        [inf, 2]]`` will return ``True``. On the other hand `numpy.NaN` is never
        symmetric, say, ``[[1, nan], [nan, 2]]`` will return ``False``.
    
        When ``atol`` and/or ``rtol`` are set to , then the comparison is performed
        by `numpy.allclose` and the tolerance values are passed to it. Otherwise an
        exact comparison against zero is performed by internal functions. Hence
        performance can improve or degrade depending on the size and dtype of the
        array. If one of ``atol`` or ``rtol`` given the other one is automatically
        set to zero.
    
        Examples
        --------
        >>> import numpy as np
        >>> from scipy.linalg import ishermitian
        >>> A = np.arange(9).reshape(3, 3)
        >>> A = A + A.T
        >>> ishermitian(A)
        True
        >>> A = np.array([[1., 2. + 3.j], [2. - 3.j, 4.]])
        >>> ishermitian(A)
        True
        >>> Ac = np.array([[1. + 1.j, 3.j], [3.j, 2.]])
        >>> ishermitian(Ac)  # not Hermitian but symmetric
        False
        >>> Af = np.array([[0, 1 + 1j], [1 - (1+1e-12)*1j, 0]])
        >>> ishermitian(Af)
        False
        >>> ishermitian(Af, atol=5e-11) # almost hermitian with atol
        True
    """
    pass

def issymmetric(a, atol=None, rtol=None): # real signature unknown; restored from __doc__
    """
    issymmetric(a, atol=None, rtol=None)
    Check if a square 2D array is symmetric.
    
        Parameters
        ----------
        a : ndarray
            Input array of size (N, N).
    
        atol : float, optional
            Absolute error bound
    
        rtol : float, optional
            Relative error bound
    
        Returns
        -------
        sym : bool
            Returns True if the array symmetric.
    
        Raises
        ------
        TypeError
            If the dtype of the array is not supported, in particular, NumPy
            float16, float128 and complex256 dtypes for exact comparisons.
    
        See Also
        --------
        ishermitian : Check if a square 2D array is Hermitian
    
        Notes
        -----
        For square empty arrays the result is returned True by convention. Complex
        valued arrays are tested for symmetricity and not for being Hermitian (see
        examples)
    
        The diagonal of the array is not scanned. Thus if there are infs, NaNs or
        similar problematic entries on the diagonal, they will be ignored. However,
        `numpy.inf` will be treated as a number, that is to say ``[[1, inf],
        [inf, 2]]`` will return ``True``. On the other hand `numpy.NaN` is never
        symmetric, say, ``[[1, nan], [nan, 2]]`` will return ``False``.
    
        When ``atol`` and/or ``rtol`` are set to , then the comparison is performed
        by `numpy.allclose` and the tolerance values are passed to it. Otherwise an
        exact comparison against zero is performed by internal functions. Hence
        performance can improve or degrade depending on the size and dtype of the
        array. If one of ``atol`` or ``rtol`` given the other one is automatically
        set to zero.
    
        Examples
        --------
        >>> import numpy as np
        >>> from scipy.linalg import issymmetric
        >>> A = np.arange(9).reshape(3, 3)
        >>> A = A + A.T
        >>> issymmetric(A)
        True
        >>> Ac = np.array([[1. + 1.j, 3.j], [3.j, 2.]])
        >>> issymmetric(Ac)  # not Hermitian but symmetric
        True
    """
    pass

def is_sym_her_complex_c(*args, **kwargs): # real signature unknown
    pass

def is_sym_her_complex_noncontig(*args, **kwargs): # real signature unknown
    pass

def is_sym_her_real_c(*args, **kwargs): # real signature unknown
    pass

def is_sym_her_real_noncontig(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__all__ = [
    'bandwidth',
    'issymmetric',
    'ishermitian',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9f8f5a00>'

__pyx_capi__ = {
    '__pyx_fuse_0band_check_internal_c': None, # (!) real value is '<capsule object "__pyx_ctuple_int__and_int (__Pyx_memviewslice)" at 0xffff9f878300>'
    '__pyx_fuse_0is_sym_her_complex_c_internal': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice)" at 0xffff9f8788d0>'
    '__pyx_fuse_0is_sym_her_real_c_internal': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice)" at 0xffff9f878660>'
    '__pyx_fuse_0swap_c_and_f_layout': None, # (!) real value is '<capsule object "void (float *, float *, int, int, int)" at 0xffff9f878210>'
    '__pyx_fuse_10band_check_internal_c': None, # (!) real value is '<capsule object "__pyx_ctuple_int__and_int (__Pyx_memviewslice)" at 0xffff9f8785d0>'
    '__pyx_fuse_10is_sym_her_real_c_internal': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice)" at 0xffff9f878840>'
    '__pyx_fuse_11band_check_internal_c': None, # (!) real value is '<capsule object "__pyx_ctuple_int__and_int (__Pyx_memviewslice)" at 0xffff9f878600>'
    '__pyx_fuse_11is_sym_her_real_c_internal': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice)" at 0xffff9f878870>'
    '__pyx_fuse_12band_check_internal_c': None, # (!) real value is '<capsule object "__pyx_ctuple_int__and_int (__Pyx_memviewslice)" at 0xffff9f878630>'
    '__pyx_fuse_12is_sym_her_real_c_internal': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice)" at 0xffff9f8788a0>'
    '__pyx_fuse_1band_check_internal_c': None, # (!) real value is '<capsule object "__pyx_ctuple_int__and_int (__Pyx_memviewslice)" at 0xffff9f878330>'
    '__pyx_fuse_1is_sym_her_complex_c_internal': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice)" at 0xffff9f878900>'
    '__pyx_fuse_1is_sym_her_real_c_internal': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice)" at 0xffff9f878690>'
    '__pyx_fuse_1swap_c_and_f_layout': None, # (!) real value is '<capsule object "void (double *, double *, int, int, int)" at 0xffff9f8784b0>'
    '__pyx_fuse_2band_check_internal_c': None, # (!) real value is '<capsule object "__pyx_ctuple_int__and_int (__Pyx_memviewslice)" at 0xffff9f878390>'
    '__pyx_fuse_2is_sym_her_real_c_internal': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice)" at 0xffff9f8786c0>'
    '__pyx_fuse_2swap_c_and_f_layout': None, # (!) real value is '<capsule object "void (__pyx_t_float_complex *, __pyx_t_float_complex *, int, int, int)" at 0xffff9f878450>'
    '__pyx_fuse_3band_check_internal_c': None, # (!) real value is '<capsule object "__pyx_ctuple_int__and_int (__Pyx_memviewslice)" at 0xffff9f8783c0>'
    '__pyx_fuse_3is_sym_her_real_c_internal': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice)" at 0xffff9f8786f0>'
    '__pyx_fuse_3swap_c_and_f_layout': None, # (!) real value is '<capsule object "void (__pyx_t_double_complex *, __pyx_t_double_complex *, int, int, int)" at 0xffff9f878510>'
    '__pyx_fuse_4band_check_internal_c': None, # (!) real value is '<capsule object "__pyx_ctuple_int__and_int (__Pyx_memviewslice)" at 0xffff9f8783f0>'
    '__pyx_fuse_4is_sym_her_real_c_internal': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice)" at 0xffff9f878720>'
    '__pyx_fuse_5band_check_internal_c': None, # (!) real value is '<capsule object "__pyx_ctuple_int__and_int (__Pyx_memviewslice)" at 0xffff9f878420>'
    '__pyx_fuse_5is_sym_her_real_c_internal': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice)" at 0xffff9f878750>'
    '__pyx_fuse_6band_check_internal_c': None, # (!) real value is '<capsule object "__pyx_ctuple_int__and_int (__Pyx_memviewslice)" at 0xffff9f878540>'
    '__pyx_fuse_6is_sym_her_real_c_internal': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice)" at 0xffff9f878780>'
    '__pyx_fuse_7band_check_internal_c': None, # (!) real value is '<capsule object "__pyx_ctuple_int__and_int (__Pyx_memviewslice)" at 0xffff9f8784e0>'
    '__pyx_fuse_7is_sym_her_real_c_internal': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice)" at 0xffff9f8787b0>'
    '__pyx_fuse_8band_check_internal_c': None, # (!) real value is '<capsule object "__pyx_ctuple_int__and_int (__Pyx_memviewslice)" at 0xffff9f878570>'
    '__pyx_fuse_8is_sym_her_real_c_internal': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice)" at 0xffff9f8787e0>'
    '__pyx_fuse_9band_check_internal_c': None, # (!) real value is '<capsule object "__pyx_ctuple_int__and_int (__Pyx_memviewslice)" at 0xffff9f8785a0>'
    '__pyx_fuse_9is_sym_her_real_c_internal': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice)" at 0xffff9f878810>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.linalg._cythonized_array_utils', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9f8f5a00>, origin='/.venv/lib/python3.8/site-packages/scipy/linalg/_cythonized_array_utils.cpython-38-aarch64-linux-gnu.so')"

__test__ = {
    'bandwidth (line 46)': 'Return the lower and upper bandwidth of a 2D numeric array.\n\n    Parameters\n    ----------\n    a : ndarray\n        Input array of size (N, M)\n\n    Returns\n    -------\n    lu : tuple\n        2-tuple of ints indicating the lower and upper bandwith. A zero\n        denotes no sub- or super-diagonal on that side (triangular), and,\n        say for N rows (N-1) means that side is full. Same example applies\n        to the upper triangular part with (M-1).\n\n    Raises\n    ------\n    TypeError\n        If the dtype of the array is not supported, in particular, NumPy\n        float16, float128 and complex256 dtypes.\n\n    Notes\n    -----\n    This helper function simply runs over the array looking for the nonzero\n    entries whether there exists a banded structure in the array or not. Hence,\n    the performance depends on the density of nonzero entries and also\n    memory-layout. Fortran- or C- contiguous arrays are handled best and\n    otherwise suffers from extra random memory access cost.\n\n    The strategy is to look for only untested band elements in the upper\n    and lower triangular parts separately; depending on the memory layout\n    we scan row-wise or column-wise. Moreover, say we are scanning rows\n    and in the 6th row, 4th entry is nonzero then, on the succeeding rows\n    the horizontal search is done only up to that band entries since we know\n    that band is occupied. Therefore, a completely dense matrix scan cost is\n    in the the order of n.\n\n    Examples\n    --------\n    >>> import numpy as np\n    >>> from scipy.linalg import bandwidth\n    >>> A = np.array([[3., 0., 0., 0., 0.],\n    ...               [0., 4., 0., 0., 0.],\n    ...               [0., 0., 5., 1., 0.],\n    ...               [8., 0., 0., 6., 2.],\n    ...               [0., 9., 0., 0., 7.]])\n    >>> bandwidth(A)\n    (3, 1)\n\n    ',
    'ishermitian (line 322)': 'Check if a square 2D array is Hermitian.\n\n    Parameters\n    ----------\n    a : ndarray\n        Input array of size (N, N)\n\n    atol : float, optional\n        Absolute error bound\n\n    rtol : float, optional\n        Relative error bound\n\n    Returns\n    -------\n    her : bool\n        Returns True if the array Hermitian.\n\n    Raises\n    ------\n    TypeError\n        If the dtype of the array is not supported, in particular, NumPy\n        float16, float128 and complex256 dtypes.\n\n    See Also\n    --------\n    issymmetric : Check if a square 2D array is symmetric\n\n    Notes\n    -----\n    For square empty arrays the result is returned True by convention.\n\n    `numpy.inf` will be treated as a number, that is to say ``[[1, inf],\n    [inf, 2]]`` will return ``True``. On the other hand `numpy.NaN` is never\n    symmetric, say, ``[[1, nan], [nan, 2]]`` will return ``False``.\n\n    When ``atol`` and/or ``rtol`` are set to , then the comparison is performed\n    by `numpy.allclose` and the tolerance values are passed to it. Otherwise an\n    exact comparison against zero is performed by internal functions. Hence\n    performance can improve or degrade depending on the size and dtype of the\n    array. If one of ``atol`` or ``rtol`` given the other one is automatically\n    set to zero.\n\n    Examples\n    --------\n    >>> import numpy as np\n    >>> from scipy.linalg import ishermitian\n    >>> A = np.arange(9).reshape(3, 3)\n    >>> A = A + A.T\n    >>> ishermitian(A)\n    True\n    >>> A = np.array([[1., 2. + 3.j], [2. - 3.j, 4.]])\n    >>> ishermitian(A)\n    True\n    >>> Ac = np.array([[1. + 1.j, 3.j], [3.j, 2.]])\n    >>> ishermitian(Ac)  # not Hermitian but symmetric\n    False\n    >>> Af = np.array([[0, 1 + 1j], [1 - (1+1e-12)*1j, 0]])\n    >>> ishermitian(Af)\n    False\n    >>> ishermitian(Af, atol=5e-11) # almost hermitian with atol\n    True\n\n    ',
    'issymmetric (line 192)': 'Check if a square 2D array is symmetric.\n\n    Parameters\n    ----------\n    a : ndarray\n        Input array of size (N, N).\n\n    atol : float, optional\n        Absolute error bound\n\n    rtol : float, optional\n        Relative error bound\n\n    Returns\n    -------\n    sym : bool\n        Returns True if the array symmetric.\n\n    Raises\n    ------\n    TypeError\n        If the dtype of the array is not supported, in particular, NumPy\n        float16, float128 and complex256 dtypes for exact comparisons.\n\n    See Also\n    --------\n    ishermitian : Check if a square 2D array is Hermitian\n\n    Notes\n    -----\n    For square empty arrays the result is returned True by convention. Complex\n    valued arrays are tested for symmetricity and not for being Hermitian (see\n    examples)\n\n    The diagonal of the array is not scanned. Thus if there are infs, NaNs or\n    similar problematic entries on the diagonal, they will be ignored. However,\n    `numpy.inf` will be treated as a number, that is to say ``[[1, inf],\n    [inf, 2]]`` will return ``True``. On the other hand `numpy.NaN` is never\n    symmetric, say, ``[[1, nan], [nan, 2]]`` will return ``False``.\n\n    When ``atol`` and/or ``rtol`` are set to , then the comparison is performed\n    by `numpy.allclose` and the tolerance values are passed to it. Otherwise an\n    exact comparison against zero is performed by internal functions. Hence\n    performance can improve or degrade depending on the size and dtype of the\n    array. If one of ``atol`` or ``rtol`` given the other one is automatically\n    set to zero.\n\n    Examples\n    --------\n    >>> import numpy as np\n    >>> from scipy.linalg import issymmetric\n    >>> A = np.arange(9).reshape(3, 3)\n    >>> A = A + A.T\n    >>> issymmetric(A)\n    True\n    >>> Ac = np.array([[1. + 1.j, 3.j], [3.j, 2.]])\n    >>> issymmetric(Ac)  # not Hermitian but symmetric\n    True\n\n    ',
}

