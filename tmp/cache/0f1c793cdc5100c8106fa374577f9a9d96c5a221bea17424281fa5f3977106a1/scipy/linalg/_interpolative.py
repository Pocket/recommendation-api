# encoding: utf-8
# module scipy.linalg._interpolative
# from /.venv/lib/python3.8/site-packages/scipy/linalg/_interpolative.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
"""
This module '_interpolative' is auto-generated with f2py (version:2).
Functions:
  r = id_srand(n)
  id_srandi(t)
  id_srando()
  y = idd_frm(n,w,x,m=len(x))
  y = idd_sfrm(l,n,w,x,m=len(x))
  n,w = idd_frmi(m)
  n,w = idd_sfrmi(l,m)
  krank,list,rnorms = iddp_id(eps,a,m=shape(a,0),n=shape(a,1))
  list,rnorms = iddr_id(a,krank,m=shape(a,0),n=shape(a,1))
  approx = idd_reconid(col,list,proj,m=shape(col,0),krank=shape(col,1),n=len(list))
  p = idd_reconint(list,proj,n=len(list),krank=shape(proj,0))
  col = idd_copycols(a,krank,list,m=shape(a,0),n=shape(a,1))
  u,v,s,ier = idd_id2svd(b,list,proj,m=shape(b,0),krank=shape(b,1),n=len(list),w=)
  snorm,v = idd_snorm(m,n,matvect,matvec,its,p1t=,p2t=,p3t=,p4t=,p1=,p2=,p3=,p4=,u=,matvect_extra_args=(),matvec_extra_args=())
  snorm = idd_diffsnorm(m,n,matvect,matvect2,matvec,matvec2,its,p1t=,p2t=,p3t=,p4t=,p1t2=,p2t2=,p3t2=,p4t2=,p1=,p2=,p3=,p4=,p12=,p22=,p32=,p42=,w=,matvect_extra_args=(),matvect2_extra_args=(),matvec_extra_args=(),matvec2_extra_args=())
  u,v,s,ier = iddr_svd(a,krank,m=shape(a,0),n=shape(a,1),r=)
  krank,iu,iv,is,w,ier = iddp_svd(eps,a,m=shape(a,0),n=shape(a,1))
  krank,list,proj = iddp_aid(eps,a,work,proj,m=shape(a,0),n=shape(a,1))
  krank,ra = idd_estrank(eps,a,w,ra,m=shape(a,0),n=shape(a,1))
  krank,iu,iv,is,w,ier = iddp_asvd(eps,a,winit,w,m=shape(a,0),n=shape(a,1))
  krank,list,proj,ier = iddp_rid(eps,m,n,matvect,proj,p1=,p2=,p3=,p4=,matvect_extra_args=())
  krank,ra,ier = idd_findrank(eps,m,n,matvect,p1=,p2=,p3=,p4=,w=,matvect_extra_args=())
  krank,iu,iv,is,w,ier = iddp_rsvd(eps,m,n,matvect,matvec,p1t=,p2t=,p3t=,p4t=,p1=,p2=,p3=,p4=,matvect_extra_args=(),matvec_extra_args=())
  list,proj = iddr_aid(a,krank,w,m=shape(a,0),n=shape(a,1))
  w = iddr_aidi(m,n,krank)
  u,v,s,ier = iddr_asvd(a,krank,w,m=shape(a,0),n=shape(a,1))
  list,proj = iddr_rid(m,n,matvect,krank,p1=,p2=,p3=,p4=,matvect_extra_args=())
  u,v,s,ier = iddr_rsvd(m,n,matvect,matvec,krank,p1t=,p2t=,p3t=,p4t=,p1=,p2=,p3=,p4=,w=,matvect_extra_args=(),matvec_extra_args=())
  y = idz_frm(n,w,x,m=len(x))
  y = idz_sfrm(l,n,w,x,m=len(x))
  n,w = idz_frmi(m)
  n,w = idz_sfrmi(l,m)
  krank,list,rnorms = idzp_id(eps,a,m=shape(a,0),n=shape(a,1))
  list,rnorms = idzr_id(a,krank,m=shape(a,0),n=shape(a,1))
  approx = idz_reconid(col,list,proj,m=shape(col,0),krank=shape(col,1),n=len(list))
  p = idz_reconint(list,proj,n=len(list),krank=shape(proj,0))
  col = idz_copycols(a,krank,list,m=shape(a,0),n=shape(a,1))
  u,v,s,ier = idz_id2svd(b,list,proj,m=shape(b,0),krank=shape(b,1),n=len(list),w=)
  snorm,v = idz_snorm(m,n,matveca,matvec,its,p1a=,p2a=,p3a=,p4a=,p1=,p2=,p3=,p4=,u=,matveca_extra_args=(),matvec_extra_args=())
  snorm = idz_diffsnorm(m,n,matveca,matveca2,matvec,matvec2,its,p1a=,p2a=,p3a=,p4a=,p1a2=,p2a2=,p3a2=,p4a2=,p1=,p2=,p3=,p4=,p12=,p22=,p32=,p42=,w=,matveca_extra_args=(),matveca2_extra_args=(),matvec_extra_args=(),matvec2_extra_args=())
  u,v,s,ier = idzr_svd(a,krank,m=shape(a,0),n=shape(a,1),r=)
  krank,iu,iv,is,w,ier = idzp_svd(eps,a,m=shape(a,0),n=shape(a,1))
  krank,list,proj = idzp_aid(eps,a,work,proj,m=shape(a,0),n=shape(a,1))
  krank,ra = idz_estrank(eps,a,w,ra,m=shape(a,0),n=shape(a,1))
  krank,iu,iv,is,w,ier = idzp_asvd(eps,a,winit,w,m=shape(a,0),n=shape(a,1))
  krank,list,proj,ier = idzp_rid(eps,m,n,matveca,proj,p1=,p2=,p3=,p4=,matveca_extra_args=())
  krank,ra,ier = idz_findrank(eps,m,n,matveca,p1=,p2=,p3=,p4=,w=,matveca_extra_args=())
  krank,iu,iv,is,w,ier = idzp_rsvd(eps,m,n,matveca,matvec,p1a=,p2a=,p3a=,p4a=,p1=,p2=,p3=,p4=,matveca_extra_args=(),matvec_extra_args=())
  list,proj = idzr_aid(a,krank,w,m=shape(a,0),n=shape(a,1))
  w = idzr_aidi(m,n,krank)
  u,v,s,ier = idzr_asvd(a,krank,w,m=shape(a,0),n=shape(a,1))
  list,proj = idzr_rid(m,n,matveca,krank,p1=,p2=,p3=,p4=,matveca_extra_args=())
  u,v,s,ier = idzr_rsvd(m,n,matveca,matvec,krank,p1a=,p2a=,p3a=,p4a=,p1=,p2=,p3=,p4=,w=,matveca_extra_args=(),matvec_extra_args=())
.
"""
# no imports

# Variables with simple values

__version__ = b'$Revision: $'

# functions

def iddp_aid(eps, a, work, proj, m=None, n=None): # real signature unknown; restored from __doc__
    """
    krank,list,proj = iddp_aid(eps,a,work,proj,[m,n])
    
    Wrapper for ``iddp_aid``.
    
    Parameters
    ----------
    eps : input float
    a : input rank-2 array('d') with bounds (m,n)
    work : input rank-1 array('d') with bounds (17 * m + 70)
    proj : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    m : input int, optional
        Default: shape(a,0)
    n : input int, optional
        Default: shape(a,1)
    
    Returns
    -------
    krank : int
    list : rank-1 array('i') with bounds (n)
    proj : rank-1 array('d') with bounds (*)
    """
    pass

def iddp_asvd(eps, a, winit, w, m=None, n=None): # real signature unknown; restored from __doc__
    """
    krank,iu,iv,is,w,ier = iddp_asvd(eps,a,winit,w,[m,n])
    
    Wrapper for ``iddp_asvd``.
    
    Parameters
    ----------
    eps : input float
    a : input rank-2 array('d') with bounds (m,n)
    winit : input rank-1 array('d') with bounds (17 * m + 70)
    w : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    m : input int, optional
        Default: shape(a,0)
    n : input int, optional
        Default: shape(a,1)
    
    Returns
    -------
    krank : int
    iu : int
    iv : int
    is : int
    w : rank-1 array('d') with bounds (*)
    ier : int
    """
    pass

def iddp_id(eps, a, m=None, n=None): # real signature unknown; restored from __doc__
    """
    krank,list,rnorms = iddp_id(eps,a,[m,n])
    
    Wrapper for ``iddp_id``.
    
    Parameters
    ----------
    eps : input float
    a : input rank-2 array('d') with bounds (m,n)
    
    Other Parameters
    ----------------
    m : input int, optional
        Default: shape(a,0)
    n : input int, optional
        Default: shape(a,1)
    
    Returns
    -------
    krank : int
    list : rank-1 array('i') with bounds (n)
    rnorms : rank-1 array('d') with bounds (n)
    """
    pass

def iddp_rid(eps, m, n, matvect, proj, p1=None, p2=None, p3=None, p4=None, matvect_extra_args=None): # real signature unknown; restored from __doc__
    """
    krank,list,proj,ier = iddp_rid(eps,m,n,matvect,proj,[p1,p2,p3,p4,matvect_extra_args])
    
    Wrapper for ``iddp_rid``.
    
    Parameters
    ----------
    eps : input float
    m : input int
    n : input int
    matvect : call-back function
    proj : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    matvect_extra_args : input tuple, optional
        Default: ()
    p1 : input float
    p2 : input float
    p3 : input float
    p4 : input float
    
    Returns
    -------
    krank : int
    list : rank-1 array('i') with bounds (n)
    proj : rank-1 array('d') with bounds (*)
    ier : int
    
    Notes
    -----
    Call-back functions::
    
      def matvect(x,[m,n,p1,p2,p3,p4]): return y
      Required arguments:
        x : input rank-1 array('d') with bounds (m)
      Optional arguments:
        m : input int, optional
        Default: len(x)
        n : input int
        p1 : input float
        p2 : input float
        p3 : input float
        p4 : input float
      Return objects:
        y : rank-1 array('d') with bounds (n)
    """
    pass

def iddp_rsvd(eps, m, n, matvect, matvec, p1t=None, p2t=None, p3t=None, p4t=None, p1=None, p2=None, p3=None, p4=None, matvect_extra_args=None, matvec_extra_args=None): # real signature unknown; restored from __doc__
    """
    krank,iu,iv,is,w,ier = iddp_rsvd(eps,m,n,matvect,matvec,[p1t,p2t,p3t,p4t,p1,p2,p3,p4,matvect_extra_args,matvec_extra_args])
    
    Wrapper for ``iddp_rsvd``.
    
    Parameters
    ----------
    eps : input float
    m : input int
    n : input int
    matvect : call-back function
    matvec : call-back function
    
    Other Parameters
    ----------------
    matvect_extra_args : input tuple, optional
        Default: ()
    p1t : input float
    p2t : input float
    p3t : input float
    p4t : input float
    matvec_extra_args : input tuple, optional
        Default: ()
    p1 : input float
    p2 : input float
    p3 : input float
    p4 : input float
    
    Returns
    -------
    krank : int
    iu : int
    iv : int
    is : int
    w : rank-1 array('d') with bounds ((min(m,n)+1)*(3*m+5*n+1)+25*pow(min(m,n),2))
    ier : int
    
    Notes
    -----
    Call-back functions::
    
      def matvect(x,[m,n,p1,p2,p3,p4]): return y
      Required arguments:
        x : input rank-1 array('d') with bounds (m)
      Optional arguments:
        m : input int, optional
        Default: len(x)
        n : input int
        p1 : input float
        p2 : input float
        p3 : input float
        p4 : input float
      Return objects:
        y : rank-1 array('d') with bounds (n)
      def matvec(x,[n,m,p1,p2,p3,p4]): return y
      Required arguments:
        x : input rank-1 array('d') with bounds (n)
      Optional arguments:
        n : input int, optional
        Default: len(x)
        m : input int
        p1 : input float
        p2 : input float
        p3 : input float
        p4 : input float
      Return objects:
        y : rank-1 array('d') with bounds (m)
    """
    pass

def iddp_svd(eps, a, m=None, n=None): # real signature unknown; restored from __doc__
    """
    krank,iu,iv,is,w,ier = iddp_svd(eps,a,[m,n])
    
    Wrapper for ``iddp_svd``.
    
    Parameters
    ----------
    eps : input float
    a : input rank-2 array('d') with bounds (m,n)
    
    Other Parameters
    ----------------
    m : input int, optional
        Default: shape(a,0)
    n : input int, optional
        Default: shape(a,1)
    
    Returns
    -------
    krank : int
    iu : int
    iv : int
    is : int
    w : rank-1 array('d') with bounds ((min(m,n)+1)*(m+2*n+9)+8*min(m,n)+15*pow(min(m,n),2))
    ier : int
    """
    pass

def iddr_aid(a, krank, w, m=None, n=None): # real signature unknown; restored from __doc__
    """
    list,proj = iddr_aid(a,krank,w,[m,n])
    
    Wrapper for ``iddr_aid``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (m,n)
    krank : input int
    w : input rank-1 array('d') with bounds ((2*krank+17)*n+27*m+100)
    
    Other Parameters
    ----------------
    m : input int, optional
        Default: shape(a,0)
    n : input int, optional
        Default: shape(a,1)
    
    Returns
    -------
    list : rank-1 array('i') with bounds (n)
    proj : rank-1 array('d') with bounds (max(krank*(n-krank),1))
    """
    pass

def iddr_aidi(m, n, krank): # real signature unknown; restored from __doc__
    """
    w = iddr_aidi(m,n,krank)
    
    Wrapper for ``iddr_aidi``.
    
    Parameters
    ----------
    m : input int
    n : input int
    krank : input int
    
    Returns
    -------
    w : rank-1 array('d') with bounds ((2*krank+17)*n+27*m+100)
    """
    pass

def iddr_asvd(a, krank, w, m=None, n=None): # real signature unknown; restored from __doc__
    """
    u,v,s,ier = iddr_asvd(a,krank,w,[m,n])
    
    Wrapper for ``iddr_asvd``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (m,n)
    krank : input int
    w : input rank-1 array('d') with bounds ((2*krank+28)*m+(6*krank+21)*n+25*pow(krank,2)+100)
    
    Other Parameters
    ----------------
    m : input int, optional
        Default: shape(a,0)
    n : input int, optional
        Default: shape(a,1)
    
    Returns
    -------
    u : rank-2 array('d') with bounds (m,krank)
    v : rank-2 array('d') with bounds (n,krank)
    s : rank-1 array('d') with bounds (krank)
    ier : int
    """
    pass

def iddr_id(a, krank, m=None, n=None): # real signature unknown; restored from __doc__
    """
    list,rnorms = iddr_id(a,krank,[m,n])
    
    Wrapper for ``iddr_id``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (m,n)
    krank : input int
    
    Other Parameters
    ----------------
    m : input int, optional
        Default: shape(a,0)
    n : input int, optional
        Default: shape(a,1)
    
    Returns
    -------
    list : rank-1 array('i') with bounds (n)
    rnorms : rank-1 array('d') with bounds (n)
    """
    pass

def iddr_rid(m, n, matvect, krank, p1=None, p2=None, p3=None, p4=None, matvect_extra_args=None): # real signature unknown; restored from __doc__
    """
    list,proj = iddr_rid(m,n,matvect,krank,[p1,p2,p3,p4,matvect_extra_args])
    
    Wrapper for ``iddr_rid``.
    
    Parameters
    ----------
    m : input int
    n : input int
    matvect : call-back function
    krank : input int
    
    Other Parameters
    ----------------
    matvect_extra_args : input tuple, optional
        Default: ()
    p1 : input float
    p2 : input float
    p3 : input float
    p4 : input float
    
    Returns
    -------
    list : rank-1 array('i') with bounds (n)
    proj : rank-1 array('d') with bounds (m+(krank+3)*n)
    
    Notes
    -----
    Call-back functions::
    
      def matvect(x,[m,n,p1,p2,p3,p4]): return y
      Required arguments:
        x : input rank-1 array('d') with bounds (m)
      Optional arguments:
        m : input int, optional
        Default: len(x)
        n : input int
        p1 : input float
        p2 : input float
        p3 : input float
        p4 : input float
      Return objects:
        y : rank-1 array('d') with bounds (n)
    """
    pass

def iddr_rsvd(m, n, matvect, matvec, krank, p1t=None, p2t=None, p3t=None, p4t=None, p1=None, p2=None, p3=None, p4=None, w=None, matvect_extra_args=None, matvec_extra_args=None): # real signature unknown; restored from __doc__
    """
    u,v,s,ier = iddr_rsvd(m,n,matvect,matvec,krank,[p1t,p2t,p3t,p4t,p1,p2,p3,p4,w,matvect_extra_args,matvec_extra_args])
    
    Wrapper for ``iddr_rsvd``.
    
    Parameters
    ----------
    m : input int
    n : input int
    matvect : call-back function
    matvec : call-back function
    krank : input int
    
    Other Parameters
    ----------------
    matvect_extra_args : input tuple, optional
        Default: ()
    p1t : input float
    p2t : input float
    p3t : input float
    p4t : input float
    matvec_extra_args : input tuple, optional
        Default: ()
    p1 : input float
    p2 : input float
    p3 : input float
    p4 : input float
    w : input rank-1 array('d') with bounds ((krank+1)*(2*m+4*n)+25*pow(krank,2))
    
    Returns
    -------
    u : rank-2 array('d') with bounds (m,krank)
    v : rank-2 array('d') with bounds (n,krank)
    s : rank-1 array('d') with bounds (krank)
    ier : int
    
    Notes
    -----
    Call-back functions::
    
      def matvect(x,[m,n,p1,p2,p3,p4]): return y
      Required arguments:
        x : input rank-1 array('d') with bounds (m)
      Optional arguments:
        m : input int, optional
        Default: len(x)
        n : input int
        p1 : input float
        p2 : input float
        p3 : input float
        p4 : input float
      Return objects:
        y : rank-1 array('d') with bounds (n)
      def matvec(x,[n,m,p1,p2,p3,p4]): return y
      Required arguments:
        x : input rank-1 array('d') with bounds (n)
      Optional arguments:
        n : input int, optional
        Default: len(x)
        m : input int
        p1 : input float
        p2 : input float
        p3 : input float
        p4 : input float
      Return objects:
        y : rank-1 array('d') with bounds (m)
    """
    pass

def iddr_svd(a, krank, m=None, n=None, r=None): # real signature unknown; restored from __doc__
    """
    u,v,s,ier = iddr_svd(a,krank,[m,n,r])
    
    Wrapper for ``iddr_svd``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (m,n)
    krank : input int
    
    Other Parameters
    ----------------
    m : input int, optional
        Default: shape(a,0)
    n : input int, optional
        Default: shape(a,1)
    r : input rank-1 array('d') with bounds ((krank+2)*n+8*min(m,n)+15*pow(krank,2)+8*krank)
    
    Returns
    -------
    u : rank-2 array('d') with bounds (m,krank)
    v : rank-2 array('d') with bounds (n,krank)
    s : rank-1 array('d') with bounds (krank)
    ier : int
    """
    pass

def idd_copycols(a, krank, p_list, m=None, n=None): # real signature unknown; restored from __doc__
    """
    col = idd_copycols(a,krank,list,[m,n])
    
    Wrapper for ``idd_copycols``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (m,n)
    krank : input int
    list : input rank-1 array('i') with bounds (*)
    
    Other Parameters
    ----------------
    m : input int, optional
        Default: shape(a,0)
    n : input int, optional
        Default: shape(a,1)
    
    Returns
    -------
    col : rank-2 array('d') with bounds (m,krank)
    """
    pass

def idd_diffsnorm(m, n, matvect, matvect2, matvec, matvec2, its, p1t=None, p2t=None, p3t=None, p4t=None, p1t2=None, p2t2=None, p3t2=None, p4t2=None, p1=None, p2=None, p3=None, p4=None, p12=None, p22=None, p32=None, p42=None, w=None, matvect_extra_args=None, matvect2_extra_args=None, matvec_extra_args=None, matvec2_extra_args=None): # real signature unknown; restored from __doc__
    """
    snorm = idd_diffsnorm(m,n,matvect,matvect2,matvec,matvec2,its,[p1t,p2t,p3t,p4t,p1t2,p2t2,p3t2,p4t2,p1,p2,p3,p4,p12,p22,p32,p42,w,matvect_extra_args,matvect2_extra_args,matvec_extra_args,matvec2_extra_args])
    
    Wrapper for ``idd_diffsnorm``.
    
    Parameters
    ----------
    m : input int
    n : input int
    matvect : call-back function
    matvect2 : call-back function
    matvec : call-back function
    matvec2 : call-back function
    its : input int
    
    Other Parameters
    ----------------
    matvect_extra_args : input tuple, optional
        Default: ()
    p1t : input float
    p2t : input float
    p3t : input float
    p4t : input float
    matvect2_extra_args : input tuple, optional
        Default: ()
    p1t2 : input float
    p2t2 : input float
    p3t2 : input float
    p4t2 : input float
    matvec_extra_args : input tuple, optional
        Default: ()
    p1 : input float
    p2 : input float
    p3 : input float
    p4 : input float
    matvec2_extra_args : input tuple, optional
        Default: ()
    p12 : input float
    p22 : input float
    p32 : input float
    p42 : input float
    w : input rank-1 array('d') with bounds (3*(m+n))
    
    Returns
    -------
    snorm : float
    
    Notes
    -----
    Call-back functions::
    
      def matvect(x,[m,n,p1,p2,p3,p4]): return y
      Required arguments:
        x : input rank-1 array('d') with bounds (m)
      Optional arguments:
        m : input int, optional
        Default: len(x)
        n : input int
        p1 : input float
        p2 : input float
        p3 : input float
        p4 : input float
      Return objects:
        y : rank-1 array('d') with bounds (n)
      def matvect2(x,[m,n,p1,p2,p3,p4]): return y
      Required arguments:
        x : input rank-1 array('d') with bounds (m)
      Optional arguments:
        m : input int, optional
        Default: len(x)
        n : input int
        p1 : input float
        p2 : input float
        p3 : input float
        p4 : input float
      Return objects:
        y : rank-1 array('d') with bounds (n)
      def matvec(x,[n,m,p1,p2,p3,p4]): return y
      Required arguments:
        x : input rank-1 array('d') with bounds (n)
      Optional arguments:
        n : input int, optional
        Default: len(x)
        m : input int
        p1 : input float
        p2 : input float
        p3 : input float
        p4 : input float
      Return objects:
        y : rank-1 array('d') with bounds (m)
      def matvec2(x,[n,m,p1,p2,p3,p4]): return y
      Required arguments:
        x : input rank-1 array('d') with bounds (n)
      Optional arguments:
        n : input int, optional
        Default: len(x)
        m : input int
        p1 : input float
        p2 : input float
        p3 : input float
        p4 : input float
      Return objects:
        y : rank-1 array('d') with bounds (m)
    """
    pass

def idd_estrank(eps, a, w, ra, m=None, n=None): # real signature unknown; restored from __doc__
    """
    krank,ra = idd_estrank(eps,a,w,ra,[m,n])
    
    Wrapper for ``idd_estrank``.
    
    Parameters
    ----------
    eps : input float
    a : input rank-2 array('d') with bounds (m,n)
    w : input rank-1 array('d') with bounds (17 * m + 70)
    ra : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    m : input int, optional
        Default: shape(a,0)
    n : input int, optional
        Default: shape(a,1)
    
    Returns
    -------
    krank : int
    ra : rank-1 array('d') with bounds (*)
    """
    pass

def idd_findrank(eps, m, n, matvect, p1=None, p2=None, p3=None, p4=None, w=None, matvect_extra_args=None): # real signature unknown; restored from __doc__
    """
    krank,ra,ier = idd_findrank(eps,m,n,matvect,[p1,p2,p3,p4,w,matvect_extra_args])
    
    Wrapper for ``idd_findrank``.
    
    Parameters
    ----------
    eps : input float
    m : input int
    n : input int
    matvect : call-back function
    
    Other Parameters
    ----------------
    matvect_extra_args : input tuple, optional
        Default: ()
    p1 : input float
    p2 : input float
    p3 : input float
    p4 : input float
    w : input rank-1 array('d') with bounds (m+2*n+1)
    
    Returns
    -------
    krank : int
    ra : rank-1 array('d') with bounds (2*n*min(m,n))
    ier : int
    
    Notes
    -----
    Call-back functions::
    
      def matvect(x,[m,n,p1,p2,p3,p4]): return y
      Required arguments:
        x : input rank-1 array('d') with bounds (m)
      Optional arguments:
        m : input int, optional
        Default: len(x)
        n : input int
        p1 : input float
        p2 : input float
        p3 : input float
        p4 : input float
      Return objects:
        y : rank-1 array('d') with bounds (n)
    """
    pass

def idd_frm(n, w, x, m=None): # real signature unknown; restored from __doc__
    """
    y = idd_frm(n,w,x,[m])
    
    Wrapper for ``idd_frm``.
    
    Parameters
    ----------
    n : input int
    w : input rank-1 array('d') with bounds (17 * m + 70)
    x : input rank-1 array('d') with bounds (m)
    
    Other Parameters
    ----------------
    m : input int, optional
        Default: len(x)
    
    Returns
    -------
    y : rank-1 array('d') with bounds (n)
    """
    pass

def idd_frmi(m): # real signature unknown; restored from __doc__
    """
    n,w = idd_frmi(m)
    
    Wrapper for ``idd_frmi``.
    
    Parameters
    ----------
    m : input int
    
    Returns
    -------
    n : int
    w : rank-1 array('d') with bounds (17 * m + 70)
    """
    pass

def idd_id2svd(b, p_list, proj, m=None, krank=None, n=None, w=None): # real signature unknown; restored from __doc__
    """
    u,v,s,ier = idd_id2svd(b,list,proj,[m,krank,n,w])
    
    Wrapper for ``idd_id2svd``.
    
    Parameters
    ----------
    b : input rank-2 array('d') with bounds (m,krank)
    list : input rank-1 array('i') with bounds (n)
    proj : input rank-2 array('d') with bounds (krank,n-krank)
    
    Other Parameters
    ----------------
    m : input int, optional
        Default: shape(b,0)
    krank : input int, optional
        Default: shape(b,1)
    n : input int, optional
        Default: len(list)
    w : input rank-1 array('d') with bounds ((krank+1)*(m+3*n)+26*pow(krank,2))
    
    Returns
    -------
    u : rank-2 array('d') with bounds (m,krank)
    v : rank-2 array('d') with bounds (n,krank)
    s : rank-1 array('d') with bounds (krank)
    ier : int
    """
    pass

def idd_reconid(col, p_list, proj, m=None, krank=None, n=None): # real signature unknown; restored from __doc__
    """
    approx = idd_reconid(col,list,proj,[m,krank,n])
    
    Wrapper for ``idd_reconid``.
    
    Parameters
    ----------
    col : input rank-2 array('d') with bounds (m,krank)
    list : input rank-1 array('i') with bounds (n)
    proj : input rank-2 array('d') with bounds (krank,n-krank)
    
    Other Parameters
    ----------------
    m : input int, optional
        Default: shape(col,0)
    krank : input int, optional
        Default: shape(col,1)
    n : input int, optional
        Default: len(list)
    
    Returns
    -------
    approx : rank-2 array('d') with bounds (m,n)
    """
    pass

def idd_reconint(p_list, proj, n=None, krank=None): # real signature unknown; restored from __doc__
    """
    p = idd_reconint(list,proj,[n,krank])
    
    Wrapper for ``idd_reconint``.
    
    Parameters
    ----------
    list : input rank-1 array('i') with bounds (n)
    proj : input rank-2 array('d') with bounds (krank,n-krank)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: len(list)
    krank : input int, optional
        Default: shape(proj,0)
    
    Returns
    -------
    p : rank-2 array('d') with bounds (krank,n)
    """
    pass

def idd_sfrm(l, n, w, x, m=None): # real signature unknown; restored from __doc__
    """
    y = idd_sfrm(l,n,w,x,[m])
    
    Wrapper for ``idd_sfrm``.
    
    Parameters
    ----------
    l : input int
    n : input int
    w : input rank-1 array('d') with bounds (27 * m + 90)
    x : input rank-1 array('d') with bounds (m)
    
    Other Parameters
    ----------------
    m : input int, optional
        Default: len(x)
    
    Returns
    -------
    y : rank-1 array('d') with bounds (l)
    """
    pass

def idd_sfrmi(l, m): # real signature unknown; restored from __doc__
    """
    n,w = idd_sfrmi(l,m)
    
    Wrapper for ``idd_sfrmi``.
    
    Parameters
    ----------
    l : input int
    m : input int
    
    Returns
    -------
    n : int
    w : rank-1 array('d') with bounds (27 * m + 90)
    """
    pass

def idd_snorm(m, n, matvect, matvec, its, p1t=None, p2t=None, p3t=None, p4t=None, p1=None, p2=None, p3=None, p4=None, u=None, matvect_extra_args=None, matvec_extra_args=None): # real signature unknown; restored from __doc__
    """
    snorm,v = idd_snorm(m,n,matvect,matvec,its,[p1t,p2t,p3t,p4t,p1,p2,p3,p4,u,matvect_extra_args,matvec_extra_args])
    
    Wrapper for ``idd_snorm``.
    
    Parameters
    ----------
    m : input int
    n : input int
    matvect : call-back function
    matvec : call-back function
    its : input int
    
    Other Parameters
    ----------------
    matvect_extra_args : input tuple, optional
        Default: ()
    p1t : input float
    p2t : input float
    p3t : input float
    p4t : input float
    matvec_extra_args : input tuple, optional
        Default: ()
    p1 : input float
    p2 : input float
    p3 : input float
    p4 : input float
    u : input rank-1 array('d') with bounds (m)
    
    Returns
    -------
    snorm : float
    v : rank-1 array('d') with bounds (n)
    
    Notes
    -----
    Call-back functions::
    
      def matvect(x,[m,n,p1,p2,p3,p4]): return y
      Required arguments:
        x : input rank-1 array('d') with bounds (m)
      Optional arguments:
        m : input int, optional
        Default: len(x)
        n : input int
        p1 : input float
        p2 : input float
        p3 : input float
        p4 : input float
      Return objects:
        y : rank-1 array('d') with bounds (n)
      def matvec(x,[n,m,p1,p2,p3,p4]): return y
      Required arguments:
        x : input rank-1 array('d') with bounds (n)
      Optional arguments:
        n : input int, optional
        Default: len(x)
        m : input int
        p1 : input float
        p2 : input float
        p3 : input float
        p4 : input float
      Return objects:
        y : rank-1 array('d') with bounds (m)
    """
    pass

def idzp_aid(eps, a, work, proj, m=None, n=None): # real signature unknown; restored from __doc__
    """
    krank,list,proj = idzp_aid(eps,a,work,proj,[m,n])
    
    Wrapper for ``idzp_aid``.
    
    Parameters
    ----------
    eps : input float
    a : input rank-2 array('D') with bounds (m,n)
    work : input rank-1 array('D') with bounds (17 * m + 70)
    proj : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    m : input int, optional
        Default: shape(a,0)
    n : input int, optional
        Default: shape(a,1)
    
    Returns
    -------
    krank : int
    list : rank-1 array('i') with bounds (n)
    proj : rank-1 array('D') with bounds (*)
    """
    pass

def idzp_asvd(eps, a, winit, w, m=None, n=None): # real signature unknown; restored from __doc__
    """
    krank,iu,iv,is,w,ier = idzp_asvd(eps,a,winit,w,[m,n])
    
    Wrapper for ``idzp_asvd``.
    
    Parameters
    ----------
    eps : input float
    a : input rank-2 array('D') with bounds (m,n)
    winit : input rank-1 array('D') with bounds (17 * m + 70)
    w : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    m : input int, optional
        Default: shape(a,0)
    n : input int, optional
        Default: shape(a,1)
    
    Returns
    -------
    krank : int
    iu : int
    iv : int
    is : int
    w : rank-1 array('D') with bounds (*)
    ier : int
    """
    pass

def idzp_id(eps, a, m=None, n=None): # real signature unknown; restored from __doc__
    """
    krank,list,rnorms = idzp_id(eps,a,[m,n])
    
    Wrapper for ``idzp_id``.
    
    Parameters
    ----------
    eps : input float
    a : input rank-2 array('D') with bounds (m,n)
    
    Other Parameters
    ----------------
    m : input int, optional
        Default: shape(a,0)
    n : input int, optional
        Default: shape(a,1)
    
    Returns
    -------
    krank : int
    list : rank-1 array('i') with bounds (n)
    rnorms : rank-1 array('d') with bounds (n)
    """
    pass

def idzp_rid(eps, m, n, matveca, proj, p1=None, p2=None, p3=None, p4=None, matveca_extra_args=None): # real signature unknown; restored from __doc__
    """
    krank,list,proj,ier = idzp_rid(eps,m,n,matveca,proj,[p1,p2,p3,p4,matveca_extra_args])
    
    Wrapper for ``idzp_rid``.
    
    Parameters
    ----------
    eps : input float
    m : input int
    n : input int
    matveca : call-back function
    proj : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    matveca_extra_args : input tuple, optional
        Default: ()
    p1 : input complex
    p2 : input complex
    p3 : input complex
    p4 : input complex
    
    Returns
    -------
    krank : int
    list : rank-1 array('i') with bounds (n)
    proj : rank-1 array('D') with bounds (*)
    ier : int
    
    Notes
    -----
    Call-back functions::
    
      def matveca(x,[m,n,p1,p2,p3,p4]): return y
      Required arguments:
        x : input rank-1 array('D') with bounds (m)
      Optional arguments:
        m : input int, optional
        Default: len(x)
        n : input int
        p1 : input complex
        p2 : input complex
        p3 : input complex
        p4 : input complex
      Return objects:
        y : rank-1 array('D') with bounds (n)
    """
    pass

def idzp_rsvd(eps, m, n, matveca, matvec, p1a=None, p2a=None, p3a=None, p4a=None, p1=None, p2=None, p3=None, p4=None, matveca_extra_args=None, matvec_extra_args=None): # real signature unknown; restored from __doc__
    """
    krank,iu,iv,is,w,ier = idzp_rsvd(eps,m,n,matveca,matvec,[p1a,p2a,p3a,p4a,p1,p2,p3,p4,matveca_extra_args,matvec_extra_args])
    
    Wrapper for ``idzp_rsvd``.
    
    Parameters
    ----------
    eps : input float
    m : input int
    n : input int
    matveca : call-back function
    matvec : call-back function
    
    Other Parameters
    ----------------
    matveca_extra_args : input tuple, optional
        Default: ()
    p1a : input complex
    p2a : input complex
    p3a : input complex
    p4a : input complex
    matvec_extra_args : input tuple, optional
        Default: ()
    p1 : input complex
    p2 : input complex
    p3 : input complex
    p4 : input complex
    
    Returns
    -------
    krank : int
    iu : int
    iv : int
    is : int
    w : rank-1 array('D') with bounds ((min(m,n)+1)*(3*m+5*n+11)+8*pow(min(m,n),2))
    ier : int
    
    Notes
    -----
    Call-back functions::
    
      def matveca(x,[m,n,p1,p2,p3,p4]): return y
      Required arguments:
        x : input rank-1 array('D') with bounds (m)
      Optional arguments:
        m : input int, optional
        Default: len(x)
        n : input int
        p1 : input complex
        p2 : input complex
        p3 : input complex
        p4 : input complex
      Return objects:
        y : rank-1 array('D') with bounds (n)
      def matvec(x,[n,m,p1,p2,p3,p4]): return y
      Required arguments:
        x : input rank-1 array('D') with bounds (n)
      Optional arguments:
        n : input int, optional
        Default: len(x)
        m : input int
        p1 : input complex
        p2 : input complex
        p3 : input complex
        p4 : input complex
      Return objects:
        y : rank-1 array('D') with bounds (m)
    """
    pass

def idzp_svd(eps, a, m=None, n=None): # real signature unknown; restored from __doc__
    """
    krank,iu,iv,is,w,ier = idzp_svd(eps,a,[m,n])
    
    Wrapper for ``idzp_svd``.
    
    Parameters
    ----------
    eps : input float
    a : input rank-2 array('D') with bounds (m,n)
    
    Other Parameters
    ----------------
    m : input int, optional
        Default: shape(a,0)
    n : input int, optional
        Default: shape(a,1)
    
    Returns
    -------
    krank : int
    iu : int
    iv : int
    is : int
    w : rank-1 array('D') with bounds ((min(m,n)+1)*(m+2*n+9)+8*min(m,n)+6*pow(min(m,n),2))
    ier : int
    """
    pass

def idzr_aid(a, krank, w, m=None, n=None): # real signature unknown; restored from __doc__
    """
    list,proj = idzr_aid(a,krank,w,[m,n])
    
    Wrapper for ``idzr_aid``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (m,n)
    krank : input int
    w : input rank-1 array('D') with bounds ((2*krank+17)*n+21*m+80)
    
    Other Parameters
    ----------------
    m : input int, optional
        Default: shape(a,0)
    n : input int, optional
        Default: shape(a,1)
    
    Returns
    -------
    list : rank-1 array('i') with bounds (n)
    proj : rank-1 array('D') with bounds (max(krank*(n-krank),1))
    """
    pass

def idzr_aidi(m, n, krank): # real signature unknown; restored from __doc__
    """
    w = idzr_aidi(m,n,krank)
    
    Wrapper for ``idzr_aidi``.
    
    Parameters
    ----------
    m : input int
    n : input int
    krank : input int
    
    Returns
    -------
    w : rank-1 array('D') with bounds ((2*krank+17)*n+21*m+80)
    """
    pass

def idzr_asvd(a, krank, w, m=None, n=None): # real signature unknown; restored from __doc__
    """
    u,v,s,ier = idzr_asvd(a,krank,w,[m,n])
    
    Wrapper for ``idzr_asvd``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (m,n)
    krank : input int
    w : input rank-1 array('D') with bounds ((2*krank+22)*m+(6*krank+21)*n+8*pow(krank,2)+10*krank+90)
    
    Other Parameters
    ----------------
    m : input int, optional
        Default: shape(a,0)
    n : input int, optional
        Default: shape(a,1)
    
    Returns
    -------
    u : rank-2 array('D') with bounds (m,krank)
    v : rank-2 array('D') with bounds (n,krank)
    s : rank-1 array('d') with bounds (krank)
    ier : int
    """
    pass

def idzr_id(a, krank, m=None, n=None): # real signature unknown; restored from __doc__
    """
    list,rnorms = idzr_id(a,krank,[m,n])
    
    Wrapper for ``idzr_id``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (m,n)
    krank : input int
    
    Other Parameters
    ----------------
    m : input int, optional
        Default: shape(a,0)
    n : input int, optional
        Default: shape(a,1)
    
    Returns
    -------
    list : rank-1 array('i') with bounds (n)
    rnorms : rank-1 array('d') with bounds (n)
    """
    pass

def idzr_rid(m, n, matveca, krank, p1=None, p2=None, p3=None, p4=None, matveca_extra_args=None): # real signature unknown; restored from __doc__
    """
    list,proj = idzr_rid(m,n,matveca,krank,[p1,p2,p3,p4,matveca_extra_args])
    
    Wrapper for ``idzr_rid``.
    
    Parameters
    ----------
    m : input int
    n : input int
    matveca : call-back function
    krank : input int
    
    Other Parameters
    ----------------
    matveca_extra_args : input tuple, optional
        Default: ()
    p1 : input complex
    p2 : input complex
    p3 : input complex
    p4 : input complex
    
    Returns
    -------
    list : rank-1 array('i') with bounds (n)
    proj : rank-1 array('D') with bounds (m+(krank+3)*n)
    
    Notes
    -----
    Call-back functions::
    
      def matveca(x,[m,n,p1,p2,p3,p4]): return y
      Required arguments:
        x : input rank-1 array('D') with bounds (m)
      Optional arguments:
        m : input int, optional
        Default: len(x)
        n : input int
        p1 : input complex
        p2 : input complex
        p3 : input complex
        p4 : input complex
      Return objects:
        y : rank-1 array('D') with bounds (n)
    """
    pass

def idzr_rsvd(m, n, matveca, matvec, krank, p1a=None, p2a=None, p3a=None, p4a=None, p1=None, p2=None, p3=None, p4=None, w=None, matveca_extra_args=None, matvec_extra_args=None): # real signature unknown; restored from __doc__
    """
    u,v,s,ier = idzr_rsvd(m,n,matveca,matvec,krank,[p1a,p2a,p3a,p4a,p1,p2,p3,p4,w,matveca_extra_args,matvec_extra_args])
    
    Wrapper for ``idzr_rsvd``.
    
    Parameters
    ----------
    m : input int
    n : input int
    matveca : call-back function
    matvec : call-back function
    krank : input int
    
    Other Parameters
    ----------------
    matveca_extra_args : input tuple, optional
        Default: ()
    p1a : input complex
    p2a : input complex
    p3a : input complex
    p4a : input complex
    matvec_extra_args : input tuple, optional
        Default: ()
    p1 : input complex
    p2 : input complex
    p3 : input complex
    p4 : input complex
    w : input rank-1 array('D') with bounds ((krank+1)*(2*m+4*n+10)+8*pow(krank,2))
    
    Returns
    -------
    u : rank-2 array('D') with bounds (m,krank)
    v : rank-2 array('D') with bounds (n,krank)
    s : rank-1 array('d') with bounds (krank)
    ier : int
    
    Notes
    -----
    Call-back functions::
    
      def matveca(x,[m,n,p1,p2,p3,p4]): return y
      Required arguments:
        x : input rank-1 array('D') with bounds (m)
      Optional arguments:
        m : input int, optional
        Default: len(x)
        n : input int
        p1 : input complex
        p2 : input complex
        p3 : input complex
        p4 : input complex
      Return objects:
        y : rank-1 array('D') with bounds (n)
      def matvec(x,[n,m,p1,p2,p3,p4]): return y
      Required arguments:
        x : input rank-1 array('D') with bounds (n)
      Optional arguments:
        n : input int, optional
        Default: len(x)
        m : input int
        p1 : input complex
        p2 : input complex
        p3 : input complex
        p4 : input complex
      Return objects:
        y : rank-1 array('D') with bounds (m)
    """
    pass

def idzr_svd(a, krank, m=None, n=None, r=None): # real signature unknown; restored from __doc__
    """
    u,v,s,ier = idzr_svd(a,krank,[m,n,r])
    
    Wrapper for ``idzr_svd``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (m,n)
    krank : input int
    
    Other Parameters
    ----------------
    m : input int, optional
        Default: shape(a,0)
    n : input int, optional
        Default: shape(a,1)
    r : input rank-1 array('D') with bounds ((krank+2)*n+8*min(m,n)+6*pow(krank,2)+8*krank)
    
    Returns
    -------
    u : rank-2 array('D') with bounds (m,krank)
    v : rank-2 array('D') with bounds (n,krank)
    s : rank-1 array('d') with bounds (krank)
    ier : int
    """
    pass

def idz_copycols(a, krank, p_list, m=None, n=None): # real signature unknown; restored from __doc__
    """
    col = idz_copycols(a,krank,list,[m,n])
    
    Wrapper for ``idz_copycols``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (m,n)
    krank : input int
    list : input rank-1 array('i') with bounds (*)
    
    Other Parameters
    ----------------
    m : input int, optional
        Default: shape(a,0)
    n : input int, optional
        Default: shape(a,1)
    
    Returns
    -------
    col : rank-2 array('D') with bounds (m,krank)
    """
    pass

def idz_diffsnorm(m, n, matveca, matveca2, matvec, matvec2, its, p1a=None, p2a=None, p3a=None, p4a=None, p1a2=None, p2a2=None, p3a2=None, p4a2=None, p1=None, p2=None, p3=None, p4=None, p12=None, p22=None, p32=None, p42=None, w=None, matveca_extra_args=None, matveca2_extra_args=None, matvec_extra_args=None, matvec2_extra_args=None): # real signature unknown; restored from __doc__
    """
    snorm = idz_diffsnorm(m,n,matveca,matveca2,matvec,matvec2,its,[p1a,p2a,p3a,p4a,p1a2,p2a2,p3a2,p4a2,p1,p2,p3,p4,p12,p22,p32,p42,w,matveca_extra_args,matveca2_extra_args,matvec_extra_args,matvec2_extra_args])
    
    Wrapper for ``idz_diffsnorm``.
    
    Parameters
    ----------
    m : input int
    n : input int
    matveca : call-back function
    matveca2 : call-back function
    matvec : call-back function
    matvec2 : call-back function
    its : input int
    
    Other Parameters
    ----------------
    matveca_extra_args : input tuple, optional
        Default: ()
    p1a : input complex
    p2a : input complex
    p3a : input complex
    p4a : input complex
    matveca2_extra_args : input tuple, optional
        Default: ()
    p1a2 : input complex
    p2a2 : input complex
    p3a2 : input complex
    p4a2 : input complex
    matvec_extra_args : input tuple, optional
        Default: ()
    p1 : input complex
    p2 : input complex
    p3 : input complex
    p4 : input complex
    matvec2_extra_args : input tuple, optional
        Default: ()
    p12 : input complex
    p22 : input complex
    p32 : input complex
    p42 : input complex
    w : input rank-1 array('D') with bounds (3*(m+n))
    
    Returns
    -------
    snorm : float
    
    Notes
    -----
    Call-back functions::
    
      def matveca(x,[m,n,p1,p2,p3,p4]): return y
      Required arguments:
        x : input rank-1 array('D') with bounds (m)
      Optional arguments:
        m : input int, optional
        Default: len(x)
        n : input int
        p1 : input complex
        p2 : input complex
        p3 : input complex
        p4 : input complex
      Return objects:
        y : rank-1 array('D') with bounds (n)
      def matveca2(x,[m,n,p1,p2,p3,p4]): return y
      Required arguments:
        x : input rank-1 array('D') with bounds (m)
      Optional arguments:
        m : input int, optional
        Default: len(x)
        n : input int
        p1 : input complex
        p2 : input complex
        p3 : input complex
        p4 : input complex
      Return objects:
        y : rank-1 array('D') with bounds (n)
      def matvec(x,[n,m,p1,p2,p3,p4]): return y
      Required arguments:
        x : input rank-1 array('D') with bounds (n)
      Optional arguments:
        n : input int, optional
        Default: len(x)
        m : input int
        p1 : input complex
        p2 : input complex
        p3 : input complex
        p4 : input complex
      Return objects:
        y : rank-1 array('D') with bounds (m)
      def matvec2(x,[n,m,p1,p2,p3,p4]): return y
      Required arguments:
        x : input rank-1 array('D') with bounds (n)
      Optional arguments:
        n : input int, optional
        Default: len(x)
        m : input int
        p1 : input complex
        p2 : input complex
        p3 : input complex
        p4 : input complex
      Return objects:
        y : rank-1 array('D') with bounds (m)
    """
    pass

def idz_estrank(eps, a, w, ra, m=None, n=None): # real signature unknown; restored from __doc__
    """
    krank,ra = idz_estrank(eps,a,w,ra,[m,n])
    
    Wrapper for ``idz_estrank``.
    
    Parameters
    ----------
    eps : input float
    a : input rank-2 array('D') with bounds (m,n)
    w : input rank-1 array('D') with bounds (17 * m + 70)
    ra : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    m : input int, optional
        Default: shape(a,0)
    n : input int, optional
        Default: shape(a,1)
    
    Returns
    -------
    krank : int
    ra : rank-1 array('D') with bounds (*)
    """
    pass

def idz_findrank(eps, m, n, matveca, p1=None, p2=None, p3=None, p4=None, w=None, matveca_extra_args=None): # real signature unknown; restored from __doc__
    """
    krank,ra,ier = idz_findrank(eps,m,n,matveca,[p1,p2,p3,p4,w,matveca_extra_args])
    
    Wrapper for ``idz_findrank``.
    
    Parameters
    ----------
    eps : input float
    m : input int
    n : input int
    matveca : call-back function
    
    Other Parameters
    ----------------
    matveca_extra_args : input tuple, optional
        Default: ()
    p1 : input complex
    p2 : input complex
    p3 : input complex
    p4 : input complex
    w : input rank-1 array('D') with bounds (m+2*n+1)
    
    Returns
    -------
    krank : int
    ra : rank-1 array('D') with bounds (2*n*min(m,n))
    ier : int
    
    Notes
    -----
    Call-back functions::
    
      def matveca(x,[m,n,p1,p2,p3,p4]): return y
      Required arguments:
        x : input rank-1 array('D') with bounds (m)
      Optional arguments:
        m : input int, optional
        Default: len(x)
        n : input int
        p1 : input complex
        p2 : input complex
        p3 : input complex
        p4 : input complex
      Return objects:
        y : rank-1 array('D') with bounds (n)
    """
    pass

def idz_frm(n, w, x, m=None): # real signature unknown; restored from __doc__
    """
    y = idz_frm(n,w,x,[m])
    
    Wrapper for ``idz_frm``.
    
    Parameters
    ----------
    n : input int
    w : input rank-1 array('D') with bounds (17 * m + 70)
    x : input rank-1 array('D') with bounds (m)
    
    Other Parameters
    ----------------
    m : input int, optional
        Default: len(x)
    
    Returns
    -------
    y : rank-1 array('D') with bounds (n)
    """
    pass

def idz_frmi(m): # real signature unknown; restored from __doc__
    """
    n,w = idz_frmi(m)
    
    Wrapper for ``idz_frmi``.
    
    Parameters
    ----------
    m : input int
    
    Returns
    -------
    n : int
    w : rank-1 array('D') with bounds (17 * m + 70)
    """
    pass

def idz_id2svd(b, p_list, proj, m=None, krank=None, n=None, w=None): # real signature unknown; restored from __doc__
    """
    u,v,s,ier = idz_id2svd(b,list,proj,[m,krank,n,w])
    
    Wrapper for ``idz_id2svd``.
    
    Parameters
    ----------
    b : input rank-2 array('D') with bounds (m,krank)
    list : input rank-1 array('i') with bounds (n)
    proj : input rank-2 array('D') with bounds (krank,n-krank)
    
    Other Parameters
    ----------------
    m : input int, optional
        Default: shape(b,0)
    krank : input int, optional
        Default: shape(b,1)
    n : input int, optional
        Default: len(list)
    w : input rank-1 array('D') with bounds ((krank+1)*(m+3*n+10)+9*pow(krank,2))
    
    Returns
    -------
    u : rank-2 array('D') with bounds (m,krank)
    v : rank-2 array('D') with bounds (n,krank)
    s : rank-1 array('d') with bounds (krank)
    ier : int
    """
    pass

def idz_reconid(col, p_list, proj, m=None, krank=None, n=None): # real signature unknown; restored from __doc__
    """
    approx = idz_reconid(col,list,proj,[m,krank,n])
    
    Wrapper for ``idz_reconid``.
    
    Parameters
    ----------
    col : input rank-2 array('D') with bounds (m,krank)
    list : input rank-1 array('i') with bounds (n)
    proj : input rank-2 array('D') with bounds (krank,n-krank)
    
    Other Parameters
    ----------------
    m : input int, optional
        Default: shape(col,0)
    krank : input int, optional
        Default: shape(col,1)
    n : input int, optional
        Default: len(list)
    
    Returns
    -------
    approx : rank-2 array('D') with bounds (m,n)
    """
    pass

def idz_reconint(p_list, proj, n=None, krank=None): # real signature unknown; restored from __doc__
    """
    p = idz_reconint(list,proj,[n,krank])
    
    Wrapper for ``idz_reconint``.
    
    Parameters
    ----------
    list : input rank-1 array('i') with bounds (n)
    proj : input rank-2 array('D') with bounds (krank,n-krank)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: len(list)
    krank : input int, optional
        Default: shape(proj,0)
    
    Returns
    -------
    p : rank-2 array('D') with bounds (krank,n)
    """
    pass

def idz_sfrm(l, n, w, x, m=None): # real signature unknown; restored from __doc__
    """
    y = idz_sfrm(l,n,w,x,[m])
    
    Wrapper for ``idz_sfrm``.
    
    Parameters
    ----------
    l : input int
    n : input int
    w : input rank-1 array('D') with bounds (27 * m + 90)
    x : input rank-1 array('D') with bounds (m)
    
    Other Parameters
    ----------------
    m : input int, optional
        Default: len(x)
    
    Returns
    -------
    y : rank-1 array('D') with bounds (l)
    """
    pass

def idz_sfrmi(l, m): # real signature unknown; restored from __doc__
    """
    n,w = idz_sfrmi(l,m)
    
    Wrapper for ``idz_sfrmi``.
    
    Parameters
    ----------
    l : input int
    m : input int
    
    Returns
    -------
    n : int
    w : rank-1 array('D') with bounds (27 * m + 90)
    """
    pass

def idz_snorm(m, n, matveca, matvec, its, p1a=None, p2a=None, p3a=None, p4a=None, p1=None, p2=None, p3=None, p4=None, u=None, matveca_extra_args=None, matvec_extra_args=None): # real signature unknown; restored from __doc__
    """
    snorm,v = idz_snorm(m,n,matveca,matvec,its,[p1a,p2a,p3a,p4a,p1,p2,p3,p4,u,matveca_extra_args,matvec_extra_args])
    
    Wrapper for ``idz_snorm``.
    
    Parameters
    ----------
    m : input int
    n : input int
    matveca : call-back function
    matvec : call-back function
    its : input int
    
    Other Parameters
    ----------------
    matveca_extra_args : input tuple, optional
        Default: ()
    p1a : input complex
    p2a : input complex
    p3a : input complex
    p4a : input complex
    matvec_extra_args : input tuple, optional
        Default: ()
    p1 : input complex
    p2 : input complex
    p3 : input complex
    p4 : input complex
    u : input rank-1 array('D') with bounds (m)
    
    Returns
    -------
    snorm : float
    v : rank-1 array('D') with bounds (n)
    
    Notes
    -----
    Call-back functions::
    
      def matveca(x,[m,n,p1,p2,p3,p4]): return y
      Required arguments:
        x : input rank-1 array('D') with bounds (m)
      Optional arguments:
        m : input int, optional
        Default: len(x)
        n : input int
        p1 : input complex
        p2 : input complex
        p3 : input complex
        p4 : input complex
      Return objects:
        y : rank-1 array('D') with bounds (n)
      def matvec(x,[n,m,p1,p2,p3,p4]): return y
      Required arguments:
        x : input rank-1 array('D') with bounds (n)
      Optional arguments:
        n : input int, optional
        Default: len(x)
        m : input int
        p1 : input complex
        p2 : input complex
        p3 : input complex
        p4 : input complex
      Return objects:
        y : rank-1 array('D') with bounds (m)
    """
    pass

def id_srand(n): # real signature unknown; restored from __doc__
    """
    r = id_srand(n)
    
    Wrapper for ``id_srand``.
    
    Parameters
    ----------
    n : input int
    
    Returns
    -------
    r : rank-1 array('d') with bounds (n)
    """
    pass

def id_srandi(t): # real signature unknown; restored from __doc__
    """
    id_srandi(t)
    
    Wrapper for ``id_srandi``.
    
    Parameters
    ----------
    t : input rank-1 array('d') with bounds (55)
    """
    pass

def id_srando(): # real signature unknown; restored from __doc__
    """
    id_srando()
    
    Wrapper for ``id_srando``.
    """
    pass

# classes

class __interpolative_error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924ac0>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.linalg._interpolative', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924ac0>, origin='/.venv/lib/python3.8/site-packages/scipy/linalg/_interpolative.cpython-38-aarch64-linux-gnu.so')"

