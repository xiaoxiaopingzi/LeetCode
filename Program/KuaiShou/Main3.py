# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: Main3.py 
@time: 2018-09-25 18:35  
"""
m = int(input())
resList = []
for i in range(m):
    temp = input()
    s = temp[-6:]
    temp_int = int(s)
    resList.append(temp_int)

resList = sorted(resList)
for i in resList:
    print(i)