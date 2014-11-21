""" Fibonacci number generator. """

from collections import deque


def fibonacci():
    """
    Generates an infinite sequence of fibonacci numbers
    """

    fibs = deque()
    while True:
        if len(fibs) < 2:
            fib = len(fibs) + 1
        else:
            fib = sum(fibs)
            fibs.popleft()
        fibs.append(fib)
        yield fib
