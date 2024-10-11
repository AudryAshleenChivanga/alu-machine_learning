#!/usr/bin/env python3
"""Poisson distribution class"""

class Poisson:
    """Represents a Poisson distribution"""

    def __init__(self, data=None, lambtha=1.):
        """
        Class constructor for Poisson distribution.
        
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
                raise ValueError("data must have multiple values")
            
            # Estimate lambtha as the mean of the data
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """
        Calculates the PMF for a given number of successes k.
        
        Parameters:
        - k: number of successes
        
        Returns:
        - PMF value for k
        """
        if not isinstance(k, int):
            k = int(k)
        
        if k < 0:
            return 0
        
        return (self.lambtha ** k *
                self._euler_exp(-self.lambtha)) / self._factorial(k)

    def _factorial(self, k):
        """Calculates the factorial of k."""
        if k == 0 or k == 1:
            return 1
        result = 1
        for i in range(2, k + 1):
            result *= i
        return result

    def _euler_exp(self, x):
        """Approximates Euler's number raised to a power."""
        n = 50  # Higher value gives better precision
        result = 1.0
        term = 1.0
        for i in range(1, n + 1):
            term *= x / i
            result += term
        return result

# Example usage
if __name__ == "__main__":
    # Poisson-like data sample
    data = [4, 5, 6, 5, 4, 5, 3, 6, 5, 5, 4, 6, 5, 7, 4, 5]

    # Instance with data
    p1 = Poisson(data)
    print(f'P(9): {p1.pmf(9):.10f}')  # Output to 10 decimal places

    # Instance with lambtha
    p2 = Poisson(lambtha=5)
    print(f'P(9): {p2.pmf(9):.10f}')  # Output to 10 decimal places
