# encoding: utf-8
# module scipy.stats._unuran.unuran_wrapper
# from /.venv/lib/python3.8/site-packages/scipy/stats/_unuran/unuran_wrapper.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import warnings as warnings # /usr/local/lib/python3.8/warnings.py
import threading as threading # /usr/local/lib/python3.8/threading.py
import functools as functools # /usr/local/lib/python3.8/functools.py
import numpy as np # /.venv/lib/python3.8/site-packages/numpy/__init__.py
import scipy.stats as stats # /.venv/lib/python3.8/site-packages/scipy/stats/__init__.py
from scipy.stats.unuran_wrapper import (DiscreteAliasUrn, DiscreteGuideTable, 
    Method, NumericalInverseHermite, NumericalInversePolynomial, 
    SimpleRatioUniforms, TransformedDensityRejection, UNURANError, _URNG, 
    __pyx_unpickle__URNG, _validate_domain, _validate_qmc_input)


# functions

def argsreduce(cond, *args): # reliably restored by inspect
    """
    Clean arguments to:
    
        1. Ensure all arguments are iterable (arrays of dimension at least one
        2. If cond != True and size > 1, ravel(args[i]) where ravel(condition) is
           True, in 1D.
    
        Return list of processed arguments.
    
        Examples
        --------
        >>> import numpy as np
        >>> rng = np.random.default_rng()
        >>> A = rng.random((4, 5))
        >>> B = 2
        >>> C = rng.random((1, 5))
        >>> cond = np.ones(A.shape)
        >>> [A1, B1, C1] = argsreduce(cond, A, B, C)
        >>> A1.shape
        (4, 5)
        >>> B1.shape
        (1,)
        >>> C1.shape
        (1, 5)
        >>> cond[2,:] = 0
        >>> [A1, B1, C1] = argsreduce(cond, A, B, C)
        >>> A1.shape
        (15,)
        >>> B1.shape
        (1,)
        >>> C1.shape
        (15,)
    """
    pass

def check_random_state(seed): # reliably restored by inspect
    """
    Turn `seed` into a `np.random.RandomState` instance.
    
        Parameters
        ----------
        seed : {None, int, `numpy.random.Generator`, `numpy.random.RandomState`}, optional
            If `seed` is None (or `np.random`), the `numpy.random.RandomState`
            singleton is used.
            If `seed` is an int, a new ``RandomState`` instance is used,
            seeded with `seed`.
            If `seed` is already a ``Generator`` or ``RandomState`` instance then
            that instance is used.
    
        Returns
        -------
        seed : {`numpy.random.Generator`, `numpy.random.RandomState`}
            Random number generator.
    """
    pass

def namedtuple(typename, field_names, *, rename=False, defaults=None, module=None): # reliably restored by inspect
    """
    Returns a new subclass of tuple with named fields.
    
        >>> Point = namedtuple('Point', ['x', 'y'])
        >>> Point.__doc__                   # docstring for the new class
        'Point(x, y)'
        >>> p = Point(11, y=22)             # instantiate with positional args or keywords
        >>> p[0] + p[1]                     # indexable like a plain tuple
        33
        >>> x, y = p                        # unpack like a regular tuple
        >>> x, y
        (11, 22)
        >>> p.x + p.y                       # fields also accessible by name
        33
        >>> d = p._asdict()                 # convert to a dictionary
        >>> d['x']
        11
        >>> Point(**d)                      # convert from a dictionary
        Point(x=11, y=22)
        >>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
        Point(x=100, y=22)
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class rv_frozen(object):
    # no doc
    def cdf(self, x): # reliably restored by inspect
        # no doc
        pass

    def entropy(self): # reliably restored by inspect
        # no doc
        pass

    def expect(self, func=None, lb=None, ub=None, conditional=False, **kwds): # reliably restored by inspect
        # no doc
        pass

    def interval(self, confidence=None, **kwds): # reliably restored by inspect
        # no doc
        pass

    def isf(self, q): # reliably restored by inspect
        # no doc
        pass

    def logcdf(self, x): # reliably restored by inspect
        # no doc
        pass

    def logsf(self, x): # reliably restored by inspect
        # no doc
        pass

    def mean(self): # reliably restored by inspect
        # no doc
        pass

    def median(self): # reliably restored by inspect
        # no doc
        pass

    def moment(self, order=None, **kwds): # reliably restored by inspect
        # no doc
        pass

    def ppf(self, q): # reliably restored by inspect
        # no doc
        pass

    def rvs(self, size=None, random_state=None): # reliably restored by inspect
        # no doc
        pass

    def sf(self, x): # reliably restored by inspect
        # no doc
        pass

    def stats(self, moments=None): # reliably restored by inspect
        # no doc
        pass

    def std(self): # reliably restored by inspect
        # no doc
        pass

    def support(self): # reliably restored by inspect
        # no doc
        pass

    def var(self): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, dist, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    random_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'scipy.stats._distn_infrastructure', '__init__': <function rv_frozen.__init__ at 0xffff938415e0>, 'random_state': <property object at 0xffff93839d60>, 'cdf': <function rv_frozen.cdf at 0xffff93841790>, 'logcdf': <function rv_frozen.logcdf at 0xffff93841820>, 'ppf': <function rv_frozen.ppf at 0xffff938418b0>, 'isf': <function rv_frozen.isf at 0xffff93841940>, 'rvs': <function rv_frozen.rvs at 0xffff938419d0>, 'sf': <function rv_frozen.sf at 0xffff93841a60>, 'logsf': <function rv_frozen.logsf at 0xffff93841af0>, 'stats': <function rv_frozen.stats at 0xffff93841b80>, 'median': <function rv_frozen.median at 0xffff93841c10>, 'mean': <function rv_frozen.mean at 0xffff93841ca0>, 'var': <function rv_frozen.var at 0xffff93841d30>, 'std': <function rv_frozen.std at 0xffff93841dc0>, 'moment': <function rv_frozen.moment at 0xffff93841e50>, 'entropy': <function rv_frozen.entropy at 0xffff93841ee0>, 'interval': <function rv_frozen.interval at 0xffff93841f70>, 'expect': <function rv_frozen.expect at 0xffff93843040>, 'support': <function rv_frozen.support at 0xffff938430d0>, '__dict__': <attribute '__dict__' of 'rv_frozen' objects>, '__weakref__': <attribute '__weakref__' of 'rv_frozen' objects>, '__doc__': None})"


class UError(tuple):
    """ UError(max_error, mean_absolute_error) """
    def _asdict(self): # reliably restored by inspect
        """ Return a new dict which maps field names to their values. """
        pass

    @classmethod
    def _make(cls, *args, **kwargs): # real signature unknown
        """ Make a new UError object from a sequence or iterable """
        pass

    def _replace(self, **kwds): # reliably restored by inspect
        """ Return a new UError object replacing specified fields with new values """
        pass

    def __getnewargs__(self): # reliably restored by inspect
        """ Return self as a plain tuple.  Used by copy and pickle. """
        pass

    def __init__(self, max_error, mean_absolute_error): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(_cls, max_error, mean_absolute_error): # reliably restored by inspect
        """ Create new instance of UError(max_error, mean_absolute_error) """
        pass

    def __repr__(self): # reliably restored by inspect
        """ Return a nicely formatted representation string """
        pass

    max_error = None # (!) real value is '<_collections._tuplegetter object at 0xffff92955610>'
    mean_absolute_error = None # (!) real value is '<_collections._tuplegetter object at 0xffff929555e0>'
    _fields = (
        'max_error',
        'mean_absolute_error',
    )
    _fields_defaults = {}
    _field_defaults = {}
    __slots__ = ()


# variables with complex values

__all__ = [
    'UNURANError',
    'TransformedDensityRejection',
    'DiscreteAliasUrn',
    'NumericalInversePolynomial',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924760>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.stats._unuran.unuran_wrapper', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924760>, origin='/.venv/lib/python3.8/site-packages/scipy/stats/_unuran/unuran_wrapper.cpython-38-aarch64-linux-gnu.so')"

__test__ = {
    'TransformedDensityRejection.ppf_hat (line 973)': '\n        ppf_hat(u)\n\n        Evaluate the inverse of the CDF of the hat distribution at `u`.\n\n        Parameters\n        ----------\n        u : array_like\n            An array of percentiles\n\n        Returns\n        -------\n        ppf_hat : array_like\n            Array of quantiles corresponding to the given percentiles.\n\n        Examples\n        --------\n        >>> from scipy.stats.sampling import TransformedDensityRejection\n        >>> from scipy.stats import norm\n        >>> import numpy as np\n        >>> from math import exp\n        >>>\n        >>> class MyDist:\n        ...     def pdf(self, x):\n        ...         return exp(-0.5 * x**2)\n        ...     def dpdf(self, x):\n        ...         return -x * exp(-0.5 * x**2)\n        ...\n        >>> dist = MyDist()\n        >>> rng = TransformedDensityRejection(dist)\n        >>>\n        >>> rng.ppf_hat(0.5)\n        -0.00018050266342393984\n        >>> norm.ppf(0.5)\n        0.0\n        >>> u = np.linspace(0, 1, num=1000)\n        >>> ppf_hat = rng.ppf_hat(u)\n        ',
}

