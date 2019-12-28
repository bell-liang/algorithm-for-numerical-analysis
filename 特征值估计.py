# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 19:17:49 2019

@author: bell liang
"""
# 特征值估计之幂法、反幂法
import numpy as np
import math

def caculate_power_method(A, v0, k):
    u = v0
    for i in range(k):
        v = A.dot(u.T)
        m = np.max(v)
        u = v / m
#        if (i+1) % 5 == 0:
#            print("k:", i+1, '\n', v,'\n', m, '\n', u)
        print("k:", i+1, '\n', v,'\n', m, '\n', u)
    return m

def caculate_power_method_origin_translation(A, v0, k, p):
    B = A - p * np.eye(len(A))
    u = v0
    for i in range(k):
        v = B.dot(u.T)
        m = np.max(v)
        u = v / m
#        if (i+1) % 5 == 0:
#            print("k:", i+1, '\n', v,'\n', m, '\n', u)
        print("k:", i+1, '\n', v,'\n', m, '\n', u)
    return m + p

def caculate_inverse_power_method(A, P, v0, k, p):
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
    B = P.dot(A - p * np.eye(len(A)))
    u = v0
    B = caculate_triangular_factorization(B)
    for i in range(k):
        v = caculate_U_x(B, caculate_L_y(B, u))
        m = np.max(v)
        u = v / m
#        if (i+1) % 5 == 0:
#            print("k:", i+1, '\n', v,'\n', m, '\n', u)
        print("k:", i+1, '\n', v,'\n', m, '\n', u)
    return 1 / m + p

def caculate_householder_transformation(x):
    x = x.reshape(-1, 1).copy()
    a = x[0] / abs(x[0]) * math.sqrt(sum(x ** 2))
    x[0] += a
    u = x
    b = 1 / 2 * sum(u ** 2)
    return np.eye(len(x)) - 1 / b * u.dot(u.T)

def caculate_QR_decompose(A):
    H = caculate_householder_transformation(A[0:, 0])
    print("H1:", H)
    R = H.dot(A)
    Q = H
    print(A)
    print("R:", R)
    for i in range(1, len(A)-1):
        H = np.eye(len(A))
        H[i:, i:] = caculate_householder_transformation(R[i:, i])
        print("H", i+1, H)
        R = H.dot(R)
        print(R)
        Q = H.dot(Q)
    return(-(Q.T), -R)
    

# page-248-example-2
A = np.array([[1., 1., 0.5],
              [1., 1., 0.25],
              [0.5, 0.25, 2.]])
v0 = np.array([1., 1., 1.])
k = 20
u = caculate_power_method(A, v0, k)

# page-250-example-4
p = 0.75
k1 = 10
u1 = caculate_power_method_origin_translation(A, v0, k1, p)

# page-253-example-5
A1 = np.array([[2., 1., 0.],
               [1., 3., 1.],
               [0., 1., 4.]])
P = np.array([[0., 1., 0.],
              [0., 0., 1.],
              [1., 0., 0.]])
v0 = np.array([1., 1., 1.])
k2 = 3
p1 = 1.2679
u2 = caculate_inverse_power_method(A1, P, v0, k2, p1)

# page-256-example-6
x = np.array([3., 5., 1., 1.])
H = caculate_householder_transformation(x)

# page-260-example-7
A = np.array([[2., -2., 3.],
              [1., 1., 1.],
              [1., 3., -1]])
Q, R = caculate_QR_decompose(A)