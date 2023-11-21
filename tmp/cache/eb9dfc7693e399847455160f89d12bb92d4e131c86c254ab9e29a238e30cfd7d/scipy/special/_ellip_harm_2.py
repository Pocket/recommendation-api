# encoding: utf-8
# module scipy.special._ellip_harm_2
# from /.venv/lib/python3.8/site-packages/scipy/special/_ellip_harm_2.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

# Variables with simple values

nan = nan

# functions

def _ellipsoid(*args, **kwargs): # real signature unknown
    pass

def _ellipsoid_norm(*args, **kwargs): # real signature unknown
    pass

# classes

class LowLevelCallable(tuple):
    """
    Low-level callback function.
    
        Parameters
        ----------
        function : {PyCapsule, ctypes function pointer, cffi function pointer}
            Low-level callback function.
        user_data : {PyCapsule, ctypes void pointer, cffi void pointer}
            User data to pass on to the callback function.
        signature : str, optional
            Signature of the function. If omitted, determined from *function*,
            if possible.
    
        Attributes
        ----------
        function
            Callback function given.
        user_data
            User data given.
        signature
            Signature of the function.
    
        Methods
        -------
        from_cython
            Class method for constructing callables from Cython C-exported
            functions.
    
        Notes
        -----
        The argument ``function`` can be one of:
    
        - PyCapsule, whose name contains the C function signature
        - ctypes function pointer
        - cffi function pointer
    
        The signature of the low-level callback must match one of those expected
        by the routine it is passed to.
    
        If constructing low-level functions from a PyCapsule, the name of the
        capsule must be the corresponding signature, in the format::
    
            return_type (arg1_type, arg2_type, ...)
    
        For example::
    
            "void (double)"
            "double (double, int *, void *)"
    
        The context of a PyCapsule passed in as ``function`` is used as ``user_data``,
        if an explicit value for ``user_data`` was not given.
    """
    @classmethod
    def from_cython(cls, *args, **kwargs): # real signature unknown
        """
        Create a low-level callback function from an exported Cython function.
        
                Parameters
                ----------
                module : module
                    Cython module where the exported function resides
                name : str
                    Name of the exported function
                user_data : {PyCapsule, ctypes void pointer, cffi void pointer}, optional
                    User data to pass on to the callback function.
                signature : str, optional
                    Signature of the function. If omitted, determined from *function*.
        """
        pass

    @classmethod
    def _parse_callback(cls, *args, **kwargs): # real signature unknown
        pass

    def __getitem__(self, idx): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(cls, function, user_data=None, signature=None): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    function = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    signature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    user_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __slots__ = ()


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff92e5d490>'

__pyx_capi__ = {
    '_F_integrand': None, # (!) real value is '<capsule object "double (double, void *)" at 0xffff92e5d330>'
    '_F_integrand1': None, # (!) real value is '<capsule object "double (double, void *)" at 0xffff92e5d360>'
    '_F_integrand2': None, # (!) real value is '<capsule object "double (double, void *)" at 0xffff92e5d390>'
    '_F_integrand3': None, # (!) real value is '<capsule object "double (double, void *)" at 0xffff92e5d450>'
    '_F_integrand4': None, # (!) real value is '<capsule object "double (double, void *)" at 0xffff92e5d420>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.special._ellip_harm_2', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff92e5d490>, origin='/.venv/lib/python3.8/site-packages/scipy/special/_ellip_harm_2.cpython-38-aarch64-linux-gnu.so')"

__test__ = {}

