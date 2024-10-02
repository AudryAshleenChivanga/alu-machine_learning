#!/usr/bin/env python3
"""
This module contains the function that calculates the 
intergral of a polynomial.
"""


def poly_derivative(poly):
    """
    Calculates the integral of a polynomial.
    """
    if not isinstance(poly, list) or not all(isinstance(coef, (int, float)) for coef in poly):
        return None
    C = 0  # Define the constant C, you can change this value as needed
    if not isinstance(C, (int, float)):
        return None
    integral = [C]  
    for i, coef in enumerate(poly):
        integral_coef = coef / (i + 1)
        # Convert to int if the result is a whole number
        if integral_coef.is_integer():
            integral.append(int(integral_coef))
        else:
            integral.append(integral_coef)
    return integral
