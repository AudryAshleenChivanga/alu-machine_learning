#!/usr/bin/env python3
""" defines Binomial class that represents a binomial distribution """


class Binomial:
    """
    class that represents a binomial distribution

    class constructor:
        def __init__(self, data=None, n=1, p=0.5)

    instance attributes:
        n [int]: number of Bernoulli trials
        p [float]: probability of success

    instance methods:
        None
    """

    def __init__(self, data=None, n=1, p=0.5):
        """
        class constructor

        parameters:
            data [list]: data to be used to estimate the distribution
            n [int]: number of Bernoulli trials
            p [float]: probability of success

        Sets the instance attributes n and p
        If data is not given:
            Use the given n and p
            Raise ValueError if n is not a positive value
            Raise ValueError if p is not a valid probability
        If data is given:
            Calculate n and p from data
            Round n to the nearest integer (rounded, not casting)
            Raise TypeError if data is not a list
            Raise ValueError if data does not contain at least two data points
        """
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if not (0 < p < 1):
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                # Calculate p from data
                p = sum(data) / (len(data) * max(data))
                # Calculate n by rounding the total number of trials
                self.n = round(max(data))
                # Recalculate p based on n
                self.p = p

# Example Usage (In another file like 10-main.py):
if __name__ == "__main__":
    import numpy as np

    np.random.seed(0)
    data = np.random.binomial(50, 0.6, 100).tolist()
    b1 = Binomial(data)
    print('n:', b1.n, "p:", b1.p)

    b2 = Binomial(n=50, p=0.6)
    print('n:', b2.n, "p:", b2.p)
