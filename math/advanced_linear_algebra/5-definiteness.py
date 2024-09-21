#!/usr/bin/env python3

"""
This module provides a function to determine the definiteness of a matrix.
"""

import numpy as np

def definiteness(matrix):
    """
    Calculates the definiteness of a matrix.

    Parameters:
    matrix (numpy.ndarray): The matrix whose definiteness is to be calculated.

    Returns:
    str: One of 'Positive definite', 'Positive semi-definite',
    'Negative definite', 'Negative semi-definite', 'Indefinite', or None.

    Raises:
    TypeError: If the input is not a numpy.ndarray.
    """
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    if len(matrix.shape) != 2 or matrix.shape[0] != matrix.shape[1]:
        return None

    eigenvalues = np.linalg.eigvals(matrix)

    if np.all(eigenvalues > 0):
        return "Positive definite"
    elif np.all(eigenvalues >= 0):
        return "Positive semi-definite"
    elif np.all(eigenvalues < 0):
        return "Negative definite"
    elif np.all(eigenvalues <= 0):
        return "Negative semi-definite"
    elif np.any(eigenvalues > 0) and np.any(eigenvalues < 0):
        return "Indefinite"
    else:
        return None


if __name__ == '__main__':
    definiteness = __import__('5-definiteness').definiteness
    import numpy as np

    mat1 = np.array([[5, 1], [1, 1]])
    mat2 = np.array([[2, 4], [4, 8]])
    mat3 = np.array([[-1, 1], [1, -1]])
    mat4 = np.array([[-2, 4], [4, -9]])
    mat5 = np.array([[1, 2], [2, 1]])
    mat6 = np.array([])
    mat7 = np.array([[1, 2, 3], [4, 5, 6]])
    mat8 = [[1, 2], [1, 2]]

    print(definiteness(mat1))  # Positive definite
    print(definiteness(mat2))  # Positive semi-definite
    print(definiteness(mat3))  # Negative semi-definite
    print(definiteness(mat4))  # Negative definite
    print(definiteness(mat5))  # Indefinite
    print(definiteness(mat6))  # None
    print(definiteness(mat7))  # None
    try:
        definiteness(mat8)
    except Exception as e:
        print(e)  # matrix must be a numpy.ndarray
