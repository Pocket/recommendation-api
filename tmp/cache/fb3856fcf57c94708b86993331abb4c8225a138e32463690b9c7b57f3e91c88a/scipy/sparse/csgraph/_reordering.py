# encoding: utf-8
# module scipy.sparse.csgraph._reordering
# from /.venv/lib/python3.8/site-packages/scipy/sparse/csgraph/_reordering.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /.venv/lib/python3.8/site-packages/numpy/__init__.py
from scipy.sparse.csgraph._matching import maximum_bipartite_matching

from _warnings import warn

import numpy as __numpy
import scipy.sparse._base as __scipy_sparse__base
import scipy.sparse._compressed as __scipy_sparse__compressed


# functions

def isspmatrix(x): # reliably restored by inspect
    """
    Is x of a sparse matrix type?
    
        Parameters
        ----------
        x
            object to check for being a sparse matrix
    
        Returns
        -------
        bool
            True if x is a sparse matrix, False otherwise
    
        Notes
        -----
        issparse and isspmatrix are aliases for the same function.
    
        Examples
        --------
        >>> from scipy.sparse import csr_matrix, isspmatrix
        >>> isspmatrix(csr_matrix([[5]]))
        True
    
        >>> from scipy.sparse import isspmatrix
        >>> isspmatrix(5)
        False
    """
    pass

def isspmatrix_coo(x): # reliably restored by inspect
    """
    Is x of coo_matrix type?
    
        Parameters
        ----------
        x
            object to check for being a coo matrix
    
        Returns
        -------
        bool
            True if x is a coo matrix, False otherwise
    
        Examples
        --------
        >>> from scipy.sparse import coo_matrix, isspmatrix_coo
        >>> isspmatrix_coo(coo_matrix([[5]]))
        True
    
        >>> from scipy.sparse import coo_matrix, csr_matrix, isspmatrix_coo
        >>> isspmatrix_coo(csr_matrix([[5]]))
        False
    """
    pass

def isspmatrix_csc(x): # reliably restored by inspect
    """
    Is x of csc_matrix type?
    
        Parameters
        ----------
        x
            object to check for being a csc matrix
    
        Returns
        -------
        bool
            True if x is a csc matrix, False otherwise
    
        Examples
        --------
        >>> from scipy.sparse import csc_matrix, isspmatrix_csc
        >>> isspmatrix_csc(csc_matrix([[5]]))
        True
    
        >>> from scipy.sparse import csc_matrix, csr_matrix, isspmatrix_csc
        >>> isspmatrix_csc(csr_matrix([[5]]))
        False
    """
    pass

def isspmatrix_csr(x): # reliably restored by inspect
    """
    Is x of csr_matrix type?
    
        Parameters
        ----------
        x
            object to check for being a csr matrix
    
        Returns
        -------
        bool
            True if x is a csr matrix, False otherwise
    
        Examples
        --------
        >>> from scipy.sparse import csr_matrix, isspmatrix_csr
        >>> isspmatrix_csr(csr_matrix([[5]]))
        True
    
        >>> from scipy.sparse import csc_matrix, csr_matrix, isspmatrix_csc
        >>> isspmatrix_csr(csc_matrix([[5]]))
        False
    """
    pass

def reverse_cuthill_mckee(graph, symmetric_mode=False): # real signature unknown; restored from __doc__
    """
    reverse_cuthill_mckee(graph, symmetric_mode=False)
        
        Returns the permutation array that orders a sparse CSR or CSC matrix
        in Reverse-Cuthill McKee ordering.  
        
        It is assumed by default, ``symmetric_mode=False``, that the input matrix 
        is not symmetric and works on the matrix ``A+A.T``. If you are 
        guaranteed that the matrix is symmetric in structure (values of matrix 
        elements do not matter) then set ``symmetric_mode=True``.
        
        Parameters
        ----------
        graph : sparse matrix
            Input sparse in CSC or CSR sparse matrix format.
        symmetric_mode : bool, optional
            Is input matrix guaranteed to be symmetric.
    
        Returns
        -------
        perm : ndarray
            Array of permuted row and column indices.
     
        Notes
        -----
        .. versionadded:: 0.15.0
    
        References
        ----------
        E. Cuthill and J. McKee, "Reducing the Bandwidth of Sparse Symmetric Matrices",
        ACM '69 Proceedings of the 1969 24th national conference, (1969).
    
        Examples
        --------
        >>> from scipy.sparse import csr_matrix
        >>> from scipy.sparse.csgraph import reverse_cuthill_mckee
    
        >>> graph = [
        ... [0, 1, 2, 0],
        ... [0, 0, 0, 1],
        ... [2, 0, 0, 3],
        ... [0, 0, 0, 0]
        ... ]
        >>> graph = csr_matrix(graph)
        >>> print(graph)
          (0, 1)	1
          (0, 2)	2
          (1, 3)	1
          (2, 0)	2
          (2, 3)	3
    
        >>> reverse_cuthill_mckee(graph)
        array([3, 2, 1, 0], dtype=int32)
    """
    pass

def structural_rank(graph): # real signature unknown; restored from __doc__
    """
    structural_rank(graph)
        
        Compute the structural rank of a graph (matrix) with a given 
        sparsity pattern.
    
        The structural rank of a matrix is the number of entries in the maximum 
        transversal of the corresponding bipartite graph, and is an upper bound 
        on the numerical rank of the matrix. A graph has full structural rank 
        if it is possible to permute the elements to make the diagonal zero-free.
    
        .. versionadded:: 0.19.0
    
        Parameters
        ----------
        graph : sparse matrix
            Input sparse matrix.
    
        Returns
        -------
        rank : int
            The structural rank of the sparse graph.
        
        References
        ----------
        .. [1] I. S. Duff, "Computing the Structural Index", SIAM J. Alg. Disc. 
                Meth., Vol. 7, 594 (1986).
        
        .. [2] http://www.cise.ufl.edu/research/sparse/matrices/legend.html
    
        Examples
        --------
        >>> from scipy.sparse import csr_matrix
        >>> from scipy.sparse.csgraph import structural_rank
    
        >>> graph = [
        ... [0, 1, 2, 0],
        ... [1, 0, 0, 1],
        ... [2, 0, 0, 3],
        ... [0, 1, 3, 0]
        ... ]
        >>> graph = csr_matrix(graph)
        >>> print(graph)
          (0, 1)	1
          (0, 2)	2
          (1, 0)	1
          (1, 3)	1
          (2, 0)	2
          (2, 3)	3
          (3, 1)	1
          (3, 2)	3
    
        >>> structural_rank(graph)
        4
    """
    pass

def _reverse_cuthill_mckee(*args, **kwargs): # real signature unknown
    """
    Reverse Cuthill-McKee ordering of a sparse symmetric CSR or CSC matrix.  
        We follow the original Cuthill-McKee paper and always start the routine
        at a node of lowest degree for each connected component.
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class csr_matrix(__scipy_sparse__compressed._cs_matrix):
    """
    Compressed Sparse Row matrix
    
        This can be instantiated in several ways:
            csr_matrix(D)
                with a dense matrix or rank-2 ndarray D
    
            csr_matrix(S)
                with another sparse matrix S (equivalent to S.tocsr())
    
            csr_matrix((M, N), [dtype])
                to construct an empty matrix with shape (M, N)
                dtype is optional, defaulting to dtype='d'.
    
            csr_matrix((data, (row_ind, col_ind)), [shape=(M, N)])
                where ``data``, ``row_ind`` and ``col_ind`` satisfy the
                relationship ``a[row_ind[k], col_ind[k]] = data[k]``.
    
            csr_matrix((data, indices, indptr), [shape=(M, N)])
                is the standard CSR representation where the column indices for
                row i are stored in ``indices[indptr[i]:indptr[i+1]]`` and their
                corresponding values are stored in ``data[indptr[i]:indptr[i+1]]``.
                If the shape parameter is not supplied, the matrix dimensions
                are inferred from the index arrays.
    
        Attributes
        ----------
        dtype : dtype
            Data type of the matrix
        shape : 2-tuple
            Shape of the matrix
        ndim : int
            Number of dimensions (this is always 2)
        nnz
            Number of stored values, including explicit zeros
        data
            CSR format data array of the matrix
        indices
            CSR format index array of the matrix
        indptr
            CSR format index pointer array of the matrix
        has_sorted_indices
            Whether indices are sorted
    
        Notes
        -----
    
        Sparse matrices can be used in arithmetic operations: they support
        addition, subtraction, multiplication, division, and matrix power.
    
        Advantages of the CSR format
          - efficient arithmetic operations CSR + CSR, CSR * CSR, etc.
          - efficient row slicing
          - fast matrix vector products
    
        Disadvantages of the CSR format
          - slow column slicing operations (consider CSC)
          - changes to the sparsity structure are expensive (consider LIL or DOK)
    
        Examples
        --------
    
        >>> import numpy as np
        >>> from scipy.sparse import csr_matrix
        >>> csr_matrix((3, 4), dtype=np.int8).toarray()
        array([[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]], dtype=int8)
    
        >>> row = np.array([0, 0, 1, 2, 2, 2])
        >>> col = np.array([0, 2, 2, 0, 1, 2])
        >>> data = np.array([1, 2, 3, 4, 5, 6])
        >>> csr_matrix((data, (row, col)), shape=(3, 3)).toarray()
        array([[1, 0, 2],
               [0, 0, 3],
               [4, 5, 6]])
    
        >>> indptr = np.array([0, 2, 3, 6])
        >>> indices = np.array([0, 2, 2, 0, 1, 2])
        >>> data = np.array([1, 2, 3, 4, 5, 6])
        >>> csr_matrix((data, indices, indptr), shape=(3, 3)).toarray()
        array([[1, 0, 2],
               [0, 0, 3],
               [4, 5, 6]])
    
        Duplicate entries are summed together:
    
        >>> row = np.array([0, 1, 2, 0])
        >>> col = np.array([0, 1, 1, 0])
        >>> data = np.array([1, 2, 4, 8])
        >>> csr_matrix((data, (row, col)), shape=(3, 3)).toarray()
        array([[9, 0, 0],
               [0, 2, 0],
               [0, 4, 0]])
    
        As an example of how to construct a CSR matrix incrementally,
        the following snippet builds a term-document matrix from texts:
    
        >>> docs = [["hello", "world", "hello"], ["goodbye", "cruel", "world"]]
        >>> indptr = [0]
        >>> indices = []
        >>> data = []
        >>> vocabulary = {}
        >>> for d in docs:
        ...     for term in d:
        ...         index = vocabulary.setdefault(term, len(vocabulary))
        ...         indices.append(index)
        ...         data.append(1)
        ...     indptr.append(len(indices))
        ...
        >>> csr_matrix((data, indices, indptr), dtype=int).toarray()
        array([[2, 1, 0, 0],
               [0, 1, 1, 1]])
    """
    def getcol(self, i): # reliably restored by inspect
        """
        Returns a copy of column i of the matrix, as a (m x 1)
                CSR matrix (column vector).
        """
        pass

    def getrow(self, i): # reliably restored by inspect
        """
        Returns a copy of row i of the matrix, as a (1 x n)
                CSR matrix (row vector).
        """
        pass

    def tobsr(self, blocksize=None, copy=True): # reliably restored by inspect
        """
        Convert this matrix to Block Sparse Row format.
        
                With copy=False, the data/indices may be shared between this matrix and
                the resultant bsr_matrix.
        
                When blocksize=(R, C) is provided, it will be used for construction of
                the bsr_matrix.
        """
        pass

    def tocsc(self, copy=False): # reliably restored by inspect
        """
        Convert this matrix to Compressed Sparse Column format.
        
                With copy=False, the data/indices may be shared between this matrix and
                the resultant csc_matrix.
        """
        pass

    def tocsr(self, copy=False): # reliably restored by inspect
        """
        Convert this matrix to Compressed Sparse Row format.
        
                With copy=False, the data/indices may be shared between this matrix and
                the resultant csr_matrix.
        """
        pass

    def tolil(self, copy=False): # reliably restored by inspect
        """
        Convert this matrix to List of Lists format.
        
                With copy=False, the data/indices may be shared between this matrix and
                the resultant lil_matrix.
        """
        pass

    def transpose(self, axes=None, copy=False): # reliably restored by inspect
        """
        Reverses the dimensions of the sparse matrix.
        
                Parameters
                ----------
                axes : None, optional
                    This argument is in the signature *solely* for NumPy
                    compatibility reasons. Do not pass in anything except
                    for the default value.
                copy : bool, optional
                    Indicates whether or not attributes of `self` should be
                    copied whenever possible. The degree to which attributes
                    are copied varies depending on the type of sparse matrix
                    being used.
        
                Returns
                -------
                p : `self` with the dimensions reversed.
        
                See Also
                --------
                numpy.matrix.transpose : NumPy's implementation of 'transpose'
                                         for matrices
        """
        pass

    def _get_arrayXint(self, row, col): # reliably restored by inspect
        # no doc
        pass

    def _get_arrayXslice(self, row, col): # reliably restored by inspect
        # no doc
        pass

    def _get_intXarray(self, row, col): # reliably restored by inspect
        # no doc
        pass

    def _get_intXslice(self, row, col): # reliably restored by inspect
        # no doc
        pass

    def _get_sliceXarray(self, row, col): # reliably restored by inspect
        # no doc
        pass

    def _get_sliceXint(self, row, col): # reliably restored by inspect
        # no doc
        pass

    def _swap(self, x): # reliably restored by inspect
        """ swap the members of x if this is a column-oriented matrix """
        pass

    def __init__(self, arg1, shape=None, dtype=None, copy=False): # reliably restored by inspect
        # no doc
        pass

    def __iter__(self): # reliably restored by inspect
        # no doc
        pass

    format = 'csr'


class DTYPE(__numpy.floating, float):
    """
    Double-precision floating-point number type, compatible with Python `float`
        and C ``double``.
    
        :Character code: ``'d'``
        :Canonical name: `numpy.double`
        :Alias: `numpy.float_`
        :Alias on this platform (Linux aarch64): `numpy.float64`: 64-bit precision floating-point number type: sign bit, 11 bits exponent, 52 bits mantissa.
    """
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        double.as_integer_ratio() -> (int, int)
        
                Return a pair of integers, whose ratio is exactly equal to the original
                floating point number, and with a positive denominator.
                Raise `OverflowError` on infinities and a `ValueError` on NaNs.
        
                >>> np.double(10.0).as_integer_ratio()
                (10, 1)
                >>> np.double(0.0).as_integer_ratio()
                (0, 1)
                >>> np.double(-.25).as_integer_ratio()
                (-1, 4)
        """
        pass

    def is_integer(self): # real signature unknown; restored from __doc__
        """
        double.is_integer() -> bool
        
                Return ``True`` if the floating point number is finite with integral
                value, and ``False`` otherwise.
        
                .. versionadded:: 1.22
        
                Examples
                --------
                >>> np.double(-2.0).is_integer()
                True
                >>> np.double(3.2).is_integer()
                False
        """
        return False

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    @classmethod
    def __class_getitem__(cls, *args, **kwargs): # real signature unknown
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass


class ITYPE(__numpy.signedinteger):
    """
    Signed integer type, compatible with C ``int``.
    
        :Character code: ``'i'``
        :Canonical name: `numpy.intc`
        :Alias on this platform (Linux aarch64): `numpy.int32`: 32-bit signed integer (``-2_147_483_648`` to ``2_147_483_647``).
    """
    def bit_count(self): # real signature unknown; restored from __doc__
        """
        int32.bit_count() -> int
        
                Computes the number of 1-bits in the absolute value of the input.
                Analogous to the builtin `int.bit_count` or ``popcount`` in C++.
        
                Examples
                --------
                >>> np.int32(127).bit_count()
                7
                >>> np.int32(-127).bit_count()
                7
        """
        return 0

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    @classmethod
    def __class_getitem__(cls, *args, **kwargs): # real signature unknown
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass


class SparseEfficiencyWarning(__scipy_sparse__base.SparseWarning):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff972b8f40>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.sparse.csgraph._reordering', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff972b8f40>, origin='/.venv/lib/python3.8/site-packages/scipy/sparse/csgraph/_reordering.cpython-38-aarch64-linux-gnu.so')"

__test__ = {
    'reverse_cuthill_mckee (line 17)': '\n    reverse_cuthill_mckee(graph, symmetric_mode=False)\n    \n    Returns the permutation array that orders a sparse CSR or CSC matrix\n    in Reverse-Cuthill McKee ordering.  \n    \n    It is assumed by default, ``symmetric_mode=False``, that the input matrix \n    is not symmetric and works on the matrix ``A+A.T``. If you are \n    guaranteed that the matrix is symmetric in structure (values of matrix \n    elements do not matter) then set ``symmetric_mode=True``.\n    \n    Parameters\n    ----------\n    graph : sparse matrix\n        Input sparse in CSC or CSR sparse matrix format.\n    symmetric_mode : bool, optional\n        Is input matrix guaranteed to be symmetric.\n\n    Returns\n    -------\n    perm : ndarray\n        Array of permuted row and column indices.\n \n    Notes\n    -----\n    .. versionadded:: 0.15.0\n\n    References\n    ----------\n    E. Cuthill and J. McKee, "Reducing the Bandwidth of Sparse Symmetric Matrices",\n    ACM \'69 Proceedings of the 1969 24th national conference, (1969).\n\n    Examples\n    --------\n    >>> from scipy.sparse import csr_matrix\n    >>> from scipy.sparse.csgraph import reverse_cuthill_mckee\n\n    >>> graph = [\n    ... [0, 1, 2, 0],\n    ... [0, 0, 0, 1],\n    ... [2, 0, 0, 3],\n    ... [0, 0, 0, 0]\n    ... ]\n    >>> graph = csr_matrix(graph)\n    >>> print(graph)\n      (0, 1)\t1\n      (0, 2)\t2\n      (1, 3)\t1\n      (2, 0)\t2\n      (2, 3)\t3\n\n    >>> reverse_cuthill_mckee(graph)\n    array([3, 2, 1, 0], dtype=int32)\n    \n    ',
    'structural_rank (line 172)': '\n    structural_rank(graph)\n    \n    Compute the structural rank of a graph (matrix) with a given \n    sparsity pattern.\n\n    The structural rank of a matrix is the number of entries in the maximum \n    transversal of the corresponding bipartite graph, and is an upper bound \n    on the numerical rank of the matrix. A graph has full structural rank \n    if it is possible to permute the elements to make the diagonal zero-free.\n\n    .. versionadded:: 0.19.0\n\n    Parameters\n    ----------\n    graph : sparse matrix\n        Input sparse matrix.\n\n    Returns\n    -------\n    rank : int\n        The structural rank of the sparse graph.\n    \n    References\n    ----------\n    .. [1] I. S. Duff, "Computing the Structural Index", SIAM J. Alg. Disc. \n            Meth., Vol. 7, 594 (1986).\n    \n    .. [2] http://www.cise.ufl.edu/research/sparse/matrices/legend.html\n\n    Examples\n    --------\n    >>> from scipy.sparse import csr_matrix\n    >>> from scipy.sparse.csgraph import structural_rank\n\n    >>> graph = [\n    ... [0, 1, 2, 0],\n    ... [1, 0, 0, 1],\n    ... [2, 0, 0, 3],\n    ... [0, 1, 3, 0]\n    ... ]\n    >>> graph = csr_matrix(graph)\n    >>> print(graph)\n      (0, 1)\t1\n      (0, 2)\t2\n      (1, 0)\t1\n      (1, 3)\t1\n      (2, 0)\t2\n      (2, 3)\t3\n      (3, 1)\t1\n      (3, 2)\t3\n\n    >>> structural_rank(graph)\n    4\n\n    ',
}

