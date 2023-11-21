# encoding: utf-8
# module scipy.fftpack.convolve
# from /.venv/lib/python3.8/site-packages/scipy/fftpack/convolve.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /.venv/lib/python3.8/site-packages/numpy/__init__.py
from scipy.fft._pocketfft.pypocketfft import r2r_fftpack


# functions

def convolve(x, omega, swap_real_imag=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    y = convolve(x,omega,[swap_real_imag,overwrite_x])
    
        Wrapper for ``convolve``.
    
        Parameters
        ----------
        x : input rank-1 array('d') with bounds (n)
        omega : input rank-1 array('d') with bounds (n)
    
        Other Parameters
        ----------------
        overwrite_x : input int, optional
            Default: 0
        swap_real_imag : input int, optional
             Default: 0
    
        Returns
        -------
        y : rank-1 array('d') with bounds (n) and x storage
    """
    pass

def convolve_z(x, omega_real, omega_imag, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    y = convolve_z(x,omega_real,omega_imag,[overwrite_x])
    
        Wrapper for ``convolve_z``.
    
        Parameters
        ----------
        x : input rank-1 array('d') with bounds (n)
        omega_real : input rank-1 array('d') with bounds (n)
        omega_imag : input rank-1 array('d') with bounds (n)
    
        Other Parameters
        ----------------
        overwrite_x : input int, optional
            Default: 0
    
        Returns
        -------
        y : rank-1 array('d') with bounds (n) and x storage
    """
    pass

def destroy_convolve_cache(*args, **kwargs): # real signature unknown
    pass

def init_convolution_kernel(n, kernel_func, d=None, zero_nyquist=None, kernel_func_extra_args=None): # real signature unknown; restored from __doc__
    """
    omega = init_convolution_kernel(n,kernel_func,[d,zero_nyquist,kernel_func_extra_args])
    
        Wrapper for ``init_convolution_kernel``.
    
        Parameters
        ----------
        n : input int
        kernel_func : call-back function
    
        Other Parameters
        ----------------
        d : input int, optional
            Default: 0
        kernel_func_extra_args : input tuple, optional
            Default: ()
        zero_nyquist : input int, optional
            Default: d%2
    
        Returns
        -------
        omega : rank-1 array('d') with bounds (n)
    
        Notes
        -----
        Call-back functions::
    
          def kernel_func(k): return kernel_func
          Required arguments:
            k : input int
          Return objects:
            kernel_func : float
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__all__ = [
    'destroy_convolve_cache',
    'convolve',
    'convolve_z',
    'init_convolution_kernel',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff92d66640>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.fftpack.convolve', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff92d66640>, origin='/.venv/lib/python3.8/site-packages/scipy/fftpack/convolve.cpython-38-aarch64-linux-gnu.so')"

__test__ = {}

