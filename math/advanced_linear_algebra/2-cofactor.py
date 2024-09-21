#!/usr/bin/env python3

"""
This module provides a function to calculate the cofactor matrix
of a given matrix.
"""


def cofactor(matrix):
    """
    Calculates the cofactor matrix of a matrix.

    Parameters:
    matrix (list of lists): The matrix for which the cofactor matrix
    is calculated.

    Returns:
    list of lists: The cofactor matrix of the input matrix.

    Raises:
    TypeError: If the input is not a list of lists.
    ValueError: If the matrix is not a non-empty square matrix.
    """
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if len(matrix) == 0 or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    size = len(matrix)

    if size == 1:
        return [[1]]

    cofactor_matrix = []
    for i in range(size):
        cofactor_row = []
        for j in range(size):
            sub_matrix = [
                row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])
            ]
            cofactor_value = (-1) ** (i + j) * determinant(sub_matrix)
            cofactor_row.append(cofactor_value)
        cofactor_matrix.append(cofactor_row)

    return cofactor_matrix


def determinant(matrix):
    """
    Calculates the determinant of a matrix using recursion.

    Parameters:
    matrix (list of lists): The matrix for which the determinant
    is calculated.

    Returns:
    int/float: The determinant of the matrix.

    Raises:
    TypeError: If the input is not a list of lists.
    ValueError: If the matrix is not square.
    """
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
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
    mat1 = [[5]]
    mat2 = [[1, 2], [3, 4]]
    mat3 = [[1, 1], [1, 1]]
    mat4 = [[5, 7, 9], [3, 1, 8], [6, 2, 4]]
    mat5 = []
    mat6 = [[1, 2, 3], [4, 5, 6]]

    print(cofactor(mat1))
    print(cofactor(mat2))
    print(cofactor(mat3))
    print(cofactor(mat4))

    try:
        cofactor(mat5)
    except Exception as e:
        print(e)

    try:
        cofactor(mat6)
    except Exception as e:
        print(e)
