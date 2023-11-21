# encoding: utf-8
# module scipy.interpolate.interpnd
# from /.venv/lib/python3.8/site-packages/scipy/interpolate/interpnd.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
"""
Simple N-D interpolation

.. versionadded:: 0.9
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /.venv/lib/python3.8/site-packages/numpy/__init__.py
import scipy.spatial._qhull as qhull # /.venv/lib/python3.8/site-packages/scipy/spatial/_qhull.cpython-38-aarch64-linux-gnu.so
import warnings as warnings # /usr/local/lib/python3.8/warnings.py

# functions

def estimate_gradients_2d_global(*args, **kwargs): # real signature unknown
    pass

def _ndim_coords_from_arrays(*args, **kwargs): # real signature unknown
    """ Convert a tuple of coordinate arrays to a (..., ndim)-shaped array. """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class NDInterpolatorBase(object):
    """
    Common routines for interpolators.
    
        .. versionadded:: 0.9
    """
    def _check_call_shape(self, *args, **kwargs): # real signature unknown
        pass

    def _scale_x(self, *args, **kwargs): # real signature unknown
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """
        interpolator(xi)
        
                Evaluate interpolator at given points.
        
                Parameters
                ----------
                x1, x2, ... xn: array-like of float
                    Points where to interpolate data at.
                    x1, x2, ... xn can be array-like of float with broadcastable shape.
                    or x1 can be array-like of float with shape ``(..., ndim)``
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        Check shape of points and values arrays, and reshape values to
                (npoints, nvalues).  Ensure the `points` and values arrays are
                C-contiguous, and of correct type.
        """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'scipy.interpolate.interpnd', '__doc__': '\\n    Common routines for interpolators.\\n\\n    .. versionadded:: 0.9\\n\\n    ', '__init__': <cyfunction NDInterpolatorBase.__init__ at 0xffff925ef2b0>, '_check_call_shape': <cyfunction NDInterpolatorBase._check_call_shape at 0xffff925ef380>, '_scale_x': <cyfunction NDInterpolatorBase._scale_x at 0xffff925ef450>, '__call__': <cyfunction NDInterpolatorBase.__call__ at 0xffff925ef520>, '__dict__': <attribute '__dict__' of 'NDInterpolatorBase' objects>, '__weakref__': <attribute '__weakref__' of 'NDInterpolatorBase' objects>})"


class CloughTocher2DInterpolator(NDInterpolatorBase):
    """
    CloughTocher2DInterpolator(points, values, tol=1e-6).
    
        Piecewise cubic, C1 smooth, curvature-minimizing interpolant in 2D.
    
        .. versionadded:: 0.9
    
        Methods
        -------
        __call__
    
        Parameters
        ----------
        points : ndarray of floats, shape (npoints, ndims); or Delaunay
            Data point coordinates, or a precomputed Delaunay triangulation.
        values : ndarray of float or complex, shape (npoints, ...)
            Data values.
        fill_value : float, optional
            Value used to fill in for requested points outside of the
            convex hull of the input points.  If not provided, then
            the default is ``nan``.
        tol : float, optional
            Absolute/relative tolerance for gradient estimation.
        maxiter : int, optional
            Maximum number of iterations in gradient estimation.
        rescale : bool, optional
            Rescale points to unit cube before performing interpolation.
            This is useful if some of the input dimensions have
            incommensurable units and differ by many orders of magnitude.
    
        Notes
        -----
        The interpolant is constructed by triangulating the input data
        with Qhull [1]_, and constructing a piecewise cubic
        interpolating Bezier polynomial on each triangle, using a
        Clough-Tocher scheme [CT]_.  The interpolant is guaranteed to be
        continuously differentiable.
    
        The gradients of the interpolant are chosen so that the curvature
        of the interpolating surface is approximatively minimized. The
        gradients necessary for this are estimated using the global
        algorithm described in [Nielson83]_ and [Renka84]_.
    
        Examples
        --------
        We can interpolate values on a 2D plane:
    
        >>> from scipy.interpolate import CloughTocher2DInterpolator
        >>> import numpy as np
        >>> import matplotlib.pyplot as plt
        >>> rng = np.random.default_rng()
        >>> x = rng.random(10) - 0.5
        >>> y = rng.random(10) - 0.5
        >>> z = np.hypot(x, y)
        >>> X = np.linspace(min(x), max(x))
        >>> Y = np.linspace(min(y), max(y))
        >>> X, Y = np.meshgrid(X, Y)  # 2D grid for interpolation
        >>> interp = CloughTocher2DInterpolator(list(zip(x, y)), z)
        >>> Z = interp(X, Y)
        >>> plt.pcolormesh(X, Y, Z, shading='auto')
        >>> plt.plot(x, y, "ok", label="input point")
        >>> plt.legend()
        >>> plt.colorbar()
        >>> plt.axis("equal")
        >>> plt.show()
    
        See also
        --------
        griddata :
            Interpolate unstructured D-D data.
        LinearNDInterpolator :
            Piecewise linear interpolant in N > 1 dimensions.
        NearestNDInterpolator :
            Nearest-neighbor interpolation in N > 1 dimensions.
    
        References
        ----------
        .. [1] http://www.qhull.org/
    
        .. [CT] See, for example,
           P. Alfeld,
           ''A trivariate Clough-Tocher scheme for tetrahedral data''.
           Computer Aided Geometric Design, 1, 169 (1984);
           G. Farin,
           ''Triangular Bernstein-Bezier patches''.
           Computer Aided Geometric Design, 3, 83 (1986).
    
        .. [Nielson83] G. Nielson,
           ''A method for interpolating scattered data based upon a minimum norm
           network''.
           Math. Comp., 40, 253 (1983).
    
        .. [Renka84] R. J. Renka and A. K. Cline.
           ''A Triangle-based C1 interpolation method.'',
           Rocky Mountain J. Math., 14, 223 (1984).
    """
    def _do_evaluate(self, *args, **kwargs): # real signature unknown
        pass

    def _evaluate_complex(self, *args, **kwargs): # real signature unknown
        pass

    def _evaluate_double(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class GradientEstimationWarning(Warning):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class LinearNDInterpolator(NDInterpolatorBase):
    """
    LinearNDInterpolator(points, values, fill_value=np.nan, rescale=False)
    
        Piecewise linear interpolant in N > 1 dimensions.
    
        .. versionadded:: 0.9
    
        Methods
        -------
        __call__
    
        Parameters
        ----------
        points : ndarray of floats, shape (npoints, ndims); or Delaunay
            Data point coordinates, or a precomputed Delaunay triangulation.
        values : ndarray of float or complex, shape (npoints, ...)
            Data values.
        fill_value : float, optional
            Value used to fill in for requested points outside of the
            convex hull of the input points.  If not provided, then
            the default is ``nan``.
        rescale : bool, optional
            Rescale points to unit cube before performing interpolation.
            This is useful if some of the input dimensions have
            incommensurable units and differ by many orders of magnitude.
    
        Notes
        -----
        The interpolant is constructed by triangulating the input data
        with Qhull [1]_, and on each triangle performing linear
        barycentric interpolation.
    
        Examples
        --------
        We can interpolate values on a 2D plane:
    
        >>> from scipy.interpolate import LinearNDInterpolator
        >>> import numpy as np
        >>> import matplotlib.pyplot as plt
        >>> rng = np.random.default_rng()
        >>> x = rng.random(10) - 0.5
        >>> y = rng.random(10) - 0.5
        >>> z = np.hypot(x, y)
        >>> X = np.linspace(min(x), max(x))
        >>> Y = np.linspace(min(y), max(y))
        >>> X, Y = np.meshgrid(X, Y)  # 2D grid for interpolation
        >>> interp = LinearNDInterpolator(list(zip(x, y)), z)
        >>> Z = interp(X, Y)
        >>> plt.pcolormesh(X, Y, Z, shading='auto')
        >>> plt.plot(x, y, "ok", label="input point")
        >>> plt.legend()
        >>> plt.colorbar()
        >>> plt.axis("equal")
        >>> plt.show()
    
        See also
        --------
        griddata :
            Interpolate unstructured D-D data.
        NearestNDInterpolator :
            Nearest-neighbor interpolation in N dimensions.
        CloughTocher2DInterpolator :
            Piecewise cubic, C1 smooth, curvature-minimizing interpolant in 2D.
    
        References
        ----------
        .. [1] http://www.qhull.org/
    """
    def _do_evaluate(self, *args, **kwargs): # real signature unknown
        pass

    def _evaluate_complex(self, *args, **kwargs): # real signature unknown
        pass

    def _evaluate_double(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff925fcf10>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.interpolate.interpnd', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff925fcf10>, origin='/.venv/lib/python3.8/site-packages/scipy/interpolate/interpnd.cpython-38-aarch64-linux-gnu.so')"

__test__ = {}

