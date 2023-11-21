# encoding: utf-8
# module scipy.fft._pocketfft.pypocketfft
# from /.venv/lib/python3.8/site-packages/scipy/fft/_pocketfft/pypocketfft.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
"""
Fast Fourier and Hartley transforms.

This module supports
- single, double, and long double precision
- complex and real-valued transforms
- multi-dimensional transforms

For two- and higher-dimensional transforms the code will use SSE2 and AVX
vector instructions for faster execution if these are supported by the CPU and
were enabled during compilation.
"""
# no imports

# functions

def c2c(a, axes=None, forward=True, inorm=0, out=None, nthreads=1): # real signature unknown; restored from __doc__
    """
    c2c(a: numpy.ndarray, axes: object = None, forward: bool = True, inorm: int = 0, out: object = None, nthreads: int = 1) -> numpy.ndarray
    
    Performs a complex FFT.
    
    Parameters
    ----------
    a : numpy.ndarray (any complex or real type)
        The input data. If its type is real, a more efficient real-to-complex
        transform will be used.
    axes : list of integers
        The axes along which the FFT is carried out.
        If not set, all axes will be transformed.
    forward : bool
        If `True`, a negative sign is used in the exponent, else a positive one.
    inorm : int
        Normalization type
          0 : no normalization
          1 : divide by sqrt(N)
          2 : divide by N
        where N is the product of the lengths of the transformed axes.
    out : numpy.ndarray (same shape as `a`, complex type with same accuracy as `a`)
        May be identical to `a`, but if it isn't, it must not overlap with `a`.
        If None, a new array is allocated to store the output.
    nthreads : int
        Number of threads to use. If 0, use the system default (typically governed
        by the `OMP_NUM_THREADS` environment variable).
    
    Returns
    -------
    numpy.ndarray (same shape as `a`, complex type with same accuracy as `a`)
        The transformed data.
    """
    pass

def c2r(a, axes=None, lastsize=0, forward=True, inorm=0, out=None, nthreads=1): # real signature unknown; restored from __doc__
    """
    c2r(a: numpy.ndarray, axes: object = None, lastsize: int = 0, forward: bool = True, inorm: int = 0, out: object = None, nthreads: int = 1) -> numpy.ndarray
    
    Performs an FFT whose output is strictly real.
    
    Parameters
    ----------
    a : numpy.ndarray (any complex type)
        The input data
    axes : list of integers
        The axes along which the FFT is carried out.
        If not set, all axes will be transformed in ascending order.
    lastsize : the output size of the last axis to be transformed.
        If the corresponding input axis has size n, this can be 2*n-2 or 2*n-1.
    forward : bool
        If `True`, a negative sign is used in the exponent, else a positive one.
    inorm : int
        Normalization type
          0 : no normalization
          1 : divide by sqrt(N)
          2 : divide by N
        where N is the product of the lengths of the transformed output axes.
    out : numpy.ndarray (real type with same accuracy as `a`)
        For the required shape, see the `Returns` section.
        Must not overlap with `a`.
        If None, a new array is allocated to store the output.
    nthreads : int
        Number of threads to use. If 0, use the system default (typically governed
        by the `OMP_NUM_THREADS` environment variable).
    
    Returns
    -------
    numpy.ndarray (real type with same accuracy as `a`)
        The transformed data. The shape is identical to that of the input array,
        except for the axis that was transformed last, which has now `lastsize`
        entries.
    """
    pass

def dct(a, type, axes=None, inorm=0, out=None, nthreads=1, ortho=None): # real signature unknown; restored from __doc__
    """
    dct(a: numpy.ndarray, type: int, axes: object = None, inorm: int = 0, out: object = None, nthreads: int = 1, ortho: object = None) -> numpy.ndarray
    
    Performs a discrete cosine transform.
    
    Parameters
    ----------
    a : numpy.ndarray (any real type)
        The input data
    type : integer
        the type of DCT. Must be in [1; 4].
    axes : list of integers
        The axes along which the transform is carried out.
        If not set, all axes will be transformed.
    inorm : int
        Normalization type
          0 : no normalization
          1 : divide by sqrt(N)
          2 : divide by N
        where N is the product of n_i for every transformed axis i.
        n_i is 2*(<axis_length>-1 for type 1 and 2*<axis length>
        for types 2, 3, 4.
        Making the transform orthogonal involves the following additional steps
        for every 1D sub-transform:
          Type 1 : multiply first and last input value by sqrt(2)
                   divide first and last output value by sqrt(2)
          Type 2 : divide first output value by sqrt(2)
          Type 3 : multiply first input value by sqrt(2)
          Type 4 : nothing
    out : numpy.ndarray (same shape and data type as `a`)
        May be identical to `a`, but if it isn't, it must not overlap with `a`.
        If None, a new array is allocated to store the output.
    nthreads : int
        Number of threads to use. If 0, use the system default (typically governed
        by the `OMP_NUM_THREADS` environment variable).
    ortho: bool
        Orthogonalize transform (defaults to ``inorm=1``)
    
    Returns
    -------
    numpy.ndarray (same shape and data type as `a`)
        The transformed data
    """
    pass

def dst(a, type, axes=None, inorm=0, out=None, nthreads=1, ortho=None): # real signature unknown; restored from __doc__
    """
    dst(a: numpy.ndarray, type: int, axes: object = None, inorm: int = 0, out: object = None, nthreads: int = 1, ortho: object = None) -> numpy.ndarray
    
    Performs a discrete sine transform.
    
    Parameters
    ----------
    a : numpy.ndarray (any real type)
        The input data
    type : integer
        the type of DST. Must be in [1; 4].
    axes : list of integers
        The axes along which the transform is carried out.
        If not set, all axes will be transformed.
    inorm : int
        Normalization type
          0 : no normalization
          1 : divide by sqrt(N)
          2 : divide by N
        where N is the product of n_i for every transformed axis i.
        n_i is 2*(<axis_length>+1 for type 1 and 2*<axis length>
        for types 2, 3, 4.
        Making the transform orthogonal involves the following additional steps
        for every 1D sub-transform:
          Type 1 : nothing
          Type 2 : divide first output value by sqrt(2)
          Type 3 : multiply first input value by sqrt(2)
          Type 4 : nothing
    out : numpy.ndarray (same shape and data type as `a`)
        May be identical to `a`, but if it isn't, it must not overlap with `a`.
        If None, a new array is allocated to store the output.
    nthreads : int
        Number of threads to use. If 0, use the system default (typically governed
        by the `OMP_NUM_THREADS` environment variable).
    ortho: bool
        Orthogonalize transform (defaults to ``inorm=1``)
    
    Returns
    -------
    numpy.ndarray (same shape and data type as `a`)
        The transformed data
    """
    pass

def genuine_hartley(a, axes=None, inorm=0, out=None, nthreads=1): # real signature unknown; restored from __doc__
    """
    genuine_hartley(a: numpy.ndarray, axes: object = None, inorm: int = 0, out: object = None, nthreads: int = 1) -> numpy.ndarray
    
    Performs a full Hartley transform.
    A full Fourier transform is carried out over the requested axes, and the
    sum of real and imaginary parts of the result is stored in the output
    array. For a single transformed axis, this is identical to `separable_hartley`,
    but when transforming multiple axes, the results are different.
    
    Parameters
    ----------
    a : numpy.ndarray (any real type)
        The input data
    axes : list of integers
        The axes along which the transform is carried out.
        If not set, all axes will be transformed.
    inorm : int
        Normalization type
          0 : no normalization
          1 : divide by sqrt(N)
          2 : divide by N
        where N is the product of the lengths of the transformed axes.
    out : numpy.ndarray (same shape and data type as `a`)
        May be identical to `a`, but if it isn't, it must not overlap with `a`.
        If None, a new array is allocated to store the output.
    nthreads : int
        Number of threads to use. If 0, use the system default (typically governed
        by the `OMP_NUM_THREADS` environment variable).
    
    Returns
    -------
    numpy.ndarray (same shape and data type as `a`)
        The transformed data
    """
    pass

def good_size(*args, **kwargs): # real signature unknown
    """
    Returns a good length to pad an FFT to.
    
    Parameters
    ----------
    target : int
        Minimum transform length
    real : bool, optional
        True if either input or output of FFT should be fully real.
    
    Returns
    -------
    out : int
        The smallest fast size >= n
    """
    pass

def r2c(a, axes=None, forward=True, inorm=0, out=None, nthreads=1): # real signature unknown; restored from __doc__
    """
    r2c(a: numpy.ndarray, axes: object = None, forward: bool = True, inorm: int = 0, out: object = None, nthreads: int = 1) -> numpy.ndarray
    
    Performs an FFT whose input is strictly real.
    
    Parameters
    ----------
    a : numpy.ndarray (any real type)
        The input data
    axes : list of integers
        The axes along which the FFT is carried out.
        If not set, all axes will be transformed in ascending order.
    forward : bool
        If `True`, a negative sign is used in the exponent, else a positive one.
    inorm : int
        Normalization type
          0 : no normalization
          1 : divide by sqrt(N)
          2 : divide by N
        where N is the product of the lengths of the transformed input axes.
    out : numpy.ndarray (complex type with same accuracy as `a`)
        For the required shape, see the `Returns` section.
        Must not overlap with `a`.
        If None, a new array is allocated to store the output.
    nthreads : int
        Number of threads to use. If 0, use the system default (typically governed
        by the `OMP_NUM_THREADS` environment variable).
    
    Returns
    -------
    numpy.ndarray (complex type with same accuracy as `a`)
        The transformed data. The shape is identical to that of the input array,
        except for the axis that was transformed last. If the length of that axis
        was n on input, it is n//2+1 on output.
    """
    pass

def r2r_fftpack(a, axes, real2hermitian, forward, inorm=0, out=None, nthreads=1): # real signature unknown; restored from __doc__
    """
    r2r_fftpack(a: numpy.ndarray, axes: object, real2hermitian: bool, forward: bool, inorm: int = 0, out: object = None, nthreads: int = 1) -> numpy.ndarray
    
    Performs a real-valued FFT using the FFTPACK storage scheme.
    
    Parameters
    ----------
    a : numpy.ndarray (any real type)
        The input data
    axes : list of integers
        The axes along which the FFT is carried out.
        If not set, all axes will be transformed.
    real2hermitian : bool
        if True, the input is purely real and the output will have Hermitian
        symmetry and be stored in FFTPACK's halfcomplex ordering, otherwise the
        opposite.
    forward : bool
        If `True`, a negative sign is used in the exponent, else a positive one.
    inorm : int
        Normalization type
          0 : no normalization
          1 : divide by sqrt(N)
          2 : divide by N
        where N is the length of `axis`.
    out : numpy.ndarray (same shape and data type as `a`)
        May be identical to `a`, but if it isn't, it must not overlap with `a`.
        If None, a new array is allocated to store the output.
    nthreads : int
        Number of threads to use. If 0, use the system default (typically governed
        by the `OMP_NUM_THREADS` environment variable).
    
    Returns
    -------
    numpy.ndarray (same shape and data type as `a`)
        The transformed data. The shape is identical to that of the input array.
    """
    pass

def separable_hartley(a, axes=None, inorm=0, out=None, nthreads=1): # real signature unknown; restored from __doc__
    """
    separable_hartley(a: numpy.ndarray, axes: object = None, inorm: int = 0, out: object = None, nthreads: int = 1) -> numpy.ndarray
    
    Performs a separable Hartley transform.
    For every requested axis, a 1D forward Fourier transform is carried out, and
    the real and imaginary parts of the result are added before the next axis is
    processed.
    
    Parameters
    ----------
    a : numpy.ndarray (any real type)
        The input data
    axes : list of integers
        The axes along which the transform is carried out.
        If not set, all axes will be transformed.
    inorm : int
        Normalization type
          0 : no normalization
          1 : divide by sqrt(N)
          2 : divide by N
        where N is the product of the lengths of the transformed axes.
    out : numpy.ndarray (same shape and data type as `a`)
        May be identical to `a`, but if it isn't, it must not overlap with `a`.
        If None, a new array is allocated to store the output.
    nthreads : int
        Number of threads to use. If 0, use the system default (typically governed
        by the `OMP_NUM_THREADS` environment variable).
    
    Returns
    -------
    numpy.ndarray (same shape and data type as `a`)
        The transformed data
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff92cf8190>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.fft._pocketfft.pypocketfft', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff92cf8190>, origin='/.venv/lib/python3.8/site-packages/scipy/fft/_pocketfft/pypocketfft.cpython-38-aarch64-linux-gnu.so')"

