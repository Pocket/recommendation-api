# encoding: utf-8
# module scipy.linalg._fblas
# from /.venv/lib/python3.8/site-packages/scipy/linalg/_fblas.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
"""
This module '_fblas' is auto-generated with f2py (version:2).
Functions:
  c,s = srotg(a,b)
  c,s = drotg(a,b)
  c,s = crotg(a,b)
  c,s = zrotg(a,b)
  param = srotmg(d1,d2,x1,y1)
  param = drotmg(d1,d2,x1,y1)
  x,y = srot(x,y,c,s,n=(len(x)-1-offx)/abs(incx)+1,offx=0,incx=1,offy=0,incy=1,overwrite_x=0,overwrite_y=0)
  x,y = drot(x,y,c,s,n=(len(x)-1-offx)/abs(incx)+1,offx=0,incx=1,offy=0,incy=1,overwrite_x=0,overwrite_y=0)
  x,y = csrot(x,y,c,s,n=(len(x)-1-offx)/abs(incx)+1,offx=0,incx=1,offy=0,incy=1,overwrite_x=0,overwrite_y=0)
  x,y = zdrot(x,y,c,s,n=(len(x)-1-offx)/abs(incx)+1,offx=0,incx=1,offy=0,incy=1,overwrite_x=0,overwrite_y=0)
  x,y = srotm(x,y,param,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1,overwrite_x=0,overwrite_y=0)
  x,y = drotm(x,y,param,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1,overwrite_x=0,overwrite_y=0)
  x,y = sswap(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)
  x,y = dswap(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)
  x,y = cswap(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)
  x,y = zswap(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)
  x = sscal(a,x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)
  x = dscal(a,x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)
  x = cscal(a,x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)
  x = zscal(a,x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)
  x = csscal(a,x,n=(len(x)-offx)/abs(incx),offx=0,incx=1,overwrite_x=0)
  x = zdscal(a,x,n=(len(x)-offx)/abs(incx),offx=0,incx=1,overwrite_x=0)
  y = scopy(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)
  y = dcopy(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)
  y = ccopy(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)
  y = zcopy(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)
  z = saxpy(x,y,n=(len(x)-offx)/abs(incx),a=1.0,offx=0,incx=1,offy=0,incy=1)
  z = daxpy(x,y,n=(len(x)-offx)/abs(incx),a=1.0,offx=0,incx=1,offy=0,incy=1)
  z = caxpy(x,y,n=(len(x)-offx)/abs(incx),a=(1.0, 0.0),offx=0,incx=1,offy=0,incy=1)
  z = zaxpy(x,y,n=(len(x)-offx)/abs(incx),a=(1.0, 0.0),offx=0,incx=1,offy=0,incy=1)
  xy = sdot(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)
  xy = ddot(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)
  xy = cdotu(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)
  xy = zdotu(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)
  xy = cdotc(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)
  xy = zdotc(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)
  n2 = snrm2(x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)
  n2 = scnrm2(x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)
  n2 = dnrm2(x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)
  n2 = dznrm2(x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)
  s = sasum(x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)
  s = scasum(x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)
  s = dasum(x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)
  s = dzasum(x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)
  k = isamax(x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)
  k = idamax(x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)
  k = icamax(x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)
  k = izamax(x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)
  y = sgemv(alpha,a,x,beta=0.0,y=,offx=0,incx=1,offy=0,incy=1,trans=0,overwrite_y=0)
  y = dgemv(alpha,a,x,beta=0.0,y=,offx=0,incx=1,offy=0,incy=1,trans=0,overwrite_y=0)
  y = cgemv(alpha,a,x,beta=(0.0, 0.0),y=,offx=0,incx=1,offy=0,incy=1,trans=0,overwrite_y=0)
  y = zgemv(alpha,a,x,beta=(0.0, 0.0),y=,offx=0,incx=1,offy=0,incy=1,trans=0,overwrite_y=0)
  yout = sgbmv(m,n,kl,ku,alpha,a,x,incx=1,offx=0,beta=0.0,y=,incy=1,offy=0,trans=0,overwrite_y=0)
  yout = dgbmv(m,n,kl,ku,alpha,a,x,incx=1,offx=0,beta=0.0,y=,incy=1,offy=0,trans=0,overwrite_y=0)
  yout = cgbmv(m,n,kl,ku,alpha,a,x,incx=1,offx=0,beta=(0.0, 0.0),y=,incy=1,offy=0,trans=0,overwrite_y=0)
  yout = zgbmv(m,n,kl,ku,alpha,a,x,incx=1,offx=0,beta=(0.0, 0.0),y=,incy=1,offy=0,trans=0,overwrite_y=0)
  yout = ssbmv(k,alpha,a,x,incx=1,offx=0,beta=0.0,y=,incy=1,offy=0,lower=0,overwrite_y=0)
  yout = dsbmv(k,alpha,a,x,incx=1,offx=0,beta=0.0,y=,incy=1,offy=0,lower=0,overwrite_y=0)
  yout = chbmv(k,alpha,a,x,incx=1,offx=0,beta=(0.0, 0.0),y=,incy=1,offy=0,lower=0,overwrite_y=0)
  yout = zhbmv(k,alpha,a,x,incx=1,offx=0,beta=(0.0, 0.0),y=,incy=1,offy=0,lower=0,overwrite_y=0)
  yout = sspmv(n,alpha,ap,x,incx=1,offx=0,beta=0.0,y=,incy=1,offy=0,lower=0,overwrite_y=0)
  yout = dspmv(n,alpha,ap,x,incx=1,offx=0,beta=0.0,y=,incy=1,offy=0,lower=0,overwrite_y=0)
  yout = cspmv(n,alpha,ap,x,incx=1,offx=0,beta=(0.0, 0.0),y=,incy=1,offy=0,lower=0,overwrite_y=0)
  yout = zspmv(n,alpha,ap,x,incx=1,offx=0,beta=(0.0, 0.0),y=,incy=1,offy=0,lower=0,overwrite_y=0)
  yout = chpmv(n,alpha,ap,x,incx=1,offx=0,beta=(0.0, 0.0),y=,incy=1,offy=0,lower=0,overwrite_y=0)
  yout = zhpmv(n,alpha,ap,x,incx=1,offx=0,beta=(0.0, 0.0),y=,incy=1,offy=0,lower=0,overwrite_y=0)
  y = ssymv(alpha,a,x,beta=0.0,y=,offx=0,incx=1,offy=0,incy=1,lower=0,overwrite_y=0)
  y = dsymv(alpha,a,x,beta=0.0,y=,offx=0,incx=1,offy=0,incy=1,lower=0,overwrite_y=0)
  y = chemv(alpha,a,x,beta=(0.0, 0.0),y=,offx=0,incx=1,offy=0,incy=1,lower=0,overwrite_y=0)
  y = zhemv(alpha,a,x,beta=(0.0, 0.0),y=,offx=0,incx=1,offy=0,incy=1,lower=0,overwrite_y=0)
  a = sger(alpha,x,y,incx=1,incy=1,a=0.0,overwrite_x=1,overwrite_y=1,overwrite_a=0)
  a = dger(alpha,x,y,incx=1,incy=1,a=0.0,overwrite_x=1,overwrite_y=1,overwrite_a=0)
  a = cgeru(alpha,x,y,incx=1,incy=1,a=(0.0,0.0),overwrite_x=1,overwrite_y=1,overwrite_a=0)
  a = zgeru(alpha,x,y,incx=1,incy=1,a=(0.0,0.0),overwrite_x=1,overwrite_y=1,overwrite_a=0)
  a = cgerc(alpha,x,y,incx=1,incy=1,a=(0.0,0.0),overwrite_x=1,overwrite_y=1,overwrite_a=0)
  a = zgerc(alpha,x,y,incx=1,incy=1,a=(0.0,0.0),overwrite_x=1,overwrite_y=1,overwrite_a=0)
  a = ssyr(alpha,x,lower=0,incx=1,offx=0,n=(len(x)-1-offx)/abs(incx)+1,a=,overwrite_a=0)
  a = dsyr(alpha,x,lower=0,incx=1,offx=0,n=(len(x)-1-offx)/abs(incx)+1,a=,overwrite_a=0)
  a = csyr(alpha,x,lower=0,incx=1,offx=0,n=(len(x)-1-offx)/abs(incx)+1,a=,overwrite_a=0)
  a = zsyr(alpha,x,lower=0,incx=1,offx=0,n=(len(x)-1-offx)/abs(incx)+1,a=,overwrite_a=0)
  a = cher(alpha,x,lower=0,incx=1,offx=0,n=(len(x)-1-offx)/abs(incx)+1,a=,overwrite_a=0)
  a = zher(alpha,x,lower=0,incx=1,offx=0,n=(len(x)-1-offx)/abs(incx)+1,a=,overwrite_a=0)
  a = ssyr2(alpha,x,y,lower=0,incx=1,offx=0,incy=1,offy=0,n=((len(x)-1-offx)/abs(incx)+1 <=(len(y)-1-offy)/abs(incy)+1 ?(len(x)-1-offx)/abs(incx)+1 :(len(y)-1-offy)/abs(incy)+1),a=,overwrite_a=0)
  a = dsyr2(alpha,x,y,lower=0,incx=1,offx=0,incy=1,offy=0,n=((len(x)-1-offx)/abs(incx)+1 <=(len(y)-1-offy)/abs(incy)+1 ?(len(x)-1-offx)/abs(incx)+1 :(len(y)-1-offy)/abs(incy)+1),a=,overwrite_a=0)
  a = cher2(alpha,x,y,lower=0,incx=1,offx=0,incy=1,offy=0,n=((len(x)-1-offx)/abs(incx)+1 <=(len(y)-1-offy)/abs(incy)+1 ?(len(x)-1-offx)/abs(incx)+1 :(len(y)-1-offy)/abs(incy)+1),a=,overwrite_a=0)
  a = zher2(alpha,x,y,lower=0,incx=1,offx=0,incy=1,offy=0,n=((len(x)-1-offx)/abs(incx)+1 <=(len(y)-1-offy)/abs(incy)+1 ?(len(x)-1-offx)/abs(incx)+1 :(len(y)-1-offy)/abs(incy)+1),a=,overwrite_a=0)
  apu = sspr(n,alpha,x,ap,incx=1,offx=0,lower=0,overwrite_ap=0)
  apu = dspr(n,alpha,x,ap,incx=1,offx=0,lower=0,overwrite_ap=0)
  apu = cspr(n,alpha,x,ap,incx=1,offx=0,lower=0,overwrite_ap=0)
  apu = zspr(n,alpha,x,ap,incx=1,offx=0,lower=0,overwrite_ap=0)
  apu = chpr(n,alpha,x,ap,incx=1,offx=0,lower=0,overwrite_ap=0)
  apu = zhpr(n,alpha,x,ap,incx=1,offx=0,lower=0,overwrite_ap=0)
  apu = sspr2(n,alpha,x,y,ap,incx=1,offx=0,incy=1,offy=0,lower=0,overwrite_ap=0)
  apu = dspr2(n,alpha,x,y,ap,incx=1,offx=0,incy=1,offy=0,lower=0,overwrite_ap=0)
  apu = chpr2(n,alpha,x,y,ap,incx=1,offx=0,incy=1,offy=0,lower=0,overwrite_ap=0)
  apu = zhpr2(n,alpha,x,y,ap,incx=1,offx=0,incy=1,offy=0,lower=0,overwrite_ap=0)
  xout = stbsv(k,a,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)
  xout = dtbsv(k,a,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)
  xout = ctbsv(k,a,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)
  xout = ztbsv(k,a,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)
  xout = stpsv(n,ap,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)
  xout = dtpsv(n,ap,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)
  xout = ctpsv(n,ap,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)
  xout = ztpsv(n,ap,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)
  x = strmv(a,x,offx=0,incx=1,lower=0,trans=0,diag=0,overwrite_x=0)
  x = dtrmv(a,x,offx=0,incx=1,lower=0,trans=0,diag=0,overwrite_x=0)
  x = ctrmv(a,x,offx=0,incx=1,lower=0,trans=0,diag=0,overwrite_x=0)
  x = ztrmv(a,x,offx=0,incx=1,lower=0,trans=0,diag=0,overwrite_x=0)
  xout = strsv(a,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)
  xout = dtrsv(a,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)
  xout = ctrsv(a,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)
  xout = ztrsv(a,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)
  xout = stbmv(k,a,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)
  xout = dtbmv(k,a,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)
  xout = ctbmv(k,a,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)
  xout = ztbmv(k,a,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)
  xout = stpmv(n,ap,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)
  xout = dtpmv(n,ap,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)
  xout = ctpmv(n,ap,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)
  xout = ztpmv(n,ap,x,incx=1,offx=0,lower=0,trans=0,diag=0,overwrite_x=0)
  c = sgemm(alpha,a,b,beta=0.0,c=,trans_a=0,trans_b=0,overwrite_c=0)
  c = dgemm(alpha,a,b,beta=0.0,c=,trans_a=0,trans_b=0,overwrite_c=0)
  c = cgemm(alpha,a,b,beta=(0.0, 0.0),c=,trans_a=0,trans_b=0,overwrite_c=0)
  c = zgemm(alpha,a,b,beta=(0.0, 0.0),c=,trans_a=0,trans_b=0,overwrite_c=0)
  c = ssymm(alpha,a,b,beta=0.0,c=,side=0,lower=0,overwrite_c=0)
  c = dsymm(alpha,a,b,beta=0.0,c=,side=0,lower=0,overwrite_c=0)
  c = csymm(alpha,a,b,beta=(0.0, 0.0),c=,side=0,lower=0,overwrite_c=0)
  c = zsymm(alpha,a,b,beta=(0.0, 0.0),c=,side=0,lower=0,overwrite_c=0)
  c = chemm(alpha,a,b,beta=(0.0, 0.0),c=,side=0,lower=0,overwrite_c=0)
  c = zhemm(alpha,a,b,beta=(0.0, 0.0),c=,side=0,lower=0,overwrite_c=0)
  c = ssyrk(alpha,a,beta=0.0,c=,trans=0,lower=0,overwrite_c=0)
  c = dsyrk(alpha,a,beta=0.0,c=,trans=0,lower=0,overwrite_c=0)
  c = csyrk(alpha,a,beta=(0.0, 0.0),c=,trans=0,lower=0,overwrite_c=0)
  c = zsyrk(alpha,a,beta=(0.0, 0.0),c=,trans=0,lower=0,overwrite_c=0)
  c = cherk(alpha,a,beta=(0.0, 0.0),c=,trans=0,lower=0,overwrite_c=0)
  c = zherk(alpha,a,beta=(0.0, 0.0),c=,trans=0,lower=0,overwrite_c=0)
  c = ssyr2k(alpha,a,b,beta=0.0,c=,trans=0,lower=0,overwrite_c=0)
  c = dsyr2k(alpha,a,b,beta=0.0,c=,trans=0,lower=0,overwrite_c=0)
  c = csyr2k(alpha,a,b,beta=(0.0, 0.0),c=,trans=0,lower=0,overwrite_c=0)
  c = zsyr2k(alpha,a,b,beta=(0.0, 0.0),c=,trans=0,lower=0,overwrite_c=0)
  c = cher2k(alpha,a,b,beta=(0.0, 0.0),c=,trans=0,lower=0,overwrite_c=0)
  c = zher2k(alpha,a,b,beta=(0.0, 0.0),c=,trans=0,lower=0,overwrite_c=0)
  b = strmm(alpha,a,b,side=0,lower=0,trans_a=0,diag=0,overwrite_b=0)
  b = dtrmm(alpha,a,b,side=0,lower=0,trans_a=0,diag=0,overwrite_b=0)
  b = ctrmm(alpha,a,b,side=0,lower=0,trans_a=0,diag=0,overwrite_b=0)
  b = ztrmm(alpha,a,b,side=0,lower=0,trans_a=0,diag=0,overwrite_b=0)
  x = strsm(alpha,a,b,side=0,lower=0,trans_a=0,diag=0,overwrite_b=0)
  x = dtrsm(alpha,a,b,side=0,lower=0,trans_a=0,diag=0,overwrite_b=0)
  x = ctrsm(alpha,a,b,side=0,lower=0,trans_a=0,diag=0,overwrite_b=0)
  x = ztrsm(alpha,a,b,side=0,lower=0,trans_a=0,diag=0,overwrite_b=0)
.
"""
# no imports

# Variables with simple values

__version__ = b'$Revision: $'

# functions

def caxpy(x, y, n=None, a=None, offx=None, incx=None, offy=None, incy=None): # real signature unknown; restored from __doc__
    """
    z = caxpy(x,y,[n,a,offx,incx,offy,incy])
    
    Wrapper for ``caxpy``.
    
    Parameters
    ----------
    x : input rank-1 array('F') with bounds (*)
    y : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    a : input complex, optional
        Default: (1.0, 0.0)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    z : rank-1 array('F') with bounds (*) and y storage
    """
    pass

def ccopy(x, y, n=None, offx=None, incx=None, offy=None, incy=None): # real signature unknown; restored from __doc__
    """
    y = ccopy(x,y,[n,offx,incx,offy,incy])
    
    Wrapper for ``ccopy``.
    
    Parameters
    ----------
    x : input rank-1 array('F') with bounds (*)
    y : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    y : rank-1 array('F') with bounds (*)
    """
    pass

def cdotc(x, y, n=None, offx=None, incx=None, offy=None, incy=None): # real signature unknown; restored from __doc__
    """
    xy = cdotc(x,y,[n,offx,incx,offy,incy])
    
    Wrapper for ``cdotc``.
    
    Parameters
    ----------
    x : input rank-1 array('F') with bounds (*)
    y : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    xy : complex
    """
    pass

def cdotu(x, y, n=None, offx=None, incx=None, offy=None, incy=None): # real signature unknown; restored from __doc__
    """
    xy = cdotu(x,y,[n,offx,incx,offy,incy])
    
    Wrapper for ``cdotu``.
    
    Parameters
    ----------
    x : input rank-1 array('F') with bounds (*)
    y : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    xy : complex
    """
    pass

def cgbmv(m, n, kl, ku, alpha, a, x, incx=None, offx=None, beta=None, y=None, incy=None, offy=None, trans=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    yout = cgbmv(m,n,kl,ku,alpha,a,x,[incx,offx,beta,y,incy,offy,trans,overwrite_y])
    
    Wrapper for ``cgbmv``.
    
    Parameters
    ----------
    m : input int
    n : input int
    kl : input int
    ku : input int
    alpha : input complex
    a : input rank-2 array('F') with bounds (lda,n)
    x : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    beta : input complex, optional
        Default: (0.0, 0.0)
    y : input rank-1 array('F') with bounds (ly)
    overwrite_y : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    
    Returns
    -------
    yout : rank-1 array('F') with bounds (ly) and y storage
    """
    pass

def cgemm(alpha, a, b, beta=None, c=None, trans_a=None, trans_b=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = cgemm(alpha,a,b,[beta,c,trans_a,trans_b,overwrite_c])
    
    Wrapper for ``cgemm``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('F') with bounds (lda,ka)
    b : input rank-2 array('F') with bounds (ldb,kb)
    
    Other Parameters
    ----------------
    beta : input complex, optional
        Default: (0.0, 0.0)
    c : input rank-2 array('F') with bounds (m,n)
    overwrite_c : input int, optional
        Default: 0
    trans_a : input int, optional
        Default: 0
    trans_b : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('F') with bounds (m,n)
    """
    pass

def cgemv(alpha, a, x, beta=None, y=None, offx=None, incx=None, offy=None, incy=None, trans=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    y = cgemv(alpha,a,x,[beta,y,offx,incx,offy,incy,trans,overwrite_y])
    
    Wrapper for ``cgemv``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('F') with bounds (m,n)
    x : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    beta : input complex, optional
        Default: (0.0, 0.0)
    y : input rank-1 array('F') with bounds (ly)
    overwrite_y : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    trans : input int, optional
        Default: 0
    
    Returns
    -------
    y : rank-1 array('F') with bounds (ly)
    """
    pass

def cgerc(alpha, x, y, incx=None, incy=None, a=None, overwrite_x=None, overwrite_y=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = cgerc(alpha,x,y,[incx,incy,a,overwrite_x,overwrite_y,overwrite_a])
    
    Wrapper for ``cgerc``.
    
    Parameters
    ----------
    alpha : input complex
    x : input rank-1 array('F') with bounds (m)
    y : input rank-1 array('F') with bounds (n)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 1
    incx : input int, optional
        Default: 1
    overwrite_y : input int, optional
        Default: 1
    incy : input int, optional
        Default: 1
    a : input rank-2 array('F') with bounds (m,n), optional
        Default: (0.0,0.0)
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('F') with bounds (m,n)
    """
    pass

def cgeru(alpha, x, y, incx=None, incy=None, a=None, overwrite_x=None, overwrite_y=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = cgeru(alpha,x,y,[incx,incy,a,overwrite_x,overwrite_y,overwrite_a])
    
    Wrapper for ``cgeru``.
    
    Parameters
    ----------
    alpha : input complex
    x : input rank-1 array('F') with bounds (m)
    y : input rank-1 array('F') with bounds (n)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 1
    incx : input int, optional
        Default: 1
    overwrite_y : input int, optional
        Default: 1
    incy : input int, optional
        Default: 1
    a : input rank-2 array('F') with bounds (m,n), optional
        Default: (0.0,0.0)
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('F') with bounds (m,n)
    """
    pass

def chbmv(k, alpha, a, x, incx=None, offx=None, beta=None, y=None, incy=None, offy=None, lower=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    yout = chbmv(k,alpha,a,x,[incx,offx,beta,y,incy,offy,lower,overwrite_y])
    
    Wrapper for ``chbmv``.
    
    Parameters
    ----------
    k : input int
    alpha : input complex
    a : input rank-2 array('F') with bounds (lda,n)
    x : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    beta : input complex, optional
        Default: (0.0, 0.0)
    y : input rank-1 array('F') with bounds (ly)
    overwrite_y : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    yout : rank-1 array('F') with bounds (ly) and y storage
    """
    pass

def chemm(alpha, a, b, beta=None, c=None, side=None, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = chemm(alpha,a,b,[beta,c,side,lower,overwrite_c])
    
    Wrapper for ``chemm``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('F') with bounds (lda,ka)
    b : input rank-2 array('F') with bounds (ldb,kb)
    
    Other Parameters
    ----------------
    beta : input complex, optional
        Default: (0.0, 0.0)
    c : input rank-2 array('F') with bounds (m,n)
    overwrite_c : input int, optional
        Default: 0
    side : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('F') with bounds (m,n)
    """
    pass

def chemv(alpha, a, x, beta=None, y=None, offx=None, incx=None, offy=None, incy=None, lower=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    y = chemv(alpha,a,x,[beta,y,offx,incx,offy,incy,lower,overwrite_y])
    
    Wrapper for ``chemv``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('F') with bounds (n,n)
    x : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    beta : input complex, optional
        Default: (0.0, 0.0)
    y : input rank-1 array('F') with bounds (ly)
    overwrite_y : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    y : rank-1 array('F') with bounds (ly)
    """
    pass

def cher(alpha, x, lower=None, incx=None, offx=None, n=None, a=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = cher(alpha,x,[lower,incx,offx,n,a,overwrite_a])
    
    Wrapper for ``cher``.
    
    Parameters
    ----------
    alpha : input complex
    x : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    n : input int, optional
        Default: (len(x)-1-offx)/abs(incx)+1
    a : input rank-2 array('F') with bounds (n,n)
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('F') with bounds (n,n)
    """
    pass

def cher2(alpha, x, y, lower=None, incx=None, offx=None, incy=None, offy=None, n=None, a=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = cher2(alpha,x,y,[lower,incx,offx,incy,offy,n,a,overwrite_a])
    
    Wrapper for ``cher2``.
    
    Parameters
    ----------
    alpha : input complex
    x : input rank-1 array('F') with bounds (*)
    y : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    n : input int, optional
        Default: ((len(x)-1-offx)/abs(incx)+1 <=(len(y)-1-offy)/abs(incy)+1 ?(len(x)-1-offx)/abs(incx)+1 :(len(y)-1-offy)/abs(incy)+1)
    a : input rank-2 array('F') with bounds (n,n)
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('F') with bounds (n,n)
    """
    pass

def cher2k(alpha, a, b, beta=None, c=None, trans=None, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = cher2k(alpha,a,b,[beta,c,trans,lower,overwrite_c])
    
    Wrapper for ``cher2k``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('F') with bounds (lda,ka)
    b : input rank-2 array('F') with bounds (ldb,kb)
    
    Other Parameters
    ----------------
    beta : input complex, optional
        Default: (0.0, 0.0)
    c : input rank-2 array('F') with bounds (n,n)
    overwrite_c : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('F') with bounds (n,n)
    """
    pass

def cherk(alpha, a, beta=None, c=None, trans=None, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = cherk(alpha,a,[beta,c,trans,lower,overwrite_c])
    
    Wrapper for ``cherk``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('F') with bounds (lda,ka)
    
    Other Parameters
    ----------------
    beta : input complex, optional
        Default: (0.0, 0.0)
    c : input rank-2 array('F') with bounds (n,n)
    overwrite_c : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('F') with bounds (n,n)
    """
    pass

def chpmv(n, alpha, ap, x, incx=None, offx=None, beta=None, y=None, incy=None, offy=None, lower=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    yout = chpmv(n,alpha,ap,x,[incx,offx,beta,y,incy,offy,lower,overwrite_y])
    
    Wrapper for ``chpmv``.
    
    Parameters
    ----------
    n : input int
    alpha : input complex
    ap : input rank-1 array('F') with bounds (*)
    x : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    beta : input complex, optional
        Default: (0.0, 0.0)
    y : input rank-1 array('F') with bounds (ly)
    overwrite_y : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    yout : rank-1 array('F') with bounds (ly) and y storage
    """
    pass

def chpr(n, alpha, x, ap, incx=None, offx=None, lower=None, overwrite_ap=None): # real signature unknown; restored from __doc__
    """
    apu = chpr(n,alpha,x,ap,[incx,offx,lower,overwrite_ap])
    
    Wrapper for ``chpr``.
    
    Parameters
    ----------
    n : input int
    alpha : input float
    x : input rank-1 array('F') with bounds (*)
    ap : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    overwrite_ap : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    apu : rank-1 array('F') with bounds (*) and ap storage
    """
    pass

def chpr2(n, alpha, x, y, ap, incx=None, offx=None, incy=None, offy=None, lower=None, overwrite_ap=None): # real signature unknown; restored from __doc__
    """
    apu = chpr2(n,alpha,x,y,ap,[incx,offx,incy,offy,lower,overwrite_ap])
    
    Wrapper for ``chpr2``.
    
    Parameters
    ----------
    n : input int
    alpha : input complex
    x : input rank-1 array('F') with bounds (*)
    y : input rank-1 array('F') with bounds (*)
    ap : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    overwrite_ap : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    apu : rank-1 array('F') with bounds (*) and ap storage
    """
    pass

def crotg(a, b): # real signature unknown; restored from __doc__
    """
    c,s = crotg(a,b)
    
    Wrapper for ``crotg``.
    
    Parameters
    ----------
    a : input complex
    b : input complex
    
    Returns
    -------
    c : complex
    s : complex
    """
    pass

def cscal(a, x, n=None, offx=None, incx=None): # real signature unknown; restored from __doc__
    """
    x = cscal(a,x,[n,offx,incx])
    
    Wrapper for ``cscal``.
    
    Parameters
    ----------
    a : input complex
    x : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    x : rank-1 array('F') with bounds (*)
    """
    pass

def cspmv(n, alpha, ap, x, incx=None, offx=None, beta=None, y=None, incy=None, offy=None, lower=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    yout = cspmv(n,alpha,ap,x,[incx,offx,beta,y,incy,offy,lower,overwrite_y])
    
    Wrapper for ``cspmv``.
    
    Parameters
    ----------
    n : input int
    alpha : input complex
    ap : input rank-1 array('F') with bounds (*)
    x : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    beta : input complex, optional
        Default: (0.0, 0.0)
    y : input rank-1 array('F') with bounds (ly)
    overwrite_y : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    yout : rank-1 array('F') with bounds (ly) and y storage
    """
    pass

def cspr(n, alpha, x, ap, incx=None, offx=None, lower=None, overwrite_ap=None): # real signature unknown; restored from __doc__
    """
    apu = cspr(n,alpha,x,ap,[incx,offx,lower,overwrite_ap])
    
    Wrapper for ``cspr``.
    
    Parameters
    ----------
    n : input int
    alpha : input complex
    x : input rank-1 array('F') with bounds (*)
    ap : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    overwrite_ap : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    apu : rank-1 array('F') with bounds (*) and ap storage
    """
    pass

def csrot(x, y, c, s, n=None, offx=None, incx=None, offy=None, incy=None, overwrite_x=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    x,y = csrot(x,y,c,s,[n,offx,incx,offy,incy,overwrite_x,overwrite_y])
    
    Wrapper for ``csrot``.
    
    Parameters
    ----------
    x : input rank-1 array('F') with bounds (*)
    y : input rank-1 array('F') with bounds (*)
    c : input float
    s : input float
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-1-offx)/abs(incx)+1
    overwrite_x : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    overwrite_y : input int, optional
        Default: 0
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    x : rank-1 array('F') with bounds (*)
    y : rank-1 array('F') with bounds (*)
    """
    pass

def csscal(a, x, n=None, offx=None, incx=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    x = csscal(a,x,[n,offx,incx,overwrite_x])
    
    Wrapper for ``csscal``.
    
    Parameters
    ----------
    a : input float
    x : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    overwrite_x : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    x : rank-1 array('F') with bounds (*)
    """
    pass

def cswap(x, y, n=None, offx=None, incx=None, offy=None, incy=None): # real signature unknown; restored from __doc__
    """
    x,y = cswap(x,y,[n,offx,incx,offy,incy])
    
    Wrapper for ``cswap``.
    
    Parameters
    ----------
    x : input rank-1 array('F') with bounds (*)
    y : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    x : rank-1 array('F') with bounds (*)
    y : rank-1 array('F') with bounds (*)
    """
    pass

def csymm(alpha, a, b, beta=None, c=None, side=None, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = csymm(alpha,a,b,[beta,c,side,lower,overwrite_c])
    
    Wrapper for ``csymm``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('F') with bounds (lda,ka)
    b : input rank-2 array('F') with bounds (ldb,kb)
    
    Other Parameters
    ----------------
    beta : input complex, optional
        Default: (0.0, 0.0)
    c : input rank-2 array('F') with bounds (m,n)
    overwrite_c : input int, optional
        Default: 0
    side : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('F') with bounds (m,n)
    """
    pass

def csyr(alpha, x, lower=None, incx=None, offx=None, n=None, a=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = csyr(alpha,x,[lower,incx,offx,n,a,overwrite_a])
    
    Wrapper for ``csyr``.
    
    Parameters
    ----------
    alpha : input complex
    x : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    n : input int, optional
        Default: (len(x)-1-offx)/abs(incx)+1
    a : input rank-2 array('F') with bounds (n,n)
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('F') with bounds (n,n)
    """
    pass

def csyr2k(alpha, a, b, beta=None, c=None, trans=None, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = csyr2k(alpha,a,b,[beta,c,trans,lower,overwrite_c])
    
    Wrapper for ``csyr2k``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('F') with bounds (lda,ka)
    b : input rank-2 array('F') with bounds (ldb,kb)
    
    Other Parameters
    ----------------
    beta : input complex, optional
        Default: (0.0, 0.0)
    c : input rank-2 array('F') with bounds (n,n)
    overwrite_c : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('F') with bounds (n,n)
    """
    pass

def csyrk(alpha, a, beta=None, c=None, trans=None, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = csyrk(alpha,a,[beta,c,trans,lower,overwrite_c])
    
    Wrapper for ``csyrk``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('F') with bounds (lda,ka)
    
    Other Parameters
    ----------------
    beta : input complex, optional
        Default: (0.0, 0.0)
    c : input rank-2 array('F') with bounds (n,n)
    overwrite_c : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('F') with bounds (n,n)
    """
    pass

def ctbmv(k, a, x, incx=None, offx=None, lower=None, trans=None, diag=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    xout = ctbmv(k,a,x,[incx,offx,lower,trans,diag,overwrite_x])
    
    Wrapper for ``ctbmv``.
    
    Parameters
    ----------
    k : input int
    a : input rank-2 array('F') with bounds (lda,n)
    x : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    diag : input int, optional
        Default: 0
    
    Returns
    -------
    xout : rank-1 array('F') with bounds (*) and x storage
    """
    pass

def ctbsv(k, a, x, incx=None, offx=None, lower=None, trans=None, diag=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    xout = ctbsv(k,a,x,[incx,offx,lower,trans,diag,overwrite_x])
    
    Wrapper for ``ctbsv``.
    
    Parameters
    ----------
    k : input int
    a : input rank-2 array('F') with bounds (lda,n)
    x : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    diag : input int, optional
        Default: 0
    
    Returns
    -------
    xout : rank-1 array('F') with bounds (*) and x storage
    """
    pass

def ctpmv(n, ap, x, incx=None, offx=None, lower=None, trans=None, diag=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    xout = ctpmv(n,ap,x,[incx,offx,lower,trans,diag,overwrite_x])
    
    Wrapper for ``ctpmv``.
    
    Parameters
    ----------
    n : input int
    ap : input rank-1 array('F') with bounds (*)
    x : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    diag : input int, optional
        Default: 0
    
    Returns
    -------
    xout : rank-1 array('F') with bounds (*) and x storage
    """
    pass

def ctpsv(n, ap, x, incx=None, offx=None, lower=None, trans=None, diag=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    xout = ctpsv(n,ap,x,[incx,offx,lower,trans,diag,overwrite_x])
    
    Wrapper for ``ctpsv``.
    
    Parameters
    ----------
    n : input int
    ap : input rank-1 array('F') with bounds (*)
    x : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    diag : input int, optional
        Default: 0
    
    Returns
    -------
    xout : rank-1 array('F') with bounds (*) and x storage
    """
    pass

def ctrmm(alpha, a, b, side=None, lower=None, trans_a=None, diag=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    b = ctrmm(alpha,a,b,[side,lower,trans_a,diag,overwrite_b])
    
    Wrapper for ``ctrmm``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('F') with bounds (lda,k)
    b : input rank-2 array('F') with bounds (ldb,n)
    
    Other Parameters
    ----------------
    overwrite_b : input int, optional
        Default: 0
    side : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    trans_a : input int, optional
        Default: 0
    diag : input int, optional
        Default: 0
    
    Returns
    -------
    b : rank-2 array('F') with bounds (ldb,n)
    """
    pass

def ctrmv(a, x, offx=None, incx=None, lower=None, trans=None, diag=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    x = ctrmv(a,x,[offx,incx,lower,trans,diag,overwrite_x])
    
    Wrapper for ``ctrmv``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    x : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    diag : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-1 array('F') with bounds (*)
    """
    pass

def ctrsm(alpha, a, b, side=None, lower=None, trans_a=None, diag=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x = ctrsm(alpha,a,b,[side,lower,trans_a,diag,overwrite_b])
    
    Wrapper for ``ctrsm``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('F') with bounds (lda,*)
    b : input rank-2 array('F') with bounds (ldb,n)
    
    Other Parameters
    ----------------
    overwrite_b : input int, optional
        Default: 0
    side : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    trans_a : input int, optional
        Default: 0
    diag : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('F') with bounds (ldb,n) and b storage
    """
    pass

def ctrsv(a, x, incx=None, offx=None, lower=None, trans=None, diag=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    xout = ctrsv(a,x,[incx,offx,lower,trans,diag,overwrite_x])
    
    Wrapper for ``ctrsv``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    x : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    diag : input int, optional
        Default: 0
    
    Returns
    -------
    xout : rank-1 array('F') with bounds (*) and x storage
    """
    pass

def dasum(x, n=None, offx=None, incx=None): # real signature unknown; restored from __doc__
    """
    s = dasum(x,[n,offx,incx])
    
    Wrapper for ``dasum``.
    
    Parameters
    ----------
    x : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    s : float
    """
    pass

def daxpy(x, y, n=None, a=None, offx=None, incx=None, offy=None, incy=None): # real signature unknown; restored from __doc__
    """
    z = daxpy(x,y,[n,a,offx,incx,offy,incy])
    
    Wrapper for ``daxpy``.
    
    Parameters
    ----------
    x : input rank-1 array('d') with bounds (*)
    y : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    a : input float, optional
        Default: 1.0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    z : rank-1 array('d') with bounds (*) and y storage
    """
    pass

def dcopy(x, y, n=None, offx=None, incx=None, offy=None, incy=None): # real signature unknown; restored from __doc__
    """
    y = dcopy(x,y,[n,offx,incx,offy,incy])
    
    Wrapper for ``dcopy``.
    
    Parameters
    ----------
    x : input rank-1 array('d') with bounds (*)
    y : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    y : rank-1 array('d') with bounds (*)
    """
    pass

def ddot(x, y, n=None, offx=None, incx=None, offy=None, incy=None): # real signature unknown; restored from __doc__
    """
    xy = ddot(x,y,[n,offx,incx,offy,incy])
    
    Wrapper for ``ddot``.
    
    Parameters
    ----------
    x : input rank-1 array('d') with bounds (*)
    y : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    xy : float
    """
    pass

def dgbmv(m, n, kl, ku, alpha, a, x, incx=None, offx=None, beta=None, y=None, incy=None, offy=None, trans=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    yout = dgbmv(m,n,kl,ku,alpha,a,x,[incx,offx,beta,y,incy,offy,trans,overwrite_y])
    
    Wrapper for ``dgbmv``.
    
    Parameters
    ----------
    m : input int
    n : input int
    kl : input int
    ku : input int
    alpha : input float
    a : input rank-2 array('d') with bounds (lda,n)
    x : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    beta : input float, optional
        Default: 0.0
    y : input rank-1 array('d') with bounds (ly)
    overwrite_y : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    
    Returns
    -------
    yout : rank-1 array('d') with bounds (ly) and y storage
    """
    pass

def dgemm(alpha, a, b, beta=None, c=None, trans_a=None, trans_b=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = dgemm(alpha,a,b,[beta,c,trans_a,trans_b,overwrite_c])
    
    Wrapper for ``dgemm``.
    
    Parameters
    ----------
    alpha : input float
    a : input rank-2 array('d') with bounds (lda,ka)
    b : input rank-2 array('d') with bounds (ldb,kb)
    
    Other Parameters
    ----------------
    beta : input float, optional
        Default: 0.0
    c : input rank-2 array('d') with bounds (m,n)
    overwrite_c : input int, optional
        Default: 0
    trans_a : input int, optional
        Default: 0
    trans_b : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('d') with bounds (m,n)
    """
    pass

def dgemv(alpha, a, x, beta=None, y=None, offx=None, incx=None, offy=None, incy=None, trans=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    y = dgemv(alpha,a,x,[beta,y,offx,incx,offy,incy,trans,overwrite_y])
    
    Wrapper for ``dgemv``.
    
    Parameters
    ----------
    alpha : input float
    a : input rank-2 array('d') with bounds (m,n)
    x : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    beta : input float, optional
        Default: 0.0
    y : input rank-1 array('d') with bounds (ly)
    overwrite_y : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    trans : input int, optional
        Default: 0
    
    Returns
    -------
    y : rank-1 array('d') with bounds (ly)
    """
    pass

def dger(alpha, x, y, incx=None, incy=None, a=None, overwrite_x=None, overwrite_y=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = dger(alpha,x,y,[incx,incy,a,overwrite_x,overwrite_y,overwrite_a])
    
    Wrapper for ``dger``.
    
    Parameters
    ----------
    alpha : input float
    x : input rank-1 array('d') with bounds (m)
    y : input rank-1 array('d') with bounds (n)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 1
    incx : input int, optional
        Default: 1
    overwrite_y : input int, optional
        Default: 1
    incy : input int, optional
        Default: 1
    a : input rank-2 array('d') with bounds (m,n), optional
        Default: 0.0
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('d') with bounds (m,n)
    """
    pass

def dnrm2(x, n=None, offx=None, incx=None): # real signature unknown; restored from __doc__
    """
    n2 = dnrm2(x,[n,offx,incx])
    
    Wrapper for ``dnrm2``.
    
    Parameters
    ----------
    x : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    n2 : float
    """
    pass

def drot(x, y, c, s, n=None, offx=None, incx=None, offy=None, incy=None, overwrite_x=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    x,y = drot(x,y,c,s,[n,offx,incx,offy,incy,overwrite_x,overwrite_y])
    
    Wrapper for ``drot``.
    
    Parameters
    ----------
    x : input rank-1 array('d') with bounds (*)
    y : input rank-1 array('d') with bounds (*)
    c : input float
    s : input float
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-1-offx)/abs(incx)+1
    overwrite_x : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    overwrite_y : input int, optional
        Default: 0
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    x : rank-1 array('d') with bounds (*)
    y : rank-1 array('d') with bounds (*)
    """
    pass

def drotg(a, b): # real signature unknown; restored from __doc__
    """
    c,s = drotg(a,b)
    
    Wrapper for ``drotg``.
    
    Parameters
    ----------
    a : input float
    b : input float
    
    Returns
    -------
    c : float
    s : float
    """
    pass

def drotm(x, y, param, n=None, offx=None, incx=None, offy=None, incy=None, overwrite_x=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    x,y = drotm(x,y,param,[n,offx,incx,offy,incy,overwrite_x,overwrite_y])
    
    Wrapper for ``drotm``.
    
    Parameters
    ----------
    x : input rank-1 array('d') with bounds (*)
    y : input rank-1 array('d') with bounds (*)
    param : input rank-1 array('d') with bounds (5)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    overwrite_x : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    overwrite_y : input int, optional
        Default: 0
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    x : rank-1 array('d') with bounds (*)
    y : rank-1 array('d') with bounds (*)
    """
    pass

def drotmg(d1, d2, x1, y1): # real signature unknown; restored from __doc__
    """
    param = drotmg(d1,d2,x1,y1)
    
    Wrapper for ``drotmg``.
    
    Parameters
    ----------
    d1 : input float
    d2 : input float
    x1 : input float
    y1 : input float
    
    Returns
    -------
    param : rank-1 array('d') with bounds (5)
    """
    pass

def dsbmv(k, alpha, a, x, incx=None, offx=None, beta=None, y=None, incy=None, offy=None, lower=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    yout = dsbmv(k,alpha,a,x,[incx,offx,beta,y,incy,offy,lower,overwrite_y])
    
    Wrapper for ``dsbmv``.
    
    Parameters
    ----------
    k : input int
    alpha : input float
    a : input rank-2 array('d') with bounds (lda,n)
    x : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    beta : input float, optional
        Default: 0.0
    y : input rank-1 array('d') with bounds (ly)
    overwrite_y : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    yout : rank-1 array('d') with bounds (ly) and y storage
    """
    pass

def dscal(a, x, n=None, offx=None, incx=None): # real signature unknown; restored from __doc__
    """
    x = dscal(a,x,[n,offx,incx])
    
    Wrapper for ``dscal``.
    
    Parameters
    ----------
    a : input float
    x : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    x : rank-1 array('d') with bounds (*)
    """
    pass

def dspmv(n, alpha, ap, x, incx=None, offx=None, beta=None, y=None, incy=None, offy=None, lower=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    yout = dspmv(n,alpha,ap,x,[incx,offx,beta,y,incy,offy,lower,overwrite_y])
    
    Wrapper for ``dspmv``.
    
    Parameters
    ----------
    n : input int
    alpha : input float
    ap : input rank-1 array('d') with bounds (*)
    x : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    beta : input float, optional
        Default: 0.0
    y : input rank-1 array('d') with bounds (ly)
    overwrite_y : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    yout : rank-1 array('d') with bounds (ly) and y storage
    """
    pass

def dspr(n, alpha, x, ap, incx=None, offx=None, lower=None, overwrite_ap=None): # real signature unknown; restored from __doc__
    """
    apu = dspr(n,alpha,x,ap,[incx,offx,lower,overwrite_ap])
    
    Wrapper for ``dspr``.
    
    Parameters
    ----------
    n : input int
    alpha : input float
    x : input rank-1 array('d') with bounds (*)
    ap : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    overwrite_ap : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    apu : rank-1 array('d') with bounds (*) and ap storage
    """
    pass

def dspr2(n, alpha, x, y, ap, incx=None, offx=None, incy=None, offy=None, lower=None, overwrite_ap=None): # real signature unknown; restored from __doc__
    """
    apu = dspr2(n,alpha,x,y,ap,[incx,offx,incy,offy,lower,overwrite_ap])
    
    Wrapper for ``dspr2``.
    
    Parameters
    ----------
    n : input int
    alpha : input float
    x : input rank-1 array('d') with bounds (*)
    y : input rank-1 array('d') with bounds (*)
    ap : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    overwrite_ap : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    apu : rank-1 array('d') with bounds (*) and ap storage
    """
    pass

def dswap(x, y, n=None, offx=None, incx=None, offy=None, incy=None): # real signature unknown; restored from __doc__
    """
    x,y = dswap(x,y,[n,offx,incx,offy,incy])
    
    Wrapper for ``dswap``.
    
    Parameters
    ----------
    x : input rank-1 array('d') with bounds (*)
    y : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    x : rank-1 array('d') with bounds (*)
    y : rank-1 array('d') with bounds (*)
    """
    pass

def dsymm(alpha, a, b, beta=None, c=None, side=None, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = dsymm(alpha,a,b,[beta,c,side,lower,overwrite_c])
    
    Wrapper for ``dsymm``.
    
    Parameters
    ----------
    alpha : input float
    a : input rank-2 array('d') with bounds (lda,ka)
    b : input rank-2 array('d') with bounds (ldb,kb)
    
    Other Parameters
    ----------------
    beta : input float, optional
        Default: 0.0
    c : input rank-2 array('d') with bounds (m,n)
    overwrite_c : input int, optional
        Default: 0
    side : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('d') with bounds (m,n)
    """
    pass

def dsymv(alpha, a, x, beta=None, y=None, offx=None, incx=None, offy=None, incy=None, lower=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    y = dsymv(alpha,a,x,[beta,y,offx,incx,offy,incy,lower,overwrite_y])
    
    Wrapper for ``dsymv``.
    
    Parameters
    ----------
    alpha : input float
    a : input rank-2 array('d') with bounds (n,n)
    x : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    beta : input float, optional
        Default: 0.0
    y : input rank-1 array('d') with bounds (ly)
    overwrite_y : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    y : rank-1 array('d') with bounds (ly)
    """
    pass

def dsyr(alpha, x, lower=None, incx=None, offx=None, n=None, a=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = dsyr(alpha,x,[lower,incx,offx,n,a,overwrite_a])
    
    Wrapper for ``dsyr``.
    
    Parameters
    ----------
    alpha : input float
    x : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    n : input int, optional
        Default: (len(x)-1-offx)/abs(incx)+1
    a : input rank-2 array('d') with bounds (n,n)
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('d') with bounds (n,n)
    """
    pass

def dsyr2(alpha, x, y, lower=None, incx=None, offx=None, incy=None, offy=None, n=None, a=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = dsyr2(alpha,x,y,[lower,incx,offx,incy,offy,n,a,overwrite_a])
    
    Wrapper for ``dsyr2``.
    
    Parameters
    ----------
    alpha : input float
    x : input rank-1 array('d') with bounds (*)
    y : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    n : input int, optional
        Default: ((len(x)-1-offx)/abs(incx)+1 <=(len(y)-1-offy)/abs(incy)+1 ?(len(x)-1-offx)/abs(incx)+1 :(len(y)-1-offy)/abs(incy)+1)
    a : input rank-2 array('d') with bounds (n,n)
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('d') with bounds (n,n)
    """
    pass

def dsyr2k(alpha, a, b, beta=None, c=None, trans=None, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = dsyr2k(alpha,a,b,[beta,c,trans,lower,overwrite_c])
    
    Wrapper for ``dsyr2k``.
    
    Parameters
    ----------
    alpha : input float
    a : input rank-2 array('d') with bounds (lda,ka)
    b : input rank-2 array('d') with bounds (ldb,kb)
    
    Other Parameters
    ----------------
    beta : input float, optional
        Default: 0.0
    c : input rank-2 array('d') with bounds (n,n)
    overwrite_c : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('d') with bounds (n,n)
    """
    pass

def dsyrk(alpha, a, beta=None, c=None, trans=None, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = dsyrk(alpha,a,[beta,c,trans,lower,overwrite_c])
    
    Wrapper for ``dsyrk``.
    
    Parameters
    ----------
    alpha : input float
    a : input rank-2 array('d') with bounds (lda,ka)
    
    Other Parameters
    ----------------
    beta : input float, optional
        Default: 0.0
    c : input rank-2 array('d') with bounds (n,n)
    overwrite_c : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('d') with bounds (n,n)
    """
    pass

def dtbmv(k, a, x, incx=None, offx=None, lower=None, trans=None, diag=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    xout = dtbmv(k,a,x,[incx,offx,lower,trans,diag,overwrite_x])
    
    Wrapper for ``dtbmv``.
    
    Parameters
    ----------
    k : input int
    a : input rank-2 array('d') with bounds (lda,n)
    x : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    diag : input int, optional
        Default: 0
    
    Returns
    -------
    xout : rank-1 array('d') with bounds (*) and x storage
    """
    pass

def dtbsv(k, a, x, incx=None, offx=None, lower=None, trans=None, diag=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    xout = dtbsv(k,a,x,[incx,offx,lower,trans,diag,overwrite_x])
    
    Wrapper for ``dtbsv``.
    
    Parameters
    ----------
    k : input int
    a : input rank-2 array('d') with bounds (lda,n)
    x : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    diag : input int, optional
        Default: 0
    
    Returns
    -------
    xout : rank-1 array('d') with bounds (*) and x storage
    """
    pass

def dtpmv(n, ap, x, incx=None, offx=None, lower=None, trans=None, diag=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    xout = dtpmv(n,ap,x,[incx,offx,lower,trans,diag,overwrite_x])
    
    Wrapper for ``dtpmv``.
    
    Parameters
    ----------
    n : input int
    ap : input rank-1 array('d') with bounds (*)
    x : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    diag : input int, optional
        Default: 0
    
    Returns
    -------
    xout : rank-1 array('d') with bounds (*) and x storage
    """
    pass

def dtpsv(n, ap, x, incx=None, offx=None, lower=None, trans=None, diag=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    xout = dtpsv(n,ap,x,[incx,offx,lower,trans,diag,overwrite_x])
    
    Wrapper for ``dtpsv``.
    
    Parameters
    ----------
    n : input int
    ap : input rank-1 array('d') with bounds (*)
    x : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    diag : input int, optional
        Default: 0
    
    Returns
    -------
    xout : rank-1 array('d') with bounds (*) and x storage
    """
    pass

def dtrmm(alpha, a, b, side=None, lower=None, trans_a=None, diag=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    b = dtrmm(alpha,a,b,[side,lower,trans_a,diag,overwrite_b])
    
    Wrapper for ``dtrmm``.
    
    Parameters
    ----------
    alpha : input float
    a : input rank-2 array('d') with bounds (lda,k)
    b : input rank-2 array('d') with bounds (ldb,n)
    
    Other Parameters
    ----------------
    overwrite_b : input int, optional
        Default: 0
    side : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    trans_a : input int, optional
        Default: 0
    diag : input int, optional
        Default: 0
    
    Returns
    -------
    b : rank-2 array('d') with bounds (ldb,n)
    """
    pass

def dtrmv(a, x, offx=None, incx=None, lower=None, trans=None, diag=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    x = dtrmv(a,x,[offx,incx,lower,trans,diag,overwrite_x])
    
    Wrapper for ``dtrmv``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    x : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    diag : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-1 array('d') with bounds (*)
    """
    pass

def dtrsm(alpha, a, b, side=None, lower=None, trans_a=None, diag=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x = dtrsm(alpha,a,b,[side,lower,trans_a,diag,overwrite_b])
    
    Wrapper for ``dtrsm``.
    
    Parameters
    ----------
    alpha : input float
    a : input rank-2 array('d') with bounds (lda,*)
    b : input rank-2 array('d') with bounds (ldb,n)
    
    Other Parameters
    ----------------
    overwrite_b : input int, optional
        Default: 0
    side : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    trans_a : input int, optional
        Default: 0
    diag : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('d') with bounds (ldb,n) and b storage
    """
    pass

def dtrsv(a, x, incx=None, offx=None, lower=None, trans=None, diag=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    xout = dtrsv(a,x,[incx,offx,lower,trans,diag,overwrite_x])
    
    Wrapper for ``dtrsv``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    x : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    diag : input int, optional
        Default: 0
    
    Returns
    -------
    xout : rank-1 array('d') with bounds (*) and x storage
    """
    pass

def dzasum(x, n=None, offx=None, incx=None): # real signature unknown; restored from __doc__
    """
    s = dzasum(x,[n,offx,incx])
    
    Wrapper for ``dzasum``.
    
    Parameters
    ----------
    x : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    s : float
    """
    pass

def dznrm2(x, n=None, offx=None, incx=None): # real signature unknown; restored from __doc__
    """
    n2 = dznrm2(x,[n,offx,incx])
    
    Wrapper for ``dznrm2``.
    
    Parameters
    ----------
    x : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    n2 : float
    """
    pass

def icamax(x, n=None, offx=None, incx=None): # real signature unknown; restored from __doc__
    """
    k = icamax(x,[n,offx,incx])
    
    Wrapper for ``icamax``.
    
    Parameters
    ----------
    x : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    k : int
    """
    pass

def idamax(x, n=None, offx=None, incx=None): # real signature unknown; restored from __doc__
    """
    k = idamax(x,[n,offx,incx])
    
    Wrapper for ``idamax``.
    
    Parameters
    ----------
    x : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    k : int
    """
    pass

def isamax(x, n=None, offx=None, incx=None): # real signature unknown; restored from __doc__
    """
    k = isamax(x,[n,offx,incx])
    
    Wrapper for ``isamax``.
    
    Parameters
    ----------
    x : input rank-1 array('f') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    k : int
    """
    pass

def izamax(x, n=None, offx=None, incx=None): # real signature unknown; restored from __doc__
    """
    k = izamax(x,[n,offx,incx])
    
    Wrapper for ``izamax``.
    
    Parameters
    ----------
    x : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    k : int
    """
    pass

def sasum(x, n=None, offx=None, incx=None): # real signature unknown; restored from __doc__
    """
    s = sasum(x,[n,offx,incx])
    
    Wrapper for ``sasum``.
    
    Parameters
    ----------
    x : input rank-1 array('f') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    s : float
    """
    pass

def saxpy(x, y, n=None, a=None, offx=None, incx=None, offy=None, incy=None): # real signature unknown; restored from __doc__
    """
    z = saxpy(x,y,[n,a,offx,incx,offy,incy])
    
    Wrapper for ``saxpy``.
    
    Parameters
    ----------
    x : input rank-1 array('f') with bounds (*)
    y : input rank-1 array('f') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    a : input float, optional
        Default: 1.0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    z : rank-1 array('f') with bounds (*) and y storage
    """
    pass

def scasum(x, n=None, offx=None, incx=None): # real signature unknown; restored from __doc__
    """
    s = scasum(x,[n,offx,incx])
    
    Wrapper for ``scasum``.
    
    Parameters
    ----------
    x : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    s : float
    """
    pass

def scnrm2(x, n=None, offx=None, incx=None): # real signature unknown; restored from __doc__
    """
    n2 = scnrm2(x,[n,offx,incx])
    
    Wrapper for ``scnrm2``.
    
    Parameters
    ----------
    x : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    n2 : float
    """
    pass

def scopy(x, y, n=None, offx=None, incx=None, offy=None, incy=None): # real signature unknown; restored from __doc__
    """
    y = scopy(x,y,[n,offx,incx,offy,incy])
    
    Wrapper for ``scopy``.
    
    Parameters
    ----------
    x : input rank-1 array('f') with bounds (*)
    y : input rank-1 array('f') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    y : rank-1 array('f') with bounds (*)
    """
    pass

def sdot(x, y, n=None, offx=None, incx=None, offy=None, incy=None): # real signature unknown; restored from __doc__
    """
    xy = sdot(x,y,[n,offx,incx,offy,incy])
    
    Wrapper for ``sdot``.
    
    Parameters
    ----------
    x : input rank-1 array('f') with bounds (*)
    y : input rank-1 array('f') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    xy : float
    """
    pass

def sgbmv(m, n, kl, ku, alpha, a, x, incx=None, offx=None, beta=None, y=None, incy=None, offy=None, trans=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    yout = sgbmv(m,n,kl,ku,alpha,a,x,[incx,offx,beta,y,incy,offy,trans,overwrite_y])
    
    Wrapper for ``sgbmv``.
    
    Parameters
    ----------
    m : input int
    n : input int
    kl : input int
    ku : input int
    alpha : input float
    a : input rank-2 array('f') with bounds (lda,n)
    x : input rank-1 array('f') with bounds (*)
    
    Other Parameters
    ----------------
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    beta : input float, optional
        Default: 0.0
    y : input rank-1 array('f') with bounds (ly)
    overwrite_y : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    
    Returns
    -------
    yout : rank-1 array('f') with bounds (ly) and y storage
    """
    pass

def sgemm(alpha, a, b, beta=None, c=None, trans_a=None, trans_b=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = sgemm(alpha,a,b,[beta,c,trans_a,trans_b,overwrite_c])
    
    Wrapper for ``sgemm``.
    
    Parameters
    ----------
    alpha : input float
    a : input rank-2 array('f') with bounds (lda,ka)
    b : input rank-2 array('f') with bounds (ldb,kb)
    
    Other Parameters
    ----------------
    beta : input float, optional
        Default: 0.0
    c : input rank-2 array('f') with bounds (m,n)
    overwrite_c : input int, optional
        Default: 0
    trans_a : input int, optional
        Default: 0
    trans_b : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('f') with bounds (m,n)
    """
    pass

def sgemv(alpha, a, x, beta=None, y=None, offx=None, incx=None, offy=None, incy=None, trans=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    y = sgemv(alpha,a,x,[beta,y,offx,incx,offy,incy,trans,overwrite_y])
    
    Wrapper for ``sgemv``.
    
    Parameters
    ----------
    alpha : input float
    a : input rank-2 array('f') with bounds (m,n)
    x : input rank-1 array('f') with bounds (*)
    
    Other Parameters
    ----------------
    beta : input float, optional
        Default: 0.0
    y : input rank-1 array('f') with bounds (ly)
    overwrite_y : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    trans : input int, optional
        Default: 0
    
    Returns
    -------
    y : rank-1 array('f') with bounds (ly)
    """
    pass

def sger(alpha, x, y, incx=None, incy=None, a=None, overwrite_x=None, overwrite_y=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = sger(alpha,x,y,[incx,incy,a,overwrite_x,overwrite_y,overwrite_a])
    
    Wrapper for ``sger``.
    
    Parameters
    ----------
    alpha : input float
    x : input rank-1 array('f') with bounds (m)
    y : input rank-1 array('f') with bounds (n)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 1
    incx : input int, optional
        Default: 1
    overwrite_y : input int, optional
        Default: 1
    incy : input int, optional
        Default: 1
    a : input rank-2 array('f') with bounds (m,n), optional
        Default: 0.0
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('f') with bounds (m,n)
    """
    pass

def snrm2(x, n=None, offx=None, incx=None): # real signature unknown; restored from __doc__
    """
    n2 = snrm2(x,[n,offx,incx])
    
    Wrapper for ``snrm2``.
    
    Parameters
    ----------
    x : input rank-1 array('f') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    n2 : float
    """
    pass

def srot(x, y, c, s, n=None, offx=None, incx=None, offy=None, incy=None, overwrite_x=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    x,y = srot(x,y,c,s,[n,offx,incx,offy,incy,overwrite_x,overwrite_y])
    
    Wrapper for ``srot``.
    
    Parameters
    ----------
    x : input rank-1 array('f') with bounds (*)
    y : input rank-1 array('f') with bounds (*)
    c : input float
    s : input float
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-1-offx)/abs(incx)+1
    overwrite_x : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    overwrite_y : input int, optional
        Default: 0
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    x : rank-1 array('f') with bounds (*)
    y : rank-1 array('f') with bounds (*)
    """
    pass

def srotg(a, b): # real signature unknown; restored from __doc__
    """
    c,s = srotg(a,b)
    
    Wrapper for ``srotg``.
    
    Parameters
    ----------
    a : input float
    b : input float
    
    Returns
    -------
    c : float
    s : float
    """
    pass

def srotm(x, y, param, n=None, offx=None, incx=None, offy=None, incy=None, overwrite_x=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    x,y = srotm(x,y,param,[n,offx,incx,offy,incy,overwrite_x,overwrite_y])
    
    Wrapper for ``srotm``.
    
    Parameters
    ----------
    x : input rank-1 array('f') with bounds (*)
    y : input rank-1 array('f') with bounds (*)
    param : input rank-1 array('f') with bounds (5)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    overwrite_x : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    overwrite_y : input int, optional
        Default: 0
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    x : rank-1 array('f') with bounds (*)
    y : rank-1 array('f') with bounds (*)
    """
    pass

def srotmg(d1, d2, x1, y1): # real signature unknown; restored from __doc__
    """
    param = srotmg(d1,d2,x1,y1)
    
    Wrapper for ``srotmg``.
    
    Parameters
    ----------
    d1 : input float
    d2 : input float
    x1 : input float
    y1 : input float
    
    Returns
    -------
    param : rank-1 array('f') with bounds (5)
    """
    pass

def ssbmv(k, alpha, a, x, incx=None, offx=None, beta=None, y=None, incy=None, offy=None, lower=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    yout = ssbmv(k,alpha,a,x,[incx,offx,beta,y,incy,offy,lower,overwrite_y])
    
    Wrapper for ``ssbmv``.
    
    Parameters
    ----------
    k : input int
    alpha : input float
    a : input rank-2 array('f') with bounds (lda,n)
    x : input rank-1 array('f') with bounds (*)
    
    Other Parameters
    ----------------
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    beta : input float, optional
        Default: 0.0
    y : input rank-1 array('f') with bounds (ly)
    overwrite_y : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    yout : rank-1 array('f') with bounds (ly) and y storage
    """
    pass

def sscal(a, x, n=None, offx=None, incx=None): # real signature unknown; restored from __doc__
    """
    x = sscal(a,x,[n,offx,incx])
    
    Wrapper for ``sscal``.
    
    Parameters
    ----------
    a : input float
    x : input rank-1 array('f') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    x : rank-1 array('f') with bounds (*)
    """
    pass

def sspmv(n, alpha, ap, x, incx=None, offx=None, beta=None, y=None, incy=None, offy=None, lower=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    yout = sspmv(n,alpha,ap,x,[incx,offx,beta,y,incy,offy,lower,overwrite_y])
    
    Wrapper for ``sspmv``.
    
    Parameters
    ----------
    n : input int
    alpha : input float
    ap : input rank-1 array('f') with bounds (*)
    x : input rank-1 array('f') with bounds (*)
    
    Other Parameters
    ----------------
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    beta : input float, optional
        Default: 0.0
    y : input rank-1 array('f') with bounds (ly)
    overwrite_y : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    yout : rank-1 array('f') with bounds (ly) and y storage
    """
    pass

def sspr(n, alpha, x, ap, incx=None, offx=None, lower=None, overwrite_ap=None): # real signature unknown; restored from __doc__
    """
    apu = sspr(n,alpha,x,ap,[incx,offx,lower,overwrite_ap])
    
    Wrapper for ``sspr``.
    
    Parameters
    ----------
    n : input int
    alpha : input float
    x : input rank-1 array('f') with bounds (*)
    ap : input rank-1 array('f') with bounds (*)
    
    Other Parameters
    ----------------
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    overwrite_ap : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    apu : rank-1 array('f') with bounds (*) and ap storage
    """
    pass

def sspr2(n, alpha, x, y, ap, incx=None, offx=None, incy=None, offy=None, lower=None, overwrite_ap=None): # real signature unknown; restored from __doc__
    """
    apu = sspr2(n,alpha,x,y,ap,[incx,offx,incy,offy,lower,overwrite_ap])
    
    Wrapper for ``sspr2``.
    
    Parameters
    ----------
    n : input int
    alpha : input float
    x : input rank-1 array('f') with bounds (*)
    y : input rank-1 array('f') with bounds (*)
    ap : input rank-1 array('f') with bounds (*)
    
    Other Parameters
    ----------------
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    overwrite_ap : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    apu : rank-1 array('f') with bounds (*) and ap storage
    """
    pass

def sswap(x, y, n=None, offx=None, incx=None, offy=None, incy=None): # real signature unknown; restored from __doc__
    """
    x,y = sswap(x,y,[n,offx,incx,offy,incy])
    
    Wrapper for ``sswap``.
    
    Parameters
    ----------
    x : input rank-1 array('f') with bounds (*)
    y : input rank-1 array('f') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    x : rank-1 array('f') with bounds (*)
    y : rank-1 array('f') with bounds (*)
    """
    pass

def ssymm(alpha, a, b, beta=None, c=None, side=None, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = ssymm(alpha,a,b,[beta,c,side,lower,overwrite_c])
    
    Wrapper for ``ssymm``.
    
    Parameters
    ----------
    alpha : input float
    a : input rank-2 array('f') with bounds (lda,ka)
    b : input rank-2 array('f') with bounds (ldb,kb)
    
    Other Parameters
    ----------------
    beta : input float, optional
        Default: 0.0
    c : input rank-2 array('f') with bounds (m,n)
    overwrite_c : input int, optional
        Default: 0
    side : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('f') with bounds (m,n)
    """
    pass

def ssymv(alpha, a, x, beta=None, y=None, offx=None, incx=None, offy=None, incy=None, lower=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    y = ssymv(alpha,a,x,[beta,y,offx,incx,offy,incy,lower,overwrite_y])
    
    Wrapper for ``ssymv``.
    
    Parameters
    ----------
    alpha : input float
    a : input rank-2 array('f') with bounds (n,n)
    x : input rank-1 array('f') with bounds (*)
    
    Other Parameters
    ----------------
    beta : input float, optional
        Default: 0.0
    y : input rank-1 array('f') with bounds (ly)
    overwrite_y : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    y : rank-1 array('f') with bounds (ly)
    """
    pass

def ssyr(alpha, x, lower=None, incx=None, offx=None, n=None, a=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = ssyr(alpha,x,[lower,incx,offx,n,a,overwrite_a])
    
    Wrapper for ``ssyr``.
    
    Parameters
    ----------
    alpha : input float
    x : input rank-1 array('f') with bounds (*)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    n : input int, optional
        Default: (len(x)-1-offx)/abs(incx)+1
    a : input rank-2 array('f') with bounds (n,n)
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('f') with bounds (n,n)
    """
    pass

def ssyr2(alpha, x, y, lower=None, incx=None, offx=None, incy=None, offy=None, n=None, a=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = ssyr2(alpha,x,y,[lower,incx,offx,incy,offy,n,a,overwrite_a])
    
    Wrapper for ``ssyr2``.
    
    Parameters
    ----------
    alpha : input float
    x : input rank-1 array('f') with bounds (*)
    y : input rank-1 array('f') with bounds (*)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    n : input int, optional
        Default: ((len(x)-1-offx)/abs(incx)+1 <=(len(y)-1-offy)/abs(incy)+1 ?(len(x)-1-offx)/abs(incx)+1 :(len(y)-1-offy)/abs(incy)+1)
    a : input rank-2 array('f') with bounds (n,n)
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('f') with bounds (n,n)
    """
    pass

def ssyr2k(alpha, a, b, beta=None, c=None, trans=None, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = ssyr2k(alpha,a,b,[beta,c,trans,lower,overwrite_c])
    
    Wrapper for ``ssyr2k``.
    
    Parameters
    ----------
    alpha : input float
    a : input rank-2 array('f') with bounds (lda,ka)
    b : input rank-2 array('f') with bounds (ldb,kb)
    
    Other Parameters
    ----------------
    beta : input float, optional
        Default: 0.0
    c : input rank-2 array('f') with bounds (n,n)
    overwrite_c : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('f') with bounds (n,n)
    """
    pass

def ssyrk(alpha, a, beta=None, c=None, trans=None, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = ssyrk(alpha,a,[beta,c,trans,lower,overwrite_c])
    
    Wrapper for ``ssyrk``.
    
    Parameters
    ----------
    alpha : input float
    a : input rank-2 array('f') with bounds (lda,ka)
    
    Other Parameters
    ----------------
    beta : input float, optional
        Default: 0.0
    c : input rank-2 array('f') with bounds (n,n)
    overwrite_c : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('f') with bounds (n,n)
    """
    pass

def stbmv(k, a, x, incx=None, offx=None, lower=None, trans=None, diag=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    xout = stbmv(k,a,x,[incx,offx,lower,trans,diag,overwrite_x])
    
    Wrapper for ``stbmv``.
    
    Parameters
    ----------
    k : input int
    a : input rank-2 array('f') with bounds (lda,n)
    x : input rank-1 array('f') with bounds (*)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    diag : input int, optional
        Default: 0
    
    Returns
    -------
    xout : rank-1 array('f') with bounds (*) and x storage
    """
    pass

def stbsv(k, a, x, incx=None, offx=None, lower=None, trans=None, diag=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    xout = stbsv(k,a,x,[incx,offx,lower,trans,diag,overwrite_x])
    
    Wrapper for ``stbsv``.
    
    Parameters
    ----------
    k : input int
    a : input rank-2 array('f') with bounds (lda,n)
    x : input rank-1 array('f') with bounds (*)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    diag : input int, optional
        Default: 0
    
    Returns
    -------
    xout : rank-1 array('f') with bounds (*) and x storage
    """
    pass

def stpmv(n, ap, x, incx=None, offx=None, lower=None, trans=None, diag=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    xout = stpmv(n,ap,x,[incx,offx,lower,trans,diag,overwrite_x])
    
    Wrapper for ``stpmv``.
    
    Parameters
    ----------
    n : input int
    ap : input rank-1 array('f') with bounds (*)
    x : input rank-1 array('f') with bounds (*)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    diag : input int, optional
        Default: 0
    
    Returns
    -------
    xout : rank-1 array('f') with bounds (*) and x storage
    """
    pass

def stpsv(n, ap, x, incx=None, offx=None, lower=None, trans=None, diag=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    xout = stpsv(n,ap,x,[incx,offx,lower,trans,diag,overwrite_x])
    
    Wrapper for ``stpsv``.
    
    Parameters
    ----------
    n : input int
    ap : input rank-1 array('f') with bounds (*)
    x : input rank-1 array('f') with bounds (*)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    diag : input int, optional
        Default: 0
    
    Returns
    -------
    xout : rank-1 array('f') with bounds (*) and x storage
    """
    pass

def strmm(alpha, a, b, side=None, lower=None, trans_a=None, diag=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    b = strmm(alpha,a,b,[side,lower,trans_a,diag,overwrite_b])
    
    Wrapper for ``strmm``.
    
    Parameters
    ----------
    alpha : input float
    a : input rank-2 array('f') with bounds (lda,k)
    b : input rank-2 array('f') with bounds (ldb,n)
    
    Other Parameters
    ----------------
    overwrite_b : input int, optional
        Default: 0
    side : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    trans_a : input int, optional
        Default: 0
    diag : input int, optional
        Default: 0
    
    Returns
    -------
    b : rank-2 array('f') with bounds (ldb,n)
    """
    pass

def strmv(a, x, offx=None, incx=None, lower=None, trans=None, diag=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    x = strmv(a,x,[offx,incx,lower,trans,diag,overwrite_x])
    
    Wrapper for ``strmv``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    x : input rank-1 array('f') with bounds (*)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    diag : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-1 array('f') with bounds (*)
    """
    pass

def strsm(alpha, a, b, side=None, lower=None, trans_a=None, diag=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x = strsm(alpha,a,b,[side,lower,trans_a,diag,overwrite_b])
    
    Wrapper for ``strsm``.
    
    Parameters
    ----------
    alpha : input float
    a : input rank-2 array('f') with bounds (lda,*)
    b : input rank-2 array('f') with bounds (ldb,n)
    
    Other Parameters
    ----------------
    overwrite_b : input int, optional
        Default: 0
    side : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    trans_a : input int, optional
        Default: 0
    diag : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('f') with bounds (ldb,n) and b storage
    """
    pass

def strsv(a, x, incx=None, offx=None, lower=None, trans=None, diag=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    xout = strsv(a,x,[incx,offx,lower,trans,diag,overwrite_x])
    
    Wrapper for ``strsv``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    x : input rank-1 array('f') with bounds (*)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    diag : input int, optional
        Default: 0
    
    Returns
    -------
    xout : rank-1 array('f') with bounds (*) and x storage
    """
    pass

def zaxpy(x, y, n=None, a=None, offx=None, incx=None, offy=None, incy=None): # real signature unknown; restored from __doc__
    """
    z = zaxpy(x,y,[n,a,offx,incx,offy,incy])
    
    Wrapper for ``zaxpy``.
    
    Parameters
    ----------
    x : input rank-1 array('D') with bounds (*)
    y : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    a : input complex, optional
        Default: (1.0, 0.0)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    z : rank-1 array('D') with bounds (*) and y storage
    """
    pass

def zcopy(x, y, n=None, offx=None, incx=None, offy=None, incy=None): # real signature unknown; restored from __doc__
    """
    y = zcopy(x,y,[n,offx,incx,offy,incy])
    
    Wrapper for ``zcopy``.
    
    Parameters
    ----------
    x : input rank-1 array('D') with bounds (*)
    y : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    y : rank-1 array('D') with bounds (*)
    """
    pass

def zdotc(x, y, n=None, offx=None, incx=None, offy=None, incy=None): # real signature unknown; restored from __doc__
    """
    xy = zdotc(x,y,[n,offx,incx,offy,incy])
    
    Wrapper for ``zdotc``.
    
    Parameters
    ----------
    x : input rank-1 array('D') with bounds (*)
    y : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    xy : complex
    """
    pass

def zdotu(x, y, n=None, offx=None, incx=None, offy=None, incy=None): # real signature unknown; restored from __doc__
    """
    xy = zdotu(x,y,[n,offx,incx,offy,incy])
    
    Wrapper for ``zdotu``.
    
    Parameters
    ----------
    x : input rank-1 array('D') with bounds (*)
    y : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    xy : complex
    """
    pass

def zdrot(x, y, c, s, n=None, offx=None, incx=None, offy=None, incy=None, overwrite_x=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    x,y = zdrot(x,y,c,s,[n,offx,incx,offy,incy,overwrite_x,overwrite_y])
    
    Wrapper for ``zdrot``.
    
    Parameters
    ----------
    x : input rank-1 array('D') with bounds (*)
    y : input rank-1 array('D') with bounds (*)
    c : input float
    s : input float
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-1-offx)/abs(incx)+1
    overwrite_x : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    overwrite_y : input int, optional
        Default: 0
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    x : rank-1 array('D') with bounds (*)
    y : rank-1 array('D') with bounds (*)
    """
    pass

def zdscal(a, x, n=None, offx=None, incx=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    x = zdscal(a,x,[n,offx,incx,overwrite_x])
    
    Wrapper for ``zdscal``.
    
    Parameters
    ----------
    a : input float
    x : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    overwrite_x : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    x : rank-1 array('D') with bounds (*)
    """
    pass

def zgbmv(m, n, kl, ku, alpha, a, x, incx=None, offx=None, beta=None, y=None, incy=None, offy=None, trans=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    yout = zgbmv(m,n,kl,ku,alpha,a,x,[incx,offx,beta,y,incy,offy,trans,overwrite_y])
    
    Wrapper for ``zgbmv``.
    
    Parameters
    ----------
    m : input int
    n : input int
    kl : input int
    ku : input int
    alpha : input complex
    a : input rank-2 array('D') with bounds (lda,n)
    x : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    beta : input complex, optional
        Default: (0.0, 0.0)
    y : input rank-1 array('D') with bounds (ly)
    overwrite_y : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    
    Returns
    -------
    yout : rank-1 array('D') with bounds (ly) and y storage
    """
    pass

def zgemm(alpha, a, b, beta=None, c=None, trans_a=None, trans_b=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = zgemm(alpha,a,b,[beta,c,trans_a,trans_b,overwrite_c])
    
    Wrapper for ``zgemm``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('D') with bounds (lda,ka)
    b : input rank-2 array('D') with bounds (ldb,kb)
    
    Other Parameters
    ----------------
    beta : input complex, optional
        Default: (0.0, 0.0)
    c : input rank-2 array('D') with bounds (m,n)
    overwrite_c : input int, optional
        Default: 0
    trans_a : input int, optional
        Default: 0
    trans_b : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('D') with bounds (m,n)
    """
    pass

def zgemv(alpha, a, x, beta=None, y=None, offx=None, incx=None, offy=None, incy=None, trans=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    y = zgemv(alpha,a,x,[beta,y,offx,incx,offy,incy,trans,overwrite_y])
    
    Wrapper for ``zgemv``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('D') with bounds (m,n)
    x : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    beta : input complex, optional
        Default: (0.0, 0.0)
    y : input rank-1 array('D') with bounds (ly)
    overwrite_y : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    trans : input int, optional
        Default: 0
    
    Returns
    -------
    y : rank-1 array('D') with bounds (ly)
    """
    pass

def zgerc(alpha, x, y, incx=None, incy=None, a=None, overwrite_x=None, overwrite_y=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = zgerc(alpha,x,y,[incx,incy,a,overwrite_x,overwrite_y,overwrite_a])
    
    Wrapper for ``zgerc``.
    
    Parameters
    ----------
    alpha : input complex
    x : input rank-1 array('D') with bounds (m)
    y : input rank-1 array('D') with bounds (n)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 1
    incx : input int, optional
        Default: 1
    overwrite_y : input int, optional
        Default: 1
    incy : input int, optional
        Default: 1
    a : input rank-2 array('D') with bounds (m,n), optional
        Default: (0.0,0.0)
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('D') with bounds (m,n)
    """
    pass

def zgeru(alpha, x, y, incx=None, incy=None, a=None, overwrite_x=None, overwrite_y=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = zgeru(alpha,x,y,[incx,incy,a,overwrite_x,overwrite_y,overwrite_a])
    
    Wrapper for ``zgeru``.
    
    Parameters
    ----------
    alpha : input complex
    x : input rank-1 array('D') with bounds (m)
    y : input rank-1 array('D') with bounds (n)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 1
    incx : input int, optional
        Default: 1
    overwrite_y : input int, optional
        Default: 1
    incy : input int, optional
        Default: 1
    a : input rank-2 array('D') with bounds (m,n), optional
        Default: (0.0,0.0)
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('D') with bounds (m,n)
    """
    pass

def zhbmv(k, alpha, a, x, incx=None, offx=None, beta=None, y=None, incy=None, offy=None, lower=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    yout = zhbmv(k,alpha,a,x,[incx,offx,beta,y,incy,offy,lower,overwrite_y])
    
    Wrapper for ``zhbmv``.
    
    Parameters
    ----------
    k : input int
    alpha : input complex
    a : input rank-2 array('D') with bounds (lda,n)
    x : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    beta : input complex, optional
        Default: (0.0, 0.0)
    y : input rank-1 array('D') with bounds (ly)
    overwrite_y : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    yout : rank-1 array('D') with bounds (ly) and y storage
    """
    pass

def zhemm(alpha, a, b, beta=None, c=None, side=None, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = zhemm(alpha,a,b,[beta,c,side,lower,overwrite_c])
    
    Wrapper for ``zhemm``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('D') with bounds (lda,ka)
    b : input rank-2 array('D') with bounds (ldb,kb)
    
    Other Parameters
    ----------------
    beta : input complex, optional
        Default: (0.0, 0.0)
    c : input rank-2 array('D') with bounds (m,n)
    overwrite_c : input int, optional
        Default: 0
    side : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('D') with bounds (m,n)
    """
    pass

def zhemv(alpha, a, x, beta=None, y=None, offx=None, incx=None, offy=None, incy=None, lower=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    y = zhemv(alpha,a,x,[beta,y,offx,incx,offy,incy,lower,overwrite_y])
    
    Wrapper for ``zhemv``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('D') with bounds (n,n)
    x : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    beta : input complex, optional
        Default: (0.0, 0.0)
    y : input rank-1 array('D') with bounds (ly)
    overwrite_y : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    y : rank-1 array('D') with bounds (ly)
    """
    pass

def zher(alpha, x, lower=None, incx=None, offx=None, n=None, a=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = zher(alpha,x,[lower,incx,offx,n,a,overwrite_a])
    
    Wrapper for ``zher``.
    
    Parameters
    ----------
    alpha : input complex
    x : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    n : input int, optional
        Default: (len(x)-1-offx)/abs(incx)+1
    a : input rank-2 array('D') with bounds (n,n)
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('D') with bounds (n,n)
    """
    pass

def zher2(alpha, x, y, lower=None, incx=None, offx=None, incy=None, offy=None, n=None, a=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = zher2(alpha,x,y,[lower,incx,offx,incy,offy,n,a,overwrite_a])
    
    Wrapper for ``zher2``.
    
    Parameters
    ----------
    alpha : input complex
    x : input rank-1 array('D') with bounds (*)
    y : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    n : input int, optional
        Default: ((len(x)-1-offx)/abs(incx)+1 <=(len(y)-1-offy)/abs(incy)+1 ?(len(x)-1-offx)/abs(incx)+1 :(len(y)-1-offy)/abs(incy)+1)
    a : input rank-2 array('D') with bounds (n,n)
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('D') with bounds (n,n)
    """
    pass

def zher2k(alpha, a, b, beta=None, c=None, trans=None, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = zher2k(alpha,a,b,[beta,c,trans,lower,overwrite_c])
    
    Wrapper for ``zher2k``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('D') with bounds (lda,ka)
    b : input rank-2 array('D') with bounds (ldb,kb)
    
    Other Parameters
    ----------------
    beta : input complex, optional
        Default: (0.0, 0.0)
    c : input rank-2 array('D') with bounds (n,n)
    overwrite_c : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('D') with bounds (n,n)
    """
    pass

def zherk(alpha, a, beta=None, c=None, trans=None, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = zherk(alpha,a,[beta,c,trans,lower,overwrite_c])
    
    Wrapper for ``zherk``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('D') with bounds (lda,ka)
    
    Other Parameters
    ----------------
    beta : input complex, optional
        Default: (0.0, 0.0)
    c : input rank-2 array('D') with bounds (n,n)
    overwrite_c : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('D') with bounds (n,n)
    """
    pass

def zhpmv(n, alpha, ap, x, incx=None, offx=None, beta=None, y=None, incy=None, offy=None, lower=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    yout = zhpmv(n,alpha,ap,x,[incx,offx,beta,y,incy,offy,lower,overwrite_y])
    
    Wrapper for ``zhpmv``.
    
    Parameters
    ----------
    n : input int
    alpha : input complex
    ap : input rank-1 array('D') with bounds (*)
    x : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    beta : input complex, optional
        Default: (0.0, 0.0)
    y : input rank-1 array('D') with bounds (ly)
    overwrite_y : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    yout : rank-1 array('D') with bounds (ly) and y storage
    """
    pass

def zhpr(n, alpha, x, ap, incx=None, offx=None, lower=None, overwrite_ap=None): # real signature unknown; restored from __doc__
    """
    apu = zhpr(n,alpha,x,ap,[incx,offx,lower,overwrite_ap])
    
    Wrapper for ``zhpr``.
    
    Parameters
    ----------
    n : input int
    alpha : input float
    x : input rank-1 array('D') with bounds (*)
    ap : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    overwrite_ap : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    apu : rank-1 array('D') with bounds (*) and ap storage
    """
    pass

def zhpr2(n, alpha, x, y, ap, incx=None, offx=None, incy=None, offy=None, lower=None, overwrite_ap=None): # real signature unknown; restored from __doc__
    """
    apu = zhpr2(n,alpha,x,y,ap,[incx,offx,incy,offy,lower,overwrite_ap])
    
    Wrapper for ``zhpr2``.
    
    Parameters
    ----------
    n : input int
    alpha : input complex
    x : input rank-1 array('D') with bounds (*)
    y : input rank-1 array('D') with bounds (*)
    ap : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    overwrite_ap : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    apu : rank-1 array('D') with bounds (*) and ap storage
    """
    pass

def zrotg(a, b): # real signature unknown; restored from __doc__
    """
    c,s = zrotg(a,b)
    
    Wrapper for ``zrotg``.
    
    Parameters
    ----------
    a : input complex
    b : input complex
    
    Returns
    -------
    c : complex
    s : complex
    """
    pass

def zscal(a, x, n=None, offx=None, incx=None): # real signature unknown; restored from __doc__
    """
    x = zscal(a,x,[n,offx,incx])
    
    Wrapper for ``zscal``.
    
    Parameters
    ----------
    a : input complex
    x : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    x : rank-1 array('D') with bounds (*)
    """
    pass

def zspmv(n, alpha, ap, x, incx=None, offx=None, beta=None, y=None, incy=None, offy=None, lower=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    yout = zspmv(n,alpha,ap,x,[incx,offx,beta,y,incy,offy,lower,overwrite_y])
    
    Wrapper for ``zspmv``.
    
    Parameters
    ----------
    n : input int
    alpha : input complex
    ap : input rank-1 array('D') with bounds (*)
    x : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    beta : input complex, optional
        Default: (0.0, 0.0)
    y : input rank-1 array('D') with bounds (ly)
    overwrite_y : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    yout : rank-1 array('D') with bounds (ly) and y storage
    """
    pass

def zspr(n, alpha, x, ap, incx=None, offx=None, lower=None, overwrite_ap=None): # real signature unknown; restored from __doc__
    """
    apu = zspr(n,alpha,x,ap,[incx,offx,lower,overwrite_ap])
    
    Wrapper for ``zspr``.
    
    Parameters
    ----------
    n : input int
    alpha : input complex
    x : input rank-1 array('D') with bounds (*)
    ap : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    overwrite_ap : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    apu : rank-1 array('D') with bounds (*) and ap storage
    """
    pass

def zswap(x, y, n=None, offx=None, incx=None, offy=None, incy=None): # real signature unknown; restored from __doc__
    """
    x,y = zswap(x,y,[n,offx,incx,offy,incy])
    
    Wrapper for ``zswap``.
    
    Parameters
    ----------
    x : input rank-1 array('D') with bounds (*)
    y : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    x : rank-1 array('D') with bounds (*)
    y : rank-1 array('D') with bounds (*)
    """
    pass

def zsymm(alpha, a, b, beta=None, c=None, side=None, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = zsymm(alpha,a,b,[beta,c,side,lower,overwrite_c])
    
    Wrapper for ``zsymm``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('D') with bounds (lda,ka)
    b : input rank-2 array('D') with bounds (ldb,kb)
    
    Other Parameters
    ----------------
    beta : input complex, optional
        Default: (0.0, 0.0)
    c : input rank-2 array('D') with bounds (m,n)
    overwrite_c : input int, optional
        Default: 0
    side : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('D') with bounds (m,n)
    """
    pass

def zsyr(alpha, x, lower=None, incx=None, offx=None, n=None, a=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = zsyr(alpha,x,[lower,incx,offx,n,a,overwrite_a])
    
    Wrapper for ``zsyr``.
    
    Parameters
    ----------
    alpha : input complex
    x : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    n : input int, optional
        Default: (len(x)-1-offx)/abs(incx)+1
    a : input rank-2 array('D') with bounds (n,n)
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('D') with bounds (n,n)
    """
    pass

def zsyr2k(alpha, a, b, beta=None, c=None, trans=None, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = zsyr2k(alpha,a,b,[beta,c,trans,lower,overwrite_c])
    
    Wrapper for ``zsyr2k``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('D') with bounds (lda,ka)
    b : input rank-2 array('D') with bounds (ldb,kb)
    
    Other Parameters
    ----------------
    beta : input complex, optional
        Default: (0.0, 0.0)
    c : input rank-2 array('D') with bounds (n,n)
    overwrite_c : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('D') with bounds (n,n)
    """
    pass

def zsyrk(alpha, a, beta=None, c=None, trans=None, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = zsyrk(alpha,a,[beta,c,trans,lower,overwrite_c])
    
    Wrapper for ``zsyrk``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('D') with bounds (lda,ka)
    
    Other Parameters
    ----------------
    beta : input complex, optional
        Default: (0.0, 0.0)
    c : input rank-2 array('D') with bounds (n,n)
    overwrite_c : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('D') with bounds (n,n)
    """
    pass

def ztbmv(k, a, x, incx=None, offx=None, lower=None, trans=None, diag=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    xout = ztbmv(k,a,x,[incx,offx,lower,trans,diag,overwrite_x])
    
    Wrapper for ``ztbmv``.
    
    Parameters
    ----------
    k : input int
    a : input rank-2 array('D') with bounds (lda,n)
    x : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    diag : input int, optional
        Default: 0
    
    Returns
    -------
    xout : rank-1 array('D') with bounds (*) and x storage
    """
    pass

def ztbsv(k, a, x, incx=None, offx=None, lower=None, trans=None, diag=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    xout = ztbsv(k,a,x,[incx,offx,lower,trans,diag,overwrite_x])
    
    Wrapper for ``ztbsv``.
    
    Parameters
    ----------
    k : input int
    a : input rank-2 array('D') with bounds (lda,n)
    x : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    diag : input int, optional
        Default: 0
    
    Returns
    -------
    xout : rank-1 array('D') with bounds (*) and x storage
    """
    pass

def ztpmv(n, ap, x, incx=None, offx=None, lower=None, trans=None, diag=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    xout = ztpmv(n,ap,x,[incx,offx,lower,trans,diag,overwrite_x])
    
    Wrapper for ``ztpmv``.
    
    Parameters
    ----------
    n : input int
    ap : input rank-1 array('D') with bounds (*)
    x : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    diag : input int, optional
        Default: 0
    
    Returns
    -------
    xout : rank-1 array('D') with bounds (*) and x storage
    """
    pass

def ztpsv(n, ap, x, incx=None, offx=None, lower=None, trans=None, diag=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    xout = ztpsv(n,ap,x,[incx,offx,lower,trans,diag,overwrite_x])
    
    Wrapper for ``ztpsv``.
    
    Parameters
    ----------
    n : input int
    ap : input rank-1 array('D') with bounds (*)
    x : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    diag : input int, optional
        Default: 0
    
    Returns
    -------
    xout : rank-1 array('D') with bounds (*) and x storage
    """
    pass

def ztrmm(alpha, a, b, side=None, lower=None, trans_a=None, diag=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    b = ztrmm(alpha,a,b,[side,lower,trans_a,diag,overwrite_b])
    
    Wrapper for ``ztrmm``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('D') with bounds (lda,k)
    b : input rank-2 array('D') with bounds (ldb,n)
    
    Other Parameters
    ----------------
    overwrite_b : input int, optional
        Default: 0
    side : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    trans_a : input int, optional
        Default: 0
    diag : input int, optional
        Default: 0
    
    Returns
    -------
    b : rank-2 array('D') with bounds (ldb,n)
    """
    pass

def ztrmv(a, x, offx=None, incx=None, lower=None, trans=None, diag=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    x = ztrmv(a,x,[offx,incx,lower,trans,diag,overwrite_x])
    
    Wrapper for ``ztrmv``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    x : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    diag : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-1 array('D') with bounds (*)
    """
    pass

def ztrsm(alpha, a, b, side=None, lower=None, trans_a=None, diag=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x = ztrsm(alpha,a,b,[side,lower,trans_a,diag,overwrite_b])
    
    Wrapper for ``ztrsm``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('D') with bounds (lda,*)
    b : input rank-2 array('D') with bounds (ldb,n)
    
    Other Parameters
    ----------------
    overwrite_b : input int, optional
        Default: 0
    side : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    trans_a : input int, optional
        Default: 0
    diag : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('D') with bounds (ldb,n) and b storage
    """
    pass

def ztrsv(a, x, incx=None, offx=None, lower=None, trans=None, diag=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    xout = ztrsv(a,x,[incx,offx,lower,trans,diag,overwrite_x])
    
    Wrapper for ``ztrsv``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    x : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    diag : input int, optional
        Default: 0
    
    Returns
    -------
    xout : rank-1 array('D') with bounds (*) and x storage
    """
    pass

# classes

class __fblas_error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9f8e5e80>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.linalg._fblas', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9f8e5e80>, origin='/.venv/lib/python3.8/site-packages/scipy/linalg/_fblas.cpython-38-aarch64-linux-gnu.so')"

