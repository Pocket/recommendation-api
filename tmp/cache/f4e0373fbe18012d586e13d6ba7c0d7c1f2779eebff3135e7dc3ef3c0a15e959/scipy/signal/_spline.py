# encoding: utf-8
# module scipy.signal._spline
# from /.venv/lib/python3.8/site-packages/scipy/signal/_spline.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

# functions

def cspline2d(input, lambda=0.0, precision=-1.0): # real signature unknown; restored from __doc__
    """
    out = cspline2d(input, lambda=0.0, precision=-1.0)
    
        Coefficients for 2-D cubic (3rd order) B-spline.
    
        Return the third-order B-spline coefficients over a regularly spaced
        input grid for the two-dimensional input image.
    
        Parameters
        ----------
        input : ndarray
            The input signal.
        lambda : float
            Specifies the amount of smoothing in the transfer function.
        precision : float
            Specifies the precision for computing the infinite sum needed to apply mirror-
            symmetric boundary conditions.
    
        Returns
        -------
        output : ndarray
            The filtered signal.
    
        Examples
        --------
        Examples are given :ref:`in the tutorial <tutorial-signal-bsplines>`.
    """
    pass

def qspline2d(input, lambda=0.0, precision=-1.0): # real signature unknown; restored from __doc__
    """
    out = qspline2d(input, lambda=0.0, precision=-1.0)
    
        Coefficients for 2-D quadratic (2nd order) B-spline:
    
        Return the second-order B-spline coefficients over a regularly spaced
        input grid for the two-dimensional input image.
    
        Parameters
        ----------
        input : ndarray
            The input signal.
        lambda : float
            Specifies the amount of smoothing in the transfer function.
        precision : float
            Specifies the precision for computing the infinite sum needed to apply mirror-
            symmetric boundary conditions.
    
        Returns
        -------
        output : ndarray
            The filtered signal.
    
        Examples
        --------
        Examples are given :ref:`in the tutorial <tutorial-signal-bsplines>`.
    """
    pass

def sepfir2d(input, hrow, hcol): # real signature unknown; restored from __doc__
    """
    out = sepfir2d(input, hrow, hcol)
    
        Convolve with a 2-D separable FIR filter.
    
        Convolve the rank-2 input array with the separable filter defined by the
        rank-1 arrays hrow, and hcol. Mirror symmetric boundary conditions are
        assumed. This function can be used to find an image given its B-spline
        representation.
    
        Parameters
        ----------
        input : ndarray
            The input signal. Must be a rank-2 array.
        hrow : ndarray
            A rank-1 array defining the row direction of the filter.
            Must be odd-length
        hcol : ndarray
            A rank-1 array defining the column direction of the filter.
            Must be odd-length
    
        Returns
        -------
        output : ndarray
            The filtered signal.
    
        Examples
        --------
        Examples are given :ref:`in the tutorial <tutorial-signal-bsplines>`.
    """
    pass

def symiirorder1(input, c0, z1, precision=-1.0): # real signature unknown; restored from __doc__
    """
    out = symiirorder1(input, c0, z1, precision=-1.0)
    
        Implement a smoothing IIR filter with mirror-symmetric boundary conditions
        using a cascade of first-order sections.  The second section uses a
        reversed sequence.  This implements a system with the following
        transfer function and mirror-symmetric boundary conditions::
    
                               c0              
               H(z) = ---------------------    
                       (1-z1/z) (1 - z1 z)     
    
        The resulting signal will have mirror symmetric boundary conditions as well.
    
        Parameters
        ----------
        input : ndarray
            The input signal.
        c0, z1 : scalar
            Parameters in the transfer function.
        precision :
            Specifies the precision for calculating initial conditions
            of the recursive filter based on mirror-symmetric input.
    
        Returns
        -------
        output : ndarray
            The filtered signal.
    """
    pass

def symiirorder2(input, r, omega, precision=-1.0): # real signature unknown; restored from __doc__
    """
    out = symiirorder2(input, r, omega, precision=-1.0)
    
        Implement a smoothing IIR filter with mirror-symmetric boundary conditions
        using a cascade of second-order sections.  The second section uses a
        reversed sequence.  This implements the following transfer function::
    
                                      cs^2
             H(z) = ---------------------------------------
                    (1 - a2/z - a3/z^2) (1 - a2 z - a3 z^2 )
    
        where::
    
              a2 = (2 r cos omega)
              a3 = - r^2
              cs = 1 - 2 r cos omega + r^2
    
        Parameters
        ----------
        input : ndarray
            The input signal.
        r, omega : float
            Parameters in the transfer function.
        precision : float
            Specifies the precision for calculating initial conditions
            of the recursive filter based on mirror-symmetric input.
    
        Returns
        -------
        output : ndarray
            The filtered signal.
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff92cf2e80>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.signal._spline', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff92cf2e80>, origin='/.venv/lib/python3.8/site-packages/scipy/signal/_spline.cpython-38-aarch64-linux-gnu.so')"

