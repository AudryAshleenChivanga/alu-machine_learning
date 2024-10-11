#!/usr/bin/env python3
""" defines Exponential class that represents exponential distribution """


class Exponential:
    """
    class that represents exponential distribution

    class constructor:
        def __init__(self, data=None, lambtha=1.)

    instance attributes:
        lambtha [float]: the expected number of occurrences in a given time

    instance methods:
        def pdf(self, x): calculates PDF for given time period
        def cdf(self, x): calculates CDF for given time period
    """

    def __init__(self, data=None, lambtha=1.):
        """
        class constructor

        parameters:
            data [list]: data to be used to estimate the distribution
            lambtha [float]: the expected number of occurrences on a given time

        Sets the instance attribute lambtha as a float
        If data is not given:
            Use the given lambtha or
            raise ValueError if lambtha is not a positive value
        If data is given:
            Calculate the lambtha of data
            Raise TypeError if data is not a list
            Raise ValueError if data does not contain at least two data points
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = 1 / (sum(data) / len(data))

    def pdf(self, x):
        """
        calculates the value of the PDF for a given time period

        parameters:
            x [int]: time period
                If x is out of range, return 0

        return:
            the PDF value for x
        """
        if x < 0:
            return 0
        e = 2.7182818285
        return self.lambtha * (e ** (-self.lambtha * x))

    def cdf(self, x):
        """
        calculates the value of the CDF for a given time period

        parameters:
            x [int]: time period
                If x is out of range, return 0

        return:
            the CDF value for x
        """
        if x < 0:
            return 0
        e = 2.7182818285
        return 1 - (e ** (-self.lambtha * x))
