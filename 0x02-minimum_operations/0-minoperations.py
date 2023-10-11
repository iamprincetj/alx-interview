#!/usr/bin/env python3
""" Minimum Operations """

def minOperations(n):
    """ Minimum Operations """
    if n <= 1:
        return 0
    i = 2
    res = 0
    while i <= n:
        if n % i == 0:
            res += i
            n = n / i
        else:
            i += 1
    return res
