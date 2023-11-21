# encoding: utf-8
# module parser
# from /usr/local/lib/python3.8/lib-dynload/parser.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
""" This is an interface to Python's internal parser. """
# no imports

# Variables with simple values

__copyright__ = 'Copyright 1995-1996 by Virginia Polytechnic Institute & State\nUniversity, Blacksburg, Virginia, USA, and Fred L. Drake, Jr., Reston,\nVirginia, USA.  Portions copyright 1991-1995 by Stichting Mathematisch\nCentrum, Amsterdam, The Netherlands.'

__version__ = '0.5'

# functions

def compilest(*args, **kwargs): # real signature unknown
    """ Compiles an ST object into a code object. """
    pass

def expr(*args, **kwargs): # real signature unknown
    """ Creates an ST object from an expression. """
    pass

def isexpr(*args, **kwargs): # real signature unknown
    """ Determines if an ST object was created from an expression. """
    pass

def issuite(*args, **kwargs): # real signature unknown
    """ Determines if an ST object was created from a suite. """
    pass

def sequence2st(*args, **kwargs): # real signature unknown
    """ Creates an ST object from a tree representation. """
    pass

def st2list(*args, **kwargs): # real signature unknown
    """ Creates a list-tree representation of an ST. """
    pass

def st2tuple(*args, **kwargs): # real signature unknown
    """ Creates a tuple-tree representation of an ST. """
    pass

def suite(*args, **kwargs): # real signature unknown
    """ Creates an ST object from a suite. """
    pass

def tuple2st(*args, **kwargs): # real signature unknown
    """ Creates an ST object from a tree representation. """
    pass

def _pickler(*args, **kwargs): # real signature unknown
    """ Returns the pickle magic to allow ST objects to be pickled. """
    pass

# classes

class ParserError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class STType(object):
    """ Intermediate representation of a Python parse tree. """
    def compile(self, *args, **kwargs): # real signature unknown
        """ Compile this ST object into a code object. """
        pass

    def isexpr(self, *args, **kwargs): # real signature unknown
        """ Determines if this ST object was created from an expression. """
        pass

    def issuite(self, *args, **kwargs): # real signature unknown
        """ Determines if this ST object was created from a suite. """
        pass

    def tolist(self, *args, **kwargs): # real signature unknown
        """ Creates a list-tree representation of this ST. """
        pass

    def totuple(self, *args, **kwargs): # real signature unknown
        """ Creates a tuple-tree representation of this ST. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
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

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
        pass

    __hash__ = None


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac9245e0>'

__spec__ = None # (!) real value is "ModuleSpec(name='parser', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac9245e0>, origin='/usr/local/lib/python3.8/lib-dynload/parser.cpython-38-aarch64-linux-gnu.so')"

