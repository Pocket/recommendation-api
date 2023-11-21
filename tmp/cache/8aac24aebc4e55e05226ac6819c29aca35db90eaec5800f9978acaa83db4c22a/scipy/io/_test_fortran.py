# encoding: utf-8
# module scipy.io._test_fortran
# from /.venv/lib/python3.8/site-packages/scipy/io/_test_fortran.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
"""
This module '_test_fortran' is auto-generated with f2py (version:2).
Functions:
  a = read_unformatted_double(m,n,k,filename)
  a = read_unformatted_int(m,n,k,filename)
  a,b = read_unformatted_mixed(m,n,k,filename)
.
"""
# no imports

# Variables with simple values

__version__ = b'$Revision: $'

# functions

def read_unformatted_double(m, n, k, filename): # real signature unknown; restored from __doc__
    """
    a = read_unformatted_double(m,n,k,filename)
    
    Wrapper for ``read_unformatted_double``.
    
    Parameters
    ----------
    m : input int
    n : input int
    k : input int
    filename : input string(len=4096)
    
    Returns
    -------
    a : rank-3 array('d') with bounds (m,n,k)
    """
    pass

def read_unformatted_int(m, n, k, filename): # real signature unknown; restored from __doc__
    """
    a = read_unformatted_int(m,n,k,filename)
    
    Wrapper for ``read_unformatted_int``.
    
    Parameters
    ----------
    m : input int
    n : input int
    k : input int
    filename : input string(len=4096)
    
    Returns
    -------
    a : rank-3 array('i') with bounds (m,n,k)
    """
    pass

def read_unformatted_mixed(m, n, k, filename): # real signature unknown; restored from __doc__
    """
    a,b = read_unformatted_mixed(m,n,k,filename)
    
    Wrapper for ``read_unformatted_mixed``.
    
    Parameters
    ----------
    m : input int
    n : input int
    k : input int
    filename : input string(len=4096)
    
    Returns
    -------
    a : rank-2 array('d') with bounds (m,n)
    b : rank-1 array('i') with bounds (k)
    """
    pass

# classes

class __test_fortran_error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924ac0>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.io._test_fortran', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924ac0>, origin='/.venv/lib/python3.8/site-packages/scipy/io/_test_fortran.cpython-38-aarch64-linux-gnu.so')"

