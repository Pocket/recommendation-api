# encoding: utf-8
# module scipy.linalg.cython_blas
# from /.venv/lib/python3.8/site-packages/scipy/linalg/cython_blas.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
"""
BLAS Functions for Cython
=========================

Usable from Cython via::

    cimport scipy.linalg.cython_blas

These wrappers do not check for alignment of arrays.
Alignment should be checked before these wrappers are used.

Raw function pointers (Fortran-style pointer arguments):

- caxpy
- ccopy
- cdotc
- cdotu
- cgbmv
- cgemm
- cgemv
- cgerc
- cgeru
- chbmv
- chemm
- chemv
- cher
- cher2
- cher2k
- cherk
- chpmv
- chpr
- chpr2
- crotg
- cscal
- csrot
- csscal
- cswap
- csymm
- csyr2k
- csyrk
- ctbmv
- ctbsv
- ctpmv
- ctpsv
- ctrmm
- ctrmv
- ctrsm
- ctrsv
- dasum
- daxpy
- dcabs1
- dcopy
- ddot
- dgbmv
- dgemm
- dgemv
- dger
- dnrm2
- drot
- drotg
- drotm
- drotmg
- dsbmv
- dscal
- dsdot
- dspmv
- dspr
- dspr2
- dswap
- dsymm
- dsymv
- dsyr
- dsyr2
- dsyr2k
- dsyrk
- dtbmv
- dtbsv
- dtpmv
- dtpsv
- dtrmm
- dtrmv
- dtrsm
- dtrsv
- dzasum
- dznrm2
- icamax
- idamax
- isamax
- izamax
- lsame
- sasum
- saxpy
- scasum
- scnrm2
- scopy
- sdot
- sdsdot
- sgbmv
- sgemm
- sgemv
- sger
- snrm2
- srot
- srotg
- srotm
- srotmg
- ssbmv
- sscal
- sspmv
- sspr
- sspr2
- sswap
- ssymm
- ssymv
- ssyr
- ssyr2
- ssyr2k
- ssyrk
- stbmv
- stbsv
- stpmv
- stpsv
- strmm
- strmv
- strsm
- strsv
- zaxpy
- zcopy
- zdotc
- zdotu
- zdrot
- zdscal
- zgbmv
- zgemm
- zgemv
- zgerc
- zgeru
- zhbmv
- zhemm
- zhemv
- zher
- zher2
- zher2k
- zherk
- zhpmv
- zhpr
- zhpr2
- zrotg
- zscal
- zswap
- zsymm
- zsyr2k
- zsyrk
- ztbmv
- ztbsv
- ztpmv
- ztpsv
- ztrmm
- ztrmv
- ztrsm
- ztrsv
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

# functions

def _test_cdotc(*args, **kwargs): # real signature unknown
    pass

def _test_cdotu(*args, **kwargs): # real signature unknown
    pass

def _test_dasum(*args, **kwargs): # real signature unknown
    pass

def _test_ddot(*args, **kwargs): # real signature unknown
    pass

def _test_dgemm(*args, **kwargs): # real signature unknown
    pass

def _test_dnrm2(*args, **kwargs): # real signature unknown
    pass

def _test_dzasum(*args, **kwargs): # real signature unknown
    pass

def _test_dznrm2(*args, **kwargs): # real signature unknown
    pass

def _test_icamax(*args, **kwargs): # real signature unknown
    pass

def _test_idamax(*args, **kwargs): # real signature unknown
    pass

def _test_isamax(*args, **kwargs): # real signature unknown
    pass

def _test_izamax(*args, **kwargs): # real signature unknown
    pass

def _test_sasum(*args, **kwargs): # real signature unknown
    pass

def _test_scasum(*args, **kwargs): # real signature unknown
    pass

def _test_scnrm2(*args, **kwargs): # real signature unknown
    pass

def _test_sdot(*args, **kwargs): # real signature unknown
    pass

def _test_snrm2(*args, **kwargs): # real signature unknown
    pass

def _test_zdotc(*args, **kwargs): # real signature unknown
    pass

def _test_zdotu(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9bcb4820>'

__pyx_capi__ = {
    'caxpy': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bcb4c60>'
    'ccopy': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bcb4cc0>'
    'cdotc': None, # (!) real value is '<capsule object "__pyx_t_float_complex (int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bcb4cf0>'
    'cdotu': None, # (!) real value is '<capsule object "__pyx_t_float_complex (int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bcb4d20>'
    'cgbmv': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0xffff9bcb4d50>'
    'cgemm': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0xffff9bcb4d80>'
    'cgemv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0xffff9bcb4db0>'
    'cgerc': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bcb4de0>'
    'cgeru': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bcb4e10>'
    'chbmv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0xffff9bcb4e40>'
    'chemm': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0xffff9bcb4e70>'
    'chemv': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0xffff9bcb4ea0>'
    'cher': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bcb4ed0>'
    'cher2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bcb4f00>'
    'cher2k': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_float_complex *, int *)" at 0xffff9bcb4f30>'
    'cherk': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_float_complex *, int *)" at 0xffff9bcb4930>'
    'chpmv': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0xffff9bcb4f90>'
    'chpr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *)" at 0xffff9bcb4fc0>'
    'chpr2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *)" at 0xffff9bcb4f60>'
    'crotg': None, # (!) real value is '<capsule object "void (__pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_float_complex *)" at 0xffff9bcb9030>'
    'cscal': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0xffff9bcb9060>'
    'csrot': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *)" at 0xffff9bcb9090>'
    'csscal': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_float_complex *, int *)" at 0xffff9bcb90c0>'
    'cswap': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bcb90f0>'
    'csymm': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0xffff9bcb9120>'
    'csyr2k': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0xffff9bcb9150>'
    'csyrk': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0xffff9bcb9180>'
    'ctbmv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bcb91b0>'
    'ctbsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bcb91e0>'
    'ctpmv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0xffff9bcb9210>'
    'ctpsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0xffff9bcb9240>'
    'ctrmm': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bcb9270>'
    'ctrmv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bcb92a0>'
    'ctrsm': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bcb92d0>'
    'ctrsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bcb9300>'
    'dasum': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_d (int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0xffff9bcb9330>'
    'daxpy': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0xffff9bcb9360>'
    'dcabs1': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_d (__pyx_t_double_complex *)" at 0xffff9bcb9390>'
    'dcopy': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0xffff9bcb93c0>'
    'ddot': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_d (int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0xffff9bcb93f0>'
    'dgbmv': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0xffff9bcb9420>'
    'dgemm': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0xffff9bcb9450>'
    'dgemv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0xffff9bcb9480>'
    'dger': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0xffff9bcb94b0>'
    'dnrm2': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_d (int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0xffff9bcb94e0>'
    'drot': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *)" at 0xffff9bcb9510>'
    'drotg': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *)" at 0xffff9bcb9540>'
    'drotm': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *)" at 0xffff9bcb9570>'
    'drotmg': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *)" at 0xffff9bcb95a0>'
    'dsbmv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0xffff9bcb95d0>'
    'dscal': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0xffff9bcb9600>'
    'dsdot': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_d (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0xffff9bcb9630>'
    'dspmv': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0xffff9bcb9660>'
    'dspr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *)" at 0xffff9bcb9690>'
    'dspr2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *)" at 0xffff9bcb96c0>'
    'dswap': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0xffff9bcb96f0>'
    'dsymm': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0xffff9bcb9720>'
    'dsymv': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0xffff9bcb9750>'
    'dsyr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0xffff9bcb9780>'
    'dsyr2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0xffff9bcb97b0>'
    'dsyr2k': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0xffff9bcb97e0>'
    'dsyrk': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0xffff9bcb9810>'
    'dtbmv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0xffff9bcb9840>'
    'dtbsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0xffff9bcb9870>'
    'dtpmv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0xffff9bcb98a0>'
    'dtpsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0xffff9bcb98d0>'
    'dtrmm': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0xffff9bcb9900>'
    'dtrmv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0xffff9bcb9930>'
    'dtrsm': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0xffff9bcb9960>'
    'dtrsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0xffff9bcb9990>'
    'dzasum': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_d (int *, __pyx_t_double_complex *, int *)" at 0xffff9bcb99c0>'
    'dznrm2': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_d (int *, __pyx_t_double_complex *, int *)" at 0xffff9bcb99f0>'
    'icamax': None, # (!) real value is '<capsule object "int (int *, __pyx_t_float_complex *, int *)" at 0xffff9bcb9a20>'
    'idamax': None, # (!) real value is '<capsule object "int (int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0xffff9bcb9a50>'
    'isamax': None, # (!) real value is '<capsule object "int (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0xffff9bcb9a80>'
    'izamax': None, # (!) real value is '<capsule object "int (int *, __pyx_t_double_complex *, int *)" at 0xffff9bcb9ab0>'
    'lsame': None, # (!) real value is '<capsule object "int (char *, char *)" at 0xffff9bcb9ae0>'
    'sasum': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_s (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0xffff9bcb9b10>'
    'saxpy': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0xffff9bcb9b40>'
    'scasum': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_s (int *, __pyx_t_float_complex *, int *)" at 0xffff9bcb9b70>'
    'scnrm2': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_s (int *, __pyx_t_float_complex *, int *)" at 0xffff9bcb9ba0>'
    'scopy': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0xffff9bcb9bd0>'
    'sdot': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_s (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0xffff9bcb9c00>'
    'sdsdot': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_s (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0xffff9bcb9c30>'
    'sgbmv': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0xffff9bcb9c60>'
    'sgemm': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0xffff9bcb9c90>'
    'sgemv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0xffff9bcb9cc0>'
    'sger': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0xffff9bcb9cf0>'
    'snrm2': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_s (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0xffff9bcb9d20>'
    'srot': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *)" at 0xffff9bcb9d50>'
    'srotg': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *)" at 0xffff9bcb9d80>'
    'srotm': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *)" at 0xffff9bcb9db0>'
    'srotmg': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *)" at 0xffff9bcb9de0>'
    'ssbmv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0xffff9bcb9e10>'
    'sscal': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0xffff9bcb9e40>'
    'sspmv': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0xffff9bcb9e70>'
    'sspr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *)" at 0xffff9bcb9ea0>'
    'sspr2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *)" at 0xffff9bcb9ed0>'
    'sswap': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0xffff9bcb9f00>'
    'ssymm': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0xffff9bcb9f30>'
    'ssymv': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0xffff9bcb9f60>'
    'ssyr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0xffff9bcb9f90>'
    'ssyr2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0xffff9bcb9fc0>'
    'ssyr2k': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0xffff9bcba030>'
    'ssyrk': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0xffff9bcba060>'
    'stbmv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0xffff9bcba090>'
    'stbsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0xffff9bcba0c0>'
    'stpmv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0xffff9bcba0f0>'
    'stpsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0xffff9bcba120>'
    'strmm': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0xffff9bcba150>'
    'strmv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0xffff9bcba180>'
    'strsm': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0xffff9bcba1b0>'
    'strsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0xffff9bcba1e0>'
    'zaxpy': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcba210>'
    'zcopy': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcba240>'
    'zdotc': None, # (!) real value is '<capsule object "__pyx_t_double_complex (int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcba270>'
    'zdotu': None, # (!) real value is '<capsule object "__pyx_t_double_complex (int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcba2a0>'
    'zdrot': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *)" at 0xffff9bcba2d0>'
    'zdscal': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_double_complex *, int *)" at 0xffff9bcba300>'
    'zgbmv': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0xffff9bcba330>'
    'zgemm': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0xffff9bcba360>'
    'zgemv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0xffff9bcba390>'
    'zgerc': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcba3c0>'
    'zgeru': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcba3f0>'
    'zhbmv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0xffff9bcba420>'
    'zhemm': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0xffff9bcba450>'
    'zhemv': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0xffff9bcba480>'
    'zher': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcba4b0>'
    'zher2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcba4e0>'
    'zher2k': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_double_complex *, int *)" at 0xffff9bcba510>'
    'zherk': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_double_complex *, int *)" at 0xffff9bcba540>'
    'zhpmv': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0xffff9bcba570>'
    'zhpr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *)" at 0xffff9bcba5a0>'
    'zhpr2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *)" at 0xffff9bcba5d0>'
    'zrotg': None, # (!) real value is '<capsule object "void (__pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_double_complex *)" at 0xffff9bcba600>'
    'zscal': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0xffff9bcba630>'
    'zswap': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcba660>'
    'zsymm': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0xffff9bcba690>'
    'zsyr2k': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0xffff9bcba6c0>'
    'zsyrk': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0xffff9bcba6f0>'
    'ztbmv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcba720>'
    'ztbsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcba750>'
    'ztpmv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0xffff9bcba780>'
    'ztpsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0xffff9bcba7b0>'
    'ztrmm': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcba7e0>'
    'ztrmv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcba810>'
    'ztrsm': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcba840>'
    'ztrsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcba870>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.linalg.cython_blas', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9bcb4820>, origin='/.venv/lib/python3.8/site-packages/scipy/linalg/cython_blas.cpython-38-aarch64-linux-gnu.so')"

__test__ = {}

