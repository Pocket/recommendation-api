# encoding: utf-8
# module scipy.sparse.csgraph._matching
# from /.venv/lib/python3.8/site-packages/scipy/sparse/csgraph/_matching.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import warnings as warnings # /usr/local/lib/python3.8/warnings.py
import numpy as np # /.venv/lib/python3.8/site-packages/numpy/__init__.py
import numpy as __numpy


# functions

def isspmatrix_coo(x): # reliably restored by inspect
    """
    Is x of coo_matrix type?
    
        Parameters
        ----------
        x
            object to check for being a coo matrix
    
        Returns
        -------
        bool
            True if x is a coo matrix, False otherwise
    
        Examples
        --------
        >>> from scipy.sparse import coo_matrix, isspmatrix_coo
        >>> isspmatrix_coo(coo_matrix([[5]]))
        True
    
        >>> from scipy.sparse import coo_matrix, csr_matrix, isspmatrix_coo
        >>> isspmatrix_coo(csr_matrix([[5]]))
        False
    """
    pass

def isspmatrix_csc(x): # reliably restored by inspect
    """
    Is x of csc_matrix type?
    
        Parameters
        ----------
        x
            object to check for being a csc matrix
    
        Returns
        -------
        bool
            True if x is a csc matrix, False otherwise
    
        Examples
        --------
        >>> from scipy.sparse import csc_matrix, isspmatrix_csc
        >>> isspmatrix_csc(csc_matrix([[5]]))
        True
    
        >>> from scipy.sparse import csc_matrix, csr_matrix, isspmatrix_csc
        >>> isspmatrix_csc(csr_matrix([[5]]))
        False
    """
    pass

def isspmatrix_csr(x): # reliably restored by inspect
    """
    Is x of csr_matrix type?
    
        Parameters
        ----------
        x
            object to check for being a csr matrix
    
        Returns
        -------
        bool
            True if x is a csr matrix, False otherwise
    
        Examples
        --------
        >>> from scipy.sparse import csr_matrix, isspmatrix_csr
        >>> isspmatrix_csr(csr_matrix([[5]]))
        True
    
        >>> from scipy.sparse import csc_matrix, csr_matrix, isspmatrix_csc
        >>> isspmatrix_csr(csc_matrix([[5]]))
        False
    """
    pass

def maximum_bipartite_matching(graph, perm_type='row'): # real signature unknown; restored from __doc__
    """
    maximum_bipartite_matching(graph, perm_type='row')
    
        Returns a matching of a bipartite graph whose cardinality is as least that
        of any given matching of the graph.
    
        Parameters
        ----------
        graph : sparse matrix
            Input sparse in CSR format whose rows represent one partition of the
            graph and whose columns represent the other partition. An edge between
            two vertices is indicated by the corresponding entry in the matrix
            existing in its sparse representation.
        perm_type : str, {'row', 'column'}
            Which partition to return the matching in terms of: If ``'row'``, the
            function produces an array whose length is the number of columns in the
            input, and whose :math:`j`'th element is the row matched to the
            :math:`j`'th column. Conversely, if ``perm_type`` is ``'column'``, this
            returns the columns matched to each row.
    
        Returns
        -------
        perm : ndarray
            A matching of the vertices in one of the two partitions. Unmatched
            vertices are represented by a ``-1`` in the result.
    
        Notes
        -----
        This function implements the Hopcroft--Karp algorithm [1]_. Its time
        complexity is :math:`O(\lvert E \rvert \sqrt{\lvert V \rvert})`, and its
        space complexity is linear in the number of rows. In practice, this
        asymmetry between rows and columns means that it can be more efficient to
        transpose the input if it contains more columns than rows.
    
        By Konig's theorem, the cardinality of the matching is also the number of
        vertices appearing in a minimum vertex cover of the graph.
    
        Note that if the sparse representation contains explicit zeros, these are
        still counted as edges.
    
        The implementation was changed in SciPy 1.4.0 to allow matching of general
        bipartite graphs, where previous versions would assume that a perfect
        matching existed. As such, code written against 1.4.0 will not necessarily
        work on older versions.
    
        References
        ----------
        .. [1] John E. Hopcroft and Richard M. Karp. "An n^{5 / 2} Algorithm for
               Maximum Matchings in Bipartite Graphs" In: SIAM Journal of Computing
               2.4 (1973), pp. 225--231. :doi:`10.1137/0202019`
    
        Examples
        --------
        >>> from scipy.sparse import csr_matrix
        >>> from scipy.sparse.csgraph import maximum_bipartite_matching
    
        As a simple example, consider a bipartite graph in which the partitions
        contain 2 and 3 elements respectively. Suppose that one partition contains
        vertices labelled 0 and 1, and that the other partition contains vertices
        labelled A, B, and C. Suppose that there are edges connecting 0 and C,
        1 and A, and 1 and B. This graph would then be represented by the following
        sparse matrix:
    
        >>> graph = csr_matrix([[0, 0, 1], [1, 1, 0]])
    
        Here, the 1s could be anything, as long as they end up being stored as
        elements in the sparse matrix. We can now calculate maximum matchings as
        follows:
    
        >>> print(maximum_bipartite_matching(graph, perm_type='column'))
        [2 0]
        >>> print(maximum_bipartite_matching(graph, perm_type='row'))
        [ 1 -1  0]
    
        The first output tells us that 1 and 2 are matched with C and A
        respectively, and the second output tells us that A, B, and C are matched
        with 1, nothing, and 0 respectively.
    
        Note that explicit zeros are still converted to edges. This means that a
        different way to represent the above graph is by using the CSR structure
        directly as follows:
    
        >>> data = [0, 0, 0]
        >>> indices = [2, 0, 1]
        >>> indptr = [0, 1, 3]
        >>> graph = csr_matrix((data, indices, indptr))
        >>> print(maximum_bipartite_matching(graph, perm_type='column'))
        [2 0]
        >>> print(maximum_bipartite_matching(graph, perm_type='row'))
        [ 1 -1  0]
    
        When one or both of the partitions are empty, the matching is empty as
        well:
    
        >>> graph = csr_matrix((2, 0))
        >>> print(maximum_bipartite_matching(graph, perm_type='column'))
        [-1 -1]
        >>> print(maximum_bipartite_matching(graph, perm_type='row'))
        []
    
        When the input matrix is square, and the graph is known to admit a perfect
        matching, i.e. a matching with the property that every vertex in the graph
        belongs to some edge in the matching, then one can view the output as the
        permutation of rows (or columns) turning the input matrix into one with the
        property that all diagonal elements are non-empty:
    
        >>> a = [[0, 1, 2, 0], [1, 0, 0, 1], [2, 0, 0, 3], [0, 1, 3, 0]]
        >>> graph = csr_matrix(a)
        >>> perm = maximum_bipartite_matching(graph, perm_type='row')
        >>> print(graph[perm].toarray())
        [[1 0 0 1]
         [0 1 2 0]
         [0 1 3 0]
         [2 0 0 3]]
    """
    pass

def min_weight_full_bipartite_matching(biadjacency_matrix, maximize=False): # real signature unknown; restored from __doc__
    """
    min_weight_full_bipartite_matching(biadjacency_matrix, maximize=False)
    
        Returns the minimum weight full matching of a bipartite graph.
    
        .. versionadded:: 1.6.0
    
        Parameters
        ----------
        biadjacency_matrix : sparse matrix
            Biadjacency matrix of the bipartite graph: A sparse matrix in CSR, CSC,
            or COO format whose rows represent one partition of the graph and whose
            columns represent the other partition. An edge between two vertices is
            indicated by the corresponding entry in the matrix, and the weight of
            the edge is given by the value of that entry. This should not be
            confused with the full adjacency matrix of the graph, as we only need
            the submatrix defining the bipartite structure.
    
        maximize : bool (default: False)
            Calculates a maximum weight matching if true.
    
        Returns
        -------
        row_ind, col_ind : array
            An array of row indices and one of corresponding column indices giving
            the optimal matching. The total weight of the matching can be computed
            as ``graph[row_ind, col_ind].sum()``. The row indices will be
            sorted; in the case of a square matrix they will be equal to
            ``numpy.arange(graph.shape[0])``.
    
        Notes
        -----
    
        Let :math:`G = ((U, V), E)` be a weighted bipartite graph with non-zero
        weights :math:`w : E \to \mathbb{R} \setminus \{0\}`. This function then
        produces a matching :math:`M \subseteq E` with cardinality
    
        .. math::
           \lvert M \rvert = \min(\lvert U \rvert, \lvert V \rvert),
    
        which minimizes the sum of the weights of the edges included in the
        matching, :math:`\sum_{e \in M} w(e)`, or raises an error if no such
        matching exists.
    
        When :math:`\lvert U \rvert = \lvert V \rvert`, this is commonly
        referred to as a perfect matching; here, since we allow
        :math:`\lvert U \rvert` and :math:`\lvert V \rvert` to differ, we
        follow Karp [1]_ and refer to the matching as *full*.
    
        This function implements the LAPJVsp algorithm [2]_, short for "Linear
        assignment problem, Jonker--Volgenant, sparse".
    
        The problem it solves is equivalent to the rectangular linear assignment
        problem. [3]_ As such, this function can be used to solve the same problems
        as :func:`scipy.optimize.linear_sum_assignment`. That function may perform
        better when the input is dense, or for certain particular types of inputs,
        such as those for which the :math:`(i, j)`'th entry is the distance between
        two points in Euclidean space.
    
        If no full matching exists, this function raises a ``ValueError``. For
        determining the size of the largest matching in the graph, see
        :func:`maximum_bipartite_matching`.
    
        We require that weights are non-zero only to avoid issues with the handling
        of explicit zeros when converting between different sparse representations.
        Zero weights can be handled by adding a constant to all weights, so that
        the resulting matrix contains no zeros.
    
        References
        ----------
        .. [1] Richard Manning Karp:
           An algorithm to Solve the m x n Assignment Problem in Expected Time
           O(mn log n).
           Networks, 10(2):143-152, 1980.
        .. [2] Roy Jonker and Anton Volgenant:
           A Shortest Augmenting Path Algorithm for Dense and Sparse Linear
           Assignment Problems.
           Computing 38:325-340, 1987.
        .. [3] https://en.wikipedia.org/wiki/Assignment_problem
    
        Examples
        --------
        >>> from scipy.sparse import csr_matrix
        >>> from scipy.sparse.csgraph import min_weight_full_bipartite_matching
    
        Let us first consider an example in which all weights are equal:
    
        >>> biadjacency_matrix = csr_matrix([[1, 1, 1], [1, 0, 0], [0, 1, 0]])
    
        Here, all we get is a perfect matching of the graph:
    
        >>> print(min_weight_full_bipartite_matching(biadjacency_matrix)[1])
        [2 0 1]
    
        That is, the first, second, and third rows are matched with the third,
        first, and second column respectively. Note that in this example, the 0
        in the input matrix does *not* correspond to an edge with weight 0, but
        rather a pair of vertices not paired by an edge.
    
        Note also that in this case, the output matches the result of applying
        :func:`maximum_bipartite_matching`:
    
        >>> from scipy.sparse.csgraph import maximum_bipartite_matching
        >>> biadjacency = csr_matrix([[1, 1, 1], [1, 0, 0], [0, 1, 0]])
        >>> print(maximum_bipartite_matching(biadjacency, perm_type='column'))
        [2 0 1]
    
        When multiple edges are available, the ones with lowest weights are
        preferred:
    
        >>> biadjacency = csr_matrix([[3, 3, 6], [4, 3, 5], [10, 1, 8]])
        >>> row_ind, col_ind = min_weight_full_bipartite_matching(biadjacency)
        >>> print(col_ind)
        [0 2 1]
    
        The total weight in this case is :math:`3 + 5 + 1 = 9`:
    
        >>> print(biadjacency[row_ind, col_ind].sum())
        9
    
        When the matrix is not square, i.e. when the two partitions have different
        cardinalities, the matching is as large as the smaller of the two
        partitions:
    
        >>> biadjacency = csr_matrix([[0, 1, 1], [0, 2, 3]])
        >>> row_ind, col_ind = min_weight_full_bipartite_matching(biadjacency)
        >>> print(row_ind, col_ind)
        [0 1] [2 1]
        >>> biadjacency = csr_matrix([[0, 1], [3, 1], [1, 4]])
        >>> row_ind, col_ind = min_weight_full_bipartite_matching(biadjacency)
        >>> print(row_ind, col_ind)
        [0 2] [1 0]
    
        When one or both of the partitions are empty, the matching is empty as
        well:
    
        >>> biadjacency = csr_matrix((2, 0))
        >>> row_ind, col_ind = min_weight_full_bipartite_matching(biadjacency)
        >>> print(row_ind, col_ind)
        [] []
    
        In general, we will always reach the same sum of weights as if we had used
        :func:`scipy.optimize.linear_sum_assignment` but note that for that one,
        missing edges are represented by a matrix entry of ``float('inf')``. Let us
        generate a random sparse matrix with integer entries between 1 and 10:
    
        >>> import numpy as np
        >>> from scipy.sparse import random
        >>> from scipy.optimize import linear_sum_assignment
        >>> sparse = random(10, 10, random_state=42, density=.5, format='coo') * 10
        >>> sparse.data = np.ceil(sparse.data)
        >>> dense = sparse.toarray()
        >>> dense = np.full(sparse.shape, np.inf)
        >>> dense[sparse.row, sparse.col] = sparse.data
        >>> sparse = sparse.tocsr()
        >>> row_ind, col_ind = linear_sum_assignment(dense)
        >>> print(dense[row_ind, col_ind].sum())
        28.0
        >>> row_ind, col_ind = min_weight_full_bipartite_matching(sparse)
        >>> print(sparse[row_ind, col_ind].sum())
        28.0
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class BTYPE(__numpy.unsignedinteger):
    """
    Unsigned integer type, compatible with C ``unsigned char``.
    
        :Character code: ``'B'``
        :Canonical name: `numpy.ubyte`
        :Alias on this platform (Linux aarch64): `numpy.uint8`: 8-bit unsigned integer (``0`` to ``255``).
    """
    def bit_count(self): # real signature unknown; restored from __doc__
        """
        uint8.bit_count() -> int
        
                Computes the number of 1-bits in the absolute value of the input.
                Analogous to the builtin `int.bit_count` or ``popcount`` in C++.
        
                Examples
                --------
                >>> np.uint8(127).bit_count()
                7
        """
        return 0

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    @classmethod
    def __class_getitem__(cls, *args, **kwargs): # real signature unknown
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
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
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
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

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass


class DTYPE(__numpy.floating, float):
    """
    Double-precision floating-point number type, compatible with Python `float`
        and C ``double``.
    
        :Character code: ``'d'``
        :Canonical name: `numpy.double`
        :Alias: `numpy.float_`
        :Alias on this platform (Linux aarch64): `numpy.float64`: 64-bit precision floating-point number type: sign bit, 11 bits exponent, 52 bits mantissa.
    """
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        double.as_integer_ratio() -> (int, int)
        
                Return a pair of integers, whose ratio is exactly equal to the original
                floating point number, and with a positive denominator.
                Raise `OverflowError` on infinities and a `ValueError` on NaNs.
        
                >>> np.double(10.0).as_integer_ratio()
                (10, 1)
                >>> np.double(0.0).as_integer_ratio()
                (0, 1)
                >>> np.double(-.25).as_integer_ratio()
                (-1, 4)
        """
        pass

    def is_integer(self): # real signature unknown; restored from __doc__
        """
        double.is_integer() -> bool
        
                Return ``True`` if the floating point number is finite with integral
                value, and ``False`` otherwise.
        
                .. versionadded:: 1.22
        
                Examples
                --------
                >>> np.double(-2.0).is_integer()
                True
                >>> np.double(3.2).is_integer()
                False
        """
        return False

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    @classmethod
    def __class_getitem__(cls, *args, **kwargs): # real signature unknown
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
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
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
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

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
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


class ITYPE(__numpy.signedinteger):
    """
    Signed integer type, compatible with C ``int``.
    
        :Character code: ``'i'``
        :Canonical name: `numpy.intc`
        :Alias on this platform (Linux aarch64): `numpy.int32`: 32-bit signed integer (``-2_147_483_648`` to ``2_147_483_647``).
    """
    def bit_count(self): # real signature unknown; restored from __doc__
        """
        int32.bit_count() -> int
        
                Computes the number of 1-bits in the absolute value of the input.
                Analogous to the builtin `int.bit_count` or ``popcount`` in C++.
        
                Examples
                --------
                >>> np.int32(127).bit_count()
                7
                >>> np.int32(-127).bit_count()
                7
        """
        return 0

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    @classmethod
    def __class_getitem__(cls, *args, **kwargs): # real signature unknown
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
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
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
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

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff932c87c0>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.sparse.csgraph._matching', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff932c87c0>, origin='/.venv/lib/python3.8/site-packages/scipy/sparse/csgraph/_matching.cpython-38-aarch64-linux-gnu.so')"

__test__ = {
    'maximum_bipartite_matching (line 16)': '\n    maximum_bipartite_matching(graph, perm_type=\'row\')\n\n    Returns a matching of a bipartite graph whose cardinality is as least that\n    of any given matching of the graph.\n\n    Parameters\n    ----------\n    graph : sparse matrix\n        Input sparse in CSR format whose rows represent one partition of the\n        graph and whose columns represent the other partition. An edge between\n        two vertices is indicated by the corresponding entry in the matrix\n        existing in its sparse representation.\n    perm_type : str, {\'row\', \'column\'}\n        Which partition to return the matching in terms of: If ``\'row\'``, the\n        function produces an array whose length is the number of columns in the\n        input, and whose :math:`j`\'th element is the row matched to the\n        :math:`j`\'th column. Conversely, if ``perm_type`` is ``\'column\'``, this\n        returns the columns matched to each row.\n\n    Returns\n    -------\n    perm : ndarray\n        A matching of the vertices in one of the two partitions. Unmatched\n        vertices are represented by a ``-1`` in the result.\n\n    Notes\n    -----\n    This function implements the Hopcroft--Karp algorithm [1]_. Its time\n    complexity is :math:`O(\\lvert E \\rvert \\sqrt{\\lvert V \\rvert})`, and its\n    space complexity is linear in the number of rows. In practice, this\n    asymmetry between rows and columns means that it can be more efficient to\n    transpose the input if it contains more columns than rows.\n\n    By Konig\'s theorem, the cardinality of the matching is also the number of\n    vertices appearing in a minimum vertex cover of the graph.\n\n    Note that if the sparse representation contains explicit zeros, these are\n    still counted as edges.\n\n    The implementation was changed in SciPy 1.4.0 to allow matching of general\n    bipartite graphs, where previous versions would assume that a perfect\n    matching existed. As such, code written against 1.4.0 will not necessarily\n    work on older versions.\n\n    References\n    ----------\n    .. [1] John E. Hopcroft and Richard M. Karp. "An n^{5 / 2} Algorithm for\n           Maximum Matchings in Bipartite Graphs" In: SIAM Journal of Computing\n           2.4 (1973), pp. 225--231. :doi:`10.1137/0202019`\n\n    Examples\n    --------\n    >>> from scipy.sparse import csr_matrix\n    >>> from scipy.sparse.csgraph import maximum_bipartite_matching\n\n    As a simple example, consider a bipartite graph in which the partitions\n    contain 2 and 3 elements respectively. Suppose that one partition contains\n    vertices labelled 0 and 1, and that the other partition contains vertices\n    labelled A, B, and C. Suppose that there are edges connecting 0 and C,\n    1 and A, and 1 and B. This graph would then be represented by the following\n    sparse matrix:\n\n    >>> graph = csr_matrix([[0, 0, 1], [1, 1, 0]])\n\n    Here, the 1s could be anything, as long as they end up being stored as\n    elements in the sparse matrix. We can now calculate maximum matchings as\n    follows:\n\n    >>> print(maximum_bipartite_matching(graph, perm_type=\'column\'))\n    [2 0]\n    >>> print(maximum_bipartite_matching(graph, perm_type=\'row\'))\n    [ 1 -1  0]\n\n    The first output tells us that 1 and 2 are matched with C and A\n    respectively, and the second output tells us that A, B, and C are matched\n    with 1, nothing, and 0 respectively.\n\n    Note that explicit zeros are still converted to edges. This means that a\n    different way to represent the above graph is by using the CSR structure\n    directly as follows:\n\n    >>> data = [0, 0, 0]\n    >>> indices = [2, 0, 1]\n    >>> indptr = [0, 1, 3]\n    >>> graph = csr_matrix((data, indices, indptr))\n    >>> print(maximum_bipartite_matching(graph, perm_type=\'column\'))\n    [2 0]\n    >>> print(maximum_bipartite_matching(graph, perm_type=\'row\'))\n    [ 1 -1  0]\n\n    When one or both of the partitions are empty, the matching is empty as\n    well:\n\n    >>> graph = csr_matrix((2, 0))\n    >>> print(maximum_bipartite_matching(graph, perm_type=\'column\'))\n    [-1 -1]\n    >>> print(maximum_bipartite_matching(graph, perm_type=\'row\'))\n    []\n\n    When the input matrix is square, and the graph is known to admit a perfect\n    matching, i.e. a matching with the property that every vertex in the graph\n    belongs to some edge in the matching, then one can view the output as the\n    permutation of rows (or columns) turning the input matrix into one with the\n    property that all diagonal elements are non-empty:\n\n    >>> a = [[0, 1, 2, 0], [1, 0, 0, 1], [2, 0, 0, 3], [0, 1, 3, 0]]\n    >>> graph = csr_matrix(a)\n    >>> perm = maximum_bipartite_matching(graph, perm_type=\'row\')\n    >>> print(graph[perm].toarray())\n    [[1 0 0 1]\n     [0 1 2 0]\n     [0 1 3 0]\n     [2 0 0 3]]\n\n    ',
    'min_weight_full_bipartite_matching (line 282)': '\n    min_weight_full_bipartite_matching(biadjacency_matrix, maximize=False)\n\n    Returns the minimum weight full matching of a bipartite graph.\n\n    .. versionadded:: 1.6.0\n\n    Parameters\n    ----------\n    biadjacency_matrix : sparse matrix\n        Biadjacency matrix of the bipartite graph: A sparse matrix in CSR, CSC,\n        or COO format whose rows represent one partition of the graph and whose\n        columns represent the other partition. An edge between two vertices is\n        indicated by the corresponding entry in the matrix, and the weight of\n        the edge is given by the value of that entry. This should not be\n        confused with the full adjacency matrix of the graph, as we only need\n        the submatrix defining the bipartite structure.\n\n    maximize : bool (default: False)\n        Calculates a maximum weight matching if true.\n\n    Returns\n    -------\n    row_ind, col_ind : array\n        An array of row indices and one of corresponding column indices giving\n        the optimal matching. The total weight of the matching can be computed\n        as ``graph[row_ind, col_ind].sum()``. The row indices will be\n        sorted; in the case of a square matrix they will be equal to\n        ``numpy.arange(graph.shape[0])``.\n\n    Notes\n    -----\n\n    Let :math:`G = ((U, V), E)` be a weighted bipartite graph with non-zero\n    weights :math:`w : E \\to \\mathbb{R} \\setminus \\{0\\}`. This function then\n    produces a matching :math:`M \\subseteq E` with cardinality\n\n    .. math::\n       \\lvert M \\rvert = \\min(\\lvert U \\rvert, \\lvert V \\rvert),\n\n    which minimizes the sum of the weights of the edges included in the\n    matching, :math:`\\sum_{e \\in M} w(e)`, or raises an error if no such\n    matching exists.\n\n    When :math:`\\lvert U \\rvert = \\lvert V \\rvert`, this is commonly\n    referred to as a perfect matching; here, since we allow\n    :math:`\\lvert U \\rvert` and :math:`\\lvert V \\rvert` to differ, we\n    follow Karp [1]_ and refer to the matching as *full*.\n\n    This function implements the LAPJVsp algorithm [2]_, short for "Linear\n    assignment problem, Jonker--Volgenant, sparse".\n\n    The problem it solves is equivalent to the rectangular linear assignment\n    problem. [3]_ As such, this function can be used to solve the same problems\n    as :func:`scipy.optimize.linear_sum_assignment`. That function may perform\n    better when the input is dense, or for certain particular types of inputs,\n    such as those for which the :math:`(i, j)`\'th entry is the distance between\n    two points in Euclidean space.\n\n    If no full matching exists, this function raises a ``ValueError``. For\n    determining the size of the largest matching in the graph, see\n    :func:`maximum_bipartite_matching`.\n\n    We require that weights are non-zero only to avoid issues with the handling\n    of explicit zeros when converting between different sparse representations.\n    Zero weights can be handled by adding a constant to all weights, so that\n    the resulting matrix contains no zeros.\n\n    References\n    ----------\n    .. [1] Richard Manning Karp:\n       An algorithm to Solve the m x n Assignment Problem in Expected Time\n       O(mn log n).\n       Networks, 10(2):143-152, 1980.\n    .. [2] Roy Jonker and Anton Volgenant:\n       A Shortest Augmenting Path Algorithm for Dense and Sparse Linear\n       Assignment Problems.\n       Computing 38:325-340, 1987.\n    .. [3] https://en.wikipedia.org/wiki/Assignment_problem\n\n    Examples\n    --------\n    >>> from scipy.sparse import csr_matrix\n    >>> from scipy.sparse.csgraph import min_weight_full_bipartite_matching\n\n    Let us first consider an example in which all weights are equal:\n\n    >>> biadjacency_matrix = csr_matrix([[1, 1, 1], [1, 0, 0], [0, 1, 0]])\n\n    Here, all we get is a perfect matching of the graph:\n\n    >>> print(min_weight_full_bipartite_matching(biadjacency_matrix)[1])\n    [2 0 1]\n\n    That is, the first, second, and third rows are matched with the third,\n    first, and second column respectively. Note that in this example, the 0\n    in the input matrix does *not* correspond to an edge with weight 0, but\n    rather a pair of vertices not paired by an edge.\n\n    Note also that in this case, the output matches the result of applying\n    :func:`maximum_bipartite_matching`:\n\n    >>> from scipy.sparse.csgraph import maximum_bipartite_matching\n    >>> biadjacency = csr_matrix([[1, 1, 1], [1, 0, 0], [0, 1, 0]])\n    >>> print(maximum_bipartite_matching(biadjacency, perm_type=\'column\'))\n    [2 0 1]\n\n    When multiple edges are available, the ones with lowest weights are\n    preferred:\n\n    >>> biadjacency = csr_matrix([[3, 3, 6], [4, 3, 5], [10, 1, 8]])\n    >>> row_ind, col_ind = min_weight_full_bipartite_matching(biadjacency)\n    >>> print(col_ind)\n    [0 2 1]\n\n    The total weight in this case is :math:`3 + 5 + 1 = 9`:\n\n    >>> print(biadjacency[row_ind, col_ind].sum())\n    9\n\n    When the matrix is not square, i.e. when the two partitions have different\n    cardinalities, the matching is as large as the smaller of the two\n    partitions:\n\n    >>> biadjacency = csr_matrix([[0, 1, 1], [0, 2, 3]])\n    >>> row_ind, col_ind = min_weight_full_bipartite_matching(biadjacency)\n    >>> print(row_ind, col_ind)\n    [0 1] [2 1]\n    >>> biadjacency = csr_matrix([[0, 1], [3, 1], [1, 4]])\n    >>> row_ind, col_ind = min_weight_full_bipartite_matching(biadjacency)\n    >>> print(row_ind, col_ind)\n    [0 2] [1 0]\n\n    When one or both of the partitions are empty, the matching is empty as\n    well:\n\n    >>> biadjacency = csr_matrix((2, 0))\n    >>> row_ind, col_ind = min_weight_full_bipartite_matching(biadjacency)\n    >>> print(row_ind, col_ind)\n    [] []\n\n    In general, we will always reach the same sum of weights as if we had used\n    :func:`scipy.optimize.linear_sum_assignment` but note that for that one,\n    missing edges are represented by a matrix entry of ``float(\'inf\')``. Let us\n    generate a random sparse matrix with integer entries between 1 and 10:\n\n    >>> import numpy as np\n    >>> from scipy.sparse import random\n    >>> from scipy.optimize import linear_sum_assignment\n    >>> sparse = random(10, 10, random_state=42, density=.5, format=\'coo\') * 10\n    >>> sparse.data = np.ceil(sparse.data)\n    >>> dense = sparse.toarray()\n    >>> dense = np.full(sparse.shape, np.inf)\n    >>> dense[sparse.row, sparse.col] = sparse.data\n    >>> sparse = sparse.tocsr()\n    >>> row_ind, col_ind = linear_sum_assignment(dense)\n    >>> print(dense[row_ind, col_ind].sum())\n    28.0\n    >>> row_ind, col_ind = min_weight_full_bipartite_matching(sparse)\n    >>> print(sparse[row_ind, col_ind].sum())\n    28.0\n\n    ',
}

