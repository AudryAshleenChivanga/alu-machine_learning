#!/usr/bin/env python3
"""
This module contains the function summation_i_squared to calculate
the sum of squares of integers.
"""


def summation_i_squared(n):
    """
    Calculates the sum of squares of integers from 1 to n using the formula:
    sum(i^2) = n(n + 1)(2n + 1) / 6

    :param n: integer stopping condition
    :return: integer value of the sum of squares, or None if n is invalid
    """
    if isinstance(n, int) and n > 0:
        return (n * (n + 1) * (2 * n + 1)) // 6
    return None


if __name__ == "__main__":
    # Example usage
    n = 5
    print(summation_i_squared(n))
