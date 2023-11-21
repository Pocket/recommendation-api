# encoding: utf-8
# module scipy.io.matlab._mio5_utils
# from /.venv/lib/python3.8/site-packages/scipy/io/matlab/_mio5_utils.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
""" Cython mio5 utility routines (-*- python -*- like) """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import sys as sys # <module 'sys' (built-in)>
import numpy as np # /.venv/lib/python3.8/site-packages/numpy/__init__.py
import scipy.io.matlab._mio5_params as mio5p # /.venv/lib/python3.8/site-packages/scipy/io/matlab/_mio5_params.py
from scipy.io.matlab._mio_utils import chars_to_strings, squeeze_element

import scipy.sparse._compressed as __scipy_sparse__compressed


# Variables with simple values

swapped_code = '>'

# functions

def byteswap_u4(*args, **kwargs): # real signature unknown
    pass

def pycopy(x): # reliably restored by inspect
    """
    Shallow copy operation on arbitrary Python objects.
    
        See the module's __doc__ string for more info.
    """
    pass

def __pyx_unpickle_VarHeader5(*args, **kwargs): # real signature unknown
    pass

# classes

class csc_matrix(__scipy_sparse__compressed._cs_matrix):
    """
    Compressed Sparse Column matrix
    
        This can be instantiated in several ways:
    
            csc_matrix(D)
                with a dense matrix or rank-2 ndarray D
    
            csc_matrix(S)
                with another sparse matrix S (equivalent to S.tocsc())
    
            csc_matrix((M, N), [dtype])
                to construct an empty matrix with shape (M, N)
                dtype is optional, defaulting to dtype='d'.
    
            csc_matrix((data, (row_ind, col_ind)), [shape=(M, N)])
                where ``data``, ``row_ind`` and ``col_ind`` satisfy the
                relationship ``a[row_ind[k], col_ind[k]] = data[k]``.
    
            csc_matrix((data, indices, indptr), [shape=(M, N)])
                is the standard CSC representation where the row indices for
                column i are stored in ``indices[indptr[i]:indptr[i+1]]``
                and their corresponding values are stored in
                ``data[indptr[i]:indptr[i+1]]``.  If the shape parameter is
                not supplied, the matrix dimensions are inferred from
                the index arrays.
    
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
            Data array of the matrix
        indices
            CSC format index array
        indptr
            CSC format index pointer array
        has_sorted_indices
            Whether indices are sorted
    
        Notes
        -----
    
        Sparse matrices can be used in arithmetic operations: they support
        addition, subtraction, multiplication, division, and matrix power.
    
        Advantages of the CSC format
            - efficient arithmetic operations CSC + CSC, CSC * CSC, etc.
            - efficient column slicing
            - fast matrix vector products (CSR, BSR may be faster)
    
        Disadvantages of the CSC format
          - slow row slicing operations (consider CSR)
          - changes to the sparsity structure are expensive (consider LIL or DOK)
    
    
        Examples
        --------
    
        >>> import numpy as np
        >>> from scipy.sparse import csc_matrix
        >>> csc_matrix((3, 4), dtype=np.int8).toarray()
        array([[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]], dtype=int8)
    
        >>> row = np.array([0, 2, 2, 0, 1, 2])
        >>> col = np.array([0, 0, 1, 2, 2, 2])
        >>> data = np.array([1, 2, 3, 4, 5, 6])
        >>> csc_matrix((data, (row, col)), shape=(3, 3)).toarray()
        array([[1, 0, 4],
               [0, 0, 5],
               [2, 3, 6]])
    
        >>> indptr = np.array([0, 2, 3, 6])
        >>> indices = np.array([0, 2, 2, 0, 1, 2])
        >>> data = np.array([1, 2, 3, 4, 5, 6])
        >>> csc_matrix((data, indices, indptr), shape=(3, 3)).toarray()
        array([[1, 0, 4],
               [0, 0, 5],
               [2, 3, 6]])
    """
    def getcol(self, i): # reliably restored by inspect
        """
        Returns a copy of column i of the matrix, as a (m x 1)
                CSC matrix (column vector).
        """
        pass

    def getrow(self, i): # reliably restored by inspect
        """
        Returns a copy of row i of the matrix, as a (1 x n)
                CSR matrix (row vector).
        """
        pass

    def nonzero(self): # reliably restored by inspect
        """
        nonzero indices
        
                Returns a tuple of arrays (row,col) containing the indices
                of the non-zero elements of the matrix.
        
                Examples
                --------
                >>> from scipy.sparse import csr_matrix
                >>> A = csr_matrix([[1,2,0],[0,0,3],[4,0,5]])
                >>> A.nonzero()
                (array([0, 0, 1, 2, 2]), array([0, 1, 2, 0, 2]))
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

    format = 'csc'


class VarHeader5(object):
    # no doc
    def set_dims(self, *args, **kwargs): # real signature unknown
        """
        Allow setting of dimensions from python
        
                This is for constructing headers for tests
        """
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

    dims = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_global = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_logical = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mclass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nzmax = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class VarReader5(object):
    # no doc
    def array_from_header(self, *args, **kwargs): # real signature unknown
        """
        Read array of any class, given matrix `header`
        
                Parameters
                ----------
                header : VarHeader5
                   array header object
                process : int, optional
                   If not zero, apply post-processing on returned array
        
                Returns
                -------
                arr : array or sparse array
                   read array
        """
        pass

    def read_cells(self, *args, **kwargs): # real signature unknown
        """ Read cell array from stream """
        pass

    def read_char(self, *args, **kwargs): # real signature unknown
        """
        Read char matrices from stream as arrays
        
                Matrices of char are likely to be converted to matrices of
                string by later processing in ``array_from_header``
        """
        pass

    def read_fieldnames(self, *args, **kwargs): # real signature unknown
        """ Read fieldnames for struct-like matrix. """
        pass

    def read_full_tag(self, *args, **kwargs): # real signature unknown
        """
        Python method for reading full u4, u4 tag from stream
        
                Returns
                -------
                mdtype : int32
                   matlab data type code
                byte_count : int32
                   number of data bytes following
        
                Notes
                -----
                Assumes tag is in fact full, that is, is not a small data
                element.  This means it can skip some checks and makes it
                slightly faster than ``read_tag``
        """
        pass

    def read_header(self, *args, **kwargs): # real signature unknown
        """
        Return matrix header for current stream position
        
                Returns matrix headers at top level and sub levels
        
                Parameters
                ----------
                check_stream_limit : if True, then if the returned header
                is passed to array_from_header, it will be verified that
                the length of the uncompressed data is not overlong (which
                can indicate .mat file corruption)
        """
        pass

    def read_numeric(self, *args, **kwargs): # real signature unknown
        """
        Read numeric data element into ndarray
        
                Reads element, then casts to ndarray.
        
                The type of the array is usually given by the ``mdtype`` returned via
                ``read_element``.  Sparse logical arrays are an exception, where the
                type of the array may be ``np.bool_`` even if the ``mdtype`` claims the
                data is of float64 type.
        
                Parameters
                ----------
                copy : bool, optional
                    Whether to copy the array before returning.  If False, return array
                    backed by bytes read from file.
                nnz : int, optional
                    Number of non-zero values when reading numeric data from sparse
                    matrices.  -1 if not reading sparse matrices, or to disable check
                    for bytes data instead of declared data type (see Notes).
        
                Returns
                -------
                arr : array
                    Numeric array
        
                Notes
                -----
                MATLAB apparently likes to store sparse logical matrix data as bytes
                instead of miDOUBLE (float64) data type, even though the data element
                still declares its type as miDOUBLE.  We can guess this has happened by
                looking for the length of the data compared to the expected number of
                elements, using the `nnz` input parameter.
        """
        pass

    def read_opaque(self, *args, **kwargs): # real signature unknown
        """
        Read opaque (function workspace) type
        
                Looking at some mat files, the structure of this type seems to
                be:
        
                * array flags as usual (already read into `hdr`)
                * 3 int8 strings
                * a matrix
        
                Then there's a matrix at the end of the mat file that seems have
                the anonymous founction workspaces - we load it as
                ``__function_workspace__``
        
                See the comments at the beginning of ``mio5.py``
        """
        pass

    def read_real_complex(self, *args, **kwargs): # real signature unknown
        """ Read real / complex matrices from stream """
        pass

    def read_struct(self, *args, **kwargs): # real signature unknown
        """
        Read struct or object array from stream
        
                Objects are just structs with an extra field *classname*,
                defined before (this here) struct format structure
        """
        pass

    def read_tag(self, *args, **kwargs): # real signature unknown
        """
        Read tag mdtype and byte_count
        
                Does necessary swapping and takes account of SDE formats.
        
                See also ``read_full_tag`` method.
        
                Returns
                -------
                mdtype : int
                   matlab data type code
                byte_count : int
                   number of bytes following that comprise the data
                tag_data : None or str
                   Any data from the tag itself.  This is None for a full tag,
                   and string length `byte_count` if this is a small data
                   element.
        """
        pass

    def set_stream(self, *args, **kwargs): # real signature unknown
        """
        Set stream of best type from file-like `fobj`
        
                Called from Python when initiating a variable read
        """
        pass

    def shape_from_header(self, *args, **kwargs): # real signature unknown
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

    is_swapped = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    little_endian = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0xffff9539c720>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9539c4c0>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.io.matlab._mio5_utils', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9539c4c0>, origin='/.venv/lib/python3.8/site-packages/scipy/io/matlab/_mio5_utils.cpython-38-aarch64-linux-gnu.so')"

__test__ = {}

