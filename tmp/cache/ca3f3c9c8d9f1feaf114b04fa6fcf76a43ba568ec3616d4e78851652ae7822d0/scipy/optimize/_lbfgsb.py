# encoding: utf-8
# module scipy.optimize._lbfgsb
# from /.venv/lib/python3.8/site-packages/scipy/optimize/_lbfgsb.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
"""
This module '_lbfgsb' is auto-generated with f2py (version:2).
Functions:
  setulb(m,x,l,u,nbd,f,g,factr,pgtol,wa,iwa,task,iprint,csave,lsave,isave,dsave,maxls,n=len(x))
COMMON blocks:
  /types/ intvar
.
"""
# no imports

# Variables with simple values

__version__ = b'$Revision: $'

# functions

def setulb(m, x, l, u, nbd, f, g, factr, pgtol, wa, iwa, task, iprint, csave, lsave, isave, dsave, maxls, n=None): # real signature unknown; restored from __doc__
    """
    setulb(m,x,l,u,nbd,f,g,factr,pgtol,wa,iwa,task,iprint,csave,lsave,isave,dsave,maxls,[n])
    
    Wrapper for ``setulb``.
    
    Parameters
    ----------
    m : input int
    x : in/output rank-1 array('d') with bounds (n)
    l : input rank-1 array('d') with bounds (n)
    u : input rank-1 array('d') with bounds (n)
    nbd : input rank-1 array('i') with bounds (n)
    f : in/output rank-0 array(float,'d')
    g : in/output rank-1 array('d') with bounds (n)
    factr : input float
    pgtol : input float
    wa : in/output rank-1 array('d') with bounds (2*m*n+5*n+11*m*m+8*m)
    iwa : in/output rank-1 array('i') with bounds (3 * n)
    task : in/output rank-0 array(string(len=60),'c')
    iprint : input int
    csave : in/output rank-0 array(string(len=60),'c')
    lsave : in/output rank-1 array('i') with bounds (4)
    isave : in/output rank-1 array('i') with bounds (44)
    dsave : in/output rank-1 array('d') with bounds (29)
    maxls : input int
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: len(x)
    """
    pass

def types(*args, **kwargs): # real signature unknown
    """ 'i'-scalar """
    pass

# classes

class __lbfgsb_error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff92e08400>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.optimize._lbfgsb', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff92e08400>, origin='/.venv/lib/python3.8/site-packages/scipy/optimize/_lbfgsb.cpython-38-aarch64-linux-gnu.so')"

