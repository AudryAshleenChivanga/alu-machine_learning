#!/usr/bin/env python3

"""
    Adding 2 matrices - eyyy advanced way
"""


def add_matrices(mat1, mat2):
    """
    Adds two matrices element-wise.

    Args:
        mat1: The first matrix (list of lists).
        mat2: The second matrix (list of lists).

    Returns:
        A new matrix that is the result of element-wise addition,
        or None if the matrices do not have the same shape.
    """
    # Check if both matrices have the same shape
    if not are_same_shape(mat1, mat2):
        return None

    # Perform element-wise addition
    return add_recursive(mat1, mat2)


def are_same_shape(mat1, mat2):
    """
    Recursively checks if two matrices have the same shape.

    Args:
        mat1: The first matrix (list of lists).
        mat2: The second matrix (list of lists).

    Returns:
        True if both matrices have the same shape, False otherwise.
    """
    if type(mat1) != type(mat2):
        return False
    if isinstance(mat1, list):
        if len(mat1) != len(mat2):
            return False
        for sub_mat1, sub_mat2 in zip(mat1, mat2):
            if not are_same_shape(sub_mat1, sub_mat2):
                return False
    return True


def add_recursive(mat1, mat2):
    """
    Recursively adds two matrices element-wise.

    Args:
        mat1: The first matrix (list of lists).
        mat2: The second matrix (list of lists).

    Returns:
        A new matrix that is the result of element-wise addition.
    """
    if isinstance(mat1, list):
        return [add_recursive(sub_mat1, sub_mat2) for sub_mat1, sub_mat2 in zip(mat1, mat2)]
    else:
        return mat1 + mat2
