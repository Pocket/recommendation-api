# encoding: utf-8
# module scipy.interpolate.dfitpack
# from /.venv/lib/python3.8/site-packages/scipy/interpolate/dfitpack.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
"""
This module 'dfitpack' is auto-generated with f2py (version:2).
Functions:
  ier = fpchec(x,t,k)
  y = splev(t,c,k,x,e=0)
  y = splder(t,c,k,x,nu=1,e=0)
  splint,wrk = splint(t,c,k,a,b)
  zero,m,ier = sproot(t,c,mest=3*(n-7))
  d,ier = spalde(t,c,k1,x)
  n,c,fp,ier = curfit(iopt,x,y,w,t,wrk,iwrk,xb=x[0],xe=x[m-1],k=3,s=0.0)
  n,c,fp,ier = percur(iopt,x,y,w,t,wrk,iwrk,k=3,s=0.0)
  n,c,fp,ier = parcur(iopt,ipar,idim,u,x,w,ub,ue,t,wrk,iwrk,k=3.0,s=0.0)
  x,y,w,xb,xe,k,s,n,t,c,fp,fpint,nrdata,ier = fpcurf0(x,y,k,w=1.0,xb=x[0],xe=x[m-1],s=m,nest=(s==0.0?m+k+1:MAX(m/2,2*k1)))
  x,y,w,xb,xe,k,s,n,t,c,fp,fpint,nrdata,ier = fpcurf1(x,y,w,xb,xe,k,s,n,t,c,fp,fpint,nrdata,ier,overwrite_x=1,overwrite_y=1,overwrite_w=1,overwrite_t=1,overwrite_c=1,overwrite_fpint=1,overwrite_nrdata=1)
  x,y,w,xb,xe,k,s,n,t,c,fp,fpint,nrdata,ier = fpcurfm1(x,y,k,t,w=1.0,xb=x[0],xe=x[m-1],overwrite_t=1)
  z,ier = bispev(tx,ty,c,kx,ky,x,y)
  z,ier = parder(tx,ty,c,kx,ky,nux,nuy,x,y)
  newc,ier = pardtc(tx,ty,c,kx,ky,nux,nuy)
  z,ier = bispeu(tx,ty,c,kx,ky,x,y)
  z,ier = pardeu(tx,ty,c,kx,ky,nux,nuy,x,y)
  nx,tx,ny,ty,c,fp,wrk1,ier = surfit_smth(x,y,z,w=1.0,xb=dmin(x,m),xe=dmax(x,m),yb=dmin(y,m),ye=dmax(y,m),kx=3,ky=3,s=m,nxest=imax(kx+1+sqrt(m/2),2*(kx+1)),nyest=imax(ky+1+sqrt(m/2),2*(ky+1)),eps=1e-16,lwrk2=calc_surfit_lwrk2(m,kx,ky,nxest,nyest))
  tx,ty,c,fp,ier = surfit_lsq(x,y,z,nx,tx,ny,ty,w=1.0,xb=calc_b(x,m,tx,nx),xe=calc_e(x,m,tx,nx),yb=calc_b(y,m,ty,ny),ye=calc_e(y,m,ty,ny),kx=3,ky=3,eps=1e-16,lwrk2=calc_surfit_lwrk2(m,kx,ky,nxest,nyest),overwrite_tx=1,overwrite_ty=1)
  nt,tt,np,tp,c,fp,ier = spherfit_smth(teta,phi,r,w=1.0,s=m,eps=1e-16)
  tt,tp,c,fp,ier = spherfit_lsq(teta,phi,r,tt,tp,w=1.0,eps=1e-16,overwrite_tt=1,overwrite_tp=1)
  nx,tx,ny,ty,c,fp,ier = regrid_smth(x,y,z,xb=dmin(x,mx),xe=dmax(x,mx),yb=dmin(y,my),ye=dmax(y,my),kx=3,ky=3,s=0.0)
  nu,tu,nv,tv,c,fp,ier = regrid_smth_spher(iopt,ider,u,v,r,r0=,r1=,s=0.0)
  dblint = dblint(tx,ty,c,kx,ky,xb,xe,yb,ye)
COMMON blocks:
  /types/ intvar
.
"""
# no imports

# Variables with simple values

__version__ = b'$Revision: $'

# functions

def bispeu(tx, ty, c, kx, ky, x, y): # real signature unknown; restored from __doc__
    """
    z,ier = bispeu(tx,ty,c,kx,ky,x,y)
    
    Wrapper for ``bispeu``.
    
    Parameters
    ----------
    tx : input rank-1 array('d') with bounds (nx)
    ty : input rank-1 array('d') with bounds (ny)
    c : input rank-1 array('d') with bounds ((nx-kx-1)*(ny-ky-1))
    kx : input int
    ky : input int
    x : input rank-1 array('d') with bounds (m)
    y : input rank-1 array('d') with bounds (m)
    
    Returns
    -------
    z : rank-1 array('d') with bounds (m)
    ier : int
    """
    pass

def bispev(tx, ty, c, kx, ky, x, y): # real signature unknown; restored from __doc__
    """
    z,ier = bispev(tx,ty,c,kx,ky,x,y)
    
    Wrapper for ``bispev``.
    
    Parameters
    ----------
    tx : input rank-1 array('d') with bounds (nx)
    ty : input rank-1 array('d') with bounds (ny)
    c : input rank-1 array('d') with bounds ((nx-kx-1)*(ny-ky-1))
    kx : input int
    ky : input int
    x : input rank-1 array('d') with bounds (mx)
    y : input rank-1 array('d') with bounds (my)
    
    Returns
    -------
    z : rank-2 array('d') with bounds (mx,my)
    ier : int
    """
    pass

def curfit(iopt, x, y, w, t, wrk, iwrk, xb=None, xe=None, k=None, s=None): # real signature unknown; restored from __doc__
    """
    n,c,fp,ier = curfit(iopt,x,y,w,t,wrk,iwrk,[xb,xe,k,s])
    
    Wrapper for ``curfit``.
    
    Parameters
    ----------
    iopt : input int
    x : input rank-1 array('d') with bounds (m)
    y : input rank-1 array('d') with bounds (m)
    w : input rank-1 array('d') with bounds (m)
    t : in/output rank-1 array('d') with bounds (nest)
    wrk : in/output rank-1 array('d') with bounds (lwrk)
    iwrk : in/output rank-1 array('i') with bounds (nest)
    
    Other Parameters
    ----------------
    xb : input float, optional
        Default: x[0]
    xe : input float, optional
        Default: x[m-1]
    k : input int, optional
        Default: 3
    s : input float, optional
        Default: 0.0
    
    Returns
    -------
    n : int
    c : rank-1 array('d') with bounds (n)
    fp : float
    ier : int
    """
    pass

def dblint(tx, ty, c, kx, ky, xb, xe, yb, ye): # real signature unknown; restored from __doc__
    """
    dblint = dblint(tx,ty,c,kx,ky,xb,xe,yb,ye)
    
    Wrapper for ``dblint``.
    
    Parameters
    ----------
    tx : input rank-1 array('d') with bounds (nx)
    ty : input rank-1 array('d') with bounds (ny)
    c : input rank-1 array('d') with bounds ((nx-kx-1)*(ny-ky-1))
    kx : input int
    ky : input int
    xb : input float
    xe : input float
    yb : input float
    ye : input float
    
    Returns
    -------
    dblint : float
    """
    pass

def fpchec(x, t, k): # real signature unknown; restored from __doc__
    """
    ier = fpchec(x,t,k)
    
    Wrapper for ``fpchec``.
    
    Parameters
    ----------
    x : input rank-1 array('d') with bounds (m)
    t : input rank-1 array('d') with bounds (n)
    k : input int
    
    Returns
    -------
    ier : int
    """
    pass

def fpcurf0(x, y, k, w=None, xb=None, xe=None, s=None, nest=None): # real signature unknown; restored from __doc__
    """
    x,y,w,xb,xe,k,s,n,t,c,fp,fpint,nrdata,ier = fpcurf0(x,y,k,[w,xb,xe,s,nest])
    
    Wrapper for ``fpcurf0``.
    
    Parameters
    ----------
    x : input rank-1 array('d') with bounds (m)
    y : input rank-1 array('d') with bounds (m)
    k : input int
    
    Other Parameters
    ----------------
    w : input rank-1 array('d') with bounds (m), optional
        Default: 1.0
    xb : input float, optional
        Default: x[0]
    xe : input float, optional
        Default: x[m-1]
    s : input float, optional
        Default: m
    nest : input int, optional
        Default: (s==0.0?m+k+1:MAX(m/2,2*k1))
    
    Returns
    -------
    x : rank-1 array('d') with bounds (m)
    y : rank-1 array('d') with bounds (m)
    w : rank-1 array('d') with bounds (m)
    xb : float
    xe : float
    k : int
    s : float
    n : int
    t : rank-1 array('d') with bounds (nest)
    c : rank-1 array('d') with bounds (nest)
    fp : float
    fpint : rank-1 array('d') with bounds (nest)
    nrdata : rank-1 array('i') with bounds (nest)
    ier : int
    """
    pass

def fpcurf1(x, y, w, xb, xe, k, s, n, t, c, fp, fpint, nrdata, ier, overwrite_x=None, overwrite_y=None, overwrite_w=None, overwrite_t=None, overwrite_c=None, overwrite_fpint=None, overwrite_nrdata=None): # real signature unknown; restored from __doc__
    """
    x,y,w,xb,xe,k,s,n,t,c,fp,fpint,nrdata,ier = fpcurf1(x,y,w,xb,xe,k,s,n,t,c,fp,fpint,nrdata,ier,[overwrite_x,overwrite_y,overwrite_w,overwrite_t,overwrite_c,overwrite_fpint,overwrite_nrdata])
    
    Wrapper for ``fpcurf1``.
    
    Parameters
    ----------
    x : input rank-1 array('d') with bounds (m)
    y : input rank-1 array('d') with bounds (m)
    w : input rank-1 array('d') with bounds (m)
    xb : input float
    xe : input float
    k : input int
    s : input float
    n : input int
    t : input rank-1 array('d') with bounds (nest)
    c : input rank-1 array('d') with bounds (nest)
    fp : input float
    fpint : input rank-1 array('d') with bounds (nest)
    nrdata : input rank-1 array('i') with bounds (nest)
    ier : input int
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 1
    overwrite_y : input int, optional
        Default: 1
    overwrite_w : input int, optional
        Default: 1
    overwrite_t : input int, optional
        Default: 1
    overwrite_c : input int, optional
        Default: 1
    overwrite_fpint : input int, optional
        Default: 1
    overwrite_nrdata : input int, optional
        Default: 1
    
    Returns
    -------
    x : rank-1 array('d') with bounds (m)
    y : rank-1 array('d') with bounds (m)
    w : rank-1 array('d') with bounds (m)
    xb : float
    xe : float
    k : int
    s : float
    n : int
    t : rank-1 array('d') with bounds (nest)
    c : rank-1 array('d') with bounds (nest)
    fp : float
    fpint : rank-1 array('d') with bounds (nest)
    nrdata : rank-1 array('i') with bounds (nest)
    ier : int
    """
    pass

def fpcurfm1(x, y, k, t, w=None, xb=None, xe=None, overwrite_t=None): # real signature unknown; restored from __doc__
    """
    x,y,w,xb,xe,k,s,n,t,c,fp,fpint,nrdata,ier = fpcurfm1(x,y,k,t,[w,xb,xe,overwrite_t])
    
    Wrapper for ``fpcurfm1``.
    
    Parameters
    ----------
    x : input rank-1 array('d') with bounds (m)
    y : input rank-1 array('d') with bounds (m)
    k : input int
    t : input rank-1 array('d') with bounds (n)
    
    Other Parameters
    ----------------
    w : input rank-1 array('d') with bounds (m), optional
        Default: 1.0
    xb : input float, optional
        Default: x[0]
    xe : input float, optional
        Default: x[m-1]
    overwrite_t : input int, optional
        Default: 1
    
    Returns
    -------
    x : rank-1 array('d') with bounds (m)
    y : rank-1 array('d') with bounds (m)
    w : rank-1 array('d') with bounds (m)
    xb : float
    xe : float
    k : int
    s : float
    n : int
    t : rank-1 array('d') with bounds (n)
    c : rank-1 array('d') with bounds (nest)
    fp : float
    fpint : rank-1 array('d') with bounds (nest)
    nrdata : rank-1 array('i') with bounds (nest)
    ier : int
    """
    pass

def parcur(iopt, ipar, idim, u, x, w, ub, ue, t, wrk, iwrk, k=None, s=None): # real signature unknown; restored from __doc__
    """
    n,c,fp,ier = parcur(iopt,ipar,idim,u,x,w,ub,ue,t,wrk,iwrk,[k,s])
    
    Wrapper for ``parcur``.
    
    Parameters
    ----------
    iopt : input int
    ipar : input int
    idim : input int
    u : in/output rank-1 array('d') with bounds (m)
    x : input rank-1 array('d') with bounds (mx)
    w : input rank-1 array('d') with bounds (m)
    ub : input float
    ue : input float
    t : in/output rank-1 array('d') with bounds (nest)
    wrk : in/output rank-1 array('d') with bounds (lwrk)
    iwrk : in/output rank-1 array('i') with bounds (nest)
    
    Other Parameters
    ----------------
    k : input int, optional
        Default: 3.0
    s : input float, optional
        Default: 0.0
    
    Returns
    -------
    n : int
    c : rank-1 array('d') with bounds (nc)
    fp : float
    ier : int
    """
    pass

def parder(tx, ty, c, kx, ky, nux, nuy, x, y): # real signature unknown; restored from __doc__
    """
    z,ier = parder(tx,ty,c,kx,ky,nux,nuy,x,y)
    
    Wrapper for ``parder``.
    
    Parameters
    ----------
    tx : input rank-1 array('d') with bounds (nx)
    ty : input rank-1 array('d') with bounds (ny)
    c : input rank-1 array('d') with bounds ((nx-kx-1)*(ny-ky-1))
    kx : input int
    ky : input int
    nux : input int
    nuy : input int
    x : input rank-1 array('d') with bounds (mx)
    y : input rank-1 array('d') with bounds (my)
    
    Returns
    -------
    z : rank-2 array('d') with bounds (mx,my)
    ier : int
    """
    pass

def pardeu(tx, ty, c, kx, ky, nux, nuy, x, y): # real signature unknown; restored from __doc__
    """
    z,ier = pardeu(tx,ty,c,kx,ky,nux,nuy,x,y)
    
    Wrapper for ``pardeu``.
    
    Parameters
    ----------
    tx : input rank-1 array('d') with bounds (nx)
    ty : input rank-1 array('d') with bounds (ny)
    c : input rank-1 array('d') with bounds ((nx-kx-1)*(ny-ky-1))
    kx : input int
    ky : input int
    nux : input int
    nuy : input int
    x : input rank-1 array('d') with bounds (m)
    y : input rank-1 array('d') with bounds (m)
    
    Returns
    -------
    z : rank-1 array('d') with bounds (m)
    ier : int
    """
    pass

def pardtc(tx, ty, c, kx, ky, nux, nuy): # real signature unknown; restored from __doc__
    """
    newc,ier = pardtc(tx,ty,c,kx,ky,nux,nuy)
    
    Wrapper for ``pardtc``.
    
    Parameters
    ----------
    tx : input rank-1 array('d') with bounds (nx)
    ty : input rank-1 array('d') with bounds (ny)
    c : input rank-1 array('d') with bounds ((nx-kx-1)*(ny-ky-1))
    kx : input int
    ky : input int
    nux : input int
    nuy : input int
    
    Returns
    -------
    newc : rank-1 array('d') with bounds ((nx-kx-1)*(ny-ky-1))
    ier : int
    """
    pass

def percur(iopt, x, y, w, t, wrk, iwrk, k=None, s=None): # real signature unknown; restored from __doc__
    """
    n,c,fp,ier = percur(iopt,x,y,w,t,wrk,iwrk,[k,s])
    
    Wrapper for ``percur``.
    
    Parameters
    ----------
    iopt : input int
    x : input rank-1 array('d') with bounds (m)
    y : input rank-1 array('d') with bounds (m)
    w : input rank-1 array('d') with bounds (m)
    t : in/output rank-1 array('d') with bounds (nest)
    wrk : in/output rank-1 array('d') with bounds (lwrk)
    iwrk : in/output rank-1 array('i') with bounds (nest)
    
    Other Parameters
    ----------------
    k : input int, optional
        Default: 3
    s : input float, optional
        Default: 0.0
    
    Returns
    -------
    n : int
    c : rank-1 array('d') with bounds (n)
    fp : float
    ier : int
    """
    pass

def regrid_smth(x, y, z, xb=None, xe=None, yb=None, ye=None, kx=None, ky=None, s=None): # real signature unknown; restored from __doc__
    """
    nx,tx,ny,ty,c,fp,ier = regrid_smth(x,y,z,[xb,xe,yb,ye,kx,ky,s])
    
    Wrapper for ``regrid_smth``.
    
    Parameters
    ----------
    x : input rank-1 array('d') with bounds (mx)
    y : input rank-1 array('d') with bounds (my)
    z : input rank-1 array('d') with bounds (mx*my)
    
    Other Parameters
    ----------------
    xb : input float, optional
        Default: dmin(x,mx)
    xe : input float, optional
        Default: dmax(x,mx)
    yb : input float, optional
        Default: dmin(y,my)
    ye : input float, optional
        Default: dmax(y,my)
    kx : input int, optional
        Default: 3
    ky : input int, optional
        Default: 3
    s : input float, optional
        Default: 0.0
    
    Returns
    -------
    nx : int
    tx : rank-1 array('d') with bounds (nxest)
    ny : int
    ty : rank-1 array('d') with bounds (nyest)
    c : rank-1 array('d') with bounds ((nxest-kx-1)*(nyest-ky-1))
    fp : float
    ier : int
    """
    pass

def regrid_smth_spher(iopt, ider, u, v, r, r0=None, r1=None, s=None): # real signature unknown; restored from __doc__
    """
    nu,tu,nv,tv,c,fp,ier = regrid_smth_spher(iopt,ider,u,v,r,[r0,r1,s])
    
    Wrapper for ``regrid_smth_spher``.
    
    Parameters
    ----------
    iopt : input rank-1 array('i') with bounds (3)
    ider : input rank-1 array('i') with bounds (4)
    u : input rank-1 array('d') with bounds (mu)
    v : input rank-1 array('d') with bounds (mv)
    r : input rank-1 array('d') with bounds (mu*mv)
    
    Other Parameters
    ----------------
    r0 : input float
    r1 : input float
    s : input float, optional
        Default: 0.0
    
    Returns
    -------
    nu : int
    tu : rank-1 array('d') with bounds (nuest)
    nv : int
    tv : rank-1 array('d') with bounds (nvest)
    c : rank-1 array('d') with bounds ((nuest-4)*(nvest-4))
    fp : float
    ier : int
    """
    pass

def spalde(t, c, k1, x): # real signature unknown; restored from __doc__
    """
    d,ier = spalde(t,c,k1,x)
    
    Wrapper for ``spalde``.
    
    Parameters
    ----------
    t : input rank-1 array('d') with bounds (n)
    c : input rank-1 array('d') with bounds (n)
    k1 : input int
    x : input float
    
    Returns
    -------
    d : rank-1 array('d') with bounds (k1)
    ier : int
    """
    pass

def spherfit_lsq(teta, phi, r, tt, tp, w=None, eps=None, overwrite_tt=None, overwrite_tp=None): # real signature unknown; restored from __doc__
    """
    tt,tp,c,fp,ier = spherfit_lsq(teta,phi,r,tt,tp,[w,eps,overwrite_tt,overwrite_tp])
    
    Wrapper for ``spherfit_lsq``.
    
    Parameters
    ----------
    teta : input rank-1 array('d') with bounds (m)
    phi : input rank-1 array('d') with bounds (m)
    r : input rank-1 array('d') with bounds (m)
    tt : input rank-1 array('d') with bounds (ntest)
    tp : input rank-1 array('d') with bounds (npest)
    
    Other Parameters
    ----------------
    w : input rank-1 array('d') with bounds (m), optional
        Default: 1.0
    eps : input float, optional
        Default: 1e-16
    overwrite_tt : input int, optional
        Default: 1
    overwrite_tp : input int, optional
        Default: 1
    
    Returns
    -------
    tt : rank-1 array('d') with bounds (ntest)
    tp : rank-1 array('d') with bounds (npest)
    c : rank-1 array('d') with bounds ((nt-4)*(np-4))
    fp : float
    ier : int
    """
    pass

def spherfit_smth(teta, phi, r, w=None, s=None, eps=None): # real signature unknown; restored from __doc__
    """
    nt,tt,np,tp,c,fp,ier = spherfit_smth(teta,phi,r,[w,s,eps])
    
    Wrapper for ``spherfit_smth``.
    
    Parameters
    ----------
    teta : input rank-1 array('d') with bounds (m)
    phi : input rank-1 array('d') with bounds (m)
    r : input rank-1 array('d') with bounds (m)
    
    Other Parameters
    ----------------
    w : input rank-1 array('d') with bounds (m), optional
        Default: 1.0
    s : input float, optional
        Default: m
    eps : input float, optional
        Default: 1e-16
    
    Returns
    -------
    nt : int
    tt : rank-1 array('d') with bounds (ntest)
    np : int
    tp : rank-1 array('d') with bounds (npest)
    c : rank-1 array('d') with bounds ((ntest-4)*(npest-4))
    fp : float
    ier : int
    """
    pass

def splder(t, c, k, x, nu=None, e=None): # real signature unknown; restored from __doc__
    """
    y = splder(t,c,k,x,[nu,e])
    
    Wrapper for ``splder``.
    
    Parameters
    ----------
    t : input rank-1 array('d') with bounds (n)
    c : input rank-1 array('d') with bounds (n)
    k : input int
    x : input rank-1 array('d') with bounds (m)
    
    Other Parameters
    ----------------
    nu : input int, optional
        Default: 1
    e : input int, optional
        Default: 0
    
    Returns
    -------
    y : rank-1 array('d') with bounds (m)
    """
    pass

def splev(t, c, k, x, e=None): # real signature unknown; restored from __doc__
    """
    y = splev(t,c,k,x,[e])
    
    Wrapper for ``splev``.
    
    Parameters
    ----------
    t : input rank-1 array('d') with bounds (n)
    c : input rank-1 array('d') with bounds (n)
    k : input int
    x : input rank-1 array('d') with bounds (m)
    
    Other Parameters
    ----------------
    e : input int, optional
        Default: 0
    
    Returns
    -------
    y : rank-1 array('d') with bounds (m)
    """
    pass

def splint(t, c, k, a, b): # real signature unknown; restored from __doc__
    """
    splint,wrk = splint(t,c,k,a,b)
    
    Wrapper for ``splint``.
    
    Parameters
    ----------
    t : input rank-1 array('d') with bounds (n)
    c : input rank-1 array('d') with bounds (nc)
    k : input int
    a : input float
    b : input float
    
    Returns
    -------
    splint : float
    wrk : rank-1 array('d') with bounds (n)
    """
    pass

def sproot(t, c, mest=None): # real signature unknown; restored from __doc__
    """
    zero,m,ier = sproot(t,c,[mest])
    
    Wrapper for ``sproot``.
    
    Parameters
    ----------
    t : input rank-1 array('d') with bounds (n)
    c : input rank-1 array('d') with bounds (nc)
    
    Other Parameters
    ----------------
    mest : input int, optional
        Default: 3*(n-7)
    
    Returns
    -------
    zero : rank-1 array('d') with bounds (mest)
    m : int
    ier : int
    """
    pass

def surfit_lsq(x, y, z, nx, tx, ny, ty, w=None, xb=None, xe=None, yb=None, ye=None, kx=None, ky=None, eps=None, lwrk2=None, overwrite_tx=None, overwrite_ty=None): # real signature unknown; restored from __doc__
    """
    tx,ty,c,fp,ier = surfit_lsq(x,y,z,nx,tx,ny,ty,[w,xb,xe,yb,ye,kx,ky,eps,lwrk2,overwrite_tx,overwrite_ty])
    
    Wrapper for ``surfit_lsq``.
    
    Parameters
    ----------
    x : input rank-1 array('d') with bounds (m)
    y : input rank-1 array('d') with bounds (m)
    z : input rank-1 array('d') with bounds (m)
    nx : input int
    tx : input rank-1 array('d') with bounds (nmax)
    ny : input int
    ty : input rank-1 array('d') with bounds (nmax)
    
    Other Parameters
    ----------------
    w : input rank-1 array('d') with bounds (m), optional
        Default: 1.0
    xb : input float, optional
        Default: calc_b(x,m,tx,nx)
    xe : input float, optional
        Default: calc_e(x,m,tx,nx)
    yb : input float, optional
        Default: calc_b(y,m,ty,ny)
    ye : input float, optional
        Default: calc_e(y,m,ty,ny)
    kx : input int, optional
        Default: 3
    ky : input int, optional
        Default: 3
    eps : input float, optional
        Default: 1e-16
    overwrite_tx : input int, optional
        Default: 1
    overwrite_ty : input int, optional
        Default: 1
    lwrk2 : input int, optional
        Default: calc_surfit_lwrk2(m,kx,ky,nxest,nyest)
    
    Returns
    -------
    tx : rank-1 array('d') with bounds (nmax)
    ty : rank-1 array('d') with bounds (nmax)
    c : rank-1 array('d') with bounds ((nx-kx-1)*(ny-ky-1))
    fp : float
    ier : int
    """
    pass

def surfit_smth(x, y, z, w=None, xb=None, xe=None, yb=None, ye=None, kx=None, ky=None, s=None, nxest=None, nyest=None, eps=None, lwrk2=None): # real signature unknown; restored from __doc__
    """
    nx,tx,ny,ty,c,fp,wrk1,ier = surfit_smth(x,y,z,[w,xb,xe,yb,ye,kx,ky,s,nxest,nyest,eps,lwrk2])
    
    Wrapper for ``surfit_smth``.
    
    Parameters
    ----------
    x : input rank-1 array('d') with bounds (m)
    y : input rank-1 array('d') with bounds (m)
    z : input rank-1 array('d') with bounds (m)
    
    Other Parameters
    ----------------
    w : input rank-1 array('d') with bounds (m), optional
        Default: 1.0
    xb : input float, optional
        Default: dmin(x,m)
    xe : input float, optional
        Default: dmax(x,m)
    yb : input float, optional
        Default: dmin(y,m)
    ye : input float, optional
        Default: dmax(y,m)
    kx : input int, optional
        Default: 3
    ky : input int, optional
        Default: 3
    s : input float, optional
        Default: m
    nxest : input int, optional
        Default: imax(kx+1+sqrt(m/2),2*(kx+1))
    nyest : input int, optional
        Default: imax(ky+1+sqrt(m/2),2*(ky+1))
    eps : input float, optional
        Default: 1e-16
    lwrk2 : input int, optional
        Default: calc_surfit_lwrk2(m,kx,ky,nxest,nyest)
    
    Returns
    -------
    nx : int
    tx : rank-1 array('d') with bounds (nmax)
    ny : int
    ty : rank-1 array('d') with bounds (nmax)
    c : rank-1 array('d') with bounds ((nxest-kx-1)*(nyest-ky-1))
    fp : float
    wrk1 : rank-1 array('d') with bounds (lwrk1)
    ier : int
    """
    pass

def types(*args, **kwargs): # real signature unknown
    """ 'i'-scalar """
    pass

# classes

class _dfitpack_error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff93063fa0>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.interpolate.dfitpack', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff93063fa0>, origin='/.venv/lib/python3.8/site-packages/scipy/interpolate/dfitpack.cpython-38-aarch64-linux-gnu.so')"

