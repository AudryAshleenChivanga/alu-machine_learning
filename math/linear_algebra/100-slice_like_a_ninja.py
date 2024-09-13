#!/usr/bin/env python3

"""
This script slices a matrix along specific axes (hahaha just like a ninja).
"""

import numpy as np

def np_slice(matrix, axes={}):
    """
    Slices a matrix along specific axes.

    Args:
        matrix: The numpy.ndarray to slice.
        axes: A dictionary where the key is an axis to slice along,
              and the value is a tuple representing the slice to make along that axis.

    Returns:
        A new numpy.ndarray that has been sliced along the specified axes.
    """
    if not axes:  # If no axes are provided, return the matrix as is
        return matrix[...]

    slices = []
    for i in range(matrix.ndim):  # Iterate over each dimension of the matrix
        if i in axes:
            slices.append(slice(*axes[i]))  # Append the slice specified for this axis
        else:
            slices.append(slice(None))  # Append a default slice (':') if no slice is specified for this axis

    return matrix[tuple(slices)]  # Return the sliced matrix
mat1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(np_slice(mat1, axes={1: (1, 3)}))  # Output sliced matrix
print(mat1)
