#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/6/4 5:49
#@Author: 黄怀宇
#@File  : BacktrackingLinearSearch.py
import matplotlib.pyplot as plt
# from cvxpy import *
import numpy
import pylab
# a1 = Variable()
# a2 = Variable()
# obj = Minimize(exp(a1+3*a2 - 0.1) + exp(a1-3*a2-0.1) + exp(-a1-0.1))
# prob = Problem(obj)
# prob.solve()
from numpy import *


def target(x1: double, x2: double):
    f: double = exp(x1+3*x2 - 0.1) + exp(x1-3*x2-0.1)+exp(-x1-0.1)
    return f


def targetgt(x1: double, x2: double):
    gtf11: double = exp(x1+3*x2 - 0.1) + exp(x1-3*x2-0.1)-exp(-x1-0.1)
    gtf12: double = 3*exp(x1+3*x2 - 0.1) - 3*exp(x1-3*x2-0.1)
    return gtf11, gtf12


x1 = 1
x2 = 1
k = 0           # Statistical cycle-index
while numpy.abs(numpy.linalg.norm([targetgt(x1, x2)])) > 0.00000000000000000000000001:
    d: double = numpy.zeros((1, 2))
    d = d - targetgt(x1, x2)
    t = 1
    x = 0.4
    b = 0.9
    # plt.plot(target(x1, x2) - prob.value, k, 'ro')
    pylab.semilogx(numpy.abs(numpy.linalg.norm([targetgt(x1, x2)])), k, 'ro')
    pylab.pause(0.05)
    while target(x1 + t*d[0, 0], x2 + t*d[0, 1]) > target(x1, x2) + x*t*(targetgt(x1, x2)*mat(d).T)[0, 0]:
        t = 0.9*t
    x1 = x1 + t*d[0, 0]
    x2 = x2 + t*d[0, 1]
    k = k + 1
    print(k)
    print(x1, x2)
