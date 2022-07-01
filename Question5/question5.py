#!/usr/bin/env python


def isPrimeNumber_v1 (n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
        else:
            return True

def isPrimeNumber_v2 (n):
    xrange = range
    return 0 not in map(lambda i: n % i, xrange(2, int(n**0.5+1)))