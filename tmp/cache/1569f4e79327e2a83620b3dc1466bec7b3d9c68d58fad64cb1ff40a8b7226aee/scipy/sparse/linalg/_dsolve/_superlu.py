# encoding: utf-8
# module scipy.sparse.linalg._dsolve._superlu
# from /.venv/lib/python3.8/site-packages/scipy/sparse/linalg/_dsolve/_superlu.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

# functions

def gssv(A, B): # real signature unknown; restored from __doc__
    """
    Direct inversion of sparse matrix.
    
    X = gssv(A,B) solves A*X = B for X.
    """
    pass

def gstrf(A, *more): # real signature unknown; restored from __doc__
    """
    gstrf(A, ...)
    
    performs a factorization of the sparse matrix A=*(N,nnz,nzvals,rowind,colptr) and 
    returns a factored_lu object.
    
    Parameters
    ----------
    
    Matrix to be factorized is represented as N,nnz,nzvals,rowind,colptr
      as separate arguments.  This is compressed sparse column representation.
    
    N : int 
        number of rows and columns
    nnz : int
        number of non-zero elements
    nzvals : array
        non-zero values 
    rowind : array 
        row-index for this column (same size as nzvals)
    colptr : array 
        index into rowind for first non-zero value in this column
        size is (N+1).  Last value should be nnz. 
    
    Other Parameters
    ----------------
    options
        specifies additional options for SuperLU
        (same keys and values as in superlu_options_t C structure,
        and additionally 'Relax' and 'PanelSize')
    
    ilu : bool
        whether to perform an incomplete LU decomposition
        (default: false)
    """
    pass

# classes

class SuperLU(object):
    """
    LU factorization of a sparse matrix.
    
        Factorization is represented as::
    
            Pr @ A @ Pc = L @ U
    
        To construct these `SuperLU` objects, call the `splu` and `spilu`
        functions.
    
        Attributes
        ----------
        shape
        nnz
        perm_c
        perm_r
        L
        U
    
        Methods
        -------
        solve
    
        Notes
        -----
    
        .. versionadded:: 0.14.0
    
        Examples
        --------
        The LU decomposition can be used to solve matrix equations. Consider:
    
        >>> import numpy as np
        >>> from scipy.sparse import csc_matrix, linalg as sla
        >>> A = csc_matrix([[1,2,0,4],[1,0,0,1],[1,0,2,1],[2,2,1,0.]])
    
        This can be solved for a given right-hand side:
    
        >>> lu = sla.splu(A)
        >>> b = np.array([1, 2, 3, 4])
        >>> x = lu.solve(b)
        >>> A.dot(x)
        array([ 1.,  2.,  3.,  4.])
    
        The ``lu`` object also contains an explicit representation of the
        decomposition. The permutations are represented as mappings of
        indices:
    
        >>> lu.perm_r
        array([0, 2, 1, 3], dtype=int32)
        >>> lu.perm_c
        array([2, 0, 1, 3], dtype=int32)
    
        The L and U factors are sparse matrices in CSC format:
    
        >>> lu.L.A
        array([[ 1. ,  0. ,  0. ,  0. ],
               [ 0. ,  1. ,  0. ,  0. ],
               [ 0. ,  0. ,  1. ,  0. ],
               [ 1. ,  0.5,  0.5,  1. ]])
        >>> lu.U.A
        array([[ 2.,  0.,  1.,  4.],
               [ 0.,  2.,  1.,  1.],
               [ 0.,  0.,  1.,  1.],
               [ 0.,  0.,  0., -5.]])
    
        The permutation matrices can be constructed:
    
        >>> Pr = csc_matrix((np.ones(4), (lu.perm_r, np.arange(4))))
        >>> Pc = csc_matrix((np.ones(4), (np.arange(4), lu.perm_c)))
    
        We can reassemble the original matrix:
    
        >>> (Pr.T @ (lu.L @ lu.U) @ Pc.T).A
        array([[ 1.,  2.,  0.,  4.],
               [ 1.,  0.,  0.,  1.],
               [ 1.,  0.,  2.,  1.],
               [ 2.,  2.,  1.,  0.]])
    """
    def solve(self, rhs, trans=None): # real signature unknown; restored from __doc__
        """
        solve(rhs[, trans])
        
            Solves linear system of equations with one or several right-hand sides.
        
            Parameters
            ----------
            rhs : ndarray, shape (n,) or (n, k)
                Right hand side(s) of equation
            trans : {'N', 'T', 'H'}, optional
                Type of system to solve::
        
                    'N':   A   @ x == rhs  (default)
                    'T':   A^T @ x == rhs
                    'H':   A^H @ x == rhs
        
                i.e., normal, transposed, and hermitian conjugate.
        
            Returns
            -------
            x : ndarray, shape ``rhs.shape``
                Solution vector(s)
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    L = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Lower triangular factor with unit diagonal as a
    `scipy.sparse.csc_matrix`.

    .. versionadded:: 0.14.0"""

    nnz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of nonzero elements in the matrix."""

    perm_c = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Permutation Pc represented as an array of indices.

    The column permutation matrix can be reconstructed via:

    >>> Pc = np.zeros((n, n))
    >>> Pc[np.arange(n), perm_c] = 1"""

    perm_r = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Permutation Pr represented as an array of indices.

    The row permutation matrix can be reconstructed via:

    >>> Pr = np.zeros((n, n))
    >>> Pr[perm_r, np.arange(n)] = 1"""

    shape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Shape of the original matrix as a tuple of ints."""

    U = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Upper triangular factor as a `scipy.sparse.csc_matrix`.

    .. versionadded:: 0.14.0"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff995fa6d0>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.sparse.linalg._dsolve._superlu', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff995fa6d0>, origin='/.venv/lib/python3.8/site-packages/scipy/sparse/linalg/_dsolve/_superlu.cpython-38-aarch64-linux-gnu.so')"

