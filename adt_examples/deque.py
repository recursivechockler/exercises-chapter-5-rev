"""Deque Implementation."""


class Deque:
    """Double-ended queue class."""

    def __init__(self, n):
        """Initialise deque."""
        self.n = n
        self.buffer = [None] * n
        self.left = 0
        self.right = 0
        self.size = 0

    def append(self, x):
        """Append to right of deque."""
        self.buffer[self.right] = x
        self.right = (self.right + 1) % self.n
        self.size += 1

    def appendleft(self, x):
        """Append to left of deque."""
        self.left = (self.left - 1) % self.n
        self.buffer[self.left] = x
        self.size += 1

    def pop(self):
        """Remove last item in queue and return it."""
        self.right = (self.right - 1) % self.n
        val = self.buffer[self.right]
        self.buffer[self.right] = None
        self.size -= 1
        return val

    def popleft(self):
        """Remove first item in queue and return it."""
        val = self.buffer[self.left]
        self.buffer[self.left] = None
        self.left = (self.left + 1) % self.n
        self.size -= 1
        return val

    def peek(self):
        """Peek at end of queue."""
        return self.buffer[(self.right - 1) % self.n]

    def peekleft(self):
        """Peek at start of queue."""
        return self.buffer[self.left]

    def __len__(self):
        """Return length of queue."""
        return self.size

    def __iter__(self):
        """Return deque iterator."""
        return DQIterator(self)


class DQIterator:
    """Deque iterator class."""

    def __init__(self, dq):
        """Initialise Deque."""
        self.dq = dq
        self.pos = dq.left
        self.count = 0
        self.length = len(dq)

    def __iter__(self):
        """DQ iterator."""
        return self

    def __next__(self):
        """Return next item in iteration, if there is one."""
        if self.count >= self.length:
            raise StopIteration
        val = self.dq.buffer[self.pos]
        self.pos = (self.pos + 1) % self.dq.n
        self.count += 1
        return val
