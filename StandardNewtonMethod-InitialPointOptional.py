#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/6/5 3:14
#@Author: 黄怀宇
#@File  : StandardNewtonMethod-InitialPointOptional.py
from numpy import *
from cvxpy import *
import numpy as np
from math import log
# rank n input access add
rank: int = 1                               # 30
n: int = 2                                  # 100
if rank > n:
    exit()
x: double = (np.random.random(n))*2         # 0 < x < 2
R: int = -1                                 # make sure first circle run
while rank != R:
    A1 = np.random.random((len(x), rank))
    A2 = np.random.random((rank, len(x)))
    A = np.dot(A1, A2)
    R = linalg.matrix_rank(A)
print('subject to Ax = b')
print('the vector x is: \n', x)
print('the random matrix is: \n', A)
print('b = Ax : b = \n', np.dot(A, x))
print('the rank of random matrix A is', R)


def maxentropy(vector: double):
    i: int = 0
    total: double = 0
    while i < len(vector):
        print('IIII', i)
        print('total************', total)
        total = total + vector[i]*log(vector[i], 10)
        i = i + 1
    return total


def maxentropygt1(vector: double):
    i: int = 0
    total: double = 0
    while i < len(vector):
        print('total', total)
        total = total + 1.0 / log(10) + log(vector[i], 10)
        i = i + 1
    return total


def maxentropygt2(vector: double):
    i: int = 0
    total: double = 0
    while i < len(vector):
        total = total + 1.0 / (vector[i] * log(10))
        i = i + 1
    return total


k: int = 0
# print('^^^^^', maxentropygt2(x))
dnt = np.multiply((-1.0 / maxentropygt2(x)), maxentropygt1(x))
subnewton = maxentropygt2(x) * (np.dot(dnt, dnt.T))

while subnewton / 2 > 0.00000000000000000000000001:
    dnt: double = np.multiply((-1.0 / maxentropygt2(x)), maxentropygt1(x))
    subnewton = maxentropygt2(x) * (np.dot(dnt, dnt.T))
    t = 1
    aerf = 0.4
    beita = 0.9
    # print('9999999999', maxentropy(x))
    print('The value of X is:', x)
    # print('8888888888888', x + np.multiply(t, dnt))
    while maxentropy(x + np.multiply(t, dnt)) > maxentropy(x) - aerf * t * subnewton:
        t = beita * t
    x = x + np.multiply(t, dnt)
    k = k+1

