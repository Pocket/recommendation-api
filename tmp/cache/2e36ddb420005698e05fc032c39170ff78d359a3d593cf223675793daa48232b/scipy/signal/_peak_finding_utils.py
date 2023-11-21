# encoding: utf-8
# module scipy.signal._peak_finding_utils
# from /.venv/lib/python3.8/site-packages/scipy/signal/_peak_finding_utils.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
""" Utility functions for finding peaks in signals. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import warnings as warnings # /usr/local/lib/python3.8/warnings.py
import numpy as np # /.venv/lib/python3.8/site-packages/numpy/__init__.py

# functions

def _local_maxima_1d(*args, **kwargs): # real signature unknown
    """
    Find local maxima in a 1D array.
    
        This function finds all local maxima in a 1D array and returns the indices
        for their edges and midpoints (rounded down for even plateau sizes).
    
        Parameters
        ----------
        x : ndarray
            The array to search for local maxima.
    
        Returns
        -------
        midpoints : ndarray
            Indices of midpoints of local maxima in `x`.
        left_edges : ndarray
            Indices of edges to the left of local maxima in `x`.
        right_edges : ndarray
            Indices of edges to the right of local maxima in `x`.
    
        Notes
        -----
        - Compared to `argrelmax` this function is significantly faster and can
          detect maxima that are more than one sample wide. However this comes at
          the cost of being only applicable to 1D arrays.
        - A maxima is defined as one or more samples of equal value that are
          surrounded on both sides by at least one smaller sample.
    
        .. versionadded:: 1.1.0
    """
    pass

def _peak_prominences(*args, **kwargs): # real signature unknown
    """
    Calculate the prominence of each peak in a signal.
    
        Parameters
        ----------
        x : ndarray
            A signal with peaks.
        peaks : ndarray
            Indices of peaks in `x`.
        wlen : np.intp
            A window length in samples (see `peak_prominences`) which is rounded up
            to the nearest odd integer. If smaller than 2 the entire signal `x` is
            used.
    
        Returns
        -------
        prominences : ndarray
            The calculated prominences for each peak in `peaks`.
        left_bases, right_bases : ndarray
            The peaks' bases as indices in `x` to the left and right of each peak.
    
        Raises
        ------
        ValueError
            If a value in `peaks` is an invalid index for `x`.
    
        Warns
        -----
        PeakPropertyWarning
            If a prominence of 0 was calculated for any peak.
    
        Notes
        -----
        This is the inner function to `peak_prominences`.
    
        .. versionadded:: 1.1.0
    """
    pass

def _peak_widths(*args, **kwargs): # real signature unknown
    """
    Calculate the width of each each peak in a signal.
    
        Parameters
        ----------
        x : ndarray
            A signal with peaks.
        peaks : ndarray
            Indices of peaks in `x`.
        rel_height : np.float64
            Chooses the relative height at which the peak width is measured as a
            percentage of its prominence (see `peak_widths`).
        prominences : ndarray
            Prominences of each peak in `peaks` as returned by `peak_prominences`.
        left_bases, right_bases : ndarray
            Left and right bases of each peak in `peaks` as returned by
            `peak_prominences`.
    
        Returns
        -------
        widths : ndarray
            The widths for each peak in samples.
        width_heights : ndarray
            The height of the contour lines at which the `widths` where evaluated.
        left_ips, right_ips : ndarray
            Interpolated positions of left and right intersection points of a
            horizontal line at the respective evaluation height.
    
        Raises
        ------
        ValueError
            If the supplied prominence data doesn't satisfy the condition
            ``0 <= left_base <= peak <= right_base < x.shape[0]`` for each peak or
            if `peaks`, `left_bases` and `right_bases` don't share the same shape.
            Or if `rel_height` is not at least 0.
    
        Warnings
        --------
        PeakPropertyWarning
            If a width of 0 was calculated for any peak.
    
        Notes
        -----
        This is the inner function to `peak_widths`.
    
        .. versionadded:: 1.1.0
    """
    pass

def _select_by_peak_distance(*args, **kwargs): # real signature unknown
    """
    Evaluate which peaks fulfill the distance condition.
    
        Parameters
        ----------
        peaks : ndarray
            Indices of peaks in `vector`.
        priority : ndarray
            An array matching `peaks` used to determine priority of each peak. A
            peak with a higher priority value is kept over one with a lower one.
        distance : np.float64
            Minimal distance that peaks must be spaced.
    
        Returns
        -------
        keep : ndarray[bool]
            A boolean mask evaluating to true where `peaks` fulfill the distance
            condition.
    
        Notes
        -----
        Declaring the input arrays as C-contiguous doesn't seem to have performance
        advantages.
    
        .. versionadded:: 1.1.0
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class PeakPropertyWarning(RuntimeWarning):
    """ Calculated property of a peak has unexpected value. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__all__ = [
    '_local_maxima_1d',
    '_select_by_peak_distance',
    '_peak_prominences',
    '_peak_widths',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9d1fc2e0>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.signal._peak_finding_utils', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9d1fc2e0>, origin='/.venv/lib/python3.8/site-packages/scipy/signal/_peak_finding_utils.cpython-38-aarch64-linux-gnu.so')"

__test__ = {}

