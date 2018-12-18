# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: Main3.py 
@time: 2018-09-16 18:43  
"""


def ndays(year, month, day):
    msp = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    msr = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        ms = msr
    else:
        ms = msp
    d = 0
    for i in range(month - 1):
        d += ms[i]
    d += day
    return d


yearInput = int(input())
mouthInput = int(input())
dayInput = int(input())

print(ndays(yearInput, mouthInput, dayInput))
