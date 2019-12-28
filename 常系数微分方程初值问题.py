# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 19:30:31 2019

@author: liang
"""

import numpy as np
import matplotlib.pyplot as plt

def caculate_Euler_method(a, b, y0, f, h):
    x = np.arange(a, b+h, h)
    y = [1.]
    temp = y0
    for i in range(len(x)-1):
        temp = temp + h * f(x[i], temp)
        y.append(temp)
    return(x, y)

def caculate_improved_Euler_method(a, b, y0, f, h):
    x = np.arange(a, b+h, h)
    y = [1.]
    temp = y0
    for i in range(len(x)-1):
        y_p = temp + h * f(x[i], temp)
        y_c = temp + h * f(x[i+1], y_p)
        temp = (y_p + y_c) / 2
        y.append(temp)
    return(x, y)
    

# page-281-example-1
def f1(x, y):
    return(y - 2 * x / y)
a = 0
b = 1
y0 = 1
h = 0.1
x1, y1 = caculate_Euler_method(a, b, y0, f1, h)

# page-284-example-2
def f2(x, y):
    return(y - 2 * x / y)
a = 0
b = 1
y0 = 1
h = 0.1
x2, y2 = caculate_improved_Euler_method(a, b, y0, f2, h)

plt.plot(x1, y1, 'r')
plt.plot(x2, y2, 'b')
plt.show()