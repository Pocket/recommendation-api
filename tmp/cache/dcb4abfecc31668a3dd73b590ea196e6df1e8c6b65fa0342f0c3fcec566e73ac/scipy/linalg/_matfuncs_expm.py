# encoding: utf-8
# module scipy.linalg._matfuncs_expm
# from /.venv/lib/python3.8/site-packages/scipy/linalg/_matfuncs_expm.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import math as math # /usr/local/lib/python3.8/lib-dynload/math.cpython-38-aarch64-linux-gnu.so
import random as random # /usr/local/lib/python3.8/random.py
import numpy as np # /.venv/lib/python3.8/site-packages/numpy/__init__.py

# functions

def pade_UV_calc(*args, **kwargs): # real signature unknown
    """ Helper functions for expm to solve the final polynomial evaluation """
    pass

def pick_pade_structure(*args, **kwargs): # real signature unknown
    """ Helper functions for expm to choose Pade approximation order """
    pass

def _norm1est(*args, **kwargs): # real signature unknown
    """
    Compute a lower bound for the 1-norm of 2D matrix A or its powers.
    
        Computing the 1-norm of 8th or 10th power of a very large array is a very
        wasteful computation if we explicitly compute the actual power. The
        estimation exploits (in a nutshell) the following:
    
            (A @ A @ ... A) @ <thin array> = (A @ (A @ (... @ (A @ <thin array>)))
    
        And in fact all the rest is practically Ward's power method with ``t``
        starting vectors, hence, thin array and smarter selection of those vectors.
    
        Thus at some point ``expm`` which uses this function to scale-square, will
        switch to estimating when ``np.abs(A).sum(axis=0).max()`` becomes slower
        than the estimate (``linalg.norm`` is even slower). Currently the switch
        is chosen to be ``n=400``.
    
        Parameters
        ----------
        A : ndarray
            Input square array of shape (N, N).
        m : int, optional
            If it is different than one, then m-th power of the matrix norm is
            computed.
        t : int, optional
            The number of columns of the internal matrix used in the iterations.
        max_iter : int, optional
            The number of total iterations to be performed. Problems that require
            more than 5 iterations are rarely reported in practice.
    
        Returns
        -------
        c : float
            The resulting 1-norm condition number estimate of A.
    
        Notes
        -----
        Implements a SciPy adaptation of Algorithm 2.4 of [1], and the original
        Fortran code given in [2].
    
        The algorithm involves randomized elements and hence if needed, the seed
        of the Python built-in "random" module can be set for reproducible results.
    
        References
        ----------
        .. [1] Nicholas J. Higham and Francoise Tisseur (2000), "A Block Algorithm
               for Matrix 1-Norm Estimation, with an Application to 1-Norm
               Pseudospectra." SIAM J. Matrix Anal. Appl. 21(4):1185-1201,
               :doi:`10.1137/S0895479899356080`
    
        .. [2] Sheung Hun Cheng, Nicholas J. Higham (2001), "Implementation for
               LAPACK of a Block Algorithm for Matrix 1-Norm Estimation",
               NA Report 393
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__all__ = [
    'pick_pade_structure',
    'pade_UV_calc',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9bc878e0>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.linalg._matfuncs_expm', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9bc878e0>, origin='/.venv/lib/python3.8/site-packages/scipy/linalg/_matfuncs_expm.cpython-38-aarch64-linux-gnu.so')"

__test__ = {}

