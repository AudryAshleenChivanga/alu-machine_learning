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
            raise ValueError("nx must be positive")
        
        # Private instance attributes
        self.__W = np.random.randn(1, nx)  # Random normal distribution
        self.__b = 0  # Bias initialization
        self.__A = 0  # Activated output initialization

    @property
    def W(self):
        """Getter for weights vector."""
        return self.__W

    @property
    def b(self):
        """Getter for bias."""
        return self.__b

    @property
    def A(self):
        """Getter for activated output."""
        return self.__A
