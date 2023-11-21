# encoding: utf-8
# module scipy.interpolate._rbfinterp_pythran
# from /.venv/lib/python3.8/site-packages/scipy/interpolate/_rbfinterp_pythran.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

# functions

def _build_evaluation_coefficients(p_float, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Construct the coefficients needed to evaluate
        the RBF.
    
        Supported prototypes:
    
        - _build_evaluation_coefficients(float[:,:], float[:,:], str, float, int[:,:], float[:], float[:])
    
        Parameters
        ----------
        x : (Q, N) float ndarray
            Evaluation point coordinates.
        y : (P, N) float ndarray
            Data point coordinates.
        kernel : str
            Name of the RBF.
        epsilon : float
            Shape parameter.
        powers : (R, N) int ndarray
            The exponents for each monomial in the polynomial.
        shift : (N,) float ndarray
            Shifts the polynomial domain for numerical stability.
        scale : (N,) float ndarray
            Scales the polynomial domain for numerical stability.
    
        Returns
        -------
        (Q, P + R) float ndarray
    """
    pass

def _build_system(p_float, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Build the system used to solve for the RBF interpolant coefficients.
    
        Supported prototypes:
    
        - _build_system(float[:,:], float[:,:], float[:], str, float, int[:,:])
    
        Parameters
        ----------
        y : (P, N) float ndarray
            Data point coordinates.
        d : (P, S) float ndarray
            Data values at `y`.
        smoothing : (P,) float ndarray
            Smoothing parameter for each data point.
        kernel : str
            Name of the RBF.
        epsilon : float
            Shape parameter.
        powers : (R, N) int ndarray
            The exponents for each monomial in the polynomial.
    
        Returns
        -------
        lhs : (P + R, P + R) float ndarray
            Left-hand side matrix.
        rhs : (P + R, S) float ndarray
            Right-hand side matrix.
        shift : (N,) float ndarray
            Domain shift used to create the polynomial matrix.
        scale : (N,) float ndarray
            Domain scaling used to create the polynomial matrix.
    """
    pass

def _kernel_matrix(p_float, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Return RBFs, with centers at `x`, evaluated at `x`.
    
        Supported prototypes:
    
        - _kernel_matrix(float[:,:], str)
    """
    pass

def _polynomial_matrix(p_float, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Return monomials, with exponents from `powers`, evaluated at `x`.
    
        Supported prototypes:
    
        - _polynomial_matrix(float[:,:], int[:,:])
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9d6a2bb0>'

__pythran__ = (
    '0.12.1',
    '2023-02-19 18:20:51.774649',
    '82b91377de06dd16be6893c7c3c66cb245b5c068e52c6d92a439d4d86f40eaba',
)

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.interpolate._rbfinterp_pythran', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9d6a2bb0>, origin='/.venv/lib/python3.8/site-packages/scipy/interpolate/_rbfinterp_pythran.cpython-38-aarch64-linux-gnu.so')"

