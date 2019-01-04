# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 22:01:38 2018

@author: USP
"""

from random import uniform
import matplotlib.pyplot as plt


def mandelbrot_func(z,c):
    '''
    Evaluates the Mandelbrot function for the provided values of z and c.
    '''
    return z**2 + c

def is_mandelbrot(c, T, z=0):
    '''
    Checks if c is in the Mandelbrot set.
    '''
    current_z = z
    in_set = True

    for _ in range(T):
        current_z = mandelbrot_func(current_z, c)
        in_set = in_set and (abs(current_z) <= 2.)

    return in_set

    
# Colors for Mandelbrot and not Mandelbrot numbers, respectively
color1, color2 = 'black', 'blue'

# Number of c's
N = 200000
cs = [complex(uniform(-2,1),uniform(-1.5,1.5)) for _ in range(N)]

# Number of iterations
T = 10

colors = [color1 if is_mandelbrot(c,T) else color2 for c in cs]

reals, imags = zip(*[(c.real, c.imag) for c in cs])

plt.figure(figsize=(8,6))
plt.title('Mandelbrot Set')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.scatter(reals, imags, s=25, c=colors, alpha=.25)
plt.savefig('mandelbrot_set.png')