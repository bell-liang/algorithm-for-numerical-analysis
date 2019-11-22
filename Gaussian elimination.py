# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 19:27:17 2019

@author: bell liang
"""

# 高斯消元法、直接三角分解法求解线性方程组

import numpy as np

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
    L = np.eye(len(A))
    for i in range(1, len(L)):
        L[i, :i] = A[i, :i]
    y = np.zeros(len(L[:, 0]))
    y[0] = b[0]
    for i in range(1, len(L)):
        y[i] = b[i] - L[i, :i].dot(y[:i])
    return(y)

def caculate_U_x(A, y):
    for i in range(1, len(A)):
        A[i, :i] = 0
    U = A
    x = np.zeros(len(U[:, 0]))
    x[-1] = y[-1] / U[-1, -1]
    for i in range(2, len(U)+1):
        x[-i] = (y[-i] - U[-i, (-i+1):].dot(x[(-i+1):])) / U[-i, -i]
    return(x)

A = np.array([[1., 1., 1., 6.],
              [0., 4., -1., 5.],
              [2., -2., 1., 1.]])
A1 = np.array([[1., 2., 3.],
               [2., 5., 2.],
               [3., 1., 5.]])
b = np.array([14., 18., 20.])

result = caculate_upper_triangle(A)
x = caculate_x(A)
LU = caculate_triangular_factorization(A1)
y = caculate_L_y(LU, b)
x1 = caculate_U_x(LU, y)
    