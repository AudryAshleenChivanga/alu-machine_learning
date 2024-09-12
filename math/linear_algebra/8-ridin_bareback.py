#!/usr/bin/env python3

"""
    This function performs matrix multiplication.
"""


def mat_mul(mat1, mat2):
    """
        This matrix perfoms matrix multiplication.
        It assumes mat 1 and mat2 are 2D matrix.
    """
    if len(mat1[0]) != len(mat2):
        return None

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]

    # Perform matrix multiplication
    for i in range(len(mat1)):  # Iterate over rows of mat1
        for j in range(len(mat2[0])):  # Iterate over columns of mat2
            for k in range(len(mat2)):  # Iterate over elements for dot product
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result
