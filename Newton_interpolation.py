# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# 牛顿差分表插值算法

import numpy as np
import matplotlib.pyplot as plt


def c_sum(x, length):
    y_len = len(x) - length + 1
    y = np.zeros(y_len)
    for i in range(0, y_len):
        for j in range(0, length):
            y[i] += x[i + j]
    return (y)


def parameter(x, y):
    result = np.zeros(len(x))
    result[0] = y[0]
    x = np.diff(x)
    for i in range(1, 6):
        y = np.diff(y) / c_sum(x, i)
        print(y)
        result[i] = y[0]
    return(result)


def calcute(x_cal, x, parameter, degree):
    y = parameter[0]
    mid_v = 1
    for i in range(0, degree):
        mid_v *= (x_cal - x[i])
        y += parameter[i + 1] * mid_v
    return (y)


x = np.array([0.40, 0.55, 0.65, 0.80, 0.90, 1.05])
y = np.array([0.41075, 0.57815, 0.69675, 0.88811, 1.02652, 1.25382])

c_x = np.arange(0.4, 1.1, 0.05)
c_y = np.zeros(len(c_x))
degree = 4

c_parameter = parameter(x, y)
for i in range(0, len(c_x)):
    c_y[i] = calcute(c_x[i], x, c_parameter, degree)

plt.plot(c_x, c_y)
plt.plot(x, y)
plt.show()

