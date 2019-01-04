# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 19:04:19 2018

@author: USP
"""

import matplotlib.pyplot as plt

def growth(x):
    return (1. + 1./x)**x

val = []

for n in range(365):
    val.append(growth(n+1))

plt.plot(val)
plt.show()