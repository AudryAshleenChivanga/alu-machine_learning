#!/usr/bin/env python3
"""
File defines a class that represents a
neural network with one hidden layer
"""


import numpy as np


class NeuralNetwork:
    """
    Class that represents a neural network with one hidden layer
    """

    def __init__(self, nx, nodes):
        """
        Initializes a neural network with one hidden layer
        """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if type(nodes) is not int:
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")
        self.__W1 = np.random.randn(nodes, nx)
        self.__b1 = np.zeros((nodes, 1))
        self.__A1 = 0
        self.__W2 = np.random.randn(1, nodes)
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        """
        Getter for the weights vector for the hidden layer
        """
        return (self.__W1)

    @property
    def b1(self):
        """
        Getter for the bias for the hidden layer
        """
        return (self.__b1)

    @property
    def A1(self):
        """
        Getter for the activated output for the hidden layer
        """
        return (self.__A1)

    @property
    def W2(self):
        """
        Getter for the weights vector for the output neuron
        """
        return (self.__W2)

    @property
    def b2(self):
        """
        Getter for the bias for the output neuron
        """
        return (self.__b2)

    @property
    def A2(self):
        """
        Getter for the activated output for the output neuron
        """
        return (self.__A2)

    def forward_prop(self, X):
        """
        Computes the forward propagation of the neural network
        """
        z1 = np.matmul(self.W1, X) + self.b1
        self.__A1 = 1 / (1 + (np.exp(-z1)))
        z2 = np.matmul(self.W2, self.__A1) + self.b2
        self.__A2 = 1 / (1 + (np.exp(-z2)))
        return (self.A1, self.A2)

    def cost(self, Y, A):
        """
        Computes the cost of the neural network
        """
        m = Y.shape[1]
        m_loss = np.sum((Y * np.log(A)) + ((1 - Y) * np.log(1.0000001 - A)))
        cost = (1 / m) * (-(m_loss))
        return (cost)

    def evaluate(self, X, Y):
        """
        Calculates the prediction and cost of the neural network
        """
        A1, A2 = self.forward_prop(X)
        cost = self.cost(Y, A2)
        prediction = np.where(A2 >= 0.5, 1, 0)
        return (prediction, cost)

    def gradient_descent(self, X, Y, A1, A2, alpha=0.05):
        """
        Computes one pass of the gradient descent on the neural network
        """
        m = Y.shape[1]
        dz2 = (A2 - Y)
        d__W2 = (1 / m) * (np.matmul(dz2, A1.transpose()))
        d__b2 = (1 / m) * (np.sum(dz2, axis=1, keepdims=True))
        dz1 = (np.matmul(self.W2.transpose(), dz2)) * (A1 * (1 - A1))
        d__W1 = (1 / m) * (np.matmul(dz1, X.transpose()))
        d__b1 = (1 / m) * (np.sum(dz1, axis=1, keepdims=True))
        self.__W1 = self.W1 - (alpha * d__W1)
        self.__b1 = self.b1 - (alpha * d__b1)
        self.__W2 = self.W2 - (alpha * d__W2)
        self.__b2 = self.b2 - (alpha * d__b2)

    def train(self, X, Y, iterations=5000, alpha=0.05,
              verbose=True, graph=True, step=100):
        """
        Training Function for the neural network
        """
        if type(iterations) is not int:
            raise TypeError("iterations must be an integer")
        if iterations <= 0:
            raise ValueError("iterations must be a positive integer")
        if type(alpha) is not float:
            raise TypeError("alpha must be a float")
        if alpha <= 0:
            raise ValueError("alpha must be positive")
        if verbose or graph:
            if type(step) is not int:
                raise TypeError("step must be an integer")
            if step <= 0 or step > iterations:
                raise ValueError("step must be positive and <= iterations")
        if graph:
            import matplotlib.pyplot as plt
            x_points = np.arange(0, iterations + 1, step)
            points = []
        for itr in range(iterations):
            A1, A2 = self.forward_prop(X)
            if verbose and (itr % step) == 0:
                cost = self.cost(Y, A2)
                print("Cost after " + str(itr) + " iterations: " + str(cost))
            if graph and (itr % step) == 0:
                cost = self.cost(Y, A2)
                points.append(cost)
            self.gradient_descent(X, Y, A1, A2, alpha)
        itr += 1
        if verbose:
            cost = self.cost(Y, A2)
            print("Cost after " + str(itr) + " iterations: " + str(cost))
        if graph:
            cost = self.cost(Y, A2)
            points.append(cost)
            y_points = np.asarray(points)
            plt.plot(x_points, y_points, 'b')
            plt.xlabel("iteration")
            plt.ylabel("cost")
            plt.title("Training Cost")
            plt.show()
        return (self.evaluate(X, Y))
