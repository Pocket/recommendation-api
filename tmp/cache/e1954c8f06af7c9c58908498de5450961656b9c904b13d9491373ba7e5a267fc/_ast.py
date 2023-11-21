# encoding: utf-8
# module _ast
# from (built-in)
# by generator 1.147
# no doc
# no imports

# Variables with simple values

PyCF_ALLOW_TOP_LEVEL_AWAIT = 8192

PyCF_ONLY_AST = 1024

PyCF_TYPE_COMMENTS = 4096

# no functions
# classes

class AST(object):
    # no doc
    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

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
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    _attributes = ()
    _fields = ()
    __dict__ = None # (!) real value is "mappingproxy({'__getattribute__': <slot wrapper '__getattribute__' of '_ast.AST' objects>, '__setattr__': <slot wrapper '__setattr__' of '_ast.AST' objects>, '__delattr__': <slot wrapper '__delattr__' of '_ast.AST' objects>, '__init__': <slot wrapper '__init__' of '_ast.AST' objects>, '__new__': <built-in method __new__ of type object at 0xffffad58d980>, '__reduce__': <method '__reduce__' of '_ast.AST' objects>, '__dict__': <attribute '__dict__' of '_ast.AST' objects>, '__doc__': None, '_fields': (), '_attributes': ()})"


class operator(AST):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _attributes = ()
    _fields = ()


class Add(operator):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class alias(AST):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _attributes = ()
    _fields = (
        'name',
        'asname',
    )


class boolop(AST):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _attributes = ()
    _fields = ()


class And(boolop):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class stmt(AST):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _attributes = (
        'lineno',
        'col_offset',
        'end_lineno',
        'end_col_offset',
    )
    _fields = ()


class AnnAssign(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'target',
        'annotation',
        'value',
        'simple',
    )


class arg(AST):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _attributes = (
        'lineno',
        'col_offset',
        'end_lineno',
        'end_col_offset',
    )
    _fields = (
        'arg',
        'annotation',
        'type_comment',
    )


class arguments(AST):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _attributes = ()
    _fields = (
        'posonlyargs',
        'args',
        'vararg',
        'kwonlyargs',
        'kw_defaults',
        'kwarg',
        'defaults',
    )


class Assert(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'test',
        'msg',
    )


class Assign(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'targets',
        'value',
        'type_comment',
    )


class AsyncFor(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'target',
        'iter',
        'body',
        'orelse',
        'type_comment',
    )


class AsyncFunctionDef(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'name',
        'args',
        'body',
        'decorator_list',
        'returns',
        'type_comment',
    )


class AsyncWith(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'items',
        'body',
        'type_comment',
    )


class expr(AST):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _attributes = (
        'lineno',
        'col_offset',
        'end_lineno',
        'end_col_offset',
    )
    _fields = ()


class Attribute(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'value',
        'attr',
        'ctx',
    )


class AugAssign(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'target',
        'op',
        'value',
    )


class expr_context(AST):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _attributes = ()
    _fields = ()


class AugLoad(expr_context):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class AugStore(expr_context):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class Await(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'value',
    )


class BinOp(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'left',
        'op',
        'right',
    )


class BitAnd(operator):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class BitOr(operator):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class BitXor(operator):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class BoolOp(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'op',
        'values',
    )


class Break(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class Call(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'func',
        'args',
        'keywords',
    )


class ClassDef(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'name',
        'bases',
        'keywords',
        'body',
        'decorator_list',
    )


class cmpop(AST):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _attributes = ()
    _fields = ()


class Compare(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'left',
        'ops',
        'comparators',
    )


class comprehension(AST):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _attributes = ()
    _fields = (
        'target',
        'iter',
        'ifs',
        'is_async',
    )


class Constant(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    n = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    s = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _fields = (
        'value',
        'kind',
    )


class Continue(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class Del(expr_context):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class Delete(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'targets',
    )


class Dict(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'keys',
        'values',
    )


class DictComp(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'key',
        'value',
        'generators',
    )


class Div(operator):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class Eq(cmpop):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class excepthandler(AST):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _attributes = (
        'lineno',
        'col_offset',
        'end_lineno',
        'end_col_offset',
    )
    _fields = ()


class ExceptHandler(excepthandler):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'type',
        'name',
        'body',
    )


class Expr(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'value',
    )


class mod(AST):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _attributes = ()
    _fields = ()


class Expression(mod):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'body',
    )


class slice(AST):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _attributes = ()
    _fields = ()


class ExtSlice(slice):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'dims',
    )


class FloorDiv(operator):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class For(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'target',
        'iter',
        'body',
        'orelse',
        'type_comment',
    )


class FormattedValue(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'value',
        'conversion',
        'format_spec',
    )


class FunctionDef(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'name',
        'args',
        'body',
        'decorator_list',
        'returns',
        'type_comment',
    )


class FunctionType(mod):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'argtypes',
        'returns',
    )


class GeneratorExp(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'elt',
        'generators',
    )


class Global(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'names',
    )


class Gt(cmpop):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class GtE(cmpop):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class If(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'test',
        'body',
        'orelse',
    )


class IfExp(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'test',
        'body',
        'orelse',
    )


class Import(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'names',
    )


class ImportFrom(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'module',
        'names',
        'level',
    )


class In(cmpop):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class Index(slice):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'value',
    )


class Interactive(mod):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'body',
    )


class unaryop(AST):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _attributes = ()
    _fields = ()


class Invert(unaryop):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class Is(cmpop):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class IsNot(cmpop):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class JoinedStr(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'values',
    )


class keyword(AST):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _attributes = ()
    _fields = (
        'arg',
        'value',
    )


class Lambda(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'args',
        'body',
    )


class List(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'elts',
        'ctx',
    )


class ListComp(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'elt',
        'generators',
    )


class Load(expr_context):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class LShift(operator):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class Lt(cmpop):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class LtE(cmpop):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class MatMult(operator):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class Mod(operator):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class Module(mod):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'body',
        'type_ignores',
    )


class Mult(operator):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class Name(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'id',
        'ctx',
    )


class NamedExpr(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'target',
        'value',
    )


class Nonlocal(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'names',
    )


class Not(unaryop):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class NotEq(cmpop):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class NotIn(cmpop):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class Or(boolop):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class Param(expr_context):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class Pass(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class Pow(operator):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class Raise(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'exc',
        'cause',
    )


class Return(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'value',
    )


class RShift(operator):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class Set(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'elts',
    )


class SetComp(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'elt',
        'generators',
    )


class Slice(slice):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'lower',
        'upper',
        'step',
    )


class Starred(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'value',
        'ctx',
    )


class Store(expr_context):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class Sub(operator):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class Subscript(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'value',
        'slice',
        'ctx',
    )


class Suite(mod):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'body',
    )


class Try(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'body',
        'handlers',
        'orelse',
        'finalbody',
    )


class Tuple(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'elts',
        'ctx',
    )


class type_ignore(AST):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _attributes = ()
    _fields = ()


class TypeIgnore(type_ignore):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'lineno',
        'tag',
    )


class UAdd(unaryop):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class UnaryOp(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'op',
        'operand',
    )


class USub(unaryop):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class While(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'test',
        'body',
        'orelse',
    )


class With(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'items',
        'body',
        'type_comment',
    )


class withitem(AST):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _attributes = ()
    _fields = (
        'context_expr',
        'optional_vars',
    )


class Yield(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'value',
    )


class YieldFrom(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'value',
    )


class __loader__(object):
    """
    Meta path import for built-in modules.
    
        All methods are either class or static methods to avoid the need to
        instantiate the class.
    """
    @classmethod
    def create_module(cls, *args, **kwargs): # real signature unknown
        """ Create a built-in module """
        pass

    @classmethod
    def exec_module(cls, *args, **kwargs): # real signature unknown
        """ Exec a built-in module """
        pass

    @classmethod
    def find_module(cls, *args, **kwargs): # real signature unknown
        """
        Find the built-in module.
        
                If 'path' is ever specified then the search is considered a failure.
        
                This method is deprecated.  Use find_spec() instead.
        """
        pass

    @classmethod
    def find_spec(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def get_code(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have code objects. """
        pass

    @classmethod
    def get_source(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have source code. """
        pass

    @classmethod
    def is_package(cls, *args, **kwargs): # real signature unknown
        """ Return False as built-in modules are never packages. """
        pass

    @classmethod
    def load_module(cls, *args, **kwargs): # real signature unknown
        """
        Load the specified module into sys.modules and return it.
        
            This method is deprecated.  Use loader.exec_module instead.
        """
        pass

    def module_repr(module): # reliably restored by inspect
        """
        Return repr for the module.
        
                The method is deprecated.  The import machinery does the job itself.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__doc__': 'Meta path import for built-in modules.\\n\\n    All methods are either class or static methods to avoid the need to\\n    instantiate the class.\\n\\n    ', 'module_repr': <staticmethod object at 0xffffacf8a430>, 'find_spec': <classmethod object at 0xffffacf8a460>, 'find_module': <classmethod object at 0xffffacf8a490>, 'create_module': <classmethod object at 0xffffacf8a4c0>, 'exec_module': <classmethod object at 0xffffacf8a4f0>, 'get_code': <classmethod object at 0xffffacf8a580>, 'get_source': <classmethod object at 0xffffacf8a610>, 'is_package': <classmethod object at 0xffffacf8a6a0>, 'load_module': <classmethod object at 0xffffacf8a6d0>, '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"


# variables with complex values

__spec__ = None # (!) real value is "ModuleSpec(name='_ast', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

