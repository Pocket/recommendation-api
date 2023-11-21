# encoding: utf-8
# module scipy.linalg._decomp_update
# from /.venv/lib/python3.8/site-packages/scipy/linalg/_decomp_update.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
"""
Routines for updating QR decompositions

.. versionadded:: 0.16.0
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /.venv/lib/python3.8/site-packages/numpy/__init__.py

# functions

def qr_delete(Q, R, k, int_p=1, which=None, overwrite_qr=False, check_finite=True): # real signature unknown; restored from __doc__
    """
    qr_delete(Q, R, k, int p=1, which=u'row', overwrite_qr=False, check_finite=True)
    
        QR downdate on row or column deletions
    
        If ``A = Q R`` is the QR factorization of ``A``, return the QR
        factorization of ``A`` where ``p`` rows or columns have been removed
        starting at row or column ``k``.
    
        Parameters
        ----------
        Q : (M, M) or (M, N) array_like
            Unitary/orthogonal matrix from QR decomposition.
        R : (M, N) or (N, N) array_like
            Upper triangular matrix from QR decomposition.
        k : int
            Index of the first row or column to delete.
        p : int, optional
            Number of rows or columns to delete, defaults to 1.
        which: {'row', 'col'}, optional
            Determines if rows or columns will be deleted, defaults to 'row'
        overwrite_qr : bool, optional
            If True, consume Q and R, overwriting their contents with their
            downdated versions, and returning approriately sized views.
            Defaults to False.
        check_finite : bool, optional
            Whether to check that the input matrix contains only finite numbers.
            Disabling may give a performance gain, but may result in problems
            (crashes, non-termination) if the inputs do contain infinities or NaNs.
            Default is True.
    
        Returns
        -------
        Q1 : ndarray
            Updated unitary/orthogonal factor
        R1 : ndarray
            Updated upper triangular factor
    
        See Also
        --------
        qr, qr_multiply, qr_insert, qr_update
    
        Notes
        -----
        This routine does not guarantee that the diagonal entries of ``R1`` are
        positive.
    
        .. versionadded:: 0.16.0
    
        References
        ----------
        .. [1] Golub, G. H. & Van Loan, C. F. Matrix Computations, 3rd Ed.
               (Johns Hopkins University Press, 1996).
    
        .. [2] Daniel, J. W., Gragg, W. B., Kaufman, L. & Stewart, G. W.
               Reorthogonalization and stable algorithms for updating the
               Gram-Schmidt QR factorization. Math. Comput. 30, 772-795 (1976).
    
        .. [3] Reichel, L. & Gragg, W. B. Algorithm 686: FORTRAN Subroutines for
               Updating the QR Decomposition. ACM Trans. Math. Softw. 16, 369-377
               (1990).
    
        Examples
        --------
        >>> import numpy as np
        >>> from scipy import linalg
        >>> a = np.array([[  3.,  -2.,  -2.],
        ...               [  6.,  -9.,  -3.],
        ...               [ -3.,  10.,   1.],
        ...               [  6.,  -7.,   4.],
        ...               [  7.,   8.,  -6.]])
        >>> q, r = linalg.qr(a)
    
        Given this QR decomposition, update q and r when 2 rows are removed.
    
        >>> q1, r1 = linalg.qr_delete(q, r, 2, 2, 'row', False)
        >>> q1
        array([[ 0.30942637,  0.15347579,  0.93845645],  # may vary (signs)
               [ 0.61885275,  0.71680171, -0.32127338],
               [ 0.72199487, -0.68017681, -0.12681844]])
        >>> r1
        array([[  9.69535971,  -0.4125685 ,  -6.80738023],  # may vary (signs)
               [  0.        , -12.19958144,   1.62370412],
               [  0.        ,   0.        ,  -0.15218213]])
    
        The update is equivalent, but faster than the following.
    
        >>> a1 = np.delete(a, slice(2,4), 0)
        >>> a1
        array([[ 3., -2., -2.],
               [ 6., -9., -3.],
               [ 7.,  8., -6.]])
        >>> q_direct, r_direct = linalg.qr(a1)
    
        Check that we have equivalent results:
    
        >>> np.dot(q1, r1)
        array([[ 3., -2., -2.],
               [ 6., -9., -3.],
               [ 7.,  8., -6.]])
        >>> np.allclose(np.dot(q1, r1), a1)
        True
    
        And the updated Q is still unitary:
    
        >>> np.allclose(np.dot(q1.T, q1), np.eye(3))
        True
    """
    pass

def qr_insert(Q, R, u, k, which=None, rcond=None, overwrite_qru=False, check_finite=True): # real signature unknown; restored from __doc__
    """
    qr_insert(Q, R, u, k, which=u'row', rcond=None, overwrite_qru=False, check_finite=True)
    
        QR update on row or column insertions
    
        If ``A = Q R`` is the QR factorization of ``A``, return the QR
        factorization of ``A`` where rows or columns have been inserted starting
        at row or column ``k``.
    
        Parameters
        ----------
        Q : (M, M) array_like
            Unitary/orthogonal matrix from the QR decomposition of A.
        R : (M, N) array_like
            Upper triangular matrix from the QR decomposition of A.
        u : (N,), (p, N), (M,), or (M, p) array_like
            Rows or columns to insert
        k : int
            Index before which `u` is to be inserted.
        which: {'row', 'col'}, optional
            Determines if rows or columns will be inserted, defaults to 'row'
        rcond : float
            Lower bound on the reciprocal condition number of ``Q`` augmented with
            ``u/||u||`` Only used when updating economic mode (thin, (M,N) (N,N))
            decompositions.  If None, machine precision is used.  Defaults to
            None.
        overwrite_qru : bool, optional
            If True, consume Q, R, and u, if possible, while performing the update,
            otherwise make copies as necessary. Defaults to False.
        check_finite : bool, optional
            Whether to check that the input matrices contain only finite numbers.
            Disabling may give a performance gain, but may result in problems
            (crashes, non-termination) if the inputs do contain infinities or NaNs.
            Default is True.
    
        Returns
        -------
        Q1 : ndarray
            Updated unitary/orthogonal factor
        R1 : ndarray
            Updated upper triangular factor
    
        Raises
        ------
        LinAlgError :
            If updating a (M,N) (N,N) factorization and the reciprocal condition
            number of Q augmented with u/||u|| is smaller than rcond.
    
        See Also
        --------
        qr, qr_multiply, qr_delete, qr_update
    
        Notes
        -----
        This routine does not guarantee that the diagonal entries of ``R1`` are
        positive.
    
        .. versionadded:: 0.16.0
    
        References
        ----------
    
        .. [1] Golub, G. H. & Van Loan, C. F. Matrix Computations, 3rd Ed.
               (Johns Hopkins University Press, 1996).
    
        .. [2] Daniel, J. W., Gragg, W. B., Kaufman, L. & Stewart, G. W.
               Reorthogonalization and stable algorithms for updating the
               Gram-Schmidt QR factorization. Math. Comput. 30, 772-795 (1976).
    
        .. [3] Reichel, L. & Gragg, W. B. Algorithm 686: FORTRAN Subroutines for
               Updating the QR Decomposition. ACM Trans. Math. Softw. 16, 369-377
               (1990).
    
        Examples
        --------
        >>> import numpy as np
        >>> from scipy import linalg
        >>> a = np.array([[  3.,  -2.,  -2.],
        ...               [  6.,  -7.,   4.],
        ...               [  7.,   8.,  -6.]])
        >>> q, r = linalg.qr(a)
    
        Given this QR decomposition, update q and r when 2 rows are inserted.
    
        >>> u = np.array([[  6.,  -9.,  -3.],
        ...               [ -3.,  10.,   1.]])
        >>> q1, r1 = linalg.qr_insert(q, r, u, 2, 'row')
        >>> q1
        array([[-0.25445668,  0.02246245,  0.18146236, -0.72798806,  0.60979671],  # may vary (signs)
               [-0.50891336,  0.23226178, -0.82836478, -0.02837033, -0.00828114],
               [-0.50891336,  0.35715302,  0.38937158,  0.58110733,  0.35235345],
               [ 0.25445668, -0.52202743, -0.32165498,  0.36263239,  0.65404509],
               [-0.59373225, -0.73856549,  0.16065817, -0.0063658 , -0.27595554]])
        >>> r1
        array([[-11.78982612,   6.44623587,   3.81685018],  # may vary (signs)
               [  0.        , -16.01393278,   3.72202865],
               [  0.        ,   0.        ,  -6.13010256],
               [  0.        ,   0.        ,   0.        ],
               [  0.        ,   0.        ,   0.        ]])
    
        The update is equivalent, but faster than the following.
    
        >>> a1 = np.insert(a, 2, u, 0)
        >>> a1
        array([[  3.,  -2.,  -2.],
               [  6.,  -7.,   4.],
               [  6.,  -9.,  -3.],
               [ -3.,  10.,   1.],
               [  7.,   8.,  -6.]])
        >>> q_direct, r_direct = linalg.qr(a1)
    
        Check that we have equivalent results:
    
        >>> np.dot(q1, r1)
        array([[  3.,  -2.,  -2.],
               [  6.,  -7.,   4.],
               [  6.,  -9.,  -3.],
               [ -3.,  10.,   1.],
               [  7.,   8.,  -6.]])
    
        >>> np.allclose(np.dot(q1, r1), a1)
        True
    
        And the updated Q is still unitary:
    
        >>> np.allclose(np.dot(q1.T, q1), np.eye(5))
        True
    """
    pass

def qr_update(Q, R, u, v, overwrite_qruv=False, check_finite=True): # real signature unknown; restored from __doc__
    """
    qr_update(Q, R, u, v, overwrite_qruv=False, check_finite=True)
    
        Rank-k QR update
    
        If ``A = Q R`` is the QR factorization of ``A``, return the QR
        factorization of ``A + u v**T`` for real ``A`` or ``A + u v**H``
        for complex ``A``.
    
        Parameters
        ----------
        Q : (M, M) or (M, N) array_like
            Unitary/orthogonal matrix from the qr decomposition of A.
        R : (M, N) or (N, N) array_like
            Upper triangular matrix from the qr decomposition of A.
        u : (M,) or (M, k) array_like
            Left update vector
        v : (N,) or (N, k) array_like
            Right update vector
        overwrite_qruv : bool, optional
            If True, consume Q, R, u, and v, if possible, while performing the
            update, otherwise make copies as necessary. Defaults to False.
        check_finite : bool, optional
            Whether to check that the input matrix contains only finite numbers.
            Disabling may give a performance gain, but may result in problems
            (crashes, non-termination) if the inputs do contain infinities or NaNs.
            Default is True.
    
        Returns
        -------
        Q1 : ndarray
            Updated unitary/orthogonal factor
        R1 : ndarray
            Updated upper triangular factor
    
        See Also
        --------
        qr, qr_multiply, qr_delete, qr_insert
    
        Notes
        -----
        This routine does not guarantee that the diagonal entries of `R1` are
        real or positive.
    
        .. versionadded:: 0.16.0
    
        References
        ----------
        .. [1] Golub, G. H. & Van Loan, C. F. Matrix Computations, 3rd Ed.
               (Johns Hopkins University Press, 1996).
    
        .. [2] Daniel, J. W., Gragg, W. B., Kaufman, L. & Stewart, G. W.
               Reorthogonalization and stable algorithms for updating the
               Gram-Schmidt QR factorization. Math. Comput. 30, 772-795 (1976).
    
        .. [3] Reichel, L. & Gragg, W. B. Algorithm 686: FORTRAN Subroutines for
               Updating the QR Decomposition. ACM Trans. Math. Softw. 16, 369-377
               (1990).
    
        Examples
        --------
        >>> import numpy as np
        >>> from scipy import linalg
        >>> a = np.array([[  3.,  -2.,  -2.],
        ...               [  6.,  -9.,  -3.],
        ...               [ -3.,  10.,   1.],
        ...               [  6.,  -7.,   4.],
        ...               [  7.,   8.,  -6.]])
        >>> q, r = linalg.qr(a)
    
        Given this q, r decomposition, perform a rank 1 update.
    
        >>> u = np.array([7., -2., 4., 3., 5.])
        >>> v = np.array([1., 3., -5.])
        >>> q_up, r_up = linalg.qr_update(q, r, u, v, False)
        >>> q_up
        array([[ 0.54073807,  0.18645997,  0.81707661, -0.02136616,  0.06902409],  # may vary (signs)
               [ 0.21629523, -0.63257324,  0.06567893,  0.34125904, -0.65749222],
               [ 0.05407381,  0.64757787, -0.12781284, -0.20031219, -0.72198188],
               [ 0.48666426, -0.30466718, -0.27487277, -0.77079214,  0.0256951 ],
               [ 0.64888568,  0.23001   , -0.4859845 ,  0.49883891,  0.20253783]])
        >>> r_up
        array([[ 18.49324201,  24.11691794, -44.98940746],  # may vary (signs)
               [  0.        ,  31.95894662, -27.40998201],
               [  0.        ,   0.        ,  -9.25451794],
               [  0.        ,   0.        ,   0.        ],
               [  0.        ,   0.        ,   0.        ]])
    
        The update is equivalent, but faster than the following.
    
        >>> a_up = a + np.outer(u, v)
        >>> q_direct, r_direct = linalg.qr(a_up)
    
        Check that we have equivalent results:
    
        >>> np.allclose(np.dot(q_up, r_up), a_up)
        True
    
        And the updated Q is still unitary:
    
        >>> np.allclose(np.dot(q_up.T, q_up), np.eye(5))
        True
    
        Updating economic (reduced, thin) decompositions is also possible:
    
        >>> qe, re = linalg.qr(a, mode='economic')
        >>> qe_up, re_up = linalg.qr_update(qe, re, u, v, False)
        >>> qe_up
        array([[ 0.54073807,  0.18645997,  0.81707661],  # may vary (signs)
               [ 0.21629523, -0.63257324,  0.06567893],
               [ 0.05407381,  0.64757787, -0.12781284],
               [ 0.48666426, -0.30466718, -0.27487277],
               [ 0.64888568,  0.23001   , -0.4859845 ]])
        >>> re_up
        array([[ 18.49324201,  24.11691794, -44.98940746],  # may vary (signs)
               [  0.        ,  31.95894662, -27.40998201],
               [  0.        ,   0.        ,  -9.25451794]])
        >>> np.allclose(np.dot(qe_up, re_up), a_up)
        True
        >>> np.allclose(np.dot(qe_up.T, qe_up), np.eye(3))
        True
    
        Similarly to the above, perform a rank 2 update.
    
        >>> u2 = np.array([[ 7., -1,],
        ...                [-2.,  4.],
        ...                [ 4.,  2.],
        ...                [ 3., -6.],
        ...                [ 5.,  3.]])
        >>> v2 = np.array([[ 1., 2.],
        ...                [ 3., 4.],
        ...                [-5., 2]])
        >>> q_up2, r_up2 = linalg.qr_update(q, r, u2, v2, False)
        >>> q_up2
        array([[-0.33626508, -0.03477253,  0.61956287, -0.64352987, -0.29618884],  # may vary (signs)
               [-0.50439762,  0.58319694, -0.43010077, -0.33395279,  0.33008064],
               [-0.21016568, -0.63123106,  0.0582249 , -0.13675572,  0.73163206],
               [ 0.12609941,  0.49694436,  0.64590024,  0.31191919,  0.47187344],
               [-0.75659643, -0.11517748,  0.10284903,  0.5986227 , -0.21299983]])
        >>> r_up2
        array([[-23.79075451, -41.1084062 ,  24.71548348],  # may vary (signs)
               [  0.        , -33.83931057,  11.02226551],
               [  0.        ,   0.        ,  48.91476811],
               [  0.        ,   0.        ,   0.        ],
               [  0.        ,   0.        ,   0.        ]])
    
        This update is also a valid qr decomposition of ``A + U V**T``.
    
        >>> a_up2 = a + np.dot(u2, v2.T)
        >>> np.allclose(a_up2, np.dot(q_up2, r_up2))
        True
        >>> np.allclose(np.dot(q_up2.T, q_up2), np.eye(5))
        True
    """
    pass

def _form_qTu(*args, **kwargs): # real signature unknown
    """
    this function only exists to expose the cdef version below for testing
            purposes. Here we perform minimal input validation to ensure that the
            inputs meet the requirements below.
    """
    pass

# classes

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

__all__ = [
    'qr_delete',
    'qr_insert',
    'qr_update',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9bcbbf10>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.linalg._decomp_update', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9bcbbf10>, origin='/.venv/lib/python3.8/site-packages/scipy/linalg/_decomp_update.cpython-38-aarch64-linux-gnu.so')"

__test__ = {
    'qr_delete (line 1446)': "\n    QR downdate on row or column deletions\n\n    If ``A = Q R`` is the QR factorization of ``A``, return the QR\n    factorization of ``A`` where ``p`` rows or columns have been removed\n    starting at row or column ``k``.\n\n    Parameters\n    ----------\n    Q : (M, M) or (M, N) array_like\n        Unitary/orthogonal matrix from QR decomposition.\n    R : (M, N) or (N, N) array_like\n        Upper triangular matrix from QR decomposition.\n    k : int\n        Index of the first row or column to delete.\n    p : int, optional\n        Number of rows or columns to delete, defaults to 1.\n    which: {'row', 'col'}, optional\n        Determines if rows or columns will be deleted, defaults to 'row'\n    overwrite_qr : bool, optional\n        If True, consume Q and R, overwriting their contents with their\n        downdated versions, and returning approriately sized views.\n        Defaults to False.\n    check_finite : bool, optional\n        Whether to check that the input matrix contains only finite numbers.\n        Disabling may give a performance gain, but may result in problems\n        (crashes, non-termination) if the inputs do contain infinities or NaNs.\n        Default is True.\n\n    Returns\n    -------\n    Q1 : ndarray\n        Updated unitary/orthogonal factor\n    R1 : ndarray\n        Updated upper triangular factor\n\n    See Also\n    --------\n    qr, qr_multiply, qr_insert, qr_update\n\n    Notes\n    -----\n    This routine does not guarantee that the diagonal entries of ``R1`` are\n    positive.\n\n    .. versionadded:: 0.16.0\n\n    References\n    ----------\n    .. [1] Golub, G. H. & Van Loan, C. F. Matrix Computations, 3rd Ed.\n           (Johns Hopkins University Press, 1996).\n\n    .. [2] Daniel, J. W., Gragg, W. B., Kaufman, L. & Stewart, G. W.\n           Reorthogonalization and stable algorithms for updating the\n           Gram-Schmidt QR factorization. Math. Comput. 30, 772-795 (1976).\n\n    .. [3] Reichel, L. & Gragg, W. B. Algorithm 686: FORTRAN Subroutines for\n           Updating the QR Decomposition. ACM Trans. Math. Softw. 16, 369-377\n           (1990).\n\n    Examples\n    --------\n    >>> import numpy as np\n    >>> from scipy import linalg\n    >>> a = np.array([[  3.,  -2.,  -2.],\n    ...               [  6.,  -9.,  -3.],\n    ...               [ -3.,  10.,   1.],\n    ...               [  6.,  -7.,   4.],\n    ...               [  7.,   8.,  -6.]])\n    >>> q, r = linalg.qr(a)\n\n    Given this QR decomposition, update q and r when 2 rows are removed.\n\n    >>> q1, r1 = linalg.qr_delete(q, r, 2, 2, 'row', False)\n    >>> q1\n    array([[ 0.30942637,  0.15347579,  0.93845645],  # may vary (signs)\n           [ 0.61885275,  0.71680171, -0.32127338],\n           [ 0.72199487, -0.68017681, -0.12681844]])\n    >>> r1\n    array([[  9.69535971,  -0.4125685 ,  -6.80738023],  # may vary (signs)\n           [  0.        , -12.19958144,   1.62370412],\n           [  0.        ,   0.        ,  -0.15218213]])\n\n    The update is equivalent, but faster than the following.\n\n    >>> a1 = np.delete(a, slice(2,4), 0)\n    >>> a1\n    array([[ 3., -2., -2.],\n           [ 6., -9., -3.],\n           [ 7.,  8., -6.]])\n    >>> q_direct, r_direct = linalg.qr(a1)\n\n    Check that we have equivalent results:\n\n    >>> np.dot(q1, r1)\n    array([[ 3., -2., -2.],\n           [ 6., -9., -3.],\n           [ 7.,  8., -6.]])\n    >>> np.allclose(np.dot(q1, r1), a1)\n    True\n\n    And the updated Q is still unitary:\n\n    >>> np.allclose(np.dot(q1.T, q1), np.eye(3))\n    True\n\n    ",
    'qr_insert (line 1691)': "\n    QR update on row or column insertions\n\n    If ``A = Q R`` is the QR factorization of ``A``, return the QR\n    factorization of ``A`` where rows or columns have been inserted starting\n    at row or column ``k``.\n\n    Parameters\n    ----------\n    Q : (M, M) array_like\n        Unitary/orthogonal matrix from the QR decomposition of A.\n    R : (M, N) array_like\n        Upper triangular matrix from the QR decomposition of A.\n    u : (N,), (p, N), (M,), or (M, p) array_like\n        Rows or columns to insert\n    k : int\n        Index before which `u` is to be inserted.\n    which: {'row', 'col'}, optional\n        Determines if rows or columns will be inserted, defaults to 'row'\n    rcond : float\n        Lower bound on the reciprocal condition number of ``Q`` augmented with\n        ``u/||u||`` Only used when updating economic mode (thin, (M,N) (N,N))\n        decompositions.  If None, machine precision is used.  Defaults to\n        None.\n    overwrite_qru : bool, optional\n        If True, consume Q, R, and u, if possible, while performing the update,\n        otherwise make copies as necessary. Defaults to False.\n    check_finite : bool, optional\n        Whether to check that the input matrices contain only finite numbers.\n        Disabling may give a performance gain, but may result in problems\n        (crashes, non-termination) if the inputs do contain infinities or NaNs.\n        Default is True.\n\n    Returns\n    -------\n    Q1 : ndarray\n        Updated unitary/orthogonal factor\n    R1 : ndarray\n        Updated upper triangular factor\n\n    Raises\n    ------\n    LinAlgError :\n        If updating a (M,N) (N,N) factorization and the reciprocal condition\n        number of Q augmented with u/||u|| is smaller than rcond.\n\n    See Also\n    --------\n    qr, qr_multiply, qr_delete, qr_update\n\n    Notes\n    -----\n    This routine does not guarantee that the diagonal entries of ``R1`` are\n    positive.\n\n    .. versionadded:: 0.16.0\n\n    References\n    ----------\n\n    .. [1] Golub, G. H. & Van Loan, C. F. Matrix Computations, 3rd Ed.\n           (Johns Hopkins University Press, 1996).\n\n    .. [2] Daniel, J. W., Gragg, W. B., Kaufman, L. & Stewart, G. W.\n           Reorthogonalization and stable algorithms for updating the\n           Gram-Schmidt QR factorization. Math. Comput. 30, 772-795 (1976).\n\n    .. [3] Reichel, L. & Gragg, W. B. Algorithm 686: FORTRAN Subroutines for\n           Updating the QR Decomposition. ACM Trans. Math. Softw. 16, 369-377\n           (1990).\n\n    Examples\n    --------\n    >>> import numpy as np\n    >>> from scipy import linalg\n    >>> a = np.array([[  3.,  -2.,  -2.],\n    ...               [  6.,  -7.,   4.],\n    ...               [  7.,   8.,  -6.]])\n    >>> q, r = linalg.qr(a)\n\n    Given this QR decomposition, update q and r when 2 rows are inserted.\n\n    >>> u = np.array([[  6.,  -9.,  -3.],\n    ...               [ -3.,  10.,   1.]])\n    >>> q1, r1 = linalg.qr_insert(q, r, u, 2, 'row')\n    >>> q1\n    array([[-0.25445668,  0.02246245,  0.18146236, -0.72798806,  0.60979671],  # may vary (signs)\n           [-0.50891336,  0.23226178, -0.82836478, -0.02837033, -0.00828114],\n           [-0.50891336,  0.35715302,  0.38937158,  0.58110733,  0.35235345],\n           [ 0.25445668, -0.52202743, -0.32165498,  0.36263239,  0.65404509],\n           [-0.59373225, -0.73856549,  0.16065817, -0.0063658 , -0.27595554]])\n    >>> r1\n    array([[-11.78982612,   6.44623587,   3.81685018],  # may vary (signs)\n           [  0.        , -16.01393278,   3.72202865],\n           [  0.        ,   0.        ,  -6.13010256],\n           [  0.        ,   0.        ,   0.        ],\n           [  0.        ,   0.        ,   0.        ]])\n\n    The update is equivalent, but faster than the following.\n\n    >>> a1 = np.insert(a, 2, u, 0)\n    >>> a1\n    array([[  3.,  -2.,  -2.],\n           [  6.,  -7.,   4.],\n           [  6.,  -9.,  -3.],\n           [ -3.,  10.,   1.],\n           [  7.,   8.,  -6.]])\n    >>> q_direct, r_direct = linalg.qr(a1)\n\n    Check that we have equivalent results:\n\n    >>> np.dot(q1, r1)\n    array([[  3.,  -2.,  -2.],\n           [  6.,  -7.,   4.],\n           [  6.,  -9.,  -3.],\n           [ -3.,  10.,   1.],\n           [  7.,   8.,  -6.]])\n\n    >>> np.allclose(np.dot(q1, r1), a1)\n    True\n\n    And the updated Q is still unitary:\n\n    >>> np.allclose(np.dot(q1.T, q1), np.eye(5))\n    True\n\n    ",
    'qr_update (line 2156)': "\n    Rank-k QR update\n\n    If ``A = Q R`` is the QR factorization of ``A``, return the QR\n    factorization of ``A + u v**T`` for real ``A`` or ``A + u v**H``\n    for complex ``A``.\n\n    Parameters\n    ----------\n    Q : (M, M) or (M, N) array_like\n        Unitary/orthogonal matrix from the qr decomposition of A.\n    R : (M, N) or (N, N) array_like\n        Upper triangular matrix from the qr decomposition of A.\n    u : (M,) or (M, k) array_like\n        Left update vector\n    v : (N,) or (N, k) array_like\n        Right update vector\n    overwrite_qruv : bool, optional\n        If True, consume Q, R, u, and v, if possible, while performing the\n        update, otherwise make copies as necessary. Defaults to False.\n    check_finite : bool, optional\n        Whether to check that the input matrix contains only finite numbers.\n        Disabling may give a performance gain, but may result in problems\n        (crashes, non-termination) if the inputs do contain infinities or NaNs.\n        Default is True.\n\n    Returns\n    -------\n    Q1 : ndarray\n        Updated unitary/orthogonal factor\n    R1 : ndarray\n        Updated upper triangular factor\n\n    See Also\n    --------\n    qr, qr_multiply, qr_delete, qr_insert\n\n    Notes\n    -----\n    This routine does not guarantee that the diagonal entries of `R1` are\n    real or positive.\n\n    .. versionadded:: 0.16.0\n\n    References\n    ----------\n    .. [1] Golub, G. H. & Van Loan, C. F. Matrix Computations, 3rd Ed.\n           (Johns Hopkins University Press, 1996).\n\n    .. [2] Daniel, J. W., Gragg, W. B., Kaufman, L. & Stewart, G. W.\n           Reorthogonalization and stable algorithms for updating the\n           Gram-Schmidt QR factorization. Math. Comput. 30, 772-795 (1976).\n\n    .. [3] Reichel, L. & Gragg, W. B. Algorithm 686: FORTRAN Subroutines for\n           Updating the QR Decomposition. ACM Trans. Math. Softw. 16, 369-377\n           (1990).\n\n    Examples\n    --------\n    >>> import numpy as np\n    >>> from scipy import linalg\n    >>> a = np.array([[  3.,  -2.,  -2.],\n    ...               [  6.,  -9.,  -3.],\n    ...               [ -3.,  10.,   1.],\n    ...               [  6.,  -7.,   4.],\n    ...               [  7.,   8.,  -6.]])\n    >>> q, r = linalg.qr(a)\n\n    Given this q, r decomposition, perform a rank 1 update.\n\n    >>> u = np.array([7., -2., 4., 3., 5.])\n    >>> v = np.array([1., 3., -5.])\n    >>> q_up, r_up = linalg.qr_update(q, r, u, v, False)\n    >>> q_up\n    array([[ 0.54073807,  0.18645997,  0.81707661, -0.02136616,  0.06902409],  # may vary (signs)\n           [ 0.21629523, -0.63257324,  0.06567893,  0.34125904, -0.65749222],\n           [ 0.05407381,  0.64757787, -0.12781284, -0.20031219, -0.72198188],\n           [ 0.48666426, -0.30466718, -0.27487277, -0.77079214,  0.0256951 ],\n           [ 0.64888568,  0.23001   , -0.4859845 ,  0.49883891,  0.20253783]])\n    >>> r_up\n    array([[ 18.49324201,  24.11691794, -44.98940746],  # may vary (signs)\n           [  0.        ,  31.95894662, -27.40998201],\n           [  0.        ,   0.        ,  -9.25451794],\n           [  0.        ,   0.        ,   0.        ],\n           [  0.        ,   0.        ,   0.        ]])\n\n    The update is equivalent, but faster than the following.\n\n    >>> a_up = a + np.outer(u, v)\n    >>> q_direct, r_direct = linalg.qr(a_up)\n\n    Check that we have equivalent results:\n\n    >>> np.allclose(np.dot(q_up, r_up), a_up)\n    True\n\n    And the updated Q is still unitary:\n\n    >>> np.allclose(np.dot(q_up.T, q_up), np.eye(5))\n    True\n\n    Updating economic (reduced, thin) decompositions is also possible:\n\n    >>> qe, re = linalg.qr(a, mode='economic')\n    >>> qe_up, re_up = linalg.qr_update(qe, re, u, v, False)\n    >>> qe_up\n    array([[ 0.54073807,  0.18645997,  0.81707661],  # may vary (signs)\n           [ 0.21629523, -0.63257324,  0.06567893],\n           [ 0.05407381,  0.64757787, -0.12781284],\n           [ 0.48666426, -0.30466718, -0.27487277],\n           [ 0.64888568,  0.23001   , -0.4859845 ]])\n    >>> re_up\n    array([[ 18.49324201,  24.11691794, -44.98940746],  # may vary (signs)\n           [  0.        ,  31.95894662, -27.40998201],\n           [  0.        ,   0.        ,  -9.25451794]])\n    >>> np.allclose(np.dot(qe_up, re_up), a_up)\n    True\n    >>> np.allclose(np.dot(qe_up.T, qe_up), np.eye(3))\n    True\n\n    Similarly to the above, perform a rank 2 update.\n\n    >>> u2 = np.array([[ 7., -1,],\n    ...                [-2.,  4.],\n    ...                [ 4.,  2.],\n    ...                [ 3., -6.],\n    ...                [ 5.,  3.]])\n    >>> v2 = np.array([[ 1., 2.],\n    ...                [ 3., 4.],\n    ...                [-5., 2]])\n    >>> q_up2, r_up2 = linalg.qr_update(q, r, u2, v2, False)\n    >>> q_up2\n    array([[-0.33626508, -0.03477253,  0.61956287, -0.64352987, -0.29618884],  # may vary (signs)\n           [-0.50439762,  0.58319694, -0.43010077, -0.33395279,  0.33008064],\n           [-0.21016568, -0.63123106,  0.0582249 , -0.13675572,  0.73163206],\n           [ 0.12609941,  0.49694436,  0.64590024,  0.31191919,  0.47187344],\n           [-0.75659643, -0.11517748,  0.10284903,  0.5986227 , -0.21299983]])\n    >>> r_up2\n    array([[-23.79075451, -41.1084062 ,  24.71548348],  # may vary (signs)\n           [  0.        , -33.83931057,  11.02226551],\n           [  0.        ,   0.        ,  48.91476811],\n           [  0.        ,   0.        ,   0.        ],\n           [  0.        ,   0.        ,   0.        ]])\n\n    This update is also a valid qr decomposition of ``A + U V**T``.\n\n    >>> a_up2 = a + np.dot(u2, v2.T)\n    >>> np.allclose(a_up2, np.dot(q_up2, r_up2))\n    True\n    >>> np.allclose(np.dot(q_up2.T, q_up2), np.eye(5))\n    True\n\n    ",
}

