# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: Main0.py 
@time: 2018-09-26 19:35  
"""
import math

N = int(input())

one_pred = []
zero_pred = []
for i in range(N):
    label, pred = map(float, input().split())
    if label == 1:
        one_pred.append([label, pred])
    else:
        zero_pred.append([label, pred])

one_pred = sorted(one_pred, key=lambda x: x[1], reverse=True)

tps = []
recallValue = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
for i in recallValue:
    tps.append(math.ceil(i * len(one_pred)))

Ps = []
for tp in tps:
    thresh = one_pred[tp - 1][1]
    count = 0
    for zero, score in zero_pred:
        if score >= thresh:
            count += 1
    print(round(tp / (tp + count) * 100))
