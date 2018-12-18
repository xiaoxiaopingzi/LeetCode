# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: Main9.py 
@time: 2018-09-15 11:23  
"""
from collections import Counter

n = int(input())
arrs = []
for i in range(n):
    arrs.append(int(input()))

t = Counter(arrs).most_common(2)
sum1 = 0
for i in t:
    sum1 += i[0]
print(sum1)
# temp = {}
# for i in arrs:
#     if i not in temp.keys():
#         temp[i] = 1
#     else:
#         temp[i] = temp[i] + 1
# temp = sorted(temp.items(), key=lambda x: x[1], reverse=True)
# print(temp)

# res = []
# for i in temp:
#     res.append(i[1])

# sum1 = temp[0][1]
#
# for i in range(1, len(temp)):
#     if temp[i][1] != temp[0][1]:
#         sum1 += temp[i][1]
#         break
# print(sum1)
