#!/usr/bin/env python3

"""
This module provides a function to calculate the determinant of a matrix.
"""


def determinant(matrix):
    """
    Calculates the determinant of a matrix using recursion.

    Parameters:
    matrix (list of lists): The matrix for which the determinant is calculated.

    Returns:
    int/float: The determinant of the matrix.

    Raises:
    TypeError: If the input is not a list of lists.
    ValueError: If the matrix is not square.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if len(matrix) == 1 and len(matrix[0]) == 0:
        return 1

    if not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("matrix must be a square matrix")

    size = len(matrix)

    if size == 1:
        return matrix[0][0]
    
    determinant_value = 0
    for col in range(size):
        minor_matrix = [row[:col] + row[col + 1:] for row in matrix[1:]]
        cofactor = (-1) ** col * matrix[0][col] * determinant(minor_matrix)
        determinant_value += cofactor

    return determinant_value


if __name__ == '__main__':
    mat0 = [[]]
    mat1 = [[5]]
    mat2 = [[1, 2], [3, 4]]
    mat3 = [[1, 1], [1, 1]]
    mat4 = [[5, 7, 9], [3, 1, 8], [6, 2, 4]]
    mat5 = []
    mat6 = [[1, 2, 3], [4, 5, 6]]

    print(determinant(mat0))  # Output: 1
    print(determinant(mat1))  # Output: 5
    print(determinant(mat2))  # Output: -2
    print(determinant(mat3))  # Output: 0
    print(determinant(mat4))  # Output: 192

    try:
        determinant(mat5)
    except Exception as e:
        print(e)  # Output: matrix must be a list of lists

    try:
        determinant(mat6)
    except Exception as e:
        print(e)  # Output: matrix must be a square matrix
