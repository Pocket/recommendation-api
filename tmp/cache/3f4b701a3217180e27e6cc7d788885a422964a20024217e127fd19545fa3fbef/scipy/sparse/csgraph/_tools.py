# encoding: utf-8
# module scipy.sparse.csgraph._tools
# from /.venv/lib/python3.8/site-packages/scipy/sparse/csgraph/_tools.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
""" Tools and utilities for working with compressed sparse graphs """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /.venv/lib/python3.8/site-packages/numpy/__init__.py
import numpy as __numpy
import scipy.sparse._compressed as __scipy_sparse__compressed


# functions

def construct_dist_matrix(graph, predecessors, directed=True, null_value=None): # real signature unknown; restored from __doc__
    """
    construct_dist_matrix(graph, predecessors, directed=True, null_value=np.inf)
    
        Construct distance matrix from a predecessor matrix
    
        .. versionadded:: 0.11.0
    
        Parameters
        ----------
        graph : array_like or sparse
            The N x N matrix representation of a directed or undirected graph.
            If dense, then non-edges are indicated by zeros or infinities.
        predecessors : array_like
            The N x N matrix of predecessors of each node (see Notes below).
        directed : bool, optional
            If True (default), then operate on a directed graph: only move from
            point i to point j along paths csgraph[i, j].
            If False, then operate on an undirected graph: the algorithm can
            progress from point i to j along csgraph[i, j] or csgraph[j, i].
        null_value : bool, optional
            value to use for distances between unconnected nodes.  Default is
            np.inf
    
        Returns
        -------
        dist_matrix : ndarray
            The N x N matrix of distances between nodes along the path specified
            by the predecessor matrix.  If no path exists, the distance is zero.
    
        Notes
        -----
        The predecessor matrix is of the form returned by
        `shortest_path`.  Row i of the predecessor matrix contains
        information on the shortest paths from point i: each entry
        predecessors[i, j] gives the index of the previous node in the path from
        point i to point j.  If no path exists between point i and j, then
        predecessors[i, j] = -9999
    
        Examples
        --------
        >>> import numpy as np
        >>> from scipy.sparse import csr_matrix
        >>> from scipy.sparse.csgraph import construct_dist_matrix
    
        >>> graph = [
        ... [0, 1, 2, 0],
        ... [0, 0, 0, 1],
        ... [0, 0, 0, 3],
        ... [0, 0, 0, 0]
        ... ]
        >>> graph = csr_matrix(graph)
        >>> print(graph)
          (0, 1)	1
          (0, 2)	2
          (1, 3)	1
          (2, 3)	3
    
        >>> pred = np.array([[-9999, 0, 0, 2],
        ...                  [1, -9999, 0, 1],
        ...                  [2, 0, -9999, 2],
        ...                  [1, 3, 3, -9999]], dtype=np.int32)
    
        >>> construct_dist_matrix(graph=graph, predecessors=pred, directed=False)
        array([[0., 1., 2., 5.],
               [1., 0., 3., 1.],
               [2., 3., 0., 3.],
               [2., 1., 3., 0.]])
    """
    pass

def csgraph_from_dense(graph, null_value=0, nan_null=True, infinity_null=True): # real signature unknown; restored from __doc__
    """
    csgraph_from_dense(graph, null_value=0, nan_null=True, infinity_null=True)
    
        Construct a CSR-format sparse graph from a dense matrix.
    
        .. versionadded:: 0.11.0
    
        Parameters
        ----------
        graph : array_like
            Input graph.  Shape should be (n_nodes, n_nodes).
        null_value : float or None (optional)
            Value that denotes non-edges in the graph.  Default is zero.
        infinity_null : bool
            If True (default), then infinite entries (both positive and negative)
            are treated as null edges.
        nan_null : bool
            If True (default), then NaN entries are treated as non-edges
    
        Returns
        -------
        csgraph : csr_matrix
            Compressed sparse representation of graph,
    
        Examples
        --------
        >>> from scipy.sparse.csgraph import csgraph_from_dense
    
        >>> graph = [
        ... [0, 1, 2, 0],
        ... [0, 0, 0, 1],
        ... [0, 0, 0, 3],
        ... [0, 0, 0, 0]
        ... ]
    
        >>> csgraph_from_dense(graph)
        <4x4 sparse matrix of type '<class 'numpy.float64'>'
            with 4 stored elements in Compressed Sparse Row format>
    """
    pass

def csgraph_from_masked(graph): # real signature unknown; restored from __doc__
    """
    csgraph_from_masked(graph)
    
        Construct a CSR-format graph from a masked array.
    
        .. versionadded:: 0.11.0
    
        Parameters
        ----------
        graph : MaskedArray
            Input graph.  Shape should be (n_nodes, n_nodes).
    
        Returns
        -------
        csgraph : csr_matrix
            Compressed sparse representation of graph,
    
        Examples
        --------
        >>> import numpy as np
        >>> from scipy.sparse.csgraph import csgraph_from_masked
    
        >>> graph_masked = np.ma.masked_array(data =[
        ... [0, 1, 2, 0],
        ... [0, 0, 0, 1],
        ... [0, 0, 0, 3],
        ... [0, 0, 0, 0]
        ... ],
        ... mask=[[ True, False, False,  True],
        ...       [ True,  True,  True, False],
        ...       [ True,  True,  True, False],
        ...       [ True,  True,  True,  True]],
        ... fill_value = 0)
    
        >>> csgraph_from_masked(graph_masked)
        <4x4 sparse matrix of type '<class 'numpy.float64'>'
            with 4 stored elements in Compressed Sparse Row format>
    """
    pass

def csgraph_masked_from_dense(graph, null_value=0, nan_null=True, infinity_null=True, copy=True): # real signature unknown; restored from __doc__
    """
    csgraph_masked_from_dense(graph, null_value=0, nan_null=True,
                                  infinity_null=True, copy=True)
    
        Construct a masked array graph representation from a dense matrix.
    
        .. versionadded:: 0.11.0
    
        Parameters
        ----------
        graph : array_like
            Input graph.  Shape should be (n_nodes, n_nodes).
        null_value : float or None (optional)
            Value that denotes non-edges in the graph.  Default is zero.
        infinity_null : bool
            If True (default), then infinite entries (both positive and negative)
            are treated as null edges.
        nan_null : bool
            If True (default), then NaN entries are treated as non-edges
    
        Returns
        -------
        csgraph : MaskedArray
            masked array representation of graph
    
        Examples
        --------
        >>> from scipy.sparse.csgraph import csgraph_masked_from_dense
    
        >>> graph = [
        ... [0, 1, 2, 0],
        ... [0, 0, 0, 1],
        ... [0, 0, 0, 3],
        ... [0, 0, 0, 0]
        ... ]
    
        >>> csgraph_masked_from_dense(graph)
        masked_array(
          data=[[--,  1,  2, --],
                [--, --, --,  1],
                [--, --, --,  3],
                [--, --, --, --]],
          mask=[[ True, False, False,  True],
                [ True,  True,  True, False],
                [ True,  True,  True, False],
                [ True,  True,  True,  True]],
          fill_value=0)
    """
    pass

def csgraph_to_dense(csgraph, null_value=0): # real signature unknown; restored from __doc__
    """
    csgraph_to_dense(csgraph, null_value=0)
    
        Convert a sparse graph representation to a dense representation
    
        .. versionadded:: 0.11.0
    
        Parameters
        ----------
        csgraph : csr_matrix, csc_matrix, or lil_matrix
            Sparse representation of a graph.
        null_value : float, optional
            The value used to indicate null edges in the dense representation.
            Default is 0.
    
        Returns
        -------
        graph : ndarray
            The dense representation of the sparse graph.
    
        Notes
        -----
        For normal sparse graph representations, calling csgraph_to_dense with
        null_value=0 produces an equivalent result to using dense format
        conversions in the main sparse package.  When the sparse representations
        have repeated values, however, the results will differ.  The tools in
        scipy.sparse will add repeating values to obtain a final value.  This
        function will select the minimum among repeating values to obtain a
        final value.  For example, here we'll create a two-node directed sparse
        graph with multiple edges from node 0 to node 1, of weights 2 and 3.
        This illustrates the difference in behavior:
    
        >>> from scipy.sparse import csr_matrix, csgraph
        >>> import numpy as np
        >>> data = np.array([2, 3])
        >>> indices = np.array([1, 1])
        >>> indptr = np.array([0, 2, 2])
        >>> M = csr_matrix((data, indices, indptr), shape=(2, 2))
        >>> M.toarray()
        array([[0, 5],
               [0, 0]])
        >>> csgraph.csgraph_to_dense(M)
        array([[0., 2.],
               [0., 0.]])
    
        The reason for this difference is to allow a compressed sparse graph to
        represent multiple edges between any two nodes.  As most sparse graph
        algorithms are concerned with the single lowest-cost edge between any
        two nodes, the default scipy.sparse behavior of summming multiple weights
        does not make sense in this context.
    
        The other reason for using this routine is to allow for graphs with
        zero-weight edges.  Let's look at the example of a two-node directed
        graph, connected by an edge of weight zero:
    
        >>> from scipy.sparse import csr_matrix, csgraph
        >>> data = np.array([0.0])
        >>> indices = np.array([1])
        >>> indptr = np.array([0, 1, 1])
        >>> M = csr_matrix((data, indices, indptr), shape=(2, 2))
        >>> M.toarray()
        array([[0, 0],
               [0, 0]])
        >>> csgraph.csgraph_to_dense(M, np.inf)
        array([[inf,  0.],
               [inf, inf]])
    
        In the first case, the zero-weight edge gets lost in the dense
        representation.  In the second case, we can choose a different null value
        and see the true form of the graph.
    
        Examples
        --------
        >>> from scipy.sparse import csr_matrix
        >>> from scipy.sparse.csgraph import csgraph_to_dense
    
        >>> graph = csr_matrix( [
        ... [0, 1, 2, 0],
        ... [0, 0, 0, 1],
        ... [0, 0, 0, 3],
        ... [0, 0, 0, 0]
        ... ])
        >>> graph
        <4x4 sparse matrix of type '<class 'numpy.int64'>'
            with 4 stored elements in Compressed Sparse Row format>
    
        >>> csgraph_to_dense(graph)
        array([[0., 1., 2., 0.],
               [0., 0., 0., 1.],
               [0., 0., 0., 3.],
               [0., 0., 0., 0.]])
    """
    pass

def csgraph_to_masked(csgraph): # real signature unknown; restored from __doc__
    """
    csgraph_to_masked(csgraph)
    
        Convert a sparse graph representation to a masked array representation
    
        .. versionadded:: 0.11.0
    
        Parameters
        ----------
        csgraph : csr_matrix, csc_matrix, or lil_matrix
            Sparse representation of a graph.
    
        Returns
        -------
        graph : MaskedArray
            The masked dense representation of the sparse graph.
    
        Examples
        --------
        >>> from scipy.sparse import csr_matrix
        >>> from scipy.sparse.csgraph import csgraph_to_masked
    
        >>> graph = csr_matrix( [
        ... [0, 1, 2, 0],
        ... [0, 0, 0, 1],
        ... [0, 0, 0, 3],
        ... [0, 0, 0, 0]
        ... ])
        >>> graph
        <4x4 sparse matrix of type '<class 'numpy.int64'>'
            with 4 stored elements in Compressed Sparse Row format>
    
        >>> csgraph_to_masked(graph)
        masked_array(
          data=[[ --, 1.0, 2.0,  --],
                [ --,  --,  --, 1.0],
                [ --,  --,  --, 3.0],
                [ --,  --,  --,  --]],
          mask=[[ True, False, False,  True],
                [ True,  True,  True, False],
                [ True,  True,  True, False],
                [ True,  True,  True,  True]],
          fill_value=1e+20)
    """
    pass

def isspmatrix(x): # reliably restored by inspect
    """
    Is x of a sparse matrix type?
    
        Parameters
        ----------
        x
            object to check for being a sparse matrix
    
        Returns
        -------
        bool
            True if x is a sparse matrix, False otherwise
    
        Notes
        -----
        issparse and isspmatrix are aliases for the same function.
    
        Examples
        --------
        >>> from scipy.sparse import csr_matrix, isspmatrix
        >>> isspmatrix(csr_matrix([[5]]))
        True
    
        >>> from scipy.sparse import isspmatrix
        >>> isspmatrix(5)
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

def isspmatrix_lil(x): # reliably restored by inspect
    """
    Is x of lil_matrix type?
    
        Parameters
        ----------
        x
            object to check for being a lil matrix
    
        Returns
        -------
        bool
            True if x is a lil matrix, False otherwise
    
        Examples
        --------
        >>> from scipy.sparse import lil_matrix, isspmatrix_lil
        >>> isspmatrix_lil(lil_matrix([[5]]))
        True
    
        >>> from scipy.sparse import lil_matrix, csr_matrix, isspmatrix_lil
        >>> isspmatrix_lil(csr_matrix([[5]]))
        False
    """
    pass

def reconstruct_path(csgraph, predecessors, directed=True): # real signature unknown; restored from __doc__
    """
    reconstruct_path(csgraph, predecessors, directed=True)
    
        Construct a tree from a graph and a predecessor list.
    
        .. versionadded:: 0.11.0
    
        Parameters
        ----------
        csgraph : array_like or sparse matrix
            The N x N matrix representing the directed or undirected graph
            from which the predecessors are drawn.
        predecessors : array_like, one dimension
            The length-N array of indices of predecessors for the tree.  The
            index of the parent of node i is given by predecessors[i].
        directed : bool, optional
            If True (default), then operate on a directed graph: only move from
            point i to point j along paths csgraph[i, j].
            If False, then operate on an undirected graph: the algorithm can
            progress from point i to j along csgraph[i, j] or csgraph[j, i].
    
        Returns
        -------
        cstree : csr matrix
            The N x N directed compressed-sparse representation of the tree drawn
            from csgraph which is encoded by the predecessor list.
    
        Examples
        --------
        >>> import numpy as np
        >>> from scipy.sparse import csr_matrix
        >>> from scipy.sparse.csgraph import reconstruct_path
    
        >>> graph = [
        ... [0, 1, 2, 0],
        ... [0, 0, 0, 1],
        ... [0, 0, 0, 3],
        ... [0, 0, 0, 0]
        ... ]
        >>> graph = csr_matrix(graph)
        >>> print(graph)
          (0, 1)	1
          (0, 2)	2
          (1, 3)	1
          (2, 3)	3
    
        >>> pred = np.array([-9999, 0, 0, 1], dtype=np.int32)
    
        >>> cstree = reconstruct_path(csgraph=graph, predecessors=pred, directed=False)
        >>> cstree.todense()
        matrix([[0., 1., 2., 0.],
                [0., 0., 0., 1.],
                [0., 0., 0., 0.],
                [0., 0., 0., 0.]])
    """
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


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff974bf3d0>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.sparse.csgraph._tools', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff974bf3d0>, origin='/.venv/lib/python3.8/site-packages/scipy/sparse/csgraph/_tools.cpython-38-aarch64-linux-gnu.so')"

__test__ = {
    'construct_dist_matrix (line 502)': '\n    construct_dist_matrix(graph, predecessors, directed=True, null_value=np.inf)\n\n    Construct distance matrix from a predecessor matrix\n\n    .. versionadded:: 0.11.0\n\n    Parameters\n    ----------\n    graph : array_like or sparse\n        The N x N matrix representation of a directed or undirected graph.\n        If dense, then non-edges are indicated by zeros or infinities.\n    predecessors : array_like\n        The N x N matrix of predecessors of each node (see Notes below).\n    directed : bool, optional\n        If True (default), then operate on a directed graph: only move from\n        point i to point j along paths csgraph[i, j].\n        If False, then operate on an undirected graph: the algorithm can\n        progress from point i to j along csgraph[i, j] or csgraph[j, i].\n    null_value : bool, optional\n        value to use for distances between unconnected nodes.  Default is\n        np.inf\n\n    Returns\n    -------\n    dist_matrix : ndarray\n        The N x N matrix of distances between nodes along the path specified\n        by the predecessor matrix.  If no path exists, the distance is zero.\n\n    Notes\n    -----\n    The predecessor matrix is of the form returned by\n    `shortest_path`.  Row i of the predecessor matrix contains\n    information on the shortest paths from point i: each entry\n    predecessors[i, j] gives the index of the previous node in the path from\n    point i to point j.  If no path exists between point i and j, then\n    predecessors[i, j] = -9999\n\n    Examples\n    --------\n    >>> import numpy as np\n    >>> from scipy.sparse import csr_matrix\n    >>> from scipy.sparse.csgraph import construct_dist_matrix\n\n    >>> graph = [\n    ... [0, 1, 2, 0],\n    ... [0, 0, 0, 1],\n    ... [0, 0, 0, 3],\n    ... [0, 0, 0, 0]\n    ... ]\n    >>> graph = csr_matrix(graph)\n    >>> print(graph)\n      (0, 1)\t1\n      (0, 2)\t2\n      (1, 3)\t1\n      (2, 3)\t3\n\n    >>> pred = np.array([[-9999, 0, 0, 2],\n    ...                  [1, -9999, 0, 1],\n    ...                  [2, 0, -9999, 2],\n    ...                  [1, 3, 3, -9999]], dtype=np.int32)\n\n    >>> construct_dist_matrix(graph=graph, predecessors=pred, directed=False)\n    array([[0., 1., 2., 5.],\n           [1., 0., 3., 1.],\n           [2., 3., 0., 3.],\n           [2., 1., 3., 0.]])\n\n    ',
    'csgraph_from_dense (line 172)': "\n    csgraph_from_dense(graph, null_value=0, nan_null=True, infinity_null=True)\n\n    Construct a CSR-format sparse graph from a dense matrix.\n\n    .. versionadded:: 0.11.0\n\n    Parameters\n    ----------\n    graph : array_like\n        Input graph.  Shape should be (n_nodes, n_nodes).\n    null_value : float or None (optional)\n        Value that denotes non-edges in the graph.  Default is zero.\n    infinity_null : bool\n        If True (default), then infinite entries (both positive and negative)\n        are treated as null edges.\n    nan_null : bool\n        If True (default), then NaN entries are treated as non-edges\n\n    Returns\n    -------\n    csgraph : csr_matrix\n        Compressed sparse representation of graph,\n\n    Examples\n    --------\n    >>> from scipy.sparse.csgraph import csgraph_from_dense\n\n    >>> graph = [\n    ... [0, 1, 2, 0],\n    ... [0, 0, 0, 1],\n    ... [0, 0, 0, 3],\n    ... [0, 0, 0, 0]\n    ... ]\n\n    >>> csgraph_from_dense(graph)\n    <4x4 sparse matrix of type '<class 'numpy.float64'>'\n        with 4 stored elements in Compressed Sparse Row format>\n\n    ",
    'csgraph_from_masked (line 18)': "\n    csgraph_from_masked(graph)\n\n    Construct a CSR-format graph from a masked array.\n\n    .. versionadded:: 0.11.0\n\n    Parameters\n    ----------\n    graph : MaskedArray\n        Input graph.  Shape should be (n_nodes, n_nodes).\n\n    Returns\n    -------\n    csgraph : csr_matrix\n        Compressed sparse representation of graph,\n\n    Examples\n    --------\n    >>> import numpy as np\n    >>> from scipy.sparse.csgraph import csgraph_from_masked\n\n    >>> graph_masked = np.ma.masked_array(data =[\n    ... [0, 1, 2, 0],\n    ... [0, 0, 0, 1],\n    ... [0, 0, 0, 3],\n    ... [0, 0, 0, 0]\n    ... ],\n    ... mask=[[ True, False, False,  True],\n    ...       [ True,  True,  True, False],\n    ...       [ True,  True,  True, False],\n    ...       [ True,  True,  True,  True]],\n    ... fill_value = 0)\n\n    >>> csgraph_from_masked(graph_masked)\n    <4x4 sparse matrix of type '<class 'numpy.float64'>'\n        with 4 stored elements in Compressed Sparse Row format>\n\n    ",
    'csgraph_masked_from_dense (line 83)': '\n    csgraph_masked_from_dense(graph, null_value=0, nan_null=True,\n                              infinity_null=True, copy=True)\n\n    Construct a masked array graph representation from a dense matrix.\n\n    .. versionadded:: 0.11.0\n\n    Parameters\n    ----------\n    graph : array_like\n        Input graph.  Shape should be (n_nodes, n_nodes).\n    null_value : float or None (optional)\n        Value that denotes non-edges in the graph.  Default is zero.\n    infinity_null : bool\n        If True (default), then infinite entries (both positive and negative)\n        are treated as null edges.\n    nan_null : bool\n        If True (default), then NaN entries are treated as non-edges\n\n    Returns\n    -------\n    csgraph : MaskedArray\n        masked array representation of graph\n\n    Examples\n    --------\n    >>> from scipy.sparse.csgraph import csgraph_masked_from_dense\n\n    >>> graph = [\n    ... [0, 1, 2, 0],\n    ... [0, 0, 0, 1],\n    ... [0, 0, 0, 3],\n    ... [0, 0, 0, 0]\n    ... ]\n\n    >>> csgraph_masked_from_dense(graph)\n    masked_array(\n      data=[[--,  1,  2, --],\n            [--, --, --,  1],\n            [--, --, --,  3],\n            [--, --, --, --]],\n      mask=[[ True, False, False,  True],\n            [ True,  True,  True, False],\n            [ True,  True,  True, False],\n            [ True,  True,  True,  True]],\n      fill_value=0)\n\n    ',
    'csgraph_to_dense (line 222)': "\n    csgraph_to_dense(csgraph, null_value=0)\n\n    Convert a sparse graph representation to a dense representation\n\n    .. versionadded:: 0.11.0\n\n    Parameters\n    ----------\n    csgraph : csr_matrix, csc_matrix, or lil_matrix\n        Sparse representation of a graph.\n    null_value : float, optional\n        The value used to indicate null edges in the dense representation.\n        Default is 0.\n\n    Returns\n    -------\n    graph : ndarray\n        The dense representation of the sparse graph.\n\n    Notes\n    -----\n    For normal sparse graph representations, calling csgraph_to_dense with\n    null_value=0 produces an equivalent result to using dense format\n    conversions in the main sparse package.  When the sparse representations\n    have repeated values, however, the results will differ.  The tools in\n    scipy.sparse will add repeating values to obtain a final value.  This\n    function will select the minimum among repeating values to obtain a\n    final value.  For example, here we'll create a two-node directed sparse\n    graph with multiple edges from node 0 to node 1, of weights 2 and 3.\n    This illustrates the difference in behavior:\n\n    >>> from scipy.sparse import csr_matrix, csgraph\n    >>> import numpy as np\n    >>> data = np.array([2, 3])\n    >>> indices = np.array([1, 1])\n    >>> indptr = np.array([0, 2, 2])\n    >>> M = csr_matrix((data, indices, indptr), shape=(2, 2))\n    >>> M.toarray()\n    array([[0, 5],\n           [0, 0]])\n    >>> csgraph.csgraph_to_dense(M)\n    array([[0., 2.],\n           [0., 0.]])\n\n    The reason for this difference is to allow a compressed sparse graph to\n    represent multiple edges between any two nodes.  As most sparse graph\n    algorithms are concerned with the single lowest-cost edge between any\n    two nodes, the default scipy.sparse behavior of summming multiple weights\n    does not make sense in this context.\n\n    The other reason for using this routine is to allow for graphs with\n    zero-weight edges.  Let's look at the example of a two-node directed\n    graph, connected by an edge of weight zero:\n\n    >>> from scipy.sparse import csr_matrix, csgraph\n    >>> data = np.array([0.0])\n    >>> indices = np.array([1])\n    >>> indptr = np.array([0, 1, 1])\n    >>> M = csr_matrix((data, indices, indptr), shape=(2, 2))\n    >>> M.toarray()\n    array([[0, 0],\n           [0, 0]])\n    >>> csgraph.csgraph_to_dense(M, np.inf)\n    array([[inf,  0.],\n           [inf, inf]])\n\n    In the first case, the zero-weight edge gets lost in the dense\n    representation.  In the second case, we can choose a different null value\n    and see the true form of the graph.\n\n    Examples\n    --------\n    >>> from scipy.sparse import csr_matrix\n    >>> from scipy.sparse.csgraph import csgraph_to_dense\n\n    >>> graph = csr_matrix( [\n    ... [0, 1, 2, 0],\n    ... [0, 0, 0, 1],\n    ... [0, 0, 0, 3],\n    ... [0, 0, 0, 0]\n    ... ])\n    >>> graph\n    <4x4 sparse matrix of type '<class 'numpy.int64'>'\n        with 4 stored elements in Compressed Sparse Row format>\n\n    >>> csgraph_to_dense(graph)\n    array([[0., 1., 2., 0.],\n           [0., 0., 0., 1.],\n           [0., 0., 0., 3.],\n           [0., 0., 0., 0.]])\n\n    ",
    'csgraph_to_masked (line 339)': "\n    csgraph_to_masked(csgraph)\n\n    Convert a sparse graph representation to a masked array representation\n\n    .. versionadded:: 0.11.0\n\n    Parameters\n    ----------\n    csgraph : csr_matrix, csc_matrix, or lil_matrix\n        Sparse representation of a graph.\n\n    Returns\n    -------\n    graph : MaskedArray\n        The masked dense representation of the sparse graph.\n\n    Examples\n    --------\n    >>> from scipy.sparse import csr_matrix\n    >>> from scipy.sparse.csgraph import csgraph_to_masked\n\n    >>> graph = csr_matrix( [\n    ... [0, 1, 2, 0],\n    ... [0, 0, 0, 1],\n    ... [0, 0, 0, 3],\n    ... [0, 0, 0, 0]\n    ... ])\n    >>> graph\n    <4x4 sparse matrix of type '<class 'numpy.int64'>'\n        with 4 stored elements in Compressed Sparse Row format>\n\n    >>> csgraph_to_masked(graph)\n    masked_array(\n      data=[[ --, 1.0, 2.0,  --],\n            [ --,  --,  --, 1.0],\n            [ --,  --,  --, 3.0],\n            [ --,  --,  --,  --]],\n      mask=[[ True, False, False,  True],\n            [ True,  True,  True, False],\n            [ True,  True,  True, False],\n            [ True,  True,  True,  True]],\n      fill_value=1e+20)\n\n    ",
    'reconstruct_path (line 413)': '\n    reconstruct_path(csgraph, predecessors, directed=True)\n\n    Construct a tree from a graph and a predecessor list.\n\n    .. versionadded:: 0.11.0\n\n    Parameters\n    ----------\n    csgraph : array_like or sparse matrix\n        The N x N matrix representing the directed or undirected graph\n        from which the predecessors are drawn.\n    predecessors : array_like, one dimension\n        The length-N array of indices of predecessors for the tree.  The\n        index of the parent of node i is given by predecessors[i].\n    directed : bool, optional\n        If True (default), then operate on a directed graph: only move from\n        point i to point j along paths csgraph[i, j].\n        If False, then operate on an undirected graph: the algorithm can\n        progress from point i to j along csgraph[i, j] or csgraph[j, i].\n\n    Returns\n    -------\n    cstree : csr matrix\n        The N x N directed compressed-sparse representation of the tree drawn\n        from csgraph which is encoded by the predecessor list.\n\n    Examples\n    --------\n    >>> import numpy as np\n    >>> from scipy.sparse import csr_matrix\n    >>> from scipy.sparse.csgraph import reconstruct_path\n\n    >>> graph = [\n    ... [0, 1, 2, 0],\n    ... [0, 0, 0, 1],\n    ... [0, 0, 0, 3],\n    ... [0, 0, 0, 0]\n    ... ]\n    >>> graph = csr_matrix(graph)\n    >>> print(graph)\n      (0, 1)\t1\n      (0, 2)\t2\n      (1, 3)\t1\n      (2, 3)\t3\n\n    >>> pred = np.array([-9999, 0, 0, 1], dtype=np.int32)\n\n    >>> cstree = reconstruct_path(csgraph=graph, predecessors=pred, directed=False)\n    >>> cstree.todense()\n    matrix([[0., 1., 2., 0.],\n            [0., 0., 0., 1.],\n            [0., 0., 0., 0.],\n            [0., 0., 0., 0.]])\n\n    ',
}

