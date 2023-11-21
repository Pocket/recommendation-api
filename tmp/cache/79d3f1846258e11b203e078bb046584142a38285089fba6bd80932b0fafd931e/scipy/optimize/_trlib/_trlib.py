# encoding: utf-8
# module scipy.optimize._trlib._trlib
# from /.venv/lib/python3.8/site-packages/scipy/optimize/_trlib/_trlib.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /.venv/lib/python3.8/site-packages/numpy/__init__.py
import scipy.optimize._trustregion as __scipy_optimize__trustregion


# functions

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class BaseQuadraticSubproblem(object):
    """
    Base/abstract class defining the quadratic model for trust-region
        minimization. Child classes must implement the ``solve`` method.
    
        Values of the objective function, Jacobian and Hessian (if provided) at
        the current iterate ``x`` are evaluated on demand and then stored as
        attributes ``fun``, ``jac``, ``hess``.
    """
    def get_boundaries_intersections(self, z, d, trust_radius): # reliably restored by inspect
        """
        Solve the scalar quadratic equation ||z + t d|| == trust_radius.
                This is like a line-sphere intersection.
                Return the two values of t, sorted from low to high.
        """
        pass

    def hessp(self, p): # reliably restored by inspect
        # no doc
        pass

    def solve(self, trust_radius): # reliably restored by inspect
        # no doc
        pass

    def __call__(self, p): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, x, fun, jac, hess=None, hessp=None): # reliably restored by inspect
        # no doc
        pass

    fun = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Value of objective function at current iteration."""

    hess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Value of Hessian of objective function at current iteration."""

    jac = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Value of Jacobian of objective function at current iteration."""

    jac_mag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Magnitude of jacobian of objective function at current iteration."""

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'scipy.optimize._trustregion', '__doc__': '\\n    Base/abstract class defining the quadratic model for trust-region\\n    minimization. Child classes must implement the ``solve`` method.\\n\\n    Values of the objective function, Jacobian and Hessian (if provided) at\\n    the current iterate ``x`` are evaluated on demand and then stored as\\n    attributes ``fun``, ``jac``, ``hess``.\\n    ', '__init__': <function BaseQuadraticSubproblem.__init__ at 0xffff9307ae50>, '__call__': <function BaseQuadraticSubproblem.__call__ at 0xffff9307aee0>, 'fun': <property object at 0xffff93080860>, 'jac': <property object at 0xffff930808b0>, 'hess': <property object at 0xffff93080900>, 'hessp': <function BaseQuadraticSubproblem.hessp at 0xffff93083160>, 'jac_mag': <property object at 0xffff93080950>, 'get_boundaries_intersections': <function BaseQuadraticSubproblem.get_boundaries_intersections at 0xffff93083280>, 'solve': <function BaseQuadraticSubproblem.solve at 0xffff93083310>, '__dict__': <attribute '__dict__' of 'BaseQuadraticSubproblem' objects>, '__weakref__': <attribute '__weakref__' of 'BaseQuadraticSubproblem' objects>})"


class TRLIBQuadraticSubproblem(__scipy_optimize__trustregion.BaseQuadraticSubproblem):
    # no doc
    def solve(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff93075e50>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.optimize._trlib._trlib', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff93075e50>, origin='/.venv/lib/python3.8/site-packages/scipy/optimize/_trlib/_trlib.cpython-38-aarch64-linux-gnu.so')"

__test__ = {}

