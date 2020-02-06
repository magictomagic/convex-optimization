#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/6/8 19:35
#@Author: 黄怀宇
#@File  : compareAndReconstruct.py
from numpy import *
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

# feasible
kfeasible: int = 0
subnewton: double = 10
flag = 1
while subnewton / 2 > 0.00000000000001:
    dx, w = np.hsplit(np.dot(np.linalg.inv(np.vstack((np.hstack((mf.maxentropygt2(x), A.T)), np.hstack((A, np.zeros((hrank, hrank))))))), np.hstack((-mf.maxentropygt1(x), np.zeros(hrank)))), [n])
    subnewton = np.dot(np.dot(dx.T, mf.maxentropygt2(x)), dx)
    # print('牛顿减少量', subnewton)
    t = 1
    aerf = 0.4
    beita = 0.9
    while mf.maxentropy(x + np.multiply(t, dx)) > mf.maxentropy(x) - aerf * t * subnewton:
        t = beita * t
    x = x + np.multiply(t, dx)
    kfeasible = kfeasible+1
print('the circle of k: feasible', kfeasible)
print('the feasible eventual value ', x)

# appoint x as 1
x = np.ones(n)
# infeasible
kinfeasible = 0
v = np.zeros(hrank)
while ((np.dot(A, x) != b).all()) | (np.linalg.norm(mf.r(x, v, A, b)) > 0.00000001):
    # print(np.linalg.norm(mf.r(x, v, A, b)))
    dx = mf.getdx(x, v, A, b)
    dv = mf.getdv(x, v, A, b)
    aerf = 0.4
    beita = 0.9
    t = 1
    while np.linalg.norm(mf.r(x + np.multiply(t, dx), v + np.multiply(t, dv), A, b)) > (1 - aerf * t) * np.linalg.norm(mf.r(x, v, A, b)):
        t = beita * t
    x = x + np.multiply(t, dx)
    v = v + np.multiply(t, dv)
    kinfeasible = kinfeasible + 1
print('the circle of k: infeasible', kinfeasible)
print('the infeasible eventual value ', x)
print('v', v)
print('w', w)
