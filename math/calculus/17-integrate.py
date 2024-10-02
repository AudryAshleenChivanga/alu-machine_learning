#!/usr/bin/env python3
"""
This module contains the function that calculates the
integral of a polynomial.
"""

def poly_integral(poly, C=0):
    """
    Calculates the integral of a polynomial.

    Parameters:
    poly (list): List of coefficients representing the polynomial.
    C (int, float): Integration constant.

    Returns:
    list: List of coefficients representing the integral of the polynomial.
    """


    if not isinstance(poly, list) or not all(
        isinstance(coef, (int, float)) for coef in poly
    ):
        return None
    if not isinstance(C, (int, float)):
        return None

    if len(poly) == 0:
        return [C]

    integral = [C]

    for i, coef in enumerate(poly):
        if coef == 0:
            integral.append(0)
        else:
            integral_coef = coef / (i + 1)
            if integral_coef.is_integer():
                integral.append(int(integral_coef))
            else:
                integral.append(integral_coef)

    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()

    return integral

# Test cases
print(poly_integral(None))  # Expected: None
print(poly_integral([]))    # Expected: [0]
print(poly_integral([0]))   # Expected: [0]
