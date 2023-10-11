#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n: int) -> int:
    """ Minimum Operations """
    if n <= 1 or isinstance(n, int) is False:
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
