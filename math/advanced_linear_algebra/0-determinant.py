#!/usr/bin/env python 3
"""
This is for caluculating a determinant .
"""


def determinant(matrix):
""" -Matrix determinant . If matrix is not a list, the function raises 
    type error same as if not a square .
"""

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")


    if not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("matrix must be a square matrix")

    
    size = len(matrix)


    if size == 0:
        return 1


    if size == 1:
        return matrix[0][0]

    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    determinant_value = 0
    for col in range(size):
        #  minor matrix by excluding current row (0) and column (col)
        minor_matrix = [row[:col] + row[col + 1:] for row in matrix[1:]]
        # Calculating  cofactor and adding to determinant
        cofactor = (-1) ** col * matrix[0][col] * determinant(minor_matrix)
        determinant_value += cofactor

