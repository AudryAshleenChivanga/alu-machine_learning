#!/usr/bin/env python3

"""
    Advanced concatenating (just trying)
"""


def cat_matrices(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis.

    Args:
        mat1: The first matrix (list of lists).
        mat2: The second matrix (list of lists).
        axis: The axis along which to concatenate. Default is 0.

    Returns:
        A new matrix that is the result of concatenation along the specified axis,
        or None if the matrices cannot be concatenated.
    """
    # If axis is 0, check if each sublist of mat1 and mat2 have the same length
    if axis == 0:
        # Check that all sublists at this level have the same length
        if isinstance(mat1[0], list) and isinstance(mat2[0], list):
            if len(mat1[0]) != len(mat2[0]):
                return None
        # Concatenate along axis 0
        return mat1 + mat2
    else:
        # If axis is greater than 0, recursively concatenate sublists
        if isinstance(mat1, list) and isinstance(mat2, list) and len(mat1) == len(mat2):
            concatenated = []
            for sub_mat1, sub_mat2 in zip(mat1, mat2):
                concatenated_sub = cat_matrices(sub_mat1, sub_mat2, axis - 1)
                if concatenated_sub is None:
                    return None
                concatenated.append(concatenated_sub)
            return concatenated
        return None
