# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: Main1.py 
@time: 2018-09-18 19:02  
"""

s = input()
resStr = []
preIndex = 0
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        count = i - preIndex
        if count != 0:
            resStr.append(count)
        resStr.append(s[i])
        preIndex = i + 1
    # print(resStr)
count = len(s) - preIndex - 1
if count != 0:
    resStr.append(count)
resStr.append(s[-1])
print(''.join(map(str, resStr)))
