#!/usr/bin/env python3

def matrix_shape(matrix):
    """ This function calculates the shape of a matrix and returns it
    as a list of integers .

    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
