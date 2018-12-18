# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: Main1.py 
@time: 2018-09-27 18:56  
"""
arrs1 = list(map(int, input().split()))
arrs2 = list(map(int, input().split()))

arrs = []
for i in arrs1:
    arrs.append(i)
for i in arrs2:
    arrs.append(i)

arrs = sorted(arrs)
print(' '.join(map(str, arrs)))
