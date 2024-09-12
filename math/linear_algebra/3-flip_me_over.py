#!/usr/bin/env python3


def matrix_transpose(matrix):
    """
    Returns the transpose of a 2D matrix.

    Args:
    - matrix (list of lists): A 2D matrix represented as a list of lists.

    Returns:
    - list of lists: A new matrix which is the transpose of the input matrix.
    """
    # Using list comprehension to transpose the matrix
    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    return transposed
