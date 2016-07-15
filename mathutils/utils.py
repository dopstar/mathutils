""" Some math utilities """

import math
import time
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


def decode_rsa_id(id_number):
    """
    Validate and decode RSA id number for Republic of South Africa

    :param id_number: ID Number string.
    Returns: Object
    """
    if not isinstance(id_number, basestring):
        raise TypeError("The ID number should be a string not of type: %s" % str(type(id_number)))
    params = {}
    id_number = ''.join(c for c in id_number if c)
    if not len(id_number) == 13:
        raise ValueError("The ID number should be of length 13.")

    date_of_birth = id_number[:6]
    try:
        tt = time.strptime(date_of_birth, '%y%m%d')  # time tuple
        if not isinstance(tt, time.struct_time):
            raise ValueError
    except ValueError:
        raise ValueError('First 6 digits must be the valid date.')

    valid = 10 - int(
        str(sum(int(i) for i in id_number[:-1:2] + str(2 * int(id_number[1::2]))))[-1]
    ) % 10 == int(id_number[-1])

    if not valid:
        raise ValueError("The ID number is not valid.")

    gender = 'Male' if int(id_number[6]) > 4 else 'Female'
    nationality = 'South African' if not int(id_number[10]) else 'Unknown'
    params = {
        'id': id_number,
        'dob': date_of_birth,
        'is_valid': valid,
        'nationality': nationality,
        'gender': gender
    }
    return type('ID#{0}'.format(id_number), (), params)
