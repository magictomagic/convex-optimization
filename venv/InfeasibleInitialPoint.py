#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/6/6 8:52
#@Author: 黄怀宇
#@File  : InfeasibleInitialPoint.py
from numpy import *
import pylab
import numpy as np
import MaxentropyFunctionLibrary as mf

# set input
hrank: int = 30                               # 30
n: int = 100                                  # 100

# s.t. Ax = b
# set A, b, ^x^
if hrank > n:
    print('hrank should < n\n')
    exit()
x: double = (np.random.rand(n))*2         # 0 < x < 2
A = mf.generateA(hrank, len(x))
b = np.dot(A, x)
# appoint x as 1, release below, appoint x as ^x^, delete below
# x = np.ones(n)

k = 0
v = np.zeros(hrank)
print(1 < 2)
while ((np.dot(A, x) != b).all()) | (np.linalg.norm(mf.r(x, v, A, b)) > 0.000000000000000001):
    print(np.linalg.norm(mf.r(x, v, A, b)))
    dx = mf.getdx(x, v, A, b)
    dv = mf.getdv(x, v, A, b)
    aerf = 0.4
    beita = 0.9
    t = 1
    pylab.semilogx(np.linalg.norm(mf.r(x, v, A, b)), k, 'ro')
    pylab.pause(0.05)
    while np.linalg.norm(mf.r(x + np.multiply(t, dx), v + np.multiply(t, dv), A, b)) > (1 - aerf * t) * np.linalg.norm(mf.r(x, v, A, b)):
        t = beita * t
    x = x + np.multiply(t, dx)
    v = v + np.multiply(t, dv)
    k = k + 1
