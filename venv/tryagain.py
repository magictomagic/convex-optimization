#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/6/5 3:14
#@Author: 黄怀宇
#@File  : StandardNewtonMethod-InitialPointOptional.py
from numpy import *
import pylab
import numpy as np

# rank n input access add
rank: int = 30                               # 30
n: int = 100                                  # 100
if rank > n:
    print('rank should < n\n')
    exit()
x: double = (np.random.rand(n))*2         # 0 < x < 2
R: int = -1                                 # make sure first circle run

# initialize A
while rank != R:
    A = np.random.random((rank, len(x)))
    R = linalg.matrix_rank(A)
print('subject to Ax = b')
print('the vector x is: \n', x)
print('the random matrix is: \n', A)
print('b = \n', np.dot(A, x))
print('the rank of random matrix A is', R)


def maxentropy(vector: double):
    i: int = 0
    total: double = 0
    while i < len(vector):
        total = total + vector[i]*np.log10(vector[i])
        i = i + 1
    return total


def maxentropygt1(vector: double):
    i: int = 0
    grad = np.zeros(n)
    while i < len(vector):
        # print('total', total)
        grad[i] = 1.0 / np.log(10) + np.log10(vector[i])
        i = i + 1
    return grad


def maxentropygt2(vector: double):
    i: int = 0
    hes = np.zeros((n, n))
    while i < len(vector):
        hes[i, i] = 1.0 / (vector[i] * np.log(10))
        i = i + 1
    return hes


k: int = 0
subnewton: double = 10
flag = 1
while subnewton / 2 > 0.00000000000000000000000000000000000000000000000000000000000000000000000000001:
    dx, w = np.hsplit(np.dot(np.linalg.inv(np.vstack((np.hstack((maxentropygt2(x), A.T)), np.hstack((A, np.zeros((rank, rank))))))), np.hstack((-maxentropygt1(x), np.zeros(rank)))), [n])
    subnewton = np.dot(np.dot(dx.T, maxentropygt2(x)), dx)
    print('牛顿减少量', subnewton)
    t = 1
    aerf = 0.4
    beita = 0.6
    print('the circle of k', k)
    pylab.semilogx(subnewton, k, 'ro')
    pylab.pause(0.05)
    while maxentropy(x + np.multiply(t, dx)) > maxentropy(x) - aerf * t * subnewton:
        t = beita * t
        print('in circle, the variety of t', t)
    x = x + np.multiply(t, dx)
    k = k+1
print(x)

