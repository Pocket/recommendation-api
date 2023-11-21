# encoding: utf-8
# module scipy.optimize._bglu_dense
# from /.venv/lib/python3.8/site-packages/scipy/optimize/_bglu_dense.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /.venv/lib/python3.8/site-packages/numpy/__init__.py
from time import timer


# functions

def lu_factor(a, overwrite_a=False, check_finite=True): # reliably restored by inspect
    """
    Compute pivoted LU decomposition of a matrix.
    
        The decomposition is::
    
            A = P L U
    
        where P is a permutation matrix, L lower triangular with unit
        diagonal elements, and U upper triangular.
    
        Parameters
        ----------
        a : (M, N) array_like
            Matrix to decompose
        overwrite_a : bool, optional
            Whether to overwrite data in A (may increase performance)
        check_finite : bool, optional
            Whether to check that the input matrix contains only finite numbers.
            Disabling may give a performance gain, but may result in problems
            (crashes, non-termination) if the inputs do contain infinities or NaNs.
    
        Returns
        -------
        lu : (M, N) ndarray
            Matrix containing U in its upper triangle, and L in its lower triangle.
            The unit diagonal elements of L are not stored.
        piv : (N,) ndarray
            Pivot indices representing the permutation matrix P:
            row i of matrix was interchanged with row piv[i].
    
        See Also
        --------
        lu : gives lu factorization in more user-friendly format
        lu_solve : solve an equation system using the LU factorization of a matrix
    
        Notes
        -----
        This is a wrapper to the ``*GETRF`` routines from LAPACK. Unlike
        :func:`lu`, it outputs the L and U factors into a single array
        and returns pivot indices instead of a permutation matrix.
    
        Examples
        --------
        >>> import numpy as np
        >>> from scipy.linalg import lu_factor
        >>> A = np.array([[2, 5, 8, 7], [5, 2, 2, 8], [7, 5, 6, 6], [5, 4, 4, 8]])
        >>> lu, piv = lu_factor(A)
        >>> piv
        array([2, 2, 3, 3], dtype=int32)
    
        Convert LAPACK's ``piv`` array to NumPy index and test the permutation
    
        >>> piv_py = [2, 0, 3, 1]
        >>> L, U = np.tril(lu, k=-1) + np.eye(4), np.triu(lu)
        >>> np.allclose(A[piv_py] - L @ U, np.zeros((4, 4)))
        True
    """
    pass

def lu_solve(lu_and_piv, b, trans=0, overwrite_b=False, check_finite=True): # reliably restored by inspect
    """
    Solve an equation system, a x = b, given the LU factorization of a
    
        Parameters
        ----------
        (lu, piv)
            Factorization of the coefficient matrix a, as given by lu_factor
        b : array
            Right-hand side
        trans : {0, 1, 2}, optional
            Type of system to solve:
    
            =====  =========
            trans  system
            =====  =========
            0      a x   = b
            1      a^T x = b
            2      a^H x = b
            =====  =========
        overwrite_b : bool, optional
            Whether to overwrite data in b (may increase performance)
        check_finite : bool, optional
            Whether to check that the input matrices contain only finite numbers.
            Disabling may give a performance gain, but may result in problems
            (crashes, non-termination) if the inputs do contain infinities or NaNs.
    
        Returns
        -------
        x : array
            Solution to the system
    
        See Also
        --------
        lu_factor : LU factorize a matrix
    
        Examples
        --------
        >>> import numpy as np
        >>> from scipy.linalg import lu_factor, lu_solve
        >>> A = np.array([[2, 5, 8, 7], [5, 2, 2, 8], [7, 5, 6, 6], [5, 4, 4, 8]])
        >>> b = np.array([1, 1, 1, 1])
        >>> lu, piv = lu_factor(A)
        >>> x = lu_solve((lu, piv), b)
        >>> np.allclose(A @ x - b, np.zeros((4,)))
        True
    """
    pass

def solve(a, b, sym_pos=False, lower=False, overwrite_a=False, overwrite_b=False, check_finite=True, assume_a=None, transposed=False): # reliably restored by inspect
    """
    Solves the linear equation set ``a @ x == b`` for the unknown ``x``
        for square `a` matrix.
    
        If the data matrix is known to be a particular type then supplying the
        corresponding string to ``assume_a`` key chooses the dedicated solver.
        The available options are
    
        ===================  ========
         generic matrix       'gen'
         symmetric            'sym'
         hermitian            'her'
         positive definite    'pos'
        ===================  ========
    
        If omitted, ``'gen'`` is the default structure.
    
        The datatype of the arrays define which solver is called regardless
        of the values. In other words, even when the complex array entries have
        precisely zero imaginary parts, the complex solver will be called based
        on the data type of the array.
    
        Parameters
        ----------
        a : (N, N) array_like
            Square input data
        b : (N, NRHS) array_like
            Input data for the right hand side.
        sym_pos : bool, default: False, deprecated
            Assume `a` is symmetric and positive definite.
    
            .. deprecated:: 0.19.0
                This keyword is deprecated and should be replaced by using
               ``assume_a = 'pos'``. `sym_pos` will be removed in SciPy 1.11.0.
    
        lower : bool, default: False
            Ignored if ``assume_a == 'gen'`` (the default). If True, the
            calculation uses only the data in the lower triangle of `a`;
            entries above the diagonal are ignored. If False (default), the
            calculation uses only the data in the upper triangle of `a`; entries
            below the diagonal are ignored.
        overwrite_a : bool, default: False
            Allow overwriting data in `a` (may enhance performance).
        overwrite_b : bool, default: False
            Allow overwriting data in `b` (may enhance performance).
        check_finite : bool, default: True
            Whether to check that the input matrices contain only finite numbers.
            Disabling may give a performance gain, but may result in problems
            (crashes, non-termination) if the inputs do contain infinities or NaNs.
        assume_a : str, {'gen', 'sym', 'her', 'pos'}
            Valid entries are explained above.
        transposed : bool, default: False
            If True, solve ``a.T @ x == b``. Raises `NotImplementedError`
            for complex `a`.
    
        Returns
        -------
        x : (N, NRHS) ndarray
            The solution array.
    
        Raises
        ------
        ValueError
            If size mismatches detected or input a is not square.
        LinAlgError
            If the matrix is singular.
        LinAlgWarning
            If an ill-conditioned input a is detected.
        NotImplementedError
            If transposed is True and input a is a complex matrix.
    
        Notes
        -----
        If the input b matrix is a 1-D array with N elements, when supplied
        together with an NxN input a, it is assumed as a valid column vector
        despite the apparent size mismatch. This is compatible with the
        numpy.dot() behavior and the returned result is still 1-D array.
    
        The generic, symmetric, Hermitian and positive definite solutions are
        obtained via calling ?GESV, ?SYSV, ?HESV, and ?POSV routines of
        LAPACK respectively.
    
        Examples
        --------
        Given `a` and `b`, solve for `x`:
    
        >>> import numpy as np
        >>> a = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]])
        >>> b = np.array([2, 4, -1])
        >>> from scipy import linalg
        >>> x = linalg.solve(a, b)
        >>> x
        array([ 2., -2.,  9.])
        >>> np.dot(a, x) == b
        array([ True,  True,  True], dtype=bool)
    """
    pass

def solve_triangular(a, b, trans=0, lower=False, unit_diagonal=False, overwrite_b=False, check_finite=True): # reliably restored by inspect
    """
    Solve the equation `a x = b` for `x`, assuming a is a triangular matrix.
    
        Parameters
        ----------
        a : (M, M) array_like
            A triangular matrix
        b : (M,) or (M, N) array_like
            Right-hand side matrix in `a x = b`
        lower : bool, optional
            Use only data contained in the lower triangle of `a`.
            Default is to use upper triangle.
        trans : {0, 1, 2, 'N', 'T', 'C'}, optional
            Type of system to solve:
    
            ========  =========
            trans     system
            ========  =========
            0 or 'N'  a x  = b
            1 or 'T'  a^T x = b
            2 or 'C'  a^H x = b
            ========  =========
        unit_diagonal : bool, optional
            If True, diagonal elements of `a` are assumed to be 1 and
            will not be referenced.
        overwrite_b : bool, optional
            Allow overwriting data in `b` (may enhance performance)
        check_finite : bool, optional
            Whether to check that the input matrices contain only finite numbers.
            Disabling may give a performance gain, but may result in problems
            (crashes, non-termination) if the inputs do contain infinities or NaNs.
    
        Returns
        -------
        x : (M,) or (M, N) ndarray
            Solution to the system `a x = b`.  Shape of return matches `b`.
    
        Raises
        ------
        LinAlgError
            If `a` is singular
    
        Notes
        -----
        .. versionadded:: 0.9.0
    
        Examples
        --------
        Solve the lower triangular system a x = b, where::
    
                 [3  0  0  0]       [4]
            a =  [2  1  0  0]   b = [2]
                 [1  0  1  0]       [4]
                 [1  1  1  1]       [2]
    
        >>> import numpy as np
        >>> from scipy.linalg import solve_triangular
        >>> a = np.array([[3, 0, 0, 0], [2, 1, 0, 0], [1, 0, 1, 0], [1, 1, 1, 1]])
        >>> b = np.array([4, 2, 4, 2])
        >>> x = solve_triangular(a, b, lower=True)
        >>> x
        array([ 1.33333333, -0.66666667,  2.66666667, -1.33333333])
        >>> a.dot(x)  # Check the result
        array([ 4.,  2.,  4.,  2.])
    """
    pass

def _consider_refactor(*args, **kwargs): # real signature unknown
    """
    This decorator records the time spent in the major BGLU
        routines - refactor, update, and solve - in order to
        calculate the average time required to solve a system.
        It also forces PLU factorization of the basis matrix from
        scratch to minimize the average solve time and to
        accumulation of roundoff error.
    
        Immediately after PLU factorization, the average solve time
        will be rather high because PLU factorization is slow. For
        some number of factor updates, the average solve time is
        expected to decrease because the updates and solves are fast.
        However, updates increase the compexity of the factorization,
        so solve times are expected to increase with each update.
        When the average solve time stops decreasing and begins
        increasing, we perform PLU factorization from scratch rather
        than updating. PLU factorization is also performed after the
        maximum permitted number of updates is reached to prevent
        further accumulation of roundoff error.
    """
    pass

def __pyx_unpickle_BGLU(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_LU(*args, **kwargs): # real signature unknown
    pass

# classes

class LU(object):
    """ Represents PLU factorization of a basis matrix with naive rank-one updates """
    def solve(self, *args, **kwargs): # real signature unknown
        """ Solve B @ v = q """
        pass

    def update(self, *args, **kwargs): # real signature unknown
        """ Rank-one update to basis and basis matrix """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """ Given matrix A and basis indices b, form basis matrix B """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    A = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    b = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    B = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    m = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class BGLU(LU):
    """
    Represents PLU factorization with Golub rank-one updates from
        Bartels, Richard H. "A stabilization of the simplex method."
        Numerische Mathematik 16.5 (1971): 414-434.
    """
    def perform_perm(self, *args, **kwargs): # real signature unknown
        """
        Perform individual row swaps defined in p returned by factor_lu to
                generate final permutation indices pi
        """
        pass

    def refactor(self, *args, **kwargs): # real signature unknown
        pass

    def solve(self, *args, **kwargs): # real signature unknown
        pass

    def update(self, *args, **kwargs): # real signature unknown
        pass

    def update_basis(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        Given matrix A and basis indices b, perform PLU factorization of
                basis matrix B
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    average_solve_times = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bglu_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    L = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mast = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_updates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ops_list = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pi = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    plu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    solves = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    U = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    updates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class LinAlgError(Exception):
    """
    Generic Python-exception-derived object raised by linalg functions.
    
        General purpose exception class, derived from Python's exception.Exception
        class, programmatically raised in linalg functions when a Linear
        Algebra-related condition would prevent further correct execution of the
        function.
    
        Parameters
        ----------
        None
    
        Examples
        --------
        >>> from numpy import linalg as LA
        >>> LA.inv(np.zeros((2,2)))
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
          File "...linalg.py", line 350,
            in inv return wrap(solve(a, identity(a.shape[0], dtype=a.dtype)))
          File "...linalg.py", line 249,
            in solve
            raise LinAlgError('Singular matrix')
        numpy.linalg.LinAlgError: Singular matrix
    """
    def __init__(self, Singular_matrix): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__all__ = [
    'LU',
    'BGLU',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff929f1190>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.optimize._bglu_dense', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff929f1190>, origin='/.venv/lib/python3.8/site-packages/scipy/optimize/_bglu_dense.cpython-38-aarch64-linux-gnu.so')"

__test__ = {}

