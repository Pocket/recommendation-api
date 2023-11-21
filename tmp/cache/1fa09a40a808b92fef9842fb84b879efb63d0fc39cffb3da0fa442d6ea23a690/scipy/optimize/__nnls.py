# encoding: utf-8
# module scipy.optimize.__nnls
# from /.venv/lib/python3.8/site-packages/scipy/optimize/__nnls.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
"""
This module '__nnls' is auto-generated with f2py (version:2).
Functions:
  x,rnorm,mode = nnls(a,m,n,b,w,zz,index_bn,maxiter,mda=shape(a,0),overwrite_a=0,overwrite_b=0)
.
"""
# no imports

# Variables with simple values

__version__ = b'$Revision: $'

# functions

def nnls(a, m, n, b, w, zz, index_bn, maxiter, mda=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,rnorm,mode = nnls(a,m,n,b,w,zz,index_bn,maxiter,[mda,overwrite_a,overwrite_b])
    
    Wrapper for ``nnls``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (mda,*)
    m : input int
    n : input int
    b : input rank-1 array('d') with bounds (*)
    w : input rank-1 array('d') with bounds (*)
    zz : input rank-1 array('d') with bounds (*)
    index_bn : input rank-1 array('i') with bounds (*)
    maxiter : input int
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    mda : input int, optional
        Default: shape(a,0)
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-1 array('d') with bounds (n)
    rnorm : float
    mode : int
    """
    pass

# classes

class ___nnls_error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff92d1bdc0>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.optimize.__nnls', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff92d1bdc0>, origin='/.venv/lib/python3.8/site-packages/scipy/optimize/__nnls.cpython-38-aarch64-linux-gnu.so')"

