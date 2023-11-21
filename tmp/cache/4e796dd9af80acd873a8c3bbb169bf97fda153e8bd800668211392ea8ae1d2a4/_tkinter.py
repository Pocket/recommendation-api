# encoding: utf-8
# module _tkinter
# from /usr/local/lib/python3.8/lib-dynload/_tkinter.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

# Variables with simple values

ALL_EVENTS = -3

DONT_WAIT = 2

EXCEPTION = 8

FILE_EVENTS = 8

IDLE_EVENTS = 32

READABLE = 2

TCL_VERSION = '8.6'

TIMER_EVENTS = 16

TK_VERSION = '8.6'

WINDOW_EVENTS = 4

WRITABLE = 4

# functions

def create(*args, **kwargs): # real signature unknown
    """
    wantTk
        if false, then Tk_Init() doesn't get called
      sync
        if true, then pass -sync to wish
      use
        if not None, then pass -use to wish
    """
    pass

def getbusywaitinterval(*args, **kwargs): # real signature unknown
    """ Return the current busy-wait interval between successive calls to Tcl_DoOneEvent in a threaded Python interpreter. """
    pass

def setbusywaitinterval(*args, **kwargs): # real signature unknown
    """
    Set the busy-wait interval in milliseconds between successive calls to Tcl_DoOneEvent in a threaded Python interpreter.
    
    It should be set to a divisor of the maximum time between frames in an animation.
    """
    pass

def _flatten(*args, **kwargs): # real signature unknown
    pass

# classes

class TclError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class Tcl_Obj(object):
    # no doc
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

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
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

    string = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the string representation of this object, either as str or bytes"""

    typename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """name of the Tcl type"""


    __hash__ = None


class TkappType(object):
    # no doc
    def adderrorinfo(self, *args, **kwargs): # real signature unknown
        pass

    def call(self, *args, **kwargs): # real signature unknown
        pass

    def createcommand(self, *args, **kwargs): # real signature unknown
        pass

    def createfilehandler(self, *args, **kwargs): # real signature unknown
        pass

    def createtimerhandler(self, *args, **kwargs): # real signature unknown
        pass

    def deletecommand(self, *args, **kwargs): # real signature unknown
        pass

    def deletefilehandler(self, *args, **kwargs): # real signature unknown
        pass

    def dooneevent(self, *args, **kwargs): # real signature unknown
        pass

    def eval(self, *args, **kwargs): # real signature unknown
        pass

    def evalfile(self, *args, **kwargs): # real signature unknown
        pass

    def exprboolean(self, *args, **kwargs): # real signature unknown
        pass

    def exprdouble(self, *args, **kwargs): # real signature unknown
        pass

    def exprlong(self, *args, **kwargs): # real signature unknown
        pass

    def exprstring(self, *args, **kwargs): # real signature unknown
        pass

    def getboolean(self, *args, **kwargs): # real signature unknown
        pass

    def getdouble(self, *args, **kwargs): # real signature unknown
        pass

    def getint(self, *args, **kwargs): # real signature unknown
        pass

    def getvar(self, *args, **kwargs): # real signature unknown
        pass

    def globalgetvar(self, *args, **kwargs): # real signature unknown
        pass

    def globalsetvar(self, *args, **kwargs): # real signature unknown
        pass

    def globalunsetvar(self, *args, **kwargs): # real signature unknown
        pass

    def interpaddr(self, *args, **kwargs): # real signature unknown
        pass

    def loadtk(self, *args, **kwargs): # real signature unknown
        pass

    def mainloop(self, *args, **kwargs): # real signature unknown
        pass

    def quit(self, *args, **kwargs): # real signature unknown
        pass

    def record(self, *args, **kwargs): # real signature unknown
        pass

    def setvar(self, *args, **kwargs): # real signature unknown
        pass

    def split(self, *args, **kwargs): # real signature unknown
        pass

    def splitlist(self, *args, **kwargs): # real signature unknown
        pass

    def unsetvar(self, *args, **kwargs): # real signature unknown
        pass

    def wantobjects(self, *args, **kwargs): # real signature unknown
        pass

    def willdispatch(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class TkttType(object):
    # no doc
    def deletetimerhandler(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924ac0>'

__spec__ = None # (!) real value is "ModuleSpec(name='_tkinter', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924ac0>, origin='/usr/local/lib/python3.8/lib-dynload/_tkinter.cpython-38-aarch64-linux-gnu.so')"

