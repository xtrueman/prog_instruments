"""Project Euler problem 7 solve"""
from __future__ import print_function
import math
import sys


def is_prime(num):
    """Checks if num is prime number"""
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def get_prime_numbers(count):
    """Get 'count' prime numbers"""
    prime_numbers = [2]
    next_number = 3

    while len(prime_numbers) < count:
        if is_prime(next_number):
            prime_numbers.append(next_number)
        next_number += 1

    return prime_numbers


if __name__ == '__main__':
    try:
        count = int(sys.argv[1])
    except (TypeError, ValueError, IndexError):
        sys.exit("Usage: euler_7.py number")
    if count < 1:
        sys.exit("Error: number must be greater than zero")

    prime_numbers = get_prime_numbers(count)
    print("Answer: %d" % prime_numbers[-1])