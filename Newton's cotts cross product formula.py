# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 19:35:46 2019

@author: bell liang
"""

# 牛顿-柯特斯求积公式、复合求积公式、龙贝格求积公式、自适应求积公式

import numpy as np
import math

# 牛顿-柯特斯系数
C = np.array([[1/2, 1/2, 0, 0, 0, 0, 0, 0],
              [1/6, 2/3, 1/6, 0, 0, 0, 0, 0],
              [1/8, 3/8, 3/8, 1/8, 0, 0, 0, 0],
              [7/90, 16/45, 2/15, 16/45, 7/90, 0, 0, 0],
              [19/288, 25/96, 25/144, 25/144, 25/96, 19/288, 0, 0],
              [41/840, 9/35, 9/280, 34/105, 9/280, 9/35, 41/840, 0],
              [751/17280, 3577/17280, 1323/17280, 2989/17280, 2989/17280, 1323/17280, 3577/17280, 3577/17280, 751/17280]
              ])

# 牛顿——柯特斯求积公式
def caculate(a, b, C, f, degree):
    k = np.arange(degree+1)
    x = np.linspace(a, b, degree+1)
    index = degree - 1
    C = C[index]
    result = 0
    for i in k:
        result += C[i] * f(x[i])
    result = (b-a) * result
    return(result)

# 复合求积公式
def caculate_composite(a, b, C, f, degree, n):
    x = np.linspace(a, b, n+1)
    result_sum = 0
    len_x = len(x) - 1
    for j in range(len_x):
        result = caculate(x[j], x[j+1], C, f, degree)
        result_sum += result
    return(result_sum)

# 龙贝格求积公式
def caculate_Romberg(a, b, f, k):
    n = k + 1
    T = np.eye(n)
    h = b - a
    T[0][0] = 1/2 * (f(a) + f(b))
    for i in range(1, n):
        x = np.arange(a+h/2, b, h)
        h = h / 2
        sum = 0
        for j in range(len(x)):
            sum += f(x[j])
        T[i][0] = 1/2 * T[i-1][0] + h * sum
    for i in range(1, n):
        for j in range(i, n):
            T[j][i] = (4 ** i * T[j][i-1] - T[j-1][i-1]) / (4 ** i - 1)
    return(T)

# 自适应求积公式    
def self_adaption_iter(a, b, S, C, f, degree, limit):
    x = np.linspace(a, b, 3)
    s = np.zeros(2)
    result = []
    for i in range(len(x)-1):
        s[i] = (caculate(x[i], x[i+1], C, f, degree))
        print("x[i]: ", x[i], "x[i+1]: ", x[i+1], "s[i]: ", s[i])
    if S - s.sum() < limit:
        print("s.sum(): ", s.sum(), "S: ", S, "\n")
        return(s.sum())
    else:
        for i in range(len(x)-1):
            result.append(self_adaption_iter(x[i], x[i+1], s[i], C, f, degree, limit))
        result_sum = 0
        for i in result:
            result_sum += i
        return(result_sum)

def caculate_self_adaption(a, b, C, f, degree, limit):
    S = caculate(a, b, C, f, degree)
    print("以下为自适应求积公式所求的各个区间：")
    result = self_adaption_iter(a, b, S, C, f, degree, limit)
    print("自适应求积算法完毕!\n")
    return(result)
    
    
def f_x_sin_x(x):
    if x == 0:
        return(1)
    else:
        result = math.sin(x) / x
        return(result)

def f_x_x_3_2(x):
    result = x ** (3/2)
    return(result)

def f_x_1_x_2(x):
    result = 1 / (x ** 2)
    return(result)

result_1 = caculate_composite(0, 1, C, f_x_sin_x, 1, 16)
result_2 = caculate_composite(0, 1, C, f_x_sin_x, 2, 16)
result_3 = caculate_composite(0, 1, C, f_x_sin_x, 3, 16)

Romberg_result = caculate_Romberg(0, 1, f_x_x_3_2, 5)

result_composite = caculate_composite(0.2, 1, C, f_x_1_x_2, 2, 16)

result_self_adaption = caculate_self_adaption(0.2, 1, C, f_x_1_x_2, 2, 0.02)

y = 0.9460831
print(result_1, result_1-y)
print(result_2, result_2-y)
print(result_3, result_3-y)
print(result_composite)
print(result_self_adaption)