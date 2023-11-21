# encoding: utf-8
# module _datetime
# from /usr/local/lib/python3.8/lib-dynload/_datetime.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
""" Fast implementation of the datetime type. """

# imports
import datetime as __datetime


# Variables with simple values

MAXYEAR = 9999

MINYEAR = 1

# no functions
# classes

class date(object):
    """ date(year, month, day) --> date object """
    def ctime(self): # real signature unknown; restored from __doc__
        """ Return ctime() style string. """
        pass

    @classmethod
    def fromisocalendar(cls, *args, **kwargs): # real signature unknown
        """
        int, int, int -> Construct a date from the ISO year, week number and weekday.
        
        This is the inverse of the date.isocalendar() function
        """
        pass

    @classmethod
    def fromisoformat(cls, *args, **kwargs): # real signature unknown
        """ str -> Construct a date from the output of date.isoformat() """
        pass

    @classmethod
    def fromordinal(cls, ordinal): # known case of _datetime.date.fromordinal
        """ int -> date corresponding to a proleptic Gregorian ordinal. """
        return date(1,1,1)

    @classmethod
    def fromtimestamp(cls, timestamp): # known case of _datetime.date.fromtimestamp
        """
        Create a date from a POSIX timestamp.
        
        The timestamp is a number, e.g. created via time.time(), that is interpreted
        as local time.
        """
        return date(1,1,1)

    def isocalendar(self): # known case of _datetime.date.isocalendar
        """ Return a 3-tuple containing ISO year, week number, and weekday. """
        return (1, 1, 1)

    def isoformat(self): # known case of _datetime.date.isoformat
        """ Return string in ISO 8601 format, YYYY-MM-DD. """
        return ""

    def isoweekday(self): # known case of _datetime.date.isoweekday
        """
        Return the day of the week represented by the date.
        Monday == 1 ... Sunday == 7
        """
        return 0

    def replace(self, year=None, month=None, day=None): # known case of _datetime.date.replace
        """ Return date with new specified fields. """
        return date(1,1,1)

    def strftime(self, format): # known case of _datetime.date.strftime
        """ format -> strftime() style string. """
        return ""

    def timetuple(self): # known case of _datetime.date.timetuple
        """ Return time tuple, compatible with time.localtime(). """
        return (0, 0, 0, 0, 0, 0, 0, 0, 0)

    @classmethod
    def today(self): # known case of _datetime.date.today
        """ Current date or datetime:  same as self.__class__.fromtimestamp(time.time()). """
        return date(1, 1, 1)

    def toordinal(self): # known case of _datetime.date.toordinal
        """ Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1. """
        return 0

    def weekday(self): # known case of _datetime.date.weekday
        """
        Return the day of the week represented by the date.
        Monday == 0 ... Sunday == 6
        """
        return 0

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Formats self with strftime. """
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

    def __init__(self, year, month, day): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(cls, year=None, month=None, day=None): # known case of _datetime.date.__new__
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ __reduce__() -> (cls, state) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    day = property(lambda self: 0)
    """:type: int"""

    month = property(lambda self: 0)
    """:type: int"""

    year = property(lambda self: 0)
    """:type: int"""


    max = datetime.date(9999, 12, 31)
    min = datetime.date(1, 1, 1)
    resolution = datetime.timedelta(days=1)


class datetime(__datetime.date):
    """
    datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])
    
    The year, month and day arguments are required. tzinfo may be None, or an
    instance of a tzinfo subclass. The remaining arguments may be ints.
    """
    def astimezone(self, tz): # known case of _datetime.datetime.astimezone
        """ tz -> convert to local time in new timezone tz """
        return datetime(1, 1, 1)

    @classmethod
    def combine(cls, date, time): # known case of _datetime.datetime.combine
        """ date, time -> datetime with same date and time fields """
        return datetime(1, 1, 1)

    def ctime(self): # real signature unknown; restored from __doc__
        """ Return ctime() style string. """
        pass

    def date(self): # known case of _datetime.datetime.date
        """ Return date object with same year, month and day. """
        return datetime(1, 1, 1)

    def dst(self): # real signature unknown; restored from __doc__
        """ Return self.tzinfo.dst(self). """
        pass

    @classmethod
    def fromisoformat(cls, *args, **kwargs): # real signature unknown
        """ string -> datetime from datetime.isoformat() output """
        pass

    @classmethod
    def fromtimestamp(cls, timestamp, tz=None): # known case of _datetime.datetime.fromtimestamp
        """ timestamp[, tz] -> tz's local time from POSIX timestamp. """
        return datetime(1, 1, 1)

    def isoformat(self, sep='T'): # known case of _datetime.datetime.isoformat
        """
        [sep] -> string in ISO 8601 format, YYYY-MM-DDT[HH[:MM[:SS[.mmm[uuu]]]]][+HH:MM].
        sep is used to separate the year from the time, and defaults to 'T'.
        The optional argument timespec specifies the number of additional terms
        of the time to include. Valid options are 'auto', 'hours', 'minutes',
        'seconds', 'milliseconds' and 'microseconds'.
        """
        return ""

    @classmethod
    def now(cls, tz=None): # known case of _datetime.datetime.now
        """
        Returns new datetime object representing current time local to tz.
        
          tz
            Timezone object.
        
        If no tz is specified, uses local timezone.
        """
        return datetime(1, 1, 1)

    def replace(self, year=None, month=None, day=None, hour=None, minute=None, second=None, microsecond=None, tzinfo=None): # known case of _datetime.datetime.replace
        """ Return datetime with new specified fields. """
        return datetime(1, 1, 1)

    @classmethod
    def strptime(cls, date_string, format): # known case of _datetime.datetime.strptime
        """ string, format -> new datetime parsed from a string (like time.strptime()). """
        return ""

    def time(self): # known case of _datetime.datetime.time
        """ Return time object with same time but with tzinfo=None. """
        return time(0, 0)

    def timestamp(self, *args, **kwargs): # real signature unknown
        """ Return POSIX timestamp as float. """
        pass

    def timetuple(self): # known case of _datetime.datetime.timetuple
        """ Return time tuple, compatible with time.localtime(). """
        return (0, 0, 0, 0, 0, 0, 0, 0, 0)

    def timetz(self): # known case of _datetime.datetime.timetz
        """ Return time object with same time and tzinfo. """
        return time(0, 0)

    def tzname(self): # real signature unknown; restored from __doc__
        """ Return self.tzinfo.tzname(self). """
        pass

    @classmethod
    def utcfromtimestamp(self, timestamp): # known case of _datetime.datetime.utcfromtimestamp
        """ Construct a naive UTC datetime from a POSIX timestamp. """
        return datetime(1, 1, 1)

    @classmethod
    def utcnow(cls): # known case of _datetime.datetime.utcnow
        """ Return a new datetime representing UTC day and time. """
        return datetime(1, 1, 1)

    def utcoffset(self): # real signature unknown; restored from __doc__
        """ Return self.tzinfo.utcoffset(self). """
        pass

    def utctimetuple(self): # known case of _datetime.datetime.utctimetuple
        """ Return UTC time tuple, compatible with time.localtime(). """
        return (0, 0, 0, 0, 0, 0, 0, 0, 0)

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
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

    def __init__(self, year, month, day, hour=None, minute=None, second=None, microsecond=None, tzinfo=None): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(cls, year=None, month=None, day=None, hour=None, minute=None, second=None, microsecond=None, tzinfo=None): # known case of _datetime.datetime.__new__
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __reduce_ex__(self, proto): # real signature unknown; restored from __doc__
        """ __reduce_ex__(proto) -> (cls, state) """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ __reduce__() -> (cls, state) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    fold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hour = property(lambda self: 0)
    """:type: int"""

    microsecond = property(lambda self: 0)
    """:type: int"""

    minute = property(lambda self: 0)
    """:type: int"""

    second = property(lambda self: 0)
    """:type: int"""

    tzinfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    max = datetime.datetime(9999, 12, 31, 23, 59, 59, 999999)
    min = datetime.datetime(1, 1, 1, 0, 0)
    resolution = datetime.timedelta(microseconds=1)


class time(object):
    """
    time([hour[, minute[, second[, microsecond[, tzinfo]]]]]) --> a time object
    
    All arguments are optional. tzinfo may be None, or an instance of
    a tzinfo subclass. The remaining arguments may be ints.
    """
    def dst(self): # real signature unknown; restored from __doc__
        """ Return self.tzinfo.dst(self). """
        pass

    @classmethod
    def fromisoformat(cls, *args, **kwargs): # real signature unknown
        """ string -> time from time.isoformat() output """
        pass

    def isoformat(self): # known case of _datetime.time.isoformat
        """
        Return string in ISO 8601 format, [HH[:MM[:SS[.mmm[uuu]]]]][+HH:MM].
        
        The optional argument timespec specifies the number of additional terms
        of the time to include. Valid options are 'auto', 'hours', 'minutes',
        'seconds', 'milliseconds' and 'microseconds'.
        """
        return ""

    def replace(self, hour=None, minute=None, second=None, microsecond=None, tzinfo=None): # known case of _datetime.time.replace
        """ Return time with new specified fields. """
        return time(0, 0)

    def strftime(self, format): # known case of _datetime.time.strftime
        """ format -> strftime() style string. """
        return ""

    def tzname(self): # real signature unknown; restored from __doc__
        """ Return self.tzinfo.tzname(self). """
        pass

    def utcoffset(self): # real signature unknown; restored from __doc__
        """ Return self.tzinfo.utcoffset(self). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Formats self with strftime. """
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

    def __init__(self, hour=None, minute=None, second=None, microsecond=None, tzinfo=None): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(cls, hour=None, minute=None, second=None, microsecond=None, tzinfo=None): # known case of _datetime.time.__new__
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce_ex__(self, proto): # real signature unknown; restored from __doc__
        """ __reduce_ex__(proto) -> (cls, state) """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ __reduce__() -> (cls, state) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    fold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hour = property(lambda self: 0)
    """:type: int"""

    microsecond = property(lambda self: 0)
    """:type: int"""

    minute = property(lambda self: 0)
    """:type: int"""

    second = property(lambda self: 0)
    """:type: int"""

    tzinfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    max = datetime.time(23, 59, 59, 999999)
    min = datetime.time(0, 0)
    resolution = datetime.timedelta(microseconds=1)


class timedelta(object):
    """
    Difference between two datetime values.
    
    timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
    
    All arguments are optional and default to 0.
    Arguments may be integers or floats, and may be positive or negative.
    """
    def total_seconds(self, *args, **kwargs): # real signature unknown
        """ Total seconds in the duration. """
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

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
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

    def __init__(self, days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0): # real signature unknown; restored from __doc__
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
    def __new__(cls, days=None, seconds=None, microseconds=None, milliseconds=None, minutes=None, hours=None, weeks=None): # known case of _datetime.timedelta.__new__
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ __reduce__() -> (cls, state) """
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

    days = property(lambda self: 0)
    """Number of days.

    :type: int
    """

    microseconds = property(lambda self: 0)
    """Number of microseconds (>= 0 and less than 1 second).

    :type: int
    """

    seconds = property(lambda self: 0)
    """Number of seconds (>= 0 and less than 1 day).

    :type: int
    """


    max = datetime.timedelta(days=999999999, seconds=86399, microseconds=999999)
    min = datetime.timedelta(days=-999999999)
    resolution = datetime.timedelta(microseconds=1)


class tzinfo(object):
    """ Abstract base class for time zone info objects. """
    def dst(self, date_time): # known case of _datetime.tzinfo.dst
        """ datetime -> DST offset as timedelta positive east of UTC. """
        return 0

    def fromutc(self, date_time): # known case of _datetime.tzinfo.fromutc
        """ datetime in UTC -> datetime in local time. """
        return datetime(1, 1, 1)

    def tzname(self, date_time): # known case of _datetime.tzinfo.tzname
        """ datetime -> string name of time zone. """
        return ""

    def utcoffset(self, date_time): # known case of _datetime.tzinfo.utcoffset
        """ datetime -> timedelta showing offset from UTC, negative values indicating West of UTC """
        return 0

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ -> (cls, state) """
        pass


class timezone(__datetime.tzinfo):
    """ Fixed offset from UTC implementation of tzinfo. """
    def dst(self, *args, **kwargs): # real signature unknown
        """ Return None. """
        pass

    def fromutc(self, *args, **kwargs): # real signature unknown
        """ datetime in UTC -> datetime in local time. """
        pass

    def tzname(self, *args, **kwargs): # real signature unknown
        """ If name is specified when timezone is created, returns the name.  Otherwise returns offset as 'UTC(+|-)HH:MM'. """
        pass

    def utcoffset(self, *args, **kwargs): # real signature unknown
        """ Return fixed offset. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getinitargs__(self, *args, **kwargs): # real signature unknown
        """ pickle support """
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

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    max = datetime.timezone(datetime.timedelta(seconds=86340))
    min = datetime.timezone(datetime.timedelta(days=-1, seconds=60))
    utc = datetime.timezone.utc


# variables with complex values

datetime_CAPI = None # (!) real value is '<capsule object "datetime.datetime_CAPI" at 0xffffac924ba0>'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924ac0>'

__spec__ = None # (!) real value is "ModuleSpec(name='_datetime', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924ac0>, origin='/usr/local/lib/python3.8/lib-dynload/_datetime.cpython-38-aarch64-linux-gnu.so')"

