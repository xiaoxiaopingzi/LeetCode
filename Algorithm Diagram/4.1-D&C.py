# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: 4.1-D&C.py 
@time: 2018-11-10 10:40

分而治之
"""

arrs = [1, 2, 3, 4, 5, 6, 7, 88, 9]


def getSum(arrs):
    if len(arrs) == 1:
        return arrs[0]
    else:
        return arrs[0] + getSum(arrs[1:])


print('sum = ', getSum(arrs))
print('sum = ', sum(arrs))


def getLength(arrs):
    if len(arrs) == 1:
        return 1
    else:
        return 1 + getLength(arrs[1:])


print('length = ', getLength(arrs))
print('length = ', len(arrs))


def getMaxValue(arrs):
    if len(arrs) == 1:
        return arrs[0]
    else:
        return max(arrs[0], getMaxValue(arrs[1:]))


print('maxValue = ', getMaxValue(arrs))
print('maxValue = ', max(arrs))
