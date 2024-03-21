#!/usr/bin/python3
"""
implement a minimum operations algorithm
"""


def prime_factors(n):
    """
    Get prime numbers
    """
    all_primes = [0 for i in range(n+1)]
    all_primes[1] = 1
    for i in range(2, n+1):
        all_primes[i] = i
    for i in range(4, n+1, 2):
        all_primes[i] = 2

    for i in range(3, int(n**0.5)+1):
        if all_primes[i] == i:
            for j in range(i*i, n+1, i):
                if all_primes[j] == j:
                    all_primes[j] = i

    nums = 0

    while n != 1:
        nums = all_primes[n] + nums
        n = n // all_primes[n]
    return nums


def minOperations(n):
    """
    implement a minimum operations algorithm
    """
    return prime_factors(n)
