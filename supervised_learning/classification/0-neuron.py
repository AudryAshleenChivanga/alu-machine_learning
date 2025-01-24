#!/usr/bin/env python3
import numpy as np


class Neuron:
    """Defines a single neuron performing binary classification."""

    def __init__(self, nx):
        """
        Initialize the Neuron.

        Parameters:
        nx (int): The number of input features to the neuron.

        Raises:
        TypeError: If nx is not an integer.
        ValueError: If nx is less than 1.
        """
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
                                                                                                                                                                        
        self.W = np.random.randn(1, nx)
        # Bias initialization
        self.b = 0
        # Activated output initialization
        self.A = 0
