# encoding: utf-8
# module scipy.integrate._lsoda
# from /.venv/lib/python3.8/site-packages/scipy/integrate/_lsoda.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
"""
This module '_lsoda' is auto-generated with f2py (version:2).
Functions:
  y,t,istate = lsoda(f,y,t,tout,rtol,atol,itask,istate,rwork,iwork,jac,jt,f_extra_args=(),overwrite_y=0,jac_extra_args=())
COMMON blocks:
  /types/ intvar
.
"""
# no imports

# Variables with simple values

__version__ = b'$Revision: $'

# functions

def lsoda(f, y, t, tout, rtol, atol, itask, istate, rwork, iwork, jac, jt, f_extra_args=None, overwrite_y=None, jac_extra_args=None): # real signature unknown; restored from __doc__
    """
    y,t,istate = lsoda(f,y,t,tout,rtol,atol,itask,istate,rwork,iwork,jac,jt,[f_extra_args,overwrite_y,jac_extra_args])
    
    Wrapper for ``lsoda``.
    
    Parameters
    ----------
    f : call-back function
    y : input rank-1 array('d') with bounds (neq)
    t : input float
    tout : input float
    rtol : input rank-1 array('d') with bounds (*)
    atol : input rank-1 array('d') with bounds (*)
    itask : input int
    istate : input int
    rwork : input rank-1 array('d') with bounds (lrw)
    iwork : input rank-1 array('i') with bounds (liw)
    jac : call-back function
    jt : input int
    
    Other Parameters
    ----------------
    f_extra_args : input tuple, optional
        Default: ()
    overwrite_y : input int, optional
        Default: 0
    jac_extra_args : input tuple, optional
        Default: ()
    
    Returns
    -------
    y : rank-1 array('d') with bounds (neq)
    t : float
    istate : int
    
    Notes
    -----
    Call-back functions::
    
      def f(t,y): return ydot
      Required arguments:
        t : input float
        y : input rank-1 array('d') with bounds (n)
      Return objects:
        ydot : rank-1 array('d') with bounds (n)
      def jac(t,y): return jac
      Required arguments:
        t : input float
        y : input rank-1 array('d') with bounds (n)
      Return objects:
        jac : rank-2 array('d') with bounds (nrowpd,n)
    """
    pass

def types(*args, **kwargs): # real signature unknown
    """ 'i'-scalar """
    pass

# classes

class __lsoda_error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff92c71a60>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.integrate._lsoda', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff92c71a60>, origin='/.venv/lib/python3.8/site-packages/scipy/integrate/_lsoda.cpython-38-aarch64-linux-gnu.so')"

