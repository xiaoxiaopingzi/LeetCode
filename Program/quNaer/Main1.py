# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: Main1.py 
@time: 2018-09-27 9:15  
"""

arrs = list(map(int, input().split()))
# arrs = sorted(arrs)
# print(arrs[len(arrs) // 2])
result = arrs[0]
times = 1
for i in range(1, len(arrs)):
    if times == 0:
        result = arrs[i]
        times = 1
    elif arrs[i] == result:
        times += 1
    else:
        times -= 1

print(result)
