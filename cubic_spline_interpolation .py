# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# 三次样条插值

import numpy as np
import matplotlib.pyplot as plt

def parameter_h(x):
    h = np.diff(x)
    print("h: ", h)
    return(h)

def parameter_μ(h):
    len_h = len(h)
    μ = np.zeros(len_h)
    for i in range(0, len_h-1):
        μ[i] = h[i] / (h[i] + h[i+1])
    μ[len_h-1] = 1
    print("μ: ", μ)
    return(μ)

def parameter_λ_1(h):
    len_h = len(h)
    λ = np.zeros(len_h)
    for i in range(1, len_h):
        λ[i] = h[i] / (h[i-1] + h[i])
    λ[0] = 1
    print("λ: ", λ)
    return(λ)

def parameter_λ_2(μ):
    len_h = len(μ)
    λ = np.zeros(len_h)
    for i in range(1, len_h):
        λ[i] = 1 - μ[i]
    λ[0] = 1
    return(λ)

def c_sum(x, length):
    y_len = len(x) - length + 1
    y = np.zeros(y_len)
    for i in range(0, y_len):
        for j in range(0, length):
            y[i] += x[i+j]
    return(y)

def parameter_f(x, y):
    len_x = len(x)
    f = np.zeros(len_x)
    x = np.diff(x)
    y = np.diff(y) / c_sum(x, 1)
    f[0] = y[0]
    f[len_x-1] = y[len_x-2]
    y = np.diff(y) / c_sum(x, 2)
    for i in range(1, len_x-1):
        f[i] = y[i-1]
    print("f: ", f)
    return(f)

def parameter_d(s, h, f):
    len_d = len(f)
    d = np.zeros(len_d)
    d[0] = 6 * (f[0] - s[0]) / h[0]
    for i in range(1, len_d-1):
        d[i] = 6 * f[i]
    d[len_d-1] = 6 * (s[1] - f[len_d-1]) / h[len_d-2]
    print("d: ", d)
    return(d)

def parameter_m(μ, λ, d):
    len_m = len(d)
    A = np.eye(len_m) * 2
    for i in range(0, len_m-1):
        A[i+1][i] = μ[i]
        A[i][i+1] = λ[i]
    print("A: ", A, A.shape)
    m = np.linalg.inv(A).dot(d.reshape(len_m, 1))
    print("m: ", m)
    return(m)

def find_x_i(x, x_pre):
    len_x = len(x)
    for i in range(0, len_x - 2):
        if x_pre < x[i+1]:
            print("i: ", i)
            return(i)

def calcute(x, y, s, x_pre):
    h = parameter_h(x)
    μ = parameter_μ(h)
    λ = parameter_λ_1(h)
    f = parameter_f(x, y)
    d = parameter_d(s, h, f)
    m = parameter_m(μ, λ, d).ravel()
    print("m: ", m)
    
    len_x_pre = len(x_pre)
    len_sol = int(len_x_pre * 4 / 5)
    result = np.zeros(len_sol)
    num = 0
    for j in range(len_sol):
        i = find_x_i(x, x_pre[j])
        num += 1
        print("次数：", num)
        x_find = x_pre[j]
        result[j] = (m[i] * ((x[i+1] - x_find) ** 3) / 6 \
                    + m[i+1] * (x_find - x[i]) ** 3 / 6 \
                    + (y[i] - m[i] * (h[i] ** 2) / 6) * (x[i+1] - x_find) \
                    + (y[i+1] - m[i+1] * (h[i] ** 2) / 6) * (x_find - x[i])) / h[i]
        print(result[j])
    print(result)
    return(result)    

x = np.arange(-5, 6, 1)
y = np.array([0.03846, 0.05882, 0.1, 0.2, 0.5, 1, 0.5, 0.2, 0.1, 0.05882, 0.03846])
s = np.array([10/(26 ** 2), -10/(26 ** 2)])

x1 = np.array([27.7, 28, 29, 30])
y1 = np.array([4.1, 4.3, 4.1, 3.0])
s1 = np.array([3.0, -4.0])

c_x = np.arange(-5, 5.2, 0.1)

c_y = calcute(x, y, s, c_x)

len_show = len(c_y)
plt.plot(c_x[0:len_show], c_y, color='r')
plt.plot(x, y, color='b')
plt.show()

