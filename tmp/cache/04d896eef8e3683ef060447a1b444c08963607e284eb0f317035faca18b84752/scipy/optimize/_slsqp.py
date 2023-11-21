# encoding: utf-8
# module scipy.optimize._slsqp
# from /.venv/lib/python3.8/site-packages/scipy/optimize/_slsqp.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
"""
This module '_slsqp' is auto-generated with f2py (version:2).
Functions:
  slsqp(m,meq,x,xl,xu,f,c,g,a,acc,iter,mode,w,jw,alpha,f0,gs,h1,h2,h3,h4,t,t0,tol,iexact,incons,ireset,itermx,line,n1,n2,n3,la=len(c),n=len(x),l_w=len(w),l_jw=len(jw))
.
"""
# no imports

# Variables with simple values

__version__ = b'$Revision: $'

# functions

def slsqp(m, meq, x, xl, xu, f, c, g, a, acc, iter, mode, w, jw, alpha, f0, gs, h1, h2, h3, h4, t, t0, tol, iexact, incons, ireset, itermx, line, n1, n2, n3, la=None, n=None, l_w=None, l_jw=None): # real signature unknown; restored from __doc__
    """
    slsqp(m,meq,x,xl,xu,f,c,g,a,acc,iter,mode,w,jw,alpha,f0,gs,h1,h2,h3,h4,t,t0,tol,iexact,incons,ireset,itermx,line,n1,n2,n3,[la,n,l_w,l_jw])
    
    Wrapper for ``slsqp``.
    
    Parameters
    ----------
    m : input int
    meq : input int
    x : in/output rank-1 array('d') with bounds (n)
    xl : input rank-1 array('d') with bounds (n)
    xu : input rank-1 array('d') with bounds (n)
    f : input float
    c : input rank-1 array('d') with bounds (la)
    g : input rank-1 array('d') with bounds (n + 1)
    a : input rank-2 array('d') with bounds (la,n + 1)
    acc : in/output rank-0 array(float,'d')
    iter : in/output rank-0 array(int,'i')
    mode : in/output rank-0 array(int,'i')
    w : input rank-1 array('d') with bounds (l_w)
    jw : input rank-1 array('i') with bounds (l_jw)
    alpha : in/output rank-0 array(float,'d')
    f0 : in/output rank-0 array(float,'d')
    gs : in/output rank-0 array(float,'d')
    h1 : in/output rank-0 array(float,'d')
    h2 : in/output rank-0 array(float,'d')
    h3 : in/output rank-0 array(float,'d')
    h4 : in/output rank-0 array(float,'d')
    t : in/output rank-0 array(float,'d')
    t0 : in/output rank-0 array(float,'d')
    tol : in/output rank-0 array(float,'d')
    iexact : in/output rank-0 array(int,'i')
    incons : in/output rank-0 array(int,'i')
    ireset : in/output rank-0 array(int,'i')
    itermx : in/output rank-0 array(int,'i')
    line : in/output rank-0 array(int,'i')
    n1 : in/output rank-0 array(int,'i')
    n2 : in/output rank-0 array(int,'i')
    n3 : in/output rank-0 array(int,'i')
    
    Other Parameters
    ----------------
    la : input int, optional
        Default: len(c)
    n : input int, optional
        Default: len(x)
    l_w : input int, optional
        Default: len(w)
    l_jw : input int, optional
        Default: len(jw)
    """
    pass

# classes

class __slsqp_error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff92aa6400>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.optimize._slsqp', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff92aa6400>, origin='/.venv/lib/python3.8/site-packages/scipy/optimize/_slsqp.cpython-38-aarch64-linux-gnu.so')"

