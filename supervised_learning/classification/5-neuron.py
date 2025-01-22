#!/usr/bin/env python3
"""
defines Neuron class that defines
a single neuron performing binary classification
"""


import numpy as np


class Neuron:
    """
    Defines class Neuron that defines a single neuron
    performing binary classification
    """

    def __init__(self, nx):
        """
        Initializes a single neuron
        performing binary classification
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
        Computes the forward propagation of the neuron
        """
        z = np.matmul(self.W, X) + self.b
        self.__A = 1 / (1 + (np.exp(-z)))
        return (self.A)

    def cost(self, Y, A):
        """
        Computes the cost of the model using logistic regression
        """
        m = Y.shape[1]
        m_loss = np.sum((Y * np.log(A)) + ((1 - Y) * np.log(1.0000001 - A)))
        cost = (1 / m) * (-(m_loss))
        return (cost)

    def evaluate(self, X, Y):
        """
        Computes the prediction and cost of the network
        """
        A = self.forward_prop(X)
        cost = self.cost(Y, A)
        prediction = np.where(A >= 0.5, 1, 0)
        return (prediction, cost)

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """
        Computes one pass of gradient descent on the neuron
        """
        m = Y.shape[1]
        dz = (A - Y)
        d__W = (1 / m) * (np.matmul(X, dz.transpose()).transpose())
        d__b = (1 / m) * (np.sum(dz))
        self.__W = self.W - (alpha * d__W)
        self.__b = self.b - (alpha * d__b)
