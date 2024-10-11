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
    import numpy as np

    np.random.seed(0)
    data = np.random.poisson(5., 100).tolist()
    
    # Creating instance with data
    p1 = Poisson(data)
    print('Lambtha:', p1.lambtha)  # Expected output: Lambtha: 4.84
    
    # Creating instance with lambtha only
    p2 = Poisson(lambtha=5)
    print('Lambtha:', p2.lambtha)  # Expected output: Lambtha: 5.0
