""" Some math utilities """

import math
from collections import Counter

from constants import gr


def fibonacci():
    """
    Generates an infinite sequence of fibonacci numbers
    """

    F_0, F_1 = 0, 1
    yield F_0
    yield F_1
    while True:
        F_0, F_1 = F_1, F_0 + F_1
        yield F_1


def is_fibonacci(number):
    """
    Checks whether the given number is a fibonacci number
    """

    is_fib = False
    for fib in fibonacci():
        is_fib = fib == number
        if is_fib or fib > number:
            break
    return is_fib


def zeckendorf(number, binary=False):
    """
    Generates Zeckendorf's representation of the given number
    """

    fibonacci_numbers = []
    for fib in fibonacci():
        if fib > number:
            break
        if fib > 0 and fib not in fibonacci_numbers:
            fibonacci_numbers.append(fib)

    zeckendorf_numbers = []
    zeckendorf_representation = Counter()
    candidate = sum(zeckendorf_numbers)
    while candidate < number:
        for fib in reversed(fibonacci_numbers):
            if candidate + fib <= number and fib not in zeckendorf_numbers and fib > 0:
                zeckendorf_numbers.append(fib)
                zeckendorf_representation[fib] = 1
                candidate = sum(zeckendorf_numbers)
    if binary:
        sequence = [str(zeckendorf_representation[fib]) for fib in reversed(fibonacci_numbers)]
        return ''.join(sequence)
    return zeckendorf_numbers


def binet(n):
    """
    Binet's Formula
    :param n: integer number
    :return: the n-th Fibonacci number
    """
    return int((gr**n - (-gr)**(-n)) / math.sqrt(5))


def F(n):
    """
    Alias for binet()
    """
    return binet(n)


def zeckendorf_to_decimal(representation):
    """
    Converts Zeckendorf representation binary sequence into a decimal integer
    :param representation: Zeckendorf representation binary sequence string.
    :return: integer.
    """

    number = 0
    for n, digit in zip(xrange(len(representation) + 1, 1, -1), (int(r) for r in representation)):
        number += digit * F(n)
    return number


def factorial(n):
    """
    Calculates the factorial of the non-negative integer
    """

    if not isinstance(n, (int, long)):
        raise TypeError("The input must be an integer")
    if n < 0:
        raise ValueError("The input must not be negative")
    if n == 0:
        return 1
    return n * factorial(n - 1)

