#!/usr/bin/env python3
"""Translate mathematical operations into code"""


def poly_integral(poly, C=0):
    """Calculates the integral of a polynomial.

    Args:
        poly (list): A list of coefficients
        representing a polynomial.
        C (int or float): A constant to be added
        to the integral.

    Returns:
        list: A new list of coefficients
        representing the integral of the polynomial,
        or None if the input is invalid.
    """

    if type(poly) != list or type(C) != int:
        return None
    if len(poly) == 0:
        return None

    integral = [C]
    if poly == [0]:
        return integral
    idx = 1
    for i in poly:
        integral.append(i / idx)
        if integral[idx] % 1 == 0:
            integral[idx] = int(integral[idx])
        idx += 1

    return integral
