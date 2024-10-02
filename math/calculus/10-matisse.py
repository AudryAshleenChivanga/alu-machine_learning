#!/usr/bin/env python3
"""
This module contains the function that calculates the polynomial
derivative of a list of coefficients.
"""


def poly_derivative(poly):
    """
    Calculates the polynomial derivative of a list of coefficients.
    param: n: int
    return: int
    """
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    if len(poly) == 1:
        return [0]
    derivative = []
    for i in range(1, len(poly)):
        derivative.append(i * poly[i])
    if derivative == [] or all(coeff == 0 for coeff in derivative):
        return [0]
    return derivative
