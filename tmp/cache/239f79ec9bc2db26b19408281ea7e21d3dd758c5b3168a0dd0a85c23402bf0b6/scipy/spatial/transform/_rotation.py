# encoding: utf-8
# module scipy.spatial.transform._rotation
# from /.venv/lib/python3.8/site-packages/scipy/spatial/transform/_rotation.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import re as re # /usr/local/lib/python3.8/re.py
import warnings as warnings # /usr/local/lib/python3.8/warnings.py
import numpy as np # /.venv/lib/python3.8/site-packages/numpy/__init__.py

# functions

def check_random_state(seed): # reliably restored by inspect
    """
    Turn `seed` into a `np.random.RandomState` instance.
    
        Parameters
        ----------
        seed : {None, int, `numpy.random.Generator`, `numpy.random.RandomState`}, optional
            If `seed` is None (or `np.random`), the `numpy.random.RandomState`
            singleton is used.
            If `seed` is an int, a new ``RandomState`` instance is used,
            seeded with `seed`.
            If `seed` is already a ``Generator`` or ``RandomState`` instance then
            that instance is used.
    
        Returns
        -------
        seed : {`numpy.random.Generator`, `numpy.random.RandomState`}
            Random number generator.
    """
    pass

def create_group(cls, group, axis=None): # reliably restored by inspect
    # no doc
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Rotation(*args, **kwargs): # real signature unknown
    pass

# classes

class Rotation(object):
    """
    Rotation in 3 dimensions.
    
        This class provides an interface to initialize from and represent rotations
        with:
    
        - Quaternions
        - Rotation Matrices
        - Rotation Vectors
        - Modified Rodrigues Parameters
        - Euler Angles
    
        The following operations on rotations are supported:
    
        - Application on vectors
        - Rotation Composition
        - Rotation Inversion
        - Rotation Indexing
    
        Indexing within a rotation is supported since multiple rotation transforms
        can be stored within a single `Rotation` instance.
    
        To create `Rotation` objects use ``from_...`` methods (see examples below).
        ``Rotation(...)`` is not supposed to be instantiated directly.
    
        Attributes
        ----------
        single
    
        Methods
        -------
        __len__
        from_quat
        from_matrix
        from_rotvec
        from_mrp
        from_euler
        as_quat
        as_matrix
        as_rotvec
        as_mrp
        as_euler
        concatenate
        apply
        __mul__
        inv
        magnitude
        mean
        reduce
        create_group
        __getitem__
        identity
        random
        align_vectors
    
        See Also
        --------
        Slerp
    
        Notes
        -----
        .. versionadded: 1.2.0
    
        Examples
        --------
        >>> from scipy.spatial.transform import Rotation as R
        >>> import numpy as np
    
        A `Rotation` instance can be initialized in any of the above formats and
        converted to any of the others. The underlying object is independent of the
        representation used for initialization.
    
        Consider a counter-clockwise rotation of 90 degrees about the z-axis. This
        corresponds to the following quaternion (in scalar-last format):
    
        >>> r = R.from_quat([0, 0, np.sin(np.pi/4), np.cos(np.pi/4)])
    
        The rotation can be expressed in any of the other formats:
    
        >>> r.as_matrix()
        array([[ 2.22044605e-16, -1.00000000e+00,  0.00000000e+00],
        [ 1.00000000e+00,  2.22044605e-16,  0.00000000e+00],
        [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00]])
        >>> r.as_rotvec()
        array([0.        , 0.        , 1.57079633])
        >>> r.as_euler('zyx', degrees=True)
        array([90.,  0.,  0.])
    
        The same rotation can be initialized using a rotation matrix:
    
        >>> r = R.from_matrix([[0, -1, 0],
        ...                    [1, 0, 0],
        ...                    [0, 0, 1]])
    
        Representation in other formats:
    
        >>> r.as_quat()
        array([0.        , 0.        , 0.70710678, 0.70710678])
        >>> r.as_rotvec()
        array([0.        , 0.        , 1.57079633])
        >>> r.as_euler('zyx', degrees=True)
        array([90.,  0.,  0.])
    
        The rotation vector corresponding to this rotation is given by:
    
        >>> r = R.from_rotvec(np.pi/2 * np.array([0, 0, 1]))
    
        Representation in other formats:
    
        >>> r.as_quat()
        array([0.        , 0.        , 0.70710678, 0.70710678])
        >>> r.as_matrix()
        array([[ 2.22044605e-16, -1.00000000e+00,  0.00000000e+00],
               [ 1.00000000e+00,  2.22044605e-16,  0.00000000e+00],
               [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00]])
        >>> r.as_euler('zyx', degrees=True)
        array([90.,  0.,  0.])
    
        The ``from_euler`` method is quite flexible in the range of input formats
        it supports. Here we initialize a single rotation about a single axis:
    
        >>> r = R.from_euler('z', 90, degrees=True)
    
        Again, the object is representation independent and can be converted to any
        other format:
    
        >>> r.as_quat()
        array([0.        , 0.        , 0.70710678, 0.70710678])
        >>> r.as_matrix()
        array([[ 2.22044605e-16, -1.00000000e+00,  0.00000000e+00],
               [ 1.00000000e+00,  2.22044605e-16,  0.00000000e+00],
               [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00]])
        >>> r.as_rotvec()
        array([0.        , 0.        , 1.57079633])
    
        It is also possible to initialize multiple rotations in a single instance
        using any of the ``from_...`` functions. Here we initialize a stack of 3
        rotations using the ``from_euler`` method:
    
        >>> r = R.from_euler('zyx', [
        ... [90, 0, 0],
        ... [0, 45, 0],
        ... [45, 60, 30]], degrees=True)
    
        The other representations also now return a stack of 3 rotations. For
        example:
    
        >>> r.as_quat()
        array([[0.        , 0.        , 0.70710678, 0.70710678],
               [0.        , 0.38268343, 0.        , 0.92387953],
               [0.39190384, 0.36042341, 0.43967974, 0.72331741]])
    
        Applying the above rotations onto a vector:
    
        >>> v = [1, 2, 3]
        >>> r.apply(v)
        array([[-2.        ,  1.        ,  3.        ],
               [ 2.82842712,  2.        ,  1.41421356],
               [ 2.24452282,  0.78093109,  2.89002836]])
    
        A `Rotation` instance can be indexed and sliced as if it were a single
        1D array or list:
    
        >>> r.as_quat()
        array([[0.        , 0.        , 0.70710678, 0.70710678],
               [0.        , 0.38268343, 0.        , 0.92387953],
               [0.39190384, 0.36042341, 0.43967974, 0.72331741]])
        >>> p = r[0]
        >>> p.as_matrix()
        array([[ 2.22044605e-16, -1.00000000e+00,  0.00000000e+00],
               [ 1.00000000e+00,  2.22044605e-16,  0.00000000e+00],
               [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00]])
        >>> q = r[1:3]
        >>> q.as_quat()
        array([[0.        , 0.38268343, 0.        , 0.92387953],
               [0.39190384, 0.36042341, 0.43967974, 0.72331741]])
    
        In fact it can be converted to numpy.array:
    
        >>> r_array = np.asarray(r)
        >>> r_array.shape
        (3,)
        >>> r_array[0].as_matrix()
        array([[ 2.22044605e-16, -1.00000000e+00,  0.00000000e+00],
               [ 1.00000000e+00,  2.22044605e-16,  0.00000000e+00],
               [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00]])
    
        Multiple rotations can be composed using the ``*`` operator:
    
        >>> r1 = R.from_euler('z', 90, degrees=True)
        >>> r2 = R.from_rotvec([np.pi/4, 0, 0])
        >>> v = [1, 2, 3]
        >>> r2.apply(r1.apply(v))
        array([-2.        , -1.41421356,  2.82842712])
        >>> r3 = r2 * r1 # Note the order
        >>> r3.apply(v)
        array([-2.        , -1.41421356,  2.82842712])
    
        Finally, it is also possible to invert rotations:
    
        >>> r1 = R.from_euler('z', [90, 45], degrees=True)
        >>> r2 = r1.inv()
        >>> r2.as_euler('zyx', degrees=True)
        array([[-90.,   0.,   0.],
               [-45.,   0.,   0.]])
    
        These examples serve as an overview into the `Rotation` class and highlight
        major functionalities. For more thorough examples of the range of input and
        output formats supported, consult the individual method's examples.
    """
    @classmethod
    def align_vectors(cls, type_cls, a, b, weights=None, return_sensitivity=False): # real signature unknown; restored from __doc__
        """
        Rotation.align_vectors(type cls, a, b, weights=None, return_sensitivity=False)
        Estimate a rotation to optimally align two sets of vectors.
        
                Find a rotation between frames A and B which best aligns a set of
                vectors `a` and `b` observed in these frames. The following loss
                function is minimized to solve for the rotation matrix
                :math:`C`:
        
                .. math::
        
                    L(C) = \frac{1}{2} \sum_{i = 1}^{n} w_i \lVert \mathbf{a}_i -
                    C \mathbf{b}_i \rVert^2 ,
        
                where :math:`w_i`'s are the `weights` corresponding to each vector.
        
                The rotation is estimated with Kabsch algorithm [1]_.
        
                Parameters
                ----------
                a : array_like, shape (N, 3)
                    Vector components observed in initial frame A. Each row of `a`
                    denotes a vector.
                b : array_like, shape (N, 3)
                    Vector components observed in another frame B. Each row of `b`
                    denotes a vector.
                weights : array_like shape (N,), optional
                    Weights describing the relative importance of the vector
                    observations. If None (default), then all values in `weights` are
                    assumed to be 1.
                return_sensitivity : bool, optional
                    Whether to return the sensitivity matrix. See Notes for details.
                    Default is False.
        
                Returns
                -------
                estimated_rotation : `Rotation` instance
                    Best estimate of the rotation that transforms `b` to `a`.
                rssd : float
                    Square root of the weighted sum of the squared distances between
                    the given sets of vectors after alignment. It is equal to
                    ``sqrt(2 * minimum_loss)``, where ``minimum_loss`` is the loss
                    function evaluated for the found optimal rotation.
                sensitivity_matrix : ndarray, shape (3, 3)
                    Sensitivity matrix of the estimated rotation estimate as explained
                    in Notes. Returned only when `return_sensitivity` is True.
        
                Notes
                -----
                This method can also compute the sensitivity of the estimated rotation
                to small perturbations of the vector measurements. Specifically we
                consider the rotation estimate error as a small rotation vector of
                frame A. The sensitivity matrix is proportional to the covariance of
                this rotation vector assuming that the vectors in `a` was measured with
                errors significantly less than their lengths. To get the true
                covariance matrix, the returned sensitivity matrix must be multiplied
                by harmonic mean [3]_ of variance in each observation. Note that
                `weights` are supposed to be inversely proportional to the observation
                variances to get consistent results. For example, if all vectors are
                measured with the same accuracy of 0.01 (`weights` must be all equal),
                then you should multiple the sensitivity matrix by 0.01**2 to get the
                covariance.
        
                Refer to [2]_ for more rigorous discussion of the covariance
                estimation.
        
                References
                ----------
                .. [1] https://en.wikipedia.org/wiki/Kabsch_algorithm
                .. [2] F. Landis Markley,
                        "Attitude determination using vector observations: a fast
                        optimal matrix algorithm", Journal of Astronautical Sciences,
                        Vol. 41, No.2, 1993, pp. 261-280.
                .. [3] https://en.wikipedia.org/wiki/Harmonic_mean
        """
        pass

    def apply(self, vectors, inverse=False): # real signature unknown; restored from __doc__
        """
        Rotation.apply(self, vectors, inverse=False)
        Apply this rotation to a set of vectors.
        
                If the original frame rotates to the final frame by this rotation, then
                its application to a vector can be seen in two ways:
        
                    - As a projection of vector components expressed in the final frame
                      to the original frame.
                    - As the physical rotation of a vector being glued to the original
                      frame as it rotates. In this case the vector components are
                      expressed in the original frame before and after the rotation.
        
                In terms of rotation matricies, this application is the same as
                ``self.as_matrix().dot(vectors)``.
        
                Parameters
                ----------
                vectors : array_like, shape (3,) or (N, 3)
                    Each `vectors[i]` represents a vector in 3D space. A single vector
                    can either be specified with shape `(3, )` or `(1, 3)`. The number
                    of rotations and number of vectors given must follow standard numpy
                    broadcasting rules: either one of them equals unity or they both
                    equal each other.
                inverse : boolean, optional
                    If True then the inverse of the rotation(s) is applied to the input
                    vectors. Default is False.
        
                Returns
                -------
                rotated_vectors : ndarray, shape (3,) or (N, 3)
                    Result of applying rotation on input vectors.
                    Shape depends on the following cases:
        
                        - If object contains a single rotation (as opposed to a stack
                          with a single rotation) and a single vector is specified with
                          shape ``(3,)``, then `rotated_vectors` has shape ``(3,)``.
                        - In all other cases, `rotated_vectors` has shape ``(N, 3)``,
                          where ``N`` is either the number of rotations or vectors.
        
                Examples
                --------
                >>> from scipy.spatial.transform import Rotation as R
                >>> import numpy as np
        
                Single rotation applied on a single vector:
        
                >>> vector = np.array([1, 0, 0])
                >>> r = R.from_rotvec([0, 0, np.pi/2])
                >>> r.as_matrix()
                array([[ 2.22044605e-16, -1.00000000e+00,  0.00000000e+00],
                       [ 1.00000000e+00,  2.22044605e-16,  0.00000000e+00],
                       [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00]])
                >>> r.apply(vector)
                array([2.22044605e-16, 1.00000000e+00, 0.00000000e+00])
                >>> r.apply(vector).shape
                (3,)
        
                Single rotation applied on multiple vectors:
        
                >>> vectors = np.array([
                ... [1, 0, 0],
                ... [1, 2, 3]])
                >>> r = R.from_rotvec([0, 0, np.pi/4])
                >>> r.as_matrix()
                array([[ 0.70710678, -0.70710678,  0.        ],
                       [ 0.70710678,  0.70710678,  0.        ],
                       [ 0.        ,  0.        ,  1.        ]])
                >>> r.apply(vectors)
                array([[ 0.70710678,  0.70710678,  0.        ],
                       [-0.70710678,  2.12132034,  3.        ]])
                >>> r.apply(vectors).shape
                (2, 3)
        
                Multiple rotations on a single vector:
        
                >>> r = R.from_rotvec([[0, 0, np.pi/4], [np.pi/2, 0, 0]])
                >>> vector = np.array([1,2,3])
                >>> r.as_matrix()
                array([[[ 7.07106781e-01, -7.07106781e-01,  0.00000000e+00],
                        [ 7.07106781e-01,  7.07106781e-01,  0.00000000e+00],
                        [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00]],
                       [[ 1.00000000e+00,  0.00000000e+00,  0.00000000e+00],
                        [ 0.00000000e+00,  2.22044605e-16, -1.00000000e+00],
                        [ 0.00000000e+00,  1.00000000e+00,  2.22044605e-16]]])
                >>> r.apply(vector)
                array([[-0.70710678,  2.12132034,  3.        ],
                       [ 1.        , -3.        ,  2.        ]])
                >>> r.apply(vector).shape
                (2, 3)
        
                Multiple rotations on multiple vectors. Each rotation is applied on the
                corresponding vector:
        
                >>> r = R.from_euler('zxy', [
                ... [0, 0, 90],
                ... [45, 30, 60]], degrees=True)
                >>> vectors = [
                ... [1, 2, 3],
                ... [1, 0, -1]]
                >>> r.apply(vectors)
                array([[ 3.        ,  2.        , -1.        ],
                       [-0.09026039,  1.11237244, -0.86860844]])
                >>> r.apply(vectors).shape
                (2, 3)
        
                It is also possible to apply the inverse rotation:
        
                >>> r = R.from_euler('zxy', [
                ... [0, 0, 90],
                ... [45, 30, 60]], degrees=True)
                >>> vectors = [
                ... [1, 2, 3],
                ... [1, 0, -1]]
                >>> r.apply(vectors, inverse=True)
                array([[-3.        ,  2.        ,  1.        ],
                       [ 1.09533535, -0.8365163 ,  0.3169873 ]])
        """
        pass

    def as_euler(self, seq, degrees=False): # real signature unknown; restored from __doc__
        """
        Rotation.as_euler(self, seq, degrees=False)
        Represent as Euler angles.
        
                Any orientation can be expressed as a composition of 3 elementary
                rotations. Once the axis sequence has been chosen, Euler angles define
                the angle of rotation around each respective axis [1]_.
        
                The algorithm from [2]_ has been used to calculate Euler angles for the
                rotation about a given sequence of axes.
        
                Euler angles suffer from the problem of gimbal lock [3]_, where the
                representation loses a degree of freedom and it is not possible to
                determine the first and third angles uniquely. In this case,
                a warning is raised, and the third angle is set to zero. Note however
                that the returned angles still represent the correct rotation.
        
                Parameters
                ----------
                seq : string, length 3
                    3 characters belonging to the set {'X', 'Y', 'Z'} for intrinsic
                    rotations, or {'x', 'y', 'z'} for extrinsic rotations [1]_.
                    Adjacent axes cannot be the same.
                    Extrinsic and intrinsic rotations cannot be mixed in one function
                    call.
                degrees : boolean, optional
                    Returned angles are in degrees if this flag is True, else they are
                    in radians. Default is False.
        
                Returns
                -------
                angles : ndarray, shape (3,) or (N, 3)
                    Shape depends on shape of inputs used to initialize object.
                    The returned angles are in the range:
        
                    - First angle belongs to [-180, 180] degrees (both inclusive)
                    - Third angle belongs to [-180, 180] degrees (both inclusive)
                    - Second angle belongs to:
        
                        - [-90, 90] degrees if all axes are different (like xyz)
                        - [0, 180] degrees if first and third axes are the same
                          (like zxz)
        
                References
                ----------
                .. [1] https://en.wikipedia.org/wiki/Euler_angles#Definition_by_intrinsic_rotations
                .. [2] Malcolm D. Shuster, F. Landis Markley, "General formula for
                       extraction the Euler angles", Journal of guidance, control, and
                       dynamics, vol. 29.1, pp. 215-221. 2006
                .. [3] https://en.wikipedia.org/wiki/Gimbal_lock#In_applied_mathematics
        
                Examples
                --------
                >>> from scipy.spatial.transform import Rotation as R
                >>> import numpy as np
        
                Represent a single rotation:
        
                >>> r = R.from_rotvec([0, 0, np.pi/2])
                >>> r.as_euler('zxy', degrees=True)
                array([90.,  0.,  0.])
                >>> r.as_euler('zxy', degrees=True).shape
                (3,)
        
                Represent a stack of single rotation:
        
                >>> r = R.from_rotvec([[0, 0, np.pi/2]])
                >>> r.as_euler('zxy', degrees=True)
                array([[90.,  0.,  0.]])
                >>> r.as_euler('zxy', degrees=True).shape
                (1, 3)
        
                Represent multiple rotations in a single object:
        
                >>> r = R.from_rotvec([
                ... [0, 0, np.pi/2],
                ... [0, -np.pi/3, 0],
                ... [np.pi/4, 0, 0]])
                >>> r.as_euler('zxy', degrees=True)
                array([[ 90.,   0.,   0.],
                       [  0.,   0., -60.],
                       [  0.,  45.,   0.]])
                >>> r.as_euler('zxy', degrees=True).shape
                (3, 3)
        """
        pass

    def as_matrix(self): # real signature unknown; restored from __doc__
        """
        Rotation.as_matrix(self)
        Represent as rotation matrix.
        
                3D rotations can be represented using rotation matrices, which
                are 3 x 3 real orthogonal matrices with determinant equal to +1 [1]_.
        
                Returns
                -------
                matrix : ndarray, shape (3, 3) or (N, 3, 3)
                    Shape depends on shape of inputs used for initialization.
        
                References
                ----------
                .. [1] https://en.wikipedia.org/wiki/Rotation_matrix#In_three_dimensions
        
                Examples
                --------
                >>> from scipy.spatial.transform import Rotation as R
                >>> import numpy as np
        
                Represent a single rotation:
        
                >>> r = R.from_rotvec([0, 0, np.pi/2])
                >>> r.as_matrix()
                array([[ 2.22044605e-16, -1.00000000e+00,  0.00000000e+00],
                       [ 1.00000000e+00,  2.22044605e-16,  0.00000000e+00],
                       [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00]])
                >>> r.as_matrix().shape
                (3, 3)
        
                Represent a stack with a single rotation:
        
                >>> r = R.from_quat([[1, 1, 0, 0]])
                >>> r.as_matrix()
                array([[[ 0.,  1.,  0.],
                        [ 1.,  0.,  0.],
                        [ 0.,  0., -1.]]])
                >>> r.as_matrix().shape
                (1, 3, 3)
        
                Represent multiple rotations:
        
                >>> r = R.from_rotvec([[np.pi/2, 0, 0], [0, 0, np.pi/2]])
                >>> r.as_matrix()
                array([[[ 1.00000000e+00,  0.00000000e+00,  0.00000000e+00],
                        [ 0.00000000e+00,  2.22044605e-16, -1.00000000e+00],
                        [ 0.00000000e+00,  1.00000000e+00,  2.22044605e-16]],
                       [[ 2.22044605e-16, -1.00000000e+00,  0.00000000e+00],
                        [ 1.00000000e+00,  2.22044605e-16,  0.00000000e+00],
                        [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00]]])
                >>> r.as_matrix().shape
                (2, 3, 3)
        
                Notes
                -----
                This function was called as_dcm before.
        
                .. versionadded:: 1.4.0
        """
        pass

    def as_mrp(self): # real signature unknown; restored from __doc__
        """
        Rotation.as_mrp(self)
        Represent as Modified Rodrigues Parameters (MRPs).
        
                MRPs are a 3 dimensional vector co-directional to the axis of rotation and whose
                magnitude is equal to ``tan(theta / 4)``, where ``theta`` is the angle of rotation
                (in radians) [1]_.
        
                MRPs have a singuarity at 360 degrees which can be avoided by ensuring the angle of
                rotation does not exceed 180 degrees, i.e. switching the direction of the rotation when
                it is past 180 degrees. This function will always return MRPs corresponding to a rotation
                of less than or equal to 180 degrees.
        
                Returns
                -------
                mrps : ndarray, shape (3,) or (N, 3)
                    Shape depends on shape of inputs used for initialization.
        
                References
                ----------
                .. [1] Shuster, M. D. "A Survery of Attitude Representations",
                       The Journal of Astronautical Sciences, Vol. 41, No.4, 1993,
                       pp. 475-476
        
                Examples
                --------
                >>> from scipy.spatial.transform import Rotation as R
                >>> import numpy as np
        
                Represent a single rotation:
        
                >>> r = R.from_rotvec([0, 0, np.pi])
                >>> r.as_mrp()
                array([0.        , 0.        , 1.         ])
                >>> r.as_mrp().shape
                (3,)
        
                Represent a stack with a single rotation:
        
                >>> r = R.from_euler('xyz', [[180, 0, 0]], degrees=True)
                >>> r.as_mrp()
                array([[1.       , 0.        , 0.         ]])
                >>> r.as_mrp().shape
                (1, 3)
        
                Represent multiple rotations:
        
                >>> r = R.from_rotvec([[np.pi/2, 0, 0], [0, 0, np.pi/2]])
                >>> r.as_mrp()
                array([[0.41421356, 0.        , 0.        ],
                       [0.        , 0.        , 0.41421356]])
                >>> r.as_mrp().shape
                (2, 3)
        
                Notes
                -----
        
                .. versionadded:: 1.6.0
        """
        pass

    def as_quat(self): # real signature unknown; restored from __doc__
        """
        Rotation.as_quat(self)
        Represent as quaternions.
        
                Rotations in 3 dimensions can be represented using unit norm
                quaternions [1]_. The mapping from quaternions to rotations is
                two-to-one, i.e. quaternions ``q`` and ``-q``, where ``-q`` simply
                reverses the sign of each component, represent the same spatial
                rotation. The returned value is in scalar-last (x, y, z, w) format.
        
                Returns
                -------
                quat : `numpy.ndarray`, shape (4,) or (N, 4)
                    Shape depends on shape of inputs used for initialization.
        
                References
                ----------
                .. [1] https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation
        
                Examples
                --------
                >>> from scipy.spatial.transform import Rotation as R
                >>> import numpy as np
        
                Represent a single rotation:
        
                >>> r = R.from_matrix([[0, -1, 0],
                ...                    [1, 0, 0],
                ...                    [0, 0, 1]])
                >>> r.as_quat()
                array([0.        , 0.        , 0.70710678, 0.70710678])
                >>> r.as_quat().shape
                (4,)
        
                Represent a stack with a single rotation:
        
                >>> r = R.from_quat([[0, 0, 0, 1]])
                >>> r.as_quat().shape
                (1, 4)
        
                Represent multiple rotations in a single object:
        
                >>> r = R.from_rotvec([[np.pi, 0, 0], [0, 0, np.pi/2]])
                >>> r.as_quat().shape
                (2, 4)
        """
        pass

    def as_rotvec(self, degrees=False): # real signature unknown; restored from __doc__
        """
        Rotation.as_rotvec(self, degrees=False)
        Represent as rotation vectors.
        
                A rotation vector is a 3 dimensional vector which is co-directional to
                the axis of rotation and whose norm gives the angle of rotation [1]_.
        
                Parameters
                ----------
                degrees : boolean, optional
                    Returned magnitudes are in degrees if this flag is True, else they are
                    in radians. Default is False.
        
                    .. versionadded:: 1.7.0
        
                Returns
                -------
                rotvec : ndarray, shape (3,) or (N, 3)
                    Shape depends on shape of inputs used for initialization.
        
                References
                ----------
                .. [1] https://en.wikipedia.org/wiki/Axis%E2%80%93angle_representation#Rotation_vector
        
                Examples
                --------
                >>> from scipy.spatial.transform import Rotation as R
                >>> import numpy as np
        
                Represent a single rotation:
        
                >>> r = R.from_euler('z', 90, degrees=True)
                >>> r.as_rotvec()
                array([0.        , 0.        , 1.57079633])
                >>> r.as_rotvec().shape
                (3,)
        
                Represent a rotation in degrees:
        
                >>> r = R.from_euler('YX', (-90, -90), degrees=True)
                >>> s = r.as_rotvec(degrees=True)
                >>> s
                array([-69.2820323, -69.2820323, -69.2820323])
                >>> np.linalg.norm(s)
                120.00000000000001
        
                Represent a stack with a single rotation:
        
                >>> r = R.from_quat([[0, 0, 1, 1]])
                >>> r.as_rotvec()
                array([[0.        , 0.        , 1.57079633]])
                >>> r.as_rotvec().shape
                (1, 3)
        
                Represent multiple rotations in a single object:
        
                >>> r = R.from_quat([[0, 0, 1, 1], [1, 1, 0, 1]])
                >>> r.as_rotvec()
                array([[0.        , 0.        , 1.57079633],
                       [1.35102172, 1.35102172, 0.        ]])
                >>> r.as_rotvec().shape
                (2, 3)
        """
        pass

    @classmethod
    def concatenate(cls, type_cls, rotations): # real signature unknown; restored from __doc__
        """
        Rotation.concatenate(type cls, rotations)
        Concatenate a sequence of `Rotation` objects.
        
                Parameters
                ----------
                rotations : sequence of `Rotation` objects
                    The rotations to concatenate.
        
                Returns
                -------
                concatenated : `Rotation` instance
                    The concatenated rotations.
        
                Notes
                -----
                .. versionadded:: 1.8.0
        """
        pass

    @classmethod
    def create_group(cls, type_cls, group, axis=None): # real signature unknown; restored from __doc__
        """
        Rotation.create_group(type cls, group, axis=u'Z')
        Create a 3D rotation group.
        
                Parameters
                ----------
                group : string
                    The name of the group. Must be one of 'I', 'O', 'T', 'Dn', 'Cn',
                    where `n` is a positive integer. The groups are:
        
                        * I: Icosahedral group
                        * O: Octahedral group
                        * T: Tetrahedral group
                        * D: Dicyclic group
                        * C: Cyclic group
        
                axis : integer
                    The cyclic rotation axis. Must be one of ['X', 'Y', 'Z'] (or
                    lowercase). Default is 'Z'. Ignored for groups 'I', 'O', and 'T'.
        
                Returns
                -------
                rotation : `Rotation` instance
                    Object containing the elements of the rotation group.
        
                Notes
                -----
                This method generates rotation groups only. The full 3-dimensional
                point groups [PointGroups]_ also contain reflections.
        
                References
                ----------
                .. [PointGroups] `Point groups
                   <https://en.wikipedia.org/wiki/Point_groups_in_three_dimensions>`_
                   on Wikipedia.
        """
        pass

    @classmethod
    def from_euler(cls, type_cls, seq, angles, degrees=False): # real signature unknown; restored from __doc__
        """
        Rotation.from_euler(type cls, seq, angles, degrees=False)
        Initialize from Euler angles.
        
                Rotations in 3-D can be represented by a sequence of 3
                rotations around a sequence of axes. In theory, any three axes spanning
                the 3-D Euclidean space are enough. In practice, the axes of rotation are
                chosen to be the basis vectors.
        
                The three rotations can either be in a global frame of reference
                (extrinsic) or in a body centred frame of reference (intrinsic), which
                is attached to, and moves with, the object under rotation [1]_.
        
                Parameters
                ----------
                seq : string
                    Specifies sequence of axes for rotations. Up to 3 characters
                    belonging to the set {'X', 'Y', 'Z'} for intrinsic rotations, or
                    {'x', 'y', 'z'} for extrinsic rotations. Extrinsic and intrinsic
                    rotations cannot be mixed in one function call.
                angles : float or array_like, shape (N,) or (N, [1 or 2 or 3])
                    Euler angles specified in radians (`degrees` is False) or degrees
                    (`degrees` is True).
                    For a single character `seq`, `angles` can be:
        
                    - a single value
                    - array_like with shape (N,), where each `angle[i]`
                      corresponds to a single rotation
                    - array_like with shape (N, 1), where each `angle[i, 0]`
                      corresponds to a single rotation
        
                    For 2- and 3-character wide `seq`, `angles` can be:
        
                    - array_like with shape (W,) where `W` is the width of
                      `seq`, which corresponds to a single rotation with `W` axes
                    - array_like with shape (N, W) where each `angle[i]`
                      corresponds to a sequence of Euler angles describing a single
                      rotation
        
                degrees : bool, optional
                    If True, then the given angles are assumed to be in degrees.
                    Default is False.
        
                Returns
                -------
                rotation : `Rotation` instance
                    Object containing the rotation represented by the sequence of
                    rotations around given axes with given angles.
        
                References
                ----------
                .. [1] https://en.wikipedia.org/wiki/Euler_angles#Definition_by_intrinsic_rotations
        
                Examples
                --------
                >>> from scipy.spatial.transform import Rotation as R
        
                Initialize a single rotation along a single axis:
        
                >>> r = R.from_euler('x', 90, degrees=True)
                >>> r.as_quat().shape
                (4,)
        
                Initialize a single rotation with a given axis sequence:
        
                >>> r = R.from_euler('zyx', [90, 45, 30], degrees=True)
                >>> r.as_quat().shape
                (4,)
        
                Initialize a stack with a single rotation around a single axis:
        
                >>> r = R.from_euler('x', [90], degrees=True)
                >>> r.as_quat().shape
                (1, 4)
        
                Initialize a stack with a single rotation with an axis sequence:
        
                >>> r = R.from_euler('zyx', [[90, 45, 30]], degrees=True)
                >>> r.as_quat().shape
                (1, 4)
        
                Initialize multiple elementary rotations in one object:
        
                >>> r = R.from_euler('x', [90, 45, 30], degrees=True)
                >>> r.as_quat().shape
                (3, 4)
        
                Initialize multiple rotations in one object:
        
                >>> r = R.from_euler('zyx', [[90, 45, 30], [35, 45, 90]], degrees=True)
                >>> r.as_quat().shape
                (2, 4)
        """
        pass

    @classmethod
    def from_matrix(cls, type_cls, matrix): # real signature unknown; restored from __doc__
        """
        Rotation.from_matrix(type cls, matrix)
        Initialize from rotation matrix.
        
                Rotations in 3 dimensions can be represented with 3 x 3 proper
                orthogonal matrices [1]_. If the input is not proper orthogonal,
                an approximation is created using the method described in [2]_.
        
                Parameters
                ----------
                matrix : array_like, shape (N, 3, 3) or (3, 3)
                    A single matrix or a stack of matrices, where ``matrix[i]`` is
                    the i-th matrix.
        
                Returns
                -------
                rotation : `Rotation` instance
                    Object containing the rotations represented by the rotation
                    matrices.
        
                References
                ----------
                .. [1] https://en.wikipedia.org/wiki/Rotation_matrix#In_three_dimensions
                .. [2] F. Landis Markley, "Unit Quaternion from Rotation Matrix",
                       Journal of guidance, control, and dynamics vol. 31.2, pp.
                       440-442, 2008.
        
                Examples
                --------
                >>> from scipy.spatial.transform import Rotation as R
                >>> import numpy as np
        
                Initialize a single rotation:
        
                >>> r = R.from_matrix([
                ... [0, -1, 0],
                ... [1, 0, 0],
                ... [0, 0, 1]])
                >>> r.as_matrix().shape
                (3, 3)
        
                Initialize multiple rotations in a single object:
        
                >>> r = R.from_matrix([
                ... [
                ...     [0, -1, 0],
                ...     [1, 0, 0],
                ...     [0, 0, 1],
                ... ],
                ... [
                ...     [1, 0, 0],
                ...     [0, 0, -1],
                ...     [0, 1, 0],
                ... ]])
                >>> r.as_matrix().shape
                (2, 3, 3)
        
                If input matrices are not special orthogonal (orthogonal with
                determinant equal to +1), then a special orthogonal estimate is stored:
        
                >>> a = np.array([
                ... [0, -0.5, 0],
                ... [0.5, 0, 0],
                ... [0, 0, 0.5]])
                >>> np.linalg.det(a)
                0.12500000000000003
                >>> r = R.from_matrix(a)
                >>> matrix = r.as_matrix()
                >>> matrix
                array([[-0.38461538, -0.92307692,  0.        ],
                       [ 0.92307692, -0.38461538,  0.        ],
                       [ 0.        ,  0.        ,  1.        ]])
                >>> np.linalg.det(matrix)
                1.0000000000000002
        
                It is also possible to have a stack containing a single rotation:
        
                >>> r = R.from_matrix([[
                ... [0, -1, 0],
                ... [1, 0, 0],
                ... [0, 0, 1]]])
                >>> r.as_matrix()
                array([[[ 0., -1.,  0.],
                        [ 1.,  0.,  0.],
                        [ 0.,  0.,  1.]]])
                >>> r.as_matrix().shape
                (1, 3, 3)
        
                Notes
                -----
                This function was called from_dcm before.
        
                .. versionadded:: 1.4.0
        """
        pass

    @classmethod
    def from_mrp(cls, type_cls, mrp): # real signature unknown; restored from __doc__
        """
        Rotation.from_mrp(type cls, mrp)
        Initialize from Modified Rodrigues Parameters (MRPs).
        
                MRPs are a 3 dimensional vector co-directional to the axis of rotation and whose
                magnitude is equal to ``tan(theta / 4)``, where ``theta`` is the angle of rotation
                (in radians) [1]_.
        
                MRPs have a singuarity at 360 degrees which can be avoided by ensuring the angle of
                rotation does not exceed 180 degrees, i.e. switching the direction of the rotation when
                it is past 180 degrees.
        
                Parameters
                ----------
                mrp : array_like, shape (N, 3) or (3,)
                    A single vector or a stack of vectors, where `mrp[i]` gives
                    the ith set of MRPs.
        
                Returns
                -------
                rotation : `Rotation` instance
                    Object containing the rotations represented by input MRPs.
        
                References
                ----------
                .. [1] Shuster, M. D. "A Survery of Attitude Representations",
                       The Journal of Astronautical Sciences, Vol. 41, No.4, 1993,
                       pp. 475-476
        
                Notes
                -----
        
                .. versionadded:: 1.6.0
        
                Examples
                --------
                >>> from scipy.spatial.transform import Rotation as R
                >>> import numpy as np
        
                Initialize a single rotation:
        
                >>> r = R.from_mrp([0, 0, 1])
                >>> r.as_euler('xyz', degrees=True)
                array([0.        , 0.        , 180.      ])
                >>> r.as_euler('xyz').shape
                (3,)
        
                Initialize multiple rotations in one object:
        
                >>> r = R.from_mrp([
                ... [0, 0, 1],
                ... [1, 0, 0]])
                >>> r.as_euler('xyz', degrees=True)
                array([[0.        , 0.        , 180.      ],
                       [180.0     , 0.        , 0.        ]])
                >>> r.as_euler('xyz').shape
                (2, 3)
        
                It is also possible to have a stack of a single rotation:
        
                >>> r = R.from_mrp([[0, 0, np.pi/2]])
                >>> r.as_euler('xyz').shape
                (1, 3)
        """
        pass

    @classmethod
    def from_quat(cls, type_cls, quat): # real signature unknown; restored from __doc__
        """
        Rotation.from_quat(type cls, quat)
        Initialize from quaternions.
        
                3D rotations can be represented using unit-norm quaternions [1]_.
        
                Parameters
                ----------
                quat : array_like, shape (N, 4) or (4,)
                    Each row is a (possibly non-unit norm) quaternion in scalar-last
                    (x, y, z, w) format. Each quaternion will be normalized to unit
                    norm.
        
                Returns
                -------
                rotation : `Rotation` instance
                    Object containing the rotations represented by input quaternions.
        
                References
                ----------
                .. [1] https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation
        
                Examples
                --------
                >>> from scipy.spatial.transform import Rotation as R
        
                Initialize a single rotation:
        
                >>> r = R.from_quat([1, 0, 0, 0])
                >>> r.as_quat()
                array([1., 0., 0., 0.])
                >>> r.as_quat().shape
                (4,)
        
                Initialize multiple rotations in a single object:
        
                >>> r = R.from_quat([
                ... [1, 0, 0, 0],
                ... [0, 0, 0, 1]
                ... ])
                >>> r.as_quat()
                array([[1., 0., 0., 0.],
                       [0., 0., 0., 1.]])
                >>> r.as_quat().shape
                (2, 4)
        
                It is also possible to have a stack of a single rotation:
        
                >>> r = R.from_quat([[0, 0, 0, 1]])
                >>> r.as_quat()
                array([[0., 0., 0., 1.]])
                >>> r.as_quat().shape
                (1, 4)
        
                Quaternions are normalized before initialization.
        
                >>> r = R.from_quat([0, 0, 1, 1])
                >>> r.as_quat()
                array([0.        , 0.        , 0.70710678, 0.70710678])
        """
        pass

    @classmethod
    def from_rotvec(cls, type_cls, rotvec, degrees=False): # real signature unknown; restored from __doc__
        """
        Rotation.from_rotvec(type cls, rotvec, degrees=False)
        Initialize from rotation vectors.
        
                A rotation vector is a 3 dimensional vector which is co-directional to
                the axis of rotation and whose norm gives the angle of rotation [1]_.
        
                Parameters
                ----------
                rotvec : array_like, shape (N, 3) or (3,)
                    A single vector or a stack of vectors, where `rot_vec[i]` gives
                    the ith rotation vector.
                degrees : bool, optional
                    If True, then the given magnitudes are assumed to be in degrees.
                    Default is False.
        
                    .. versionadded:: 1.7.0
        
                Returns
                -------
                rotation : `Rotation` instance
                    Object containing the rotations represented by input rotation
                    vectors.
        
                References
                ----------
                .. [1] https://en.wikipedia.org/wiki/Axis%E2%80%93angle_representation#Rotation_vector
        
                Examples
                --------
                >>> from scipy.spatial.transform import Rotation as R
                >>> import numpy as np
        
                Initialize a single rotation:
        
                >>> r = R.from_rotvec(np.pi/2 * np.array([0, 0, 1]))
                >>> r.as_rotvec()
                array([0.        , 0.        , 1.57079633])
                >>> r.as_rotvec().shape
                (3,)
        
                Initialize a rotation in degrees, and view it in degrees:
        
                >>> r = R.from_rotvec(45 * np.array([0, 1, 0]), degrees=True)
                >>> r.as_rotvec(degrees=True)
                array([ 0., 45.,  0.])
        
                Initialize multiple rotations in one object:
        
                >>> r = R.from_rotvec([
                ... [0, 0, np.pi/2],
                ... [np.pi/2, 0, 0]])
                >>> r.as_rotvec()
                array([[0.        , 0.        , 1.57079633],
                       [1.57079633, 0.        , 0.        ]])
                >>> r.as_rotvec().shape
                (2, 3)
        
                It is also possible to have a stack of a single rotaton:
        
                >>> r = R.from_rotvec([[0, 0, np.pi/2]])
                >>> r.as_rotvec().shape
                (1, 3)
        """
        pass

    @classmethod
    def identity(cls, type_cls, num=None): # real signature unknown; restored from __doc__
        """
        Rotation.identity(type cls, num=None)
        Get identity rotation(s).
        
                Composition with the identity rotation has no effect.
        
                Parameters
                ----------
                num : int or None, optional
                    Number of identity rotations to generate. If None (default), then a
                    single rotation is generated.
        
                Returns
                -------
                identity : Rotation object
                    The identity rotation.
        """
        pass

    def inv(self): # real signature unknown; restored from __doc__
        """
        Rotation.inv(self)
        Invert this rotation.
        
                Composition of a rotation with its inverse results in an identity
                transformation.
        
                Returns
                -------
                inverse : `Rotation` instance
                    Object containing inverse of the rotations in the current instance.
        
                Examples
                --------
                >>> from scipy.spatial.transform import Rotation as R
                >>> import numpy as np
        
                Inverting a single rotation:
        
                >>> p = R.from_euler('z', 45, degrees=True)
                >>> q = p.inv()
                >>> q.as_euler('zyx', degrees=True)
                array([-45.,   0.,   0.])
        
                Inverting multiple rotations:
        
                >>> p = R.from_rotvec([[0, 0, np.pi/3], [-np.pi/4, 0, 0]])
                >>> q = p.inv()
                >>> q.as_rotvec()
                array([[-0.        , -0.        , -1.04719755],
                       [ 0.78539816, -0.        , -0.        ]])
        """
        pass

    def magnitude(self): # real signature unknown; restored from __doc__
        """
        Rotation.magnitude(self)
        Get the magnitude(s) of the rotation(s).
        
                Returns
                -------
                magnitude : ndarray or float
                    Angle(s) in radians, float if object contains a single rotation
                    and ndarray if object contains multiple rotations.
        
                Examples
                --------
                >>> from scipy.spatial.transform import Rotation as R
                >>> import numpy as np
                >>> r = R.from_quat(np.eye(4))
                >>> r.magnitude()
                array([3.14159265, 3.14159265, 3.14159265, 0.        ])
        
                Magnitude of a single rotation:
        
                >>> r[0].magnitude()
                3.141592653589793
        """
        pass

    def mean(self, weights=None): # real signature unknown; restored from __doc__
        """
        Rotation.mean(self, weights=None)
        Get the mean of the rotations.
        
                Parameters
                ----------
                weights : array_like shape (N,), optional
                    Weights describing the relative importance of the rotations. If
                    None (default), then all values in `weights` are assumed to be
                    equal.
        
                Returns
                -------
                mean : `Rotation` instance
                    Object containing the mean of the rotations in the current
                    instance.
        
                Notes
                -----
                The mean used is the chordal L2 mean (also called the projected or
                induced arithmetic mean). If ``p`` is a set of rotations with mean
                ``m``, then ``m`` is the rotation which minimizes
                ``(weights[:, None, None] * (p.as_matrix() - m.as_matrix())**2).sum()``.
        
                Examples
                --------
                >>> from scipy.spatial.transform import Rotation as R
                >>> r = R.from_euler('zyx', [[0, 0, 0],
                ...                          [1, 0, 0],
                ...                          [0, 1, 0],
                ...                          [0, 0, 1]], degrees=True)
                >>> r.mean().as_euler('zyx', degrees=True)
                array([0.24945696, 0.25054542, 0.24945696])
        """
        pass

    @classmethod
    def random(cls, type_cls, num=None, random_state=None): # real signature unknown; restored from __doc__
        """
        Rotation.random(type cls, num=None, random_state=None)
        Generate uniformly distributed rotations.
        
                Parameters
                ----------
                num : int or None, optional
                    Number of random rotations to generate. If None (default), then a
                    single rotation is generated.
                random_state : {None, int, `numpy.random.Generator`,
                                `numpy.random.RandomState`}, optional
        
                    If `seed` is None (or `np.random`), the `numpy.random.RandomState`
                    singleton is used.
                    If `seed` is an int, a new ``RandomState`` instance is used,
                    seeded with `seed`.
                    If `seed` is already a ``Generator`` or ``RandomState`` instance
                    then that instance is used.
        
                Returns
                -------
                random_rotation : `Rotation` instance
                    Contains a single rotation if `num` is None. Otherwise contains a
                    stack of `num` rotations.
        
                Notes
                -----
                This function is optimized for efficiently sampling random rotation
                matrices in three dimensions. For generating random rotation matrices
                in higher dimensions, see `scipy.stats.special_ortho_group`.
        
                Examples
                --------
                >>> from scipy.spatial.transform import Rotation as R
        
                Sample a single rotation:
        
                >>> R.random().as_euler('zxy', degrees=True)
                array([-110.5976185 ,   55.32758512,   76.3289269 ])  # random
        
                Sample a stack of rotations:
        
                >>> R.random(5).as_euler('zxy', degrees=True)
                array([[-110.5976185 ,   55.32758512,   76.3289269 ],  # random
                       [ -91.59132005,  -14.3629884 ,  -93.91933182],
                       [  25.23835501,   45.02035145, -121.67867086],
                       [ -51.51414184,  -15.29022692, -172.46870023],
                       [ -81.63376847,  -27.39521579,    2.60408416]])
        
                See Also
                --------
                scipy.stats.special_ortho_group
        """
        pass

    def reduce(self, left=None, right=None, return_indices=False): # real signature unknown; restored from __doc__
        """
        Rotation.reduce(self, left=None, right=None, return_indices=False)
        Reduce this rotation with the provided rotation groups.
        
                Reduction of a rotation ``p`` is a transformation of the form
                ``q = l * p * r``, where ``l`` and ``r`` are chosen from `left` and
                `right` respectively, such that rotation ``q`` has the smallest
                magnitude.
        
                If `left` and `right` are rotation groups representing symmetries of
                two objects rotated by ``p``, then ``q`` is the rotation of the
                smallest magnitude to align these objects considering their symmetries.
        
                Parameters
                ----------
                left : `Rotation` instance, optional
                    Object containing the left rotation(s). Default value (None)
                    corresponds to the identity rotation.
                right : `Rotation` instance, optional
                    Object containing the right rotation(s). Default value (None)
                    corresponds to the identity rotation.
                return_indices : bool, optional
                    Whether to return the indices of the rotations from `left` and
                    `right` used for reduction.
        
                Returns
                -------
                reduced : `Rotation` instance
                    Object containing reduced rotations.
                left_best, right_best: integer ndarray
                    Indices of elements from `left` and `right` used for reduction.
        """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """
        Extract rotation(s) at given index(es) from object.
        
                Create a new `Rotation` instance containing a subset of rotations
                stored in this object.
        
                Parameters
                ----------
                indexer : index, slice, or index array
                    Specifies which rotation(s) to extract. A single indexer must be
                    specified, i.e. as if indexing a 1 dimensional array or list.
        
                Returns
                -------
                rotation : `Rotation` instance
                    Contains
                        - a single rotation, if `indexer` is a single index
                        - a stack of rotation(s), if `indexer` is a slice, or and index
                          array.
        
                Raises
                ------
                TypeError if the instance was created as a single rotation.
        
                Examples
                --------
                >>> from scipy.spatial.transform import Rotation as R
                >>> r = R.from_quat([
                ... [1, 1, 0, 0],
                ... [0, 1, 0, 1],
                ... [1, 1, -1, 0]])
                >>> r.as_quat()
                array([[ 0.70710678,  0.70710678,  0.        ,  0.        ],
                       [ 0.        ,  0.70710678,  0.        ,  0.70710678],
                       [ 0.57735027,  0.57735027, -0.57735027,  0.        ]])
        
                Indexing using a single index:
        
                >>> p = r[0]
                >>> p.as_quat()
                array([0.70710678, 0.70710678, 0.        , 0.        ])
        
                Array slicing:
        
                >>> q = r[1:3]
                >>> q.as_quat()
                array([[ 0.        ,  0.70710678,  0.        ,  0.70710678],
                       [ 0.57735027,  0.57735027, -0.57735027,  0.        ]])
        """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """
        Number of rotations contained in this object.
        
                Multiple rotations can be stored in a single instance.
        
                Returns
                -------
                length : int
                    Number of rotations stored in object.
        
                Raises
                ------
                TypeError if the instance was created as a single rotation.
        """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """
        Compose this rotation with the other.
        
                If `p` and `q` are two rotations, then the composition of 'q followed
                by p' is equivalent to `p * q`. In terms of rotation matrices,
                the composition can be expressed as
                ``p.as_matrix().dot(q.as_matrix())``.
        
                Parameters
                ----------
                other : `Rotation` instance
                    Object containing the rotations to be composed with this one. Note
                    that rotation compositions are not commutative, so ``p * q`` is
                    different from ``q * p``.
        
                Returns
                -------
                composition : `Rotation` instance
                    This function supports composition of multiple rotations at a time.
                    The following cases are possible:
        
                    - Either ``p`` or ``q`` contains a single rotation. In this case
                      `composition` contains the result of composing each rotation in
                      the other object with the single rotation.
                    - Both ``p`` and ``q`` contain ``N`` rotations. In this case each
                      rotation ``p[i]`` is composed with the corresponding rotation
                      ``q[i]`` and `output` contains ``N`` rotations.
        
                Examples
                --------
                >>> from scipy.spatial.transform import Rotation as R
                >>> import numpy as np
        
                Composition of two single rotations:
        
                >>> p = R.from_quat([0, 0, 1, 1])
                >>> q = R.from_quat([1, 0, 0, 1])
                >>> p.as_matrix()
                array([[ 0., -1.,  0.],
                       [ 1.,  0.,  0.],
                       [ 0.,  0.,  1.]])
                >>> q.as_matrix()
                array([[ 1.,  0.,  0.],
                       [ 0.,  0., -1.],
                       [ 0.,  1.,  0.]])
                >>> r = p * q
                >>> r.as_matrix()
                array([[0., 0., 1.],
                       [1., 0., 0.],
                       [0., 1., 0.]])
        
                Composition of two objects containing equal number of rotations:
        
                >>> p = R.from_quat([[0, 0, 1, 1], [1, 0, 0, 1]])
                >>> q = R.from_rotvec([[np.pi/4, 0, 0], [-np.pi/4, 0, np.pi/4]])
                >>> p.as_quat()
                array([[0.        , 0.        , 0.70710678, 0.70710678],
                       [0.70710678, 0.        , 0.        , 0.70710678]])
                >>> q.as_quat()
                array([[ 0.38268343,  0.        ,  0.        ,  0.92387953],
                       [-0.37282173,  0.        ,  0.37282173,  0.84971049]])
                >>> r = p * q
                >>> r.as_quat()
                array([[ 0.27059805,  0.27059805,  0.65328148,  0.65328148],
                       [ 0.33721128, -0.26362477,  0.26362477,  0.86446082]])
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """
        Set rotation(s) at given index(es) from object.
        
                Parameters
                ----------
                indexer : index, slice, or index array
                    Specifies which rotation(s) to replace. A single indexer must be
                    specified, i.e. as if indexing a 1 dimensional array or list.
        
                value : `Rotation` instance
                    The rotations to set.
        
                Raises
                ------
                TypeError if the instance was created as a single rotation.
        
                Notes
                -----
        
                .. versionadded:: 1.8.0
        """
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    single = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether this instance represents a single rotation."""



class Slerp(object):
    """
    Spherical Linear Interpolation of Rotations.
    
        The interpolation between consecutive rotations is performed as a rotation
        around a fixed axis with a constant angular velocity [1]_. This ensures
        that the interpolated rotations follow the shortest path between initial
        and final orientations.
    
        Parameters
        ----------
        times : array_like, shape (N,)
            Times of the known rotations. At least 2 times must be specified.
        rotations : `Rotation` instance
            Rotations to perform the interpolation between. Must contain N
            rotations.
    
        Methods
        -------
        __call__
    
        See Also
        --------
        Rotation
    
        Notes
        -----
        .. versionadded:: 1.2.0
    
        References
        ----------
        .. [1] https://en.wikipedia.org/wiki/Slerp#Quaternion_Slerp
    
        Examples
        --------
        >>> from scipy.spatial.transform import Rotation as R
        >>> from scipy.spatial.transform import Slerp
    
        Setup the fixed keyframe rotations and times:
    
        >>> key_rots = R.random(5, random_state=2342345)
        >>> key_times = [0, 1, 2, 3, 4]
    
        Create the interpolator object:
    
        >>> slerp = Slerp(key_times, key_rots)
    
        Interpolate the rotations at the given times:
    
        >>> times = [0, 0.5, 0.25, 1, 1.5, 2, 2.75, 3, 3.25, 3.60, 4]
        >>> interp_rots = slerp(times)
    
        The keyframe rotations expressed as Euler angles:
    
        >>> key_rots.as_euler('xyz', degrees=True)
        array([[ 14.31443779, -27.50095894,  -3.7275787 ],
               [ -1.79924227, -24.69421529, 164.57701743],
               [146.15020772,  43.22849451, -31.34891088],
               [ 46.39959442,  11.62126073, -45.99719267],
               [-88.94647804, -49.64400082, -65.80546984]])
    
        The interpolated rotations expressed as Euler angles. These agree with the
        keyframe rotations at both endpoints of the range of keyframe times.
    
        >>> interp_rots.as_euler('xyz', degrees=True)
        array([[  14.31443779,  -27.50095894,   -3.7275787 ],
               [   4.74588574,  -32.44683966,   81.25139984],
               [  10.71094749,  -31.56690154,   38.06896408],
               [  -1.79924227,  -24.69421529,  164.57701743],
               [  11.72796022,   51.64207311, -171.7374683 ],
               [ 146.15020772,   43.22849451,  -31.34891088],
               [  68.10921869,   20.67625074,  -48.74886034],
               [  46.39959442,   11.62126073,  -45.99719267],
               [  12.35552615,    4.21525086,  -64.89288124],
               [ -30.08117143,  -19.90769513,  -78.98121326],
               [ -88.94647804,  -49.64400082,  -65.80546984]])
    """
    def __call__(self, *args, **kwargs): # real signature unknown
        """
        Interpolate rotations.
        
                Compute the interpolated rotations at the given `times`.
        
                Parameters
                ----------
                times : array_like
                    Times to compute the interpolations at. Can be a scalar or
                    1-dimensional.
        
                Returns
                -------
                interpolated_rotation : `Rotation` instance
                    Object containing the rotations computed at given `times`.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'scipy.spatial.transform._rotation\', \'__doc__\': "Spherical Linear Interpolation of Rotations.\\n\\n    The interpolation between consecutive rotations is performed as a rotation\\n    around a fixed axis with a constant angular velocity [1]_. This ensures\\n    that the interpolated rotations follow the shortest path between initial\\n    and final orientations.\\n\\n    Parameters\\n    ----------\\n    times : array_like, shape (N,)\\n        Times of the known rotations. At least 2 times must be specified.\\n    rotations : `Rotation` instance\\n        Rotations to perform the interpolation between. Must contain N\\n        rotations.\\n\\n    Methods\\n    -------\\n    __call__\\n\\n    See Also\\n    --------\\n    Rotation\\n\\n    Notes\\n    -----\\n    .. versionadded:: 1.2.0\\n\\n    References\\n    ----------\\n    .. [1] https://en.wikipedia.org/wiki/Slerp#Quaternion_Slerp\\n\\n    Examples\\n    --------\\n    >>> from scipy.spatial.transform import Rotation as R\\n    >>> from scipy.spatial.transform import Slerp\\n\\n    Setup the fixed keyframe rotations and times:\\n\\n    >>> key_rots = R.random(5, random_state=2342345)\\n    >>> key_times = [0, 1, 2, 3, 4]\\n\\n    Create the interpolator object:\\n\\n    >>> slerp = Slerp(key_times, key_rots)\\n\\n    Interpolate the rotations at the given times:\\n\\n    >>> times = [0, 0.5, 0.25, 1, 1.5, 2, 2.75, 3, 3.25, 3.60, 4]\\n    >>> interp_rots = slerp(times)\\n\\n    The keyframe rotations expressed as Euler angles:\\n\\n    >>> key_rots.as_euler(\'xyz\', degrees=True)\\n    array([[ 14.31443779, -27.50095894,  -3.7275787 ],\\n           [ -1.79924227, -24.69421529, 164.57701743],\\n           [146.15020772,  43.22849451, -31.34891088],\\n           [ 46.39959442,  11.62126073, -45.99719267],\\n           [-88.94647804, -49.64400082, -65.80546984]])\\n\\n    The interpolated rotations expressed as Euler angles. These agree with the\\n    keyframe rotations at both endpoints of the range of keyframe times.\\n\\n    >>> interp_rots.as_euler(\'xyz\', degrees=True)\\n    array([[  14.31443779,  -27.50095894,   -3.7275787 ],\\n           [   4.74588574,  -32.44683966,   81.25139984],\\n           [  10.71094749,  -31.56690154,   38.06896408],\\n           [  -1.79924227,  -24.69421529,  164.57701743],\\n           [  11.72796022,   51.64207311, -171.7374683 ],\\n           [ 146.15020772,   43.22849451,  -31.34891088],\\n           [  68.10921869,   20.67625074,  -48.74886034],\\n           [  46.39959442,   11.62126073,  -45.99719267],\\n           [  12.35552615,    4.21525086,  -64.89288124],\\n           [ -30.08117143,  -19.90769513,  -78.98121326],\\n           [ -88.94647804,  -49.64400082,  -65.80546984]])\\n\\n    ", \'__init__\': <cyfunction Slerp.__init__ at 0xffff92eaea00>, \'__call__\': <cyfunction Slerp.__call__ at 0xffff92eaec70>, \'__dict__\': <attribute \'__dict__\' of \'Slerp\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'Slerp\' objects>})'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9294e8e0>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.spatial.transform._rotation', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9294e8e0>, origin='/.venv/lib/python3.8/site-packages/scipy/spatial/transform/_rotation.cpython-38-aarch64-linux-gnu.so')"

__test__ = {
    'Rotation.__getitem__ (line 2135)': 'Extract rotation(s) at given index(es) from object.\n\n        Create a new `Rotation` instance containing a subset of rotations\n        stored in this object.\n\n        Parameters\n        ----------\n        indexer : index, slice, or index array\n            Specifies which rotation(s) to extract. A single indexer must be\n            specified, i.e. as if indexing a 1 dimensional array or list.\n\n        Returns\n        -------\n        rotation : `Rotation` instance\n            Contains\n                - a single rotation, if `indexer` is a single index\n                - a stack of rotation(s), if `indexer` is a slice, or and index\n                  array.\n\n        Raises\n        ------\n        TypeError if the instance was created as a single rotation.\n\n        Examples\n        --------\n        >>> from scipy.spatial.transform import Rotation as R\n        >>> r = R.from_quat([\n        ... [1, 1, 0, 0],\n        ... [0, 1, 0, 1],\n        ... [1, 1, -1, 0]])\n        >>> r.as_quat()\n        array([[ 0.70710678,  0.70710678,  0.        ,  0.        ],\n               [ 0.        ,  0.70710678,  0.        ,  0.70710678],\n               [ 0.57735027,  0.57735027, -0.57735027,  0.        ]])\n\n        Indexing using a single index:\n\n        >>> p = r[0]\n        >>> p.as_quat()\n        array([0.70710678, 0.70710678, 0.        , 0.        ])\n\n        Array slicing:\n\n        >>> q = r[1:3]\n        >>> q.as_quat()\n        array([[ 0.        ,  0.70710678,  0.        ,  0.70710678],\n               [ 0.57735027,  0.57735027, -0.57735027,  0.        ]])\n\n        ',
    'Rotation.__mul__ (line 1788)': "Compose this rotation with the other.\n\n        If `p` and `q` are two rotations, then the composition of 'q followed\n        by p' is equivalent to `p * q`. In terms of rotation matrices,\n        the composition can be expressed as\n        ``p.as_matrix().dot(q.as_matrix())``.\n\n        Parameters\n        ----------\n        other : `Rotation` instance\n            Object containing the rotations to be composed with this one. Note\n            that rotation compositions are not commutative, so ``p * q`` is\n            different from ``q * p``.\n\n        Returns\n        -------\n        composition : `Rotation` instance\n            This function supports composition of multiple rotations at a time.\n            The following cases are possible:\n\n            - Either ``p`` or ``q`` contains a single rotation. In this case\n              `composition` contains the result of composing each rotation in\n              the other object with the single rotation.\n            - Both ``p`` and ``q`` contain ``N`` rotations. In this case each\n              rotation ``p[i]`` is composed with the corresponding rotation\n              ``q[i]`` and `output` contains ``N`` rotations.\n\n        Examples\n        --------\n        >>> from scipy.spatial.transform import Rotation as R\n        >>> import numpy as np\n\n        Composition of two single rotations:\n\n        >>> p = R.from_quat([0, 0, 1, 1])\n        >>> q = R.from_quat([1, 0, 0, 1])\n        >>> p.as_matrix()\n        array([[ 0., -1.,  0.],\n               [ 1.,  0.,  0.],\n               [ 0.,  0.,  1.]])\n        >>> q.as_matrix()\n        array([[ 1.,  0.,  0.],\n               [ 0.,  0., -1.],\n               [ 0.,  1.,  0.]])\n        >>> r = p * q\n        >>> r.as_matrix()\n        array([[0., 0., 1.],\n               [1., 0., 0.],\n               [0., 1., 0.]])\n\n        Composition of two objects containing equal number of rotations:\n\n        >>> p = R.from_quat([[0, 0, 1, 1], [1, 0, 0, 1]])\n        >>> q = R.from_rotvec([[np.pi/4, 0, 0], [-np.pi/4, 0, np.pi/4]])\n        >>> p.as_quat()\n        array([[0.        , 0.        , 0.70710678, 0.70710678],\n               [0.70710678, 0.        , 0.        , 0.70710678]])\n        >>> q.as_quat()\n        array([[ 0.38268343,  0.        ,  0.        ,  0.92387953],\n               [-0.37282173,  0.        ,  0.37282173,  0.84971049]])\n        >>> r = p * q\n        >>> r.as_quat()\n        array([[ 0.27059805,  0.27059805,  0.65328148,  0.65328148],\n               [ 0.33721128, -0.26362477,  0.26362477,  0.86446082]])\n\n        ",
    'Rotation.apply (line 1636)': "Apply this rotation to a set of vectors.\n\n        If the original frame rotates to the final frame by this rotation, then\n        its application to a vector can be seen in two ways:\n\n            - As a projection of vector components expressed in the final frame\n              to the original frame.\n            - As the physical rotation of a vector being glued to the original\n              frame as it rotates. In this case the vector components are\n              expressed in the original frame before and after the rotation.\n\n        In terms of rotation matricies, this application is the same as\n        ``self.as_matrix().dot(vectors)``.\n\n        Parameters\n        ----------\n        vectors : array_like, shape (3,) or (N, 3)\n            Each `vectors[i]` represents a vector in 3D space. A single vector\n            can either be specified with shape `(3, )` or `(1, 3)`. The number\n            of rotations and number of vectors given must follow standard numpy\n            broadcasting rules: either one of them equals unity or they both\n            equal each other.\n        inverse : boolean, optional\n            If True then the inverse of the rotation(s) is applied to the input\n            vectors. Default is False.\n\n        Returns\n        -------\n        rotated_vectors : ndarray, shape (3,) or (N, 3)\n            Result of applying rotation on input vectors.\n            Shape depends on the following cases:\n\n                - If object contains a single rotation (as opposed to a stack\n                  with a single rotation) and a single vector is specified with\n                  shape ``(3,)``, then `rotated_vectors` has shape ``(3,)``.\n                - In all other cases, `rotated_vectors` has shape ``(N, 3)``,\n                  where ``N`` is either the number of rotations or vectors.\n\n        Examples\n        --------\n        >>> from scipy.spatial.transform import Rotation as R\n        >>> import numpy as np\n\n        Single rotation applied on a single vector:\n\n        >>> vector = np.array([1, 0, 0])\n        >>> r = R.from_rotvec([0, 0, np.pi/2])\n        >>> r.as_matrix()\n        array([[ 2.22044605e-16, -1.00000000e+00,  0.00000000e+00],\n               [ 1.00000000e+00,  2.22044605e-16,  0.00000000e+00],\n               [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00]])\n        >>> r.apply(vector)\n        array([2.22044605e-16, 1.00000000e+00, 0.00000000e+00])\n        >>> r.apply(vector).shape\n        (3,)\n\n        Single rotation applied on multiple vectors:\n\n        >>> vectors = np.array([\n        ... [1, 0, 0],\n        ... [1, 2, 3]])\n        >>> r = R.from_rotvec([0, 0, np.pi/4])\n        >>> r.as_matrix()\n        array([[ 0.70710678, -0.70710678,  0.        ],\n               [ 0.70710678,  0.70710678,  0.        ],\n               [ 0.        ,  0.        ,  1.        ]])\n        >>> r.apply(vectors)\n        array([[ 0.70710678,  0.70710678,  0.        ],\n               [-0.70710678,  2.12132034,  3.        ]])\n        >>> r.apply(vectors).shape\n        (2, 3)\n\n        Multiple rotations on a single vector:\n\n        >>> r = R.from_rotvec([[0, 0, np.pi/4], [np.pi/2, 0, 0]])\n        >>> vector = np.array([1,2,3])\n        >>> r.as_matrix()\n        array([[[ 7.07106781e-01, -7.07106781e-01,  0.00000000e+00],\n                [ 7.07106781e-01,  7.07106781e-01,  0.00000000e+00],\n                [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00]],\n               [[ 1.00000000e+00,  0.00000000e+00,  0.00000000e+00],\n                [ 0.00000000e+00,  2.22044605e-16, -1.00000000e+00],\n                [ 0.00000000e+00,  1.00000000e+00,  2.22044605e-16]]])\n        >>> r.apply(vector)\n        array([[-0.70710678,  2.12132034,  3.        ],\n               [ 1.        , -3.        ,  2.        ]])\n        >>> r.apply(vector).shape\n        (2, 3)\n\n        Multiple rotations on multiple vectors. Each rotation is applied on the\n        corresponding vector:\n\n        >>> r = R.from_euler('zxy', [\n        ... [0, 0, 90],\n        ... [45, 30, 60]], degrees=True)\n        >>> vectors = [\n        ... [1, 2, 3],\n        ... [1, 0, -1]]\n        >>> r.apply(vectors)\n        array([[ 3.        ,  2.        , -1.        ],\n               [-0.09026039,  1.11237244, -0.86860844]])\n        >>> r.apply(vectors).shape\n        (2, 3)\n\n        It is also possible to apply the inverse rotation:\n\n        >>> r = R.from_euler('zxy', [\n        ... [0, 0, 90],\n        ... [45, 30, 60]], degrees=True)\n        >>> vectors = [\n        ... [1, 2, 3],\n        ... [1, 0, -1]]\n        >>> r.apply(vectors, inverse=True)\n        array([[-3.        ,  2.        ,  1.        ],\n               [ 1.09533535, -0.8365163 ,  0.3169873 ]])\n\n        ",
    'Rotation.as_euler (line 1420)': 'Represent as Euler angles.\n\n        Any orientation can be expressed as a composition of 3 elementary\n        rotations. Once the axis sequence has been chosen, Euler angles define\n        the angle of rotation around each respective axis [1]_.\n\n        The algorithm from [2]_ has been used to calculate Euler angles for the\n        rotation about a given sequence of axes.\n\n        Euler angles suffer from the problem of gimbal lock [3]_, where the\n        representation loses a degree of freedom and it is not possible to\n        determine the first and third angles uniquely. In this case,\n        a warning is raised, and the third angle is set to zero. Note however\n        that the returned angles still represent the correct rotation.\n\n        Parameters\n        ----------\n        seq : string, length 3\n            3 characters belonging to the set {\'X\', \'Y\', \'Z\'} for intrinsic\n            rotations, or {\'x\', \'y\', \'z\'} for extrinsic rotations [1]_.\n            Adjacent axes cannot be the same.\n            Extrinsic and intrinsic rotations cannot be mixed in one function\n            call.\n        degrees : boolean, optional\n            Returned angles are in degrees if this flag is True, else they are\n            in radians. Default is False.\n\n        Returns\n        -------\n        angles : ndarray, shape (3,) or (N, 3)\n            Shape depends on shape of inputs used to initialize object.\n            The returned angles are in the range:\n\n            - First angle belongs to [-180, 180] degrees (both inclusive)\n            - Third angle belongs to [-180, 180] degrees (both inclusive)\n            - Second angle belongs to:\n\n                - [-90, 90] degrees if all axes are different (like xyz)\n                - [0, 180] degrees if first and third axes are the same\n                  (like zxz)\n\n        References\n        ----------\n        .. [1] https://en.wikipedia.org/wiki/Euler_angles#Definition_by_intrinsic_rotations\n        .. [2] Malcolm D. Shuster, F. Landis Markley, "General formula for\n               extraction the Euler angles", Journal of guidance, control, and\n               dynamics, vol. 29.1, pp. 215-221. 2006\n        .. [3] https://en.wikipedia.org/wiki/Gimbal_lock#In_applied_mathematics\n\n        Examples\n        --------\n        >>> from scipy.spatial.transform import Rotation as R\n        >>> import numpy as np\n\n        Represent a single rotation:\n\n        >>> r = R.from_rotvec([0, 0, np.pi/2])\n        >>> r.as_euler(\'zxy\', degrees=True)\n        array([90.,  0.,  0.])\n        >>> r.as_euler(\'zxy\', degrees=True).shape\n        (3,)\n\n        Represent a stack of single rotation:\n\n        >>> r = R.from_rotvec([[0, 0, np.pi/2]])\n        >>> r.as_euler(\'zxy\', degrees=True)\n        array([[90.,  0.,  0.]])\n        >>> r.as_euler(\'zxy\', degrees=True).shape\n        (1, 3)\n\n        Represent multiple rotations in a single object:\n\n        >>> r = R.from_rotvec([\n        ... [0, 0, np.pi/2],\n        ... [0, -np.pi/3, 0],\n        ... [np.pi/4, 0, 0]])\n        >>> r.as_euler(\'zxy\', degrees=True)\n        array([[ 90.,   0.,   0.],\n               [  0.,   0., -60.],\n               [  0.,  45.,   0.]])\n        >>> r.as_euler(\'zxy\', degrees=True).shape\n        (3, 3)\n\n        ',
    'Rotation.as_matrix (line 1217)': 'Represent as rotation matrix.\n\n        3D rotations can be represented using rotation matrices, which\n        are 3 x 3 real orthogonal matrices with determinant equal to +1 [1]_.\n\n        Returns\n        -------\n        matrix : ndarray, shape (3, 3) or (N, 3, 3)\n            Shape depends on shape of inputs used for initialization.\n\n        References\n        ----------\n        .. [1] https://en.wikipedia.org/wiki/Rotation_matrix#In_three_dimensions\n\n        Examples\n        --------\n        >>> from scipy.spatial.transform import Rotation as R\n        >>> import numpy as np\n\n        Represent a single rotation:\n\n        >>> r = R.from_rotvec([0, 0, np.pi/2])\n        >>> r.as_matrix()\n        array([[ 2.22044605e-16, -1.00000000e+00,  0.00000000e+00],\n               [ 1.00000000e+00,  2.22044605e-16,  0.00000000e+00],\n               [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00]])\n        >>> r.as_matrix().shape\n        (3, 3)\n\n        Represent a stack with a single rotation:\n\n        >>> r = R.from_quat([[1, 1, 0, 0]])\n        >>> r.as_matrix()\n        array([[[ 0.,  1.,  0.],\n                [ 1.,  0.,  0.],\n                [ 0.,  0., -1.]]])\n        >>> r.as_matrix().shape\n        (1, 3, 3)\n\n        Represent multiple rotations:\n\n        >>> r = R.from_rotvec([[np.pi/2, 0, 0], [0, 0, np.pi/2]])\n        >>> r.as_matrix()\n        array([[[ 1.00000000e+00,  0.00000000e+00,  0.00000000e+00],\n                [ 0.00000000e+00,  2.22044605e-16, -1.00000000e+00],\n                [ 0.00000000e+00,  1.00000000e+00,  2.22044605e-16]],\n               [[ 2.22044605e-16, -1.00000000e+00,  0.00000000e+00],\n                [ 1.00000000e+00,  2.22044605e-16,  0.00000000e+00],\n                [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00]]])\n        >>> r.as_matrix().shape\n        (2, 3, 3)\n\n        Notes\n        -----\n        This function was called as_dcm before.\n\n        .. versionadded:: 1.4.0\n        ',
    'Rotation.as_mrp (line 1532)': 'Represent as Modified Rodrigues Parameters (MRPs).\n\n        MRPs are a 3 dimensional vector co-directional to the axis of rotation and whose\n        magnitude is equal to ``tan(theta / 4)``, where ``theta`` is the angle of rotation\n        (in radians) [1]_.\n\n        MRPs have a singuarity at 360 degrees which can be avoided by ensuring the angle of\n        rotation does not exceed 180 degrees, i.e. switching the direction of the rotation when\n        it is past 180 degrees. This function will always return MRPs corresponding to a rotation\n        of less than or equal to 180 degrees.\n\n        Returns\n        -------\n        mrps : ndarray, shape (3,) or (N, 3)\n            Shape depends on shape of inputs used for initialization.\n\n        References\n        ----------\n        .. [1] Shuster, M. D. "A Survery of Attitude Representations",\n               The Journal of Astronautical Sciences, Vol. 41, No.4, 1993,\n               pp. 475-476\n\n        Examples\n        --------\n        >>> from scipy.spatial.transform import Rotation as R\n        >>> import numpy as np\n\n        Represent a single rotation:\n\n        >>> r = R.from_rotvec([0, 0, np.pi])\n        >>> r.as_mrp()\n        array([0.        , 0.        , 1.         ])\n        >>> r.as_mrp().shape\n        (3,)\n\n        Represent a stack with a single rotation:\n\n        >>> r = R.from_euler(\'xyz\', [[180, 0, 0]], degrees=True)\n        >>> r.as_mrp()\n        array([[1.       , 0.        , 0.         ]])\n        >>> r.as_mrp().shape\n        (1, 3)\n\n        Represent multiple rotations:\n\n        >>> r = R.from_rotvec([[np.pi/2, 0, 0], [0, 0, np.pi/2]])\n        >>> r.as_mrp()\n        array([[0.41421356, 0.        , 0.        ],\n               [0.        , 0.        , 0.41421356]])\n        >>> r.as_mrp().shape\n        (2, 3)\n\n        Notes\n        -----\n\n        .. versionadded:: 1.6.0\n        ',
    'Rotation.as_quat (line 1163)': 'Represent as quaternions.\n\n        Rotations in 3 dimensions can be represented using unit norm\n        quaternions [1]_. The mapping from quaternions to rotations is\n        two-to-one, i.e. quaternions ``q`` and ``-q``, where ``-q`` simply\n        reverses the sign of each component, represent the same spatial\n        rotation. The returned value is in scalar-last (x, y, z, w) format.\n\n        Returns\n        -------\n        quat : `numpy.ndarray`, shape (4,) or (N, 4)\n            Shape depends on shape of inputs used for initialization.\n\n        References\n        ----------\n        .. [1] https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation\n\n        Examples\n        --------\n        >>> from scipy.spatial.transform import Rotation as R\n        >>> import numpy as np\n\n        Represent a single rotation:\n\n        >>> r = R.from_matrix([[0, -1, 0],\n        ...                    [1, 0, 0],\n        ...                    [0, 0, 1]])\n        >>> r.as_quat()\n        array([0.        , 0.        , 0.70710678, 0.70710678])\n        >>> r.as_quat().shape\n        (4,)\n\n        Represent a stack with a single rotation:\n\n        >>> r = R.from_quat([[0, 0, 0, 1]])\n        >>> r.as_quat().shape\n        (1, 4)\n\n        Represent multiple rotations in a single object:\n\n        >>> r = R.from_rotvec([[np.pi, 0, 0], [0, 0, np.pi/2]])\n        >>> r.as_quat().shape\n        (2, 4)\n\n        ',
    'Rotation.as_rotvec (line 1322)': "Represent as rotation vectors.\n\n        A rotation vector is a 3 dimensional vector which is co-directional to\n        the axis of rotation and whose norm gives the angle of rotation [1]_.\n\n        Parameters\n        ----------\n        degrees : boolean, optional\n            Returned magnitudes are in degrees if this flag is True, else they are\n            in radians. Default is False.\n\n            .. versionadded:: 1.7.0\n\n        Returns\n        -------\n        rotvec : ndarray, shape (3,) or (N, 3)\n            Shape depends on shape of inputs used for initialization.\n\n        References\n        ----------\n        .. [1] https://en.wikipedia.org/wiki/Axis%E2%80%93angle_representation#Rotation_vector\n\n        Examples\n        --------\n        >>> from scipy.spatial.transform import Rotation as R\n        >>> import numpy as np\n\n        Represent a single rotation:\n\n        >>> r = R.from_euler('z', 90, degrees=True)\n        >>> r.as_rotvec()\n        array([0.        , 0.        , 1.57079633])\n        >>> r.as_rotvec().shape\n        (3,)\n\n        Represent a rotation in degrees:\n\n        >>> r = R.from_euler('YX', (-90, -90), degrees=True)\n        >>> s = r.as_rotvec(degrees=True)\n        >>> s\n        array([-69.2820323, -69.2820323, -69.2820323])\n        >>> np.linalg.norm(s)\n        120.00000000000001\n\n        Represent a stack with a single rotation:\n\n        >>> r = R.from_quat([[0, 0, 1, 1]])\n        >>> r.as_rotvec()\n        array([[0.        , 0.        , 1.57079633]])\n        >>> r.as_rotvec().shape\n        (1, 3)\n\n        Represent multiple rotations in a single object:\n\n        >>> r = R.from_quat([[0, 0, 1, 1], [1, 1, 0, 1]])\n        >>> r.as_rotvec()\n        array([[0.        , 0.        , 1.57079633],\n               [1.35102172, 1.35102172, 0.        ]])\n        >>> r.as_rotvec().shape\n        (2, 3)\n\n        ",
    'Rotation.from_euler (line 904)': "Initialize from Euler angles.\n\n        Rotations in 3-D can be represented by a sequence of 3\n        rotations around a sequence of axes. In theory, any three axes spanning\n        the 3-D Euclidean space are enough. In practice, the axes of rotation are\n        chosen to be the basis vectors.\n\n        The three rotations can either be in a global frame of reference\n        (extrinsic) or in a body centred frame of reference (intrinsic), which\n        is attached to, and moves with, the object under rotation [1]_.\n\n        Parameters\n        ----------\n        seq : string\n            Specifies sequence of axes for rotations. Up to 3 characters\n            belonging to the set {'X', 'Y', 'Z'} for intrinsic rotations, or\n            {'x', 'y', 'z'} for extrinsic rotations. Extrinsic and intrinsic\n            rotations cannot be mixed in one function call.\n        angles : float or array_like, shape (N,) or (N, [1 or 2 or 3])\n            Euler angles specified in radians (`degrees` is False) or degrees\n            (`degrees` is True).\n            For a single character `seq`, `angles` can be:\n\n            - a single value\n            - array_like with shape (N,), where each `angle[i]`\n              corresponds to a single rotation\n            - array_like with shape (N, 1), where each `angle[i, 0]`\n              corresponds to a single rotation\n\n            For 2- and 3-character wide `seq`, `angles` can be:\n\n            - array_like with shape (W,) where `W` is the width of\n              `seq`, which corresponds to a single rotation with `W` axes\n            - array_like with shape (N, W) where each `angle[i]`\n              corresponds to a sequence of Euler angles describing a single\n              rotation\n\n        degrees : bool, optional\n            If True, then the given angles are assumed to be in degrees.\n            Default is False.\n\n        Returns\n        -------\n        rotation : `Rotation` instance\n            Object containing the rotation represented by the sequence of\n            rotations around given axes with given angles.\n\n        References\n        ----------\n        .. [1] https://en.wikipedia.org/wiki/Euler_angles#Definition_by_intrinsic_rotations\n\n        Examples\n        --------\n        >>> from scipy.spatial.transform import Rotation as R\n\n        Initialize a single rotation along a single axis:\n\n        >>> r = R.from_euler('x', 90, degrees=True)\n        >>> r.as_quat().shape\n        (4,)\n\n        Initialize a single rotation with a given axis sequence:\n\n        >>> r = R.from_euler('zyx', [90, 45, 30], degrees=True)\n        >>> r.as_quat().shape\n        (4,)\n\n        Initialize a stack with a single rotation around a single axis:\n\n        >>> r = R.from_euler('x', [90], degrees=True)\n        >>> r.as_quat().shape\n        (1, 4)\n\n        Initialize a stack with a single rotation with an axis sequence:\n\n        >>> r = R.from_euler('zyx', [[90, 45, 30]], degrees=True)\n        >>> r.as_quat().shape\n        (1, 4)\n\n        Initialize multiple elementary rotations in one object:\n\n        >>> r = R.from_euler('x', [90, 45, 30], degrees=True)\n        >>> r.as_quat().shape\n        (3, 4)\n\n        Initialize multiple rotations in one object:\n\n        >>> r = R.from_euler('zyx', [[90, 45, 30], [35, 45, 90]], degrees=True)\n        >>> r.as_quat().shape\n        (2, 4)\n\n        ",
    'Rotation.from_matrix (line 643)': 'Initialize from rotation matrix.\n\n        Rotations in 3 dimensions can be represented with 3 x 3 proper\n        orthogonal matrices [1]_. If the input is not proper orthogonal,\n        an approximation is created using the method described in [2]_.\n\n        Parameters\n        ----------\n        matrix : array_like, shape (N, 3, 3) or (3, 3)\n            A single matrix or a stack of matrices, where ``matrix[i]`` is\n            the i-th matrix.\n\n        Returns\n        -------\n        rotation : `Rotation` instance\n            Object containing the rotations represented by the rotation\n            matrices.\n\n        References\n        ----------\n        .. [1] https://en.wikipedia.org/wiki/Rotation_matrix#In_three_dimensions\n        .. [2] F. Landis Markley, "Unit Quaternion from Rotation Matrix",\n               Journal of guidance, control, and dynamics vol. 31.2, pp.\n               440-442, 2008.\n\n        Examples\n        --------\n        >>> from scipy.spatial.transform import Rotation as R\n        >>> import numpy as np\n\n        Initialize a single rotation:\n\n        >>> r = R.from_matrix([\n        ... [0, -1, 0],\n        ... [1, 0, 0],\n        ... [0, 0, 1]])\n        >>> r.as_matrix().shape\n        (3, 3)\n\n        Initialize multiple rotations in a single object:\n\n        >>> r = R.from_matrix([\n        ... [\n        ...     [0, -1, 0],\n        ...     [1, 0, 0],\n        ...     [0, 0, 1],\n        ... ],\n        ... [\n        ...     [1, 0, 0],\n        ...     [0, 0, -1],\n        ...     [0, 1, 0],\n        ... ]])\n        >>> r.as_matrix().shape\n        (2, 3, 3)\n\n        If input matrices are not special orthogonal (orthogonal with\n        determinant equal to +1), then a special orthogonal estimate is stored:\n\n        >>> a = np.array([\n        ... [0, -0.5, 0],\n        ... [0.5, 0, 0],\n        ... [0, 0, 0.5]])\n        >>> np.linalg.det(a)\n        0.12500000000000003\n        >>> r = R.from_matrix(a)\n        >>> matrix = r.as_matrix()\n        >>> matrix\n        array([[-0.38461538, -0.92307692,  0.        ],\n               [ 0.92307692, -0.38461538,  0.        ],\n               [ 0.        ,  0.        ,  1.        ]])\n        >>> np.linalg.det(matrix)\n        1.0000000000000002\n\n        It is also possible to have a stack containing a single rotation:\n\n        >>> r = R.from_matrix([[\n        ... [0, -1, 0],\n        ... [1, 0, 0],\n        ... [0, 0, 1]]])\n        >>> r.as_matrix()\n        array([[[ 0., -1.,  0.],\n                [ 1.,  0.,  0.],\n                [ 0.,  0.,  1.]]])\n        >>> r.as_matrix().shape\n        (1, 3, 3)\n\n        Notes\n        -----\n        This function was called from_dcm before.\n\n        .. versionadded:: 1.4.0\n        ',
    'Rotation.from_mrp (line 1064)': 'Initialize from Modified Rodrigues Parameters (MRPs).\n\n        MRPs are a 3 dimensional vector co-directional to the axis of rotation and whose\n        magnitude is equal to ``tan(theta / 4)``, where ``theta`` is the angle of rotation\n        (in radians) [1]_.\n\n        MRPs have a singuarity at 360 degrees which can be avoided by ensuring the angle of\n        rotation does not exceed 180 degrees, i.e. switching the direction of the rotation when\n        it is past 180 degrees.\n\n        Parameters\n        ----------\n        mrp : array_like, shape (N, 3) or (3,)\n            A single vector or a stack of vectors, where `mrp[i]` gives\n            the ith set of MRPs.\n\n        Returns\n        -------\n        rotation : `Rotation` instance\n            Object containing the rotations represented by input MRPs.\n\n        References\n        ----------\n        .. [1] Shuster, M. D. "A Survery of Attitude Representations",\n               The Journal of Astronautical Sciences, Vol. 41, No.4, 1993,\n               pp. 475-476\n\n        Notes\n        -----\n\n        .. versionadded:: 1.6.0\n\n        Examples\n        --------\n        >>> from scipy.spatial.transform import Rotation as R\n        >>> import numpy as np\n\n        Initialize a single rotation:\n\n        >>> r = R.from_mrp([0, 0, 1])\n        >>> r.as_euler(\'xyz\', degrees=True)\n        array([0.        , 0.        , 180.      ])\n        >>> r.as_euler(\'xyz\').shape\n        (3,)\n\n        Initialize multiple rotations in one object:\n\n        >>> r = R.from_mrp([\n        ... [0, 0, 1],\n        ... [1, 0, 0]])\n        >>> r.as_euler(\'xyz\', degrees=True)\n        array([[0.        , 0.        , 180.      ],\n               [180.0     , 0.        , 0.        ]])\n        >>> r.as_euler(\'xyz\').shape\n        (2, 3)\n\n        It is also possible to have a stack of a single rotation:\n\n        >>> r = R.from_mrp([[0, 0, np.pi/2]])\n        >>> r.as_euler(\'xyz\').shape\n        (1, 3)\n\n        ',
    'Rotation.from_quat (line 578)': 'Initialize from quaternions.\n\n        3D rotations can be represented using unit-norm quaternions [1]_.\n\n        Parameters\n        ----------\n        quat : array_like, shape (N, 4) or (4,)\n            Each row is a (possibly non-unit norm) quaternion in scalar-last\n            (x, y, z, w) format. Each quaternion will be normalized to unit\n            norm.\n\n        Returns\n        -------\n        rotation : `Rotation` instance\n            Object containing the rotations represented by input quaternions.\n\n        References\n        ----------\n        .. [1] https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation\n\n        Examples\n        --------\n        >>> from scipy.spatial.transform import Rotation as R\n\n        Initialize a single rotation:\n\n        >>> r = R.from_quat([1, 0, 0, 0])\n        >>> r.as_quat()\n        array([1., 0., 0., 0.])\n        >>> r.as_quat().shape\n        (4,)\n\n        Initialize multiple rotations in a single object:\n\n        >>> r = R.from_quat([\n        ... [1, 0, 0, 0],\n        ... [0, 0, 0, 1]\n        ... ])\n        >>> r.as_quat()\n        array([[1., 0., 0., 0.],\n               [0., 0., 0., 1.]])\n        >>> r.as_quat().shape\n        (2, 4)\n\n        It is also possible to have a stack of a single rotation:\n\n        >>> r = R.from_quat([[0, 0, 0, 1]])\n        >>> r.as_quat()\n        array([[0., 0., 0., 1.]])\n        >>> r.as_quat().shape\n        (1, 4)\n\n        Quaternions are normalized before initialization.\n\n        >>> r = R.from_quat([0, 0, 1, 1])\n        >>> r.as_quat()\n        array([0.        , 0.        , 0.70710678, 0.70710678])\n        ',
    'Rotation.from_rotvec (line 796)': 'Initialize from rotation vectors.\n\n        A rotation vector is a 3 dimensional vector which is co-directional to\n        the axis of rotation and whose norm gives the angle of rotation [1]_.\n\n        Parameters\n        ----------\n        rotvec : array_like, shape (N, 3) or (3,)\n            A single vector or a stack of vectors, where `rot_vec[i]` gives\n            the ith rotation vector.\n        degrees : bool, optional\n            If True, then the given magnitudes are assumed to be in degrees.\n            Default is False.\n\n            .. versionadded:: 1.7.0\n\n        Returns\n        -------\n        rotation : `Rotation` instance\n            Object containing the rotations represented by input rotation\n            vectors.\n\n        References\n        ----------\n        .. [1] https://en.wikipedia.org/wiki/Axis%E2%80%93angle_representation#Rotation_vector\n\n        Examples\n        --------\n        >>> from scipy.spatial.transform import Rotation as R\n        >>> import numpy as np\n\n        Initialize a single rotation:\n\n        >>> r = R.from_rotvec(np.pi/2 * np.array([0, 0, 1]))\n        >>> r.as_rotvec()\n        array([0.        , 0.        , 1.57079633])\n        >>> r.as_rotvec().shape\n        (3,)\n\n        Initialize a rotation in degrees, and view it in degrees:\n\n        >>> r = R.from_rotvec(45 * np.array([0, 1, 0]), degrees=True)\n        >>> r.as_rotvec(degrees=True)\n        array([ 0., 45.,  0.])\n\n        Initialize multiple rotations in one object:\n\n        >>> r = R.from_rotvec([\n        ... [0, 0, np.pi/2],\n        ... [np.pi/2, 0, 0]])\n        >>> r.as_rotvec()\n        array([[0.        , 0.        , 1.57079633],\n               [1.57079633, 0.        , 0.        ]])\n        >>> r.as_rotvec().shape\n        (2, 3)\n\n        It is also possible to have a stack of a single rotaton:\n\n        >>> r = R.from_rotvec([[0, 0, np.pi/2]])\n        >>> r.as_rotvec().shape\n        (1, 3)\n\n        ',
    'Rotation.inv (line 1869)': "Invert this rotation.\n\n        Composition of a rotation with its inverse results in an identity\n        transformation.\n\n        Returns\n        -------\n        inverse : `Rotation` instance\n            Object containing inverse of the rotations in the current instance.\n\n        Examples\n        --------\n        >>> from scipy.spatial.transform import Rotation as R\n        >>> import numpy as np\n\n        Inverting a single rotation:\n\n        >>> p = R.from_euler('z', 45, degrees=True)\n        >>> q = p.inv()\n        >>> q.as_euler('zyx', degrees=True)\n        array([-45.,   0.,   0.])\n\n        Inverting multiple rotations:\n\n        >>> p = R.from_rotvec([[0, 0, np.pi/3], [-np.pi/4, 0, 0]])\n        >>> q = p.inv()\n        >>> q.as_rotvec()\n        array([[-0.        , -0.        , -1.04719755],\n               [ 0.78539816, -0.        , -0.        ]])\n\n        ",
    'Rotation.magnitude (line 1910)': 'Get the magnitude(s) of the rotation(s).\n\n        Returns\n        -------\n        magnitude : ndarray or float\n            Angle(s) in radians, float if object contains a single rotation\n            and ndarray if object contains multiple rotations.\n\n        Examples\n        --------\n        >>> from scipy.spatial.transform import Rotation as R\n        >>> import numpy as np\n        >>> r = R.from_quat(np.eye(4))\n        >>> r.magnitude()\n        array([3.14159265, 3.14159265, 3.14159265, 0.        ])\n\n        Magnitude of a single rotation:\n\n        >>> r[0].magnitude()\n        3.141592653589793\n        ',
    'Rotation.mean (line 1945)': "Get the mean of the rotations.\n\n        Parameters\n        ----------\n        weights : array_like shape (N,), optional\n            Weights describing the relative importance of the rotations. If\n            None (default), then all values in `weights` are assumed to be\n            equal.\n\n        Returns\n        -------\n        mean : `Rotation` instance\n            Object containing the mean of the rotations in the current\n            instance.\n\n        Notes\n        -----\n        The mean used is the chordal L2 mean (also called the projected or\n        induced arithmetic mean). If ``p`` is a set of rotations with mean\n        ``m``, then ``m`` is the rotation which minimizes\n        ``(weights[:, None, None] * (p.as_matrix() - m.as_matrix())**2).sum()``.\n\n        Examples\n        --------\n        >>> from scipy.spatial.transform import Rotation as R\n        >>> r = R.from_euler('zyx', [[0, 0, 0],\n        ...                          [1, 0, 0],\n        ...                          [0, 1, 0],\n        ...                          [0, 0, 1]], degrees=True)\n        >>> r.mean().as_euler('zyx', degrees=True)\n        array([0.24945696, 0.25054542, 0.24945696])\n        ",
    'Rotation.random (line 2248)': "Generate uniformly distributed rotations.\n\n        Parameters\n        ----------\n        num : int or None, optional\n            Number of random rotations to generate. If None (default), then a\n            single rotation is generated.\n        random_state : {None, int, `numpy.random.Generator`,\n                        `numpy.random.RandomState`}, optional\n\n            If `seed` is None (or `np.random`), the `numpy.random.RandomState`\n            singleton is used.\n            If `seed` is an int, a new ``RandomState`` instance is used,\n            seeded with `seed`.\n            If `seed` is already a ``Generator`` or ``RandomState`` instance\n            then that instance is used.\n\n        Returns\n        -------\n        random_rotation : `Rotation` instance\n            Contains a single rotation if `num` is None. Otherwise contains a\n            stack of `num` rotations.\n\n        Notes\n        -----\n        This function is optimized for efficiently sampling random rotation\n        matrices in three dimensions. For generating random rotation matrices\n        in higher dimensions, see `scipy.stats.special_ortho_group`.\n\n        Examples\n        --------\n        >>> from scipy.spatial.transform import Rotation as R\n\n        Sample a single rotation:\n\n        >>> R.random().as_euler('zxy', degrees=True)\n        array([-110.5976185 ,   55.32758512,   76.3289269 ])  # random\n\n        Sample a stack of rotations:\n\n        >>> R.random(5).as_euler('zxy', degrees=True)\n        array([[-110.5976185 ,   55.32758512,   76.3289269 ],  # random\n               [ -91.59132005,  -14.3629884 ,  -93.91933182],\n               [  25.23835501,   45.02035145, -121.67867086],\n               [ -51.51414184,  -15.29022692, -172.46870023],\n               [ -81.63376847,  -27.39521579,    2.60408416]])\n\n        See Also\n        --------\n        scipy.stats.special_ortho_group\n\n       ",
}

