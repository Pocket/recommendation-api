# encoding: utf-8
# module _decimal calls itself decimal
# from /usr/local/lib/python3.8/lib-dynload/_decimal.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
""" C decimal arithmetic module """

# imports
import decimal as __decimal


# Variables with simple values

HAVE_CONTEXTVAR = True
HAVE_THREADS = True

MAX_EMAX = 999999999999999999
MAX_PREC = 999999999999999999

MIN_EMIN = -999999999999999999
MIN_ETINY = -1999999999999999997

ROUND_05UP = 'ROUND_05UP'
ROUND_CEILING = 'ROUND_CEILING'
ROUND_DOWN = 'ROUND_DOWN'
ROUND_FLOOR = 'ROUND_FLOOR'

ROUND_HALF_DOWN = 'ROUND_HALF_DOWN'
ROUND_HALF_EVEN = 'ROUND_HALF_EVEN'
ROUND_HALF_UP = 'ROUND_HALF_UP'

ROUND_UP = 'ROUND_UP'

__libmpdec_version__ = '2.4.2'

__version__ = '1.70'

# functions

def getcontext(*args, **kwargs): # real signature unknown
    """ Get the current default context. """
    pass

def localcontext(*args, **kwargs): # real signature unknown
    """
    Return a context manager that will set the default context to a copy of ctx
    on entry to the with-statement and restore the previous default context when
    exiting the with-statement. If no context is specified, a copy of the current
    default context is used.
    """
    pass

def setcontext(*args, **kwargs): # real signature unknown
    """ Set a new default context. """
    pass

# classes

class DecimalException(ArithmeticError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class Clamped(__decimal.DecimalException):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Context(object):
    """
    The context affects almost all operations and controls rounding,
    Over/Underflow, raising of exceptions and much more.  A new context
    can be constructed as follows:
    
        >>> c = Context(prec=28, Emin=-425000000, Emax=425000000,
        ...             rounding=ROUND_HALF_EVEN, capitals=1, clamp=1,
        ...             traps=[InvalidOperation, DivisionByZero, Overflow],
        ...             flags=[])
        >>>
    """
    def abs(self, *args, **kwargs): # real signature unknown
        """ Return the absolute value of x. """
        pass

    def add(self, *args, **kwargs): # real signature unknown
        """ Return the sum of x and y. """
        pass

    def canonical(self, *args, **kwargs): # real signature unknown
        """ Return a new instance of x. """
        pass

    def clear_flags(self, *args, **kwargs): # real signature unknown
        """ Reset all flags to False. """
        pass

    def clear_traps(self, *args, **kwargs): # real signature unknown
        """ Set all traps to False. """
        pass

    def compare(self, *args, **kwargs): # real signature unknown
        """ Compare x and y numerically. """
        pass

    def compare_signal(self, *args, **kwargs): # real signature unknown
        """ Compare x and y numerically.  All NaNs signal. """
        pass

    def compare_total(self, *args, **kwargs): # real signature unknown
        """ Compare x and y using their abstract representation. """
        pass

    def compare_total_mag(self, *args, **kwargs): # real signature unknown
        """ Compare x and y using their abstract representation, ignoring sign. """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        """ Return a duplicate of the context with all flags cleared. """
        pass

    def copy_abs(self, *args, **kwargs): # real signature unknown
        """ Return a copy of x with the sign set to 0. """
        pass

    def copy_decimal(self, *args, **kwargs): # real signature unknown
        """ Return a copy of Decimal x. """
        pass

    def copy_negate(self, *args, **kwargs): # real signature unknown
        """ Return a copy of x with the sign inverted. """
        pass

    def copy_sign(self, *args, **kwargs): # real signature unknown
        """ Copy the sign from y to x. """
        pass

    def create_decimal(self, *args, **kwargs): # real signature unknown
        """
        Create a new Decimal instance from num, using self as the context. Unlike the
        Decimal constructor, this function observes the context limits.
        """
        pass

    def create_decimal_from_float(self, *args, **kwargs): # real signature unknown
        """
        Create a new Decimal instance from float f.  Unlike the Decimal.from_float()
        class method, this function observes the context limits.
        """
        pass

    def divide(self, *args, **kwargs): # real signature unknown
        """ Return x divided by y. """
        pass

    def divide_int(self, *args, **kwargs): # real signature unknown
        """ Return x divided by y, truncated to an integer. """
        pass

    def divmod(self, *args, **kwargs): # real signature unknown
        """ Return quotient and remainder of the division x / y. """
        pass

    def Etiny(self, *args, **kwargs): # real signature unknown
        """
        Return a value equal to Emin - prec + 1, which is the minimum exponent value
        for subnormal results.  When underflow occurs, the exponent is set to Etiny.
        """
        pass

    def Etop(self): # real signature unknown; restored from __doc__
        """
        Return a value equal to Emax - prec + 1.  This is the maximum exponent
        if the _clamp field of the context is set to 1 (IEEE clamp mode).  Etop()
        must not be negative.
        """
        pass

    def exp(self, *args, **kwargs): # real signature unknown
        """ Return e ** x. """
        pass

    def fma(self, *args, **kwargs): # real signature unknown
        """ Return x multiplied by y, plus z. """
        pass

    def is_canonical(self, *args, **kwargs): # real signature unknown
        """ Return True if x is canonical, False otherwise. """
        pass

    def is_finite(self, *args, **kwargs): # real signature unknown
        """ Return True if x is finite, False otherwise. """
        pass

    def is_infinite(self, *args, **kwargs): # real signature unknown
        """ Return True if x is infinite, False otherwise. """
        pass

    def is_nan(self, *args, **kwargs): # real signature unknown
        """ Return True if x is a qNaN or sNaN, False otherwise. """
        pass

    def is_normal(self, *args, **kwargs): # real signature unknown
        """ Return True if x is a normal number, False otherwise. """
        pass

    def is_qnan(self, *args, **kwargs): # real signature unknown
        """ Return True if x is a quiet NaN, False otherwise. """
        pass

    def is_signed(self, *args, **kwargs): # real signature unknown
        """ Return True if x is negative, False otherwise. """
        pass

    def is_snan(self, *args, **kwargs): # real signature unknown
        """ Return True if x is a signaling NaN, False otherwise. """
        pass

    def is_subnormal(self, *args, **kwargs): # real signature unknown
        """ Return True if x is subnormal, False otherwise. """
        pass

    def is_zero(self, *args, **kwargs): # real signature unknown
        """ Return True if x is a zero, False otherwise. """
        pass

    def ln(self, *args, **kwargs): # real signature unknown
        """ Return the natural (base e) logarithm of x. """
        pass

    def log10(self, *args, **kwargs): # real signature unknown
        """ Return the base 10 logarithm of x. """
        pass

    def logb(self, *args, **kwargs): # real signature unknown
        """ Return the exponent of the magnitude of the operand's MSD. """
        pass

    def logical_and(self, *args, **kwargs): # real signature unknown
        """ Digit-wise and of x and y. """
        pass

    def logical_invert(self, *args, **kwargs): # real signature unknown
        """ Invert all digits of x. """
        pass

    def logical_or(self, *args, **kwargs): # real signature unknown
        """ Digit-wise or of x and y. """
        pass

    def logical_xor(self, *args, **kwargs): # real signature unknown
        """ Digit-wise xor of x and y. """
        pass

    def max(self, *args, **kwargs): # real signature unknown
        """ Compare the values numerically and return the maximum. """
        pass

    def max_mag(self, *args, **kwargs): # real signature unknown
        """ Compare the values numerically with their sign ignored. """
        pass

    def min(self, *args, **kwargs): # real signature unknown
        """ Compare the values numerically and return the minimum. """
        pass

    def minus(self, *args, **kwargs): # real signature unknown
        """
        Minus corresponds to the unary prefix minus operator in Python, but applies
        the context to the result.
        """
        pass

    def min_mag(self, *args, **kwargs): # real signature unknown
        """ Compare the values numerically with their sign ignored. """
        pass

    def multiply(self, *args, **kwargs): # real signature unknown
        """ Return the product of x and y. """
        pass

    def next_minus(self, *args, **kwargs): # real signature unknown
        """ Return the largest representable number smaller than x. """
        pass

    def next_plus(self, *args, **kwargs): # real signature unknown
        """ Return the smallest representable number larger than x. """
        pass

    def next_toward(self, *args, **kwargs): # real signature unknown
        """ Return the number closest to x, in the direction towards y. """
        pass

    def normalize(self, *args, **kwargs): # real signature unknown
        """ Reduce x to its simplest form. Alias for reduce(x). """
        pass

    def number_class(self, *args, **kwargs): # real signature unknown
        """ Return an indication of the class of x. """
        pass

    def plus(self, *args, **kwargs): # real signature unknown
        """
        Plus corresponds to the unary prefix plus operator in Python, but applies
        the context to the result.
        """
        pass

    def power(self, *args, **kwargs): # real signature unknown
        """
        Compute a**b. If 'a' is negative, then 'b' must be integral. The result
        will be inexact unless 'a' is integral and the result is finite and can
        be expressed exactly in 'precision' digits.  In the Python version the
        result is always correctly rounded, in the C version the result is almost
        always correctly rounded.
        
        If modulo is given, compute (a**b) % modulo. The following restrictions
        hold:
        
            * all three arguments must be integral
            * 'b' must be nonnegative
            * at least one of 'a' or 'b' must be nonzero
            * modulo must be nonzero and less than 10**prec in absolute value
        """
        pass

    def quantize(self, *args, **kwargs): # real signature unknown
        """ Return a value equal to x (rounded), having the exponent of y. """
        pass

    def radix(self, *args, **kwargs): # real signature unknown
        """ Return 10. """
        pass

    def remainder(self, *args, **kwargs): # real signature unknown
        """
        Return the remainder from integer division.  The sign of the result,
        if non-zero, is the same as that of the original dividend.
        """
        pass

    def remainder_near(self, *args, **kwargs): # real signature unknown
        """
        Return x - y * n, where n is the integer nearest the exact value of x / y
        (if the result is 0 then its sign will be the sign of x).
        """
        pass

    def rotate(self, *args, **kwargs): # real signature unknown
        """ Return a copy of x, rotated by y places. """
        pass

    def same_quantum(self, *args, **kwargs): # real signature unknown
        """ Return True if the two operands have the same exponent. """
        pass

    def scaleb(self, *args, **kwargs): # real signature unknown
        """ Return the first operand after adding the second value to its exp. """
        pass

    def shift(self, *args, **kwargs): # real signature unknown
        """ Return a copy of x, shifted by y places. """
        pass

    def sqrt(self, *args, **kwargs): # real signature unknown
        """ Square root of a non-negative number to context precision. """
        pass

    def subtract(self, *args, **kwargs): # real signature unknown
        """ Return the difference between x and y. """
        pass

    def to_eng_string(self, *args, **kwargs): # real signature unknown
        """ Convert a number to a string, using engineering notation. """
        pass

    def to_integral(self, *args, **kwargs): # real signature unknown
        """ Identical to to_integral_value(x). """
        pass

    def to_integral_exact(self, *args, **kwargs): # real signature unknown
        """ Round to an integer. Signal if the result is rounded or inexact. """
        pass

    def to_integral_value(self, *args, **kwargs): # real signature unknown
        """ Round to an integer. """
        pass

    def to_sci_string(self, *args, **kwargs): # real signature unknown
        """ Convert a number to a string using scientific notation. """
        pass

    def _apply(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, prec=28, Emin=-425000000, Emax=425000000, *more, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    capitals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    clamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Emax = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Emin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    prec = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rounding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class InvalidOperation(__decimal.DecimalException):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class ConversionSyntax(__decimal.InvalidOperation):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Decimal(object):
    """
    Construct a new Decimal object. 'value' can be an integer, string, tuple,
    or another Decimal object. If no value is given, return Decimal('0'). The
    context does not affect the conversion and is only passed to determine if
    the InvalidOperation trap is active.
    """
    def adjusted(self, *args, **kwargs): # real signature unknown
        """ Return the adjusted exponent of the number.  Defined as exp + digits - 1. """
        pass

    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Decimal.as_integer_ratio() -> (int, int)
        
        Return a pair of integers, whose ratio is exactly equal to the original
        Decimal and with a positive denominator. The ratio is in lowest terms.
        Raise OverflowError on infinities and a ValueError on NaNs.
        """
        pass

    def as_tuple(self, *args, **kwargs): # real signature unknown
        """ Return a tuple representation of the number. """
        pass

    def canonical(self, *args, **kwargs): # real signature unknown
        """
        Return the canonical encoding of the argument.  Currently, the encoding
        of a Decimal instance is always canonical, so this operation returns its
        argument unchanged.
        """
        pass

    def compare(self, *args, **kwargs): # real signature unknown
        """
        Compare self to other.  Return a decimal value:
        
            a or b is a NaN ==> Decimal('NaN')
            a < b           ==> Decimal('-1')
            a == b          ==> Decimal('0')
            a > b           ==> Decimal('1')
        """
        pass

    def compare_signal(self, *args, **kwargs): # real signature unknown
        """ Identical to compare, except that all NaNs signal. """
        pass

    def compare_total(self, Decimal, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Compare two operands using their abstract representation rather than
        their numerical value.  Similar to the compare() method, but the result
        gives a total ordering on Decimal instances.  Two Decimal instances with
        the same numeric value but different representations compare unequal
        in this ordering:
        
            >>> Decimal('12.0').compare_total(Decimal('12'))
            Decimal('-1')
        
        Quiet and signaling NaNs are also included in the total ordering. The result
        of this function is Decimal('0') if both operands have the same representation,
        Decimal('-1') if the first operand is lower in the total order than the second,
        and Decimal('1') if the first operand is higher in the total order than the
        second operand. See the specification for details of the total order.
        
        This operation is unaffected by context and is quiet: no flags are changed
        and no rounding is performed. As an exception, the C version may raise
        InvalidOperation if the second operand cannot be converted exactly.
        """
        pass

    def compare_total_mag(self, y): # real signature unknown; restored from __doc__
        """
        Compare two operands using their abstract representation rather than their
        value as in compare_total(), but ignoring the sign of each operand.
        
        x.compare_total_mag(y) is equivalent to x.copy_abs().compare_total(y.copy_abs()).
        
        This operation is unaffected by context and is quiet: no flags are changed
        and no rounding is performed. As an exception, the C version may raise
        InvalidOperation if the second operand cannot be converted exactly.
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Return self. """
        pass

    def copy_abs(self, *args, **kwargs): # real signature unknown
        """
        Return the absolute value of the argument.  This operation is unaffected by
        context and is quiet: no flags are changed and no rounding is performed.
        """
        pass

    def copy_negate(self, *args, **kwargs): # real signature unknown
        """
        Return the negation of the argument.  This operation is unaffected by context
        and is quiet: no flags are changed and no rounding is performed.
        """
        pass

    def copy_sign(self, Decimal, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Return a copy of the first operand with the sign set to be the same as the
        sign of the second operand. For example:
        
            >>> Decimal('2.3').copy_sign(Decimal('-1.5'))
            Decimal('-2.3')
        
        This operation is unaffected by context and is quiet: no flags are changed
        and no rounding is performed. As an exception, the C version may raise
        InvalidOperation if the second operand cannot be converted exactly.
        """
        pass

    def exp(self, *args, **kwargs): # real signature unknown
        """
        Return the value of the (natural) exponential function e**x at the given
        number.  The function always uses the ROUND_HALF_EVEN mode and the result
        is correctly rounded.
        """
        pass

    def fma(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Fused multiply-add.  Return self*other+third with no rounding of the
        intermediate product self*other.
        
            >>> Decimal(2).fma(3, 5)
            Decimal('11')
        """
        pass

    @classmethod
    def from_float(cls, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Class method that converts a float to a decimal number, exactly.
        Since 0.1 is not exactly representable in binary floating point,
        Decimal.from_float(0.1) is not the same as Decimal('0.1').
        
            >>> Decimal.from_float(0.1)
            Decimal('0.1000000000000000055511151231257827021181583404541015625')
            >>> Decimal.from_float(float('nan'))
            Decimal('NaN')
            >>> Decimal.from_float(float('inf'))
            Decimal('Infinity')
            >>> Decimal.from_float(float('-inf'))
            Decimal('-Infinity')
        """
        pass

    def is_canonical(self, *args, **kwargs): # real signature unknown
        """
        Return True if the argument is canonical and False otherwise.  Currently,
        a Decimal instance is always canonical, so this operation always returns
        True.
        """
        pass

    def is_finite(self, *args, **kwargs): # real signature unknown
        """
        Return True if the argument is a finite number, and False if the argument
        is infinite or a NaN.
        """
        pass

    def is_infinite(self, *args, **kwargs): # real signature unknown
        """
        Return True if the argument is either positive or negative infinity and
        False otherwise.
        """
        pass

    def is_nan(self, *args, **kwargs): # real signature unknown
        """
        Return True if the argument is a (quiet or signaling) NaN and False
        otherwise.
        """
        pass

    def is_normal(self, *args, **kwargs): # real signature unknown
        """
        Return True if the argument is a normal finite non-zero number with an
        adjusted exponent greater than or equal to Emin. Return False if the
        argument is zero, subnormal, infinite or a NaN.
        """
        pass

    def is_qnan(self, *args, **kwargs): # real signature unknown
        """ Return True if the argument is a quiet NaN, and False otherwise. """
        pass

    def is_signed(self, *args, **kwargs): # real signature unknown
        """
        Return True if the argument has a negative sign and False otherwise.
        Note that both zeros and NaNs can carry signs.
        """
        pass

    def is_snan(self, *args, **kwargs): # real signature unknown
        """ Return True if the argument is a signaling NaN and False otherwise. """
        pass

    def is_subnormal(self, *args, **kwargs): # real signature unknown
        """
        Return True if the argument is subnormal, and False otherwise. A number is
        subnormal if it is non-zero, finite, and has an adjusted exponent less
        than Emin.
        """
        pass

    def is_zero(self, *args, **kwargs): # real signature unknown
        """
        Return True if the argument is a (positive or negative) zero and False
        otherwise.
        """
        pass

    def ln(self, *args, **kwargs): # real signature unknown
        """
        Return the natural (base e) logarithm of the operand. The function always
        uses the ROUND_HALF_EVEN mode and the result is correctly rounded.
        """
        pass

    def log10(self, *args, **kwargs): # real signature unknown
        """
        Return the base ten logarithm of the operand. The function always uses the
        ROUND_HALF_EVEN mode and the result is correctly rounded.
        """
        pass

    def logb(self, *args, **kwargs): # real signature unknown
        """
        For a non-zero number, return the adjusted exponent of the operand as a
        Decimal instance.  If the operand is a zero, then Decimal('-Infinity') is
        returned and the DivisionByZero condition is raised. If the operand is
        an infinity then Decimal('Infinity') is returned.
        """
        pass

    def logical_and(self, *args, **kwargs): # real signature unknown
        """ Return the digit-wise 'and' of the two (logical) operands. """
        pass

    def logical_invert(self, *args, **kwargs): # real signature unknown
        """ Return the digit-wise inversion of the (logical) operand. """
        pass

    def logical_or(self, *args, **kwargs): # real signature unknown
        """ Return the digit-wise 'or' of the two (logical) operands. """
        pass

    def logical_xor(self, *args, **kwargs): # real signature unknown
        """ Return the digit-wise 'exclusive or' of the two (logical) operands. """
        pass

    def max(self, *args, **kwargs): # real signature unknown
        """
        Maximum of self and other.  If one operand is a quiet NaN and the other is
        numeric, the numeric operand is returned.
        """
        pass

    def max_mag(self, *args, **kwargs): # real signature unknown
        """
        Similar to the max() method, but the comparison is done using the absolute
        values of the operands.
        """
        pass

    def min(self, *args, **kwargs): # real signature unknown
        """
        Minimum of self and other. If one operand is a quiet NaN and the other is
        numeric, the numeric operand is returned.
        """
        pass

    def min_mag(self, *args, **kwargs): # real signature unknown
        """
        Similar to the min() method, but the comparison is done using the absolute
        values of the operands.
        """
        pass

    def next_minus(self, *args, **kwargs): # real signature unknown
        """
        Return the largest number representable in the given context (or in the
        current default context if no context is given) that is smaller than the
        given operand.
        """
        pass

    def next_plus(self, *args, **kwargs): # real signature unknown
        """
        Return the smallest number representable in the given context (or in the
        current default context if no context is given) that is larger than the
        given operand.
        """
        pass

    def next_toward(self, *args, **kwargs): # real signature unknown
        """
        If the two operands are unequal, return the number closest to the first
        operand in the direction of the second operand.  If both operands are
        numerically equal, return a copy of the first operand with the sign set
        to be the same as the sign of the second operand.
        """
        pass

    def normalize(self, *args, **kwargs): # real signature unknown
        """
        Normalize the number by stripping the rightmost trailing zeros and
        converting any result equal to Decimal('0') to Decimal('0e0').  Used
        for producing canonical values for members of an equivalence class.
        For example, Decimal('32.100') and Decimal('0.321000e+2') both normalize
        to the equivalent value Decimal('32.1').
        """
        pass

    def number_class(self, *args, **kwargs): # real signature unknown
        """
        Return a string describing the class of the operand.  The returned value
        is one of the following ten strings:
        
            * '-Infinity', indicating that the operand is negative infinity.
            * '-Normal', indicating that the operand is a negative normal number.
            * '-Subnormal', indicating that the operand is negative and subnormal.
            * '-Zero', indicating that the operand is a negative zero.
            * '+Zero', indicating that the operand is a positive zero.
            * '+Subnormal', indicating that the operand is positive and subnormal.
            * '+Normal', indicating that the operand is a positive normal number.
            * '+Infinity', indicating that the operand is positive infinity.
            * 'NaN', indicating that the operand is a quiet NaN (Not a Number).
            * 'sNaN', indicating that the operand is a signaling NaN.
        """
        pass

    def quantize(self, Decimal, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Return a value equal to the first operand after rounding and having the
        exponent of the second operand.
        
            >>> Decimal('1.41421356').quantize(Decimal('1.000'))
            Decimal('1.414')
        
        Unlike other operations, if the length of the coefficient after the quantize
        operation would be greater than precision, then an InvalidOperation is signaled.
        This guarantees that, unless there is an error condition, the quantized exponent
        is always equal to that of the right-hand operand.
        
        Also unlike other operations, quantize never signals Underflow, even if the
        result is subnormal and inexact.
        
        If the exponent of the second operand is larger than that of the first, then
        rounding may be necessary. In this case, the rounding mode is determined by the
        rounding argument if given, else by the given context argument; if neither
        argument is given, the rounding mode of the current thread's context is used.
        """
        pass

    def radix(self, base): # real signature unknown; restored from __doc__
        """
        Return Decimal(10), the radix (base) in which the Decimal class does
        all its arithmetic. Included for compatibility with the specification.
        """
        pass

    def remainder_near(self, *args, **kwargs): # real signature unknown
        """
        Return the remainder from dividing self by other.  This differs from
        self % other in that the sign of the remainder is chosen so as to minimize
        its absolute value. More precisely, the return value is self - n * other
        where n is the integer nearest to the exact value of self / other, and
        if two integers are equally near then the even one is chosen.
        
        If the result is zero then its sign will be the sign of self.
        """
        pass

    def rotate(self, *args, **kwargs): # real signature unknown
        """
        Return the result of rotating the digits of the first operand by an amount
        specified by the second operand.  The second operand must be an integer in
        the range -precision through precision. The absolute value of the second
        operand gives the number of places to rotate. If the second operand is
        positive then rotation is to the left; otherwise rotation is to the right.
        The coefficient of the first operand is padded on the left with zeros to
        length precision if necessary. The sign and exponent of the first operand are
        unchanged.
        """
        pass

    def same_quantum(self, *args, **kwargs): # real signature unknown
        """
        Test whether self and other have the same exponent or whether both are NaN.
        
        This operation is unaffected by context and is quiet: no flags are changed
        and no rounding is performed. As an exception, the C version may raise
        InvalidOperation if the second operand cannot be converted exactly.
        """
        pass

    def scaleb(self, *args, **kwargs): # real signature unknown
        """
        Return the first operand with the exponent adjusted the second.  Equivalently,
        return the first operand multiplied by 10**other. The second operand must be
        an integer.
        """
        pass

    def shift(self, *args, **kwargs): # real signature unknown
        """
        Return the result of shifting the digits of the first operand by an amount
        specified by the second operand.  The second operand must be an integer in
        the range -precision through precision. The absolute value of the second
        operand gives the number of places to shift. If the second operand is
        positive, then the shift is to the left; otherwise the shift is to the
        right. Digits shifted into the coefficient are zeros. The sign and exponent
        of the first operand are unchanged.
        """
        pass

    def sqrt(self, *args, **kwargs): # real signature unknown
        """
        Return the square root of the argument to full precision. The result is
        correctly rounded using the ROUND_HALF_EVEN rounding mode.
        """
        pass

    def to_eng_string(self, *args, **kwargs): # real signature unknown
        """
        Convert to an engineering-type string.  Engineering notation has an exponent
        which is a multiple of 3, so there are up to 3 digits left of the decimal
        place. For example, Decimal('123E+1') is converted to Decimal('1.23E+3').
        
        The value of context.capitals determines whether the exponent sign is lower
        or upper case. Otherwise, the context does not affect the operation.
        """
        pass

    def to_integral(self): # real signature unknown; restored from __doc__
        """
        Identical to the to_integral_value() method.  The to_integral() name has been
        kept for compatibility with older versions.
        """
        pass

    def to_integral_exact(self, *args, **kwargs): # real signature unknown
        """
        Round to the nearest integer, signaling Inexact or Rounded as appropriate if
        rounding occurs.  The rounding mode is determined by the rounding parameter
        if given, else by the given context. If neither parameter is given, then the
        rounding mode of the current default context is used.
        """
        pass

    def to_integral_value(self, *args, **kwargs): # real signature unknown
        """
        Round to the nearest integer without signaling Inexact or Rounded.  The
        rounding mode is determined by the rounding parameter if given, else by
        the given context. If neither parameter is given, then the rounding mode
        of the current default context is used.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        pass

    def __complex__(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
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

    def __floor__(self, *args, **kwargs): # real signature unknown
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
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

    def __init__(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
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

    def __reduce__(self, *args, **kwargs): # real signature unknown
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

    def __round__(self, *args, **kwargs): # real signature unknown
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

    def __sizeof__(self, *args, **kwargs): # real signature unknown
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

    def __trunc__(self, *args, **kwargs): # real signature unknown
        pass

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class DecimalTuple(tuple):
    """ DecimalTuple(sign, digits, exponent) """
    def _asdict(self): # reliably restored by inspect
        """ Return a new dict which maps field names to their values. """
        pass

    @classmethod
    def _make(cls, *args, **kwargs): # real signature unknown
        """ Make a new DecimalTuple object from a sequence or iterable """
        pass

    def _replace(self, **kwds): # reliably restored by inspect
        """ Return a new DecimalTuple object replacing specified fields with new values """
        pass

    def __getnewargs__(self): # reliably restored by inspect
        """ Return self as a plain tuple.  Used by copy and pickle. """
        pass

    def __init__(self, sign, digits, exponent): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(_cls, sign, digits, exponent): # reliably restored by inspect
        """ Create new instance of DecimalTuple(sign, digits, exponent) """
        pass

    def __repr__(self): # reliably restored by inspect
        """ Return a nicely formatted representation string """
        pass

    digits = None # (!) real value is '<_collections._tuplegetter object at 0xffffac9132b0>'
    exponent = None # (!) real value is '<_collections._tuplegetter object at 0xffffac913370>'
    sign = None # (!) real value is '<_collections._tuplegetter object at 0xffffac9132e0>'
    _fields = (
        'sign',
        'digits',
        'exponent',
    )
    _fields_defaults = {}
    _field_defaults = {}
    __slots__ = ()


class DivisionByZero(__decimal.DecimalException, ZeroDivisionError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DivisionImpossible(__decimal.InvalidOperation):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DivisionUndefined(__decimal.InvalidOperation, ZeroDivisionError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class FloatOperation(__decimal.DecimalException, TypeError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Inexact(__decimal.DecimalException):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class InvalidContext(__decimal.InvalidOperation):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Rounded(__decimal.DecimalException):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Overflow(__decimal.Inexact, __decimal.Rounded):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Subnormal(__decimal.DecimalException):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Underflow(__decimal.Inexact, __decimal.Rounded, __decimal.Subnormal):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values

BasicContext = None # (!) real value is 'Context(prec=9, rounding=ROUND_HALF_UP, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[], traps=[Clamped, InvalidOperation, DivisionByZero, Overflow, Underflow])'

DefaultContext = None # (!) real value is 'Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])'

ExtendedContext = None # (!) real value is 'Context(prec=9, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[], traps=[])'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924ac0>'

__spec__ = None # (!) real value is "ModuleSpec(name='_decimal', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924ac0>, origin='/usr/local/lib/python3.8/lib-dynload/_decimal.cpython-38-aarch64-linux-gnu.so')"

