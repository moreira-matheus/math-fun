# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 18:05:04 2018

@author: USP
"""

import matplotlib.pyplot as plt

def bday_prob(n):
    prob = 1.0
    for i in range(1,n):
        prob *= (365 - i)/365

    return (1. - prob)

probs = []
for i in range(1,366):
    probs.append(bday_prob(i))

plt.plot(probs)
plt.show()