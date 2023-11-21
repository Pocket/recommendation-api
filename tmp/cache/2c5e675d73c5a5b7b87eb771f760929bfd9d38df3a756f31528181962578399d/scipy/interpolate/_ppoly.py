# encoding: utf-8
# module scipy.interpolate._ppoly
# from /.venv/lib/python3.8/site-packages/scipy/interpolate/_ppoly.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
"""
Routines for evaluating and manipulating piecewise polynomials in
local power basis.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /.venv/lib/python3.8/site-packages/numpy/__init__.py

# functions

def evaluate(*args, **kwargs): # real signature unknown
    """
    Evaluate a piecewise polynomial.
    
        Parameters
        ----------
        c : ndarray, shape (k, m, n)
            Coefficients local polynomials of order `k-1` in `m` intervals.
            There are `n` polynomials in each interval.
            Coefficient of highest order-term comes first.
        x : ndarray, shape (m+1,)
            Breakpoints of polynomials.
        xp : ndarray, shape (r,)
            Points to evaluate the piecewise polynomial at.
        dx : int
            Order of derivative to evaluate.  The derivative is evaluated
            piecewise and may have discontinuities.
        extrapolate : bint
            Whether to extrapolate to out-of-bounds points based on first
            and last intervals, or to return NaNs.
        out : ndarray, shape (r, n)
            Value of each polynomial at each of the input points.
            This argument is modified in-place.
    """
    pass

def evaluate_bernstein(*args, **kwargs): # real signature unknown
    """
    Evaluate a piecewise polynomial in the Bernstein basis.
    
        Parameters
        ----------
        c : ndarray, shape (k, m, n)
            Coefficients local polynomials of order `k-1` in `m` intervals.
            There are `n` polynomials in each interval.
            Coefficient of highest order-term comes first.
        x : ndarray, shape (m+1,)
            Breakpoints of polynomials
        xp : ndarray, shape (r,)
            Points to evaluate the piecewise polynomial at.
        nu : int
            Order of derivative to evaluate.  The derivative is evaluated
            piecewise and may have discontinuities.
        extrapolate : bint, optional
            Whether to extrapolate to out-of-bounds points based on first
            and last intervals, or to return NaNs.
        out : ndarray, shape (r, n)
            Value of each polynomial at each of the input points.
            This argument is modified in-place.
    """
    pass

def evaluate_nd(*args, **kwargs): # real signature unknown
    """
    Evaluate a piecewise tensor-product polynomial.
    
        Parameters
        ----------
        c : ndarray, shape (k_1*...*k_d, m_1*...*m_d, n)
            Coefficients local polynomials of order `k-1` in
            `m_1`, ..., `m_d` intervals. There are `n` polynomials
            in each interval.
        ks : ndarray of int, shape (d,)
            Orders of polynomials in each dimension
        xs : d-tuple of ndarray of shape (m_d+1,) each
            Breakpoints of polynomials
        xp : ndarray, shape (r, d)
            Points to evaluate the piecewise polynomial at.
        dx : ndarray of int, shape (d,)
            Orders of derivative to evaluate.  The derivative is evaluated
            piecewise and may have discontinuities.
        extrapolate : int, optional
            Whether to extrapolate to out-of-bounds points based on first
            and last intervals, or to return NaNs.
        out : ndarray, shape (r, n)
            Value of each polynomial at each of the input points.
            For points outside the span ``x[0] ... x[-1]``,
            ``nan`` is returned.
            This argument is modified in-place.
    """
    pass

def fix_continuity(*args, **kwargs): # real signature unknown
    """
    Make a piecewise polynomial continuously differentiable to given order.
    
        Parameters
        ----------
        c : ndarray, shape (k, m, n)
            Coefficients local polynomials of order `k-1` in `m` intervals.
            There are `n` polynomials in each interval.
            Coefficient of highest order-term comes first.
    
            Coefficients c[-order-1:] are modified in-place.
        x : ndarray, shape (m+1,)
            Breakpoints of polynomials
        order : int
            Order up to which enforce piecewise differentiability.
    """
    pass

def integrate(*args, **kwargs): # real signature unknown
    """
    Compute integral over a piecewise polynomial.
    
        Parameters
        ----------
        c : ndarray, shape (k, m, n)
            Coefficients local polynomials of order `k-1` in `m` intervals.
        x : ndarray, shape (m+1,)
            Breakpoints of polynomials
        a : double
            Start point of integration.
        b : double
            End point of integration.
        extrapolate : bint, optional
            Whether to extrapolate to out-of-bounds points based on first
            and last intervals, or to return NaNs.
        out : ndarray, shape (n,)
            Integral of the piecewise polynomial, assuming the polynomial
            is zero outside the range (x[0], x[-1]).
            This argument is modified in-place.
    """
    pass

def real_roots(*args, **kwargs): # real signature unknown
    """
    Compute real roots of a real-valued piecewise polynomial function.
    
        If a section of the piecewise polynomial is identically zero, the
        values (x[begin], nan) are appended to the root list.
    
        If the piecewise polynomial is not continuous, and the sign
        changes across a breakpoint, the breakpoint is added to the root
        set if `report_discont` is True.
    
        Parameters
        ----------
        c, x
            Polynomial coefficients, as above
        y : float
            Find roots of ``pp(x) == y``.
        report_discont : bint, optional
            Whether to report discontinuities across zero at breakpoints
            as roots
        extrapolate : bint, optional
            Whether to consider roots obtained by extrapolating based
            on first and last intervals.
    """
    pass

def _croots_poly1(*args, **kwargs): # real signature unknown
    """
    Find roots of polynomials.
    
        This function is for testing croots_poly1
    
        Parameters
        ----------
        c : ndarray, (k, m, n)
            Coefficients of several order-k polynomials
        w : ndarray, (k, m, n)
            Output argument --- roots of the polynomials.
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff925abeb0>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.interpolate._ppoly', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff925abeb0>, origin='/.venv/lib/python3.8/site-packages/scipy/interpolate/_ppoly.cpython-38-aarch64-linux-gnu.so')"

__test__ = {}

