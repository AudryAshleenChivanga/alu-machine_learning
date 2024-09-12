#!/usr/bin/env python3

"""
        This function adds two matrices element-wise
"""


def add_matrices2D(mat1, mat2):
    """
    Adds two 2D matrices element-wise.

    Args:
    - mat1 (list of lists of ints/floats): The first 2D matrix.
    - mat2 (list of lists of ints/floats): The second 2D matrix.

    Returns:
    - list of lists: A new matrix containing the element-wise sum of mat1 and
    mat2.
    - None: If mat1 and mat2 are not of the same shape.
    """
    # Check if both matrices have the same number of rows
    if len(mat1) != len(mat2):
        return None

    # Check if all rows have the same number of columns
    for row1, row2 in zip(mat1, mat2):
        if len(row1) != len(row2):
            return None

    # Add matrices element-wise
    result_matrix = [[row1[i] + row2[i]
                      for i in range(len(row1))] for row1, row2
                     in zip(mat1, mat2)]

    return result_matrix
