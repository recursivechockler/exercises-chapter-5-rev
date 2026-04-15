from numbers import Number
from math import sin, cos

"""Polish calculator implementation."""


class RPCalc:
    """Polish Calculator class."""

    def __init__(self):
        """Initialise Polish calculator."""
        self.stack = []

    def push(self, n):
        """Push number / operator onto stack."""
        if isinstance(n, Number):
            res = n

        else:
            res = None
            if n == "sin":
                res = sin(self.pop())
            elif n == "cos":
                res = cos(self.pop())
            else:
                a = self.pop()
                b = self.pop()

                if n == "+":
                    res = b + a
                elif n == "*":
                    res = b * a
                elif n == "-":
                    res = b - a
                elif n == "/":
                    res = b / a

        self.stack.append(res)

    def pop(self):
        """Pop and return top item on stack."""
        return self.stack.pop()

    def peek(self):
        """Return top of stack without popping."""
        return self.stack[-1]

    def __len__(self):
        """Return number of items on stack."""
        return len(self.stack)
