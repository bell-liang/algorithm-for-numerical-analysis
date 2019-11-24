# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 20:17:59 2019

@author: bell liang
"""

# 曲线拟合的最小二乘法

import numpy as np
import matplotlib.pyplot as plt

def parameter_m(x, w, n):
    m = np.eye(n)
    x = x.T
    for i in range(n):
        for j in range(i, n):
            m[i][j] = w.dot(x ** (i+j))
    for i in range(1, n):
        for j in range(i):
            m[i][j] = m[j][i]
    print("m: ", m)
    return(m)
    
def parameter_d(x, y, w, n):
    d = np.zeros(n)
    for i in range(n):
        d[i] = (w * (x ** i) * y).sum()
    print("d: ", d)
    return(d)
    
def parameter_a(m, d):
    n = len(d)
    a = np.linalg.inv(m).dot(d.reshape(n, 1))
    print("a: ", a)
    return(a)
    
def caculate(x, y, w, n):
    n += 1
    m = parameter_m(x, w, n)
    d = parameter_d(x, y, w, n)
    a = parameter_a(m, d)
    y = np.zeros(x.shape)
    x = np.arange(x[0], x[-1], 0.1)
    y = np.zeros(x.shape)
    for i in range(len(a)):
        y += a[i] * (x ** i)
    print("y: ", y)
    return(y)

x = np.arange(1,6,1)
y = np.array([4, 4.5, 6, 8, 8.5])
w = np.array([2, 1, 3, 1, 1])
n = 1
 
result = caculate(x, y, w, n)

plt.scatter(x, y)
plt.plot(np.arange(x[0], x[-1], 0.1), result)
plt.show()

