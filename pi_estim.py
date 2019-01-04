# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 18:30:35 2018

@author: USP
"""

import random
import math
import matplotlib.pyplot as plt

n_circ = 0
N = 15000

xs, ys = [], []
colors = []
estims = []

for n in range(N):
    x, y = random.random(), random.random()
    c = 'blue'
    if (x**2 + y**2) <= 1.0:
        n_circ = n_circ + 1
        c = 'red'

    colors.append(c)
    xs.append(x)
    ys.append(y)
    estims.append(4.0*n_circ/(n+1))

plt.figure(1, figsize=(8,6))

plt.plot(estims)
plt.hlines(math.pi, 0, N)
plt.show()

plt.figure(2, figsize=(8,8))

plt.scatter(xs,ys, c=colors, alpha=0.5)
plt.show()