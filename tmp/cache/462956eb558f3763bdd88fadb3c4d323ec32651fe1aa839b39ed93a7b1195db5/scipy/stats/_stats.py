# encoding: utf-8
# module scipy.stats._stats
# from /.venv/lib/python3.8/site-packages/scipy/stats/_stats.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import warnings as warnings # /usr/local/lib/python3.8/warnings.py
import numpy as np # /.venv/lib/python3.8/site-packages/numpy/__init__.py
import scipy as scipy # /.venv/lib/python3.8/site-packages/scipy/__init__.py

# functions

def gaussian_kernel_estimate(*args, **kwargs): # real signature unknown
    """
    Evaluate a multivariate Gaussian kernel estimate.
    
        Parameters
        ----------
        points : array_like with shape (n, d)
            Data points to estimate from in d dimensions.
        values : real[:, :] with shape (n, p)
            Multivariate values associated with the data points.
        xi : array_like with shape (m, d)
            Coordinates to evaluate the estimate at in d dimensions.
        cho_cov : array_like with shape (d, d)
            (Lower) Cholesky factor of the covariance.
    
        Returns
        -------
        estimate : double[:, :] with shape (m, p)
            Multivariate Gaussian kernel estimate evaluated at the input coordinates.
    """
    pass

def gaussian_kernel_estimate_log(points, real, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    def gaussian_kernel_estimate_log(points, real[:, :] values, xi, cho_cov)
    
        Evaluate the log of the estimated pdf on a provided set of points.
    
        Parameters
        ----------
        points : array_like with shape (n, d)
            Data points to estimate from in ``d`` dimensions.
        values : real[:, :] with shape (n, p)
            Multivariate values associated with the data points.
        xi : array_like with shape (m, d)
            Coordinates to evaluate the estimate at in ``d`` dimensions.
        cho_cov : array_like with shape (d, d)
            (Lower) Cholesky factor of the covariance.
    
        Returns
        -------
        estimate : double[:, :] with shape (m, p)
            The log of the multivariate Gaussian kernel estimate evaluated at the
            input coordinates.
    """
    pass

def genhyperbolic_logpdf(*args, **kwargs): # real signature unknown
    pass

def genhyperbolic_pdf(*args, **kwargs): # real signature unknown
    pass

def geninvgauss_logpdf(*args, **kwargs): # real signature unknown
    pass

def solve_triangular(a, b, trans=0, lower=False, unit_diagonal=False, overwrite_b=False, check_finite=True): # reliably restored by inspect
    """
    Solve the equation `a x = b` for `x`, assuming a is a triangular matrix.
    
        Parameters
        ----------
        a : (M, M) array_like
            A triangular matrix
        b : (M,) or (M, N) array_like
            Right-hand side matrix in `a x = b`
        lower : bool, optional
            Use only data contained in the lower triangle of `a`.
            Default is to use upper triangle.
        trans : {0, 1, 2, 'N', 'T', 'C'}, optional
            Type of system to solve:
    
            ========  =========
            trans     system
            ========  =========
            0 or 'N'  a x  = b
            1 or 'T'  a^T x = b
            2 or 'C'  a^H x = b
            ========  =========
        unit_diagonal : bool, optional
            If True, diagonal elements of `a` are assumed to be 1 and
            will not be referenced.
        overwrite_b : bool, optional
            Allow overwriting data in `b` (may enhance performance)
        check_finite : bool, optional
            Whether to check that the input matrices contain only finite numbers.
            Disabling may give a performance gain, but may result in problems
            (crashes, non-termination) if the inputs do contain infinities or NaNs.
    
        Returns
        -------
        x : (M,) or (M, N) ndarray
            Solution to the system `a x = b`.  Shape of return matches `b`.
    
        Raises
        ------
        LinAlgError
            If `a` is singular
    
        Notes
        -----
        .. versionadded:: 0.9.0
    
        Examples
        --------
        Solve the lower triangular system a x = b, where::
    
                 [3  0  0  0]       [4]
            a =  [2  1  0  0]   b = [2]
                 [1  0  1  0]       [4]
                 [1  1  1  1]       [2]
    
        >>> import numpy as np
        >>> from scipy.linalg import solve_triangular
        >>> a = np.array([[3, 0, 0, 0], [2, 1, 0, 0], [1, 0, 1, 0], [1, 1, 1, 1]])
        >>> b = np.array([4, 2, 4, 2])
        >>> x = solve_triangular(a, b, lower=True)
        >>> x
        array([ 1.33333333, -0.66666667,  2.66666667, -1.33333333])
        >>> a.dot(x)  # Check the result
        array([ 4.,  2.,  4.,  2.])
    """
    pass

def von_mises_cdf(*args, **kwargs): # real signature unknown
    pass

def _center_distance_matrix(*args, **kwargs): # real signature unknown
    pass

def _kendall_dis(*args, **kwargs): # real signature unknown
    pass

def _local_correlations(*args, **kwargs): # real signature unknown
    pass

def _local_covariance(*args, **kwargs): # real signature unknown
    pass

def _rank_distance_matrix(*args, **kwargs): # real signature unknown
    pass

def _studentized_range_cdf_logconst(*args, **kwargs): # real signature unknown
    """ Evaluates log of constant terms in the cdf integrand """
    pass

def _studentized_range_pdf_logconst(*args, **kwargs): # real signature unknown
    """ Evaluates log of constant terms in the pdf integrand """
    pass

def _toint64(*args, **kwargs): # real signature unknown
    pass

def _transform_distance_matrix(*args, **kwargs): # real signature unknown
    pass

def _weightedrankedtau(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff937641c0>'

__pyx_capi__ = {
    '_genhyperbolic_logpdf': None, # (!) real value is '<capsule object "double (double, void *)" at 0xffff937647b0>'
    '_genhyperbolic_pdf': None, # (!) real value is '<capsule object "double (double, void *)" at 0xffff93764780>'
    '_geninvgauss_pdf': None, # (!) real value is '<capsule object "double (double, void *)" at 0xffff93764660>'
    '_studentized_range_cdf': None, # (!) real value is '<capsule object "double (int, double *, void *)" at 0xffff93764690>'
    '_studentized_range_cdf_asymptotic': None, # (!) real value is '<capsule object "double (double, void *)" at 0xffff937646c0>'
    '_studentized_range_moment': None, # (!) real value is '<capsule object "double (int, double *, void *)" at 0xffff93764750>'
    '_studentized_range_pdf': None, # (!) real value is '<capsule object "double (int, double *, void *)" at 0xffff937646f0>'
    '_studentized_range_pdf_asymptotic': None, # (!) real value is '<capsule object "double (double, void *)" at 0xffff93764720>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.stats._stats', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff937641c0>, origin='/.venv/lib/python3.8/site-packages/scipy/stats/_stats.cpython-38-aarch64-linux-gnu.so')"

__test__ = {}

