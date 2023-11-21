# encoding: utf-8
# module scipy.sparse.csgraph._flow
# from /.venv/lib/python3.8/site-packages/scipy/sparse/csgraph/_flow.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /.venv/lib/python3.8/site-packages/numpy/__init__.py
import warnings as warnings # /usr/local/lib/python3.8/warnings.py
import numpy as __numpy
import scipy.sparse._compressed as __scipy_sparse__compressed


# functions

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

def maximum_flow(csgraph, source, sink): # real signature unknown; restored from __doc__
    """
    maximum_flow(csgraph, source, sink)
    
        Maximize the flow between two vertices in a graph.
    
        .. versionadded:: 1.4.0
    
        Parameters
        ----------
        csgraph : csr_matrix
            The square matrix representing a directed graph whose (i, j)'th entry
            is an integer representing the capacity of the edge between
            vertices i and j.
        source : int
            The source vertex from which the flow flows.
        sink : int
            The sink vertex to which the flow flows.
        method: {'edmonds_karp', 'dinic'}, optional
            The method/algorithm to be used for computing the maximum flow.
            Following methods are supported,
    
                * 'edmonds_karp': Edmonds Karp algorithm in [1]_.
                * 'dinic': Dinic's algorithm in [4]_.
    
            Default is 'dinic'.
    
            .. versionadded:: 1.8.0
    
        Returns
        -------
        res : MaximumFlowResult
            A maximum flow represented by a ``MaximumFlowResult``
            which includes the value of the flow in ``flow_value``,
            and the flow graph in ``flow``.
    
        Raises
        ------
        TypeError:
            if the input graph is not in CSR format.
    
        ValueError:
            if the capacity values are not integers, or the source or sink are out
            of bounds.
    
        Notes
        -----
        This solves the maximum flow problem on a given directed weighted graph:
        A flow associates to every edge a value, also called a flow, less than the
        capacity of the edge, so that for every vertex (apart from the source and
        the sink vertices), the total incoming flow is equal to the total outgoing
        flow. The value of a flow is the sum of the flow of all edges leaving the
        source vertex, and the maximum flow problem consists of finding a flow
        whose value is maximal.
    
        By the max-flow min-cut theorem, the maximal value of the flow is also the
        total weight of the edges in a minimum cut.
    
        To solve the problem, we provide Edmonds--Karp [1]_ and Dinic's algorithm
        [4]_. The implementation of both algorithms strive to exploit sparsity.
        The time complexity of the former :math:`O(|V|\,|E|^2)` and its space
        complexity is :math:`O(|E|)`. The latter achieves its performance by
        building level graphs and finding blocking flows in them. Its time
        complexity is :math:`O(|V|^2\,|E|)` and its space complexity is
        :math:`O(|E|)`.
    
        The maximum flow problem is usually defined with real valued capacities,
        but we require that all capacities are integral to ensure convergence. When
        dealing with rational capacities, or capacities belonging to
        :math:`x\mathbb{Q}` for some fixed :math:`x \in \mathbb{R}`, it is possible
        to reduce the problem to the integral case by scaling all capacities
        accordingly.
    
        Solving a maximum-flow problem can be used for example for graph cuts
        optimization in computer vision [3]_.
    
        References
        ----------
        .. [1] Edmonds, J. and Karp, R. M.
               Theoretical improvements in algorithmic efficiency for network flow
               problems. 1972. Journal of the ACM. 19 (2): pp. 248-264
        .. [2] Cormen, T. H. and Leiserson, C. E. and Rivest, R. L. and Stein C.
               Introduction to Algorithms. Second Edition. 2001. MIT Press.
        .. [3] https://en.wikipedia.org/wiki/Graph_cuts_in_computer_vision
        .. [4] Dinic, Efim A.
               Algorithm for solution of a problem of maximum flow in networks with
               power estimation. In Soviet Math. Doklady, vol. 11, pp. 1277-1280.
               1970.
    
        Examples
        --------
        Perhaps the simplest flow problem is that of a graph of only two vertices
        with an edge from source (0) to sink (1)::
    
            (0) --5--> (1)
    
        Here, the maximum flow is simply the capacity of the edge:
    
        >>> import numpy as np
        >>> from scipy.sparse import csr_matrix
        >>> from scipy.sparse.csgraph import maximum_flow
        >>> graph = csr_matrix([[0, 5], [0, 0]])
        >>> maximum_flow(graph, 0, 1).flow_value
        5
        >>> maximum_flow(graph, 0, 1, method='edmonds_karp').flow_value
        5
    
        If, on the other hand, there is a bottleneck between source and sink, that
        can reduce the maximum flow::
    
            (0) --5--> (1) --3--> (2)
    
        >>> graph = csr_matrix([[0, 5, 0], [0, 0, 3], [0, 0, 0]])
        >>> maximum_flow(graph, 0, 2).flow_value
        3
    
        A less trivial example is given in [2]_, Chapter 26.1:
    
        >>> graph = csr_matrix([[0, 16, 13,  0,  0,  0],
        ...                     [0,  0, 10, 12,  0,  0],
        ...                     [0,  4,  0,  0, 14,  0],
        ...                     [0,  0,  9,  0,  0, 20],
        ...                     [0,  0,  0,  7,  0,  4],
        ...                     [0,  0,  0,  0,  0,  0]])
        >>> maximum_flow(graph, 0, 5).flow_value
        23
    
        It is possible to reduce the problem of finding a maximum matching in a
        bipartite graph to a maximum flow problem: Let :math:`G = ((U, V), E)` be a
        bipartite graph. Then, add to the graph a source vertex with edges to every
        vertex in :math:`U` and a sink vertex with edges from every vertex in
        :math:`V`. Finally, give every edge in the resulting graph a capacity of 1.
        Then, a maximum flow in the new graph gives a maximum matching in the
        original graph consisting of the edges in :math:`E` whose flow is positive.
    
        Assume that the edges are represented by a
        :math:`\lvert U \rvert \times \lvert V \rvert` matrix in CSR format whose
        :math:`(i, j)`'th entry is 1 if there is an edge from :math:`i \in U` to
        :math:`j \in V` and 0 otherwise; that is, the input is of the form required
        by :func:`maximum_bipartite_matching`. Then the CSR representation of the
        graph constructed above contains this matrix as a block. Here's an example:
    
        >>> graph = csr_matrix([[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 1, 0]])
        >>> print(graph.toarray())
        [[0 1 0 1]
         [1 0 1 0]
         [0 1 1 0]]
        >>> i, j = graph.shape
        >>> n = graph.nnz
        >>> indptr = np.concatenate([[0],
        ...                          graph.indptr + i,
        ...                          np.arange(n + i + 1, n + i + j + 1),
        ...                          [n + i + j]])
        >>> indices = np.concatenate([np.arange(1, i + 1),
        ...                           graph.indices + i + 1,
        ...                           np.repeat(i + j + 1, j)])
        >>> data = np.ones(n + i + j, dtype=int)
        >>>
        >>> graph_flow = csr_matrix((data, indices, indptr))
        >>> print(graph_flow.toarray())
        [[0 1 1 1 0 0 0 0 0]
         [0 0 0 0 0 1 0 1 0]
         [0 0 0 0 1 0 1 0 0]
         [0 0 0 0 0 1 1 0 0]
         [0 0 0 0 0 0 0 0 1]
         [0 0 0 0 0 0 0 0 1]
         [0 0 0 0 0 0 0 0 1]
         [0 0 0 0 0 0 0 0 1]
         [0 0 0 0 0 0 0 0 0]]
    
        At this point, we can find the maximum flow between the added sink and the
        added source and the desired matching can be obtained by restricting the
        flow function to the block corresponding to the original graph:
    
        >>> result = maximum_flow(graph_flow, 0, i+j+1, method='dinic')
        >>> matching = result.flow[1:i+1, i+1:i+j+1]
        >>> print(matching.toarray())
        [[0 1 0 0]
         [1 0 0 0]
         [0 0 1 0]]
    
        This tells us that the first, second, and third vertex in :math:`U` are
        matched with the second, first, and third vertex in :math:`V` respectively.
    
        While this solves the maximum bipartite matching problem in general, note
        that algorithms specialized to that problem, such as
        :func:`maximum_bipartite_matching`, will generally perform better.
    
        This approach can also be used to solve various common generalizations of
        the maximum bipartite matching problem. If, for instance, some vertices can
        be matched with more than one other vertex, this may be handled by
        modifying the capacities of the new graph appropriately.
    """
    pass

def _add_reverse_edges(*args, **kwargs): # real signature unknown
    """
    Add reversed edges to all edges in a graph.
    
        This adds to a given directed weighted graph all edges in the reverse
        direction and give them weight 0, unless they already exist.
    
        Parameters
        ----------
        a : csr_matrix
            The square matrix in CSR format representing a directed graph
    
        Returns
        -------
        res : csr_matrix
            A new matrix in CSR format in which the missing edges are represented
            by explicit zeros.
    """
    pass

def _make_edge_pointers(*args, **kwargs): # real signature unknown
    """ Create for each edge pointers to its reverse. """
    pass

def _make_tails(*args, **kwargs): # real signature unknown
    """ Create for each edge pointers to its tail. """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class csr_matrix(__scipy_sparse__compressed._cs_matrix):
    """
    Compressed Sparse Row matrix
    
        This can be instantiated in several ways:
            csr_matrix(D)
                with a dense matrix or rank-2 ndarray D
    
            csr_matrix(S)
                with another sparse matrix S (equivalent to S.tocsr())
    
            csr_matrix((M, N), [dtype])
                to construct an empty matrix with shape (M, N)
                dtype is optional, defaulting to dtype='d'.
    
            csr_matrix((data, (row_ind, col_ind)), [shape=(M, N)])
                where ``data``, ``row_ind`` and ``col_ind`` satisfy the
                relationship ``a[row_ind[k], col_ind[k]] = data[k]``.
    
            csr_matrix((data, indices, indptr), [shape=(M, N)])
                is the standard CSR representation where the column indices for
                row i are stored in ``indices[indptr[i]:indptr[i+1]]`` and their
                corresponding values are stored in ``data[indptr[i]:indptr[i+1]]``.
                If the shape parameter is not supplied, the matrix dimensions
                are inferred from the index arrays.
    
        Attributes
        ----------
        dtype : dtype
            Data type of the matrix
        shape : 2-tuple
            Shape of the matrix
        ndim : int
            Number of dimensions (this is always 2)
        nnz
            Number of stored values, including explicit zeros
        data
            CSR format data array of the matrix
        indices
            CSR format index array of the matrix
        indptr
            CSR format index pointer array of the matrix
        has_sorted_indices
            Whether indices are sorted
    
        Notes
        -----
    
        Sparse matrices can be used in arithmetic operations: they support
        addition, subtraction, multiplication, division, and matrix power.
    
        Advantages of the CSR format
          - efficient arithmetic operations CSR + CSR, CSR * CSR, etc.
          - efficient row slicing
          - fast matrix vector products
    
        Disadvantages of the CSR format
          - slow column slicing operations (consider CSC)
          - changes to the sparsity structure are expensive (consider LIL or DOK)
    
        Examples
        --------
    
        >>> import numpy as np
        >>> from scipy.sparse import csr_matrix
        >>> csr_matrix((3, 4), dtype=np.int8).toarray()
        array([[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]], dtype=int8)
    
        >>> row = np.array([0, 0, 1, 2, 2, 2])
        >>> col = np.array([0, 2, 2, 0, 1, 2])
        >>> data = np.array([1, 2, 3, 4, 5, 6])
        >>> csr_matrix((data, (row, col)), shape=(3, 3)).toarray()
        array([[1, 0, 2],
               [0, 0, 3],
               [4, 5, 6]])
    
        >>> indptr = np.array([0, 2, 3, 6])
        >>> indices = np.array([0, 2, 2, 0, 1, 2])
        >>> data = np.array([1, 2, 3, 4, 5, 6])
        >>> csr_matrix((data, indices, indptr), shape=(3, 3)).toarray()
        array([[1, 0, 2],
               [0, 0, 3],
               [4, 5, 6]])
    
        Duplicate entries are summed together:
    
        >>> row = np.array([0, 1, 2, 0])
        >>> col = np.array([0, 1, 1, 0])
        >>> data = np.array([1, 2, 4, 8])
        >>> csr_matrix((data, (row, col)), shape=(3, 3)).toarray()
        array([[9, 0, 0],
               [0, 2, 0],
               [0, 4, 0]])
    
        As an example of how to construct a CSR matrix incrementally,
        the following snippet builds a term-document matrix from texts:
    
        >>> docs = [["hello", "world", "hello"], ["goodbye", "cruel", "world"]]
        >>> indptr = [0]
        >>> indices = []
        >>> data = []
        >>> vocabulary = {}
        >>> for d in docs:
        ...     for term in d:
        ...         index = vocabulary.setdefault(term, len(vocabulary))
        ...         indices.append(index)
        ...         data.append(1)
        ...     indptr.append(len(indices))
        ...
        >>> csr_matrix((data, indices, indptr), dtype=int).toarray()
        array([[2, 1, 0, 0],
               [0, 1, 1, 1]])
    """
    def getcol(self, i): # reliably restored by inspect
        """
        Returns a copy of column i of the matrix, as a (m x 1)
                CSR matrix (column vector).
        """
        pass

    def getrow(self, i): # reliably restored by inspect
        """
        Returns a copy of row i of the matrix, as a (1 x n)
                CSR matrix (row vector).
        """
        pass

    def tobsr(self, blocksize=None, copy=True): # reliably restored by inspect
        """
        Convert this matrix to Block Sparse Row format.
        
                With copy=False, the data/indices may be shared between this matrix and
                the resultant bsr_matrix.
        
                When blocksize=(R, C) is provided, it will be used for construction of
                the bsr_matrix.
        """
        pass

    def tocsc(self, copy=False): # reliably restored by inspect
        """
        Convert this matrix to Compressed Sparse Column format.
        
                With copy=False, the data/indices may be shared between this matrix and
                the resultant csc_matrix.
        """
        pass

    def tocsr(self, copy=False): # reliably restored by inspect
        """
        Convert this matrix to Compressed Sparse Row format.
        
                With copy=False, the data/indices may be shared between this matrix and
                the resultant csr_matrix.
        """
        pass

    def tolil(self, copy=False): # reliably restored by inspect
        """
        Convert this matrix to List of Lists format.
        
                With copy=False, the data/indices may be shared between this matrix and
                the resultant lil_matrix.
        """
        pass

    def transpose(self, axes=None, copy=False): # reliably restored by inspect
        """
        Reverses the dimensions of the sparse matrix.
        
                Parameters
                ----------
                axes : None, optional
                    This argument is in the signature *solely* for NumPy
                    compatibility reasons. Do not pass in anything except
                    for the default value.
                copy : bool, optional
                    Indicates whether or not attributes of `self` should be
                    copied whenever possible. The degree to which attributes
                    are copied varies depending on the type of sparse matrix
                    being used.
        
                Returns
                -------
                p : `self` with the dimensions reversed.
        
                See Also
                --------
                numpy.matrix.transpose : NumPy's implementation of 'transpose'
                                         for matrices
        """
        pass

    def _get_arrayXint(self, row, col): # reliably restored by inspect
        # no doc
        pass

    def _get_arrayXslice(self, row, col): # reliably restored by inspect
        # no doc
        pass

    def _get_intXarray(self, row, col): # reliably restored by inspect
        # no doc
        pass

    def _get_intXslice(self, row, col): # reliably restored by inspect
        # no doc
        pass

    def _get_sliceXarray(self, row, col): # reliably restored by inspect
        # no doc
        pass

    def _get_sliceXint(self, row, col): # reliably restored by inspect
        # no doc
        pass

    def _swap(self, x): # reliably restored by inspect
        """ swap the members of x if this is a column-oriented matrix """
        pass

    def __init__(self, arg1, shape=None, dtype=None, copy=False): # reliably restored by inspect
        # no doc
        pass

    def __iter__(self): # reliably restored by inspect
        # no doc
        pass

    format = 'csr'


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


class MaximumFlowResult(object):
    """
    Represents the result of a maximum flow calculation.
    
        Attributes
        ----------
        flow_value : int
            The value of the maximum flow.
        flow : csr_matrix
            The maximum flow.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    residual = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'scipy.sparse.csgraph._flow', '__doc__': 'Represents the result of a maximum flow calculation.\\n\\n    Attributes\\n    ----------\\n    flow_value : int\\n        The value of the maximum flow.\\n    flow : csr_matrix\\n        The maximum flow.\\n    ', '__init__': <cyfunction MaximumFlowResult.__init__ at 0xffff9f5f75f0>, '__repr__': <cyfunction MaximumFlowResult.__repr__ at 0xffff9f5f76c0>, 'residual': <property object at 0xffff932fa720>, '__dict__': <attribute '__dict__' of 'MaximumFlowResult' objects>, '__weakref__': <attribute '__weakref__' of 'MaximumFlowResult' objects>})"


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9f60fe50>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.sparse.csgraph._flow', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9f60fe50>, origin='/.venv/lib/python3.8/site-packages/scipy/sparse/csgraph/_flow.cpython-38-aarch64-linux-gnu.so')"

__test__ = {
    'maximum_flow (line 43)': "\n    maximum_flow(csgraph, source, sink)\n\n    Maximize the flow between two vertices in a graph.\n\n    .. versionadded:: 1.4.0\n\n    Parameters\n    ----------\n    csgraph : csr_matrix\n        The square matrix representing a directed graph whose (i, j)'th entry\n        is an integer representing the capacity of the edge between\n        vertices i and j.\n    source : int\n        The source vertex from which the flow flows.\n    sink : int\n        The sink vertex to which the flow flows.\n    method: {'edmonds_karp', 'dinic'}, optional\n        The method/algorithm to be used for computing the maximum flow.\n        Following methods are supported,\n\n            * 'edmonds_karp': Edmonds Karp algorithm in [1]_.\n            * 'dinic': Dinic's algorithm in [4]_.\n\n        Default is 'dinic'.\n\n        .. versionadded:: 1.8.0\n\n    Returns\n    -------\n    res : MaximumFlowResult\n        A maximum flow represented by a ``MaximumFlowResult``\n        which includes the value of the flow in ``flow_value``,\n        and the flow graph in ``flow``.\n\n    Raises\n    ------\n    TypeError:\n        if the input graph is not in CSR format.\n\n    ValueError:\n        if the capacity values are not integers, or the source or sink are out\n        of bounds.\n\n    Notes\n    -----\n    This solves the maximum flow problem on a given directed weighted graph:\n    A flow associates to every edge a value, also called a flow, less than the\n    capacity of the edge, so that for every vertex (apart from the source and\n    the sink vertices), the total incoming flow is equal to the total outgoing\n    flow. The value of a flow is the sum of the flow of all edges leaving the\n    source vertex, and the maximum flow problem consists of finding a flow\n    whose value is maximal.\n\n    By the max-flow min-cut theorem, the maximal value of the flow is also the\n    total weight of the edges in a minimum cut.\n\n    To solve the problem, we provide Edmonds--Karp [1]_ and Dinic's algorithm\n    [4]_. The implementation of both algorithms strive to exploit sparsity.\n    The time complexity of the former :math:`O(|V|\\,|E|^2)` and its space\n    complexity is :math:`O(|E|)`. The latter achieves its performance by\n    building level graphs and finding blocking flows in them. Its time\n    complexity is :math:`O(|V|^2\\,|E|)` and its space complexity is\n    :math:`O(|E|)`.\n\n    The maximum flow problem is usually defined with real valued capacities,\n    but we require that all capacities are integral to ensure convergence. When\n    dealing with rational capacities, or capacities belonging to\n    :math:`x\\mathbb{Q}` for some fixed :math:`x \\in \\mathbb{R}`, it is possible\n    to reduce the problem to the integral case by scaling all capacities\n    accordingly.\n\n    Solving a maximum-flow problem can be used for example for graph cuts\n    optimization in computer vision [3]_.\n\n    References\n    ----------\n    .. [1] Edmonds, J. and Karp, R. M.\n           Theoretical improvements in algorithmic efficiency for network flow\n           problems. 1972. Journal of the ACM. 19 (2): pp. 248-264\n    .. [2] Cormen, T. H. and Leiserson, C. E. and Rivest, R. L. and Stein C.\n           Introduction to Algorithms. Second Edition. 2001. MIT Press.\n    .. [3] https://en.wikipedia.org/wiki/Graph_cuts_in_computer_vision\n    .. [4] Dinic, Efim A.\n           Algorithm for solution of a problem of maximum flow in networks with\n           power estimation. In Soviet Math. Doklady, vol. 11, pp. 1277-1280.\n           1970.\n\n    Examples\n    --------\n    Perhaps the simplest flow problem is that of a graph of only two vertices\n    with an edge from source (0) to sink (1)::\n\n        (0) --5--> (1)\n\n    Here, the maximum flow is simply the capacity of the edge:\n\n    >>> import numpy as np\n    >>> from scipy.sparse import csr_matrix\n    >>> from scipy.sparse.csgraph import maximum_flow\n    >>> graph = csr_matrix([[0, 5], [0, 0]])\n    >>> maximum_flow(graph, 0, 1).flow_value\n    5\n    >>> maximum_flow(graph, 0, 1, method='edmonds_karp').flow_value\n    5\n\n    If, on the other hand, there is a bottleneck between source and sink, that\n    can reduce the maximum flow::\n\n        (0) --5--> (1) --3--> (2)\n\n    >>> graph = csr_matrix([[0, 5, 0], [0, 0, 3], [0, 0, 0]])\n    >>> maximum_flow(graph, 0, 2).flow_value\n    3\n\n    A less trivial example is given in [2]_, Chapter 26.1:\n\n    >>> graph = csr_matrix([[0, 16, 13,  0,  0,  0],\n    ...                     [0,  0, 10, 12,  0,  0],\n    ...                     [0,  4,  0,  0, 14,  0],\n    ...                     [0,  0,  9,  0,  0, 20],\n    ...                     [0,  0,  0,  7,  0,  4],\n    ...                     [0,  0,  0,  0,  0,  0]])\n    >>> maximum_flow(graph, 0, 5).flow_value\n    23\n\n    It is possible to reduce the problem of finding a maximum matching in a\n    bipartite graph to a maximum flow problem: Let :math:`G = ((U, V), E)` be a\n    bipartite graph. Then, add to the graph a source vertex with edges to every\n    vertex in :math:`U` and a sink vertex with edges from every vertex in\n    :math:`V`. Finally, give every edge in the resulting graph a capacity of 1.\n    Then, a maximum flow in the new graph gives a maximum matching in the\n    original graph consisting of the edges in :math:`E` whose flow is positive.\n\n    Assume that the edges are represented by a\n    :math:`\\lvert U \\rvert \\times \\lvert V \\rvert` matrix in CSR format whose\n    :math:`(i, j)`'th entry is 1 if there is an edge from :math:`i \\in U` to\n    :math:`j \\in V` and 0 otherwise; that is, the input is of the form required\n    by :func:`maximum_bipartite_matching`. Then the CSR representation of the\n    graph constructed above contains this matrix as a block. Here's an example:\n\n    >>> graph = csr_matrix([[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 1, 0]])\n    >>> print(graph.toarray())\n    [[0 1 0 1]\n     [1 0 1 0]\n     [0 1 1 0]]\n    >>> i, j = graph.shape\n    >>> n = graph.nnz\n    >>> indptr = np.concatenate([[0],\n    ...                          graph.indptr + i,\n    ...                          np.arange(n + i + 1, n + i + j + 1),\n    ...                          [n + i + j]])\n    >>> indices = np.concatenate([np.arange(1, i + 1),\n    ...                           graph.indices + i + 1,\n    ...                           np.repeat(i + j + 1, j)])\n    >>> data = np.ones(n + i + j, dtype=int)\n    >>>\n    >>> graph_flow = csr_matrix((data, indices, indptr))\n    >>> print(graph_flow.toarray())\n    [[0 1 1 1 0 0 0 0 0]\n     [0 0 0 0 0 1 0 1 0]\n     [0 0 0 0 1 0 1 0 0]\n     [0 0 0 0 0 1 1 0 0]\n     [0 0 0 0 0 0 0 0 1]\n     [0 0 0 0 0 0 0 0 1]\n     [0 0 0 0 0 0 0 0 1]\n     [0 0 0 0 0 0 0 0 1]\n     [0 0 0 0 0 0 0 0 0]]\n\n    At this point, we can find the maximum flow between the added sink and the\n    added source and the desired matching can be obtained by restricting the\n    flow function to the block corresponding to the original graph:\n\n    >>> result = maximum_flow(graph_flow, 0, i+j+1, method='dinic')\n    >>> matching = result.flow[1:i+1, i+1:i+j+1]\n    >>> print(matching.toarray())\n    [[0 1 0 0]\n     [1 0 0 0]\n     [0 0 1 0]]\n\n    This tells us that the first, second, and third vertex in :math:`U` are\n    matched with the second, first, and third vertex in :math:`V` respectively.\n\n    While this solves the maximum bipartite matching problem in general, note\n    that algorithms specialized to that problem, such as\n    :func:`maximum_bipartite_matching`, will generally perform better.\n\n    This approach can also be used to solve various common generalizations of\n    the maximum bipartite matching problem. If, for instance, some vertices can\n    be matched with more than one other vertex, this may be handled by\n    modifying the capacities of the new graph appropriately.\n\n    ",
}

