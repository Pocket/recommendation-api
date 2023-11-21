# encoding: utf-8
# module scipy.stats._stats_pythran
# from /.venv/lib/python3.8/site-packages/scipy/stats/_stats_pythran.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

# functions

def siegelslopes(float64, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Supported prototypes:
    
        - siegelslopes(float64[:], float64[:], str)
        - siegelslopes(float32[:], float32[:], str)
    """
    pass

def _Aij(p_int, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Sum of upper-left and lower right blocks of contingency table.
    
        Supported prototypes:
    
        - _Aij(int[:,:], int, int)
        - _Aij(float[:,:], int, int)
    """
    pass

def _a_ij_Aij_Dij2(p_int, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    A term that appears in the ASE of Kendall's tau and Somers' D.
    
        Supported prototypes:
    
        - _a_ij_Aij_Dij2(int[:,:])
        - _a_ij_Aij_Dij2(float[:,:])
    """
    pass

def _compute_outer_prob_inside_method(int64, int64_1, int64_2, int64_3): # real signature unknown; restored from __doc__
    """
    Count the proportion of paths that do not stay strictly inside two
    diagonal lines.
    
    Supported prototypes:
    
    - _compute_outer_prob_inside_method(int64, int64, int64, int64)
    
    Parameters
    ----------
    m : integer
        m > 0
    n : integer
        n > 0
    g : integer
        g is greatest common divisor of m and n
    h : integer
        0 <= h <= lcm(m,n)
    
    Returns
    -------
    p : float
        The proportion of paths that do not stay inside the two lines.
    
    The classical algorithm counts the integer lattice paths from (0, 0)
    to (m, n) which satisfy |x/m - y/n| < h / lcm(m, n).
    The paths make steps of size +1 in either positive x or positive y
    directions.
    We are, however, interested in 1 - proportion to computes p-values,
    so we change the recursion to compute 1 - p directly while staying
    within the "inside method" a described by Hodges.
    
    We generally follow Hodges' treatment of Drion/Gnedenko/Korolyuk.
    Hodges, J.L. Jr.,
    "The Significance Probability of the Smirnov Two-Sample Test,"
    Arkiv fiur Matematik, 3, No. 43 (1958), 469-86.
    
    For the recursion for 1-p see
    Viehmann, T.: "Numerically more stable computation of the p-values
    for the two-sample Kolmogorov-Smirnov test," arXiv: 2102.08037
    """
    pass

def _concordant_pairs(p_int, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Twice the number of concordant pairs, excluding ties.
    
        Supported prototypes:
    
        - _concordant_pairs(int[:,:])
        - _concordant_pairs(float[:,:])
    """
    pass

def _Dij(p_int, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Sum of lower-left and upper-right blocks of contingency table.
    
        Supported prototypes:
    
        - _Dij(int[:,:], int, int)
        - _Dij(float[:,:], int, int)
    """
    pass

def _discordant_pairs(p_int, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Twice the number of discordant pairs, excluding ties.
    
        Supported prototypes:
    
        - _discordant_pairs(int[:,:])
        - _discordant_pairs(float[:,:])
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff92c399d0>'

__pythran__ = (
    '0.12.1',
    '2023-02-19 18:19:19.780659',
    '19e5b0f7aa5208fcd48c0b9e9ed4efc343826182b5812f76cccc80278a5c1b87',
)

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.stats._stats_pythran', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff92c399d0>, origin='/.venv/lib/python3.8/site-packages/scipy/stats/_stats_pythran.cpython-38-aarch64-linux-gnu.so')"

