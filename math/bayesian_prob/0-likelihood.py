#!/usr/bin/env python3
"""Function that calculates the likelihood of obtaining this data 
given various hypothetical probabilities of developing severe 
side effects"""

import numpy as np


def likelihood(x, n, P):
    """Calculates the likelihood of obtaining this data given various 
    hypothetical probabilities of developing severe side effects"""
    
    if type(n) is not int or n <= 0:
        raise ValueError("n must be a positive integer")
    
    if type(x) is not int or x < 0:
        raise ValueError("x must be an integer >= 0")
    
    if x > n:
        raise ValueError("x cannot be greater than n")
    
    if (not isinstance(P, np.ndarray)) or len(P.shape) != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    
    if np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in P must be in [0, 1]")
    
    num = np.math.factorial(n)
    den = np.math.factorial(x) * np.math.factorial(n - x)
    coef = num / den
    return coef * (P ** x) * ((1 - P) ** (n - x))
