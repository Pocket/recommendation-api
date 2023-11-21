# encoding: utf-8
# module scipy.optimize._minpack2
# from /.venv/lib/python3.8/site-packages/scipy/optimize/_minpack2.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
"""
This module '_minpack2' is auto-generated with f2py (version:2).
Functions:
  stp,f,g,task = dcsrch(stp,f,g,ftol,gtol,xtol,task,stpmin,stpmax,isave,dsave)
  stx,fx,dx,sty,fy,dy,stp,brackt = dcstep(stx,fx,dx,sty,fy,dy,stp,fp,dp,brackt,stpmin,stpmax)
.
"""
# no imports

# Variables with simple values

__version__ = b'$Revision: $'

# functions

def dcsrch(stp, f, g, ftol, gtol, xtol, task, stpmin, stpmax, isave, dsave): # real signature unknown; restored from __doc__
    """
    stp,f,g,task = dcsrch(stp,f,g,ftol,gtol,xtol,task,stpmin,stpmax,isave,dsave)
    
    Wrapper for ``dcsrch``.
    
    Parameters
    ----------
    stp : input float
    f : input float
    g : input float
    ftol : input float
    gtol : input float
    xtol : input float
    task : input string(len=60)
    stpmin : input float
    stpmax : input float
    isave : in/output rank-1 array('i') with bounds (2)
    dsave : in/output rank-1 array('d') with bounds (13)
    
    Returns
    -------
    stp : float
    f : float
    g : float
    task : string(len=60)
    """
    pass

def dcstep(stx, fx, dx, sty, fy, dy, stp, fp, dp, brackt, stpmin, stpmax): # real signature unknown; restored from __doc__
    """
    stx,fx,dx,sty,fy,dy,stp,brackt = dcstep(stx,fx,dx,sty,fy,dy,stp,fp,dp,brackt,stpmin,stpmax)
    
    Wrapper for ``dcstep``.
    
    Parameters
    ----------
    stx : input float
    fx : input float
    dx : input float
    sty : input float
    fy : input float
    dy : input float
    stp : input float
    fp : input float
    dp : input float
    brackt : input int
    stpmin : input float
    stpmax : input float
    
    Returns
    -------
    stx : float
    fx : float
    dx : float
    sty : float
    fy : float
    dy : float
    stp : float
    brackt : int
    """
    pass

# classes

class __minpack2_error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff953878e0>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.optimize._minpack2', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff953878e0>, origin='/.venv/lib/python3.8/site-packages/scipy/optimize/_minpack2.cpython-38-aarch64-linux-gnu.so')"

