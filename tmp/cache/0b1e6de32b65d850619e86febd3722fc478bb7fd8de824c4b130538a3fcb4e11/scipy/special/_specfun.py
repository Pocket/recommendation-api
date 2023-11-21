# encoding: utf-8
# module scipy.special._specfun
# from /.venv/lib/python3.8/site-packages/scipy/special/_specfun.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
"""
This module '_specfun' is auto-generated with f2py (version:2).
Functions:
  cqm,cqd = clqmn(m,n,z)
  qm,qd = lqmn(m,n,x)
  cpm,cpd = clpmn(m,n,x,y,ntype)
  n,m,pcode,zo = jdzo(nt)
  bn = bernob(n)
  cqn,cqd = clqn(n,z)
  xa,xb,xc,xd = airyzo(nt,kf=1)
  en = eulerb(n)
  qn,qd = lqnb(n,x)
  vm,vl,dl = lamv(v,x)
  dv,dp,pdf,pdd = pbdv(v,x)
  zo = cerzo(nt)
  nm,bl,dl = lamn(n,x)
  cpn,cpd = clpn(n,z)
  pm,pd = lpmn(m,n,x)
  zo = fcszo(kf,nt)
  cpb,cpd = cpbdn(n,z)
  pn,pd = lpn(n,x)
  fc = fcoef(kd,m,q,a)
  nm,ry,dy = rcty(n,x)
  zo,zv = cyzo(nt,kf,kc)
  zo = klvnzo(nt,kd)
  rj0,rj1,ry0,ry1 = jyzo(n,nt)
  nm,rj,dj = rctj(n,x)
  cv,eg = segv(m,n,c,kd)
.
"""
# no imports

# Variables with simple values

__version__ = b'$Revision: $'

# functions

def airyzo(nt, kf=None): # real signature unknown; restored from __doc__
    """
    xa,xb,xc,xd = airyzo(nt,[kf])
    
    Wrapper for ``airyzo``.
    
    Parameters
    ----------
    nt : input int
    
    Other Parameters
    ----------------
    kf : input int, optional
        Default: 1
    
    Returns
    -------
    xa : rank-1 array('d') with bounds (nt)
    xb : rank-1 array('d') with bounds (nt)
    xc : rank-1 array('d') with bounds (nt)
    xd : rank-1 array('d') with bounds (nt)
    """
    pass

def bernob(n): # real signature unknown; restored from __doc__
    """
    bn = bernob(n)
    
    Wrapper for ``bernob``.
    
    Parameters
    ----------
    n : input int
    
    Returns
    -------
    bn : rank-1 array('d') with bounds (n + 1)
    """
    pass

def cerzo(nt): # real signature unknown; restored from __doc__
    """
    zo = cerzo(nt)
    
    Wrapper for ``cerzo``.
    
    Parameters
    ----------
    nt : input int
    
    Returns
    -------
    zo : rank-1 array('D') with bounds (nt)
    """
    pass

def clpmn(m, n, x, y, ntype): # real signature unknown; restored from __doc__
    """
    cpm,cpd = clpmn(m,n,x,y,ntype)
    
    Wrapper for ``clpmn``.
    
    Parameters
    ----------
    m : input int
    n : input int
    x : input float
    y : input float
    ntype : input int
    
    Returns
    -------
    cpm : rank-2 array('D') with bounds (m + 1,n + 1)
    cpd : rank-2 array('D') with bounds (m + 1,n + 1)
    """
    pass

def clpn(n, z): # real signature unknown; restored from __doc__
    """
    cpn,cpd = clpn(n,z)
    
    Wrapper for ``clpn``.
    
    Parameters
    ----------
    n : input int
    z : input complex
    
    Returns
    -------
    cpn : rank-1 array('D') with bounds (n + 1)
    cpd : rank-1 array('D') with bounds (n + 1)
    """
    pass

def clqmn(m, n, z): # real signature unknown; restored from __doc__
    """
    cqm,cqd = clqmn(m,n,z)
    
    Wrapper for ``clqmn``.
    
    Parameters
    ----------
    m : input int
    n : input int
    z : input complex
    
    Returns
    -------
    cqm : rank-2 array('D') with bounds (mm + 1,n + 1)
    cqd : rank-2 array('D') with bounds (mm + 1,n + 1)
    """
    pass

def clqn(n, z): # real signature unknown; restored from __doc__
    """
    cqn,cqd = clqn(n,z)
    
    Wrapper for ``clqn``.
    
    Parameters
    ----------
    n : input int
    z : input complex
    
    Returns
    -------
    cqn : rank-1 array('D') with bounds (n + 1)
    cqd : rank-1 array('D') with bounds (n + 1)
    """
    pass

def cpbdn(n, z): # real signature unknown; restored from __doc__
    """
    cpb,cpd = cpbdn(n,z)
    
    Wrapper for ``cpbdn``.
    
    Parameters
    ----------
    n : input int
    z : input complex
    
    Returns
    -------
    cpb : rank-1 array('D') with bounds (abs(n)+2)
    cpd : rank-1 array('D') with bounds (abs(n)+2)
    """
    pass

def cyzo(nt, kf, kc): # real signature unknown; restored from __doc__
    """
    zo,zv = cyzo(nt,kf,kc)
    
    Wrapper for ``cyzo``.
    
    Parameters
    ----------
    nt : input int
    kf : input int
    kc : input int
    
    Returns
    -------
    zo : rank-1 array('D') with bounds (nt)
    zv : rank-1 array('D') with bounds (nt)
    """
    pass

def eulerb(n): # real signature unknown; restored from __doc__
    """
    en = eulerb(n)
    
    Wrapper for ``eulerb``.
    
    Parameters
    ----------
    n : input int
    
    Returns
    -------
    en : rank-1 array('d') with bounds (n + 1)
    """
    pass

def fcoef(kd, m, q, a): # real signature unknown; restored from __doc__
    """
    fc = fcoef(kd,m,q,a)
    
    Wrapper for ``fcoef``.
    
    Parameters
    ----------
    kd : input int
    m : input int
    q : input float
    a : input float
    
    Returns
    -------
    fc : rank-1 array('d') with bounds (251)
    """
    pass

def fcszo(kf, nt): # real signature unknown; restored from __doc__
    """
    zo = fcszo(kf,nt)
    
    Wrapper for ``fcszo``.
    
    Parameters
    ----------
    kf : input int
    nt : input int
    
    Returns
    -------
    zo : rank-1 array('D') with bounds (nt)
    """
    pass

def jdzo(nt): # real signature unknown; restored from __doc__
    """
    n,m,pcode,zo = jdzo(nt)
    
    Wrapper for ``jdzo``.
    
    Parameters
    ----------
    nt : input int
    
    Returns
    -------
    n : rank-1 array('i') with bounds (1400)
    m : rank-1 array('i') with bounds (1400)
    pcode : rank-1 array('i') with bounds (1400)
    zo : rank-1 array('d') with bounds (1401)
    """
    pass

def jyzo(n, nt): # real signature unknown; restored from __doc__
    """
    rj0,rj1,ry0,ry1 = jyzo(n,nt)
    
    Wrapper for ``jyzo``.
    
    Parameters
    ----------
    n : input int
    nt : input int
    
    Returns
    -------
    rj0 : rank-1 array('d') with bounds (nt)
    rj1 : rank-1 array('d') with bounds (nt)
    ry0 : rank-1 array('d') with bounds (nt)
    ry1 : rank-1 array('d') with bounds (nt)
    """
    pass

def klvnzo(nt, kd): # real signature unknown; restored from __doc__
    """
    zo = klvnzo(nt,kd)
    
    Wrapper for ``klvnzo``.
    
    Parameters
    ----------
    nt : input int
    kd : input int
    
    Returns
    -------
    zo : rank-1 array('d') with bounds (nt)
    """
    pass

def lamn(n, x): # real signature unknown; restored from __doc__
    """
    nm,bl,dl = lamn(n,x)
    
    Wrapper for ``lamn``.
    
    Parameters
    ----------
    n : input int
    x : input float
    
    Returns
    -------
    nm : int
    bl : rank-1 array('d') with bounds (n + 1)
    dl : rank-1 array('d') with bounds (n + 1)
    """
    pass

def lamv(v, x): # real signature unknown; restored from __doc__
    """
    vm,vl,dl = lamv(v,x)
    
    Wrapper for ``lamv``.
    
    Parameters
    ----------
    v : input float
    x : input float
    
    Returns
    -------
    vm : float
    vl : rank-1 array('d') with bounds ((int)v+1)
    dl : rank-1 array('d') with bounds ((int)v+1)
    """
    pass

def lpmn(m, n, x): # real signature unknown; restored from __doc__
    """
    pm,pd = lpmn(m,n,x)
    
    Wrapper for ``lpmn``.
    
    Parameters
    ----------
    m : input int
    n : input int
    x : input float
    
    Returns
    -------
    pm : rank-2 array('d') with bounds (m + 1,n + 1)
    pd : rank-2 array('d') with bounds (m + 1,n + 1)
    """
    pass

def lpn(n, x): # real signature unknown; restored from __doc__
    """
    pn,pd = lpn(n,x)
    
    Wrapper for ``lpn``.
    
    Parameters
    ----------
    n : input int
    x : input float
    
    Returns
    -------
    pn : rank-1 array('d') with bounds (n + 1)
    pd : rank-1 array('d') with bounds (n + 1)
    """
    pass

def lqmn(m, n, x): # real signature unknown; restored from __doc__
    """
    qm,qd = lqmn(m,n,x)
    
    Wrapper for ``lqmn``.
    
    Parameters
    ----------
    m : input int
    n : input int
    x : input float
    
    Returns
    -------
    qm : rank-2 array('d') with bounds (mm + 1,n + 1)
    qd : rank-2 array('d') with bounds (mm + 1,n + 1)
    """
    pass

def lqnb(n, x): # real signature unknown; restored from __doc__
    """
    qn,qd = lqnb(n,x)
    
    Wrapper for ``lqnb``.
    
    Parameters
    ----------
    n : input int
    x : input float
    
    Returns
    -------
    qn : rank-1 array('d') with bounds (n + 1)
    qd : rank-1 array('d') with bounds (n + 1)
    """
    pass

def pbdv(v, x): # real signature unknown; restored from __doc__
    """
    dv,dp,pdf,pdd = pbdv(v,x)
    
    Wrapper for ``pbdv``.
    
    Parameters
    ----------
    v : input float
    x : input float
    
    Returns
    -------
    dv : rank-1 array('d') with bounds (abs((int)v)+2)
    dp : rank-1 array('d') with bounds (abs((int)v)+2)
    pdf : float
    pdd : float
    """
    pass

def rctj(n, x): # real signature unknown; restored from __doc__
    """
    nm,rj,dj = rctj(n,x)
    
    Wrapper for ``rctj``.
    
    Parameters
    ----------
    n : input int
    x : input float
    
    Returns
    -------
    nm : int
    rj : rank-1 array('d') with bounds (n + 1)
    dj : rank-1 array('d') with bounds (n + 1)
    """
    pass

def rcty(n, x): # real signature unknown; restored from __doc__
    """
    nm,ry,dy = rcty(n,x)
    
    Wrapper for ``rcty``.
    
    Parameters
    ----------
    n : input int
    x : input float
    
    Returns
    -------
    nm : int
    ry : rank-1 array('d') with bounds (n + 1)
    dy : rank-1 array('d') with bounds (n + 1)
    """
    pass

def segv(m, n, c, kd): # real signature unknown; restored from __doc__
    """
    cv,eg = segv(m,n,c,kd)
    
    Wrapper for ``segv``.
    
    Parameters
    ----------
    m : input int
    n : input int
    c : input float
    kd : input int
    
    Returns
    -------
    cv : float
    eg : rank-1 array('d') with bounds (n-m+2)
    """
    pass

# classes

class __specfun_error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9beeafa0>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.special._specfun', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9beeafa0>, origin='/.venv/lib/python3.8/site-packages/scipy/special/_specfun.cpython-38-aarch64-linux-gnu.so')"

