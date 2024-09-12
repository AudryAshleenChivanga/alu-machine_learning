#!/usr/bin/env python3

"""
    This method concatenates two matrices along a specific axis
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
        Concatenates 2D matrices containing ints or floats
        Concatenates in a specific axis .
    """
    if not mat1 or not mat2:
        return None

    # If concatenating along axis 0 (rows), check if both have the same number of columns
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        # Create a new matrix by concatenating along the rows
        return [row[:] for row in mat1] + [row[:] for row in mat2]

    # If concatenating along axis 1 (columns), check if both have the same number of rows
    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        # Create a new matrix by concatenating along the columns
        return [mat1[i] + mat2[i] for i in range(len(mat1))]

    # If axis is neither 0 nor 1, return None
    else:
        return None
