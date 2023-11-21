# encoding: utf-8
# module scipy.sparse._csparsetools
# from /.venv/lib/python3.8/site-packages/scipy/sparse/_csparsetools.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
""" Fast snippets for LIL matrices. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /.venv/lib/python3.8/site-packages/numpy/__init__.py

# functions

def lil_fancy_get(*args, **kwargs): # real signature unknown
    """
    Get multiple items at given indices in LIL matrix and store to
        another LIL.
    
        Parameters
        ----------
        M, N, rows, data
            LIL matrix data, initially empty
        new_rows, new_idx
            Data for LIL matrix to insert to.
            Must be preallocated to shape `i_idx.shape`!
        i_idx, j_idx
            Indices of elements to insert to the new LIL matrix.
    """
    pass

def lil_fancy_set(*args, **kwargs): # real signature unknown
    """
    Set multiple items to a LIL matrix.
    
        Checks for zero elements and deletes them.
    
        Parameters
        ----------
        M, N, rows, data
            LIL matrix data
        i_idx, j_idx
            Indices of elements to insert to the new LIL matrix.
        values
            Values of items to set.
    """
    pass

def lil_flatten_to_array(*args, **kwargs): # real signature unknown
    pass

def lil_get1(*args, **kwargs): # real signature unknown
    """
    Get a single item from LIL matrix.
    
        Doesn't do output type conversion. Checks for bounds errors.
    
        Parameters
        ----------
        M, N, rows, datas
            Shape and data arrays for a LIL matrix
        i, j : int
            Indices at which to get
    
        Returns
        -------
        x
            Value at indices.
    """
    pass

def lil_get_lengths(*args, **kwargs): # real signature unknown
    pass

def lil_get_row_ranges(*args, **kwargs): # real signature unknown
    """
    Column-slicing fast path for LIL matrices.
        Extracts values from rows/datas and inserts in to
        new_rows/new_datas.
        Parameters
        ----------
        M, N
             Shape of input array
        rows, datas
             LIL data for input array, shape (M, N)
        new_rows, new_datas
             LIL data for output array, shape (len(irows), nj)
        irows : iterator
             Iterator yielding row indices
        j_start, j_stop, j_stride
             Column range(j_start, j_stop, j_stride) to get
        nj : int
             Number of columns corresponding to j_* variables.
    """
    pass

def lil_insert(*args, **kwargs): # real signature unknown
    """
    Insert a single item to LIL matrix.
    
        Checks for bounds errors and deletes item if x is zero.
    
        Parameters
        ----------
        M, N, rows, datas
            Shape and data arrays for a LIL matrix
        i, j : int
            Indices at which to get
        x
            Value to insert.
    """
    pass

def _lil_fancy_get_int32(*args, **kwargs): # real signature unknown
    pass

def _lil_fancy_get_int64(*args, **kwargs): # real signature unknown
    pass

def _lil_fancy_set_int32_bool_(*args, **kwargs): # real signature unknown
    pass

def _lil_fancy_set_int32_clongdouble(*args, **kwargs): # real signature unknown
    pass

def _lil_fancy_set_int32_complex128(*args, **kwargs): # real signature unknown
    pass

def _lil_fancy_set_int32_complex64(*args, **kwargs): # real signature unknown
    pass

def _lil_fancy_set_int32_float32(*args, **kwargs): # real signature unknown
    pass

def _lil_fancy_set_int32_float64(*args, **kwargs): # real signature unknown
    pass

def _lil_fancy_set_int32_int16(*args, **kwargs): # real signature unknown
    pass

def _lil_fancy_set_int32_int32(*args, **kwargs): # real signature unknown
    pass

def _lil_fancy_set_int32_int64(*args, **kwargs): # real signature unknown
    pass

def _lil_fancy_set_int32_int8(*args, **kwargs): # real signature unknown
    pass

def _lil_fancy_set_int32_longdouble(*args, **kwargs): # real signature unknown
    pass

def _lil_fancy_set_int32_uint16(*args, **kwargs): # real signature unknown
    pass

def _lil_fancy_set_int32_uint32(*args, **kwargs): # real signature unknown
    pass

def _lil_fancy_set_int32_uint64(*args, **kwargs): # real signature unknown
    pass

def _lil_fancy_set_int32_uint8(*args, **kwargs): # real signature unknown
    pass

def _lil_fancy_set_int64_bool_(*args, **kwargs): # real signature unknown
    pass

def _lil_fancy_set_int64_clongdouble(*args, **kwargs): # real signature unknown
    pass

def _lil_fancy_set_int64_complex128(*args, **kwargs): # real signature unknown
    pass

def _lil_fancy_set_int64_complex64(*args, **kwargs): # real signature unknown
    pass

def _lil_fancy_set_int64_float32(*args, **kwargs): # real signature unknown
    pass

def _lil_fancy_set_int64_float64(*args, **kwargs): # real signature unknown
    pass

def _lil_fancy_set_int64_int16(*args, **kwargs): # real signature unknown
    pass

def _lil_fancy_set_int64_int32(*args, **kwargs): # real signature unknown
    pass

def _lil_fancy_set_int64_int64(*args, **kwargs): # real signature unknown
    pass

def _lil_fancy_set_int64_int8(*args, **kwargs): # real signature unknown
    pass

def _lil_fancy_set_int64_longdouble(*args, **kwargs): # real signature unknown
    pass

def _lil_fancy_set_int64_uint16(*args, **kwargs): # real signature unknown
    pass

def _lil_fancy_set_int64_uint32(*args, **kwargs): # real signature unknown
    pass

def _lil_fancy_set_int64_uint64(*args, **kwargs): # real signature unknown
    pass

def _lil_fancy_set_int64_uint8(*args, **kwargs): # real signature unknown
    pass

def _lil_flatten_to_array_bool_(*args, **kwargs): # real signature unknown
    pass

def _lil_flatten_to_array_clongdouble(*args, **kwargs): # real signature unknown
    pass

def _lil_flatten_to_array_complex128(*args, **kwargs): # real signature unknown
    pass

def _lil_flatten_to_array_complex64(*args, **kwargs): # real signature unknown
    pass

def _lil_flatten_to_array_float32(*args, **kwargs): # real signature unknown
    pass

def _lil_flatten_to_array_float64(*args, **kwargs): # real signature unknown
    pass

def _lil_flatten_to_array_int16(*args, **kwargs): # real signature unknown
    pass

def _lil_flatten_to_array_int32(*args, **kwargs): # real signature unknown
    pass

def _lil_flatten_to_array_int64(*args, **kwargs): # real signature unknown
    pass

def _lil_flatten_to_array_int8(*args, **kwargs): # real signature unknown
    pass

def _lil_flatten_to_array_longdouble(*args, **kwargs): # real signature unknown
    pass

def _lil_flatten_to_array_uint16(*args, **kwargs): # real signature unknown
    pass

def _lil_flatten_to_array_uint32(*args, **kwargs): # real signature unknown
    pass

def _lil_flatten_to_array_uint64(*args, **kwargs): # real signature unknown
    pass

def _lil_flatten_to_array_uint8(*args, **kwargs): # real signature unknown
    pass

def _lil_get_lengths_int32(*args, **kwargs): # real signature unknown
    pass

def _lil_get_lengths_int64(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9f820d90>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.sparse._csparsetools', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9f820d90>, origin='/.venv/lib/python3.8/site-packages/scipy/sparse/_csparsetools.cpython-38-aarch64-linux-gnu.so')"

__test__ = {}

