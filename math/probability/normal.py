#!/usr/bin/env python3
""" defines Normal class that represents a normal distribution """


class Normal:
    """
    class that represents normal distribution

    class constructor:
        def __init__(self, data=None, mean=0., stddev=1.)

    instance attributes:
        mean [float]: the mean of the distribution
        stddev [float]: the standard deviation of the distribution
    """

    def __init__(self, data=None, mean=0., stddev=1.):
        """
        class constructor

        parameters:
            data [list]: data to be used to estimate the distribution
            mean [float]: the mean of the distribution
            stddev [float]: the standard deviation of the distribution

        Sets the instance attributes mean and stddev as floats
        If data is not given:
            Use the given mean and stddev or
            raise ValueError if stddev is not positive or equals to 0
        If data is given:
            Calculate the mean and standard deviation of data
            Raise TypeError if data is not a list
            Raise ValueError if data does not contain at least two data points
        """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = float(sum(data) / len(data))
            self.stddev = float((sum((x - self.mean) ** 2 for x in data) / len(data)) ** 0.5)
