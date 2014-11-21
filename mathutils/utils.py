""" Fibonacci number generator. """

from collections import deque


def fibonacci():
    """
    Generates an infinite sequence of fibonacci numbers
    """

    fibs = deque(maxlen=2)
    while True:
        fibs.append(sum(fibs) if len(fibs) >= 2 else len(fibs) + 1)
        yield fibs[-1]
