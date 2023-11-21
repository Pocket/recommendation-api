# encoding: utf-8
# module scipy.linalg._solve_toeplitz
# from /.venv/lib/python3.8/site-packages/scipy/linalg/_solve_toeplitz.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as __numpy


# functions

def asarray(a, dtype=None, order=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    asarray(a, dtype=None, order=None, *, like=None)
    
        Convert the input to an array.
    
        Parameters
        ----------
        a : array_like
            Input data, in any form that can be converted to an array.  This
            includes lists, lists of tuples, tuples, tuples of tuples, tuples
            of lists and ndarrays.
        dtype : data-type, optional
            By default, the data-type is inferred from the input data.
        order : {'C', 'F', 'A', 'K'}, optional
            Memory layout.  'A' and 'K' depend on the order of input array a.
            'C' row-major (C-style),
            'F' column-major (Fortran-style) memory representation.
            'A' (any) means 'F' if `a` is Fortran contiguous, 'C' otherwise
            'K' (keep) preserve input order
            Defaults to 'K'.
        like : array_like, optional
            Reference object to allow the creation of arrays which are not
            NumPy arrays. If an array-like passed in as ``like`` supports
            the ``__array_function__`` protocol, the result will be defined
            by it. In this case, it ensures the creation of an array object
            compatible with that passed in via this argument.
    
            .. versionadded:: 1.20.0
    
        Returns
        -------
        out : ndarray
            Array interpretation of `a`.  No copy is performed if the input
            is already an ndarray with matching dtype and order.  If `a` is a
            subclass of ndarray, a base class ndarray is returned.
    
        See Also
        --------
        asanyarray : Similar function which passes through subclasses.
        ascontiguousarray : Convert input to a contiguous array.
        asfarray : Convert input to a floating point ndarray.
        asfortranarray : Convert input to an ndarray with column-major
                         memory order.
        asarray_chkfinite : Similar function which checks input for NaNs and Infs.
        fromiter : Create an array from an iterator.
        fromfunction : Construct an array by executing a function on grid
                       positions.
    
        Examples
        --------
        Convert a list into an array:
    
        >>> a = [1, 2]
        >>> np.asarray(a)
        array([1, 2])
    
        Existing arrays are not copied:
    
        >>> a = np.array([1, 2])
        >>> np.asarray(a) is a
        True
    
        If `dtype` is set, array is copied only if dtype does not match:
    
        >>> a = np.array([1, 2], dtype=np.float32)
        >>> np.asarray(a, dtype=np.float32) is a
        True
        >>> np.asarray(a, dtype=np.float64) is a
        False
    
        Contrary to `asanyarray`, ndarray subclasses are not passed through:
    
        >>> issubclass(np.recarray, np.ndarray)
        True
        >>> a = np.array([(1.0, 2), (3.0, 4)], dtype='f4,i4').view(np.recarray)
        >>> np.asarray(a) is a
        False
        >>> np.asanyarray(a) is a
        True
    """
    pass

def levinson(*args, **kwargs): # real signature unknown
    """
    Solve a linear Toeplitz system using Levinson recursion.
    
        Parameters
        ----------
        a : array, dtype=double or complex128, shape=(2n-1,)
            The first column of the matrix in reverse order (without the diagonal)
            followed by the first (see below)
        b : array, dtype=double  or complex128, shape=(n,)
            The right hand side vector. Both a and b must have the same type
            (double or complex128).
    
        Notes
        -----
        For example, the 5x5 toeplitz matrix below should be represented as
        the linear array ``a`` on the right ::
    
            [ a0    a1   a2  a3  a4 ]
            [ a-1   a0   a1  a2  a3 ]
            [ a-2  a-1   a0  a1  a2 ] -> [a-4  a-3  a-2  a-1  a0  a1  a2  a3  a4]
            [ a-3  a-2  a-1  a0  a1 ]
            [ a-4  a-3  a-2  a-1 a0 ]
    
        Returns
        -------
        x : arrray, shape=(n,)
            The solution vector
        reflection_coeff : array, shape=(n+1,)
            Toeplitz reflection coefficients. When a is symmetric Toeplitz and
            ``b`` is ``a[n:]``, as in the solution of autoregressive systems,
            then ``reflection_coeff`` also correspond to the partial
            autocorrelation function.
    """
    pass

def zeros(shape, dtype=None, order='C', *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    zeros(shape, dtype=float, order='C', *, like=None)
    
        Return a new array of given shape and type, filled with zeros.
    
        Parameters
        ----------
        shape : int or tuple of ints
            Shape of the new array, e.g., ``(2, 3)`` or ``2``.
        dtype : data-type, optional
            The desired data-type for the array, e.g., `numpy.int8`.  Default is
            `numpy.float64`.
        order : {'C', 'F'}, optional, default: 'C'
            Whether to store multi-dimensional data in row-major
            (C-style) or column-major (Fortran-style) order in
            memory.
        like : array_like, optional
            Reference object to allow the creation of arrays which are not
            NumPy arrays. If an array-like passed in as ``like`` supports
            the ``__array_function__`` protocol, the result will be defined
            by it. In this case, it ensures the creation of an array object
            compatible with that passed in via this argument.
    
            .. versionadded:: 1.20.0
    
        Returns
        -------
        out : ndarray
            Array of zeros with the given shape, dtype, and order.
    
        See Also
        --------
        zeros_like : Return an array of zeros with shape and type of input.
        empty : Return a new uninitialized array.
        ones : Return a new array setting values to one.
        full : Return a new array of given shape filled with value.
    
        Examples
        --------
        >>> np.zeros(5)
        array([ 0.,  0.,  0.,  0.,  0.])
    
        >>> np.zeros((5,), dtype=int)
        array([0, 0, 0, 0, 0])
    
        >>> np.zeros((2, 1))
        array([[ 0.],
               [ 0.]])
    
        >>> s = (2,2)
        >>> np.zeros(s)
        array([[ 0.,  0.],
               [ 0.,  0.]])
    
        >>> np.zeros((2,), dtype=[('x', 'i4'), ('y', 'i4')]) # custom dtype
        array([(0, 0), (0, 0)],
              dtype=[('x', '<i4'), ('y', '<i4')])
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class complex128(__numpy.complexfloating, complex):
    """
    Complex number type composed of two double-precision floating-point
        numbers, compatible with Python `complex`.
    
        :Character code: ``'D'``
        :Canonical name: `numpy.cdouble`
        :Alias: `numpy.cfloat`
        :Alias: `numpy.complex_`
        :Alias on this platform (Linux aarch64): `numpy.complex128`: Complex number type composed of 2 64-bit-precision floating-point numbers.
    """
    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    @classmethod
    def __class_getitem__(cls, *args, **kwargs): # real signature unknown
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass


class float64(__numpy.floating, float):
    """
    Double-precision floating-point number type, compatible with Python `float`
        and C ``double``.
    
        :Character code: ``'d'``
        :Canonical name: `numpy.double`
        :Alias: `numpy.float_`
        :Alias on this platform (Linux aarch64): `numpy.float64`: 64-bit precision floating-point number type: sign bit, 11 bits exponent, 52 bits mantissa.
    """
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        double.as_integer_ratio() -> (int, int)
        
                Return a pair of integers, whose ratio is exactly equal to the original
                floating point number, and with a positive denominator.
                Raise `OverflowError` on infinities and a `ValueError` on NaNs.
        
                >>> np.double(10.0).as_integer_ratio()
                (10, 1)
                >>> np.double(0.0).as_integer_ratio()
                (0, 1)
                >>> np.double(-.25).as_integer_ratio()
                (-1, 4)
        """
        pass

    def is_integer(self): # real signature unknown; restored from __doc__
        """
        double.is_integer() -> bool
        
                Return ``True`` if the floating point number is finite with integral
                value, and ``False`` otherwise.
        
                .. versionadded:: 1.22
        
                Examples
                --------
                >>> np.double(-2.0).is_integer()
                True
                >>> np.double(3.2).is_integer()
                False
        """
        return False

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    @classmethod
    def __class_getitem__(cls, *args, **kwargs): # real signature unknown
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass


class LinAlgError(Exception):
    """
    Generic Python-exception-derived object raised by linalg functions.
    
        General purpose exception class, derived from Python's exception.Exception
        class, programmatically raised in linalg functions when a Linear
        Algebra-related condition would prevent further correct execution of the
        function.
    
        Parameters
        ----------
        None
    
        Examples
        --------
        >>> from numpy import linalg as LA
        >>> LA.inv(np.zeros((2,2)))
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
          File "...linalg.py", line 350,
            in inv return wrap(solve(a, identity(a.shape[0], dtype=a.dtype)))
          File "...linalg.py", line 249,
            in solve
            raise LinAlgError('Singular matrix')
        numpy.linalg.LinAlgError: Singular matrix
    """
    def __init__(self, Singular_matrix): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9f887340>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.linalg._solve_toeplitz', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9f887340>, origin='/.venv/lib/python3.8/site-packages/scipy/linalg/_solve_toeplitz.cpython-38-aarch64-linux-gnu.so')"

__test__ = {}

