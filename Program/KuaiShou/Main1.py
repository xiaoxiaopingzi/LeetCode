# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: Main1.py 
@time: 2018-09-25 18:35  
"""
import math

n, p, h, w = map(int, input().split())
num_DuanLuo = list(map(int, input().split()))


flag = True
for s in range(1, min(h, w) + 1):
    temp1 = w // s
    temp2 = h // s
    totalHangShu = 0
    for i in num_DuanLuo:
        totalHangShu += math.ceil(i / temp1)
    if totalHangShu > p * temp2:
        print(s - 1)
        flag = False
        break

if flag:
    print(min(h, w))
