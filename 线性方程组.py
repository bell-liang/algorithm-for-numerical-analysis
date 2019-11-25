# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 19:27:17 2019

@author: bell liang
"""

# 高斯消元法、直接三角分解法、平方法、改进的平方法（对称正定矩阵适用）、追赶法（对三角矩阵适用）求解线性方程组

import numpy as np
import math

def caculate_upper_triangle(A):
    count = len(A) - 1
    for i in range(count):
        index = np.argmax(np.abs(A[i:, i]))
        A[[i, index+i], :] = A[[index+i, i], :]
        row = i + 1
        m = A[row:, i] / A[i, i]
        A[row:, i] = 0
        for j in range(i+1, count+1):
            A[j, row:] = A[j, row:] - A[i, row:] * m[j-i-1]
    return(A)

def caculate_x(A):
    x = np.zeros(len(A[:, 0]))
    count = len(x) + 1
    x[-1] = A[-1, -1] / A[-1, -2]
    for i in range(2, count):
        x[-i] = (A[-i, -1]- A[-i, -i:-1].dot(x[(-i+1):])) / A[-i, -i-1]
    return(x)

def caculate_triangular_factorization(A):
    A[1:, 0] = A[1:, 0] / A[0, 0]
    for i in range(1, len(A)-1):
        for j in range(i, len(A)):
            A[i, j] = A[i, j] - A[i, :i].dot(A[:i, j])
        for j in range(i+1, len(A)):
            A[j, i] = (A[j, i] - A[j, :i].dot(A[:i, i]))
    A[-1, -1] = A[-1, -1] - A[-1, :-1].dot(A[:-1, -1])
    return(A)

def caculate_L_y(A, b):
    y = np.zeros(len(A[:, 0]))
    y[0] = b[0]
    for i in range(1, len(A)):
        y[i] = b[i] - A[i, :i].dot(y[:i])
    return(y)

def caculate_U_x(A, y):
    x = np.zeros(len(A[:, 0]))
    x[-1] = y[-1] / A[-1, -1]
    for i in range(2, len(A)+1):
        x[-i] = (y[-i] - A[-i, (-i+1):].dot(x[(-i+1):])) / A[-i, -i]
    return(x)

def caculate_square_root_method(A):
    A[0, 0] = math.sqrt(A[0, 0])
    A[1:, 0] = A[1:, 0] / A[0, 0]
    A[0, 1:] = A[1:, 0]
    for i in range(1, len(A)-1):
        print(A[i, i] - np.sum(A[i, :i] ** 2))
        A[i, i] = math.sqrt(abs(A[i, i] - np.sum(A[i, :i] ** 2)))
        for j in range(i+1, len(A)):
            A[j, i] = A[j, i] - A[j, :i].dot(A[:i, i])
        A[i, i+1:] = A[i+1:, i]
    A[-1, -1] = math.sqrt(A[-1, -1] - np.sum(A[-1, :-1] ** 2))
    print(A)
    return(A)

def caculate_square_root_method_y(A, b):
    y = np.zeros(len(A))
    y[0] = b[0] / A[0, 0]
    for i in range(1, len(A)):
        y[i] = (b[i] - A[i, :i].dot(y[:i])) / A[i, i]
    return(y)

def caculate_square_root_method_x(A, y):
    x = np.zeros(len(A))
    x[-1] = y[-1] / A[-1, -1]
    for i in range(2, len(A)+1):
        x[-i] = (y[-2] - A[-i, -i:].dot(x[-i:])) / A[-i, -i]
    return(x)
    
def caculate_improved_square_root_method(A):
    A[1:, 0] = A[1:, 0] / A[0, 0]
    A[0, 1:] = A[1:, 0]
    for i in range(1, len(A)-1):
        A[i, i] = A[i, i] - np.sum(A[i, :i] ** 2 * A.diagonal()[:i])
        t = A[:i, i] * A.diagonal()[:i]
        for j in range(i+1, len(A)):
            A[j, i] = (A[j, i] - A[j, :i].dot(t)) / A[i, i]
        A[i, i+1:] = A[i+1:, i]
    A[-1, -1] = A[-1, -1] - np.sum(A[-1, :-1] ** 2 * A.diagonal()[:-1])
    return(A)

def caculate_improved_square_root_method_y(A, b):
    y = np.zeros(len(A[:, 0]))
    y[0] = b[0]
    for i in range(1, len(A)):
        y[i] = b[i] - A[i, :i].dot(y[:i])
    return(y)

def caculate_improved_square_root_method_x(A, y):
    x = np.zeros(len(A[:, 0]))
    x[-1] = y[-1] / A[-1, -1]
    for i in range(2, len(A)+1):
        x[-i] = y[-i] / A[-i, -i] - A[-i, (-i+1):].dot(x[(-i+1):])
    return(x)

def cacualte_chase_method(A):
    A[0, 1] = A[0, 1] / A[0, 0]
    for i in range(1, len(A)-1):
        A[i, i] = A[i, i] - A[i, i-1] * A[i-1, i]
        A[i, i+1] = A[i, i+1] / A[i, i]
    A[-1, -1] = A[-1, -1] - A[-1, -2] * A[-2, -1]
    return(A)

def cacualte_chase_method_y(A, b):
    y = np.zeros(len(A))
    y[0] = b[0] / A[0, 0]
    for i in range(1, len(A)):
        y[i] = (b[i] - A[i, i-1] * y[i-1]) / A[i, i]
    return(y)

def cacualte_chase_method_x(A, y):
    x = np.zeros(len(A))
    x[-1] = y[-1]
    for i in range(2, len(A)+1):
        x[-i] = y[-i] - A[-i, -i+1] * x[-i+1]
    return(x)
    
# page-143-example-2
A1 = np.array([[1., 1., 1., 6.],
              [0., 4., -1., 5.],
              [2., -2., 1., 1.]])

result = caculate_upper_triangle(A1)
x1 = caculate_x(A1)

# page-153-example-5
A2 = np.array([[1., 2., 3.],
               [2., 5., 2.],
               [3., 1., 5.]])
b1 = np.array([14., 18., 20.])

LU = caculate_triangular_factorization(A2)
y2 = caculate_L_y(LU, b1)
x2 = caculate_U_x(LU, y2)

# page-177-practice-10
A3 = np.array([[2., -1., 1.],
               [-1., -2., 3.],
               [1., 3., 1.]])
b3 = np.array([4., 5., 6.])

LDL_T = caculate_improved_square_root_method(A3)
y3 = caculate_improved_square_root_method_y(LDL_T, b3)
x3 = caculate_improved_square_root_method_x(LDL_T, y3)


LL_T = caculate_square_root_method(A3)
y4 = caculate_square_root_method_y(LL_T, b3)
x4 = caculate_square_root_method_x(LL_T, y4)

# page-177-practice-9
A4 = np.zeros((5, 5))
A4[0, 0] = 2.
A4[0, 1] = -1.
for i in range(1, len(A4)-1):
    A4[i, i-1] = -1.
    A4[i, i] = 2.
    A4[i, i+1] = -1.
A4[-1, -2] = -1.
A4[-1, -1] = 2.
b4 = np.zeros(len(A4))
b4[0] = 1
LU = cacualte_chase_method(A4)
y5 = cacualte_chase_method_y(LU, b4)
x5 = cacualte_chase_method_x(LU, y5)
