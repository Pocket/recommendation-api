# encoding: utf-8
# module scipy.integrate._vode
# from /.venv/lib/python3.8/site-packages/scipy/integrate/_vode.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
"""
This module '_vode' is auto-generated with f2py (version:2).
Functions:
  y,t,istate = dvode(f,jac,y,t,tout,rtol,atol,itask,istate,rwork,iwork,mf,f_extra_args=(),jac_extra_args=(),overwrite_y=0)
  y,t,istate = zvode(f,jac,y,t,tout,rtol,atol,itask,istate,zwork,rwork,iwork,mf,f_extra_args=(),jac_extra_args=(),overwrite_y=0)
COMMON blocks:
  /types/ intvar
.
"""
# no imports

# Variables with simple values

__version__ = b'$Revision: $'

# functions

def dvode(f, jac, y, t, tout, rtol, atol, itask, istate, rwork, iwork, mf, f_extra_args=None, jac_extra_args=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    y,t,istate = dvode(f,jac,y,t,tout,rtol,atol,itask,istate,rwork,iwork,mf,[f_extra_args,jac_extra_args,overwrite_y])
    
    Wrapper for ``dvode``.
    
    Parameters
    ----------
    f : call-back function
    jac : call-back function
    y : input rank-1 array('d') with bounds (neq)
    t : input float
    tout : input float
    rtol : input rank-1 array('d') with bounds (*)
    atol : input rank-1 array('d') with bounds (*)
    itask : input int
    istate : input int
    rwork : input rank-1 array('d') with bounds (lrw)
    iwork : input rank-1 array('i') with bounds (liw)
    mf : input int
    
    Other Parameters
    ----------------
    f_extra_args : input tuple, optional
        Default: ()
    jac_extra_args : input tuple, optional
        Default: ()
    overwrite_y : input int, optional
        Default: 0
    
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

def zvode(f, jac, y, t, tout, rtol, atol, itask, istate, zwork, rwork, iwork, mf, f_extra_args=None, jac_extra_args=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    y,t,istate = zvode(f,jac,y,t,tout,rtol,atol,itask,istate,zwork,rwork,iwork,mf,[f_extra_args,jac_extra_args,overwrite_y])
    
    Wrapper for ``zvode``.
    
    Parameters
    ----------
    f : call-back function
    jac : call-back function
    y : input rank-1 array('D') with bounds (neq)
    t : input float
    tout : input float
    rtol : input rank-1 array('d') with bounds (*)
    atol : input rank-1 array('d') with bounds (*)
    itask : input int
    istate : input int
    zwork : input rank-1 array('D') with bounds (lzw)
    rwork : input rank-1 array('d') with bounds (lrw)
    iwork : input rank-1 array('i') with bounds (liw)
    mf : input int
    
    Other Parameters
    ----------------
    f_extra_args : input tuple, optional
        Default: ()
    jac_extra_args : input tuple, optional
        Default: ()
    overwrite_y : input int, optional
        Default: 0
    
    Returns
    -------
    y : rank-1 array('D') with bounds (neq)
    t : float
    istate : int
    
    Notes
    -----
    Call-back functions::
    
      def f(t,y): return ydot
      Required arguments:
        t : input float
        y : input rank-1 array('D') with bounds (n)
      Return objects:
        ydot : rank-1 array('D') with bounds (n)
      def jac(t,y): return jac
      Required arguments:
        t : input float
        y : input rank-1 array('D') with bounds (n)
      Return objects:
        jac : rank-2 array('D') with bounds (nrowpd,n)
    """
    pass

# classes

class __vode_error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff92c72700>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.integrate._vode', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff92c72700>, origin='/.venv/lib/python3.8/site-packages/scipy/integrate/_vode.cpython-38-aarch64-linux-gnu.so')"

