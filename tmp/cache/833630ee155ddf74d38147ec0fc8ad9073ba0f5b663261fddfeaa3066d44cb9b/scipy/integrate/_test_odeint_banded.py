# encoding: utf-8
# module scipy.integrate._test_odeint_banded
# from /.venv/lib/python3.8/site-packages/scipy/integrate/_test_odeint_banded.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
"""
This module '_test_odeint_banded' is auto-generated with f2py (version:2).
Functions:
  jac = getbands()
  banded5x5(t,y,f,n=len(y))
  banded5x5_jac(t,y,ml,mu,jac,n=len(y),nrowpd=shape(jac,0))
  banded5x5_bjac(t,y,ml,mu,bjac,n=shape(bjac,1),nrowpd=shape(bjac,0))
  nst,nfe,nje = banded5x5_solve(y,nsteps,dt,jt)
COMMON blocks:
  /jac/ bands(4,5)
.
"""
# no imports

# Variables with simple values

__version__ = b'$Revision: $'

# functions

def banded5x5(t, y, f, n=None): # real signature unknown; restored from __doc__
    """
    banded5x5(t,y,f,[n])
    
    Wrapper for ``banded5x5``.
    
    Parameters
    ----------
    t : input float
    y : input rank-1 array('d') with bounds (n)
    f : input rank-1 array('d') with bounds (n)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: len(y)
    """
    pass

def banded5x5_bjac(t, y, ml, mu, bjac, n=None, nrowpd=None): # real signature unknown; restored from __doc__
    """
    banded5x5_bjac(t,y,ml,mu,bjac,[n,nrowpd])
    
    Wrapper for ``banded5x5_bjac``.
    
    Parameters
    ----------
    t : input float
    y : input rank-1 array('d') with bounds (5)
    ml : input int
    mu : input int
    bjac : input rank-2 array('d') with bounds (nrowpd,n)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: shape(bjac,1)
    nrowpd : input int, optional
        Default: shape(bjac,0)
    """
    pass

def banded5x5_jac(t, y, ml, mu, jac, n=None, nrowpd=None): # real signature unknown; restored from __doc__
    """
    banded5x5_jac(t,y,ml,mu,jac,[n,nrowpd])
    
    Wrapper for ``banded5x5_jac``.
    
    Parameters
    ----------
    t : input float
    y : input rank-1 array('d') with bounds (n)
    ml : input int
    mu : input int
    jac : input rank-2 array('d') with bounds (nrowpd,n)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: len(y)
    nrowpd : input int, optional
        Default: shape(jac,0)
    """
    pass

def banded5x5_solve(y, nsteps, dt, jt): # real signature unknown; restored from __doc__
    """
    nst,nfe,nje = banded5x5_solve(y,nsteps,dt,jt)
    
    Wrapper for ``banded5x5_solve``.
    
    Parameters
    ----------
    y : in/output rank-1 array('d') with bounds (5)
    nsteps : input int
    dt : input float
    jt : input int
    
    Returns
    -------
    nst : int
    nfe : int
    nje : int
    """
    pass

def getbands(): # real signature unknown; restored from __doc__
    """
    jac = getbands()
    
    Wrapper for ``getbands``.
    
    Returns
    -------
    jac : rank-2 array('d') with bounds (4,5)
    """
    pass

def jac(*args, **kwargs): # real signature unknown
    """ 'd'-array(4,5) """
    pass

# classes

class __test_odeint_banded_error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924ac0>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.integrate._test_odeint_banded', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924ac0>, origin='/.venv/lib/python3.8/site-packages/scipy/integrate/_test_odeint_banded.cpython-38-aarch64-linux-gnu.so')"

