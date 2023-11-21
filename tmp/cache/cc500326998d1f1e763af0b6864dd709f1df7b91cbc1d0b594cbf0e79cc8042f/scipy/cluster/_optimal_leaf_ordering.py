# encoding: utf-8
# module scipy.cluster._optimal_leaf_ordering
# from /.venv/lib/python3.8/site-packages/scipy/cluster/_optimal_leaf_ordering.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /.venv/lib/python3.8/site-packages/numpy/__init__.py

# functions

def is_valid_dm(D, tol=0.0, throw=False, name=None, warning=False): # reliably restored by inspect
    """
    Return True if input array is a valid distance matrix.
    
        Distance matrices must be 2-dimensional numpy arrays.
        They must have a zero-diagonal, and they must be symmetric.
    
        Parameters
        ----------
        D : array_like
            The candidate object to test for validity.
        tol : float, optional
            The distance matrix should be symmetric. `tol` is the maximum
            difference between entries ``ij`` and ``ji`` for the distance
            metric to be considered symmetric.
        throw : bool, optional
            An exception is thrown if the distance matrix passed is not valid.
        name : str, optional
            The name of the variable to checked. This is useful if
            throw is set to True so the offending variable can be identified
            in the exception message when an exception is thrown.
        warning : bool, optional
            Instead of throwing an exception, a warning message is
            raised.
    
        Returns
        -------
        valid : bool
            True if the variable `D` passed is a valid distance matrix.
    
        Notes
        -----
        Small numerical differences in `D` and `D.T` and non-zeroness of
        the diagonal are ignored if they are within the tolerance specified
        by `tol`.
    """
    pass

def is_valid_y(y, warning=False, throw=False, name=None): # reliably restored by inspect
    """
    Return True if the input array is a valid condensed distance matrix.
    
        Condensed distance matrices must be 1-dimensional numpy arrays.
        Their length must be a binomial coefficient :math:`{n \choose 2}`
        for some positive integer n.
    
        Parameters
        ----------
        y : array_like
            The condensed distance matrix.
        warning : bool, optional
            Invokes a warning if the variable passed is not a valid
            condensed distance matrix. The warning message explains why
            the distance matrix is not valid.  `name` is used when
            referencing the offending variable.
        throw : bool, optional
            Throws an exception if the variable passed is not a valid
            condensed distance matrix.
        name : bool, optional
            Used when referencing the offending variable in the
            warning or exception message.
    """
    pass

def optimal_leaf_ordering(*args, **kwargs): # real signature unknown
    """
    Compute the optimal leaf order for Z (according to D) and return an
        optimally sorted Z.
    
        We start by sorting and relabelling Z and D according to the current leaf
        order in Z.
    
        This is because when everything is sorted each cluster (including
        singletons) can be defined by its range over (0...n_points).
    
        This is used extensively to loop efficiently over the various arrays in the
        algorithm.
    """
    pass

def squareform(X, force=None, checks=True): # reliably restored by inspect
    """
    Convert a vector-form distance vector to a square-form distance
        matrix, and vice-versa.
    
        Parameters
        ----------
        X : array_like
            Either a condensed or redundant distance matrix.
        force : str, optional
            As with MATLAB(TM), if force is equal to ``'tovector'`` or
            ``'tomatrix'``, the input will be treated as a distance matrix or
            distance vector respectively.
        checks : bool, optional
            If set to False, no checks will be made for matrix
            symmetry nor zero diagonals. This is useful if it is known that
            ``X - X.T1`` is small and ``diag(X)`` is close to zero.
            These values are ignored any way so they do not disrupt the
            squareform transformation.
    
        Returns
        -------
        Y : ndarray
            If a condensed distance matrix is passed, a redundant one is
            returned, or if a redundant one is passed, a condensed distance
            matrix is returned.
    
        Notes
        -----
        1. ``v = squareform(X)``
    
           Given a square n-by-n symmetric distance matrix ``X``,
           ``v = squareform(X)`` returns a ``n * (n-1) / 2``
           (i.e. binomial coefficient n choose 2) sized vector `v`
           where :math:`v[{n \choose 2} - {n-i \choose 2} + (j-i-1)]`
           is the distance between distinct points ``i`` and ``j``.
           If ``X`` is non-square or asymmetric, an error is raised.
    
        2. ``X = squareform(v)``
    
           Given a ``n * (n-1) / 2`` sized vector ``v``
           for some integer ``n >= 1`` encoding distances as described,
           ``X = squareform(v)`` returns a n-by-n distance matrix ``X``.
           The ``X[i, j]`` and ``X[j, i]`` values are set to
           :math:`v[{n \choose 2} - {n-i \choose 2} + (j-i-1)]`
           and all diagonal elements are zero.
    
        In SciPy 0.19.0, ``squareform`` stopped casting all input types to
        float64, and started returning arrays of the same dtype as the input.
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9282f340>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.cluster._optimal_leaf_ordering', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9282f340>, origin='/.venv/lib/python3.8/site-packages/scipy/cluster/_optimal_leaf_ordering.cpython-38-aarch64-linux-gnu.so')"

__test__ = {}

