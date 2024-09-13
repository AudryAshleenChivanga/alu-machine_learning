#!/usr/bin/env python3

"""
    This matrix slices a matrix along specific axes (hahaha just like a ninja
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
    # Create a tuple of slices for all axes, defaulting to full slice ':'
    slices = [slice(None)] * matrix.ndim

    # Update slices according to the axes dictionary
    for axis, slice_range in axes.items():
        slices[axis] = slice(*slice_range)

    # Use tuple of slices to slice the matrix
    return matrix[tuple(slices)]
