# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: Main1.py 
@time: 2018-09-18 19:02  
"""

N = int(input())
prices = sorted(list(map(int, input().split())))
M = int(input())

# def getValue(prices, M):
#     temp = {}
#     for index, i in enumerate(prices):
#         if i in temp:
#             return [temp[i], 1]
#         else:
#             temp[getattr()]
index1 = 0
index2 = len(prices) - 1

while index1 < index2:
    temp = prices[index1:index2 + 1]
    tempSum = sum(temp)
    if tempSum < M:
        print(0)
        break
    elif tempSum == M:
        print(1)
        break
    else:
        index2 -= 1
