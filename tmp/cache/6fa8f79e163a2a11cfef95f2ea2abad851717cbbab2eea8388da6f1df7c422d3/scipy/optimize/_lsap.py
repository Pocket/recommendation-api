# encoding: utf-8
# module scipy.optimize._lsap
# from /.venv/lib/python3.8/site-packages/scipy/optimize/_lsap.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
""" Solves the rectangular linear sum assignment. """
# no imports

# functions

def linear_sum_assignment(cost): # real signature unknown; restored from __doc__
    """
    Solve the linear sum assignment problem.
    
    Parameters
    ----------
    cost_matrix : array
        The cost matrix of the bipartite graph.
    
    maximize : bool (default: False)
        Calculates a maximum weight matching if true.
    
    Returns
    -------
    row_ind, col_ind : array
        An array of row indices and one of corresponding column indices giving
        the optimal assignment. The cost of the assignment can be computed
        as ``cost_matrix[row_ind, col_ind].sum()``. The row indices will be
        sorted; in the case of a square cost matrix they will be equal to
        ``numpy.arange(cost_matrix.shape[0])``.
    
    See Also
    --------
    scipy.sparse.csgraph.min_weight_full_bipartite_matching : for sparse inputs
    
    Notes
    -----
    
    The linear sum assignment problem [1]_ is also known as minimum weight
    matching in bipartite graphs. A problem instance is described by a matrix
    C, where each C[i,j] is the cost of matching vertex i of the first partite
    set (a 'worker') and vertex j of the second set (a 'job'). The goal is to
    find a complete assignment of workers to jobs of minimal cost.
    
    Formally, let X be a boolean matrix where :math:`X[i,j] = 1` iff row i is
    assigned to column j. Then the optimal assignment has cost
    
    .. math::
        \min \sum_i \sum_j C_{i,j} X_{i,j}
    
    where, in the case where the matrix X is square, each row is assigned to
    exactly one column, and each column to exactly one row.
    
    This function can also solve a generalization of the classic assignment
    problem where the cost matrix is rectangular. If it has more rows than
    columns, then not every row needs to be assigned to a column, and vice
    versa.
    
    This implementation is a modified Jonker-Volgenant algorithm with no
    initialization, described in ref. [2]_.
    
    .. versionadded:: 0.17.0
    
    References
    ----------
    
    .. [1] https://en.wikipedia.org/wiki/Assignment_problem
    
    .. [2] DF Crouse. On implementing 2D rectangular assignment algorithms.
           *IEEE Transactions on Aerospace and Electronic Systems*,
           52(4):1679-1696, August 2016, :doi:`10.1109/TAES.2016.140952`
    
    Examples
    --------
    >>> import numpy as np
    >>> cost = np.array([[4, 1, 3], [2, 0, 5], [3, 2, 2]])
    >>> from scipy.optimize import linear_sum_assignment
    >>> row_ind, col_ind = linear_sum_assignment(cost)
    >>> col_ind
    array([1, 0, 2])
    >>> cost[row_ind, col_ind].sum()
    5
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff92a425e0>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.optimize._lsap', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff92a425e0>, origin='/.venv/lib/python3.8/site-packages/scipy/optimize/_lsap.cpython-38-aarch64-linux-gnu.so')"

