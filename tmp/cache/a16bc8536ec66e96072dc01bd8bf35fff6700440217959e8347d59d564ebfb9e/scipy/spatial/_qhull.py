# encoding: utf-8
# module scipy.spatial._qhull
# from /.venv/lib/python3.8/site-packages/scipy/spatial/_qhull.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
"""
Wrappers for Qhull triangulation, plus some additional N-D geometry utilities

.. versionadded:: 0.9
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /.venv/lib/python3.8/site-packages/numpy/__init__.py
import warnings as warnings # /usr/local/lib/python3.8/warnings.py

# functions

def tsearch(tri, xi): # real signature unknown; restored from __doc__
    """
    tsearch(tri, xi)
    
        Find simplices containing the given points. This function does the
        same thing as `Delaunay.find_simplex`.
    
        Parameters
        ----------
        tri : DelaunayInfo
            Delaunay triangulation
        xi : ndarray of double, shape (..., ndim)
            Points to locate
    
        Returns
        -------
        i : ndarray of int, same shape as `xi`
            Indices of simplices containing each point.
            Points outside the triangulation get the value -1.
    
        See Also
        --------
        Delaunay.find_simplex
    
        Notes
        -----
        .. versionadded:: 0.9
    
        Examples
        --------
        >>> import numpy as np
        >>> import matplotlib.pyplot as plt
        >>> from scipy.spatial import Delaunay, delaunay_plot_2d, tsearch
        >>> rng = np.random.default_rng()
    
        The Delaunay triangulation of a set of random points:
    
        >>> pts = rng.random((20, 2))
        >>> tri = Delaunay(pts)
        >>> _ = delaunay_plot_2d(tri)
    
        Find the simplices containing a given set of points:
    
        >>> loc = rng.uniform(0.2, 0.8, (5, 2))
        >>> s = tsearch(tri, loc)
        >>> plt.triplot(pts[:, 0], pts[:, 1], tri.simplices[s], 'b-', mask=s==-1)
        >>> plt.scatter(loc[:, 0], loc[:, 1], c='r', marker='x')
        >>> plt.show()
    """
    pass

def _copy_docstr(*args, **kwargs): # real signature unknown
    pass

def _get_barycentric_transforms(*args, **kwargs): # real signature unknown
    """
    Compute barycentric affine coordinate transformations for given
        simplices.
    
        Returns
        -------
        Tinvs : array, shape (nsimplex, ndim+1, ndim)
            Barycentric transforms for each simplex.
    
            Tinvs[i,:ndim,:ndim] contains inverse of the matrix ``T``,
            and Tinvs[i,ndim,:] contains the vector ``r_n`` (see below).
    
        Notes
        -----
        Barycentric transform from ``x`` to ``c`` is defined by::
    
            T c = x - r_n
    
        where the ``r_1, ..., r_n`` are the vertices of the simplex.
        The matrix ``T`` is defined by the condition::
    
            T e_j = r_j - r_n
    
        where ``e_j`` is the unit axis vector, e.g, ``e_2 = [0,1,0,0,...]``
        This implies that ``T_ij = (r_j - r_n)_i``.
    
        For the barycentric transforms, we need to compute the inverse
        matrix ``T^-1`` and store the vectors ``r_n`` for each vertex.
        These are stacked into the `Tinvs` returned.
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class _QhullUser(object):
    """ Takes care of basic dealings with the Qhull objects """
    def close(self): # real signature unknown; restored from __doc__
        """
        close()
        
                Finish incremental processing.
        
                Call this to free resources taken up by Qhull, when using the
                incremental mode. After calling this, adding more points is no
                longer possible.
        """
        pass

    def _add_points(self, *args, **kwargs): # real signature unknown
        """
        add_points(points, restart=False)
        
                Process a set of additional new points.
        
                Parameters
                ----------
                points : ndarray
                    New points to add. The dimensionality should match that of the
                    initial points.
                restart : bool, optional
                    Whether to restart processing from scratch, rather than
                    adding points incrementally.
        
                Raises
                ------
                QhullError
                    Raised when Qhull encounters an error condition, such as
                    geometrical degeneracy when options to resolve are not enabled.
        
                See Also
                --------
                close
        
                Notes
                -----
                You need to specify ``incremental=True`` when constructing the
                object to be able to add points incrementally. Incremental addition
                of points is also not possible after `close` has been called.
        """
        pass

    def _update(self, *args, **kwargs): # real signature unknown
        pass

    def __del__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _qhull = None
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'scipy.spatial._qhull', '__doc__': '\\n    Takes care of basic dealings with the Qhull objects\\n    ', '_qhull': None, '__init__': <cyfunction _QhullUser.__init__ at 0xffff973e0e10>, 'close': <cyfunction _QhullUser.close at 0xffff973e0ee0>, '__del__': <cyfunction _QhullUser.__del__ at 0xffff95299040>, '_update': <cyfunction _QhullUser._update at 0xffff95299110>, '_add_points': <cyfunction _QhullUser._add_points at 0xffff952991e0>, '__dict__': <attribute '__dict__' of '_QhullUser' objects>, '__weakref__': <attribute '__weakref__' of '_QhullUser' objects>})"


class ConvexHull(_QhullUser):
    """
    ConvexHull(points, incremental=False, qhull_options=None)
    
        Convex hulls in N dimensions.
    
        .. versionadded:: 0.12.0
    
        Parameters
        ----------
        points : ndarray of floats, shape (npoints, ndim)
            Coordinates of points to construct a convex hull from
        incremental : bool, optional
            Allow adding new points incrementally. This takes up some additional
            resources.
        qhull_options : str, optional
            Additional options to pass to Qhull. See Qhull manual
            for details. (Default: "Qx" for ndim > 4 and "" otherwise)
            Option "Qt" is always enabled.
    
        Attributes
        ----------
        points : ndarray of double, shape (npoints, ndim)
            Coordinates of input points.
        vertices : ndarray of ints, shape (nvertices,)
            Indices of points forming the vertices of the convex hull.
            For 2-D convex hulls, the vertices are in counterclockwise order.
            For other dimensions, they are in input order.
        simplices : ndarray of ints, shape (nfacet, ndim)
            Indices of points forming the simplical facets of the convex hull.
        neighbors : ndarray of ints, shape (nfacet, ndim)
            Indices of neighbor facets for each facet.
            The kth neighbor is opposite to the kth vertex.
            -1 denotes no neighbor.
        equations : ndarray of double, shape (nfacet, ndim+1)
            [normal, offset] forming the hyperplane equation of the facet
            (see `Qhull documentation <http://www.qhull.org/>`__  for more).
        coplanar : ndarray of int, shape (ncoplanar, 3)
            Indices of coplanar points and the corresponding indices of
            the nearest facets and nearest vertex indices.  Coplanar
            points are input points which were *not* included in the
            triangulation due to numerical precision issues.
    
            If option "Qc" is not specified, this list is not computed.
        good : ndarray of bool or None
            A one-dimensional Boolean array indicating which facets are
            good. Used with options that compute good facets, e.g. QGn
            and QG-n. Good facets are defined as those that are
            visible (n) or invisible (-n) from point n, where
            n is the nth point in 'points'. The 'good' attribute may be
            used as an index into 'simplices' to return the good (visible)
            facets: simplices[good]. A facet is visible from the outside
            of the hull only, and neither coplanarity nor degeneracy count
            as cases of visibility.
    
            If a "QGn" or "QG-n" option is not specified, None is returned.
    
            .. versionadded:: 1.3.0
        area : float
            Surface area of the convex hull when input dimension > 2.
            When input `points` are 2-dimensional, this is the perimeter of the convex hull.
    
            .. versionadded:: 0.17.0
        volume : float
            Volume of the convex hull when input dimension > 2.
            When input `points` are 2-dimensional, this is the area of the convex hull.
    
            .. versionadded:: 0.17.0
    
        Raises
        ------
        QhullError
            Raised when Qhull encounters an error condition, such as
            geometrical degeneracy when options to resolve are not enabled.
        ValueError
            Raised if an incompatible array is given as input.
    
        Notes
        -----
        The convex hull is computed using the
        `Qhull library <http://www.qhull.org/>`__.
    
        Examples
        --------
    
        Convex hull of a random set of points:
    
        >>> from scipy.spatial import ConvexHull, convex_hull_plot_2d
        >>> import numpy as np
        >>> rng = np.random.default_rng()
        >>> points = rng.random((30, 2))   # 30 random points in 2-D
        >>> hull = ConvexHull(points)
    
        Plot it:
    
        >>> import matplotlib.pyplot as plt
        >>> plt.plot(points[:,0], points[:,1], 'o')
        >>> for simplex in hull.simplices:
        ...     plt.plot(points[simplex, 0], points[simplex, 1], 'k-')
    
        We could also have directly used the vertices of the hull, which
        for 2-D are guaranteed to be in counterclockwise order:
    
        >>> plt.plot(points[hull.vertices,0], points[hull.vertices,1], 'r--', lw=2)
        >>> plt.plot(points[hull.vertices[0],0], points[hull.vertices[0],1], 'ro')
        >>> plt.show()
    
        Facets visible from a point:
    
        Create a square and add a point above the square.
    
        >>> generators = np.array([[0.2, 0.2],
        ...                        [0.2, 0.4],
        ...                        [0.4, 0.4],
        ...                        [0.4, 0.2],
        ...                        [0.3, 0.6]])
    
        Call ConvexHull with the QG option. QG4 means
        compute the portions of the hull not including
        point 4, indicating the facets that are visible
        from point 4.
    
        >>> hull = ConvexHull(points=generators,
        ...                   qhull_options='QG4')
    
        The "good" array indicates which facets are
        visible from point 4.
    
        >>> print(hull.simplices)
            [[1 0]
             [1 2]
             [3 0]
             [3 2]]
        >>> print(hull.good)
            [False  True False False]
    
        Now plot it, highlighting the visible facets.
    
        >>> fig = plt.figure()
        >>> ax = fig.add_subplot(1,1,1)
        >>> for visible_facet in hull.simplices[hull.good]:
        ...     ax.plot(hull.points[visible_facet, 0],
        ...             hull.points[visible_facet, 1],
        ...             color='violet',
        ...             lw=6)
        >>> convex_hull_plot_2d(hull, ax=ax)
            <Figure size 640x480 with 1 Axes> # may vary
        >>> plt.show()
    
        References
        ----------
        .. [Qhull] http://www.qhull.org/
    """
    def add_points(self, points, restart=False): # real signature unknown; restored from __doc__
        """
        add_points(points, restart=False)
        
                Process a set of additional new points.
        
                Parameters
                ----------
                points : ndarray
                    New points to add. The dimensionality should match that of the
                    initial points.
                restart : bool, optional
                    Whether to restart processing from scratch, rather than
                    adding points incrementally.
        
                Raises
                ------
                QhullError
                    Raised when Qhull encounters an error condition, such as
                    geometrical degeneracy when options to resolve are not enabled.
        
                See Also
                --------
                close
        
                Notes
                -----
                You need to specify ``incremental=True`` when constructing the
                object to be able to add points incrementally. Incremental addition
                of points is also not possible after `close` has been called.
        """
        pass

    def _update(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Delaunay(_QhullUser):
    """
    Delaunay(points, furthest_site=False, incremental=False, qhull_options=None)
    
        Delaunay tessellation in N dimensions.
    
        .. versionadded:: 0.9
    
        Parameters
        ----------
        points : ndarray of floats, shape (npoints, ndim)
            Coordinates of points to triangulate
        furthest_site : bool, optional
            Whether to compute a furthest-site Delaunay triangulation.
            Default: False
    
            .. versionadded:: 0.12.0
        incremental : bool, optional
            Allow adding new points incrementally. This takes up some additional
            resources.
        qhull_options : str, optional
            Additional options to pass to Qhull. See Qhull manual for
            details. Option "Qt" is always enabled.
            Default:"Qbb Qc Qz Qx Q12" for ndim > 4 and "Qbb Qc Qz Q12" otherwise.
            Incremental mode omits "Qz".
    
            .. versionadded:: 0.12.0
    
        Attributes
        ----------
        points : ndarray of double, shape (npoints, ndim)
            Coordinates of input points.
        simplices : ndarray of ints, shape (nsimplex, ndim+1)
            Indices of the points forming the simplices in the triangulation.
            For 2-D, the points are oriented counterclockwise.
        neighbors : ndarray of ints, shape (nsimplex, ndim+1)
            Indices of neighbor simplices for each simplex.
            The kth neighbor is opposite to the kth vertex.
            For simplices at the boundary, -1 denotes no neighbor.
        equations : ndarray of double, shape (nsimplex, ndim+2)
            [normal, offset] forming the hyperplane equation of the facet
            on the paraboloid
            (see `Qhull documentation <http://www.qhull.org/>`__ for more).
        paraboloid_scale, paraboloid_shift : float
            Scale and shift for the extra paraboloid dimension
            (see `Qhull documentation <http://www.qhull.org/>`__ for more).
        transform : ndarray of double, shape (nsimplex, ndim+1, ndim)
            Affine transform from ``x`` to the barycentric coordinates ``c``.
            This is defined by::
    
                T c = x - r
    
            At vertex ``j``, ``c_j = 1`` and the other coordinates zero.
    
            For simplex ``i``, ``transform[i,:ndim,:ndim]`` contains
            inverse of the matrix ``T``, and ``transform[i,ndim,:]``
            contains the vector ``r``.
    
            If the simplex is degenerate or nearly degenerate, its
            barycentric transform contains NaNs.
        vertex_to_simplex : ndarray of int, shape (npoints,)
            Lookup array, from a vertex, to some simplex which it is a part of.
            If qhull option "Qc" was not specified, the list will contain -1
            for points that are not vertices of the tessellation.
        convex_hull : ndarray of int, shape (nfaces, ndim)
            Vertices of facets forming the convex hull of the point set.
            The array contains the indices of the points belonging to
            the (N-1)-dimensional facets that form the convex hull
            of the triangulation.
    
            .. note::
    
               Computing convex hulls via the Delaunay triangulation is
               inefficient and subject to increased numerical instability.
               Use `ConvexHull` instead.
        coplanar : ndarray of int, shape (ncoplanar, 3)
            Indices of coplanar points and the corresponding indices of
            the nearest facet and the nearest vertex.  Coplanar
            points are input points which were *not* included in the
            triangulation due to numerical precision issues.
    
            If option "Qc" is not specified, this list is not computed.
    
            .. versionadded:: 0.12.0
        vertices
            Same as `simplices`, but deprecated.
    
            .. deprecated:: 0.12.0
                Delaunay attribute `vertices` is deprecated in favour of `simplices`
                and will be removed in Scipy 1.11.0.
        vertex_neighbor_vertices : tuple of two ndarrays of int; (indptr, indices)
            Neighboring vertices of vertices. The indices of neighboring
            vertices of vertex `k` are ``indices[indptr[k]:indptr[k+1]]``.
        furthest_site
            True if this was a furthest site triangulation and False if not.
    
            .. versionadded:: 1.4.0
    
        Raises
        ------
        QhullError
            Raised when Qhull encounters an error condition, such as
            geometrical degeneracy when options to resolve are not enabled.
        ValueError
            Raised if an incompatible array is given as input.
    
        Notes
        -----
        The tessellation is computed using the Qhull library
        `Qhull library <http://www.qhull.org/>`__.
    
        .. note::
    
           Unless you pass in the Qhull option "QJ", Qhull does not
           guarantee that each input point appears as a vertex in the
           Delaunay triangulation. Omitted points are listed in the
           `coplanar` attribute.
    
        Examples
        --------
        Triangulation of a set of points:
    
        >>> import numpy as np
        >>> points = np.array([[0, 0], [0, 1.1], [1, 0], [1, 1]])
        >>> from scipy.spatial import Delaunay
        >>> tri = Delaunay(points)
    
        We can plot it:
    
        >>> import matplotlib.pyplot as plt
        >>> plt.triplot(points[:,0], points[:,1], tri.simplices)
        >>> plt.plot(points[:,0], points[:,1], 'o')
        >>> plt.show()
    
        Point indices and coordinates for the two triangles forming the
        triangulation:
    
        >>> tri.simplices
        array([[2, 3, 0],                 # may vary
               [3, 1, 0]], dtype=int32)
    
        Note that depending on how rounding errors go, the simplices may
        be in a different order than above.
    
        >>> points[tri.simplices]
        array([[[ 1. ,  0. ],            # may vary
                [ 1. ,  1. ],
                [ 0. ,  0. ]],
               [[ 1. ,  1. ],
                [ 0. ,  1.1],
                [ 0. ,  0. ]]])
    
        Triangle 0 is the only neighbor of triangle 1, and it's opposite to
        vertex 1 of triangle 1:
    
        >>> tri.neighbors[1]
        array([-1,  0, -1], dtype=int32)
        >>> points[tri.simplices[1,1]]
        array([ 0. ,  1.1])
    
        We can find out which triangle points are in:
    
        >>> p = np.array([(0.1, 0.2), (1.5, 0.5), (0.5, 1.05)])
        >>> tri.find_simplex(p)
        array([ 1, -1, 1], dtype=int32)
    
        The returned integers in the array are the indices of the simplex the
        corresponding point is in. If -1 is returned, the point is in no simplex.
        Be aware that the shortcut in the following example only works correctly
        for valid points as invalid points result in -1 which is itself a valid
        index for the last simplex in the list.
    
        >>> p_valids = np.array([(0.1, 0.2), (0.5, 1.05)])
        >>> tri.simplices[tri.find_simplex(p_valids)]
        array([[3, 1, 0],                 # may vary
               [3, 1, 0]], dtype=int32)
    
        We can also compute barycentric coordinates in triangle 1 for
        these points:
    
        >>> b = tri.transform[1,:2].dot(np.transpose(p - tri.transform[1,2]))
        >>> np.c_[np.transpose(b), 1 - b.sum(axis=0)]
        array([[ 0.1       ,  0.09090909,  0.80909091],
               [ 1.5       , -0.90909091,  0.40909091],
               [ 0.5       ,  0.5       ,  0.        ]])
    
        The coordinates for the first point are all positive, meaning it
        is indeed inside the triangle. The third point is on an edge,
        hence its null third coordinate.
    """
    def add_points(self, points, restart=False): # real signature unknown; restored from __doc__
        """
        add_points(points, restart=False)
        
                Process a set of additional new points.
        
                Parameters
                ----------
                points : ndarray
                    New points to add. The dimensionality should match that of the
                    initial points.
                restart : bool, optional
                    Whether to restart processing from scratch, rather than
                    adding points incrementally.
        
                Raises
                ------
                QhullError
                    Raised when Qhull encounters an error condition, such as
                    geometrical degeneracy when options to resolve are not enabled.
        
                See Also
                --------
                close
        
                Notes
                -----
                You need to specify ``incremental=True`` when constructing the
                object to be able to add points incrementally. Incremental addition
                of points is also not possible after `close` has been called.
        """
        pass

    def find_simplex(self, xi, bruteforce=False, tol=None): # real signature unknown; restored from __doc__
        """
        find_simplex(self, xi, bruteforce=False, tol=None)
        
                Find the simplices containing the given points.
        
                Parameters
                ----------
                tri : DelaunayInfo
                    Delaunay triangulation
                xi : ndarray of double, shape (..., ndim)
                    Points to locate
                bruteforce : bool, optional
                    Whether to only perform a brute-force search
                tol : float, optional
                    Tolerance allowed in the inside-triangle check.
                    Default is ``100*eps``.
        
                Returns
                -------
                i : ndarray of int, same shape as `xi`
                    Indices of simplices containing each point.
                    Points outside the triangulation get the value -1.
        
                Notes
                -----
                This uses an algorithm adapted from Qhull's ``qh_findbestfacet``,
                which makes use of the connection between a convex hull and a
                Delaunay triangulation. After finding the simplex closest to
                the point in N+1 dimensions, the algorithm falls back to
                directed search in N dimensions.
        """
        pass

    def lift_points(self, x): # real signature unknown; restored from __doc__
        """
        lift_points(self, x)
        
                Lift points to the Qhull paraboloid.
        """
        pass

    def plane_distance(self, xi): # real signature unknown; restored from __doc__
        """
        plane_distance(self, xi)
        
                Compute hyperplane distances to the point `xi` from all simplices.
        """
        pass

    def _update(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    convex_hull = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Vertices of facets forming the convex hull of the point set.

        :type: *ndarray of int, shape (nfaces, ndim)*

        The array contains the indices of the points
        belonging to the (N-1)-dimensional facets that form the convex
        hull of the triangulation.

        .. note::

           Computing convex hulls via the Delaunay triangulation is
           inefficient and subject to increased numerical instability.
           Use `ConvexHull` instead.

        """

    points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Affine transform from ``x`` to the barycentric coordinates ``c``.

        :type: *ndarray of double, shape (nsimplex, ndim+1, ndim)*

        This is defined by::

            T c = x - r

        At vertex ``j``, ``c_j = 1`` and the other coordinates zero.

        For simplex ``i``, ``transform[i,:ndim,:ndim]`` contains
        inverse of the matrix ``T``, and ``transform[i,ndim,:]``
        contains the vector ``r``.

        """

    vertex_neighbor_vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Neighboring vertices of vertices.

        Tuple of two ndarrays of int: (indptr, indices). The indices of
        neighboring vertices of vertex `k` are
        ``indices[indptr[k]:indptr[k+1]]``.

        """

    vertex_to_simplex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Lookup array, from a vertex, to some simplex which it is a part of.

        :type: *ndarray of int, shape (npoints,)*
        """

    vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class HalfspaceIntersection(_QhullUser):
    """
    HalfspaceIntersection(halfspaces, interior_point, incremental=False, qhull_options=None)
    
        Halfspace intersections in N dimensions.
    
        .. versionadded:: 0.19.0
    
        Parameters
        ----------
        halfspaces : ndarray of floats, shape (nineq, ndim+1)
            Stacked Inequalities of the form Ax + b <= 0 in format [A; b]
        interior_point : ndarray of floats, shape (ndim,)
            Point clearly inside the region defined by halfspaces. Also called a feasible
            point, it can be obtained by linear programming.
        incremental : bool, optional
            Allow adding new halfspaces incrementally. This takes up some additional
            resources.
        qhull_options : str, optional
            Additional options to pass to Qhull. See Qhull manual
            for details. (Default: "Qx" for ndim > 4 and "" otherwise)
            Option "H" is always enabled.
    
        Attributes
        ----------
        halfspaces : ndarray of double, shape (nineq, ndim+1)
            Input halfspaces.
        interior_point :ndarray of floats, shape (ndim,)
            Input interior point.
        intersections : ndarray of double, shape (ninter, ndim)
            Intersections of all halfspaces.
        dual_points : ndarray of double, shape (nineq, ndim)
            Dual points of the input halfspaces.
        dual_facets : list of lists of ints
            Indices of points forming the (non necessarily simplicial) facets of
            the dual convex hull.
        dual_vertices : ndarray of ints, shape (nvertices,)
            Indices of halfspaces forming the vertices of the dual convex hull.
            For 2-D convex hulls, the vertices are in counterclockwise order.
            For other dimensions, they are in input order.
        dual_equations : ndarray of double, shape (nfacet, ndim+1)
            [normal, offset] forming the hyperplane equation of the dual facet
            (see `Qhull documentation <http://www.qhull.org/>`__  for more).
        dual_area : float
            Area of the dual convex hull
        dual_volume : float
            Volume of the dual convex hull
    
        Raises
        ------
        QhullError
            Raised when Qhull encounters an error condition, such as
            geometrical degeneracy when options to resolve are not enabled.
        ValueError
            Raised if an incompatible array is given as input.
    
        Notes
        -----
        The intersections are computed using the
        `Qhull library <http://www.qhull.org/>`__.
        This reproduces the "qhalf" functionality of Qhull.
    
        Examples
        --------
    
        Halfspace intersection of planes forming some polygon
    
        >>> from scipy.spatial import HalfspaceIntersection
        >>> import numpy as np
        >>> halfspaces = np.array([[-1, 0., 0.],
        ...                        [0., -1., 0.],
        ...                        [2., 1., -4.],
        ...                        [-0.5, 1., -2.]])
        >>> feasible_point = np.array([0.5, 0.5])
        >>> hs = HalfspaceIntersection(halfspaces, feasible_point)
    
        Plot halfspaces as filled regions and intersection points:
    
        >>> import matplotlib.pyplot as plt
        >>> fig = plt.figure()
        >>> ax = fig.add_subplot(1, 1, 1, aspect='equal')
        >>> xlim, ylim = (-1, 3), (-1, 3)
        >>> ax.set_xlim(xlim)
        >>> ax.set_ylim(ylim)
        >>> x = np.linspace(-1, 3, 100)
        >>> symbols = ['-', '+', 'x', '*']
        >>> signs = [0, 0, -1, -1]
        >>> fmt = {"color": None, "edgecolor": "b", "alpha": 0.5}
        >>> for h, sym, sign in zip(halfspaces, symbols, signs):
        ...     hlist = h.tolist()
        ...     fmt["hatch"] = sym
        ...     if h[1]== 0:
        ...         ax.axvline(-h[2]/h[0], label='{}x+{}y+{}=0'.format(*hlist))
        ...         xi = np.linspace(xlim[sign], -h[2]/h[0], 100)
        ...         ax.fill_between(xi, ylim[0], ylim[1], **fmt)
        ...     else:
        ...         ax.plot(x, (-h[2]-h[0]*x)/h[1], label='{}x+{}y+{}=0'.format(*hlist))
        ...         ax.fill_between(x, (-h[2]-h[0]*x)/h[1], ylim[sign], **fmt)
        >>> x, y = zip(*hs.intersections)
        >>> ax.plot(x, y, 'o', markersize=8)
    
        By default, qhull does not provide with a way to compute an interior point.
        This can easily be computed using linear programming. Considering halfspaces
        of the form :math:`Ax + b \leq 0`, solving the linear program:
    
        .. math::
    
            max \: y
    
            s.t. Ax + y ||A_i|| \leq -b
    
        With :math:`A_i` being the rows of A, i.e. the normals to each plane.
    
        Will yield a point x that is furthest inside the convex polyhedron. To
        be precise, it is the center of the largest hypersphere of radius y
        inscribed in the polyhedron. This point is called the Chebyshev center
        of the polyhedron (see [1]_ 4.3.1, pp148-149). The
        equations outputted by Qhull are always normalized.
    
        >>> from scipy.optimize import linprog
        >>> from matplotlib.patches import Circle
        >>> norm_vector = np.reshape(np.linalg.norm(halfspaces[:, :-1], axis=1),
        ...     (halfspaces.shape[0], 1))
        >>> c = np.zeros((halfspaces.shape[1],))
        >>> c[-1] = -1
        >>> A = np.hstack((halfspaces[:, :-1], norm_vector))
        >>> b = - halfspaces[:, -1:]
        >>> res = linprog(c, A_ub=A, b_ub=b, bounds=(None, None))
        >>> x = res.x[:-1]
        >>> y = res.x[-1]
        >>> circle = Circle(x, radius=y, alpha=0.3)
        >>> ax.add_patch(circle)
        >>> plt.legend(bbox_to_anchor=(1.6, 1.0))
        >>> plt.show()
    
        References
        ----------
        .. [Qhull] http://www.qhull.org/
        .. [1] S. Boyd, L. Vandenberghe, Convex Optimization, available
               at http://stanford.edu/~boyd/cvxbook/
    """
    def add_halfspaces(self, halfspaces, restart=False): # real signature unknown; restored from __doc__
        """
        add_halfspaces(halfspaces, restart=False)
        
                Process a set of additional new halfspaces.
        
                Parameters
                ----------
                halfspaces : ndarray
                    New halfspaces to add. The dimensionality should match that of the
                    initial halfspaces.
                restart : bool, optional
                    Whether to restart processing from scratch, rather than
                    adding halfspaces incrementally.
        
                Raises
                ------
                QhullError
                    Raised when Qhull encounters an error condition, such as
                    geometrical degeneracy when options to resolve are not enabled.
        
                See Also
                --------
                close
        
                Notes
                -----
                You need to specify ``incremental=True`` when constructing the
                object to be able to add halfspaces incrementally. Incremental addition
                of halfspaces is also not possible after `close` has been called.
        """
        pass

    def _update(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    dual_vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    halfspaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class QhullError(RuntimeError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class Voronoi(_QhullUser):
    """
    Voronoi(points, furthest_site=False, incremental=False, qhull_options=None)
    
        Voronoi diagrams in N dimensions.
    
        .. versionadded:: 0.12.0
    
        Parameters
        ----------
        points : ndarray of floats, shape (npoints, ndim)
            Coordinates of points to construct a Voronoi diagram from
        furthest_site : bool, optional
            Whether to compute a furthest-site Voronoi diagram. Default: False
        incremental : bool, optional
            Allow adding new points incrementally. This takes up some additional
            resources.
        qhull_options : str, optional
            Additional options to pass to Qhull. See Qhull manual
            for details. (Default: "Qbb Qc Qz Qx" for ndim > 4 and
            "Qbb Qc Qz" otherwise. Incremental mode omits "Qz".)
    
        Attributes
        ----------
        points : ndarray of double, shape (npoints, ndim)
            Coordinates of input points.
        vertices : ndarray of double, shape (nvertices, ndim)
            Coordinates of the Voronoi vertices.
        ridge_points : ndarray of ints, shape ``(nridges, 2)``
            Indices of the points between which each Voronoi ridge lies.
        ridge_vertices : list of list of ints, shape ``(nridges, *)``
            Indices of the Voronoi vertices forming each Voronoi ridge.
        regions : list of list of ints, shape ``(nregions, *)``
            Indices of the Voronoi vertices forming each Voronoi region.
            -1 indicates vertex outside the Voronoi diagram.
            When qhull option "Qz" was specified, an empty sublist
            represents the Voronoi region for a point at infinity that
            was added internally.
        point_region : array of ints, shape (npoints)
            Index of the Voronoi region for each input point.
            If qhull option "Qc" was not specified, the list will contain -1
            for points that are not associated with a Voronoi region.
            If qhull option "Qz" was specified, there will be one less
            element than the number of regions because an extra point
            at infinity is added internally to facilitate computation.
        furthest_site
            True if this was a furthest site triangulation and False if not.
    
            .. versionadded:: 1.4.0
    
        Raises
        ------
        QhullError
            Raised when Qhull encounters an error condition, such as
            geometrical degeneracy when options to resolve are not enabled.
        ValueError
            Raised if an incompatible array is given as input.
    
        Notes
        -----
        The Voronoi diagram is computed using the
        `Qhull library <http://www.qhull.org/>`__.
    
        Examples
        --------
        Voronoi diagram for a set of point:
    
        >>> import numpy as np
        >>> points = np.array([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2],
        ...                    [2, 0], [2, 1], [2, 2]])
        >>> from scipy.spatial import Voronoi, voronoi_plot_2d
        >>> vor = Voronoi(points)
    
        Plot it:
    
        >>> import matplotlib.pyplot as plt
        >>> fig = voronoi_plot_2d(vor)
        >>> plt.show()
    
        The Voronoi vertices:
    
        >>> vor.vertices
        array([[0.5, 0.5],
               [0.5, 1.5],
               [1.5, 0.5],
               [1.5, 1.5]])
    
        There is a single finite Voronoi region, and four finite Voronoi
        ridges:
    
        >>> vor.regions
        [[], [-1, 0], [-1, 1], [1, -1, 0], [3, -1, 2], [-1, 3], [-1, 2], [0, 1, 3, 2], [2, -1, 0], [3, -1, 1]]
        >>> vor.ridge_vertices
        [[-1, 0], [-1, 0], [-1, 1], [-1, 1], [0, 1], [-1, 3], [-1, 2], [2, 3], [-1, 3], [-1, 2], [1, 3], [0, 2]]
    
        The ridges are perpendicular between lines drawn between the following
        input points:
    
        >>> vor.ridge_points
        array([[0, 3],
               [0, 1],
               [2, 5],
               [2, 1],
               [1, 4],
               [7, 8],
               [7, 6],
               [7, 4],
               [8, 5],
               [6, 3],
               [4, 5],
               [4, 3]], dtype=int32)
    """
    def add_points(self, points, restart=False): # real signature unknown; restored from __doc__
        """
        add_points(points, restart=False)
        
                Process a set of additional new points.
        
                Parameters
                ----------
                points : ndarray
                    New points to add. The dimensionality should match that of the
                    initial points.
                restart : bool, optional
                    Whether to restart processing from scratch, rather than
                    adding points incrementally.
        
                Raises
                ------
                QhullError
                    Raised when Qhull encounters an error condition, such as
                    geometrical degeneracy when options to resolve are not enabled.
        
                See Also
                --------
                close
        
                Notes
                -----
                You need to specify ``incremental=True`` when constructing the
                object to be able to add points incrementally. Incremental addition
                of points is also not possible after `close` has been called.
        """
        pass

    def _update(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ridge_dict = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class _Qhull(object):
    # no doc
    def add_points(self, *args, **kwargs): # real signature unknown
        pass

    def check_active(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, *args, **kwargs): # real signature unknown
        """ Uninitialize this instance """
        pass

    def get_extremes_2d(self, *args, **kwargs): # real signature unknown
        """
        Compute the extremal points in a 2-D convex hull, i.e. the
                vertices of the convex hull, ordered counterclockwise.
        
                See qhull/io.c:qh_printextremes_2d
        """
        pass

    def get_hull_facets(self, *args, **kwargs): # real signature unknown
        """
        Returns the facets contained in the current Qhull.
                This function does not assume that the hull is simplicial,
                meaning that facets will have different number of vertices.
                It is thus less efficient but more general than get_simplex_facet_array.
        
                Returns
                -------
                facets: list of lists of ints
                    The indices of the vertices forming each facet.
        """
        pass

    def get_hull_points(self, *args, **kwargs): # real signature unknown
        """
        Returns all points currently contained in Qhull.
                It is equivalent to retrieving the input in most cases, except in
                halfspace mode, where the points are in fact the points of the dual
                hull.
        
                Returns
                -------
                points: array of double, shape (nrpoints, ndim)
                    The array of points contained in Qhull.
        """
        pass

    def get_paraboloid_shift_scale(self, *args, **kwargs): # real signature unknown
        pass

    def get_points(self, *args, **kwargs): # real signature unknown
        pass

    def get_simplex_facet_array(self, *args, **kwargs): # real signature unknown
        """
        Return array of simplical facets currently in Qhull.
        
                Returns
                -------
                facets : array of int, shape (nfacets, ndim+1)
                    Indices of coordinates of vertices forming the simplical facets
                neighbors : array of int, shape (nfacets, ndim)
                    Indices of neighboring facets.  The kth neighbor is opposite
                    the kth vertex, and the first neighbor is the horizon facet
                    for the first vertex.
        
                    Facets extending to infinity are denoted with index -1.
                equations : array of double, shape (nfacets, ndim+2)
        """
        pass

    def get_voronoi_diagram(self, *args, **kwargs): # real signature unknown
        """
        Return the voronoi diagram currently in Qhull.
        
                Returns
                -------
                voronoi_vertices : array of double, shape (nvoronoi_vertices, ndim)
                    Coordinates of the Voronoi vertices
        
                ridge_points : array of double, shape (nridges, 2)
                    Voronoi ridges, as indices to the points array.
        
                ridge_vertices : list of lists, shape (nridges, *)
                    Voronoi vertices for each Voronoi ridge, as indices to
                    the Voronoi vertices array.
                    Infinity is indicated by index ``-1``.
        
                regions : list of lists, shape (nregion, *)
                    Voronoi vertices of all regions.
        
                point_region : array of int, shape (npoint,)
                    Index of the Voronoi region for each input point.
        """
        pass

    def triangulate(self, *args, **kwargs): # real signature unknown
        pass

    def volume_area(self, *args, **kwargs): # real signature unknown
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

    furthest_site = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mode_option = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ndim = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

__all__ = [
    'Delaunay',
    'ConvexHull',
    'QhullError',
    'Voronoi',
    'HalfspaceIntersection',
    'tsearch',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9f8eadf0>'

__pyx_capi__ = {
    '_barycentric_coordinate_single': None, # (!) real value is '<capsule object "void (int, double *, double *, double *, int)" at 0xffff95294780>'
    '_barycentric_coordinates': None, # (!) real value is '<capsule object "void (int, double *, double *, double *)" at 0xffff952947b0>'
    '_barycentric_inside': None, # (!) real value is '<capsule object "int (int, double *, double *, double *, double)" at 0xffff95294750>'
    '_distplane': None, # (!) real value is '<capsule object "double (__pyx_t_5scipy_7spatial_6_qhull_DelaunayInfo_t *, int, double *)" at 0xffff95294810>'
    '_find_simplex': None, # (!) real value is '<capsule object "int (__pyx_t_5scipy_7spatial_6_qhull_DelaunayInfo_t *, double *, double *, int *, double, double)" at 0xffff952948d0>'
    '_find_simplex_bruteforce': None, # (!) real value is '<capsule object "int (__pyx_t_5scipy_7spatial_6_qhull_DelaunayInfo_t *, double *, double *, double, double)" at 0xffff95294870>'
    '_find_simplex_directed': None, # (!) real value is '<capsule object "int (__pyx_t_5scipy_7spatial_6_qhull_DelaunayInfo_t *, double *, double *, int *, double, double)" at 0xffff952948a0>'
    '_get_delaunay_info': None, # (!) real value is '<capsule object "int (__pyx_t_5scipy_7spatial_6_qhull_DelaunayInfo_t *, PyObject *, int, int, int)" at 0xffff95294720>'
    '_is_point_fully_outside': None, # (!) real value is '<capsule object "int (__pyx_t_5scipy_7spatial_6_qhull_DelaunayInfo_t *, double *, double)" at 0xffff95294840>'
    '_lift_point': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_7spatial_6_qhull_DelaunayInfo_t *, double *, double *)" at 0xffff952947e0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.spatial._qhull', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9f8eadf0>, origin='/.venv/lib/python3.8/site-packages/scipy/spatial/_qhull.cpython-38-aarch64-linux-gnu.so')"

__test__ = {
    'tsearch (line 2172)': "\n    tsearch(tri, xi)\n\n    Find simplices containing the given points. This function does the\n    same thing as `Delaunay.find_simplex`.\n\n    Parameters\n    ----------\n    tri : DelaunayInfo\n        Delaunay triangulation\n    xi : ndarray of double, shape (..., ndim)\n        Points to locate\n\n    Returns\n    -------\n    i : ndarray of int, same shape as `xi`\n        Indices of simplices containing each point.\n        Points outside the triangulation get the value -1.\n\n    See Also\n    --------\n    Delaunay.find_simplex\n\n    Notes\n    -----\n    .. versionadded:: 0.9\n\n    Examples\n    --------\n    >>> import numpy as np\n    >>> import matplotlib.pyplot as plt\n    >>> from scipy.spatial import Delaunay, delaunay_plot_2d, tsearch\n    >>> rng = np.random.default_rng()\n\n    The Delaunay triangulation of a set of random points:\n\n    >>> pts = rng.random((20, 2))\n    >>> tri = Delaunay(pts)\n    >>> _ = delaunay_plot_2d(tri)\n\n    Find the simplices containing a given set of points:\n\n    >>> loc = rng.uniform(0.2, 0.8, (5, 2))\n    >>> s = tsearch(tri, loc)\n    >>> plt.triplot(pts[:, 0], pts[:, 1], tri.simplices[s], 'b-', mask=s==-1)\n    >>> plt.scatter(loc[:, 0], loc[:, 1], c='r', marker='x')\n    >>> plt.show()\n\n    ",
}

