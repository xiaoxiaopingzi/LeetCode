# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: Main8.py 
@time: 2018-09-26 18:45  
"""
import math

n = int(input())
realsAndPred = {}

countOfOne = 0
for i in range(n):
    real, pred = map(float, input().split())
    if real == 1.0:
        countOfOne += 1
    realsAndPred[real] = pred

recallValue = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
realsAndPred = sorted(realsAndPred, key=lambda x: x[1], reverse=True)

for i in recallValue:
    temp = int(countOfOne * i)
    # print(temp)
    tempList = realsAndPred[:temp + 1]
    count = 0
    for key, value in tempList:
        if key == 1.0:
            count += 1
    # print(count)
    print(round(count / temp) * 100)
