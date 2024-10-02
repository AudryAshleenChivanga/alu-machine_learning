#!/usr/bin/env python3
"""
This module contains the function that calculates the summation of i squared.
"""


def summation_i_squared(n):
    """
    Calculates the summation of i squared.
    param: n: int
    return: int
    """
    if type(n) is not int or n < 1:
        return None
    return int((n * (n + 1) * (2 * n + 1)) / 6)
