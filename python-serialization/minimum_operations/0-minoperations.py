#!/usr/bin/python3
"""Module for calculating minimum operations."""


def minOperations(n):
    """Calculate fewest number of operations to reach n H characters."""
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
