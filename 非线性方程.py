# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 19:46:26 2019

@author: bell liang
"""

# 解非线性方程组之二分法、牛顿法、简化牛顿法、牛顿下山法、重根情形下的牛顿法
import math

def caculate_dichotomy(f, a, b, limit):
    y_a = f(a)
    x_mid = (a + b) / 2.
    y_mid = f(x_mid)
    while y_mid != 0 and abs(a - x_mid) > limit:
        if y_mid * y_a < 0:
            b = x_mid
        else:
            a = x_mid
        y_a = f(a)
        x_mid = (a + b) / 2.
        y_mid = f(x_mid)
        print(x_mid, y_mid)
    return(x_mid)

def caculate_newton_method(f, f_dor, x0, limit):
    x_k = x0 - f(x0) / f_dor(x0)
    while abs(x_k - x0) > limit:
        x0 = x_k
        x_k = x0 - f(x0) / f_dor(x0)
        print(x_k, abs(x_k - x0))
    return(x_k)

def caculate_reduced_newton_method(f, f_dor, x0, limit):
    x_k = x0 - f(x0) / f_dor(x0)
    f_dor_x0 = f_dor(x0)
    while abs(x_k - x0) > limit:
        x0 = x_k
        x_k = x0 - f(x0) / f_dor_x0
        print(x_k, abs(x_k - x0))
    return(x_k)

def caculate_newton_downhill_method(f, f_dor, x0, limit):
    p = 1
    x_k = x0 -  p * f(x0) / f_dor(x0)
    while abs(f(x_k)) >= abs(f(x0)):
        p = p / 2
        x_k = x0 -  p * f(x0) / f_dor(x0)
        print(x_k)
    while abs(x_k - x0) > limit:
        p = 1
        x0 = x_k
        x_k = x0 - p * f(x0) / f_dor(x0)
        while abs(f(x_k)) >= abs(f(x0)):
            p = p / 2
            x_k = x0 -  p * f(x0) / f_dor(x0)
            print(x_k)
        print(x_k, abs(x_k - x0))
    return(x_k)

def caculate_newton_method_repeated_root(f, f_dor, f_dor_2, x0, limit):
    x_k = x0 - f(x0) * f_dor(x0) / (f_dor(x0)) ** 2 - f(x0) * f_dor_2(x0)
    while abs(x_k - x0) > limit:
        x0 = x_k
        x_k = x0 - f(x0) * f_dor(x0) / ((f_dor(x0)) ** 2 - f(x0) * f_dor_2(x0))
        print(x_k, abs(x_k - x0))
    return(x_k)

# page-214-example-2
def f1(x):
    return(x ** 3 - x -1)
def f1_dor(x):
    return(3 * x ** 2 - 1)
    
a1 = 1.0
b1 = 1.5
limit1 = 0.005
x1 = 1.2
x2 = 0.6

y1 = caculate_dichotomy(f1, a1, b1, limit1)
print("\n")
y3 = caculate_reduced_newton_method(f1, f1_dor, x1, limit1)
print("\n")
y4 = caculate_newton_downhill_method(f1, f1_dor, x2, limit1)
print("\n")

# page-223-example-7
def f2(x):
    return(x * math.exp(x) - 1)

def f2_dor(x):
    return((1 + x) * math.exp(x))

x0 = 0.5
limit2 = 0.001

y2 = caculate_newton_method(f2, f2_dor, x0, limit2);

# page-227-example-9
def f3(x):
    return(x ** 4 - 4 * (x ** 2) + 4)

def f3_dor(x):
    return(4 * x ** 3 - 8 * x)

def f3_dor_2(x):
    return(12 * x ** 2 - 8)

x3 = 1.5
limit3 = 0.00000001
y5 = caculate_newton_method_repeated_root(f3, f3_dor, f3_dor_2, x3, limit3)
