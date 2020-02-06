#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/6/4 4:32
#@Author: 黄怀宇
#@File  : theMatrix.py
import matplotlib.pyplot as plt
from cvxpy import *

a1 = Variable()
a2 = Variable()

obj = Minimize(exp(a1+3*a2 - 0.1) + exp(a1-3*a2-0.1)+exp(-a1-0.1))
prob = Problem(obj)
prob.solve()
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal var", a1.value, a2.value)





