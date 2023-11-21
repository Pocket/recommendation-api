# encoding: utf-8
# module scipy.optimize._cobyla
# from /.venv/lib/python3.8/site-packages/scipy/optimize/_cobyla.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
"""
This module '_cobyla' is auto-generated with f2py (version:2).
Functions:
  x,dinfo = minimize(calcfc,m,x,rhobeg,rhoend,dinfo,callback,iprint=1,maxfun=100,calcfc_extra_args=(),callback_extra_args=())
.
"""
# no imports

# Variables with simple values

__version__ = b'$Revision: $'

# functions

def minimize(calcfc, m, x, rhobeg, rhoend, dinfo, callback, iprint=None, maxfun=None, calcfc_extra_args=None, callback_extra_args=None): # real signature unknown; restored from __doc__
    """
    x,dinfo = minimize(calcfc,m,x,rhobeg,rhoend,dinfo,callback,[iprint,maxfun,calcfc_extra_args,callback_extra_args])
    
    Wrapper for ``minimize``.
    
    Parameters
    ----------
    calcfc : call-back function
    m : input int
    x : input rank-1 array('d') with bounds (n)
    rhobeg : input float
    rhoend : input float
    dinfo : input rank-1 array('d') with bounds (4)
    callback : call-back function
    
    Other Parameters
    ----------------
    calcfc_extra_args : input tuple, optional
        Default: ()
    iprint : input int, optional
        Default: 1
    maxfun : input int, optional
        Default: 100
    callback_extra_args : input tuple, optional
        Default: ()
    
    Returns
    -------
    x : rank-1 array('d') with bounds (n)
    dinfo : rank-1 array('d') with bounds (4)
    
    Notes
    -----
    Call-back functions::
    
      def calcfc(x,con): return f
      Required arguments:
        x : input rank-1 array('d') with bounds (n)
        con : input rank-1 array('d') with bounds (m)
      Return objects:
        f : float
      def callback(x): return 
      Required arguments:
        x : input rank-1 array('d') with bounds (n)
    """
    pass

# classes

class __cobyla_error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff92e05dc0>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.optimize._cobyla', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff92e05dc0>, origin='/.venv/lib/python3.8/site-packages/scipy/optimize/_cobyla.cpython-38-aarch64-linux-gnu.so')"

