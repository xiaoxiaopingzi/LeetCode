# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: Main.py 
@time: 2018-09-05 15:51
"""
# from functools import reduce
#
# n, k = map(int, input().split())
# list = [i for i in range(1, n + 1)]
#
#
# def getYiHuo(i, j):
#     return i ^ j
#
# # for i in range(k-1):
# #     for
#
#
# yiHuoValue = reduce(getYiHuo, list)
# # print(yiHuoValue)
# print(7)
import re
# s = str(input())
inputStr = re.findall('[0-9a-zA-Z]+', input(), flags=0)
print(inputStr)
# inputStr = s.findall()
# inputStr = list(input().split('[^0-9a-zA-Z]'))
print(inputStr)
result = []
for index, str in enumerate(inputStr):
    str = str.lower()
    if index != 0:
        str = str[0].upper() + str[1:]

    result.append(str)

print(''.join(result))