# encoding: utf-8
# module scipy.optimize.cython_optimize._zeros
# from /.venv/lib/python3.8/site-packages/scipy/optimize/cython_optimize/_zeros.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
""" Cython wrappers for root finders in c_zeros """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

# functions

def full_output_example(*args, **kwargs): # real signature unknown
    """
    Example of Cython optimize zeros functions with full output.
    
        Parameters
        ----------
        args : sequence of float
            extra arguments of zero function
        xa : float
            first boundary of zero function
        xb : float
            second boundary of zero function
        xtol : float
            absolute tolerance of zero function
        rtol : float
            relative tolerance of zero function
        mitr : int
            max. iteration of zero function
    
        Returns
        -------
        full_output : dict
            the root, number of function calls, number of iterations, and the zero
            function error number 
    
        This example finds the roots of a 3rd order polynomial with coefficients
        given as `args`.
    """
    pass

def loop_example(*args, **kwargs): # real signature unknown
    """
    Example of Cython optimize zeros functions with map.
    
        Parameters
        ----------
        method : str
            name of the Cython optimize zeros function to call
        a0 : sequence of float
            first extra argument which is mapped to output
        args : sequence of float
            the remaining extra arguments which are constant
        xa : float
            first bound of zero function
        xb : float
            second bound of zero function
        xtol : float
            absolute tolerance of zero function
        rtol : float
            relative tolerance of zero function
        mitr : int
            max. iteration of zero function
    
        Returns
        -------
        roots : sequence of float
            the root for each of the values of `a0`
    
        This example finds the roots of a 3rd order polynomial given a sequence of
        constant terms as `a0` and fixed 1st, 2nd, and 3rd order terms in `args`.
    """
    pass

# no classes
# variables with complex values

EXAMPLES_MAP = {
    'bisect': None, # (!) real value is '<cyfunction __Pyx_CFunc_double____tuple____float____float____float____float____int___to_py.<locals>.wrap at 0xffff9ccf32b0>'
    'brenth': None, # (!) real value is '<cyfunction __Pyx_CFunc_double____tuple____float____float____float____float____int___to_py.<locals>.wrap at 0xffff9ccf3450>'
    'brentq': None, # (!) real value is '<cyfunction __Pyx_CFunc_double____tuple____float____float____float____float____int___to_py.<locals>.wrap at 0xffff9ccf3520>'
    'ridder': None, # (!) real value is '<cyfunction __Pyx_CFunc_double____tuple____float____float____float____float____int___to_py.<locals>.wrap at 0xffff9ccf3380>'
}

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924760>'

__pyx_capi__ = {
    'bisect': None, # (!) real value is '<capsule object "double (__pyx_t_5scipy_8optimize_15cython_optimize_6_zeros_callback_type, double, double, void *, double, double, int, __pyx_t_5scipy_8optimize_15cython_optimize_6_zeros_zeros_full_output *)" at 0xffffac924c90>'
    'brenth': None, # (!) real value is '<capsule object "double (__pyx_t_5scipy_8optimize_15cython_optimize_6_zeros_callback_type, double, double, void *, double, double, int, __pyx_t_5scipy_8optimize_15cython_optimize_6_zeros_zeros_full_output *)" at 0xffffac924f00>'
    'brentq': None, # (!) real value is '<capsule object "double (__pyx_t_5scipy_8optimize_15cython_optimize_6_zeros_callback_type, double, double, void *, double, double, int, __pyx_t_5scipy_8optimize_15cython_optimize_6_zeros_zeros_full_output *)" at 0xffffac924ab0>'
    'ridder': None, # (!) real value is '<capsule object "double (__pyx_t_5scipy_8optimize_15cython_optimize_6_zeros_callback_type, double, double, void *, double, double, int, __pyx_t_5scipy_8optimize_15cython_optimize_6_zeros_zeros_full_output *)" at 0xffffac924f60>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.optimize.cython_optimize._zeros', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924760>, origin='/.venv/lib/python3.8/site-packages/scipy/optimize/cython_optimize/_zeros.cpython-38-aarch64-linux-gnu.so')"

__test__ = {}

