""" Some math utilities """

from collections import deque


def fibonacci():
    """
    Generates an infinite sequence of fibonacci numbers
    """

    fibs = deque(maxlen=2)
    while True:
        fibs.append(sum(fibs) if len(fibs) == 2 else len(fibs) + 1)
        yield fibs[-1]


def zeckendorf(number):
    """
    Generates Zeckendorf's representation of the given number
    """

    fibonacci_numbers = []
    for fib in fibonacci():
        if fib > number:
            break
        fibonacci_numbers.append(fib)

    zeckendorf_numbers = []
    candidate = sum(zeckendorf_numbers)
    while candidate < number:
        for fib in reversed(fibonacci_numbers):
            if candidate + fib <= number and fib not in zeckendorf_numbers:
                zeckendorf_numbers.append(fib)
                candidate = sum(zeckendorf_numbers)
    return zeckendorf_numbers
