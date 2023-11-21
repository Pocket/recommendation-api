# encoding: utf-8
# module scipy.sparse.linalg._propack._spropack
# from /.venv/lib/python3.8/site-packages/scipy/sparse/linalg/_propack/_spropack.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
"""
This module '_spropack' is auto-generated with f2py (version:2).
Functions:
  u,sigma,bnd,v,info = slansvd(jobu,jobv,m,n,k,aprod,u,v,tolin,work,iwork,doption,ioption,dparm,iparm,kmax=(shape(u,1)-1),ldu=shape(u,0),ldv=shape(v,0),lwork=len(work),liwork=len(iwork),aprod_extra_args=())
  u,sigma,bnd,v,info = slansvd_irl(which,jobu,jobv,m,n,p,neig,maxiter,aprod,u,v,tolin,work,iwork,doption,ioption,dparm,iparm,dim=(shape(u,1)-1),ldu=shape(u,0),ldv=shape(v,0),lwork=len(work),liwork=len(iwork),aprod_extra_args=())
COMMON blocks:
  /timing/ nopx,nreorth,ndot,nreorthu,nreorthv,nitref,nrestart,nbsvd,tmvopx,tgetu0,tupdmu,tupdnu,tintv,tlanbpro,treorth,treorthu,treorthv,telru,telrv,tbsvd,tnorm2,tlansvd,nlandim,tritzvec,trestart,tdot,nsing
.
"""
# no imports

# Variables with simple values

__version__ = b'$Revision: $'

# functions

def slansvd(jobu, jobv, m, n, k, aprod, u, v, tolin, work, iwork, doption, ioption, dparm, iparm, kmax=None, ldu=None, ldv=None, lwork=None, liwork=None, aprod_extra_args=None): # real signature unknown; restored from __doc__
    """
    u,sigma,bnd,v,info = slansvd(jobu,jobv,m,n,k,aprod,u,v,tolin,work,iwork,doption,ioption,dparm,iparm,[kmax,ldu,ldv,lwork,liwork,aprod_extra_args])
    
    Wrapper for ``slansvd``.
    
    Parameters
    ----------
    jobu : input string(len=1)
    jobv : input string(len=1)
    m : input int
    n : input int
    k : input int
    aprod : call-back function => saprod
    u : input rank-2 array('f') with bounds (ldu,kmax + 1)
    v : input rank-2 array('f') with bounds (ldv,kmax)
    tolin : input float
    work : input rank-1 array('f') with bounds (lwork)
    iwork : input rank-1 array('i') with bounds (liwork)
    doption : input rank-1 array('f') with bounds (3)
    ioption : input rank-1 array('i') with bounds (2)
    dparm : input rank-1 array('f') with bounds (*)
    iparm : input rank-1 array('i') with bounds (*)
    
    Other Parameters
    ----------------
    kmax : input int, optional
        Default: (shape(u,1)-1)
    aprod_extra_args : input tuple, optional
        Default: ()
    ldu : input int, optional
        Default: shape(u,0)
    ldv : input int, optional
        Default: shape(v,0)
    lwork : input int, optional
        Default: len(work)
    liwork : input int, optional
        Default: len(iwork)
    
    Returns
    -------
    u : rank-2 array('f') with bounds (ldu,kmax + 1)
    sigma : rank-1 array('f') with bounds (k)
    bnd : rank-1 array('f') with bounds (k)
    v : rank-2 array('f') with bounds (ldv,kmax)
    info : int
    
    Notes
    -----
    Call-back functions::
    
      def saprod(transa,m,n,x,y,dparm,iparm): return saprod
      Required arguments:
        transa : input string(len=1)
        m : input int
        n : input int
        x : input rank-1 array('f') with bounds ((transa[0] == 'n' ? n : m))
        y : input rank-1 array('f') with bounds ((transa[0] == 'n' ? m : n))
        dparm : input rank-1 array('f') with bounds (*)
        iparm : input rank-1 array('i') with bounds (*)
      Return objects:
        saprod : float
    """
    pass

def slansvd_irl(which, jobu, jobv, m, n, p, neig, maxiter, aprod, u, v, tolin, work, iwork, doption, ioption, dparm, iparm, dim=None, ldu=None, ldv=None, lwork=None, liwork=None, aprod_extra_args=None): # real signature unknown; restored from __doc__
    """
    u,sigma,bnd,v,info = slansvd_irl(which,jobu,jobv,m,n,p,neig,maxiter,aprod,u,v,tolin,work,iwork,doption,ioption,dparm,iparm,[dim,ldu,ldv,lwork,liwork,aprod_extra_args])
    
    Wrapper for ``slansvd_irl``.
    
    Parameters
    ----------
    which : input string(len=1)
    jobu : input string(len=1)
    jobv : input string(len=1)
    m : input int
    n : input int
    p : input int
    neig : input int
    maxiter : input int
    aprod : call-back function => saprod
    u : input rank-2 array('f') with bounds (ldu,dim + 1)
    v : input rank-2 array('f') with bounds (ldv,dim)
    tolin : input float
    work : input rank-1 array('f') with bounds (lwork)
    iwork : input rank-1 array('i') with bounds (liwork)
    doption : input rank-1 array('f') with bounds (4)
    ioption : input rank-1 array('i') with bounds (2)
    dparm : input rank-1 array('f') with bounds (*)
    iparm : input rank-1 array('i') with bounds (*)
    
    Other Parameters
    ----------------
    dim : input int, optional
        Default: (shape(u,1)-1)
    aprod_extra_args : input tuple, optional
        Default: ()
    ldu : input int, optional
        Default: shape(u,0)
    ldv : input int, optional
        Default: shape(v,0)
    lwork : input int, optional
        Default: len(work)
    liwork : input int, optional
        Default: len(iwork)
    
    Returns
    -------
    u : rank-2 array('f') with bounds (ldu,dim + 1)
    sigma : rank-1 array('f') with bounds (neig)
    bnd : rank-1 array('f') with bounds (neig)
    v : rank-2 array('f') with bounds (ldv,dim)
    info : int
    
    Notes
    -----
    Call-back functions::
    
      def saprod(transa,m,n,x,y,dparm,iparm): return saprod
      Required arguments:
        transa : input string(len=1)
        m : input int
        n : input int
        x : input rank-1 array('f') with bounds ((transa[0] == 'n' ? n : m))
        y : input rank-1 array('f') with bounds ((transa[0] == 'n' ? m : n))
        dparm : input rank-1 array('f') with bounds (*)
        iparm : input rank-1 array('i') with bounds (*)
      Return objects:
        saprod : float
    """
    pass

def timing(*args, **kwargs): # real signature unknown
    """
    'i'-scalar
    'i'-scalar
    'i'-scalar
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
    'i'-scalar
    'f'-scalar
    'f'-scalar
    'f'-scalar
    'i'-scalar
    """
    pass

# classes

class __spropack_error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924a60>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.sparse.linalg._propack._spropack', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924a60>, origin='/.venv/lib/python3.8/site-packages/scipy/sparse/linalg/_propack/_spropack.cpython-38-aarch64-linux-gnu.so')"

