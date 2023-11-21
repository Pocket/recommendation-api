# encoding: utf-8
# module scipy.interpolate._bspl
# from /.venv/lib/python3.8/site-packages/scipy/interpolate/_bspl.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
""" Routines for evaluating and manipulating B-splines. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /.venv/lib/python3.8/site-packages/numpy/__init__.py

# functions

def evaluate_all_bspl(t, k, x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Evaluate the ``k+1`` B-splines which are non-zero on interval ``m``.
    
        Parameters
        ----------
        t : ndarray, shape (nt + k + 1,)
            sorted 1D array of knots
        k : int
            spline order
        xval: float
            argument at which to evaluate the B-splines
        m : int
            index of the left edge of the evaluation interval, ``t[m] <= x < t[m+1]``
        nu : int, optional
            Evaluate derivatives order `nu`. Default is zero.
    
        Returns
        -------
        ndarray, shape (k+1,)
            The values of B-splines :math:`[B_{m-k}(xval), ..., B_{m}(xval)]` if
            `nu` is zero, otherwise the derivatives of order `nu`.
    
        Examples
        --------
    
        A textbook use of this sort of routine is plotting the ``k+1`` polynomial
        pieces which make up a B-spline of order `k`.
    
        Consider a cubic spline
    
        >>> k = 3
        >>> t = [0., 1., 2., 3., 4.]   # internal knots
        >>> a, b = t[0], t[-1]    # base interval is [a, b)
        >>> t = np.array([a]*k + t + [b]*k)  # add boundary knots
    
        >>> import matplotlib.pyplot as plt
        >>> xx = np.linspace(a, b, 100)
        >>> plt.plot(xx, BSpline.basis_element(t[k:-k])(xx),
        ...          lw=3, alpha=0.5, label='basis_element')
    
        Now we use slide an interval ``t[m]..t[m+1]`` along the base interval
        ``a..b`` and use `evaluate_all_bspl` to compute the restriction of
        the B-spline of interest to this interval:
    
        >>> for i in range(k+1):
        ...    x1, x2 = t[2*k - i], t[2*k - i + 1]
        ...    xx = np.linspace(x1 - 0.5, x2 + 0.5)
        ...    yy = [evaluate_all_bspl(t, k, x, 2*k - i)[i] for x in xx]
        ...    plt.plot(xx, yy, '--', label=str(i))
        ...
        >>> plt.grid(True)
        >>> plt.legend()
        >>> plt.show()
    """
    pass

def evaluate_spline(*args, **kwargs): # real signature unknown
    """
    Evaluate a spline in the B-spline basis.
    
        Parameters
        ----------
        t : ndarray, shape (n+k+1)
            knots
        c : ndarray, shape (n, m)
            B-spline coefficients
        xp : ndarray, shape (s,)
            Points to evaluate the spline at.
        nu : int
            Order of derivative to evaluate.
        extrapolate : int, optional
            Whether to extrapolate to ouf-of-bounds points, or to return NaNs.
        out : ndarray, shape (s, m)
            Computed values of the spline at each of the input points.
            This argument is modified in-place.
    """
    pass

def _colloc(*args, **kwargs): # real signature unknown
    """
    Build the B-spline collocation matrix.
    
        The collocation matrix is defined as :math:`B_{j,l} = B_l(x_j)`,
        so that row ``j`` contains all the B-splines which are non-zero
        at ``x_j``.
    
        The matrix is constructed in the LAPACK banded storage.
        Basically, for an N-by-N matrix A with ku upper diagonals and
        kl lower diagonals, the shape of the array Ab is (2*kl + ku +1, N),
        where the last kl+ku+1 rows of Ab contain the diagonals of A, and
        the first kl rows of Ab are not referenced.
        For more info see, e.g. the docs for the ``*gbsv`` routine.
    
        This routine is not supposed to be called directly, and
        does no error checking.
    
        Parameters
        ----------
        x : ndarray, shape (n,)
            sorted 1D array of x values
        t : ndarray, shape (nt + k + 1,)
            sorted 1D array of knots
        k : int
            spline order
        ab : ndarray, shape (2*kl + ku + 1, nt), F-order
            This parameter is modified in-place.
            On exit: zeroed out.
            On exit: B-spline collocation matrix in the band storage with
            ``ku`` upper diagonals and ``kl`` lower diagonals.
            Here ``kl = ku = k``.
        offset : int, optional
            skip this many rows
    """
    pass

def _handle_lhs_derivatives(*args, **kwargs): # real signature unknown
    """
    Fill in the entries of the collocation matrix corresponding to known
        derivatives at xval.
    
        The collocation matrix is in the banded storage, as prepared by _colloc.
        No error checking.
    
        Parameters
        ----------
        t : ndarray, shape (nt + k + 1,)
            knots
        k : integer
            B-spline order
        xval : float
            The value at which to evaluate the derivatives at.
        ab : ndarray, shape(2*kl + ku + 1, nt), Fortran order
            B-spline collocation matrix.
            This argument is modified *in-place*.
        kl : integer
            Number of lower diagonals of ab.
        ku : integer
            Number of upper diagonals of ab.
        deriv_ords : 1D ndarray
            Orders of derivatives known at xval
        offset : integer, optional
            Skip this many rows of the matrix ab.
    """
    pass

def _make_design_matrix(*args, **kwargs): # real signature unknown
    """
    Returns a design matrix in CSR format.
    
        Note that only indices is passed, but not indptr because indptr is already
        precomputed in the calling Python function design_matrix.
        
        Parameters
        ----------
        x : array_like, shape (n,)
            Points to evaluate the spline at.
        t : array_like, shape (nt,)
            Sorted 1D array of knots.
        k : int
            B-spline degree.
        extrapolate : bool, optional
            Whether to extrapolate to ouf-of-bounds points.
        indices : ndarray, shape (n * (k + 1),)
            Preallocated indices of the final CSR array.
    
        Returns
        -------
        data
            The data array of a CSR array of the b-spline design matrix.
            In each row all the basis elements are evaluated at the certain point
            (first row - x[0], ..., last row - x[-1]).
        
        indices
            The indices array of a CSR array of the b-spline design matrix.
    """
    pass

def _norm_eq_lsq(*args, **kwargs): # real signature unknown
    """
    Construct the normal equations for the B-spline LSQ problem.
    
        The observation equations are ``A @ c = y``, and the normal equations are
        ``A.T @ A @ c = A.T @ y``. This routine fills in the rhs and lhs for the
        latter.
    
        The B-spline collocation matrix is defined as :math:`A_{j,l} = B_l(x_j)`,
        so that row ``j`` contains all the B-splines which are non-zero
        at ``x_j``.
    
        The normal eq matrix has at most `2k+1` bands and is constructed in the
        LAPACK symmetrix banded storage: ``A[i, j] == ab[i-j, j]`` with `i >= j`.
        See the doctsring for `scipy.linalg.cholesky_banded` for more info.
    
        This routine is not supposed to be called directly, and
        does no error checking.
    
        Parameters
        ----------
        x : ndarray, shape (n,)
            sorted 1D array of x values
        t : ndarray, shape (nt + k + 1,)
            sorted 1D array of knots
        k : int
            spline order
        y : ndarray, shape (n, s)
            a 2D array of y values. The second dimension contains all trailing
            dimensions of the original array of ordinates.
        w : ndarray, shape(n,)
            Weights.
        ab : ndarray, shape (k+1, n), in Fortran order.
            This parameter is modified in-place.
            On entry: should be zeroed out.
            On exit: LHS of the normal equations.
        rhs : ndarray, shape (n, s), in Fortran order.
            This parameter is modified in-place.
            On entry: should be zeroed out.
            On exit: RHS of the normal equations.
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff92cf1340>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.interpolate._bspl', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff92cf1340>, origin='/.venv/lib/python3.8/site-packages/scipy/interpolate/_bspl.cpython-38-aarch64-linux-gnu.so')"

__test__ = {
    'evaluate_all_bspl (line 164)': "Evaluate the ``k+1`` B-splines which are non-zero on interval ``m``.\n\n    Parameters\n    ----------\n    t : ndarray, shape (nt + k + 1,)\n        sorted 1D array of knots\n    k : int\n        spline order\n    xval: float\n        argument at which to evaluate the B-splines\n    m : int\n        index of the left edge of the evaluation interval, ``t[m] <= x < t[m+1]``\n    nu : int, optional\n        Evaluate derivatives order `nu`. Default is zero.\n\n    Returns\n    -------\n    ndarray, shape (k+1,)\n        The values of B-splines :math:`[B_{m-k}(xval), ..., B_{m}(xval)]` if\n        `nu` is zero, otherwise the derivatives of order `nu`.\n\n    Examples\n    --------\n\n    A textbook use of this sort of routine is plotting the ``k+1`` polynomial\n    pieces which make up a B-spline of order `k`.\n\n    Consider a cubic spline\n\n    >>> k = 3\n    >>> t = [0., 1., 2., 3., 4.]   # internal knots\n    >>> a, b = t[0], t[-1]    # base interval is [a, b)\n    >>> t = np.array([a]*k + t + [b]*k)  # add boundary knots\n\n    >>> import matplotlib.pyplot as plt\n    >>> xx = np.linspace(a, b, 100)\n    >>> plt.plot(xx, BSpline.basis_element(t[k:-k])(xx),\n    ...          lw=3, alpha=0.5, label='basis_element')\n\n    Now we use slide an interval ``t[m]..t[m+1]`` along the base interval\n    ``a..b`` and use `evaluate_all_bspl` to compute the restriction of\n    the B-spline of interest to this interval:\n\n    >>> for i in range(k+1):\n    ...    x1, x2 = t[2*k - i], t[2*k - i + 1]\n    ...    xx = np.linspace(x1 - 0.5, x2 + 0.5)\n    ...    yy = [evaluate_all_bspl(t, k, x, 2*k - i)[i] for x in xx]\n    ...    plt.plot(xx, yy, '--', label=str(i))\n    ...\n    >>> plt.grid(True)\n    >>> plt.legend()\n    >>> plt.show()\n\n    ",
}

