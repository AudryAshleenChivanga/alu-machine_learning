#!/usr/bin/env python3

"""
This module provides a function to calculate the shape of a matrix.
"""


def matrix_shape(matrix):
    """
    Calculate the shape of a matrix and return it as a list of integers.

    Args:
    - matrix (list): A matrix represented as a list of lists.

    Returns:
    - list: A list of integers representing the shape of the matrix.
    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
