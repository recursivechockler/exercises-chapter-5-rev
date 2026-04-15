"""Implement Fibonacci numbers."""


class Fib:
    """Find Fibonacci numbers."""

    def __init__(self):
        """Initialise the Fib numbers."""
        self.t1, self.t2 = 1, 2

    def __iter__(self):
        """Return iterator."""
        return self

    def __next__(self):
        """Return next Fib number."""
        val = self.t1
        self.t1, self.t2 = self.t2, self.t1 + self.t2
        return val
