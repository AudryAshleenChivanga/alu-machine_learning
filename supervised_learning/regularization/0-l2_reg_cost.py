#!/usr/bin/env python3
"""
Implements L2 Regularization for computing the cost of a neural network.
"""

import numpy as np


def l2_reg_cost(cost, lambtha, weights, L, m):
    """
    Computes the L2-regularized cost of a neural network.

    Parameters:
        cost: The original cost of the network without regularization.
        lambtha: parameter controlling the strength of L2 penalty.
        weights: Dictionary containing the weights and biases of the network.
        L: Total number of layers in the neural network.
        m: Number of training examples.

    Returns:
        The cost of the network adjusted for L2 regularization.
    """
    weights_squared = 0
    for i in range(1, L + 1):
        level_weight = weights["W{}".format(i)]
        # Summing up the squared norms of all weight matrices
        weights_squared += np.linalg.norm(level_weight)
    l2_reg_cost = cost + (lambtha / (2 * m)) * weights_squared
    return l2_reg_cost
