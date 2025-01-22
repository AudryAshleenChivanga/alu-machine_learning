#!/usr/bin/env python3
"""
Defines the class Neuron that defines
a single neuron performing binary
"""


import numpy as np


class Neuron:
    """
    class Neuron that defines a single neuron performing binary
    """

    def __init__(self, nx):
        """
        class constructor for Neuron

        noramlly distributed random values for weights and bias
        """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """
        Getter for the weight attribute
        """
        return (self.__W)

    @property
    def b(self):
        """
        Getter for the bias attribute
        """
        return (self.__b)

    @property
    def A(self):
        """
        Getter for the activation attribute
        """
        return (self.__A)

    def forward_prop(self, X):
        """
        calculates the forward propagation of the neuron
        """
        z = np.matmul(self.W, X) + self.b
        self.__A = 1 / (1 + (np.exp(-z)))
        return (self.A)

    def cost(self, Y, A):
        """
        calculates the cost of the model using logistic regression
        """
        m = Y.shape[1]
        m_loss = np.sum((Y * np.log(A)) + ((1 - Y) * np.log(1.0000001 - A)))
        cost = (1 / m) * (-(m_loss))
        return (cost)

    def evaluate(self, X, Y):
        """
        evaluates the neuron's predictions
        """
        A = self.forward_prop(X)
        cost = self.cost(Y, A)
        prediction = np.where(A >= 0.5, 1, 0)
        return (prediction, cost)
