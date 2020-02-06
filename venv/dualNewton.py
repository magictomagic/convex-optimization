#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/6/8 20:10
#@Author: 黄怀宇
#@File  : dualNewton.py#!/usr/bin/env python
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
subnewton: double = 10
while subnewton / 2 > 0.000000000000000000000000000000000000000000000000000000000000000000001:
    d = mf.getd(x, A, b)
    w = mf.getw(x, A, b)
    subnewton = np.dot(np.dot(d.T, mf.maxentropygt2(x)), d)
    aerf = 0.4
    beita = 0.9
    t = 1
    pylab.semilogx(subnewton, k, 'ro')
    pylab.pause(0.05)
    while mf.maxentropy(x+np.multiply(t, d)) > mf.maxentropy(x) + aerf * t * np.dot(mf.maxentropygt1(x).T, d):
        t = beita * t
    x = x + np.multiply(t, d)
    k = k + 1
