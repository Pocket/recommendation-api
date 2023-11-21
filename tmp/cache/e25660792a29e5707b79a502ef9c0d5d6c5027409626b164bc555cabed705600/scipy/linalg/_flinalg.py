# encoding: utf-8
# module scipy.linalg._flinalg
# from /.venv/lib/python3.8/site-packages/scipy/linalg/_flinalg.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
"""
This module '_flinalg' is auto-generated with f2py (version:2).
Functions:
  det,info = ddet_c(a,overwrite_a=0)
  det,info = ddet_r(a,overwrite_a=0)
  det,info = sdet_c(a,overwrite_a=0)
  det,info = sdet_r(a,overwrite_a=0)
  det,info = zdet_c(a,overwrite_a=0)
  det,info = zdet_r(a,overwrite_a=0)
  det,info = cdet_c(a,overwrite_a=0)
  det,info = cdet_r(a,overwrite_a=0)
  p,l,u,info = dlu_c(a,permute_l=0,overwrite_a=0)
  p,l,u,info = zlu_c(a,permute_l=0,overwrite_a=0)
  p,l,u,info = slu_c(a,permute_l=0,overwrite_a=0)
  p,l,u,info = clu_c(a,permute_l=0,overwrite_a=0)
.
"""
# no imports

# Variables with simple values

__version__ = b'$Revision: $'

# functions

def cdet_c(a, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    det,info = cdet_c(a,[overwrite_a])
    
    Wrapper for ``cdet_c``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    det : complex
    info : int
    """
    pass

def cdet_r(a, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    det,info = cdet_r(a,[overwrite_a])
    
    Wrapper for ``cdet_r``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    det : complex
    info : int
    """
    pass

def clu_c(a, permute_l=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    p,l,u,info = clu_c(a,[permute_l,overwrite_a])
    
    Wrapper for ``clu_c``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    permute_l : input int, optional
        Default: 0
    
    Returns
    -------
    p : rank-2 array('f') with bounds (m1,m1)
    l : rank-2 array('F') with bounds (m,k)
    u : rank-2 array('F') with bounds (k,n)
    info : int
    """
    pass

def ddet_c(a, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    det,info = ddet_c(a,[overwrite_a])
    
    Wrapper for ``ddet_c``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    det : float
    info : int
    """
    pass

def ddet_r(a, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    det,info = ddet_r(a,[overwrite_a])
    
    Wrapper for ``ddet_r``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    det : float
    info : int
    """
    pass

def dlu_c(a, permute_l=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    p,l,u,info = dlu_c(a,[permute_l,overwrite_a])
    
    Wrapper for ``dlu_c``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    permute_l : input int, optional
        Default: 0
    
    Returns
    -------
    p : rank-2 array('d') with bounds (m1,m1)
    l : rank-2 array('d') with bounds (m,k)
    u : rank-2 array('d') with bounds (k,n)
    info : int
    """
    pass

def sdet_c(a, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    det,info = sdet_c(a,[overwrite_a])
    
    Wrapper for ``sdet_c``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    det : float
    info : int
    """
    pass

def sdet_r(a, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    det,info = sdet_r(a,[overwrite_a])
    
    Wrapper for ``sdet_r``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    det : float
    info : int
    """
    pass

def slu_c(a, permute_l=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    p,l,u,info = slu_c(a,[permute_l,overwrite_a])
    
    Wrapper for ``slu_c``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    permute_l : input int, optional
        Default: 0
    
    Returns
    -------
    p : rank-2 array('f') with bounds (m1,m1)
    l : rank-2 array('f') with bounds (m,k)
    u : rank-2 array('f') with bounds (k,n)
    info : int
    """
    pass

def zdet_c(a, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    det,info = zdet_c(a,[overwrite_a])
    
    Wrapper for ``zdet_c``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    det : complex
    info : int
    """
    pass

def zdet_r(a, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    det,info = zdet_r(a,[overwrite_a])
    
    Wrapper for ``zdet_r``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    det : complex
    info : int
    """
    pass

def zlu_c(a, permute_l=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    p,l,u,info = zlu_c(a,[permute_l,overwrite_a])
    
    Wrapper for ``zlu_c``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    permute_l : input int, optional
        Default: 0
    
    Returns
    -------
    p : rank-2 array('d') with bounds (m1,m1)
    l : rank-2 array('D') with bounds (m,k)
    u : rank-2 array('D') with bounds (k,n)
    info : int
    """
    pass

# classes

class __flinalg_error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9f886760>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.linalg._flinalg', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9f886760>, origin='/.venv/lib/python3.8/site-packages/scipy/linalg/_flinalg.cpython-38-aarch64-linux-gnu.so')"

