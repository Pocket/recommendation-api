# encoding: utf-8
# module scipy.sparse.linalg._isolve._iterative
# from /.venv/lib/python3.8/site-packages/scipy/sparse/linalg/_isolve/_iterative.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
"""
This module '_iterative' is auto-generated with f2py (version:2).
Functions:
  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = sbicgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = dbicgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = cbicgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = zbicgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = sbicgstabrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = dbicgstabrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = cbicgstabrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = zbicgstabrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = scgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = dcgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = ccgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = zcgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = scgsrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = dcgsrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = ccgsrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = zcgsrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = sqmrrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = dqmrrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = cqmrrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = zqmrrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = sgmresrevcom(b,x,restrt,work,work2,iter,resid,info,ndx1,ndx2,ijob,tol)
  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = dgmresrevcom(b,x,restrt,work,work2,iter,resid,info,ndx1,ndx2,ijob,tol)
  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = cgmresrevcom(b,x,restrt,work,work2,iter,resid,info,ndx1,ndx2,ijob,tol)
  x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = zgmresrevcom(b,x,restrt,work,work2,iter,resid,info,ndx1,ndx2,ijob,tol)
.
"""
# no imports

# Variables with simple values

__version__ = b'$Revision: $'

# functions

def cbicgrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob): # real signature unknown; restored from __doc__
    """
    x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = cbicgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
    
    Wrapper for ``cbicgrevcom``.
    
    Parameters
    ----------
    b : input rank-1 array('F') with bounds (n)
    x : input rank-1 array('F') with bounds (n)
    work : in/output rank-1 array('F') with bounds (6 * ldw)
    iter : input int
    resid : input float
    info : input int
    ndx1 : input int
    ndx2 : input int
    ijob : input int
    
    Returns
    -------
    x : rank-1 array('F') with bounds (n)
    iter : int
    resid : float
    info : int
    ndx1 : int
    ndx2 : int
    sclr1 : complex
    sclr2 : complex
    ijob : int
    """
    pass

def cbicgstabrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob): # real signature unknown; restored from __doc__
    """
    x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = cbicgstabrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
    
    Wrapper for ``cbicgstabrevcom``.
    
    Parameters
    ----------
    b : input rank-1 array('F') with bounds (n)
    x : input rank-1 array('F') with bounds (n)
    work : in/output rank-1 array('F') with bounds (7 * ldw)
    iter : input int
    resid : input float
    info : input int
    ndx1 : input int
    ndx2 : input int
    ijob : input int
    
    Returns
    -------
    x : rank-1 array('F') with bounds (n)
    iter : int
    resid : float
    info : int
    ndx1 : int
    ndx2 : int
    sclr1 : complex
    sclr2 : complex
    ijob : int
    """
    pass

def ccgrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob): # real signature unknown; restored from __doc__
    """
    x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = ccgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
    
    Wrapper for ``ccgrevcom``.
    
    Parameters
    ----------
    b : input rank-1 array('F') with bounds (n)
    x : input rank-1 array('F') with bounds (n)
    work : in/output rank-1 array('F') with bounds (4 * ldw)
    iter : input int
    resid : input float
    info : input int
    ndx1 : input int
    ndx2 : input int
    ijob : input int
    
    Returns
    -------
    x : rank-1 array('F') with bounds (n)
    iter : int
    resid : float
    info : int
    ndx1 : int
    ndx2 : int
    sclr1 : complex
    sclr2 : complex
    ijob : int
    """
    pass

def ccgsrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob): # real signature unknown; restored from __doc__
    """
    x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = ccgsrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
    
    Wrapper for ``ccgsrevcom``.
    
    Parameters
    ----------
    b : input rank-1 array('F') with bounds (n)
    x : input rank-1 array('F') with bounds (n)
    work : in/output rank-1 array('F') with bounds (7 * ldw)
    iter : input int
    resid : input float
    info : input int
    ndx1 : input int
    ndx2 : input int
    ijob : input int
    
    Returns
    -------
    x : rank-1 array('F') with bounds (n)
    iter : int
    resid : float
    info : int
    ndx1 : int
    ndx2 : int
    sclr1 : complex
    sclr2 : complex
    ijob : int
    """
    pass

def cgmresrevcom(b, x, restrt, work, work2, iter, resid, info, ndx1, ndx2, ijob, tol): # real signature unknown; restored from __doc__
    """
    x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = cgmresrevcom(b,x,restrt,work,work2,iter,resid,info,ndx1,ndx2,ijob,tol)
    
    Wrapper for ``cgmresrevcom``.
    
    Parameters
    ----------
    b : input rank-1 array('F') with bounds (n)
    x : input rank-1 array('F') with bounds (n)
    restrt : input int
    work : in/output rank-1 array('F') with bounds (ldw*(6+restrt))
    work2 : in/output rank-1 array('F') with bounds (ldw2*(2*restrt+2))
    iter : input int
    resid : input float
    info : input int
    ndx1 : input int
    ndx2 : input int
    ijob : input int
    tol : input float
    
    Returns
    -------
    x : rank-1 array('F') with bounds (n)
    iter : int
    resid : float
    info : int
    ndx1 : int
    ndx2 : int
    sclr1 : complex
    sclr2 : complex
    ijob : int
    """
    pass

def cqmrrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob): # real signature unknown; restored from __doc__
    """
    x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = cqmrrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
    
    Wrapper for ``cqmrrevcom``.
    
    Parameters
    ----------
    b : input rank-1 array('F') with bounds (n)
    x : input rank-1 array('F') with bounds (n)
    work : in/output rank-1 array('F') with bounds (11 * ldw)
    iter : input int
    resid : input float
    info : input int
    ndx1 : input int
    ndx2 : input int
    ijob : input int
    
    Returns
    -------
    x : rank-1 array('F') with bounds (n)
    iter : int
    resid : float
    info : int
    ndx1 : int
    ndx2 : int
    sclr1 : complex
    sclr2 : complex
    ijob : int
    """
    pass

def dbicgrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob): # real signature unknown; restored from __doc__
    """
    x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = dbicgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
    
    Wrapper for ``dbicgrevcom``.
    
    Parameters
    ----------
    b : input rank-1 array('d') with bounds (n)
    x : input rank-1 array('d') with bounds (n)
    work : in/output rank-1 array('d') with bounds (6 * ldw)
    iter : input int
    resid : input float
    info : input int
    ndx1 : input int
    ndx2 : input int
    ijob : input int
    
    Returns
    -------
    x : rank-1 array('d') with bounds (n)
    iter : int
    resid : float
    info : int
    ndx1 : int
    ndx2 : int
    sclr1 : float
    sclr2 : float
    ijob : int
    """
    pass

def dbicgstabrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob): # real signature unknown; restored from __doc__
    """
    x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = dbicgstabrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
    
    Wrapper for ``dbicgstabrevcom``.
    
    Parameters
    ----------
    b : input rank-1 array('d') with bounds (n)
    x : input rank-1 array('d') with bounds (n)
    work : in/output rank-1 array('d') with bounds (7 * ldw)
    iter : input int
    resid : input float
    info : input int
    ndx1 : input int
    ndx2 : input int
    ijob : input int
    
    Returns
    -------
    x : rank-1 array('d') with bounds (n)
    iter : int
    resid : float
    info : int
    ndx1 : int
    ndx2 : int
    sclr1 : float
    sclr2 : float
    ijob : int
    """
    pass

def dcgrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob): # real signature unknown; restored from __doc__
    """
    x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = dcgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
    
    Wrapper for ``dcgrevcom``.
    
    Parameters
    ----------
    b : input rank-1 array('d') with bounds (n)
    x : input rank-1 array('d') with bounds (n)
    work : in/output rank-1 array('d') with bounds (4 * ldw)
    iter : input int
    resid : input float
    info : input int
    ndx1 : input int
    ndx2 : input int
    ijob : input int
    
    Returns
    -------
    x : rank-1 array('d') with bounds (n)
    iter : int
    resid : float
    info : int
    ndx1 : int
    ndx2 : int
    sclr1 : float
    sclr2 : float
    ijob : int
    """
    pass

def dcgsrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob): # real signature unknown; restored from __doc__
    """
    x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = dcgsrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
    
    Wrapper for ``dcgsrevcom``.
    
    Parameters
    ----------
    b : input rank-1 array('d') with bounds (n)
    x : input rank-1 array('d') with bounds (n)
    work : in/output rank-1 array('d') with bounds (7 * ldw)
    iter : input int
    resid : input float
    info : input int
    ndx1 : input int
    ndx2 : input int
    ijob : input int
    
    Returns
    -------
    x : rank-1 array('d') with bounds (n)
    iter : int
    resid : float
    info : int
    ndx1 : int
    ndx2 : int
    sclr1 : float
    sclr2 : float
    ijob : int
    """
    pass

def dgmresrevcom(b, x, restrt, work, work2, iter, resid, info, ndx1, ndx2, ijob, tol): # real signature unknown; restored from __doc__
    """
    x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = dgmresrevcom(b,x,restrt,work,work2,iter,resid,info,ndx1,ndx2,ijob,tol)
    
    Wrapper for ``dgmresrevcom``.
    
    Parameters
    ----------
    b : input rank-1 array('d') with bounds (n)
    x : input rank-1 array('d') with bounds (n)
    restrt : input int
    work : in/output rank-1 array('d') with bounds (ldw*(6+restrt))
    work2 : in/output rank-1 array('d') with bounds (ldw2*(2*restrt+2))
    iter : input int
    resid : input float
    info : input int
    ndx1 : input int
    ndx2 : input int
    ijob : input int
    tol : input float
    
    Returns
    -------
    x : rank-1 array('d') with bounds (n)
    iter : int
    resid : float
    info : int
    ndx1 : int
    ndx2 : int
    sclr1 : float
    sclr2 : float
    ijob : int
    """
    pass

def dqmrrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob): # real signature unknown; restored from __doc__
    """
    x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = dqmrrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
    
    Wrapper for ``dqmrrevcom``.
    
    Parameters
    ----------
    b : input rank-1 array('d') with bounds (n)
    x : input rank-1 array('d') with bounds (n)
    work : in/output rank-1 array('d') with bounds (11 * ldw)
    iter : input int
    resid : input float
    info : input int
    ndx1 : input int
    ndx2 : input int
    ijob : input int
    
    Returns
    -------
    x : rank-1 array('d') with bounds (n)
    iter : int
    resid : float
    info : int
    ndx1 : int
    ndx2 : int
    sclr1 : float
    sclr2 : float
    ijob : int
    """
    pass

def sbicgrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob): # real signature unknown; restored from __doc__
    """
    x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = sbicgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
    
    Wrapper for ``sbicgrevcom``.
    
    Parameters
    ----------
    b : input rank-1 array('f') with bounds (n)
    x : input rank-1 array('f') with bounds (n)
    work : in/output rank-1 array('f') with bounds (6 * ldw)
    iter : input int
    resid : input float
    info : input int
    ndx1 : input int
    ndx2 : input int
    ijob : input int
    
    Returns
    -------
    x : rank-1 array('f') with bounds (n)
    iter : int
    resid : float
    info : int
    ndx1 : int
    ndx2 : int
    sclr1 : float
    sclr2 : float
    ijob : int
    """
    pass

def sbicgstabrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob): # real signature unknown; restored from __doc__
    """
    x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = sbicgstabrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
    
    Wrapper for ``sbicgstabrevcom``.
    
    Parameters
    ----------
    b : input rank-1 array('f') with bounds (n)
    x : input rank-1 array('f') with bounds (n)
    work : in/output rank-1 array('f') with bounds (7 * ldw)
    iter : input int
    resid : input float
    info : input int
    ndx1 : input int
    ndx2 : input int
    ijob : input int
    
    Returns
    -------
    x : rank-1 array('f') with bounds (n)
    iter : int
    resid : float
    info : int
    ndx1 : int
    ndx2 : int
    sclr1 : float
    sclr2 : float
    ijob : int
    """
    pass

def scgrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob): # real signature unknown; restored from __doc__
    """
    x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = scgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
    
    Wrapper for ``scgrevcom``.
    
    Parameters
    ----------
    b : input rank-1 array('f') with bounds (n)
    x : input rank-1 array('f') with bounds (n)
    work : in/output rank-1 array('f') with bounds (4 * ldw)
    iter : input int
    resid : input float
    info : input int
    ndx1 : input int
    ndx2 : input int
    ijob : input int
    
    Returns
    -------
    x : rank-1 array('f') with bounds (n)
    iter : int
    resid : float
    info : int
    ndx1 : int
    ndx2 : int
    sclr1 : float
    sclr2 : float
    ijob : int
    """
    pass

def scgsrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob): # real signature unknown; restored from __doc__
    """
    x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = scgsrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
    
    Wrapper for ``scgsrevcom``.
    
    Parameters
    ----------
    b : input rank-1 array('f') with bounds (n)
    x : input rank-1 array('f') with bounds (n)
    work : in/output rank-1 array('f') with bounds (7 * ldw)
    iter : input int
    resid : input float
    info : input int
    ndx1 : input int
    ndx2 : input int
    ijob : input int
    
    Returns
    -------
    x : rank-1 array('f') with bounds (n)
    iter : int
    resid : float
    info : int
    ndx1 : int
    ndx2 : int
    sclr1 : float
    sclr2 : float
    ijob : int
    """
    pass

def sgmresrevcom(b, x, restrt, work, work2, iter, resid, info, ndx1, ndx2, ijob, tol): # real signature unknown; restored from __doc__
    """
    x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = sgmresrevcom(b,x,restrt,work,work2,iter,resid,info,ndx1,ndx2,ijob,tol)
    
    Wrapper for ``sgmresrevcom``.
    
    Parameters
    ----------
    b : input rank-1 array('f') with bounds (n)
    x : input rank-1 array('f') with bounds (n)
    restrt : input int
    work : in/output rank-1 array('f') with bounds (ldw*(6+restrt))
    work2 : in/output rank-1 array('f') with bounds (ldw2*(2*restrt+2))
    iter : input int
    resid : input float
    info : input int
    ndx1 : input int
    ndx2 : input int
    ijob : input int
    tol : input float
    
    Returns
    -------
    x : rank-1 array('f') with bounds (n)
    iter : int
    resid : float
    info : int
    ndx1 : int
    ndx2 : int
    sclr1 : float
    sclr2 : float
    ijob : int
    """
    pass

def sqmrrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob): # real signature unknown; restored from __doc__
    """
    x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = sqmrrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
    
    Wrapper for ``sqmrrevcom``.
    
    Parameters
    ----------
    b : input rank-1 array('f') with bounds (n)
    x : input rank-1 array('f') with bounds (n)
    work : in/output rank-1 array('f') with bounds (11 * ldw)
    iter : input int
    resid : input float
    info : input int
    ndx1 : input int
    ndx2 : input int
    ijob : input int
    
    Returns
    -------
    x : rank-1 array('f') with bounds (n)
    iter : int
    resid : float
    info : int
    ndx1 : int
    ndx2 : int
    sclr1 : float
    sclr2 : float
    ijob : int
    """
    pass

def zbicgrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob): # real signature unknown; restored from __doc__
    """
    x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = zbicgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
    
    Wrapper for ``zbicgrevcom``.
    
    Parameters
    ----------
    b : input rank-1 array('D') with bounds (n)
    x : input rank-1 array('D') with bounds (n)
    work : in/output rank-1 array('D') with bounds (6 * ldw)
    iter : input int
    resid : input float
    info : input int
    ndx1 : input int
    ndx2 : input int
    ijob : input int
    
    Returns
    -------
    x : rank-1 array('D') with bounds (n)
    iter : int
    resid : float
    info : int
    ndx1 : int
    ndx2 : int
    sclr1 : complex
    sclr2 : complex
    ijob : int
    """
    pass

def zbicgstabrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob): # real signature unknown; restored from __doc__
    """
    x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = zbicgstabrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
    
    Wrapper for ``zbicgstabrevcom``.
    
    Parameters
    ----------
    b : input rank-1 array('D') with bounds (n)
    x : input rank-1 array('D') with bounds (n)
    work : in/output rank-1 array('D') with bounds (7 * ldw)
    iter : input int
    resid : input float
    info : input int
    ndx1 : input int
    ndx2 : input int
    ijob : input int
    
    Returns
    -------
    x : rank-1 array('D') with bounds (n)
    iter : int
    resid : float
    info : int
    ndx1 : int
    ndx2 : int
    sclr1 : complex
    sclr2 : complex
    ijob : int
    """
    pass

def zcgrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob): # real signature unknown; restored from __doc__
    """
    x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = zcgrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
    
    Wrapper for ``zcgrevcom``.
    
    Parameters
    ----------
    b : input rank-1 array('D') with bounds (n)
    x : input rank-1 array('D') with bounds (n)
    work : in/output rank-1 array('D') with bounds (4 * ldw)
    iter : input int
    resid : input float
    info : input int
    ndx1 : input int
    ndx2 : input int
    ijob : input int
    
    Returns
    -------
    x : rank-1 array('D') with bounds (n)
    iter : int
    resid : float
    info : int
    ndx1 : int
    ndx2 : int
    sclr1 : complex
    sclr2 : complex
    ijob : int
    """
    pass

def zcgsrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob): # real signature unknown; restored from __doc__
    """
    x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = zcgsrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
    
    Wrapper for ``zcgsrevcom``.
    
    Parameters
    ----------
    b : input rank-1 array('D') with bounds (n)
    x : input rank-1 array('D') with bounds (n)
    work : in/output rank-1 array('D') with bounds (7 * ldw)
    iter : input int
    resid : input float
    info : input int
    ndx1 : input int
    ndx2 : input int
    ijob : input int
    
    Returns
    -------
    x : rank-1 array('D') with bounds (n)
    iter : int
    resid : float
    info : int
    ndx1 : int
    ndx2 : int
    sclr1 : complex
    sclr2 : complex
    ijob : int
    """
    pass

def zgmresrevcom(b, x, restrt, work, work2, iter, resid, info, ndx1, ndx2, ijob, tol): # real signature unknown; restored from __doc__
    """
    x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = zgmresrevcom(b,x,restrt,work,work2,iter,resid,info,ndx1,ndx2,ijob,tol)
    
    Wrapper for ``zgmresrevcom``.
    
    Parameters
    ----------
    b : input rank-1 array('D') with bounds (n)
    x : input rank-1 array('D') with bounds (n)
    restrt : input int
    work : in/output rank-1 array('D') with bounds (ldw*(6+restrt))
    work2 : in/output rank-1 array('D') with bounds (ldw2*(2*restrt+2))
    iter : input int
    resid : input float
    info : input int
    ndx1 : input int
    ndx2 : input int
    ijob : input int
    tol : input float
    
    Returns
    -------
    x : rank-1 array('D') with bounds (n)
    iter : int
    resid : float
    info : int
    ndx1 : int
    ndx2 : int
    sclr1 : complex
    sclr2 : complex
    ijob : int
    """
    pass

def zqmrrevcom(b, x, work, iter, resid, info, ndx1, ndx2, ijob): # real signature unknown; restored from __doc__
    """
    x,iter,resid,info,ndx1,ndx2,sclr1,sclr2,ijob = zqmrrevcom(b,x,work,iter,resid,info,ndx1,ndx2,ijob)
    
    Wrapper for ``zqmrrevcom``.
    
    Parameters
    ----------
    b : input rank-1 array('D') with bounds (n)
    x : input rank-1 array('D') with bounds (n)
    work : in/output rank-1 array('D') with bounds (11 * ldw)
    iter : input int
    resid : input float
    info : input int
    ndx1 : input int
    ndx2 : input int
    ijob : input int
    
    Returns
    -------
    x : rank-1 array('D') with bounds (n)
    iter : int
    resid : float
    info : int
    ndx1 : int
    ndx2 : int
    sclr1 : complex
    sclr2 : complex
    ijob : int
    """
    pass

# classes

class __iterative_error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9f1d5e50>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.sparse.linalg._isolve._iterative', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9f1d5e50>, origin='/.venv/lib/python3.8/site-packages/scipy/sparse/linalg/_isolve/_iterative.cpython-38-aarch64-linux-gnu.so')"

