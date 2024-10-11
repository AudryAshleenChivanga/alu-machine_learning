#!/usr/bin/env python3
"""Poisson distribution class"""

class Poisson:
    """Represents a Poisson distribution"""


    def __init__(self, data=None, lambtha=1.):
        """
        Class constructor for Poisson distribution.
        
        Parameters:
        - data: list of data to estimate the distribution (optional).
        - lambtha: expected number of occurrences in a given time frame.
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
            
            # Estimate lambtha as the mean of the data
            self.lambtha = float(sum(data) / len(data))

# Example usage
if __name__ == "__main__":
    # Generate a small sample of Poisson-like data manually
    # Example data resembling a Poisson distribution
    data = [4, 5, 6, 5, 4, 5, 3, 6, 5, 5, 4, 6, 5, 7, 4, 5]

    # Creating instance with data
    p1 = Poisson(data)
    print('Lambtha:', p1.lambtha)  # Expected output: Lambtha: (approximate average)

    # Creating instance with lambtha only
    p2 = Poisson(lambtha=5)
    print('Lambtha:', p2.lambtha)  # Expected output: Lambtha: 5.0
