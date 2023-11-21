# encoding: utf-8
# module scipy.spatial._ckdtree
# from /.venv/lib/python3.8/site-packages/scipy/spatial/_ckdtree.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /.venv/lib/python3.8/site-packages/numpy/__init__.py
import scipy as scipy # /.venv/lib/python3.8/site-packages/scipy/__init__.py
import os as os # /usr/local/lib/python3.8/os.py
import threading as threading # /usr/local/lib/python3.8/threading.py
import operator as operator # /usr/local/lib/python3.8/operator.py

# functions

def __pyx_unpickle_cKDTreeNode(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class cKDTree(object):
    """
    cKDTree(data, leafsize=16, compact_nodes=True, copy_data=False,
                balanced_tree=True, boxsize=None)
    
        kd-tree for quick nearest-neighbor lookup
    
        This class provides an index into a set of k-dimensional points
        which can be used to rapidly look up the nearest neighbors of any
        point.
    
        .. note::
           `cKDTree` is functionally identical to `KDTree`. Prior to SciPy
           v1.6.0, `cKDTree` had better performance and slightly different
           functionality but now the two names exist only for
           backward-compatibility reasons. If compatibility with SciPy < 1.6 is not
           a concern, prefer `KDTree`.
    
        Parameters
        ----------
        data : array_like, shape (n,m)
            The n data points of dimension m to be indexed. This array is
            not copied unless this is necessary to produce a contiguous
            array of doubles, and so modifying this data will result in
            bogus results. The data are also copied if the kd-tree is built
            with copy_data=True.
        leafsize : positive int, optional
            The number of points at which the algorithm switches over to
            brute-force. Default: 16.
        compact_nodes : bool, optional
            If True, the kd-tree is built to shrink the hyperrectangles to
            the actual data range. This usually gives a more compact tree that
            is robust against degenerated input data and gives faster queries
            at the expense of longer build time. Default: True.
        copy_data : bool, optional
            If True the data is always copied to protect the kd-tree against
            data corruption. Default: False.
        balanced_tree : bool, optional
            If True, the median is used to split the hyperrectangles instead of
            the midpoint. This usually gives a more compact tree and
            faster queries at the expense of longer build time. Default: True.
        boxsize : array_like or scalar, optional
            Apply a m-d toroidal topology to the KDTree.. The topology is generated
            by :math:`x_i + n_i L_i` where :math:`n_i` are integers and :math:`L_i`
            is the boxsize along i-th dimension. The input data shall be wrapped
            into :math:`[0, L_i)`. A ValueError is raised if any of the data is
            outside of this bound.
    
        Notes
        -----
        The algorithm used is described in Maneewongvatana and Mount 1999.
        The general idea is that the kd-tree is a binary tree, each of whose
        nodes represents an axis-aligned hyperrectangle. Each node specifies
        an axis and splits the set of points based on whether their coordinate
        along that axis is greater than or less than a particular value.
    
        During construction, the axis and splitting point are chosen by the
        "sliding midpoint" rule, which ensures that the cells do not all
        become long and thin.
    
        The tree can be queried for the r closest neighbors of any given point
        (optionally returning only those within some maximum distance of the
        point). It can also be queried, with a substantial gain in efficiency,
        for the r approximate closest neighbors.
    
        For large dimensions (20 is already large) do not expect this to run
        significantly faster than brute force. High-dimensional nearest-neighbor
        queries are a substantial open problem in computer science.
    
        Attributes
        ----------
        data : ndarray, shape (n,m)
            The n data points of dimension m to be indexed. This array is
            not copied unless this is necessary to produce a contiguous
            array of doubles. The data are also copied if the kd-tree is built
            with `copy_data=True`.
        leafsize : positive int
            The number of points at which the algorithm switches over to
            brute-force.
        m : int
            The dimension of a single data-point.
        n : int
            The number of data points.
        maxes : ndarray, shape (m,)
            The maximum value in each dimension of the n data points.
        mins : ndarray, shape (m,)
            The minimum value in each dimension of the n data points.
        tree : object, class cKDTreeNode
            This attribute exposes a Python view of the root node in the cKDTree
            object. A full Python view of the kd-tree is created dynamically
            on the first access. This attribute allows you to create your own
            query functions in Python.
        size : int
            The number of nodes in the tree.
    """
    def count_neighbors(self, other, r, p=2., weights=None, cumulative=True): # real signature unknown; restored from __doc__
        """
        count_neighbors(self, other, r, p=2., weights=None, cumulative=True)
        
                Count how many nearby pairs can be formed.
        
                Count the number of pairs ``(x1,x2)`` can be formed, with ``x1`` drawn
                from ``self`` and ``x2`` drawn from ``other``, and where
                ``distance(x1, x2, p) <= r``.
        
                Data points on ``self`` and ``other`` are optionally weighted by the
                ``weights`` argument. (See below)
        
                This is adapted from the "two-point correlation" algorithm described by
                Gray and Moore [1]_.  See notes for further discussion.
        
                Parameters
                ----------
                other : cKDTree instance
                    The other tree to draw points from, can be the same tree as self.
                r : float or one-dimensional array of floats
                    The radius to produce a count for. Multiple radii are searched with
                    a single tree traversal.
                    If the count is non-cumulative(``cumulative=False``), ``r`` defines
                    the edges of the bins, and must be non-decreasing.
                p : float, optional
                    1<=p<=infinity.
                    Which Minkowski p-norm to use.
                    Default 2.0.
                    A finite large p may cause a ValueError if overflow can occur.
                weights : tuple, array_like, or None, optional
                    If None, the pair-counting is unweighted.
                    If given as a tuple, weights[0] is the weights of points in ``self``, and
                    weights[1] is the weights of points in ``other``; either can be None to
                    indicate the points are unweighted.
                    If given as an array_like, weights is the weights of points in ``self``
                    and ``other``. For this to make sense, ``self`` and ``other`` must be the
                    same tree. If ``self`` and ``other`` are two different trees, a ``ValueError``
                    is raised.
                    Default: None
                cumulative : bool, optional
                    Whether the returned counts are cumulative. When cumulative is set to ``False``
                    the algorithm is optimized to work with a large number of bins (>10) specified
                    by ``r``. When ``cumulative`` is set to True, the algorithm is optimized to work
                    with a small number of ``r``. Default: True
        
                Returns
                -------
                result : scalar or 1-D array
                    The number of pairs. For unweighted counts, the result is integer.
                    For weighted counts, the result is float.
                    If cumulative is False, ``result[i]`` contains the counts with
                    ``(-inf if i == 0 else r[i-1]) < R <= r[i]``
        
                Notes
                -----
                Pair-counting is the basic operation used to calculate the two point
                correlation functions from a data set composed of position of objects.
        
                Two point correlation function measures the clustering of objects and
                is widely used in cosmology to quantify the large scale structure
                in our Universe, but it may be useful for data analysis in other fields
                where self-similar assembly of objects also occur.
        
                The Landy-Szalay estimator for the two point correlation function of
                ``D`` measures the clustering signal in ``D``. [2]_
        
                For example, given the position of two sets of objects,
        
                - objects ``D`` (data) contains the clustering signal, and
        
                - objects ``R`` (random) that contains no signal,
        
                .. math::
        
                     \xi(r) = \frac{<D, D> - 2 f <D, R> + f^2<R, R>}{f^2<R, R>},
        
                where the brackets represents counting pairs between two data sets
                in a finite bin around ``r`` (distance), corresponding to setting
                `cumulative=False`, and ``f = float(len(D)) / float(len(R))`` is the
                ratio between number of objects from data and random.
        
                The algorithm implemented here is loosely based on the dual-tree
                algorithm described in [1]_. We switch between two different
                pair-cumulation scheme depending on the setting of ``cumulative``.
                The computing time of the method we use when for
                ``cumulative == False`` does not scale with the total number of bins.
                The algorithm for ``cumulative == True`` scales linearly with the
                number of bins, though it is slightly faster when only
                1 or 2 bins are used. [5]_.
        
                As an extension to the naive pair-counting,
                weighted pair-counting counts the product of weights instead
                of number of pairs.
                Weighted pair-counting is used to estimate marked correlation functions
                ([3]_, section 2.2),
                or to properly calculate the average of data per distance bin
                (e.g. [4]_, section 2.1 on redshift).
        
                .. [1] Gray and Moore,
                       "N-body problems in statistical learning",
                       Mining the sky, 2000, :arxiv:`astro-ph/0012333`
        
                .. [2] Landy and Szalay,
                       "Bias and variance of angular correlation functions",
                       The Astrophysical Journal, 1993, :doi:`10.1086/172900`
        
                .. [3] Sheth, Connolly and Skibba,
                       "Marked correlations in galaxy formation models",
                       2005, :arxiv:`astro-ph/0511773`
        
                .. [4] Hawkins, et al.,
                       "The 2dF Galaxy Redshift Survey: correlation functions,
                       peculiar velocities and the matter density of the Universe",
                       Monthly Notices of the Royal Astronomical Society, 2002,
                       :doi:`10.1046/j.1365-2966.2003.07063.x`
        
                .. [5] https://github.com/scipy/scipy/pull/5647#issuecomment-168474926
        
                Examples
                --------
                You can count neighbors number between two kd-trees within a distance:
        
                >>> import numpy as np
                >>> from scipy.spatial import cKDTree
                >>> rng = np.random.default_rng()
                >>> points1 = rng.random((5, 2))
                >>> points2 = rng.random((5, 2))
                >>> kd_tree1 = cKDTree(points1)
                >>> kd_tree2 = cKDTree(points2)
                >>> kd_tree1.count_neighbors(kd_tree2, 0.2)
                1
        
                This number is same as the total pair number calculated by
                `query_ball_tree`:
        
                >>> indexes = kd_tree1.query_ball_tree(kd_tree2, r=0.2)
                >>> sum([len(i) for i in indexes])
                1
        """
        pass

    def query(self, x, k=1, eps=0, p=2, distance_upper_bound=None, workers=1): # real signature unknown; restored from __doc__
        """
        query(self, x, k=1, eps=0, p=2, distance_upper_bound=np.inf, workers=1)
        
                Query the kd-tree for nearest neighbors
        
                Parameters
                ----------
                x : array_like, last dimension self.m
                    An array of points to query.
                k : list of integer or integer
                    The list of k-th nearest neighbors to return. If k is an
                    integer it is treated as a list of [1, ... k] (range(1, k+1)).
                    Note that the counting starts from 1.
                eps : non-negative float
                    Return approximate nearest neighbors; the k-th returned value
                    is guaranteed to be no further than (1+eps) times the
                    distance to the real k-th nearest neighbor.
                p : float, 1<=p<=infinity
                    Which Minkowski p-norm to use.
                    1 is the sum-of-absolute-values "Manhattan" distance
                    2 is the usual Euclidean distance
                    infinity is the maximum-coordinate-difference distance
                    A finite large p may cause a ValueError if overflow can occur.
                distance_upper_bound : nonnegative float
                    Return only neighbors within this distance.  This is used to prune
                    tree searches, so if you are doing a series of nearest-neighbor
                    queries, it may help to supply the distance to the nearest neighbor
                    of the most recent point.
                workers : int, optional
                    Number of workers to use for parallel processing. If -1 is given
                    all CPU threads are used. Default: 1.
        
                    .. versionchanged:: 1.9.0
                       The "n_jobs" argument was renamed "workers". The old name
                       "n_jobs" was deprecated in SciPy 1.6.0 and was removed in
                       SciPy 1.9.0.
        
                Returns
                -------
                d : array of floats
                    The distances to the nearest neighbors.
                    If ``x`` has shape ``tuple+(self.m,)``, then ``d`` has shape ``tuple+(k,)``.
                    When k == 1, the last dimension of the output is squeezed.
                    Missing neighbors are indicated with infinite distances.
                i : ndarray of ints
                    The index of each neighbor in ``self.data``.
                    If ``x`` has shape ``tuple+(self.m,)``, then ``i`` has shape ``tuple+(k,)``.
                    When k == 1, the last dimension of the output is squeezed.
                    Missing neighbors are indicated with ``self.n``.
        
                Notes
                -----
                If the KD-Tree is periodic, the position ``x`` is wrapped into the
                box.
        
                When the input k is a list, a query for arange(max(k)) is performed, but
                only columns that store the requested values of k are preserved. This is
                implemented in a manner that reduces memory usage.
        
                Examples
                --------
        
                >>> import numpy as np
                >>> from scipy.spatial import cKDTree
                >>> x, y = np.mgrid[0:5, 2:8]
                >>> tree = cKDTree(np.c_[x.ravel(), y.ravel()])
        
                To query the nearest neighbours and return squeezed result, use
        
                >>> dd, ii = tree.query([[0, 0], [2.2, 2.9]], k=1)
                >>> print(dd, ii, sep='\n')
                [2.         0.2236068]
                [ 0 13]
        
                To query the nearest neighbours and return unsqueezed result, use
        
                >>> dd, ii = tree.query([[0, 0], [2.2, 2.9]], k=[1])
                >>> print(dd, ii, sep='\n')
                [[2.        ]
                 [0.2236068]]
                [[ 0]
                 [13]]
        
                To query the second nearest neighbours and return unsqueezed result,
                use
        
                >>> dd, ii = tree.query([[0, 0], [2.2, 2.9]], k=[2])
                >>> print(dd, ii, sep='\n')
                [[2.23606798]
                 [0.80622577]]
                [[ 6]
                 [19]]
        
                To query the first and second nearest neighbours, use
        
                >>> dd, ii = tree.query([[0, 0], [2.2, 2.9]], k=2)
                >>> print(dd, ii, sep='\n')
                [[2.         2.23606798]
                 [0.2236068  0.80622577]]
                [[ 0  6]
                 [13 19]]
        
                or, be more specific
        
                >>> dd, ii = tree.query([[0, 0], [2.2, 2.9]], k=[1, 2])
                >>> print(dd, ii, sep='\n')
                [[2.         2.23606798]
                 [0.2236068  0.80622577]]
                [[ 0  6]
                 [13 19]]
        """
        pass

    def query_ball_point(self, x, r, p=2., eps=0, workers=1, return_sorted=None, return_length=False): # real signature unknown; restored from __doc__
        """
        query_ball_point(self, x, r, p=2., eps=0, workers=1, return_sorted=None,
                                 return_length=False)
        
                Find all points within distance r of point(s) x.
        
                Parameters
                ----------
                x : array_like, shape tuple + (self.m,)
                    The point or points to search for neighbors of.
                r : array_like, float
                    The radius of points to return, shall broadcast to the length of x.
                p : float, optional
                    Which Minkowski p-norm to use.  Should be in the range [1, inf].
                    A finite large p may cause a ValueError if overflow can occur.
                eps : nonnegative float, optional
                    Approximate search. Branches of the tree are not explored if their
                    nearest points are further than ``r / (1 + eps)``, and branches are
                    added in bulk if their furthest points are nearer than
                    ``r * (1 + eps)``.
                workers : int, optional
                    Number of jobs to schedule for parallel processing. If -1 is given
                    all processors are used. Default: 1.
        
                    .. versionchanged:: 1.9.0
                       The "n_jobs" argument was renamed "workers". The old name
                       "n_jobs" was deprecated in SciPy 1.6.0 and was removed in
                       SciPy 1.9.0.
        
                return_sorted : bool, optional
                    Sorts returned indicies if True and does not sort them if False. If
                    None, does not sort single point queries, but does sort
                    multi-point queries which was the behavior before this option
                    was added.
        
                    .. versionadded:: 1.2.0
                return_length: bool, optional
                    Return the number of points inside the radius instead of a list
                    of the indices.
                    .. versionadded:: 1.3.0
        
                Returns
                -------
                results : list or array of lists
                    If `x` is a single point, returns a list of the indices of the
                    neighbors of `x`. If `x` is an array of points, returns an object
                    array of shape tuple containing lists of neighbors.
        
                Notes
                -----
                If you have many points whose neighbors you want to find, you may save
                substantial amounts of time by putting them in a cKDTree and using
                query_ball_tree.
        
                Examples
                --------
                >>> import numpy as np
                >>> from scipy import spatial
                >>> x, y = np.mgrid[0:4, 0:4]
                >>> points = np.c_[x.ravel(), y.ravel()]
                >>> tree = spatial.cKDTree(points)
                >>> tree.query_ball_point([2, 0], 1)
                [4, 8, 9, 12]
        
                Query multiple points and plot the results:
        
                >>> import matplotlib.pyplot as plt
                >>> points = np.asarray(points)
                >>> plt.plot(points[:,0], points[:,1], '.')
                >>> for results in tree.query_ball_point(([2, 0], [3, 3]), 1):
                ...     nearby_points = points[results]
                ...     plt.plot(nearby_points[:,0], nearby_points[:,1], 'o')
                >>> plt.margins(0.1, 0.1)
                >>> plt.show()
        """
        pass

    def query_ball_tree(self, other, r, p=2., eps=0): # real signature unknown; restored from __doc__
        """
        query_ball_tree(self, other, r, p=2., eps=0)
        
                Find all pairs of points between `self` and `other` whose distance is at most r
        
                Parameters
                ----------
                other : cKDTree instance
                    The tree containing points to search against.
                r : float
                    The maximum distance, has to be positive.
                p : float, optional
                    Which Minkowski norm to use.  `p` has to meet the condition
                    ``1 <= p <= infinity``.
                    A finite large p may cause a ValueError if overflow can occur.
                eps : float, optional
                    Approximate search.  Branches of the tree are not explored
                    if their nearest points are further than ``r/(1+eps)``, and
                    branches are added in bulk if their furthest points are nearer
                    than ``r * (1+eps)``.  `eps` has to be non-negative.
        
                Returns
                -------
                results : list of lists
                    For each element ``self.data[i]`` of this tree, ``results[i]`` is a
                    list of the indices of its neighbors in ``other.data``.
        
                Examples
                --------
                You can search all pairs of points between two kd-trees within a distance:
        
                >>> import matplotlib.pyplot as plt
                >>> import numpy as np
                >>> from scipy.spatial import cKDTree
                >>> rng = np.random.default_rng()
                >>> points1 = rng.random((15, 2))
                >>> points2 = rng.random((15, 2))
                >>> plt.figure(figsize=(6, 6))
                >>> plt.plot(points1[:, 0], points1[:, 1], "xk", markersize=14)
                >>> plt.plot(points2[:, 0], points2[:, 1], "og", markersize=14)
                >>> kd_tree1 = cKDTree(points1)
                >>> kd_tree2 = cKDTree(points2)
                >>> indexes = kd_tree1.query_ball_tree(kd_tree2, r=0.2)
                >>> for i in range(len(indexes)):
                ...     for j in indexes[i]:
                ...         plt.plot([points1[i, 0], points2[j, 0]],
                ...             [points1[i, 1], points2[j, 1]], "-r")
                >>> plt.show()
        """
        pass

    def query_pairs(self, r, p=2., eps=0): # real signature unknown; restored from __doc__
        """
        query_pairs(self, r, p=2., eps=0)
        
                Find all pairs of points in `self` whose distance is at most r.
        
                Parameters
                ----------
                r : positive float
                    The maximum distance.
                p : float, optional
                    Which Minkowski norm to use.  ``p`` has to meet the condition
                    ``1 <= p <= infinity``.
                    A finite large p may cause a ValueError if overflow can occur.
                eps : float, optional
                    Approximate search.  Branches of the tree are not explored
                    if their nearest points are further than ``r/(1+eps)``, and
                    branches are added in bulk if their furthest points are nearer
                    than ``r * (1+eps)``.  `eps` has to be non-negative.
                output_type : string, optional
                    Choose the output container, 'set' or 'ndarray'. Default: 'set'
        
                Returns
                -------
                results : set or ndarray
                    Set of pairs ``(i,j)``, with ``i < j``, for which the corresponding
                    positions are close. If output_type is 'ndarray', an ndarry is
                    returned instead of a set.
        
                Examples
                --------
                You can search all pairs of points in a kd-tree within a distance:
        
                >>> import matplotlib.pyplot as plt
                >>> import numpy as np
                >>> from scipy.spatial import cKDTree
                >>> rng = np.random.default_rng()
                >>> points = rng.random((20, 2))
                >>> plt.figure(figsize=(6, 6))
                >>> plt.plot(points[:, 0], points[:, 1], "xk", markersize=14)
                >>> kd_tree = cKDTree(points)
                >>> pairs = kd_tree.query_pairs(r=0.2)
                >>> for (i, j) in pairs:
                ...     plt.plot([points[i, 0], points[j, 0]],
                ...             [points[i, 1], points[j, 1]], "-r")
                >>> plt.show()
        """
        pass

    def sparse_distance_matrix(self, other, max_distance, p=2.): # real signature unknown; restored from __doc__
        """
        sparse_distance_matrix(self, other, max_distance, p=2.)
        
                Compute a sparse distance matrix
        
                Computes a distance matrix between two cKDTrees, leaving as zero
                any distance greater than max_distance.
        
                Parameters
                ----------
                other : cKDTree
        
                max_distance : positive float
        
                p : float, 1<=p<=infinity
                    Which Minkowski p-norm to use.
                    A finite large p may cause a ValueError if overflow can occur.
        
                output_type : string, optional
                    Which container to use for output data. Options: 'dok_matrix',
                    'coo_matrix', 'dict', or 'ndarray'. Default: 'dok_matrix'.
        
                Returns
                -------
                result : dok_matrix, coo_matrix, dict or ndarray
                    Sparse matrix representing the results in "dictionary of keys"
                    format. If a dict is returned the keys are (i,j) tuples of indices.
                    If output_type is 'ndarray' a record array with fields 'i', 'j',
                    and 'v' is returned,
        
                Examples
                --------
                You can compute a sparse distance matrix between two kd-trees:
        
                >>> import numpy as np
                >>> from scipy.spatial import cKDTree
                >>> rng = np.random.default_rng()
                >>> points1 = rng.random((5, 2))
                >>> points2 = rng.random((5, 2))
                >>> kd_tree1 = cKDTree(points1)
                >>> kd_tree2 = cKDTree(points2)
                >>> sdm = kd_tree1.sparse_distance_matrix(kd_tree2, 0.3)
                >>> sdm.toarray()
                array([[0.        , 0.        , 0.12295571, 0.        , 0.        ],
                   [0.        , 0.        , 0.        , 0.        , 0.        ],
                   [0.28942611, 0.        , 0.        , 0.2333084 , 0.        ],
                   [0.        , 0.        , 0.        , 0.        , 0.        ],
                   [0.24617575, 0.29571802, 0.26836782, 0.        , 0.        ]])
        
                You can check distances above the `max_distance` are zeros:
        
                >>> from scipy.spatial import distance_matrix
                >>> distance_matrix(points1, points2)
                array([[0.56906522, 0.39923701, 0.12295571, 0.8658745 , 0.79428925],
                   [0.37327919, 0.7225693 , 0.87665969, 0.32580855, 0.75679479],
                   [0.28942611, 0.30088013, 0.6395831 , 0.2333084 , 0.33630734],
                   [0.31994999, 0.72658602, 0.71124834, 0.55396483, 0.90785663],
                   [0.24617575, 0.29571802, 0.26836782, 0.57714465, 0.6473269 ]])
        """
        pass

    def _build_weights(self, weights): # real signature unknown; restored from __doc__
        """
        _build_weights(weights)
        
                Compute weights of nodes from weights of data points. This will sum
                up the total weight per node. This function is used internally.
        
                Parameters
                ----------
                weights : array_like
                    weights of data points; must be the same length as the data points.
                    currently only scalar weights are supported. Therefore the weights
                    array must be 1 dimensional.
        
                Returns
                -------
                node_weights : array_like
                    total weight for each KD-Tree node.
        """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, data, leafsize=16, compact_nodes=True, copy_data=False, balanced_tree=True, boxsize=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    boxsize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    indices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leafsize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    m = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    maxes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mins = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tree = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0xffff9f88adb0>'


class cKDTreeNode(object):
    """
    class cKDTreeNode
    
        This class exposes a Python view of a node in the cKDTree object.
    
        All attributes are read-only.
    
        Attributes
        ----------
        level : int
            The depth of the node. 0 is the level of the root node.
        split_dim : int
            The dimension along which this node is split. If this value is -1
            the node is a leafnode in the kd-tree. Leafnodes are not split further
            and scanned by brute force.
        split : float
            The value used to separate split this node. Points with value >= split
            in the split_dim dimension are sorted to the 'greater' subnode
            whereas those with value < split are sorted to the 'lesser' subnode.
        children : int
            The number of data points sorted to this node.
        data_points : ndarray of float64
            An array with the data points sorted to this node.
        indices : ndarray of intp
            An array with the indices of the data points sorted to this node. The
            indices refer to the position in the data set used to construct the
            kd-tree.
        lesser : cKDTreeNode or None
            Subnode with the 'lesser' data points. This attribute is None for
            leafnodes.
        greater : cKDTreeNode or None
            Subnode with the 'greater' data points. This attribute is None for
            leafnodes.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    data_points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    end_idx = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    greater = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    indices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lesser = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    split = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    split_dim = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    start_idx = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0xffff9f88ad50>'


class coo_entries(object):
    # no doc
    def coo_matrix(self, *args, **kwargs): # real signature unknown
        pass

    def dict(self, *args, **kwargs): # real signature unknown
        pass

    def dok_matrix(self, *args, **kwargs): # real signature unknown
        pass

    def ndarray(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __array_interface__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class ordered_pairs(object):
    # no doc
    def ndarray(self, *args, **kwargs): # real signature unknown
        pass

    def set(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __array_interface__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

__all__ = [
    'cKDTree',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9f88a490>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.spatial._ckdtree', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9f88a490>, origin='/.venv/lib/python3.8/site-packages/scipy/spatial/_ckdtree.cpython-38-aarch64-linux-gnu.so')"

__test__ = {
    'cKDTree.count_neighbors (line 1195)': '\n        count_neighbors(self, other, r, p=2., weights=None, cumulative=True)\n\n        Count how many nearby pairs can be formed.\n\n        Count the number of pairs ``(x1,x2)`` can be formed, with ``x1`` drawn\n        from ``self`` and ``x2`` drawn from ``other``, and where\n        ``distance(x1, x2, p) <= r``.\n\n        Data points on ``self`` and ``other`` are optionally weighted by the\n        ``weights`` argument. (See below)\n\n        This is adapted from the "two-point correlation" algorithm described by\n        Gray and Moore [1]_.  See notes for further discussion.\n\n        Parameters\n        ----------\n        other : cKDTree instance\n            The other tree to draw points from, can be the same tree as self.\n        r : float or one-dimensional array of floats\n            The radius to produce a count for. Multiple radii are searched with\n            a single tree traversal.\n            If the count is non-cumulative(``cumulative=False``), ``r`` defines\n            the edges of the bins, and must be non-decreasing.\n        p : float, optional\n            1<=p<=infinity.\n            Which Minkowski p-norm to use.\n            Default 2.0.\n            A finite large p may cause a ValueError if overflow can occur.\n        weights : tuple, array_like, or None, optional\n            If None, the pair-counting is unweighted.\n            If given as a tuple, weights[0] is the weights of points in ``self``, and\n            weights[1] is the weights of points in ``other``; either can be None to\n            indicate the points are unweighted.\n            If given as an array_like, weights is the weights of points in ``self``\n            and ``other``. For this to make sense, ``self`` and ``other`` must be the\n            same tree. If ``self`` and ``other`` are two different trees, a ``ValueError``\n            is raised.\n            Default: None\n        cumulative : bool, optional\n            Whether the returned counts are cumulative. When cumulative is set to ``False``\n            the algorithm is optimized to work with a large number of bins (>10) specified\n            by ``r``. When ``cumulative`` is set to True, the algorithm is optimized to work\n            with a small number of ``r``. Default: True\n\n        Returns\n        -------\n        result : scalar or 1-D array\n            The number of pairs. For unweighted counts, the result is integer.\n            For weighted counts, the result is float.\n            If cumulative is False, ``result[i]`` contains the counts with\n            ``(-inf if i == 0 else r[i-1]) < R <= r[i]``\n\n        Notes\n        -----\n        Pair-counting is the basic operation used to calculate the two point\n        correlation functions from a data set composed of position of objects.\n\n        Two point correlation function measures the clustering of objects and\n        is widely used in cosmology to quantify the large scale structure\n        in our Universe, but it may be useful for data analysis in other fields\n        where self-similar assembly of objects also occur.\n\n        The Landy-Szalay estimator for the two point correlation function of\n        ``D`` measures the clustering signal in ``D``. [2]_\n\n        For example, given the position of two sets of objects,\n\n        - objects ``D`` (data) contains the clustering signal, and\n\n        - objects ``R`` (random) that contains no signal,\n\n        .. math::\n\n             \\xi(r) = \\frac{<D, D> - 2 f <D, R> + f^2<R, R>}{f^2<R, R>},\n\n        where the brackets represents counting pairs between two data sets\n        in a finite bin around ``r`` (distance), corresponding to setting\n        `cumulative=False`, and ``f = float(len(D)) / float(len(R))`` is the\n        ratio between number of objects from data and random.\n\n        The algorithm implemented here is loosely based on the dual-tree\n        algorithm described in [1]_. We switch between two different\n        pair-cumulation scheme depending on the setting of ``cumulative``.\n        The computing time of the method we use when for\n        ``cumulative == False`` does not scale with the total number of bins.\n        The algorithm for ``cumulative == True`` scales linearly with the\n        number of bins, though it is slightly faster when only\n        1 or 2 bins are used. [5]_.\n\n        As an extension to the naive pair-counting,\n        weighted pair-counting counts the product of weights instead\n        of number of pairs.\n        Weighted pair-counting is used to estimate marked correlation functions\n        ([3]_, section 2.2),\n        or to properly calculate the average of data per distance bin\n        (e.g. [4]_, section 2.1 on redshift).\n\n        .. [1] Gray and Moore,\n               "N-body problems in statistical learning",\n               Mining the sky, 2000, :arxiv:`astro-ph/0012333`\n\n        .. [2] Landy and Szalay,\n               "Bias and variance of angular correlation functions",\n               The Astrophysical Journal, 1993, :doi:`10.1086/172900`\n\n        .. [3] Sheth, Connolly and Skibba,\n               "Marked correlations in galaxy formation models",\n               2005, :arxiv:`astro-ph/0511773`\n\n        .. [4] Hawkins, et al.,\n               "The 2dF Galaxy Redshift Survey: correlation functions,\n               peculiar velocities and the matter density of the Universe",\n               Monthly Notices of the Royal Astronomical Society, 2002,\n               :doi:`10.1046/j.1365-2966.2003.07063.x`\n\n        .. [5] https://github.com/scipy/scipy/pull/5647#issuecomment-168474926\n\n        Examples\n        --------\n        You can count neighbors number between two kd-trees within a distance:\n\n        >>> import numpy as np\n        >>> from scipy.spatial import cKDTree\n        >>> rng = np.random.default_rng()\n        >>> points1 = rng.random((5, 2))\n        >>> points2 = rng.random((5, 2))\n        >>> kd_tree1 = cKDTree(points1)\n        >>> kd_tree2 = cKDTree(points2)\n        >>> kd_tree1.count_neighbors(kd_tree2, 0.2)\n        1\n\n        This number is same as the total pair number calculated by\n        `query_ball_tree`:\n\n        >>> indexes = kd_tree1.query_ball_tree(kd_tree2, r=0.2)\n        >>> sum([len(i) for i in indexes])\n        1\n\n        ',
    'cKDTree.query (line 661)': '\n        query(self, x, k=1, eps=0, p=2, distance_upper_bound=np.inf, workers=1)\n\n        Query the kd-tree for nearest neighbors\n\n        Parameters\n        ----------\n        x : array_like, last dimension self.m\n            An array of points to query.\n        k : list of integer or integer\n            The list of k-th nearest neighbors to return. If k is an\n            integer it is treated as a list of [1, ... k] (range(1, k+1)).\n            Note that the counting starts from 1.\n        eps : non-negative float\n            Return approximate nearest neighbors; the k-th returned value\n            is guaranteed to be no further than (1+eps) times the\n            distance to the real k-th nearest neighbor.\n        p : float, 1<=p<=infinity\n            Which Minkowski p-norm to use.\n            1 is the sum-of-absolute-values "Manhattan" distance\n            2 is the usual Euclidean distance\n            infinity is the maximum-coordinate-difference distance\n            A finite large p may cause a ValueError if overflow can occur.\n        distance_upper_bound : nonnegative float\n            Return only neighbors within this distance.  This is used to prune\n            tree searches, so if you are doing a series of nearest-neighbor\n            queries, it may help to supply the distance to the nearest neighbor\n            of the most recent point.\n        workers : int, optional\n            Number of workers to use for parallel processing. If -1 is given\n            all CPU threads are used. Default: 1.\n\n            .. versionchanged:: 1.9.0\n               The "n_jobs" argument was renamed "workers". The old name\n               "n_jobs" was deprecated in SciPy 1.6.0 and was removed in\n               SciPy 1.9.0.\n\n        Returns\n        -------\n        d : array of floats\n            The distances to the nearest neighbors.\n            If ``x`` has shape ``tuple+(self.m,)``, then ``d`` has shape ``tuple+(k,)``.\n            When k == 1, the last dimension of the output is squeezed.\n            Missing neighbors are indicated with infinite distances.\n        i : ndarray of ints\n            The index of each neighbor in ``self.data``.\n            If ``x`` has shape ``tuple+(self.m,)``, then ``i`` has shape ``tuple+(k,)``.\n            When k == 1, the last dimension of the output is squeezed.\n            Missing neighbors are indicated with ``self.n``.\n\n        Notes\n        -----\n        If the KD-Tree is periodic, the position ``x`` is wrapped into the\n        box.\n\n        When the input k is a list, a query for arange(max(k)) is performed, but\n        only columns that store the requested values of k are preserved. This is\n        implemented in a manner that reduces memory usage.\n\n        Examples\n        --------\n\n        >>> import numpy as np\n        >>> from scipy.spatial import cKDTree\n        >>> x, y = np.mgrid[0:5, 2:8]\n        >>> tree = cKDTree(np.c_[x.ravel(), y.ravel()])\n\n        To query the nearest neighbours and return squeezed result, use\n\n        >>> dd, ii = tree.query([[0, 0], [2.2, 2.9]], k=1)\n        >>> print(dd, ii, sep=\'\\n\')\n        [2.         0.2236068]\n        [ 0 13]\n\n        To query the nearest neighbours and return unsqueezed result, use\n\n        >>> dd, ii = tree.query([[0, 0], [2.2, 2.9]], k=[1])\n        >>> print(dd, ii, sep=\'\\n\')\n        [[2.        ]\n         [0.2236068]]\n        [[ 0]\n         [13]]\n\n        To query the second nearest neighbours and return unsqueezed result,\n        use\n\n        >>> dd, ii = tree.query([[0, 0], [2.2, 2.9]], k=[2])\n        >>> print(dd, ii, sep=\'\\n\')\n        [[2.23606798]\n         [0.80622577]]\n        [[ 6]\n         [19]]\n\n        To query the first and second nearest neighbours, use\n\n        >>> dd, ii = tree.query([[0, 0], [2.2, 2.9]], k=2)\n        >>> print(dd, ii, sep=\'\\n\')\n        [[2.         2.23606798]\n         [0.2236068  0.80622577]]\n        [[ 0  6]\n         [13 19]]\n\n        or, be more specific\n\n        >>> dd, ii = tree.query([[0, 0], [2.2, 2.9]], k=[1, 2])\n        >>> print(dd, ii, sep=\'\\n\')\n        [[2.         2.23606798]\n         [0.2236068  0.80622577]]\n        [[ 0  6]\n         [13 19]]\n\n        ',
    'cKDTree.query_ball_point (line 841)': '\n        query_ball_point(self, x, r, p=2., eps=0, workers=1, return_sorted=None,\n                         return_length=False)\n\n        Find all points within distance r of point(s) x.\n\n        Parameters\n        ----------\n        x : array_like, shape tuple + (self.m,)\n            The point or points to search for neighbors of.\n        r : array_like, float\n            The radius of points to return, shall broadcast to the length of x.\n        p : float, optional\n            Which Minkowski p-norm to use.  Should be in the range [1, inf].\n            A finite large p may cause a ValueError if overflow can occur.\n        eps : nonnegative float, optional\n            Approximate search. Branches of the tree are not explored if their\n            nearest points are further than ``r / (1 + eps)``, and branches are\n            added in bulk if their furthest points are nearer than\n            ``r * (1 + eps)``.\n        workers : int, optional\n            Number of jobs to schedule for parallel processing. If -1 is given\n            all processors are used. Default: 1.\n\n            .. versionchanged:: 1.9.0\n               The "n_jobs" argument was renamed "workers". The old name\n               "n_jobs" was deprecated in SciPy 1.6.0 and was removed in\n               SciPy 1.9.0.\n\n        return_sorted : bool, optional\n            Sorts returned indicies if True and does not sort them if False. If\n            None, does not sort single point queries, but does sort\n            multi-point queries which was the behavior before this option\n            was added.\n\n            .. versionadded:: 1.2.0\n        return_length: bool, optional\n            Return the number of points inside the radius instead of a list\n            of the indices.\n            .. versionadded:: 1.3.0\n\n        Returns\n        -------\n        results : list or array of lists\n            If `x` is a single point, returns a list of the indices of the\n            neighbors of `x`. If `x` is an array of points, returns an object\n            array of shape tuple containing lists of neighbors.\n\n        Notes\n        -----\n        If you have many points whose neighbors you want to find, you may save\n        substantial amounts of time by putting them in a cKDTree and using\n        query_ball_tree.\n\n        Examples\n        --------\n        >>> import numpy as np\n        >>> from scipy import spatial\n        >>> x, y = np.mgrid[0:4, 0:4]\n        >>> points = np.c_[x.ravel(), y.ravel()]\n        >>> tree = spatial.cKDTree(points)\n        >>> tree.query_ball_point([2, 0], 1)\n        [4, 8, 9, 12]\n\n        Query multiple points and plot the results:\n\n        >>> import matplotlib.pyplot as plt\n        >>> points = np.asarray(points)\n        >>> plt.plot(points[:,0], points[:,1], \'.\')\n        >>> for results in tree.query_ball_point(([2, 0], [3, 3]), 1):\n        ...     nearby_points = points[results]\n        ...     plt.plot(nearby_points[:,0], nearby_points[:,1], \'o\')\n        >>> plt.margins(0.1, 0.1)\n        >>> plt.show()\n\n        ',
    'cKDTree.query_ball_tree (line 989)': '\n        query_ball_tree(self, other, r, p=2., eps=0)\n\n        Find all pairs of points between `self` and `other` whose distance is at most r\n\n        Parameters\n        ----------\n        other : cKDTree instance\n            The tree containing points to search against.\n        r : float\n            The maximum distance, has to be positive.\n        p : float, optional\n            Which Minkowski norm to use.  `p` has to meet the condition\n            ``1 <= p <= infinity``.\n            A finite large p may cause a ValueError if overflow can occur.\n        eps : float, optional\n            Approximate search.  Branches of the tree are not explored\n            if their nearest points are further than ``r/(1+eps)``, and\n            branches are added in bulk if their furthest points are nearer\n            than ``r * (1+eps)``.  `eps` has to be non-negative.\n\n        Returns\n        -------\n        results : list of lists\n            For each element ``self.data[i]`` of this tree, ``results[i]`` is a\n            list of the indices of its neighbors in ``other.data``.\n\n        Examples\n        --------\n        You can search all pairs of points between two kd-trees within a distance:\n\n        >>> import matplotlib.pyplot as plt\n        >>> import numpy as np\n        >>> from scipy.spatial import cKDTree\n        >>> rng = np.random.default_rng()\n        >>> points1 = rng.random((15, 2))\n        >>> points2 = rng.random((15, 2))\n        >>> plt.figure(figsize=(6, 6))\n        >>> plt.plot(points1[:, 0], points1[:, 1], "xk", markersize=14)\n        >>> plt.plot(points2[:, 0], points2[:, 1], "og", markersize=14)\n        >>> kd_tree1 = cKDTree(points1)\n        >>> kd_tree2 = cKDTree(points2)\n        >>> indexes = kd_tree1.query_ball_tree(kd_tree2, r=0.2)\n        >>> for i in range(len(indexes)):\n        ...     for j in indexes[i]:\n        ...         plt.plot([points1[i, 0], points2[j, 0]],\n        ...             [points1[i, 1], points2[j, 1]], "-r")\n        >>> plt.show()\n\n        ',
    'cKDTree.query_pairs (line 1082)': '\n        query_pairs(self, r, p=2., eps=0)\n\n        Find all pairs of points in `self` whose distance is at most r.\n\n        Parameters\n        ----------\n        r : positive float\n            The maximum distance.\n        p : float, optional\n            Which Minkowski norm to use.  ``p`` has to meet the condition\n            ``1 <= p <= infinity``.\n            A finite large p may cause a ValueError if overflow can occur.\n        eps : float, optional\n            Approximate search.  Branches of the tree are not explored\n            if their nearest points are further than ``r/(1+eps)``, and\n            branches are added in bulk if their furthest points are nearer\n            than ``r * (1+eps)``.  `eps` has to be non-negative.\n        output_type : string, optional\n            Choose the output container, \'set\' or \'ndarray\'. Default: \'set\'\n\n        Returns\n        -------\n        results : set or ndarray\n            Set of pairs ``(i,j)``, with ``i < j``, for which the corresponding\n            positions are close. If output_type is \'ndarray\', an ndarry is\n            returned instead of a set.\n\n        Examples\n        --------\n        You can search all pairs of points in a kd-tree within a distance:\n\n        >>> import matplotlib.pyplot as plt\n        >>> import numpy as np\n        >>> from scipy.spatial import cKDTree\n        >>> rng = np.random.default_rng()\n        >>> points = rng.random((20, 2))\n        >>> plt.figure(figsize=(6, 6))\n        >>> plt.plot(points[:, 0], points[:, 1], "xk", markersize=14)\n        >>> kd_tree = cKDTree(points)\n        >>> pairs = kd_tree.query_pairs(r=0.2)\n        >>> for (i, j) in pairs:\n        ...     plt.plot([points[i, 0], points[j, 0]],\n        ...             [points[i, 1], points[j, 1]], "-r")\n        >>> plt.show()\n\n        ',
    'cKDTree.sparse_distance_matrix (line 1453)': '\n        sparse_distance_matrix(self, other, max_distance, p=2.)\n\n        Compute a sparse distance matrix\n\n        Computes a distance matrix between two cKDTrees, leaving as zero\n        any distance greater than max_distance.\n\n        Parameters\n        ----------\n        other : cKDTree\n\n        max_distance : positive float\n\n        p : float, 1<=p<=infinity\n            Which Minkowski p-norm to use.\n            A finite large p may cause a ValueError if overflow can occur.\n\n        output_type : string, optional\n            Which container to use for output data. Options: \'dok_matrix\',\n            \'coo_matrix\', \'dict\', or \'ndarray\'. Default: \'dok_matrix\'.\n\n        Returns\n        -------\n        result : dok_matrix, coo_matrix, dict or ndarray\n            Sparse matrix representing the results in "dictionary of keys"\n            format. If a dict is returned the keys are (i,j) tuples of indices.\n            If output_type is \'ndarray\' a record array with fields \'i\', \'j\',\n            and \'v\' is returned,\n\n        Examples\n        --------\n        You can compute a sparse distance matrix between two kd-trees:\n\n        >>> import numpy as np\n        >>> from scipy.spatial import cKDTree\n        >>> rng = np.random.default_rng()\n        >>> points1 = rng.random((5, 2))\n        >>> points2 = rng.random((5, 2))\n        >>> kd_tree1 = cKDTree(points1)\n        >>> kd_tree2 = cKDTree(points2)\n        >>> sdm = kd_tree1.sparse_distance_matrix(kd_tree2, 0.3)\n        >>> sdm.toarray()\n        array([[0.        , 0.        , 0.12295571, 0.        , 0.        ],\n           [0.        , 0.        , 0.        , 0.        , 0.        ],\n           [0.28942611, 0.        , 0.        , 0.2333084 , 0.        ],\n           [0.        , 0.        , 0.        , 0.        , 0.        ],\n           [0.24617575, 0.29571802, 0.26836782, 0.        , 0.        ]])\n\n        You can check distances above the `max_distance` are zeros:\n\n        >>> from scipy.spatial import distance_matrix\n        >>> distance_matrix(points1, points2)\n        array([[0.56906522, 0.39923701, 0.12295571, 0.8658745 , 0.79428925],\n           [0.37327919, 0.7225693 , 0.87665969, 0.32580855, 0.75679479],\n           [0.28942611, 0.30088013, 0.6395831 , 0.2333084 , 0.33630734],\n           [0.31994999, 0.72658602, 0.71124834, 0.55396483, 0.90785663],\n           [0.24617575, 0.29571802, 0.26836782, 0.57714465, 0.6473269 ]])\n\n        ',
}

