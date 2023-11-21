# encoding: utf-8
# module scipy.optimize._lsq.givens_elimination
# from /.venv/lib/python3.8/site-packages/scipy/optimize/_lsq/givens_elimination.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /.venv/lib/python3.8/site-packages/numpy/__init__.py

# functions

def givens_elimination(*args, **kwargs): # real signature unknown
    """
    Zero out a diagonal block of a matrix by series of Givens rotations.
    
        The matrix has the structure::
    
            [ S ]
            [ D ]
    
        Where S is an upper triangular matrix with shape (n, n) and D is a
        diagonal matrix with shape (n, n) with elements from `diag`. This function
        applies Givens rotations to it such that the resulting matrix has zeros
        in place of D.
    
        Array `S` will be modified in-place.
    
        Array `v` of shape (n,) is the part of the full vector with shape (2*n,)::
    
            [ v ]
            [ 0 ]
    
        to which Givens rotations are applied. This array is modified in place,
        such that on exit it contains the first n components of the above
        mentioned vector after rotations were applied.
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff92e80a60>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.optimize._lsq.givens_elimination', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff92e80a60>, origin='/.venv/lib/python3.8/site-packages/scipy/optimize/_lsq/givens_elimination.cpython-38-aarch64-linux-gnu.so')"

__test__ = {}

