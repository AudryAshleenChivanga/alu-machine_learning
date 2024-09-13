#!/usr/bin/env python3
"""
Slice arrays along specific axes
"""


def np_slice(matrix, axes=None):
    """Slices a matrix (list of lists) along specific axes

    Args:
        matrix (list of lists): matrix to slice
        axes (dict): dictionary where the key is an axis to slice along and
                     the value is a tuple representing the slice to make along
                     that axis

    Returns:
        list of lists: the sliced matrix
    """
    if axes is None:
        return matrix

    slices = []
    ndim = len(matrix.shape) if hasattr(matrix, 'shape') else len(matrix)

    # Generate slices for each axis
    for i in range(ndim):
        if i in axes:
            slices.append(slice(*axes[i]))
        else:
            slices.append(slice(None))

    return matrix[tuple(slices)]
