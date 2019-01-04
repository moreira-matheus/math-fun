# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 22:47:41 2018

@author: USP
"""

from math import log
import matplotlib.pyplot  as plt

# ln a = ln (1 + t) = t - (1/2) * t**2 + (1/3) * t**3 - (1/4) * t**4...
# Taylor expansion: for values around a = 1
def iterative_log(a, n):
    log_approx = 0.0
    t = a - 1.
    for i in range(1,n+1, 2):
        log_approx = log_approx + (1./i) * (t**i) - (1./(i+1)) * (t**(i+1))

    return log_approx

N = 100
A = 1.02
approxs = [iterative_log(A,n) for n in range(1,N+1)]


fig = plt.figure()

axis = fig.add_axes([0.2, 0.2, 0.8, 0.8])

axis.set_title('Log approximation: $\ ln(a) = ln (1+t)\ $')

axis.plot(approxs, label='Approximation')
axis.hlines(log(A), 1, N+1, linestyles='dashed', label='Real value a = %.2f'%A)

plt.legend()
plt.show()