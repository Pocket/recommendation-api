# encoding: utf-8
# module numpy.linalg._umath_linalg
# from /.venv/lib/python3.8/site-packages/numpy/linalg/_umath_linalg.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

# Variables with simple values

__version__ = '0.1.5'

# functions

def cholesky_lo(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    cholesky_lo(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])
    
    cholesky decomposition of hermitian positive-definite matrices. 
    Broadcast to all outer dimensions. 
        "(m,m)->(m,m)"
    """
    pass

def det(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    det(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])
    
    det of the last two dimensions and broadcast on the rest. 
        "(m,m)->()"
    """
    pass

def eig(x, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    eig(x[, out1, out2], / [, out=(None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])
    
    eig on the last two dimension and broadcast to the rest. 
    Results in a vector with the  eigenvalues and a matrix with the eigenvectors. 
        "(m,m)->(m),(m,m)"
    """
    pass

def eigh_lo(x, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    eigh_lo(x[, out1, out2], / [, out=(None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])
    
    eigh on the last two dimension and broadcast to the rest, using lower triangle 
    Results in a vector of eigenvalues and a matrix with theeigenvectors. 
        "(m,m)->(m),(m,m)"
    """
    pass

def eigh_up(x, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    eigh_up(x[, out1, out2], / [, out=(None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])
    
    eigh on the last two dimension and broadcast to the rest, using upper triangle. 
    Results in a vector of eigenvalues and a matrix with the eigenvectors. 
        "(m,m)->(m),(m,m)"
    """
    pass

def eigvals(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    eigvals(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])
    
    eigvals on the last two dimension and broadcast to the rest. 
    Results in a vector of eigenvalues.
    """
    pass

def eigvalsh_lo(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    eigvalsh_lo(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])
    
    eigh on the last two dimension and broadcast to the rest, using lower triangle. 
    Results in a vector of eigenvalues and a matrix with theeigenvectors. 
        "(m,m)->(m)"
    """
    pass

def eigvalsh_up(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    eigvalsh_up(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])
    
    eigvalsh on the last two dimension and broadcast to the rest, using upper triangle. 
    Results in a vector of eigenvalues and a matrix with theeigenvectors.
        "(m,m)->(m)"
    """
    pass

def inv(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    inv(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])
    
    compute the inverse of the last two dimensions and broadcast to the rest. 
    Results in the inverse matrices. 
        "(m,m)->(m,m)"
    """
    pass

def lstsq_m(x1, x2, x3, out1=None, out2=None, out3=None, out4=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    lstsq_m(x1, x2, x3[, out1, out2, out3, out4], / [, out=(None, None, None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])
    
    least squares on the last two dimensions and broadcast to the rest. 
    For m <= n.
    """
    pass

def lstsq_n(x1, x2, x3, out1=None, out2=None, out3=None, out4=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    lstsq_n(x1, x2, x3[, out1, out2, out3, out4], / [, out=(None, None, None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])
    
    least squares on the last two dimensions and broadcast to the rest. 
    For m >= n, meaning that residuals are produced.
    """
    pass

def qr_complete(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    qr_complete(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])
    
    Compute Q matrix for the last two dimensions 
    and broadcast to the rest. For m > n.
    """
    pass

def qr_reduced(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    qr_reduced(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])
    
    Compute Q matrix for the last two dimensions 
    and broadcast to the rest.
    """
    pass

def qr_r_raw_m(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    qr_r_raw_m(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])
    
    Compute TAU vector for the last two dimensions 
    and broadcast to the rest. For m <= n.
    """
    pass

def qr_r_raw_n(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    qr_r_raw_n(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])
    
    Compute TAU vector for the last two dimensions 
    and broadcast to the rest. For m > n.
    """
    pass

def slogdet(x, out1=None, out2=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    slogdet(x[, out1, out2], / [, out=(None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])
    
    slogdet on the last two dimensions and broadcast on the rest. 
    Results in two arrays, one with sign and the other with log of the determinants. 
        "(m,m)->(),()"
    """
    pass

def solve(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    solve(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])
    
    solve the system a x = b, on the last two dimensions, broadcast to the rest. 
    Results in a matrices with the solutions. 
        "(m,m),(m,n)->(m,n)"
    """
    pass

def solve1(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    solve1(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])
    
    solve the system a x = b, for b being a vector, broadcast in the outer dimensions. 
    Results in vectors with the solutions. 
        "(m,m),(m)->(m)"
    """
    pass

def svd_m(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    svd_m(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])
    
    svd when n>=m.
    """
    pass

def svd_m_f(x, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    svd_m_f(x[, out1, out2, out3], / [, out=(None, None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])
    
    svd when m<=n
    """
    pass

def svd_m_s(x, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    svd_m_s(x[, out1, out2, out3], / [, out=(None, None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])
    
    svd when m<=n
    """
    pass

def svd_n(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    svd_n(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])
    
    svd when n<=m
    """
    pass

def svd_n_f(x, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    svd_n_f(x[, out1, out2, out3], / [, out=(None, None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])
    
    svd when m>=n
    """
    pass

def svd_n_s(x, out1=None, out2=None, out3=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    svd_n_s(x[, out1, out2, out3], / [, out=(None, None, None)], *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj, axes, axis])
    
    svd when m>=n
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac173730>'

__spec__ = None # (!) real value is "ModuleSpec(name='numpy.linalg._umath_linalg', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac173730>, origin='/.venv/lib/python3.8/site-packages/numpy/linalg/_umath_linalg.cpython-38-aarch64-linux-gnu.so')"

