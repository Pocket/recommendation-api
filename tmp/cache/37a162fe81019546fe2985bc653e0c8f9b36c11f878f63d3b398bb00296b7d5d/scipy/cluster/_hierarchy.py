# encoding: utf-8
# module scipy.cluster._hierarchy
# from /.venv/lib/python3.8/site-packages/scipy/cluster/_hierarchy.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /.venv/lib/python3.8/site-packages/numpy/__init__.py

# functions

def calculate_cluster_sizes(*args, **kwargs): # real signature unknown
    """
    Calculate the size of each cluster. The result is the fourth column of
        the linkage matrix.
    
        Parameters
        ----------
        Z : ndarray
            The linkage matrix. The fourth column can be empty.
        cs : ndarray
            The array to store the sizes.
        n : ndarray
            The number of observations.
    """
    pass

def cluster_dist(*args, **kwargs): # real signature unknown
    """
    Form flat clusters by distance criterion.
    
        Parameters
        ----------
        Z : ndarray
            The linkage matrix.
        T : ndarray
            The array to store the cluster numbers. The i'th observation belongs to
            cluster `T[i]`.
        cutoff : double
            Clusters are formed when distances are less than or equal to `cutoff`.
        n : int
            The number of observations.
    """
    pass

def cluster_in(*args, **kwargs): # real signature unknown
    """
    Form flat clusters by inconsistent criterion.
    
        Parameters
        ----------
        Z : ndarray
            The linkage matrix.
        R : ndarray
            The inconsistent matrix.
        T : ndarray
            The array to store the cluster numbers. The i'th observation belongs to
            cluster `T[i]`.
        cutoff : double
            Clusters are formed when the inconsistent values are less than or
            or equal to `cutoff`.
        n : int
            The number of observations.
    """
    pass

def cluster_maxclust_dist(*args, **kwargs): # real signature unknown
    """
    Form flat clusters by maxclust criterion.
    
        Parameters
        ----------
        Z : ndarray
            The linkage matrix.
        T : ndarray
            The array to store the cluster numbers. The i'th observation belongs to
            cluster `T[i]`.
        n : int
            The number of observations.
        mc : int
            The maximum number of clusters.
    """
    pass

def cluster_maxclust_monocrit(*args, **kwargs): # real signature unknown
    """
    Form flat clusters by maxclust_monocrit criterion.
    
        Parameters
        ----------
        Z : ndarray
            The linkage matrix.
        MC : ndarray
            The monotonic criterion array.
        T : ndarray
            The array to store the cluster numbers. The i'th observation belongs to
            cluster `T[i]`.
        n : int
            The number of observations.
        max_nc : int
            The maximum number of clusters.
    """
    pass

def cluster_monocrit(*args, **kwargs): # real signature unknown
    """
    Form flat clusters by monocrit criterion.
    
        Parameters
        ----------
        Z : ndarray
            The linkage matrix.
        MC : ndarray
            The monotonic criterion array.
        T : ndarray
            The array to store the cluster numbers. The i'th observation belongs to
            cluster `T[i]`.
        cutoff : double
            Clusters are formed when the MC values are less than or equal to
            `cutoff`.
        n : int
            The number of observations.
    """
    pass

def cophenetic_distances(*args, **kwargs): # real signature unknown
    """
    Calculate the cophenetic distances between each observation
    
        Parameters
        ----------
        Z : ndarray
            The linkage matrix.
        d : ndarray
            The condensed matrix to store the cophenetic distances.
        n : int
            The number of observations.
    """
    pass

def fast_linkage(*args, **kwargs): # real signature unknown
    """
    Perform hierarchy clustering.
    
        It implements "Generic Clustering Algorithm" from [1]. The worst case
        time complexity is O(N^3), but the best case time complexity is O(N^2) and
        it usually works quite close to the best case.
    
        Parameters
        ----------
        dists : ndarray
            A condensed matrix stores the pairwise distances of the observations.
        n : int
            The number of observations.
        method : int
            The linkage method. 0: single 1: complete 2: average 3: centroid
            4: median 5: ward 6: weighted
    
        Returns
        -------
        Z : ndarray, shape (n - 1, 4)
            Computed linkage matrix.
    
        References
        ----------
        .. [1] Daniel Mullner, "Modern hierarchical, agglomerative clustering
           algorithms", :arXiv:`1109.2378v1`.
    """
    pass

def get_max_dist_for_each_cluster(*args, **kwargs): # real signature unknown
    """
    Get the maximum inconsistency coefficient for each non-singleton cluster.
    
        Parameters
        ----------
        Z : ndarray
            The linkage matrix.
        MD : ndarray
            The array to store the result.
        n : int
            The number of observations.
    """
    pass

def get_max_Rfield_for_each_cluster(*args, **kwargs): # real signature unknown
    """
    Get the maximum statistic for each non-singleton cluster. For the i'th
        non-singleton cluster, max_rfs[i] = max{R[j, rf] j is a descendent of i}.
    
        Parameters
        ----------
        Z : ndarray
            The linkage matrix.
        R : ndarray
            The R matrix.
        max_rfs : ndarray
            The array to store the result.
        n : int
            The number of observations.
        rf : int
            Indicate which column of `R` is used.
    """
    pass

def inconsistent(*args, **kwargs): # real signature unknown
    """
    Calculate the inconsistency statistics.
    
        Parameters
        ----------
        Z : ndarray
            The linkage matrix.
        R : ndarray
            A (n - 1) x 4 matrix to store the result. The inconsistency statistics
            `R[i]` are calculated over `d` levels below cluster i. `R[i, 0]` is the
            mean of distances. `R[i, 1]` is the standard deviation of distances.
            `R[i, 2]` is the number of clusters included. `R[i, 3]` is the
            inconsistency coefficient.
    
            .. math:: \frac{\mathtt{Z[i,2]}-\mathtt{R[i,0]}} {R[i,1]}
    
        n : int
            The number of observations.
        d : int
            The number of levels included in calculation below a node.
    """
    pass

def leaders(*args, **kwargs): # real signature unknown
    """
    Find the leader (root) of each flat cluster.
    
        Parameters
        ----------
        Z : ndarray
            The linkage matrix.
        T : ndarray
            The flat clusters assignment returned by `fcluster` or `fclusterdata`.
        L : ndarray
            `L` and `M` store the result. The leader of flat cluster `L[i]` is
            node `M[i]`.
        M : ndarray
            `L` and `M` store the result. The leader of flat cluster `L[i]` is
            node `M[i]`.
        nc : int
            The number of flat clusters.
        n : int
            The number of observations.
    
        Returns
        -------
        err_node : int
            Found that `T` is invalid when examining node `err_node`.
            `-1` indicates success.
    """
    pass

def linkage(*args, **kwargs): # real signature unknown
    """
    Perform hierarchy clustering.
    
        Parameters
        ----------
        dists : ndarray
            A condensed matrix stores the pairwise distances of the observations.
        n : int
            The number of observations.
        method : int
            The linkage method. 0: single 1: complete 2: average 3: centroid
            4: median 5: ward 6: weighted
    
        Returns
        -------
        Z : ndarray, shape (n - 1, 4)
            Computed linkage matrix.
    """
    pass

def mst_single_linkage(*args, **kwargs): # real signature unknown
    """
    Perform hierarchy clustering using MST algorithm for single linkage.
    
        Parameters
        ----------
        dists : ndarray
            A condensed matrix stores the pairwise distances of the observations.
        n : int
            The number of observations.
    
        Returns
        -------
        Z : ndarray, shape (n - 1, 4)
            Computed linkage matrix.
    """
    pass

def nn_chain(*args, **kwargs): # real signature unknown
    """
    Perform hierarchy clustering using nearest-neighbor chain algorithm.
    
        Parameters
        ----------
        dists : ndarray
            A condensed matrix stores the pairwise distances of the observations.
        n : int
            The number of observations.
        method : int
            The linkage method. 0: single 1: complete 2: average 3: centroid
            4: median 5: ward 6: weighted
    
        Returns
        -------
        Z : ndarray, shape (n - 1, 4)
            Computed linkage matrix.
    """
    pass

def prelist(*args, **kwargs): # real signature unknown
    """
    Perform a pre-order traversal on the linkage tree and get a list of ids
        of the leaves.
    
        Parameters
        ----------
        Z : ndarray
            The linkage matrix.
        members : ndarray
            The array to store the result.
        n : int
            The number of observations.
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Heap(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_LinkageUnionFind(*args, **kwargs): # real signature unknown
    pass

# classes

class Heap(object):
    """
    Binary heap.
    
        Heap stores values and keys. Values are passed explicitly, whereas keys
        are assigned implicitly to natural numbers (from 0 to n - 1).
    
        The supported operations (all have O(log n) time complexity):
    
            * Return the current minimum value and the corresponding key.
            * Remove the current minimum value.
            * Change the value of the given key. Note that the key must be still
              in the heap.
    
        The heap is stored as an array, where children of parent i have indices
        2 * i + 1 and 2 * i + 2. All public methods are based on  `sift_down` and
        `sift_up` methods, which restore the heap property by moving an element
        down or up in the heap.
    """
    def change_value(self, *args, **kwargs): # real signature unknown
        pass

    def get_min(self, *args, **kwargs): # real signature unknown
        pass

    def remove_min(self, *args, **kwargs): # real signature unknown
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0xffff9280dde0>'


class LinkageUnionFind(object):
    """ Structure for fast cluster labeling in unsorted dendrogram. """
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0xffff9280de40>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9280d9a0>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.cluster._hierarchy', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9280d9a0>, origin='/.venv/lib/python3.8/site-packages/scipy/cluster/_hierarchy.cpython-38-aarch64-linux-gnu.so')"

__test__ = {}

