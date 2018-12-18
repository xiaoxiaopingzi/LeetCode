# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: Main.py 
@time: 2018-09-05 15:51
"""
import math

x, y = map(int, input().split())
n = int(math.floor(math.sqrt(2 * (x + y))))
if n * (n + 1) != 2 * (x + y):
    print(-1)
else:
    # print(n)

    # if x > n:
    #     print(2)
    # else:
    #     print(1)

    count = 0
    for i in range(1, n + 1)[::-1]:
        if i <= x:
            x = x - n
            count += 1
            n -= 1
            if x == 0:
                break

    print(count)
