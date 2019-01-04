# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 13:58:42 2018

@author: USP
"""

import random
import matplotlib.pyplot as plt

def exp_pow_num(x):
    return x**x

def exp_pow_den(x):
    return x**(1./x)

N = 20000
x_low, x_high = 10**(-6), 2

x = sorted([random.uniform(x_low, x_high) for _ in range(N)])
y_num = [exp_pow_num(i) for i in x]
y_den = [exp_pow_den(i) for i in x]

plt.figure(1)

plt.plot(x,y_num, label='$ f(x) = x^{x} $')
plt.plot(x,y_den, label='$ f(x) = x^{1/x} $')

plt.legend()
plt.show()
