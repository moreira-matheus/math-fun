# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 18:44:28 2018

@author: USP
"""

import matplotlib.pyplot as plt

def is_prime(n):
    limit = int(n/2) + 1
    factor = 2
    prime = True
    
    if n == 2:
        return True
    
    while prime and factor <= limit:
        if (n % factor) == 0:
            prime = False
        factor += 1

    return prime

def yield_prime(N):
    for n in range(2,N):
        if is_prime(n):
            yield n

primes = [p for p in yield_prime(100)]

plt.scatter(range(len(primes)), primes)
plt.show()