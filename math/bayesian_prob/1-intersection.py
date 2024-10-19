#!/usr/bin/env python3
"""Function that calculates the intersection of obtaining this data 
with various hypothetical probabilities"""

import numpy as np


def intersection(x, n, P, Pr):
    """Calculates the intersection of obtaining this data with various 
    hypothetical probabilities"""
    
    if type(n) is not int or n <= 0:
        raise ValueError("n must be a positive integer")
    
    if type(x) is not int or x < 0:
        raise ValueError("x must be an integer >= 0")
    
    if x > n:
        raise ValueError("x cannot be greater than n")
    
    if (not isinstance(P, np.ndarray)) or len(P.shape) != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    
    if (not isinstance(Pr, np.ndarray)) or Pr.shape != P.shape:
        raise TypeError("Pr must be a numpy.ndarray with the same shape as P")
    
    if np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in P must be in the range [0, 1]")
    
    if np.any(Pr < 0) or np.any(Pr > 1):
        raise ValueError("All values in Pr must be in the range [0, 1]")
    
    if not np.isclose([np.sum(Pr)], [1.])[0]:
        raise ValueError("Pr must sum to 1")
    
    num = np.math.factorial(n)
    den = np.math.factorial(x) * np.math.factorial(n - x)
    coef = num / den
    likelihood = coef * (P ** x) * ((1 - P) ** (n - x))
    
    return likelihood * Pr
