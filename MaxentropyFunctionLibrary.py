#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/6/6 23:50
#@Author: 黄怀宇
#@File  : MaxentropyFunctionLibrary.py
from numpy import *
import numpy as np


def rdual(hvector, vlagrange, matrix):       # 列向量
    return maxentropygt1(hvector) + np.dot(matrix.T, vlagrange)


def rpri(hvector, matrix, matrixb):
    return np.dot(matrix, hvector) - matrixb


def r(hvector, vlagrange, matrix, matrixb):
    return np.hstack((rdual(hvector, vlagrange, matrix), rpri(hvector, matrix, matrixb)))


def rinfeasiable(hvector, matrix, matrixb):
    return np.hstack((maxentropygt1(hvector), rpri(hvector, matrix, matrixb)))


def Dr(hvector, matrix):
    return np.vstack((np.hstack((maxentropygt2(hvector), matrix.T)), np.hstack((matrix, np.zeros((len(matrix), len(matrix)))))))


def dy(hvector, vlagrange, matrix, matrixb):
    return np.dot(-np.linalg.inv(Dr(hvector, matrix)), r(hvector, vlagrange, matrix, matrixb))


def dyinfeasiable(hvector, matrix, matrixb):
    return np.dot(-np.linalg.inv(Dr(hvector, matrix)), rinfeasiable(hvector, matrix, matrixb))


def getdx(hvector, vlagrange, matrix, matrixb):
    dx, dv = np.hsplit(dy(hvector, vlagrange, matrix, matrixb), [len(hvector)])
    return dx


def getdv(hvector, vlagrange, matrix, matrixb):
    dx, dv = np.hsplit(dy(hvector, vlagrange, matrix, matrixb), [len(hvector)])
    return dv


def getd(hvector, matrix, matrixb):
    d, w = np.hsplit(dyinfeasiable(hvector, matrix, matrixb), [len(hvector)])
    return d


def getw(hvector, matrix, matrixb):
    d, w = np.hsplit(dyinfeasiable(hvector, matrix, matrixb), [len(hvector)])
    return w


def maxentropy(vector: double):
    i: int = 0
    total: double = 0
    while i < len(vector):
        total = total + vector[i]*np.log10(vector[i])
        i = i + 1
    return total


def maxentropygt1(vector: double):
    i: int = 0
    grad = np.zeros(len(vector))
    while i < len(vector):
        # print('total', total)
        grad[i] = 1.0 / np.log(10) + np.log10(vector[i])
        i = i + 1
    return grad


def maxentropygt2(vector: double):
    i: int = 0
    hes = np.zeros((len(vector), len(vector)))
    while i < len(vector):
        hes[i, i] = 1.0 / (vector[i] * np.log(10))
        i = i + 1
    return hes


def generateA(h: int, w: int):
    r: int = -1
    while h != r:
        a = np.random.random((h, w))
        r = linalg.matrix_rank(a)
    return a
