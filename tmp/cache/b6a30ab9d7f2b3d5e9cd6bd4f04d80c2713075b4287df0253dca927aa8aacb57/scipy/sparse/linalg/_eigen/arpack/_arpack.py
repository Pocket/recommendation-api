# encoding: utf-8
# module scipy.sparse.linalg._eigen.arpack._arpack
# from /.venv/lib/python3.8/site-packages/scipy/sparse/linalg/_eigen/arpack/_arpack.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
"""
This module '_arpack' is auto-generated with f2py (version:2).
Functions:
  ido,tol,resid,v,iparam,ipntr,info = ssaupd(ido,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,n=len(resid),ncv=shape(v,1),ldv=shape(v,0),lworkl=len(workl))
  ido,tol,resid,v,iparam,ipntr,info = dsaupd(ido,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,n=len(resid),ncv=shape(v,1),ldv=shape(v,0),lworkl=len(workl))
  d,z,info = sseupd(rvec,howmny,select,sigma,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,ldz=shape(z,0),n=len(resid),ncv=len(select),ldv=shape(v,0),lworkl=len(workl))
  d,z,info = dseupd(rvec,howmny,select,sigma,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,ldz=shape(z,0),n=len(resid),ncv=len(select),ldv=shape(v,0),lworkl=len(workl))
  ido,tol,resid,v,iparam,ipntr,info = snaupd(ido,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,n=len(resid),ncv=shape(v,1),ldv=shape(v,0),lworkl=len(workl))
  ido,tol,resid,v,iparam,ipntr,info = dnaupd(ido,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,n=len(resid),ncv=shape(v,1),ldv=shape(v,0),lworkl=len(workl))
  dr,di,z,info = sneupd(rvec,howmny,select,sigmar,sigmai,workev,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,ldz=shape(z,0),n=len(resid),ncv=len(select),ldv=shape(v,0),lworkl=len(workl))
  dr,di,z,info = dneupd(rvec,howmny,select,sigmar,sigmai,workev,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,ldz=shape(z,0),n=len(resid),ncv=len(select),ldv=shape(v,0),lworkl=len(workl))
  ido,tol,resid,v,iparam,ipntr,info = cnaupd(ido,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,rwork,info,n=len(resid),ncv=shape(v,1),ldv=shape(v,0),lworkl=len(workl))
  ido,tol,resid,v,iparam,ipntr,info = znaupd(ido,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,rwork,info,n=len(resid),ncv=shape(v,1),ldv=shape(v,0),lworkl=len(workl))
  d,z,info = cneupd(rvec,howmny,select,sigma,workev,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,rwork,info,ldz=shape(z,0),n=len(resid),ncv=len(select),ldv=shape(v,0),lworkl=len(workl))
  d,z,info = zneupd(rvec,howmny,select,sigma,workev,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,rwork,info,ldz=shape(z,0),n=len(resid),ncv=len(select),ldv=shape(v,0),lworkl=len(workl))
COMMON blocks:
  /debug/ logfil,ndigit,mgetv0,msaupd,msaup2,msaitr,mseigt,msapps,msgets,mseupd,mnaupd,mnaup2,mnaitr,mneigh,mnapps,mngets,mneupd,mcaupd,mcaup2,mcaitr,mceigh,mcapps,mcgets,mceupd
  /timing/ nopx,nbx,nrorth,nitref,nrstrt,tsaupd,tsaup2,tsaitr,tseigt,tsgets,tsapps,tsconv,tnaupd,tnaup2,tnaitr,tneigh,tngets,tnapps,tnconv,tcaupd,tcaup2,tcaitr,tceigh,tcgets,tcapps,tcconv,tmvopx,tmvbx,tgetv0,titref,trvec
.
"""
# no imports

# Variables with simple values

__version__ = b'$Revision: $'

# functions

def cnaupd(ido, bmat, which, nev, tol, resid, v, iparam, ipntr, workd, workl, rwork, info, n=None, ncv=None, ldv=None, lworkl=None): # real signature unknown; restored from __doc__
    """
    ido,tol,resid,v,iparam,ipntr,info = cnaupd(ido,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,rwork,info,[n,ncv,ldv,lworkl])
    
    Wrapper for ``cnaupd``.
    
    Parameters
    ----------
    ido : input int
    bmat : input string(len=1)
    which : input string(len=2)
    nev : input int
    tol : input float
    resid : input rank-1 array('F') with bounds (n)
    v : input rank-2 array('F') with bounds (ldv,ncv)
    iparam : input rank-1 array('i') with bounds (11)
    ipntr : input rank-1 array('i') with bounds (14)
    workd : in/output rank-1 array('F') with bounds (3 * n)
    workl : in/output rank-1 array('F') with bounds (lworkl)
    rwork : in/output rank-1 array('f') with bounds (ncv)
    info : input int
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: len(resid)
    ncv : input int, optional
        Default: shape(v,1)
    ldv : input int, optional
        Default: shape(v,0)
    lworkl : input int, optional
        Default: len(workl)
    
    Returns
    -------
    ido : int
    tol : float
    resid : rank-1 array('F') with bounds (n)
    v : rank-2 array('F') with bounds (ldv,ncv)
    iparam : rank-1 array('i') with bounds (11)
    ipntr : rank-1 array('i') with bounds (14)
    info : int
    """
    pass

def cneupd(rvec, howmny, select, sigma, workev, bmat, which, nev, tol, resid, v, iparam, ipntr, workd, workl, rwork, info, ldz=None, n=None, ncv=None, ldv=None, lworkl=None): # real signature unknown; restored from __doc__
    """
    d,z,info = cneupd(rvec,howmny,select,sigma,workev,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,rwork,info,[ldz,n,ncv,ldv,lworkl])
    
    Wrapper for ``cneupd``.
    
    Parameters
    ----------
    rvec : input int
    howmny : input string(len=1)
    select : input rank-1 array('i') with bounds (ncv)
    sigma : input complex
    workev : input rank-1 array('F') with bounds (3 * ncv)
    bmat : input string(len=1)
    which : input string(len=2)
    nev : input int
    tol : input float
    resid : input rank-1 array('F') with bounds (n)
    v : input rank-2 array('F') with bounds (ldv,ncv)
    iparam : input rank-1 array('i') with bounds (11)
    ipntr : input rank-1 array('i') with bounds (14)
    workd : input rank-1 array('F') with bounds (3 * n)
    workl : input rank-1 array('F') with bounds (lworkl)
    rwork : input rank-1 array('f') with bounds (ncv)
    info : input int
    
    Other Parameters
    ----------------
    ldz : input int, optional
        Default: shape(z,0)
    n : input int, optional
        Default: len(resid)
    ncv : input int, optional
        Default: len(select)
    ldv : input int, optional
        Default: shape(v,0)
    lworkl : input int, optional
        Default: len(workl)
    
    Returns
    -------
    d : rank-1 array('F') with bounds (nev)
    z : rank-2 array('F') with bounds (n,nev)
    info : int
    """
    pass

def debug(*args, **kwargs): # real signature unknown
    """
    'i'-scalar
    'i'-scalar
    'i'-scalar
    'i'-scalar
    'i'-scalar
    'i'-scalar
    'i'-scalar
    'i'-scalar
    'i'-scalar
    'i'-scalar
    'i'-scalar
    'i'-scalar
    'i'-scalar
    'i'-scalar
    'i'-scalar
    'i'-scalar
    'i'-scalar
    'i'-scalar
    'i'-scalar
    'i'-scalar
    'i'-scalar
    'i'-scalar
    'i'-scalar
    'i'-scalar
    """
    pass

def dnaupd(ido, bmat, which, nev, tol, resid, v, iparam, ipntr, workd, workl, info, n=None, ncv=None, ldv=None, lworkl=None): # real signature unknown; restored from __doc__
    """
    ido,tol,resid,v,iparam,ipntr,info = dnaupd(ido,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,[n,ncv,ldv,lworkl])
    
    Wrapper for ``dnaupd``.
    
    Parameters
    ----------
    ido : input int
    bmat : input string(len=1)
    which : input string(len=2)
    nev : input int
    tol : input float
    resid : input rank-1 array('d') with bounds (n)
    v : input rank-2 array('d') with bounds (ldv,ncv)
    iparam : input rank-1 array('i') with bounds (11)
    ipntr : input rank-1 array('i') with bounds (14)
    workd : in/output rank-1 array('d') with bounds (3 * n)
    workl : in/output rank-1 array('d') with bounds (lworkl)
    info : input int
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: len(resid)
    ncv : input int, optional
        Default: shape(v,1)
    ldv : input int, optional
        Default: shape(v,0)
    lworkl : input int, optional
        Default: len(workl)
    
    Returns
    -------
    ido : int
    tol : float
    resid : rank-1 array('d') with bounds (n)
    v : rank-2 array('d') with bounds (ldv,ncv)
    iparam : rank-1 array('i') with bounds (11)
    ipntr : rank-1 array('i') with bounds (14)
    info : int
    """
    pass

def dneupd(rvec, howmny, select, sigmar, sigmai, workev, bmat, which, nev, tol, resid, v, iparam, ipntr, workd, workl, info, ldz=None, n=None, ncv=None, ldv=None, lworkl=None): # real signature unknown; restored from __doc__
    """
    dr,di,z,info = dneupd(rvec,howmny,select,sigmar,sigmai,workev,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,[ldz,n,ncv,ldv,lworkl])
    
    Wrapper for ``dneupd``.
    
    Parameters
    ----------
    rvec : input int
    howmny : input string(len=1)
    select : input rank-1 array('i') with bounds (ncv)
    sigmar : input float
    sigmai : input float
    workev : input rank-1 array('d') with bounds (3 * ncv)
    bmat : input string(len=1)
    which : input string(len=2)
    nev : input int
    tol : input float
    resid : input rank-1 array('d') with bounds (n)
    v : input rank-2 array('d') with bounds (n,ncv)
    iparam : input rank-1 array('i') with bounds (11)
    ipntr : input rank-1 array('i') with bounds (14)
    workd : input rank-1 array('d') with bounds (3 * n)
    workl : input rank-1 array('d') with bounds (lworkl)
    info : input int
    
    Other Parameters
    ----------------
    ldz : input int, optional
        Default: shape(z,0)
    n : input int, optional
        Default: len(resid)
    ncv : input int, optional
        Default: len(select)
    ldv : input int, optional
        Default: shape(v,0)
    lworkl : input int, optional
        Default: len(workl)
    
    Returns
    -------
    dr : rank-1 array('d') with bounds (nev + 1)
    di : rank-1 array('d') with bounds (nev + 1)
    z : rank-2 array('d') with bounds (n,nev + 1)
    info : int
    """
    pass

def dsaupd(ido, bmat, which, nev, tol, resid, v, iparam, ipntr, workd, workl, info, n=None, ncv=None, ldv=None, lworkl=None): # real signature unknown; restored from __doc__
    """
    ido,tol,resid,v,iparam,ipntr,info = dsaupd(ido,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,[n,ncv,ldv,lworkl])
    
    Wrapper for ``dsaupd``.
    
    Parameters
    ----------
    ido : input int
    bmat : input string(len=1)
    which : input string(len=2)
    nev : input int
    tol : input float
    resid : input rank-1 array('d') with bounds (n)
    v : input rank-2 array('d') with bounds (ldv,ncv)
    iparam : input rank-1 array('i') with bounds (11)
    ipntr : input rank-1 array('i') with bounds (11)
    workd : in/output rank-1 array('d') with bounds (3 * n)
    workl : in/output rank-1 array('d') with bounds (lworkl)
    info : input int
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: len(resid)
    ncv : input int, optional
        Default: shape(v,1)
    ldv : input int, optional
        Default: shape(v,0)
    lworkl : input int, optional
        Default: len(workl)
    
    Returns
    -------
    ido : int
    tol : float
    resid : rank-1 array('d') with bounds (n)
    v : rank-2 array('d') with bounds (ldv,ncv)
    iparam : rank-1 array('i') with bounds (11)
    ipntr : rank-1 array('i') with bounds (11)
    info : int
    """
    pass

def dseupd(rvec, howmny, select, sigma, bmat, which, nev, tol, resid, v, iparam, ipntr, workd, workl, info, ldz=None, n=None, ncv=None, ldv=None, lworkl=None): # real signature unknown; restored from __doc__
    """
    d,z,info = dseupd(rvec,howmny,select,sigma,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,[ldz,n,ncv,ldv,lworkl])
    
    Wrapper for ``dseupd``.
    
    Parameters
    ----------
    rvec : input int
    howmny : input string(len=1)
    select : input rank-1 array('i') with bounds (ncv)
    sigma : input float
    bmat : input string(len=1)
    which : input string(len=2)
    nev : input int
    tol : input float
    resid : input rank-1 array('d') with bounds (n)
    v : input rank-2 array('d') with bounds (ldv,ncv)
    iparam : input rank-1 array('i') with bounds (7)
    ipntr : input rank-1 array('i') with bounds (11)
    workd : input rank-1 array('d') with bounds (2 * n)
    workl : input rank-1 array('d') with bounds (lworkl)
    info : input int
    
    Other Parameters
    ----------------
    ldz : input int, optional
        Default: shape(z,0)
    n : input int, optional
        Default: len(resid)
    ncv : input int, optional
        Default: len(select)
    ldv : input int, optional
        Default: shape(v,0)
    lworkl : input int, optional
        Default: len(workl)
    
    Returns
    -------
    d : rank-1 array('d') with bounds (nev)
    z : rank-2 array('d') with bounds (n,nev)
    info : int
    """
    pass

def snaupd(ido, bmat, which, nev, tol, resid, v, iparam, ipntr, workd, workl, info, n=None, ncv=None, ldv=None, lworkl=None): # real signature unknown; restored from __doc__
    """
    ido,tol,resid,v,iparam,ipntr,info = snaupd(ido,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,[n,ncv,ldv,lworkl])
    
    Wrapper for ``snaupd``.
    
    Parameters
    ----------
    ido : input int
    bmat : input string(len=1)
    which : input string(len=2)
    nev : input int
    tol : input float
    resid : input rank-1 array('f') with bounds (n)
    v : input rank-2 array('f') with bounds (ldv,ncv)
    iparam : input rank-1 array('i') with bounds (11)
    ipntr : input rank-1 array('i') with bounds (14)
    workd : in/output rank-1 array('f') with bounds (3 * n)
    workl : in/output rank-1 array('f') with bounds (lworkl)
    info : input int
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: len(resid)
    ncv : input int, optional
        Default: shape(v,1)
    ldv : input int, optional
        Default: shape(v,0)
    lworkl : input int, optional
        Default: len(workl)
    
    Returns
    -------
    ido : int
    tol : float
    resid : rank-1 array('f') with bounds (n)
    v : rank-2 array('f') with bounds (ldv,ncv)
    iparam : rank-1 array('i') with bounds (11)
    ipntr : rank-1 array('i') with bounds (14)
    info : int
    """
    pass

def sneupd(rvec, howmny, select, sigmar, sigmai, workev, bmat, which, nev, tol, resid, v, iparam, ipntr, workd, workl, info, ldz=None, n=None, ncv=None, ldv=None, lworkl=None): # real signature unknown; restored from __doc__
    """
    dr,di,z,info = sneupd(rvec,howmny,select,sigmar,sigmai,workev,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,[ldz,n,ncv,ldv,lworkl])
    
    Wrapper for ``sneupd``.
    
    Parameters
    ----------
    rvec : input int
    howmny : input string(len=1)
    select : input rank-1 array('i') with bounds (ncv)
    sigmar : input float
    sigmai : input float
    workev : input rank-1 array('f') with bounds (3 * ncv)
    bmat : input string(len=1)
    which : input string(len=2)
    nev : input int
    tol : input float
    resid : input rank-1 array('f') with bounds (n)
    v : input rank-2 array('f') with bounds (n,ncv)
    iparam : input rank-1 array('i') with bounds (11)
    ipntr : input rank-1 array('i') with bounds (14)
    workd : input rank-1 array('f') with bounds (3 * n)
    workl : input rank-1 array('f') with bounds (lworkl)
    info : input int
    
    Other Parameters
    ----------------
    ldz : input int, optional
        Default: shape(z,0)
    n : input int, optional
        Default: len(resid)
    ncv : input int, optional
        Default: len(select)
    ldv : input int, optional
        Default: shape(v,0)
    lworkl : input int, optional
        Default: len(workl)
    
    Returns
    -------
    dr : rank-1 array('f') with bounds (nev + 1)
    di : rank-1 array('f') with bounds (nev + 1)
    z : rank-2 array('f') with bounds (n,nev + 1)
    info : int
    """
    pass

def ssaupd(ido, bmat, which, nev, tol, resid, v, iparam, ipntr, workd, workl, info, n=None, ncv=None, ldv=None, lworkl=None): # real signature unknown; restored from __doc__
    """
    ido,tol,resid,v,iparam,ipntr,info = ssaupd(ido,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,[n,ncv,ldv,lworkl])
    
    Wrapper for ``ssaupd``.
    
    Parameters
    ----------
    ido : input int
    bmat : input string(len=1)
    which : input string(len=2)
    nev : input int
    tol : input float
    resid : input rank-1 array('f') with bounds (n)
    v : input rank-2 array('f') with bounds (ldv,ncv)
    iparam : input rank-1 array('i') with bounds (11)
    ipntr : input rank-1 array('i') with bounds (11)
    workd : in/output rank-1 array('f') with bounds (3 * n)
    workl : in/output rank-1 array('f') with bounds (lworkl)
    info : input int
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: len(resid)
    ncv : input int, optional
        Default: shape(v,1)
    ldv : input int, optional
        Default: shape(v,0)
    lworkl : input int, optional
        Default: len(workl)
    
    Returns
    -------
    ido : int
    tol : float
    resid : rank-1 array('f') with bounds (n)
    v : rank-2 array('f') with bounds (ldv,ncv)
    iparam : rank-1 array('i') with bounds (11)
    ipntr : rank-1 array('i') with bounds (11)
    info : int
    """
    pass

def sseupd(rvec, howmny, select, sigma, bmat, which, nev, tol, resid, v, iparam, ipntr, workd, workl, info, ldz=None, n=None, ncv=None, ldv=None, lworkl=None): # real signature unknown; restored from __doc__
    """
    d,z,info = sseupd(rvec,howmny,select,sigma,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,info,[ldz,n,ncv,ldv,lworkl])
    
    Wrapper for ``sseupd``.
    
    Parameters
    ----------
    rvec : input int
    howmny : input string(len=1)
    select : input rank-1 array('i') with bounds (ncv)
    sigma : input float
    bmat : input string(len=1)
    which : input string(len=2)
    nev : input int
    tol : input float
    resid : input rank-1 array('f') with bounds (n)
    v : input rank-2 array('f') with bounds (ldv,ncv)
    iparam : input rank-1 array('i') with bounds (7)
    ipntr : input rank-1 array('i') with bounds (11)
    workd : input rank-1 array('f') with bounds (2 * n)
    workl : input rank-1 array('f') with bounds (lworkl)
    info : input int
    
    Other Parameters
    ----------------
    ldz : input int, optional
        Default: shape(z,0)
    n : input int, optional
        Default: len(resid)
    ncv : input int, optional
        Default: len(select)
    ldv : input int, optional
        Default: shape(v,0)
    lworkl : input int, optional
        Default: len(workl)
    
    Returns
    -------
    d : rank-1 array('f') with bounds (nev)
    z : rank-2 array('f') with bounds (n,nev)
    info : int
    """
    pass

def timing(*args, **kwargs): # real signature unknown
    """
    'i'-scalar
    'i'-scalar
    'i'-scalar
    'i'-scalar
    'i'-scalar
    'f'-scalar
    'f'-scalar
    'f'-scalar
    'f'-scalar
    'f'-scalar
    'f'-scalar
    'f'-scalar
    'f'-scalar
    'f'-scalar
    'f'-scalar
    'f'-scalar
    'f'-scalar
    'f'-scalar
    'f'-scalar
    'f'-scalar
    'f'-scalar
    'f'-scalar
    'f'-scalar
    'f'-scalar
    'f'-scalar
    'f'-scalar
    'f'-scalar
    'f'-scalar
    'f'-scalar
    'f'-scalar
    'f'-scalar
    """
    pass

def znaupd(ido, bmat, which, nev, tol, resid, v, iparam, ipntr, workd, workl, rwork, info, n=None, ncv=None, ldv=None, lworkl=None): # real signature unknown; restored from __doc__
    """
    ido,tol,resid,v,iparam,ipntr,info = znaupd(ido,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,rwork,info,[n,ncv,ldv,lworkl])
    
    Wrapper for ``znaupd``.
    
    Parameters
    ----------
    ido : input int
    bmat : input string(len=1)
    which : input string(len=2)
    nev : input int
    tol : input float
    resid : input rank-1 array('D') with bounds (n)
    v : input rank-2 array('D') with bounds (ldv,ncv)
    iparam : input rank-1 array('i') with bounds (11)
    ipntr : input rank-1 array('i') with bounds (14)
    workd : in/output rank-1 array('D') with bounds (3 * n)
    workl : in/output rank-1 array('D') with bounds (lworkl)
    rwork : in/output rank-1 array('d') with bounds (ncv)
    info : input int
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: len(resid)
    ncv : input int, optional
        Default: shape(v,1)
    ldv : input int, optional
        Default: shape(v,0)
    lworkl : input int, optional
        Default: len(workl)
    
    Returns
    -------
    ido : int
    tol : float
    resid : rank-1 array('D') with bounds (n)
    v : rank-2 array('D') with bounds (ldv,ncv)
    iparam : rank-1 array('i') with bounds (11)
    ipntr : rank-1 array('i') with bounds (14)
    info : int
    """
    pass

def zneupd(rvec, howmny, select, sigma, workev, bmat, which, nev, tol, resid, v, iparam, ipntr, workd, workl, rwork, info, ldz=None, n=None, ncv=None, ldv=None, lworkl=None): # real signature unknown; restored from __doc__
    """
    d,z,info = zneupd(rvec,howmny,select,sigma,workev,bmat,which,nev,tol,resid,v,iparam,ipntr,workd,workl,rwork,info,[ldz,n,ncv,ldv,lworkl])
    
    Wrapper for ``zneupd``.
    
    Parameters
    ----------
    rvec : input int
    howmny : input string(len=1)
    select : input rank-1 array('i') with bounds (ncv)
    sigma : input complex
    workev : input rank-1 array('D') with bounds (3 * ncv)
    bmat : input string(len=1)
    which : input string(len=2)
    nev : input int
    tol : input float
    resid : input rank-1 array('D') with bounds (n)
    v : input rank-2 array('D') with bounds (ldv,ncv)
    iparam : input rank-1 array('i') with bounds (11)
    ipntr : input rank-1 array('i') with bounds (14)
    workd : input rank-1 array('D') with bounds (3 * n)
    workl : input rank-1 array('D') with bounds (lworkl)
    rwork : input rank-1 array('d') with bounds (ncv)
    info : input int
    
    Other Parameters
    ----------------
    ldz : input int, optional
        Default: shape(z,0)
    n : input int, optional
        Default: len(resid)
    ncv : input int, optional
        Default: len(select)
    ldv : input int, optional
        Default: shape(v,0)
    lworkl : input int, optional
        Default: len(workl)
    
    Returns
    -------
    d : rank-1 array('D') with bounds (nev)
    z : rank-2 array('D') with bounds (n,nev)
    info : int
    """
    pass

# classes

class __arpack_error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff994b16a0>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.sparse.linalg._eigen.arpack._arpack', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff994b16a0>, origin='/.venv/lib/python3.8/site-packages/scipy/sparse/linalg/_eigen/arpack/_arpack.cpython-38-aarch64-linux-gnu.so')"

