# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: Main2.py 
@time: 2018-09-27 9:31  
"""
import math

k = int(input())
sum = 0

for i in range(50):
    if math.factorial(i) <= 1e7:
        sum = sum + 1.0 / math.factorial(i)

# print("%.{}f".format(k) % sum)
print(round(sum, k))
# print(math.e)
