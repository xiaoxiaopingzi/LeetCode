# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: Main2.py 
@time: 2018-09-27 18:57  
"""

inputStr = input()
n = int(input())

if n <= 0:
    print(-1)
else:
    if len(inputStr) < n:
        print(-1)
    else:
        resList = set()

        for i in range(len(inputStr) - n + 1):
            resList.add(inputStr[i: i + n])

        resList = sorted(resList)

        print(' '.join(resList))
