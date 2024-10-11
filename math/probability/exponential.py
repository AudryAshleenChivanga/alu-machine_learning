#!/usr/bin/env python3
"""Exponential distribution class"""


class Exponential:
    """Represents an exponential distribution"""

    def __init__(self, data=None, lambtha=1.):
        """
        Class constructor for Exponential distribution.

        Parameters:
        - data: list of data to estimate the distribution.
        - lambtha: expected number of occurrences.
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
            
            # Calculate lambtha as the inverse of the mean of the data
            self.lambtha = 1 / (sum(data) / len(data))


if __name__ == "__main__":
    # Test the Exponential class
    import numpy as np

    np.random.seed(0)
    data = np.random.exponential(0.5, 100).tolist()

    e1 = Exponential(data)
    print('Lambtha:', e1.lambtha)  # Should print the lambtha estimated from the data

    e2 = Exponential(lambtha=2)
    print('Lambtha:', e2.lambtha)  # Should print the provided lambtha: 2.0
