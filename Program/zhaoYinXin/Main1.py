# -*- coding: UTF-8 -*-
"""
@author: WanZhiWen 
@file: Main1.py 
@time: 2018-09-16 18:43  
"""


def factor(num):
    if num == 1:
        return []
    else:
        for i in range(2, num + 1):
            n, d = divmod(num, i)
            if d == 0:
                return [i] + factor(n)


n = int(input())
print('*'.join(map(str, factor(n))))
