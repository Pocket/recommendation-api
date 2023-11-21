# encoding: utf-8
# module scipy.stats._statlib
# from /.venv/lib/python3.8/site-packages/scipy/stats/_statlib.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
"""
This module '_statlib' is auto-generated with f2py (version:2).
Functions:
  a,w,pw,ifault = swilk(x,a,init=0,n1=n)
  astart,a1,ifault = gscale(test,other)
  prho,ifault = prho(n,is)
.
"""
# no imports

# Variables with simple values

__version__ = b'$Revision: $'

# functions

def gscale(test, other): # real signature unknown; restored from __doc__
    """
    astart,a1,ifault = gscale(test,other)
    
    Wrapper for ``gscale``.
    
    Parameters
    ----------
    test : input int
    other : input int
    
    Returns
    -------
    astart : float
    a1 : rank-1 array('f') with bounds (l1)
    ifault : int
    """
    pass

def prho(n, is_): # real signature unknown; restored from __doc__
    """
    prho,ifault = prho(n,is)
    
    Wrapper for ``prho``.
    
    Parameters
    ----------
    n : input int
    is : input int
    
    Returns
    -------
    prho : float
    ifault : int
    """
    pass

def swilk(x, a, init=None, n1=None): # real signature unknown; restored from __doc__
    """
    a,w,pw,ifault = swilk(x,a,[init,n1])
    
    Wrapper for ``swilk``.
    
    Parameters
    ----------
    x : input rank-1 array('f') with bounds (n)
    a : input rank-1 array('f') with bounds (n2)
    
    Other Parameters
    ----------------
    init : input int, optional
        Default: 0
    n1 : input int, optional
        Default: n
    
    Returns
    -------
    a : rank-1 array('f') with bounds (n2)
    w : float
    pw : float
    ifault : int
    """
    pass

# classes

class __statlib_error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff925bb5e0>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.stats._statlib', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff925bb5e0>, origin='/.venv/lib/python3.8/site-packages/scipy/stats/_statlib.cpython-38-aarch64-linux-gnu.so')"

