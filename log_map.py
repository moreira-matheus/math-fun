# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 09:07:22 2018

@author: USP
"""

import random
import matplotlib.pyplot as plt

def logistic_map(lamb, x0):
    return lamb * x0 * (1. - x0)

random.seed(4)

T = 100

results = []
lambs = [i - random.random() for i in [1,2,3,4]]

for lamb in lambs:
    res = [0.5]
    for t in range(T):
        res.append(logistic_map(lamb, res[-1]))

    results.append(res)

plt.title('$ x_{t+1}\ =\ \lambda (1 - x_{t}) \quad\quad [x_0 = 0.5] $')
for lamb, res in zip(lambs, results):
    plt.plot(res, label='$\lambda$ = %.2f'%(lamb))

plt.xlabel('Time steps ($t$)')
plt.ylabel('Population ($x$)')
plt.ylim([0.0, 1.0])
plt.legend()
plt.savefig('verhulst.png')