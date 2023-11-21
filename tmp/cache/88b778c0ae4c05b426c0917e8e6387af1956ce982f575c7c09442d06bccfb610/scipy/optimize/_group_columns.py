# encoding: utf-8
# module scipy.optimize._group_columns
# from /.venv/lib/python3.8/site-packages/scipy/optimize/_group_columns.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
"""
Pythran implementation of columns grouping for finite difference Jacobian
estimation. Used by ._numdiff.group_columns and based on the Cython version.
"""
# no imports

# functions

def group_dense(p_int, p_int_1, p_int_2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Supported prototypes:
    
        - group_dense(int, int, int[:,:])
        - group_dense(int, int, int32[:,:])
    """
    pass

def group_sparse(p_int, p_int_1, int64, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Supported prototypes:
    
        - group_sparse(int, int, int64[::], int64[::])
        - group_sparse(int, int, int32[::], int32[::])
        - group_sparse(int, int, int64[:], int64[:])
        - group_sparse(int, int, int32[:], int32[:])
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff93377c70>'

__pythran__ = (
    '0.12.1',
    '2023-02-19 18:21:10.036838',
    'd7c1aa78dafa22cfad7f46fb815cf1eb0c6860602fdb0cdd51232c7729bd53d6',
)

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.optimize._group_columns', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff93377c70>, origin='/.venv/lib/python3.8/site-packages/scipy/optimize/_group_columns.cpython-38-aarch64-linux-gnu.so')"

