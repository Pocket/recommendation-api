# encoding: utf-8
# module scipy.signal._spectral
# from /.venv/lib/python3.8/site-packages/scipy/signal/_spectral.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
""" Tools for spectral analysis of unequally sampled signals. """
# no imports

# functions

def _lombscargle(x, y, freqs): # real signature unknown; restored from __doc__
    """
    _lombscargle(x, y, freqs)
    
    Supported prototypes:
    
    - _lombscargle(float64[:], float64[:], float64[:])
    
    Computes the Lomb-Scargle periodogram.
    
    Parameters
    ----------
    x : array_like
        Sample times.
    y : array_like
        Measurement values (must be registered so the mean is zero).
    freqs : array_like
        Angular frequencies for output periodogram.
    
    Returns
    -------
    pgram : array_like
        Lomb-Scargle periodogram.
    
    Raises
    ------
    ValueError
        If the input arrays `x` and `y` do not have the same shape.
    
    See also
    --------
    lombscargle
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9d1c56a0>'

__pythran__ = (
    '0.12.1',
    '2023-02-19 18:20:37.253039',
    'b56cff7c57981a37e4a502cd99394a47b45590ea94b06fe3923cf38ac2cdffd3',
)

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.signal._spectral', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9d1c56a0>, origin='/.venv/lib/python3.8/site-packages/scipy/signal/_spectral.cpython-38-aarch64-linux-gnu.so')"

