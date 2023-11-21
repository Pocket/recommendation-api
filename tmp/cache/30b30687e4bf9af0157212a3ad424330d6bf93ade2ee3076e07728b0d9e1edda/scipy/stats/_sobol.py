# encoding: utf-8
# module scipy.stats._sobol
# from /.venv/lib/python3.8/site-packages/scipy/stats/_sobol.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import os as os # /usr/local/lib/python3.8/os.py
import numpy as np # /.venv/lib/python3.8/site-packages/numpy/__init__.py

# Variables with simple values

_MAXDEG = 18
_MAXDIM = 21201

# functions

def get_poly_vinit(*args, **kwargs): # real signature unknown
    """
    Initialize and cache the direction numbers.
    
        Uses a dictionary to store the arrays. `kind` allows to select which
        dictionary to pull. The key of each dictionary corresponds to the `dtype`.
        If the key is not present in any of the dictionary, both dictionaries are
        initialized with `_initialize_direction_numbers`, for the given `dtype`.
    
        This is only used during the initialization step in `_initialize_v`.
    
        Parameters
        ----------
        kind : {'poly', 'vinit'}
            Select which dictionary to pull.
        dtype : {np.uint32, np.uint64}
            Which dtype to use.
    
        Returns
        -------
        poly_vinit : np.ndarray
            Either ``poly`` or ``vinit`` matrix.
    """
    pass

def _categorize(*args, **kwargs): # real signature unknown
    pass

def _cscramble(*args, **kwargs): # real signature unknown
    """ Scrambling using (left) linear matrix scramble (LMS). """
    pass

def _draw(*args, **kwargs): # real signature unknown
    pass

def _fast_forward(*args, **kwargs): # real signature unknown
    pass

def _fill_p_cumulative(*args, **kwargs): # real signature unknown
    pass

def _initialize_direction_numbers(*args, **kwargs): # real signature unknown
    """
    Load direction numbers into two arrays.
    
        Parameters
        ----------
        poly, vinit : np.ndarray
            Direction numbers arrays to fill.
        dtype : {np.uint32, np.uint64}
            Which dtype to use.
    
        Notes
        -----
        Direction numbers obtained using the search criterion D(6)
        up to the dimension 21201. This is the recommended choice by the authors.
    
        Original data can be found at https://web.maths.unsw.edu.au/~fkuo/sobol/.
        For additional details on the quantities involved, see [1].
    
        [1] S. Joe and F. Y. Kuo. Remark on algorithm 659: Implementing sobol's
            quasirandom sequence generator. ACM Trans. Math. Softw., 29(1):49-57,
            Mar. 2003.
    
        The C-code generated from putting the numbers in as literals is obscenely
        large/inefficient. The data file was thus packaged and save as an .npz data
        file for fast loading using the following code (this assumes that the file
        https://web.maths.unsw.edu.au/~fkuo/sobol/new-joe-kuo-6.21201 is present in
        the working directory):
    
            import pandas as pd
            import numpy as np
    
            # read in file content
            with open("./new-joe-kuo-6.21201", "r") as f:
                lines = f.readlines()
    
            rows = []
    
            # parse data from file line by line
            for l in lines[1:]:
                nums = [int(n) for n in l.replace(" 
    ", "").split()]
                d, s, a = nums[:3]
                vs = {f"v{i}": int(v) for i,v in enumerate(nums[3:])}
                rows.append({"d": d, "s": s, "a": a, **vs})
    
    
            # read in as dataframe, explicitly use zero values
            df = pd.DataFrame(rows).fillna(0).astype(int)
    
            # perform conversion
            df["poly"] = 2 * df["a"] + 2 ** df["s"] + 1
    
            # ensure columns are properly ordered
            vs = df[[f"v{i}" for i in range(18)]].values
    
            # add the degenerate d=1 column (not included in the data file)
            vs = np.vstack([vs[0][np.newaxis, :], vs])
            poly = np.concatenate([[1], df["poly"].values])
    
            # save as compressed .npz file to minimize size of distribution
            np.savez_compressed("./_sobol_direction_numbers", vinit=vs, poly=poly)
    """
    pass

def _initialize_v(*args, **kwargs): # real signature unknown
    """ Initialize matrix of size ``dim * bits`` with direction numbers. """
    pass

def _test_find_index(*args, **kwargs): # real signature unknown
    """ Wrapper for testing in python """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

_poly_dict = {}

_vinit_dict = {}

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff929d8640>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.stats._sobol', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff929d8640>, origin='/.venv/lib/python3.8/site-packages/scipy/stats/_sobol.cpython-38-aarch64-linux-gnu.so')"

__test__ = {}

